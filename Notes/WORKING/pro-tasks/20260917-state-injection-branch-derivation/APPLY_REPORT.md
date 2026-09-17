# Apply report

- task_id: 20260917-state-injection-branch-derivation
- author: Codex，沿用用户明确局部编辑授权
- status: DONE
- applied_file: Notes/04-Magic State Injection/State injection.md
- placement: §4.3，资源约束至 K_m 的算符等式
- Pro_round: none

把压缩的三行推导拆成三个连续步骤：先写受控 R_U 在基输入上的作用，并代入辅助线测量规则；再用 ZX=-XZ 推出 Z^sX^m=(-1)^(sm)X^mZ^s，乘右侧 Z^s 后消去 Z^(2s)；最后以线性性将标量移到输入，再用 X^m|s_X〉=(-1)^(sm)|s_X〉替换。补明辅助态系数写到数据空间，始终保留未归一化因子 1/√2。

实际稿经独立只读数学复核通过；完整目标 Obsidian 检查通过。本轮段落之外与开始时本地快照逐字节一致。暂存内容从 HEAD 仅替换本段，所有原有用户编辑留在工作区；本次 diff 和 staged diff 空白检查通过。
