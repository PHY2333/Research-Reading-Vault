# Notes/PRO_OUTPUT_PROTOCOL.md

Framework: Notes Pro-First 1.2

本协议规定 ChatGPT Pro 文本交付的外层结构，供 Codex App Browser 捕获和解析。默认使用 Fast Integrity。字段名称、状态枚举与标记保持既有语法。

当前轮次使用请求指定的冻结协议。协议更新任务的文件 payload 可以包含新协议，外层响应继续遵守该任务已固定的版本。

## 1. 绑定

实际读取请求和适用协议，核对身份与快照信息后，回复从绑定区开始：

```text
BINDING_OK
task_id: <from request>
request_id: <from request>
binding_id: <from request; value is not present in Browser prompt>
based_on_repository: <from Browser prompt>
based_on_branch: <from Browser prompt>
based_on_commit: <from Browser prompt>
END_BINDING
```

`task_id`、`request_id` 和 `binding_id` 从实际请求取得。Browser 提供的 branch 用于标识任务分支，commit 固定本轮材料版本。请求另行指定协议提交时，`based_on_commit` 仍填写本轮材料 checkpoint。

请求或适用协议无法读取，或身份字段无法确定、相互不一致时，回复为：

```text
BINDING_FAILED
```

此状态独立结束。

1.2 中，绑定区确认请求身份和快照。身份已确定后，其它必读材料缺失或无法访问，使用 `NEEDS_CONTEXT`，列明缺项；执行 `COMPLETE` 或 `REVIEW_PASS` 前应完成相应必读材料的读取。

历史任务继续遵守其冻结协议对绑定失败和材料缺项的规定。

## 2. 外层状态

绑定区之后选择且仅选择一个外层状态：

```text
PRO_STATUS: COMPLETE
PRO_STATUS: REVIEW_PASS
PRO_STATUS: NEEDS_CONTEXT
PRO_STATUS: DECISION_REQUIRED
PRO_STATUS: BLOCKED
```

- `COMPLETE`：交付符合请求范围的完整文件。
- `REVIEW_PASS`：fresh review 确认完整目标已达到要求，正文无需实质修订。
- `NEEDS_CONTEXT`：身份已绑定，但完成任务所需的材料或信息不足。
- `DECISION_REQUIRED`：继续执行需要明确范围、文件结构、互斥路线或授权。
- `BLOCKED`：存在实际执行障碍，当前无法形成所需交付。

纯格式问题按 `Notes/OBSIDIAN_MATH.md` 分工处理。需要选择数学含义的问题属于内容核验范围。

## 3. 完整文件语法

`COMPLETE` 使用以下文件块。示例中的围栏和标记均为真实语法：

```````text
BEGIN_FILE::<binding_id>
path: Notes/example.md
mode: replace
`````markdown
# Title

行内公式使用 $x+y$。

$$
x+y=z
$$
`````
END_FILE::<binding_id>
```````

文件块要求：

- `path` 是 request allowlist 内的仓库相对路径，allowlist 以请求的 `target_files` 为准。
- `mode` 使用 `replace`。
- payload 是完整、原始 Markdown，可直接保存为 UTF-8 文件。
- 同一路径在一次响应中出现一个文件块。
- 作者写作返回请求要求的全部完整目标文件。
- fresh review 修订返回全部受影响目标文件的完整版本，其余目标沿用审查 checkpoint。
- 分析内容仅写入请求明确授权的分析文件。

完整文件保留前部、正文、末尾和所需元数据。局部修改也交付整个目标文件，使用实际全文表达修改结果。

## 4. 围栏与 payload 边界

文件内容围栏至少使用五个反引号，并标注 `markdown`。开闭围栏长度相同；长度严格大于 payload 内可能出现的同类围栏。

包含本协议七反引号样例的文件，外层文件内容围栏使用八个反引号。更深的嵌套按同一原则增加。

解析时，文件内容围栏内部的文本全部属于 payload。内部出现的 `PRO_STATUS`、`BINDING_OK`、`BEGIN_FILE`、`END_FILE`、`BEGIN_MESSAGE` 或 `END_RESPONSE` 样例均作为文件内容保存。

外层状态数量、文件边界和结束位置在 payload 之外核验。Codex 通过正确识别边界兼容协议样例，同时保留实际绑定、路径和完整性验证。

## 5. 消息状态

`NEEDS_CONTEXT`、`DECISION_REQUIRED` 和 `BLOCKED` 使用一个消息块：

```text
BEGIN_MESSAGE::<binding_id>
<具体缺项、冲突或阻塞；已完成的核验；继续所需的材料或决定>
END_MESSAGE::<binding_id>
```

消息提供可执行信息。例如说明缺失文件的路径与版本、无法确定的数学条件、越权操作或所需权限。此类响应以消息交付，保持正式文件的应用前状态。

## 6. Fresh review 的两种交付

全文达到要求时：

```text
PRO_STATUS: REVIEW_PASS
END_RESPONSE::<binding_id>
```

实际回复仍先包含第 1 节的绑定区。`REVIEW_PASS` 后直接结束，文件块和消息块均省略。

需要实质修订时，使用 `COMPLETE`，按第 3 节返回全部受影响文件的完整修正版。审查以完整候选和原始目标为依据；纯格式修复留给 Codex 应用层。

## 7. 结束

所有成功绑定的响应最后写：

```text
END_RESPONSE::<binding_id>
```

结束标记位于外层，并终止本次响应。其后仅允许传输产生的空白。

文件状态只包含绑定区、一个外层状态、相应文件块和结束标记。消息状态只包含绑定区、一个外层状态、一个消息块和结束标记。这样 Codex 可以完整捕获原文，再进行验证、staging 和应用。
