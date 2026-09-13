---
task_id: 20260913-diagonal-clifford-hierarchy
route: pro-write-review
status: CHECKPOINT_PUSHED
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/对角相位门的Clifford层级.md
integration_files:
  - Notes/00-index.md
  - CANONICAL_KNOWLEDGE.md
integrity: fast
review_policy: fresh
audit_retention: errors-only
format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true
git:
  remote: main
  branch: codex/diagonal-clifford-hierarchy-20260913
  base_commit: 81a2506ca4ad10c3f5c4fa4114f35e8a511948b1
automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 2
  preauthorized_browser_rounds:
    - R01
    - R02
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - ambiguous_format_or_latex_repair
    - math_content_uncertain
    - format_check_failed_after_codex_repair
    - push_failure
    - merge_to_main
---

# 用户目标

用户先询问 S008 译文 §2.1 中 $U_{m,\boldsymbol a}$ 位于第 $(m-1)+\operatorname{wt}(\boldsymbol a)$ 层是什么意思，随后要求：“在Notes/08-Binary Extension Field Non Clifford Module中让pro写一篇笔记说明这个层级公式怎么推导”。本任务由 ChatGPT Pro 撰写完整中文笔记，再由全新 Pro 对话审查。

# 归属与工作树

正式 Notes 没有此公式完整推导的既有主笔记。《二元扩域》处理域算术和二进制表示，明确未承担其它门的层级判定；《逻辑基态的二次相位》《State injection》及 MGT 笔记分别处理态相位与前馈，不拥有本定理。新文件在用户指定 08 目录成为该单项式对角比特门层级公式的唯一 owner。

在 `.tmp/worktrees/20260913-diagonal-clifford-hierarchy/` 独立工作树中工作，保留原 main 工作树已有的 Obsidian、S009 文献与翻译改动。不新增其它前置笔记，不修改已有正文或文献登记，不删除、移动、合并或改名正式文件。

# 授权与完成条件

按 Notes Pro-First 1.1 自动连续执行 request checkpoint、R01 写作、协议捕获、允许的格式规范化、R01 应用、fresh R02 审查、机械索引集成与任务分支 commit/push。不得由 Codex 代写或语义改写 Pro 正文，不自动合并 main。证明必须同时建立层级上界和最低层数，说明非零支持与全局相位约定。

# 预定机械集成文字

R02 通过后，Codex 在 `Notes/00-index.md` 第 8 条的二元扩域链接后增加：

```md
   - [[对角相位门的Clifford层级]]：从 Pauli 共轭与相位差分推导单项式对角比特门的最低 Clifford 层级 $m+\operatorname{wt}(\boldsymbol a)-1$，并核对 $Z,S,T,\mathrm{CZ},\mathrm{CS},\mathrm{CCZ}$。
```

将该索引的 08 目录范围中的“二进制坐标表示”补为“二进制坐标表示、对角比特门的 Clifford 层级”；将 canonical 当前范围中“结构映射与二进制表示”补为“结构映射、二进制表示及单项式对角比特门的 Clifford 层级”。

在 `CANONICAL_KNOWLEDGE.md` 二元扩域条目后增加以下唯一 owner 登记；只有 Pro 正文及 fresh review 已建立全部相应结论时才应用：

```md
## 单项式对角比特门的 Clifford 层级

- 主笔记：[[对角相位门的Clifford层级]]，路径 `Notes/08-Binary Extension Field Non Clifford Module/对角相位门的Clifford层级.md`。
- 前置依赖：计算基、酉算符与共轭、比特 Pauli 算符、二进制变量及基本整数运算；有限域理论不是本公式证明的前置。
- 已有结论：对 $m\ge1$、$\boldsymbol a\in\mathbb F_2^n\setminus\{0\}$，门 $U_{m,\boldsymbol a}|\boldsymbol x\rangle=\exp(2\pi i\prod_{j:a_j=1}x_j/2^m)|\boldsymbol x\rangle$ 的最低 Clifford 层级为 $m+\operatorname{wt}(\boldsymbol a)-1$；主笔记给出 Pauli 共轭／相位差分的上界证明和排除更低层的证明。
- 写新内容时引用它：判断上述单项式相位门及 $Z,S,T,\mathrm{CZ},\mathrm{CS},\mathrm{CCZ}$ 的层级，或解释相位分母与支持大小如何共同决定层数时引用。
- 边界：采用通常的 $n$ 比特 Pauli 与 Clifford 层级，并忽略全局相位；$\boldsymbol a=0$ 只产生全局相位。相位函数在整数或模相位周期意义下计算，不能无条件改为 $\mathbb F_2$ 加法；层级编号不是电路深度或门数。本条不声称任意相位项乘积的最低层数必为各项最大值。
- 来源：S008 arXiv:2608.09727v1 §2.1 式 (1)；Cui–Gottesman–Krishna, *Diagonal gates in the Clifford hierarchy*, arXiv:1608.06596v1，§§II、IV（Theorem 3）。
- 状态：已整理。
```

# 当前阶段

CHECKPOINT_PUSHED：用户再次明确要求重试后，任务分支已成功推送至 GitHub，本地请求提交为 `862e000e9e7ccf5da4a10a368aa460e290d9f126`。认证阻塞已解除。现在继续自动执行 R01 写作和 fresh R02 审查。

此前两次推送因终端 GitHub HTTPS 凭据不可用而失败，均按仓库规则暂停；本次重试已成功。独立工作树和原 main 工作树的隔离保持不变。
