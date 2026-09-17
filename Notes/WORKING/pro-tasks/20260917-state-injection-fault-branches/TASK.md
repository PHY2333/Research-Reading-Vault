---
task_id: 20260917-state-injection-fault-branches
route: codex-only
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
git:
  remote: main
  branch: codex/state-injection-fault-branches-20260917
  base_commit: 1725e7cb1381d7d397510a7cd7f767560fe8e431
---

# 用户授权与范围

用户先询问资源 Z/X 故障的分支等式如何得到，随后明确要求“把推导过程写入正文”。本轮直接把已在对话中解释的推导接入 §5.1，沿用用户已指定的 Codex 局部修改方式，不调用 Pro。

范围是 §5.1 的资源 Pauli 故障介绍至两条故障分支恒等式。写清校正前未归一化的分支定义、CNOT 传播、辅助测量投影以及数据端残留算符；原概率段和后续校正讨论不变。

# 保留与检查

以当前本地版本为基线，本段外逐字节保留。只暂存最终推导段与任务记录，范围外已有用户编辑不纳入提交。实际段落独立数学复核及 Obsidian 数学检查通过，staged diff 进行空白检查。

沿用已有 State injection 知识归属，无新增前置笔记、索引、canonical 或文献管理变化，无翻译和截图。任务目录保留三份记录；成功推送后清理本轮临时快照。不合并 main。
