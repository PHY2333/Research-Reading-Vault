---
task_id: <task-id>
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: <new-random-hidden-id>
target_files:
  - <path>
---

# 审查对象与原始目标

审查 Browser 绑定的固定 commit 中的全部目标文件。原始目标、读者起点、事实支持和保持范围见同任务 `PRO_REQUEST.md`，执行安排见 `TASK.md`。

本轮在独立上下文中，从实际候选和来源建立判断。作者解释、自评或上一轮对话可帮助定位问题，审查结论以本轮读取的材料为依据。

# 必须读取

- 本任务 `TASK.md` 与 `PRO_REQUEST.md`。
- `Notes/WRITING_GUIDE.md`。
- `Notes/OBSIDIAN_MATH.md`。
- 适用版本的 `Notes/PRO_OUTPUT_PROTOCOL.md`。
- `target_files` 中的全部完整候选。
- 原始请求中支撑本次结论的必要来源与上下游材料。
- <本轮新增的必要材料、版本与定位；无新增时写“无”。>

需要比较修改范围时，使用 TASK 指定的基线及对应旧文件。固定 commit、来源版本和实际读取范围分别核对。

# 连续审查

首先从头阅读候选，确认原始目标已经形成一条可跟随的知识过程：读者起点能够支撑开头，各节提供下一步需要的对象、关系和理由，结尾得到请求所需的能力。

随后使用 `Notes/WRITING_GUIDE.md` 检查定义、推理、解释深度、来源范围、例子、对比及反馈整合。以具体语义和阅读影响判断修订必要性。已清楚、准确、连续的有效内容保持原有表达。

本轮特别关注：

- <任务特有的关键推理、接口或真实反馈。>
- <必须保留的数学信息、条件与来源范围。>
- <需要比较核验的局部修改范围。>

公共写作标准由统一指南承担；以上只补充当前任务的特有关注点。

# 修订与应用分工

需要实质修订时，重写受影响段落及必要衔接，并在完整文件中保留正确公式、来源支持和有效内容。使读者能够沿修订后的主线继续，而将维护记录留在任务材料中。

纯 Markdown、Obsidian 分隔符、换行、callout 引用及可唯一确定的 LaTeX 语法问题，由 Codex 在应用层规范化。出现数学含义多义、公式内容错误或来源冲突时，按内容问题核验。

文件结构与 allowlist 边界沿用原始请求；需要超出授权范围的决定时，使用相应消息状态。

# 审查输出

全文达到原始目标，且正文无需实质修订时，使用：

```text
PRO_STATUS: REVIEW_PASS
```

纯格式事项交由 Codex 处理，审查可据实通过。

存在实质问题且可以在当前范围内完成修订时，使用：

```text
PRO_STATUS: COMPLETE
```

返回全部受影响目标的完整修正版。其余目标沿用本轮审查 checkpoint。每个交付文件均为可直接替换的原始 Markdown。

材料不足、身份问题或需要决定时，按适用协议返回相应状态；消息写明实际缺项、冲突与下一步。

# 执行依据

材料提交：Browser 提示中的固定 commit。

外层协议：<默认使用该 checkpoint 的 Notes/PRO_OUTPUT_PROTOCOL.md；协议更新任务填写初始冻结协议的提交及路径。>

完整响应包含适用协议要求的绑定区和结束标记。回复在 `END_RESPONSE` 处结束。

本模板用于 fresh review：TASK 使用 `review_policy: independent`，作者请求使用 `review_policy: fresh`。历史 `same-thread` 任务按原字段和冻结协议解释，兼容说明见 `Notes/PRO_WORKFLOW.md`。
