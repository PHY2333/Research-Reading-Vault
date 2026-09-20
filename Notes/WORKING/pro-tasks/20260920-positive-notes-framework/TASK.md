---
task_id: 20260920-positive-notes-framework
route: pro-write-review
status: PREPARE
target_files:
  - AGENTS.md
  - Notes/AGENTS.md
  - Notes/WRITING_GUIDE.md
  - Notes/PRO_WORKFLOW.md
  - Notes/PRO_OUTPUT_PROTOCOL.md
  - Notes/OBSIDIAN_MATH.md
  - Notes/WORKING/README.md
  - Notes/TEMPLATES/APPLY_REPORT.md
  - Notes/TEMPLATES/BROWSER_AUTHOR_PROMPT.md
  - Notes/TEMPLATES/BROWSER_REVIEW_PROMPT.md
  - Notes/TEMPLATES/FINAL_REPORT.md
  - Notes/TEMPLATES/PRO_REQUEST.md
  - Notes/TEMPLATES/REVIEW_REQUEST.md
  - Notes/TEMPLATES/TASK.md
  - Notes/WORKING/pro-tasks/20260920-positive-notes-framework/FRAMEWORK_ANALYSIS.md

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
  remote: main
  branch: codex/positive-notes-framework-20260920
  base_commit: 32105e4418fd0d82114b36539a2ac06ff364d234

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

# 用户目标与本次授权

用户要求真实 ChatGPT Pro 分析当前 Notes 防御性行文的成因，给出正向规定的新框架文件和更新提示词，由 Codex 更新本地。执行 Pro 作者 R01、独立审查 R02，并按现有流程在任务分支 commit/push。

# 工作范围

更新现有框架与模板；Pro 的分析保存到本任务 FRAMEWORK_ANALYSIS.md。正式主题笔记作为只读语言样本，保持原内容。canonical ownership、索引与前置笔记结构保持。文献和翻译保持现状。

用户已有 Papers/SOURCES.md 改动与 S011/S012 三份未跟踪 PDF 独立保留，提交只包含本任务路径。

# 技术适配

框架文件自身含协议样例。Codex 可修复 parser 把文件 payload 内 PRO_STATUS 样例误认成外层状态的问题，保持实际协议、绑定和 allowlist 验证。

# 当前阶段

PREPARE。初始规则采用 Notes Pro-First 1.1；本轮运行协议和权限按初始 checkpoint 执行，新文本供后续任务采用。
