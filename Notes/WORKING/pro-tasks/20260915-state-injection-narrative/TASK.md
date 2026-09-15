---
task_id: 20260915-state-injection-narrative
route: pro-write-review
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
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
  branch: codex/state-injection-narrative-20260915
  base_commit: 179f4fbfaccc6d05afeaf2353bad17b90bc1efe0
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

# 用户目标与授权

用户在完成前一轮异或重写、数次局部补充之后，仍问：“我不理解为什么要把 CNOT 改成数据比特的 X 基下的描述，这样问题不是复杂化了吗？”最新明确要求：“让 pro 理解这个问题，重新组织文章，这样很容易混乱”。本轮由真实 ChatGPT Pro 全文重组，再由全新 Pro 会话独立审查。不是 Codex 再补注释。

作者应重新判断概念、记号、表示和线路的引入顺序，保持此前用户认可的异或与分支计算方法；不预设现有章节是正确的教学顺序。详见 PRO_REQUEST.md 的真实反馈与验收标准。

# 当前工作树与快照

本次开始时目标文件包含用户未提交编辑：one-bit teleportation 等标题调整，按测量记录校正的措辞，§2.1 将旧 callout 整合为简短相位回踢说明，以及 §3.1 添加测量前求和行并删去重复概括。这些编辑属于全文重组基线，完整保存到初始 checkpoint，供 Pro 阅读；不先回退或恢复历史补丁。后续若用户继续修改目标，应用前须识别并保留新改动。

# 范围与知识归属

唯一正式输出路径是现有 State injection.md；不新建、移动、删除、拆分或合并正式笔记。既有 canonical ownership、主要构造及下游接口保留；无须新增前置笔记或更新 CANONICAL_KNOWLEDGE.md、Notes/00-index.md。允许在同一文件内重排、合并段落和调整主线/补充层次。

# 来源准备

主来源仍为 S001（arXiv:2606.07734v1，已选读），其 Sec. II.B 第 3–4 页、式 (2)–(3) 及 Sec. III 开头已在本会话核验。

为回应 one-bit teleportation 的概念定位，新增已判重的辅助来源 S010：Zhou、Leung、Chuang，arXiv:quant-ph/0002039v2（2000-08-01），本地 17 页 PDF。Codex 已读引言和 Sec. II，并实际查看第 3 页式 (7) 线路；阅读状态仅记已选读。SOURCES.md 登记新来源；RELATIONS.md 记录 S010 对 S001 的上述辅助范围。无翻译或主文献笔记，S001 原登记不变。临时渲染图片成功后删除，不新增正式截图资产。

# 当前阶段

DONE。真实 6 Pro 作者全文重组已在 4cdbff321a2dfdab7f864ba03f42ee14a498403d 应用推送；全新真实 6 Pro 独立审查返回 REVIEW_PASS，绑定该固定提交。最终 Obsidian 数学检查通过，正文与作者应用版本逐字节一致。保留任务目录和 Git 审计，成功临时产物清理；不合并 main。
