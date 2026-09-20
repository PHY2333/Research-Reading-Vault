---
task_id: 20260920-binary-field-introduction
route: pro-write-review
status: PREPARE
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md

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
  branch: codex/20260920-binary-field-introduction
  base_commit: 069e43b77b5a9683b19b2855522864490ce52f83

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

用户要求真实 ChatGPT Pro 整篇重写《二元扩域》，重点改变引入方式：可以关联 S008，也可以由简单扩域例子走向多项式构造。当前指令与仓库活动流程授权在任务分支连续完成 R01、全新会话 R02、完整捕获、格式检查、应用、commit/push；主分支整合留给用户决定。

原话：“Notes/08-Binary Extension Field Non Clifford Module/二元扩域我感觉写的不好，引入方式我觉得很奇怪，能不能换种方式，比如关联Papers/S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf来引入，或者也可以讲一些简单的扩域例子，然后推广到多项式，让pro重写一份”。

# 工作范围与保持范围

唯一正式输出为 `Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md`。允许整篇教学重组、例子、论证及必要论文连接，由 Pro 成文。现有知识归属、文件路径和已有有效数学覆盖面保持；不新建前置正式笔记，不变更 canonical 与读者索引，不管理 Papers/Translations。

任务材料、机械来源摘取与执行报告保存在本任务目录。用户已有 `Papers/SOURCES.md` 修改与 S011 主文/补充、S012 三份未跟踪 PDF 保留，不纳入提交。

# 路线、Git 与执行依据

Framework: Notes Pro-First 1.2。路线 pro-write-review，TASK independent 对应作者 fresh、审查 independent。remote 实际配置为 main，指向 https://github.com/PHY2333/Research-Reading-Vault；远端主分支为 main/main。

每轮使用成功推送的固定 checkpoint 与其中 Notes/PRO_OUTPUT_PROTOCOL.md，binding_id 只写在请求文件，不提供给 Browser 提示。来源摘取是从现有文件机械取得的任务材料，不是新写的数学正文。

# 当前阶段

PREPARE（R01 第二次作者尝试）。首次请求 checkpoint `9e68c6925c2e1c6491d86fac68bd9862062837be` 已推送；材料预检发现 PDF 机械摘取包含 NUL/C0 控制字符，已在 Pro 读取阶段中止，未应用正式文件。具体保留记录见 FAILURES/R01-attempt1-interrupted.md。已修正传输格式、更新 binding，准备推送新 checkpoint 并用全新 Pro 会话执行第二次作者尝试。
