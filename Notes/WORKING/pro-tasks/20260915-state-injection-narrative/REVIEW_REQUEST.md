---
task_id: 20260915-state-injection-narrative
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: 32abbb24a1a94842955ad40ceda65585
target_files:
  - Notes/04-Magic State Injection/State injection.md
---

# 审查目标

在全新 Pro 会话中，审查 Browser 固定最新 commit 的完整 State injection.md。实际读取同任务 PRO_REQUEST.md、TASK.md、写作/Obsidian/输出协议及请求列出的相关来源和接口。不依赖作者对话、自评或上一版审查结论。

本次用户已因“为什么突然换数据 X 基，是否徒增复杂”明确认为整篇容易混乱。重点不是找一句用途说明，而是判断全文的实际引入顺序：目标与困难是否先出现，表示/符号/新线路是否随后解决当下问题，结果是否回到当前目标。

# 重点

- 基础 XOR 传态、门注入和原位输出的目标是否各自清楚并相互连接；辅助线输出与数据线输出是否不会混淆。
- 同一 CNOT 的等价改写、W_U 新算符、原位线路改变是否明确区分；X 基表示的收益是否在引入前成立，并有可追踪的 P± 代入合并等必要代数桥梁。
- s 相干输入标签与 m 测量记录是否区分；R 是否从失配需要引出；避免前面比较一次、后面又重复同一推理。
- 一般 U、具体 T、J、R 延拓非唯一性、Clifford 条件的主次顺序是否合理，既不压垮入门主线，也不省略关键证明。
- 是否真正解决用户连续反馈，而非保留旧结构并增加更多解释块；手工编辑的有效中间步是否被吸收，历史补丁是否没有机械恢复。
- PRO_REQUEST.md 的全部数学边界及后半部分错误/随机化/inner-outer/蒸馏接口是否仍准确可用。尤其不能因重组把未知 X 故障当已知 frame、把条件相干态与边缘通道混为一谈。
- 逐段检查引用、章节交叉引用与最终结构一致；必要来源确实读取。

只因个人措辞偏好不要重写已清楚准确的段落。纯 Markdown/LaTeX 语法问题由 Codex 规范化，不是整篇重发的理由。

# 输出

全文达到原始目标且无实质问题，返回 REVIEW_PASS。若需修订，直接返回 COMPLETE 和 allowlist 目标文件的完整修订版，不仅列建议。缺来源或真正结构/范围决定按协议处理。不修改 GitHub，不在 END_RESPONSE 后续写。
