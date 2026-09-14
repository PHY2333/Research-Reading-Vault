---
task_id: 20260914-state-injection-xor
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
  branch: codex/state-injection-xor-20260914
  base_commit: e834ba8af1abba11652d55914cbe8cb16b468ac7
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

# 用户目标与真实反馈

用户在连续阅读 State injection 时先质疑 CNOT 的控制方向，再指出传态等式“像是突然得到答案”。Codex 已按用户明确授权补过两处注释。随后用户认可二进制指标、异或换元与测量分支算符的解释，最新要求：“让pro按照这种异或的方式重写这篇文章，这样可以避开后续的各种展开”。本次由 Pro 重写整篇，再由全新 Pro 会话独立审查。

# 归属、范围与授权

State injection 已是该构造的 canonical owner。仅替换同一路径的完整正文，保留一般 U、原位 gadget、T injection、错误传播、inner/outer 接口及术语边界。可重组章节、删除被替代的逐分量矩阵计算和补丁注释，不能删除、移动、重命名、拆分或合并正式文件。不新增前置笔记；不修改 Notes/00-index.md 或 CANONICAL_KNOWLEDGE.md，因现有路线与主结论仍适用。若 Pro 核验发现必须改变 canonical 主结论或所有权，返回 DECISION_REQUIRED。

在当前干净工作树上建立新任务分支，继承上一轮已推送的两处解释（不先合并 main）。按 Pro-First 1.1 连续执行 checkpoint、R01、格式规范化、应用推送、独立 R02、最终应用推送；不得由 Codex 代写或语义改写 Pro 正文，不自动合并 main。

# 来源与数学预检

主来源为 Papers/SOURCES.md 已登记的 S001，arXiv:2606.07734v1，阅读状态“已选读”。Codex 已核对本地 PDF 第 3–4 页文字与电路图：Sec. II.B 的两种 CNOT 表示、一般 U 原位线路、式 (2)–(3)，以及 Sec. III 开头的 inner/outer 分工。不改变文献文件、版本、登记、阅读状态或主辅关系；无翻译任务。临时来源页图只用于核验，不新增正式截图资产。

预检发现原文“已知测量位即可把未知资源 X 错误中的 Z 因子纳入 frame”的推论缺少条件；另外需要区分单分支相干错误、忽略记录后的通道与外层 syndrome 去相干，并收紧 CCZ、sqrt(T) 的外推。已将这些问题明确交由 Pro 对照来源核验，不把旧笔记当作不可更改的数学依据。

# 当前阶段

DONE。初始 checkpoint 为 7997e1b8d407138a3ca6073ed3b8d2566b7d89cf；R01 作者稿原样应用于 9eb4ba8e5b62ee9566f6f69906355850c4bb2304，均已推送任务分支。作者 6 Pro 会话：https://chatgpt.com/c/6aa7f2bb-368c-83e8-ad9b-298b519af082。

独立 6 Pro 在全新会话 https://chatgpt.com/c/6aa7fb66-9c48-83ee-a1fb-cad514ac985e 审查上述固定 R01 提交，返回 REVIEW_PASS。R02 的 task、request、隐藏 binding、repository、branch、commit 与 END_RESPONSE 全部通过 parser 验证；无需修订正文。最终 Obsidian 数学检查、链接核对与 git diff --check 通过，无未解决项。

任务目录保留五份最小记录；成功响应、staging 和临时来源页图在应用推送成功后清理。仅使用任务分支，不自动合并 main。最终正文及范围说明见 FINAL_REPORT.md。
