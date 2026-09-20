---
task_id: <YYYYMMDD-short-name>
route: pro-write-review
status: PREPARE
target_files:
  - <path>

integrity: fast
review_policy: independent
audit_retention: errors-only

format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true

git:
  remote: <configured-remote>
  branch: codex/<task-id>
  base_commit: <commit-before-task>

automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 1
  preauthorized_browser_rounds:
    - R01
    - R02
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - ambiguous_format_or_latex_repair
    - math_content_uncertain
    - format_check_failed_after_codex_repair
    - push_failure
    - merge_to_main
---

# 用户目标

<记录本次任务要形成的理解、内容或交付结果。>

# 当前真实问题

<记录用户实际反馈及其出现位置，提供足以准备请求的上下文。>

# 本次授权

<明确目标文件、任务材料、报告和必要执行操作。需要工具适配时，单独说明已获授权的范围。>

本模板表示已授权任务分支内的连续执行。使用时依据用户实际授权填写自动化字段，并在已有轮次、次数和 `stop_only_on` 边界内运行。

# 保持范围

<列明无关正文、文件结构、canonical ownership、索引、来源登记和用户已有修改的保持范围。>

# 路线与审查安排

默认采用 `pro-write-review`，TASK 的 `review_policy: independent` 对应作者请求的 `review_policy: fresh` 与审查请求的 `review_mode: independent`。

其它路线按 `Notes/PRO_WORKFLOW.md` 选择 `none` 或 `internal` 并同步请求。历史字段按原任务解释，迁移方式记录在工作流中。

# Git 与执行依据

Framework: Notes Pro-First 1.2

`git.remote` 从仓库实际 remote 配置及目标分支关系确认；默认任务分支前缀为 `codex/`。`git.base_commit` 记录任务开始前的实际提交。

外层协议：<普通任务使用本轮固定 checkpoint 的 Notes/PRO_OUTPUT_PROTOCOL.md；协议更新任务记录另行锁定的已存在提交和路径。>

每轮材料使用实际推送成功的 checkpoint。R01 与 R02 分别读取其绑定快照，Pro 的本轮输出按已固定协议解释。

# 当前阶段

PREPARE

<随后按实际执行更新阶段、已完成结果和下一步。>
