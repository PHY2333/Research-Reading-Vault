---
task_id: 20260905-binary-extension-field-rewrite
request_id: R02
request_type: fresh-whole-file-review
binding_id: d7d59412e7a14d2c81b7cdd7a742a186
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md
---

# 审查目标

在全新 ChatGPT Pro 会话中，从头连续审查固定 commit 的完整新版。用户实际反馈是“内容像百科，主线不够明确”。首要验收对象是新的讲解过程；旧任务的 REVIEW_PASS 和本轮作者自评都不是通过依据。

# 必须读取

- 本任务 PRO_REQUEST.md 与 TASK.md。
- Notes/WRITING_GUIDE.md、Notes/OBSIDIAN_MATH.md、Notes/PRO_OUTPUT_PROTOCOL.md。
- Browser 所绑定最新 commit 的完整 Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md。
- CANONICAL_KNOWLEDGE.md 的二元扩域及相邻职责条目，Notes/00-index.md 的相关路线。
- Notes/01-量子纠错基础/二进制空间性质.md 与 Notes/07-Lifted-Product Code/Lifted product code.md，核对范围边界。

# 审查重点

本任务 PRO_REQUEST.md 的读者起点、能力目标、数学条件、覆盖面和 allowlist 全部生效。独立判断：读者能否持续知道当前解决什么问题、为什么下一结构现在出现、当前所得怎样用于下一步；是否只把百科式性质清单改成问题标题或增加装饰性过渡；是否仍有与后文无关的长证明、突然提升前置知识、最后用一大段重复摘要代替真正连接。

审查商构造／低次代表元／运算／逆元的闭合性，抽象域与表示依赖，Frobenius 和子域条件，绝对迹与范数，迹配对非退化和对偶基坐标公式，乘法矩阵／换基／结构常数，线性与双线性及可逆性条件。不能为压缩篇幅丢失必要理由或 canonical 已承诺的内容；纯数学正确但教学反馈尚未解决也不能通过。

具体 qudit／门／码／蒸馏内容不得抢占本篇，非 Clifford 与 LP 接口必须守住请求中的限定。符号、链接及中文一致，正文无任务维护语言。孤立的格式问题由 Codex 按 OBSIDIAN_MATH.md 修复，不单独要求重发全文。

# 输出

只有完整新版确实满足教学、数学和边界要求时，按协议返回 REVIEW_PASS。存在实质缺陷时，返回 COMPLETE 和完整修正文件，不只列建议。路径只允许现有二元扩域.md，mode: replace。若需改变文件结构、知识归属或处理来源冲突，按协议返回相应状态。不操作 GitHub。
