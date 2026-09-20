# Notes/AGENTS.md

本文件是 Notes Pro-First 1.2 的唯一活动路由入口。正式正文的写作与实质审查标准统一由 `Notes/WRITING_GUIDE.md` 承担。

## 1. 选择路线

### `codex-only`

处理错字、链接、路径、frontmatter、纯格式，以及用户已经提供完整成文内容的精确替换。执行者依据确定的内容完成机械操作，保持授权范围内的数学含义、理解路径和知识归属。

### `pro-write`

处理概念解释、新笔记、局部或中等规模重写。Pro 完成必要的教学组织并输出完整文件；Codex 验证、规范化格式、应用和推送。普通概念笔记通常采用 `review_policy: internal`。

### `pro-write-review`

处理整篇笔记、复杂证明、多个章节、论文一般化，以及需要整体修复理解路径的反馈。Pro 输出完整候选后，按任务的审查策略进行全文审查。新任务的独立审查使用 TASK 中的 `independent` 与作者请求中的 `fresh` 对应关系。

凡需要决定概念的引入时机、解释顺序、数学论证或读者怎样形成理解的任务，选择包含 Pro 的路线。

## 2. 活动文件

进入 Notes 任务后读取：

- `Notes/WRITING_GUIDE.md`：正文质量、正向行文和连续阅读标准。
- `Notes/PRO_WORKFLOW.md`：任务阶段、自动执行、审查策略及审计保留。
- `Notes/PRO_OUTPUT_PROTOCOL.md`：绑定、状态、完整文件和结束标记。
- `Notes/OBSIDIAN_MATH.md`：目标格式与 Codex 的上下文修复权限。

新任务使用 1.2 活动框架。已冻结任务按其记录的执行依据和协议完成；历史规则通过 Git 历史查阅。版本与审查字段的兼容关系见 `Notes/PRO_WORKFLOW.md`。

## 3. Pro 的职责

Pro 实际读取固定 checkpoint 中的请求、协议和指定材料，理解读者起点、正文需要建立的内容、来源支持范围与输出范围，然后在内部完成教学组织。

写作时，Pro 按 `Notes/WRITING_GUIDE.md` 形成连续的 reader-visible Markdown，并输出请求要求的完整文件。审查时，Pro 连续阅读完整候选，判断数学信息、推理和理解路径是否满足原始目标；需要实质修订时直接提供完整修正版。

Pro 交付文本。GitHub 写入、本地应用、命令执行及其结果记录由 Codex 承担。

## 4. Codex 的职责

Codex 负责以下执行链：

1. 读取本地仓库，整理真实反馈、读者起点、必要来源和简洁请求。
2. 建立任务分支，将请求与材料推送为固定 GitHub checkpoint。
3. 通过 `@Browser` 调用 chatgpt.com 的 Pro，完整捕获响应。
4. 验证绑定、结束标记、文件完整性和路径 allowlist，将文件提取到 staging。
5. 按 `Notes/OBSIDIAN_MATH.md` 检查并修复权限内的格式问题。
6. 核对变更路径、文件覆盖和保留范围，应用候选并执行检查。
7. 按 TASK 的授权与审查策略完成 commit、push 和 R02。
8. 提供应用报告、最终回执及清理结果。

正文的教学性、数学性和语义性修改交由 Pro。Codex 的候选比较用于完整性、路径、保留范围和格式核验；内容层面的疑点交给 Pro 或来源核验。

## 5. 格式处理入口

Codex 可直接处理 Markdown / Obsidian 外层格式，以及由上下文或已读来源唯一确定的 LaTeX 语法或转义问题。具体分类、例子和复检步骤统一见 `Notes/OBSIDIAN_MATH.md`。

权限内的纯格式修复属于应用步骤，沿已有授权继续执行。修复目标是使同一正文和数学陈述正确渲染。

需要选择数学含义、改变公式内容、补充解释，或处理来源冲突时，进入相应内容核验入口。Checker 提供诊断位置；Codex 根据完整上下文作判断和编辑。

## 6. Fast binding

每轮请求包含独立的 `binding_id`。其值由 Codex 写入请求文件，并由 Pro 从实际文件读取；Browser 提示保留该值的隐藏状态。

Codex 核对 task、request、binding ID、repository、branch、checkpoint commit、allowlist 与结束标记。Fast Integrity 使用这些字段和完整性检查，默认采用最小审计。绑定与材料缺项的状态划分统一见该轮冻结的输出协议。

## 7. 自动连续执行

当 TASK 已设置 `automation.run_to_completion: true`，并具有相应 standing authorization 时，Codex 在任务分支内连续完成已授权的操作：

- request checkpoint 的 commit/push；
- R01 发送、捕获、验证、格式规范化和应用；
- R01 应用后的 commit/push；
- 按 review policy 执行 R02；
- R02 的捕获、检查、必要应用和最终 commit/push。

执行次数和轮次同时受 TASK 的 `max_author_rounds`、`max_review_rounds` 与 `preauthorized_browser_rounds` 约束。已授权阶段在条件满足后直接衔接。额外轮次、范围变化及主分支合并按对应授权入口处理。

## 8. 暂停与交接

以下情况进入暂停状态并保留现场：

- Browser 权限、账户不匹配或连接需要用户处理；
- Pro 返回 `NEEDS_CONTEXT`、`DECISION_REQUIRED`、`BLOCKED` 或绑定失败；
- 正式文件的删除、移动、拆分、合并或重命名需要决定；
- 输出路径越出 allowlist；
- 来源冲突、数学条件冲突或数学内容尚不确定；
- 格式修复存在多个合理解释，或可能改变数学含义；
- Codex 完成权限内的上下文修复后，检查仍未通过；
- push 失败，或下一步涉及合并主分支。

暂停记录说明具体路径、失败位置、已完成部分和下一步所需材料或决定。权限内且可确定的格式修复按第 5 节完成。

## 9. Git 安全

任务使用独立分支，默认命名为 `codex/<task-id>`；具体分支以 TASK 为准。Remote 从仓库实际配置和目标分支关系确认，写入 TASK 后使用。Remote 名称与主分支名称分别核对。

暂存使用明确路径，保留用户已有的无关修改。Git 操作遵守以下边界：

- 不使用 `git add -A`；
- 不直接向主分支 push；
- 不 force push；
- push 失败后保留响应、staging 和错误信息；
- 主分支合并由用户决定。

任务完成以已授权任务分支中的结果为准，最终回执明确报告推送和合并状态。
