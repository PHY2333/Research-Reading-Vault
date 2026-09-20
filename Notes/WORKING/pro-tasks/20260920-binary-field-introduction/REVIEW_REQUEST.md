---
task_id: 20260920-binary-field-introduction
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: 37790b096004485283036de4e8385f93
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md
---

# 审查对象与原始目标

审查 Browser 绑定的固定 commit 中，本轮 `target_files` 列出的全部完整目标文件。原始目标、读者起点、事实支持和保持范围见同任务 `PRO_REQUEST.md`，执行安排见 `TASK.md`。

本轮在独立上下文中，从实际候选和来源建立判断。作者解释、自评或上一轮对话可帮助定位问题，审查结论以本轮读取的材料为依据。

# 必须读取

- 本任务 `TASK.md` 与 `PRO_REQUEST.md`。
- `Notes/WRITING_GUIDE.md`。
- `Notes/OBSIDIAN_MATH.md`。
- 适用版本的 `Notes/PRO_OUTPUT_PROTOCOL.md`。
- `target_files` 中的全部完整候选。
- 原始请求中支撑本次结论的必要来源与上下游材料。
- 无新增。原请求 SOURCE_EXCERPTS.md 包含 PDF 原始摘取及对应译本选段。

需要比较修改范围时，使用 TASK 指定的基线及对应旧文件。固定 commit、来源版本和实际读取范围分别核对。

# 连续审查

首先从头阅读候选，确认原始目标已经形成一条可跟随的知识过程：读者起点能够支撑开头，各节提供下一步需要的对象、关系和理由，结尾得到请求所需的能力。

随后使用 `Notes/WRITING_GUIDE.md` 检查定义、推理、解释深度、来源范围、例子、对比及反馈整合。以具体语义和阅读影响判断修订必要性。已清楚、准确、连续的有效内容保持原有表达。

本轮特别关注：

- 核对新稿是否从当前读者能理解的扩域例子或 S008 问题出发，具体操作能否推进到一般多项式构造；论文动机是否有实际解释和来源。
- 核对原请求所列 canonical 覆盖面和固定记号、迹对偶基与自对偶基条件、一般乘法矩阵与 S008 展开的坐标约定，以及非 Clifford 接口的准确范围。
- 全文改写限原有目标。旧稿用于覆盖范围核验，不要求保留旧顺序；重点检查用户对引入方式的反馈是否得到解决。

公共写作标准由统一指南承担；以上只补充当前任务的特有关注点。

# 修订与应用分工

需要实质修订时，重写受影响段落及必要衔接，并在完整文件中保留正确公式、来源支持和有效内容。使读者能够沿修订后的主线继续，而将维护记录留在任务材料中。

纯 Markdown、Obsidian 分隔符、换行、callout 引用及可唯一确定的 LaTeX 语法问题，由 Codex 在应用层规范化。出现数学含义多义、公式内容错误或来源冲突时，按内容问题核验。

本轮 `REVIEW_REQUEST.md` 的 `target_files` 是实际输出路径的唯一 allowlist；原始 `PRO_REQUEST.md` 提供内容、文件结构及保持范围的授权基线。每项修订同时满足这两层约束，执行安排沿用 `TASK.md`。

R02 缩小目标集合时，原始请求中其余文件仍可作为必要上下文读取，其内容保持本轮 checkpoint 的版本。路径列入本轮 allowlist 后，具体修改仍按原始内容与结构授权进行。

完成本轮目标确需调整路径范围、内容权限或正式文件结构时，使用 `DECISION_REQUIRED` 写明涉及路径、必要性和所需决定；取得授权并更新请求、形成新 checkpoint 后继续。

# 审查输出

本轮全部目标达到原始请求中对应的目标和保持要求，且正文无需实质修订时，使用：

```text
PRO_STATUS: REVIEW_PASS
```

纯格式事项交由 Codex 处理，审查可据实通过。

存在实质问题且可以同时在本轮路径范围与原始内容、结构授权内完成修订时，使用：

```text
PRO_STATUS: COMPLETE
```

返回本轮 allowlist 内全部受影响目标的完整修正版。其余本轮目标沿用审查 checkpoint。每个交付文件均为可直接替换的原始 Markdown。

材料不足、身份问题或需要决定时，按适用协议返回相应状态；消息写明实际缺项、冲突与下一步。

# 执行依据

材料提交：Browser 提示中的固定 commit。

外层协议：本轮 checkpoint 中的 Notes/PRO_OUTPUT_PROTOCOL.md（Notes Pro-First 1.2）。

完整响应包含适用协议要求的绑定区和结束标记。回复在 `END_RESPONSE` 处结束。

本模板用于 fresh review：TASK 使用 `review_policy: independent`，作者请求使用 `review_policy: fresh`。历史 `same-thread` 任务按原字段和冻结协议解释，兼容说明见 `Notes/PRO_WORKFLOW.md`。
