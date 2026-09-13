---
task_id: 20260913-diagonal-clifford-hierarchy
request_id: R01
request_type: new-proof-note
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: 527e6c8b180b4d2cb527cb8af8d382dd
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/对角相位门的Clifford层级.md
---

# 任务

由你直接写一篇完整中文教学笔记，解释并证明 S008 §2.1 的层级公式。用户已经得到公式含义和六种常见门的简短解释，现在需要真正能够跟随的推导。标题为“对角相位门的 Clifford 层级”。独立决定教学组织，正文以公式如何从递归定义推出为持续主线，不能只复述分类定理或用“每多一个控制就升一层”替代证明。

所讨论的门为

$$
U_{m,\boldsymbol a}|\boldsymbol x\rangle
=\exp\!\left(\frac{2\pi i}{2^m}\prod_{j:a_j=1}x_j\right)|\boldsymbol x\rangle,
\qquad m\ge1,\quad \boldsymbol a,\boldsymbol x\in\mathbb F_2^n.
$$

主结论对 $r=\operatorname{wt}(\boldsymbol a)\ge1$ 是最低层数 $k=m+r-1$。正文必须区分“属于第 $k$ 层”和“不能属于更低层”；后者需要论证而不只是宣称。$\boldsymbol a=0$ 为全局相位，需明确另行处理。

# 必读材料

GitHub 材料均以 Browser 指定的同一个 commit 为准：

- 本任务 TASK.md（范围和预定机械索引集成）。
- Notes/WRITING_GUIDE.md、Notes/OBSIDIAN_MATH.md、Notes/PRO_OUTPUT_PROTOCOL.md。
- Translations/S008.full.zh-CN.md：译文信息、§2.1 从 Clifford 层级定义到式 (1) 与 $T$/CS/CCZ 的相关段落，以及 [CGK17] 书目。其余 85 页译文不用全文阅读。
- CANONICAL_KNOWLEDGE.md：二元扩域、逻辑基态的二次相位、State injection 的相关条目；Notes/00-index.md 第 8 路线。只核对归属和连接，不强迫读者提前掌握其它笔记。
- Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md：第 6 节末尾的比特 Clifford 共轭判据及范围限制；不需要重写此文。
- 外部原始数学来源：Cui, Gottesman, Krishna, *Diagonal gates in the Clifford hierarchy*, arXiv:1608.06596v1，https://arxiv.org/html/1608.06596v1 或 https://arxiv.org/pdf/1608.06596v1 ，§II 的全局相位及递归定义，§IV 的 Definition 4–6、Theorem 3 及相关证明。正式发表信息为 Phys. Rev. A 95, 012329 (2017)，doi:10.1103/PhysRevA.95.012329。实际读取后准确引用，不能凭摘要冒充证明。

来源用途：S008 是读者遇到公式的位置；CGK17 是一般分类来源。本笔记专注于 $p=2$ 的单项式门，允许用独立、可核验的自包含推导证明其特例，不需要把所有素维 qudit 分类完整搬进正文。不要把新证明步骤伪称为 S008 原文已有步骤。

# 读者起点和必要闭合

允许依赖：计算基 $|\boldsymbol x\rangle$、线性算符／矩阵、酉算符、伴随与共轭、单比特 $X,Z$ 的作用、基础归纳法和二进制变量。需在首次使用时建立多比特 Pauli、Clifford 层级的递归含义、汉明重量／支持、整数相位与 XOR 的区别。无需有限域、编码、门传态或群论高级工具作前置。

需要让读者能从 $U X_j U^\dagger$ 的基态计算看到相位差分如何出现，并解释为什么这使层级计数下降。证明上界若只检查 $X_j,Z_j$，必须说明为何足以推出对所有 Pauli 的条件；不能假定 $k\ge3$ 的整个 Clifford 层是群。需要使用对角子集乘法封闭、Pauli 左右乘不改变层级或有限差分判据等性质时，给出当前证明所需的理由，不能循环引用待证公式。请自行选择最清楚的证明路线。

最低层数必须排除相位抵消与全局相位伪障碍，特别检查 $m=1$、$r=1$、$k=1$，以及重复／不同方向差分的使用。相位差分正负号必须与共轭次序一致。原句把所有 $\boldsymbol a\in\mathbb F_2^n$ 一起写出；此处明确隔离零向量特例，不把它冒称为最低 $m-1$ 层。

用 $Z,S,T,\mathrm{CZ},\mathrm{CS},\mathrm{CCZ}$ 校准参数、相位和层级；至少一个共轭算例应真正连接一般证明。区分非参与比特与支持大小。避免未经证明推广为任意多项式或任意控制门的最低层数；无需完整门综合、T-count、蒸馏协议、qudit 结构或有限域背景。

# 交付

完整单文件按协议输出，唯一 allowlist 为 target_files。不要输出 TASK、索引或 canonical 完整文件；Codex 在 fresh review 后按 TASK 预定文字机械集成。审阅 TASK 中预定索引的数学边界，如果不能由成文支撑须指出具体问题。

遵守写作规范：目标和证明地图先清楚，关键对象随用途引入，必要推理不跳步，辅助引理只服务主线；不写成性质百科，不把关键证明放进可以跳过的选读块。引用放在相关论述附近，正文无任务、模型、流程、Git、维护者语言。使用原始 Obsidian Markdown 的 $ / $$ 数学分隔符。输出前连续复读完整稿，按协议返回完整 binding、COMPLETE、五反引号文件块及 END_RESPONSE，不操作 GitHub。
