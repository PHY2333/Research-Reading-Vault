---
task_id: <task-id>
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: <random-hidden-id>
target_files:
  - <path>
---

# 用户目标

<用当前读者最终能够完成的解释、判断、计算或构造描述目标。>

# 读者起点与真实反馈

## 可以直接使用的知识

<列出本次明确允许依赖的知识，以及已经建立的记号或结论。>

## 当前需要理解的连接

<保留相关用户原话，并说明困惑出现在哪个对象、步骤或章节衔接处。>

## 正文需要建立的内容

<说明从读者起点到目标之间需要补足的对象、关系、条件或推导。按问题组织，具体教学结构由 Pro 设计。>

# 必须读取

以下材料读取 Browser 提示绑定的同一 checkpoint；另行指定版本的来源写明版本和定位。

- 同任务 `TASK.md`。
- `Notes/AGENTS.md`。
- `Notes/WRITING_GUIDE.md`。
- `Notes/OBSIDIAN_MATH.md`。
- `Notes/PRO_OUTPUT_PROTOCOL.md`。
- <已存在目标文件的全文；新建目标在此说明其新建状态。>
- <必要上游或下游笔记及具体章节。>
- <必要来源、版本、页码、公式或段落。>
- <涉及归属或接口时需要核对的 canonical 条目与索引范围。>

# 事实支持与适用范围

## 已核验、可以采用的内容

<说明来源支持的事实、条件、推导和使用位置。>

## 本次需要核验的内容

<列明需要实际取得的证据或需要完成的推导；确认无此项时写“无”。>

## 一般结论与特定情形

<明确一般结论的条件，以及论文实例、硬件、参数或实验结论的来源范围。>

# 输出与保持范围

## 本次交付

`target_files` 是本轮 Pro 输出的唯一 allowlist。请返回其中要求交付的全部完整文件。

<说明各目标的职责和本次需要形成的内容。>

## 保持原状

<列明有效旧内容、无关章节、公式、文件边界、canonical ownership、索引、来源登记及用户已有修改的保持范围。>

## 需要决定的边界

正式文件的删除、移动、拆分、合并或重命名，以及超出当前 allowlist 或授权范围的必要变更，通过 `DECISION_REQUIRED` 说明具体方案和所需决定。来源与数学歧义按适用协议处理。

# 写作执行

按 `Notes/WRITING_GUIDE.md` 的统一标准成文。由 Pro 在内部决定教学顺序，使当前对象、关系、推理和用途连续衔接；反馈通过相关段落及必要过渡整合。

输出前连续复读完整稿，确认原有有效数学信息、条件和来源支持得到保留，目标读者能够继续下一步。格式执行 `Notes/OBSIDIAN_MATH.md`。

本次产物是完整可替换文件；独立分析、设计或审查文件仅在上方目标路径明确授权时交付。

# 完成标准

- <与用户目标直接对应的一项可观察结果。>
- <本任务关键推理或章节衔接应达到的结果。>
- <需要保持的条件、来源范围或有效内容。>

# 执行依据与交付

本轮材料固定在 Browser 提供的 checkpoint。

外层协议：<默认使用该 checkpoint 的 Notes/PRO_OUTPUT_PROTOCOL.md；涉及协议改写时，填写另行锁定的已存在提交及同一路径。>

按适用协议绑定并完成本轮响应。文本交付由 Pro 承担；本地应用与 Git 写入由 Codex 执行。

本模板默认配套 TASK 的 `route: pro-write-review`、`review_policy: independent`。其它路线按 `Notes/PRO_WORKFLOW.md` 的对应关系填写；`request_type` 根据任务选择 `create`、`rewrite` 或 `local-rewrite`。
