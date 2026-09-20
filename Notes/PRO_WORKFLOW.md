# Notes/PRO_WORKFLOW.md

Framework: Notes Pro-First 1.2

本文件规定 Notes 任务从请求准备到任务分支交付的执行过程。写作和实质审查使用 `Notes/WRITING_GUIDE.md`；输出绑定与文件语法使用该轮冻结的 `Notes/PRO_OUTPUT_PROTOCOL.md`。

## 1. 任务目录与执行依据

```text
Notes/WORKING/pro-tasks/<task-id>/
├── TASK.md
├── PRO_REQUEST.md
├── REVIEW_REQUEST.md
├── APPLY_REPORT.md
├── FINAL_REPORT.md
└── FAILURES/
```

`REVIEW_REQUEST.md` 仅在需要 R02 时创建。`FAILURES/` 保存失败原文及必要现场。请求明确授权的分析产物也保存在任务目录，并列入相应输出范围。

初始准备时记录活动框架、目标路径、审查策略、实际 remote、任务分支、任务前提交和自动执行授权。材料以 Browser 提示中的固定 commit 为准。

涉及框架或协议改写时，在请求中明确本任务使用的冻结外层协议。R02 读取最新应用 checkpoint 的候选，同时按请求指定的原协议提交读取外层协议。新文本供后续任务使用。

## 2. 路线与审查策略

路线由 `Notes/AGENTS.md` 选择。新任务采用以下字段对应关系：

| TASK 的 `review_policy` | 作者请求的 `review_policy` | 执行含义 |
|---|---|---|
| `none` | `none` | 按路线完成应用，省略独立审查 |
| `internal` | `internal` | Pro 在写作轮内部完成全文自查，省略 R02 |
| `independent` | `fresh` | R01 应用后，在全新 Pro 会话执行 R02 |

第三种情况下，`REVIEW_REQUEST.md` 使用 `review_mode: independent`。普通概念笔记通常采用 `pro-write + internal`；整篇、复杂证明及整体教学修复通常采用 `pro-write-review + independent`。

### 历史兼容

TASK 的 `independent` 与作者请求的 `fresh` 表示同一独立审查安排，无需重命名历史字段。

历史 `same-thread` 继续表示其原任务规定的同会话审查，与 fresh review 分别解释。继续历史任务时使用该轮冻结的字段和协议；新建 1.2 独立审查任务时采用上表。需要迁移执行方式时，记录变更并形成新请求与 checkpoint，保留原有历史记录。

## 3. 状态

```text
PREPARE
→ CHECKPOINT_PUSHED
→ R01_RUNNING
→ R01_APPLIED
→ R02_RUNNING
→ DONE
```

省略独立审查时，从 `R01_APPLIED` 完成最终检查后进入 `DONE`。`codex-only` 按其机械操作范围完成检查、应用和交付。

异常状态保留：

```text
PERMISSION_REQUIRED
NEEDS_CONTEXT
DECISION_REQUIRED
CHECK_FAILED
BLOCKED
```

捕获、解析、staging 和格式规范化作为阶段内部步骤记录。

## 4. 准备请求与初始 checkpoint

Codex 先读取工作树并识别用户已有修改，再生成 TASK、作者请求及需要的审查请求。

作者请求以读者起点、正文待建立内容、事实支持范围和输出范围组织。保留真实反馈，并把本次解决目标写成读者能够完成的判断、计算或解释。公共写作标准通过引用统一指南调用。

每轮请求各有独立的隐藏 `binding_id`。Browser 提示提供 repository、branch、commit 和请求路径，由 Pro 实际读取请求中的身份字段。

确认以下条件后，显式暂存任务材料并 commit/push：

- 目标路径、来源和必要上下文已列明；
- TASK 与请求的路线及审查策略对应；
- remote 和任务分支来自实际配置；
- 本次暂存范围与用户已有无关修改分开；
- 自动执行轮次与次数已有授权。

push 成功后记录实际 checkpoint commit，进入 `CHECKPOINT_PUSHED`。

## 5. R01 发送与完整捕获

Codex 使用 Browser 作者模板发送 R01，并在已授权范围内持续到捕获完成。

响应先原样保存到本地临时目录：

```text
.tmp/pro-responses/<task-id>/R01.raw.md
```

完整性验证以外层结束标记为准。原文先保存再解析，供绑定、文件边界和失败诊断使用。

捕获失败或响应截断时，保留已有原文及错误位置。重试受 TASK 的次数与轮次限制；请求内容更新后重新生成相应 binding 和 checkpoint。

## 6. Fast parse 与 staging

使用 `parse_pro_response.py` 验证协议并提取文件到 staging。核验内容包括身份字段、固定提交、状态、结束标记、路径安全、allowlist、重复路径和文件块完整性。

作者 `COMPLETE` 的文件集合应覆盖请求要求的全部目标。审查 `COMPLETE` 返回所有受影响目标的完整修正版，其余目标沿用审查 checkpoint。

协议标记按外层结构解释。文件内容中的状态示例、文件标记及结束标记属于 payload，原样保留。解析器适配应围绕真实外层边界进行验证，同时保留绑定和路径检查。

解析通过后才进入格式规范化。解析失败时，保留原文和已有 staging；正式文件保持应用前状态。

## 7. Codex 上下文格式规范化

对 staging 中的目标 Markdown：

1. 运行 `check_obsidian_math.py`。
2. 读取诊断所在的完整段落、相邻公式及必要的已读来源。
3. 按 `Notes/OBSIDIAN_MATH.md` 判断为外层格式、可唯一确定的 LaTeX 语法，或内容与多义问题。
4. 对权限内的前两类直接编辑 staging。
5. 复读修复前后内容，确认数学陈述、正文含义和内容顺序保持。
6. 再次运行 checker，并记录简洁修复摘要。

Checker 负责诊断，实际编辑由 Codex 结合上下文完成。权限内的格式修复沿当前轮次继续。

数学含义需要选择、来源冲突或内容欠缺时，保存问题并交由 Pro 或来源核验。上下文修复后仍未通过检查时，进入 `CHECK_FAILED` 并保留现场。

## 8. 应用与提交 R01

收到可应用的 `COMPLETE` 后，按顺序完成：

1. 确认全部要求的目标文件及 allowlist。
2. 完成 staging 格式检查与权限内修复。
3. 比较完整候选与旧文件，核对文件覆盖和保持范围。
4. 将通过检查的文件复制到目标路径。
5. 对目标再次运行 Obsidian 数学检查和 `git diff --check`。
6. 更新 `APPLY_REPORT.md`，记录绑定、文件和检查结果。
7. 显式暂存经授权的目标及任务报告。
8. commit/push，记录实际提交和推送结果。
9. 成功后按保留策略清理该次成功响应和临时 staging。

教学表达、数学论证及段落组织的变更来自 Pro 交付。Codex 在应用时处理已定义的机械和格式事项。

若最终检查或 push 失败，保留原始响应、staging 和错误信息，进入对应异常状态。

## 9. 独立 R02

R01 应用并成功推送后，以最新应用结果和完整审查材料形成 R02 checkpoint。向全新的 Pro 会话发送 Browser 审查提示。

R02 实际读取当前候选全文、同任务原始请求、TASK、统一指南及必要来源。先判断原始学习目标、数学信息和理解主线，再按实际影响修订。

### `REVIEW_PASS`

Codex 对当前目标完成最终格式检查。权限内的格式问题直接修复、记录并提交。检查与推送完成后进入交付。

### `COMPLETE`

将受影响文件的完整修正版提取到 staging，执行与 R01 相同的绑定、路径、格式、应用和 Git 检查，再提交推送。

孤立且含义确定的格式修复留在应用层。额外 Pro 轮次按 TASK 的次数、预授权轮次和暂停条件处理。

## 10. 异常状态的下一步

- `BINDING_FAILED`：保留响应，核对请求、协议访问和身份信息，停止该次应用。
- `NEEDS_CONTEXT`：保存具体缺项；补足材料并形成新 checkpoint 后，从相应入口恢复。
- `DECISION_REQUIRED`：记录文件结构、互斥路线、范围或授权问题，等待明确决定。
- `BLOCKED`：保存实际阻塞原因及恢复条件。
- 协议、完整性或格式检查失败：进入 `CHECK_FAILED`，保留可复现的位置和现场。
- 权限或账户问题：进入 `PERMISSION_REQUIRED`。
- push 失败：停止后续应用链，保留本地提交、响应和错误信息。

内容完整性或数学语义疑点交给 Pro；权限内的纯格式问题按第 7 节处理。失败状态的外层文本含义以该轮冻结协议为准。

## 11. Standing authorization

TASK 中的 `run_to_completion: true` 与相应授权表示，Codex 可在任务分支内连续执行已列明的 R01、R02、格式规范化、commit 和 push。

各阶段在条件满足后直接衔接；执行同时遵守 `stop_only_on`、轮次上限和权限范围。新轮次、越权路径、结构变化及合并主分支使用明确的授权入口。

## 12. 审计保留与清理

默认 `audit_retention: errors-only`：

- 成功任务保留 TASK、请求、应用报告、最终报告、经授权分析产物和 Git commits。
- 成功原始响应在相应应用、检查、报告和推送完成后删除。
- 失败原文与必要现场保存到 `FAILURES/`，供恢复和核验。
- 用户已有无关材料按原状态保留。

历史 `minimal` 和 `full` 按原任务约定解释；任务显式要求保留成功原文时遵守该要求。清理仅涉及本任务允许清理的临时材料。

## 13. 完成与回执

`FINAL_REPORT.md` 记录任务分支、remote、各 checkpoint 与应用提交、Pro 状态、格式处理、检查、保留范围及未决事项。

Codex 完成已授权的最终 push 后，提供流程回执，并明确主分支合并状态。任务分支结果供用户决定后续整合。
