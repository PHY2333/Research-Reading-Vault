---
task_id: 20260915-state-injection-controlled-r-motivation
route: codex-only
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
git:
  remote: main
  branch: codex/state-injection-r-motivation-20260915
  base_commit: b92c85901cf3805d0f15e5f7459f0fb170410bc2
---

# 用户授权与范围

用户先要求 Codex 直接解释原位注入为什么需要数据 X 基控制的辅助门 R，随后明确要求“codex直接将这个动机补到笔记中”。依用户本轮授权，由 Codex 直接将已解释的动机接入正文，不调用 Pro。

范围限于 §3 导言与 §3.2：先考察 CNOT 加辅助线测量的候选线路，使用保留的 §3.1 异或测量规则比较正负输入分支，再引入只补偿负分支的相干受控 R，并衔接已有 K_m(R)、分支振幅与 R 约束。后续酉延拓、另一测量分支及校正不变。

# 归属、保留及 Git

沿用 State injection 主笔记；不新增前置笔记，不更新 CANONICAL_KNOWLEDGE.md 或 Notes/00-index.md。推导依托本笔记已建立的规则，不改变文献登记、版本、阅读状态或主辅关系，无翻译或截图任务。

开始时工作区已有 §1.2 措辞修改和 §2.1 注释整合；均保留为未提交状态，不纳入本轮提交。只暂存 §3 的本轮修改与任务记录，推送任务分支，不合并 main。新任务目录保留 TASK、APPLY_REPORT、FINAL_REPORT，既有任务目录不变。

# 完成

动机已接入正文，实际段落已通过独立局部数学复核、Obsidian 数学检查及 git diff --check。无待核对、TODO：补引用或待补推导；无临时文件。
