---
task_id: 20260917-state-injection-phase-difference
route: codex-only
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
git:
  remote: main
  branch: codex/state-injection-phase-difference-20260917
  base_commit: 9f3788693f31ca10b63d52ce8e2fc6c9144a3fa0
---

# 用户授权与范围

用户询问 §4.4 是否可以利用《对角相位门的Clifford层级》的结论，在 Codex 核对并说明衔接方案后明确回复“按这个改”。沿用本轮连续第四节修改中已指定的 Codex 直接编辑方式，应用用户确认的局部方案，不调用 Pro。

范围仅 §4.4：保留对角性使 R_U=I 的线路说明，引用相位差分恒等式和层级判据，说明 C_U=D_Δf，及单比特对角门下 U∈C3 当且仅当 C_U∈C2；以相位函数、差分、校正门的表格统一 T 与 sqrt(T)，由已有最低层数结论判断代价，保留一般非对角门及受控门的范围限制。

# 来源与保留

已读《对角相位门的Clifford层级》全文，重点采用 §3 式 (5)、(7) 和 §5 最低层数结论。sqrt(T) 的第四层来自 §5 公式，不归给未列此门的 §6 例表。CANONICAL_KNOWLEDGE.md 确认层级理论归属该笔记，State injection 只消费其结论。

编辑前本地有用户未提交修改；§4.4 外逐字节保留，既有修改不纳入本轮提交。任务分支只暂存本次 §4.4 与三份记录，不合并 main。独立实际稿复核、Obsidian 检查、引用锚点与差异范围检查通过。
