---
task_id: 20260914-state-injection-xor
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: 697ca32935814186a234d1ce265dbf0a
target_files:
  - Notes/04-Magic State Injection/State injection.md
---

# 审查对象与目标

以 Browser 指定最新 GitHub commit 的完整目标文件为准，在全新 Pro 会话中审查。实际读取本任务 PRO_REQUEST.md、TASK.md、Notes/WRITING_GUIDE.md、Notes/OBSIDIAN_MATH.md、Notes/PRO_OUTPUT_PROTOCOL.md，以及 PRO_REQUEST.md 列出的同版本必读来源和相关章节。不得依赖作者对话、自评或 Codex 摘要。

用户要用异或换元与测量分支算符重写整篇 State injection，避免后文逐分量展开。请从头连续判断主线和读者能力是否成立，而不是只搜索 XOR 记号。

# 特别审查

- 符号出现是否服务当下问题；首次换元是否一一对应、振幅不变；m 在求和与测量两个阶段是否区分；J 若采用是否只表示空间对应。
- 是否用已建立的方法贯穿一般 U、原位 gadget、T 与错误传播；是否仍有“化简得”式跳步，或把原矩阵展开换成同样难读的指标堆叠。
- R 的单态约束、R_U 的酉延拓非唯一性、K_m 与 C_U 次序及归一化是否真正建立；不能无条件把一般 U gadget 当 Clifford-only。
- T 的整数相位与 XOR 是否混淆；S 校正及分支整体相位是否正确。
- 资源 X 错误是否被误当成由 m 揭示的已知事件；条件相干态、边缘通道、syndrome 和 twirling 是否区分；inner 稳定子与 outer checks 是否混淆；CCZ、sqrt(T) 是否被过度推广。
- 文章是否保留现有 canonical 主题与下游接口，移除过时注释和重复推导，并自然说明实际读到的来源范围。

依据全文和来源独立核验 PRO_REQUEST.md 的全部完成条件。不要因为措辞偏好重写已准确清楚的段落；纯 Markdown、数学分隔符、callout 或可唯一判断的 LaTeX 语法问题由 Codex 规范化，不是重发整篇的理由。

# 输出

通过则按协议返回 REVIEW_PASS。存在实质问题则直接返回 COMPLETE 和完整修订文件，不仅列建议；唯一 allowlist 是 target_files。若必须改变正式文件结构或 canonical 主结论，返回 DECISION_REQUIRED；若必读来源缺失按协议返回并列出缺项。全程不修改 GitHub，不在 END_RESPONSE 后续写。
