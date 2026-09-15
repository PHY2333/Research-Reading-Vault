---
task_id: 20260915-state-injection-phase-kickback
route: codex-only
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
git:
  remote: main
  branch: codex/state-injection-phase-kickback-20260915
  base_commit: aa1f50a71593437b9a5a4b10b8ac773ea93da329
---

# 用户授权与范围

用户最新明确要求“codex把相位回踢部分的注释加入”。依此覆盖默认 Pro 概念写作路由，由 Codex 直接添加一条短小局部注释，不重新调用 Pro。沿用已完成的异或版正文，只在 §2.1 的 CNOT 双重描述后补充折叠 callout；不改写其它正文。

注释采用本节已建立的 X 本征态与线性性，说明目标本征值为何成为控制端相对相位，并用数据 |−〉、辅助 |+〉的例子解释。限定固定目标本征态、控制端计算基态及一般数据叠加的区别。

# 归属与记录

State injection 仍是既有主笔记；不新增前置笔记，不更新 CANONICAL_KNOWLEDGE.md 或 Notes/00-index.md，不改变文献登记、版本、阅读状态或主辅关系，无翻译和截图任务。新任务目录保留 TASK、APPLY_REPORT、FINAL_REPORT；先前 Pro 重写及独立审查记录原样保留，其审查范围不扩展到本次新增注释。不合并 main。

# 完成

注释已添加；局部独立数学复核通过，Obsidian 数学检查和 git diff --check 通过，无待核对、TODO：补引用或待补推导。仅提交目标注释及本任务三份记录。
