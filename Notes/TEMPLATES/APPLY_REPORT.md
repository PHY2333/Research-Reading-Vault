# Apply report

Framework: Notes Pro-First 1.2

按实际捕获、验证和应用结果填写。尚未完成的核验保留为空，并在 notes 中说明当前状态。多轮应用分别保留对应记录。

- task_id:
- request_id:
- checkpoint_commit:
- Pro status:
- binding_verified:
- applied_files:

## Integrity and scope

- response_complete:
- allowlist_verified:
- required_file_coverage:
- unchanged_scope_verified:
- raw_response_location:

## Format handling

- initial_Obsidian_math_check: pass | failed
- Codex_format_repair: not-needed | applied | blocked
- repair_class: none | markdown-obsidian | unambiguous-latex-syntax | mixed
- repair_summary:
- mathematical_statement_changed:
- prose_meaning_changed:
- final_Obsidian_math_check: pass | failed

`mathematical_statement_changed` 和 `prose_meaning_changed` 在完成修复前后核验后填写 `false`。发现需要改变数学内容或正文含义时，记录具体问题并进入内容核验流程。

## Application

- git_diff_check:
- application_commit:
- remote:
- push_result:
- review_required:
- notes:

## Retention and next step

- raw_response_retention:
- staging_retention:
- failure_record:
- current_stage:
- next_executor:
- next_action:

成功响应的清理以相应应用、检查、报告和推送完成为条件；失败响应及必要现场按 TASK 保留。
