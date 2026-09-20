# Notes working area

Framework: Notes Pro-First 1.2

本目录保存 Notes 任务的请求、交接、执行报告和经授权的分析产物。活动任务统一使用：

```text
Notes/WORKING/pro-tasks/<task-id>/
```

任务路线与权限见 `Notes/AGENTS.md`，阶段与保留策略见 `Notes/PRO_WORKFLOW.md`，可复用模板位于 `Notes/TEMPLATES/`。

## 内容归位

正式知识内容保存到经授权的主题笔记和读者索引。工作区保存任务原话、写作请求、审查请求、过程证据及报告。

正式笔记的知识链接指向稳定的知识笔记或来源。工作区中的分析通过后续任务整合到正式内容，其任务路径继续承担交接与审计职责。

## 保留与清理

成功任务按 TASK 保留请求、报告、经授权分析产物及 Git 记录。成功原始响应和 staging 按 `audit_retention` 清理；失败原文和必要现场保存在任务的 `FAILURES/` 中。

旧 `note-plans/`、`note-tasks/` 和 `authoring-tasks/` 通过迁移前 archive tag 与 Git 历史查阅。新任务使用本页规定的活动路径。
