这个索引用来记录本库的学习顺序和主笔记入口。它不替代具体笔记中的推导；新增主线笔记或移动目录时，应同步更新这里。

---
### 学习顺序

1. 线性代数与稳定子表示
   - [[二进制空间性质]]：$\mathbb F_2^n$、直和补空间、正交补和 CSS 码需要的线性代数记号。
   - [[逻辑基态的表示]]：从 $X$ 型稳定子、CSS 码到一般稳定子码的逻辑计算基态表示。
   - [[逻辑基态的二次相位]]：一般稳定子态在计算基展开中允许的一次相位和 $CZ$ 型二次相位。

2. 噪声通道与 magic-state 错误模型
   - [[CPTP映射与Kraus表示]]：量子信道、Kraus 表示、保迹条件和 postselection 分支的数学语言。
   - [[Clifford Twirling 与魔态错误模型]]：把 noisy $|T\rangle$ 归约为随机 $Z$ 错误模型，并区分 twirling 与独立性假设。

3. Magic-state injection
   - [[State injection]]：从 gate teleportation 推导 $U$-injection、in-place gadget、$T$ injection 和 byproduct correction。
   - [[MGT 的反向传播与稳定子码构造]]：区分物理、反向传播与稳定子码表示，并推导一般 commuting-Pauli 资源态的分支门和确定性前馈。

4. 横向 $T$ 与 triorthogonal distillation
   - [[汉明重量展开]]：把 XOR 和码字汉明重量写成整数多项式，是横向 $T$ 模 $8$ 相位分析的工具。
   - [[三正交码与横向逻辑T门]]：说明 triorthogonal 条件如何保证横向 $T$ 的非 Clifford 相位只落在逻辑一次项上。
   - [[Reed-Muller码]]：$[\![15,1,3]\!]$ Reed-Muller 码、横向 $T/T^\dagger$ 方向和 15-to-1 的 $35p^3$。
   - [[Distillation protocol]]：统一的 $G_1/G_0$ distillation 矩阵表示、syndrome、输出逻辑错误、接受概率和 yield。

5. Compact distillation factory
   - [[重复码上的逻辑T门]]：从 repetition-code logical $T$ 到 compact distillation matrix 的 $\alpha\mapsto\beta$ 变换。
   - [[Canonical distillation family]]：用 zeta/Möbius 反演构造 Jacinto 等人的 canonical compact family。
   - [[SAT搜索紧凑蒸馏工厂]]：把 support 选择、距离约束和 T-count 优化写成 SAT 搜索。

6. CCZ / qLDPC factory 延伸
   - [[Chain complex 与 cochain complex]]：chain/cochain complex 的 degree、cycle/cocycle、boundary/coboundary 和 homology/cohomology。
   - [[CSS码中的cochain complex]]：kernel、image、quotient、logical operator class 和 metacheck 的 CSS 码翻译。
   - [[Tensor product 对 direct sum 的分配律]]：解释普通 tensor product 如何把两个 direct sum 分解成双指标网格。
   - [[Cochain complex 的 tensor product]]：解释 graded vector space、total degree、coboundary map 和二项 complex 乘成三项/四项的来源。
   - [[Balanced tensor product 与 coinvariant quotient]]：固定右模、左模与中间 bimodule，说明 module tensor 与 anti-diagonal linear coinvariants 一般自然同构；作用保持选定 bases 时，它又是集合层 orbit quotient 的线性化。
   - [[Tricycle complex 的 balanced-product 构造]]：在 Menon 的有限 Abelian group-algebra 特例中构造 $R\to R^3\to R^3\to R$，并固定 regular representation 与二进制矩阵的方向约定。
   - [[Cup product 与 Leibniz rule]]：说明额外乘法 $\cup$ 和 Leibniz rule 如何让 cup product 在 cohomology 上良定义。
   - [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]：说明 cup product 后为什么要用泛函读成 physical phase，解释 classical seed code 上的 in/out/free 局部读数，并证明 ordinary tensor product 继承 integrated Leibniz。
   - [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]：解释 free-basis averaging、relative-translate operation 与 invariant integral 如何共同继承 integrated Leibniz。
   - [[Symmetric triple cup-product]]：解释 Menon 如何用 $\int_R$、symmetric integrated Leibniz、sector 和 preorientation 选择得到 physical $CCZ$ 三元组判据。
   - [[Menon 2025 Magic Tricycles]]：finite-block qLDPC tricycle codes、logical hypergraph magic state 和 single-shot $CCZ$ factory。

7. Lifted-product qLDPC 构造
   - [[Hypergraph product code]]：核心入口；从两个经典种子校验矩阵建立 HGP blocks、两个物理比特扇区、四类 Tanner 边与行／列乘积方向。
   - [[张量积与直和泛性质的 HGP-Künneth 接口]]（可选应用桥梁）：说明如何先验证双线性规则、用张量积泛性质线性化，再用直和泛性质拼接 total-degree 分量；一般分配律仍见 [[Tensor product 对 direct sum 的分配律]]。
   - [[Lifted product code]]：在 HGP 外层骨架上加入 lift 标签、循环 permutation 与环值 blocks，并区分 outer product 坐标和 inner lift 副本。
   - [[S007 中 LP 码的分层执行]]：把 outer product、inter-lift 与 intra-lift 结构对应到图 12 的提升间重排、提升内重排、门执行和定向转移。
   - [[Künneth 分解]]（可选数学支线）：用于逻辑空间、维数公式与一般系数边界，不是 HGP／LP 构造或 S007 执行的强制前置。

8. 二元扩域与非 Clifford 模块
   - [[二元扩域]]：从不可约多项式商构造 $\mathbb F_{2^s}$，建立基坐标、域运算、Frobenius、迹与范数，并说明这些结构如何变成 $s$ 比特上的二进制线性表示。
   - [[对角相位门的Clifford层级]]：从 Pauli 共轭与相位差分推导单项式对角比特门的最低 Clifford 层级 $m+\operatorname{wt}(\boldsymbol a)-1$，并核对 $Z,S,T,\mathrm{CZ},\mathrm{CS},\mathrm{CCZ}$。

---
### 当前目录归属

- `Notes/01-量子纠错基础/`：二进制空间、CSS 码和逻辑基态表示等前置结构。
- `Notes/02-Clifford与稳定子形式/`：稳定子态相位、Clifford/stabilizer 形式相关内容。
- `Notes/03-Magic State基础/`：量子通道、twirling 和 magic-state 错误模型。
- `Notes/04-Magic State Injection/`：state injection、gate teleportation 和 byproduct correction。
- `Notes/05-Magic State Distillation/`：triorthogonal code、Reed-Muller、distillation protocol、compact factory 和相关资源计数。
- `Notes/06-CCZ Distillation/`：CCZ/qLDPC factory、tricycle code、cochain complex、balanced product、metacheck 和 single-shot state preparation。
- `Notes/07-Lifted-Product Code/`：HGP 核心结构、lifted-product code、S007 分层执行案例，以及逻辑空间与一般系数问题所需的可选 Künneth 支线。
- `Notes/08-Binary Extension Field Non Clifford Module/`：二元扩域的代数基础、二进制坐标表示、对角比特门的 Clifford 层级，以及后续伽罗瓦 qudit 与扩域非 Clifford 门所需的接口。

容错架构与资源估算主题仍未建立；若后续建立 surface-code factory、lattice surgery、code distance selection、T-count/T-depth 和 spacetime volume，可另开编号目录并同步更新这里。

---
### 知识库维护

以下入口只用于维护正式知识笔记，不属于上述正式阅读顺序：

- [Notes 统一入口](AGENTS.md)
- [正文写作规范](WRITING_GUIDE.md)
- [Notes Pro-First 1.0 流程](PRO_WORKFLOW.md)
- [Pro 输出协议](PRO_OUTPUT_PROTOCOL.md)
- [Obsidian 数学格式](OBSIDIAN_MATH.md)

`Notes/WORKING/` 是单次任务的临时交接区，不属于正式阅读索引；这里不列出任何单次任务目录。

---
### 后续应补主题

- [[Clifford group]]
- [[Gottesman-Knill theorem]]
- [[T state]]
- [[Magic State Distillation]]
- [[T gate injection]]
- [[Surface-code factory]]
