#!/usr/bin/env python3
"""Parse a Fast Notes Pro response into a staging directory.

The parser validates the hidden binding ID, Git checkpoint metadata, response
completeness, and an explicit path allowlist. It never overwrites repository
files directly and does not require request/response hashes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath


def parse_key_values(lines: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in lines:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Expected key: value, got {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def safe_path(raw: str) -> str:
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe path: {raw!r}")
    return path.as_posix()


def protocol_line_indices(lines: list[str], binding_id: str) -> list[int]:
    """Locate protocol lines outside the fenced contents of file blocks.

    Files may themselves document this protocol. Their examples remain opaque
    until the exact opening fence is closed; main() validates the file headers
    and block boundaries separately.
    """
    indices: list[int] = []
    in_file_header = False
    fence: str | None = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if fence is not None:
            if stripped == fence:
                fence = None
            continue
        indices.append(index)
        if stripped == f"BEGIN_FILE::{binding_id}":
            in_file_header = True
        elif in_file_header:
            match = re.fullmatch(r"(`{5,})(?:markdown)?", stripped)
            if match:
                fence = match.group(1)
                in_file_header = False
            elif stripped == f"END_FILE::{binding_id}":
                in_file_header = False
    return indices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--report")
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--binding-id", required=True)
    parser.add_argument("--allow-path", action="append", default=[])
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    allowed = {safe_path(item) for item in args.allow_path}
    binding_id = args.binding_id
    report: dict[str, object] = {
        "binding_verified": False,
        "status": None,
        "files": [],
        "message": None,
        "error": None,
    }

    try:
        nonempty = [line.strip() for line in lines if line.strip()]
        if not nonempty:
            raise ValueError("Empty response")
        if nonempty[0] == "BINDING_FAILED":
            report["status"] = "BINDING_FAILED"
            raise ValueError("Pro reported BINDING_FAILED")
        if nonempty[0] != "BINDING_OK":
            raise ValueError("Response must begin with BINDING_OK")

        start = next(i for i, line in enumerate(lines) if line.strip() == "BINDING_OK")
        end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == "END_BINDING")
        binding = parse_key_values(lines[start + 1:end])
        expected = {
            "task_id": args.task_id,
            "request_id": args.request_id,
            "binding_id": args.binding_id,
            "based_on_repository": args.repository,
            "based_on_branch": args.branch,
            "based_on_commit": args.commit,
        }
        mismatches = {
            key: {"expected": value, "actual": binding.get(key)}
            for key, value in expected.items()
            if binding.get(key) != value
        }
        if mismatches:
            raise ValueError(f"Binding mismatch: {json.dumps(mismatches, ensure_ascii=False)}")
        report["binding_verified"] = True

        protocol_indices = protocol_line_indices(lines, binding_id)
        status_lines = [i for i in protocol_indices if lines[i].strip().startswith("PRO_STATUS:")]
        if len(status_lines) != 1:
            raise ValueError(f"Expected exactly one PRO_STATUS, found {len(status_lines)}")
        status_index = status_lines[0]
        status = lines[status_index].split(":", 1)[1].strip()
        valid = {"COMPLETE", "REVIEW_PASS", "NEEDS_CONTEXT", "DECISION_REQUIRED", "BLOCKED"}
        if status not in valid:
            raise ValueError(f"Unsupported PRO_STATUS: {status}")
        report["status"] = status

        end_marker = f"END_RESPONSE::{binding_id}"
        end_indices = [i for i in protocol_indices if lines[i].strip() == end_marker]
        if len(end_indices) != 1:
            raise ValueError(f"Expected exactly one {end_marker}, found {len(end_indices)}")
        response_end = end_indices[0]
        if any(line.strip() for line in lines[response_end + 1:]):
            raise ValueError("Non-whitespace content found after END_RESPONSE")

        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if status == "COMPLETE":
            begin_marker = f"BEGIN_FILE::{binding_id}"
            end_file_marker = f"END_FILE::{binding_id}"
            index = status_index + 1
            extracted: list[str] = []
            while index < response_end:
                if not lines[index].strip():
                    index += 1
                    continue
                if lines[index].strip() != begin_marker:
                    raise ValueError(f"Unexpected content before file block at line {index + 1}")
                index += 1
                header: list[str] = []
                while index < response_end and not re.match(r"^`{5,}(?:markdown)?\s*$", lines[index].strip()):
                    header.append(lines[index])
                    index += 1
                if index >= response_end:
                    raise ValueError("Missing >=5-backtick markdown fence")
                meta = parse_key_values(header)
                path = safe_path(meta.get("path", ""))
                if meta.get("mode") != "replace":
                    raise ValueError("Only mode: replace is allowed")
                if path not in allowed:
                    raise ValueError(f"Path not in allowlist: {path}")
                fence_match = re.match(r"^(`{5,})", lines[index].strip())
                assert fence_match is not None
                fence = fence_match.group(1)
                index += 1
                content_lines: list[str] = []
                while index < response_end and lines[index].strip() != fence:
                    content_lines.append(lines[index])
                    index += 1
                if index >= response_end:
                    raise ValueError(f"Unclosed content fence for {path}")
                index += 1
                if index >= response_end or lines[index].strip() != end_file_marker:
                    raise ValueError(f"Missing {end_file_marker} after {path}")
                index += 1
                if path in extracted:
                    raise ValueError(f"Duplicate output path: {path}")
                content = "\n".join(content_lines) + ("\n" if content_lines else "")
                target = output_dir / Path(path)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8", newline="\n")
                extracted.append(path)
            if not extracted:
                raise ValueError("COMPLETE response contained no file blocks")
            report["files"] = extracted

        elif status == "REVIEW_PASS":
            forbidden = {f"BEGIN_FILE::{binding_id}", f"BEGIN_MESSAGE::{binding_id}"}
            if any(line.strip() in forbidden for line in lines[status_index + 1:response_end]):
                raise ValueError("REVIEW_PASS must not include file or message blocks")

        else:
            if any(lines[i].strip() == f"BEGIN_FILE::{binding_id}" for i in protocol_indices):
                raise ValueError(f"{status} must not include file blocks")
            begin_message = f"BEGIN_MESSAGE::{binding_id}"
            end_message = f"END_MESSAGE::{binding_id}"
            starts = [i for i in protocol_indices if lines[i].strip() == begin_message]
            if len(starts) != 1:
                raise ValueError(f"{status} requires one message block")
            message_start = starts[0]
            message_end = next(
                (i for i in protocol_indices
                 if message_start < i < response_end and lines[i].strip() == end_message),
                None,
            )
            if message_end is None:
                raise ValueError("Missing END_MESSAGE")
            report["message"] = "\n".join(lines[message_start + 1:message_end]).strip()

        if args.report:
            Path(args.report).parent.mkdir(parents=True, exist_ok=True)
            Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": status, "files": report["files"]}, ensure_ascii=False))
        return 0
    except Exception as exc:
        report["error"] = str(exc)
        if args.report:
            Path(args.report).parent.mkdir(parents=True, exist_ok=True)
            Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
