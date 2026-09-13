# CANONICAL_KNOWLEDGE.md

本文件是面向 agent 的知识索引，记录 canonical ownership、别名、适用范围和必要来源关系。它用于写新笔记前查重和归属：如果某个概念、公式、协议或资源估算结论已经在这里登记，新内容应链接对应主笔记，只摘取当前需要的最短结论，不重新证明、不重复铺背景；它不承担面向读者的阅读顺序、正式正文复述或单次任务日志。

> 本文件只登记已经形成稳定主笔记的知识。临时想法、未核对推导和论文摘录不要直接登记为 canonical；应先放在对应草稿或论文笔记中。

---

## 1. 使用流程

写新笔记、改旧笔记或整理论文笔记时，先按以下顺序检查：

1. 搜索本文件，确认相关概念是否已有主笔记。
2. 若已有主笔记，在当前笔记中只引用最短结论，并说明这个结论用于哪一步。
3. 若当前内容只是某个通用结论的特例，优先编辑或引用主笔记，而不是另起一套推导。
4. 若发现重复解释，确定一个主笔记，另一篇改成摘要、应用或协议特例。
5. 若新增了可复用结论，或纠正了旧相位、公式、常数、适用范围，应更新本文件。

---

## 2. 条目格式

新增条目时尽量使用这个结构：

```md
## 主题名

- 主笔记：[[主笔记名]]，路径 `Notes/.../主笔记名.md`。
- 前置依赖：读这篇主笔记前默认已经知道哪些对象、记号或上游结论。
- 已有结论：用最短形式写出可复用定义、公式、协议接口或资源关系。
- 当前笔记只保留：说明这篇主笔记自己的核心内容边界，避免把上游背景全部塞进来。
- 写新内容时引用它：说明哪些场景应引用此条目。
- 不要在当前笔记重复：列出应该外链到其它主笔记的背景、完整推导或类比。
- 边界：列出相位约定、噪声假设、leading-order 条件、是否忽略 loss/leakage/measurement error 等限制。
- 状态：已整理 / 待补引用 / 待核对 / 已废弃。
```

不是每个条目都必须包含所有字段，但“主笔记、前置依赖、已有结论、写新内容时引用它”应尽量保留。新增复杂主笔记时，尤其要写清“不要在当前笔记重复”，避免后续修改把上游概念解释硬塞进正文。

---

## 3. 更新规则

- 当前笔记只保留会直接使用的公式、协议骨架或假设；通用定义、矩阵构造、错误模型和资源公式放回主笔记。
- 若读者对当前笔记提出局部疑问，先检查本文件中对应条目的“前置依赖”和“不要在当前笔记重复”；能外链上游的，不在当前笔记新增解释补丁。
- 若只是换一个协议特例，先引用通用主笔记，再说明特例参数。例如先引用 [[Distillation protocol]] 的 $G_0e^T$ 和 $G_1e^T$ 结论，再代入具体矩阵。
- 若发现主笔记中公式、相位或常数不确定，先在主笔记标 `待核对` 或 `TODO：补引用`，不要在新笔记里另起一套不一致记号。
- 论文笔记里的可复用概念应迁移到主题目录主笔记；论文笔记保留“该论文如何提出或使用这个结果”。
- `Notes/00-index.md` 只作为路线图，不承担具体推导的 canonical 归属。

---

## 4. 当前范围

本清单不按目录整批纳入，而只登记已经形成稳定主笔记的结论。目前覆盖 `Notes/01-量子纠错基础/` 至 `Notes/05-Magic State Distillation/` 的已整理主线，`Notes/06-CCZ Distillation/` 中已经稳定的 cochain/CSS、tensor 与 balanced product、tricycle complex、cup/integrated Leibniz、STCP 和 Menon 协议级归属，以及 `Notes/07-Lifted-Product Code/` 中的 Künneth 分解、HGP 与 LP 构造及 S007 第 6 节分层执行应用，以及 `Notes/08-Binary Extension Field Non Clifford Module/` 中二元扩域的构造、算术、结构映射、二进制表示及单项式对角比特门的 Clifford 层级。

尚未拆成独立概念主笔记的 single-shot CCZ factory、hypergraph magic state 等主题继续由 [[Menon 2025 Magic Tricycles]] 承担论文语境；形成稳定概念笔记后再单独登记，不在本文件预先复制论文内容。

---

## 主路线图

- 主笔记：[[Notes/00-index|00-index]]，路径 `Notes/00-index.md`。
- 已有结论：基础主线由 stabilizer 与 magic-state 基础推进到 injection、twirling、distillation、Reed-Muller、triorthogonal、compact factory、canonical family 和 SAT 搜索。CCZ/qLDPC 延伸沿 cochain/CSS → ordinary tensor 与 balanced product → tricycle complex/metachecks → cup product 与 integrated Leibniz → STCP/logical $CCZ$ → Menon single-shot CCZ factory 推进；lifted-product 构造主线沿 HGP blocks、四类边与行／列方向 → cyclic/group lift → LP 环值 blocks 与 balanced quotient 推进，并由 S007 应用笔记连接 outer/inter/intra-lift 的分层执行。Künneth 分解是逻辑空间、维数公式与一般系数边界的可选数学支线。
- 写新内容时引用它：新增主线主题、改变学习路线或加入新的一级主题目录时更新这里；普通局部补充不需要把背景重复写进路线图。

---
## 二元扩域 $\mathbb F_{2^s}$

- 主笔记：[[二元扩域]]，路径 `Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md`。
- 前置依赖：$\mathbb F_2$ 上的向量、线性映射与矩阵，以及多项式加法、乘法和整除的基本概念。
- 已有结论：对次数为 $s$ 的不可约多项式 $f(x)\in\mathbb F_2[x]$，商 $\mathbb F_2[x]\,/\,(f)$ 是含 $2^s$ 个元素的域；每个元素有唯一的次数小于 $s$ 的代表元，并在选定基后对应 $\mathbb F_2^s$ 中的坐标。加法、固定元素乘法与 Frobenius 都是 $\mathbb F_2$-线性映射；一般乘法是双线性的。主笔记还固定绝对迹、绝对范数、迹配对、对偶基和乘法矩阵的记号与适用范围。
- 当前笔记只保留：抽象域与具体表示的区别、不可约多项式商构造、可计算的域运算、有限域的必要结构、迹／范数／基与二进制矩阵接口，以及进入伽罗瓦 qudit 语境前所需的最短桥梁。
- 写新内容时引用它：涉及 $\mathbb F_{2^s}$ 元素的坐标展开、无进位加法、模不可约多项式乘法、Frobenius、子域、迹与范数、二元化矩阵，或判断某个扩域算术操作是否为 $\mathbb F_2$-线性时引用这里。
- 不要在当前笔记重复：具体 qudit Pauli/Clifford 形式、非 Clifford 门分类、扩域 CSS 码、Reed–Solomon／代数几何码以及 magic-state distillation 协议应由后续独立笔记承担。
- 边界：$\mathbb F_{2^s}$ 的抽象同构类型唯一，但基和不可约多项式给出的坐标表示并不典范；它的特征为 $2$，不能与整数剩余类环 $\mathbb Z/2^s\mathbb Z$ 混同。本文中的迹与范数默认指到 $\mathbb F_2$ 的绝对迹与绝对范数。
- 状态：已整理。

---
## 单项式对角比特门的 Clifford 层级

- 主笔记：[[对角相位门的Clifford层级]]，路径 `Notes/08-Binary Extension Field Non Clifford Module/对角相位门的Clifford层级.md`。
- 前置依赖：计算基、酉算符与共轭、比特 Pauli 算符、二进制变量及基本整数运算；有限域理论不是本公式证明的前置。
- 已有结论：对 $m\in\mathbb Z_{\ge1}$、$\boldsymbol a\in\mathbb F_2^n\setminus\{0\}$，门 $U_{m,\boldsymbol a}|\boldsymbol x\rangle=\exp(2\pi i\prod_{j:a_j=1}x_j/2^m)|\boldsymbol x\rangle$ 的最低 Clifford 层级为 $m+\operatorname{wt}(\boldsymbol a)-1$；主笔记给出 Pauli 共轭／相位差分的上界证明和排除更低层的证明。
- 写新内容时引用它：判断上述单项式相位门及 $Z,S,T,\mathrm{CZ},\mathrm{CS},\mathrm{CCZ}$ 的层级，或解释相位分母与支持大小如何共同决定层数时引用。
- 边界：采用通常的 $n$ 比特 Pauli 与 Clifford 层级，并忽略全局相位；$\boldsymbol a=0$ 只产生全局相位。相位函数在整数或模相位周期意义下计算，不能无条件改为 $\mathbb F_2$ 加法；层级编号不是电路深度或门数。本条不声称任意相位项乘积的最低层数必为各项最大值。
- 来源：S008 arXiv:2608.09727v1 §2.1 式 (1)；Cui–Gottesman–Krishna, *Diagonal gates in the Clifford hierarchy*, arXiv:1608.06596v1，§§II、IV（Theorem 3）。
- 状态：已整理。

---
## 二进制空间、补空间与正交补

- 主笔记：[[二进制空间性质]]，路径 `Notes/01-量子纠错基础/二进制空间性质.md`。
- 已有结论：直和补空间 $L$ 满足 $V=C\oplus L$，一般不唯一；正交补 $C^\perp=\{v:v\cdot c=0,\forall c\in C\}$ 唯一，但在 $\mathbb F_2^n$ 中不一定是 $C$ 的直和补空间，因为可能有非零 $v$ 满足 $v\cdot v=0$。
- 写新内容时引用它：涉及 CSS 码中的 $C_X\subset C_Z^\perp$、逻辑补空间选择、商空间或“正交补不是直和补”时引用这里，不再重讲线性代数例子。

---
## Chain complex、cochain complex 与 (co)homology

- 主笔记：[[Chain complex 与 cochain complex]]，路径 `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`。
- 前置依赖：向量空间、线性映射、kernel、image 与 quotient。
- 已有结论：Chain complex 的 differential 降低 degree，并满足
  $$
  \partial_i\partial_{i+1}=0,
  \qquad
  H_i(C)=\ker\partial_i/\operatorname{im}\partial_{i+1}.
  $$
  Cochain complex 的 coboundary 提高 degree，并满足
  $$
  \delta^{i+1}\delta^i=0,
  \qquad
  H^i(C)=\ker\delta^i/\operatorname{im}\delta^{i-1}.
  $$
  若 $C^i=\operatorname{Hom}(C_i,\mathbb F)$，则 chain differential 的对偶给出
  $$
  (\delta^if)(c)=f(\partial_{i+1}c),
  \qquad c\in C_{i+1}.
  $$
- 当前笔记只保留：chain/cochain 的 degree 方向、cycle/cocycle、boundary/coboundary、(co)homology quotient 与对偶来源。
- 写新内容时引用它：解释 degree、cycle/cocycle、boundary/coboundary、(co)homology quotient，或为 product complex 与 CSS cochain complex 提供基础术语时引用这里。
- 不要在当前笔记重复：CSS stabilizer、logical quotient 与 metacheck 的翻译放在 [[CSS码中的cochain complex]]；total-degree product differential 放在 [[Cochain complex 的 tensor product]]。
- 边界：量子码中的 cochain complex 可以直接由一串满足 $\delta^{i+1}\delta^i=0$ 的线性映射给出，不必先构造某个 chain complex 的对偶。
- 状态：已整理。

---
## CSS 码的 cochain complex 与 metacheck

- 主笔记：[[CSS码中的cochain complex]]，路径 `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`。
- 前置依赖：[[Chain complex 与 cochain complex]]、[[二进制空间性质]]，以及 check 矩阵按行保存 stabilizer support、Pauli support 使用列向量的约定。
- 已有结论：在本文采用的 $X$-check → qubit → $Z$-check convention 下，
  $$
  C^0=\mathbb F_2^{r_X},
  \qquad
  C^1=\mathbb F_2^n,
  \qquad
  C^2=\mathbb F_2^{r_Z},
  $$
  $$
  \delta^0=H_X^T,
  \qquad
  \delta^1=H_Z,
  \qquad
  \delta^1\delta^0=H_ZH_X^T=0.
  $$
  因而
  $$
  H^1(C)=\ker H_Z/\operatorname{im}H_X^T
  $$
  是 logical $X$ support classes。若再加入
  $$
  \delta^2=H_{\mathrm{meta}},
  \qquad
  H_{\mathrm{meta}}H_Z=0,
  $$
  则 $H_{\mathrm{meta}}$ 检查 $Z$-syndrome 之间的线性关系，不是新的 quantum stabilizer，并且
  $$
  H^2(C)=\ker H_{\mathrm{meta}}/\operatorname{im}H_Z
  $$
  衡量通过 metachecks、却不等价于实际 data-error syndrome 的 classes。
- 当前笔记只保留：CSS matrices 与 cochain maps 的对应、$H^1$ 的 logical-support quotient、metacheck 的 syndrome 含义，以及 logical quantities 必须对 coboundary representatives 不变的判据。
- 写新内容时引用它：把 CSS matrices 翻译成 cochain complex、识别 logical representatives、解释 metacheck，或判断某篇文献的 $H^1$ 表示 logical $X$ 还是 logical $Z$ 时引用这里。
- 不要在当前笔记重复：generic cochain 定义引用 [[Chain complex 与 cochain complex]]；CSS 陪集态证明引用 [[逻辑基态的表示]]；Menon 的具体 balanced-product matrices 引用 [[Tricycle complex 的 balanced-product 构造]]；physical $CCZ$ 判据引用 [[Symmetric triple cup-product]]。
- 边界：对偶 convention 会把 logical $Z$ classes 写成 $\ker H_X/\operatorname{im}H_Z^T$，所以不能只凭 $H^1$ 名称判断 Pauli 类型。存在 metacheck 不足以单独推出 single-shot；还需要 distance、soundness 与 decoder 条件。
- 状态：已整理。

---
## Tensor product 与 direct sum

- 主笔记：[[Tensor product 对 direct sum 的分配律]]，路径 `Notes/06-CCZ Distillation/Tensor product 对 direct sum 的分配律.md`。
- 应用接口：[[张量积与直和泛性质的 HGP-Künneth 接口]]，路径 `Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md`；它只整理“验证双线性规则—张量积线性化—直和拼接”在 HGP/Künneth 中的用法，不接管本条目的一般泛性质与分配律 ownership。
- 已有结论：固定域 $k$。若 $C=\bigoplus_i C^i$ 且 $D=\bigoplus_jD^j$，则 ordinary tensor product 有自然同构
  $$
  C\otimes_k D
  \cong
  \bigoplus_{i,j}C^i\otimes_k D^j.
  $$
  direct sum 的有限支撑条件保证分量展开是有限和。
- 写新内容时引用它：涉及普通 tensor product 对 direct sum 的分块时引用这里，不再重写 $\Phi,\Psi$ 的自然同构证明。若要使用 total degree、coboundary map 或 tensor-product complex，引用 [[Cochain complex 的 tensor product]]。
- 边界：这里是共同基域上的 ordinary tensor product；$\otimes_R$ 的 balanced relation 见 [[Balanced tensor product 与 coinvariant quotient]]。
- 状态：已整理。

---
## Cochain complex 的 tensor product

- 主笔记：[[Cochain complex 的 tensor product]]，路径 `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`。
- 前置依赖：[[Chain complex 与 cochain complex]] 和 [[Tensor product 对 direct sum 的分配律]]。
- 已有结论：对共同域 $k$ 上的 cochain complexes $C,D$，total degree 为
  $$
  (C\otimes_kD)^n
  =
  \bigoplus_{i+j=n}C^i\otimes_kD^j.
  $$
  对 homogeneous $c\in C^i$、$d\in D^j$，product coboundary 是
  $$
  \delta(c\otimes d)
  =
  \delta_Cc\otimes d+(-1)^i c\otimes\delta_Dd,
  \qquad
  \delta^2=0.
  $$
  在 $\mathbb F_2$ 上 $-1=1$，Koszul sign 消失。两个二项 complexes 给出三项 total complex；三个二项 complexes 的 degree-sector 数量是 $1,3,3,1$。
- 当前笔记只保留：total-degree decomposition、Koszul product differential、$\delta^2=0$ 的交叉项抵消，以及二项/三项 product 的 sector 计数。
- 写新内容时引用它：使用 total degree、product coboundary、Koszul sign，解释 tricycle 的 $1,3,3,1$ sectors，或进入 balanced product、cup product 与 ordinary integrated-Leibniz 推导时引用这里。
- 不要在当前笔记重复：ordinary tensor product 对 direct sum 的自然同构证明放在 [[Tensor product 对 direct sum 的分配律]]；product homology 的分解放在 [[Künneth 分解]]；module sidedness、coinvariant quotient 与 balanced relation 放在 [[Balanced tensor product 与 coinvariant quotient]]；Menon 的具体 $R\to R^3\to R^3\to R$ matrices 放在 [[Tricycle complex 的 balanced-product 构造]]。
- 边界：这里的 $\otimes_k$ 是 algebraic ordinary tensor product，不是 Hilbert-space tensor product，也不是 $\otimes_R$ balanced product。一般系数下必须保留 Koszul sign；无负号的 block matrices 只在 $\mathbb F_2$ convention 下使用。
- 状态：已整理。

---
## Künneth 分解

- 主笔记：[[Künneth 分解]]，路径 `Notes/07-Lifted-Product Code/Künneth 分解.md`。
- 前置依赖：[[Chain complex 与 cochain complex]] 中的 cycle、boundary 与 homology quotient，以及 [[Cochain complex 的 tensor product]] 中的 total degree 与 Koszul sign。
- 已有结论：比较映射
  $$
  \kappa_n:
  \bigoplus_{p+q=n}H_p(C)\otimes_kH_q(D)
  \longrightarrow H_n(C\otimes_kD),
  \qquad
  [c]\otimes[d]\longmapsto[c\otimes d]
  $$
  在域 $k$ 上是自然同构。证明把每个因子非典范地拆成零微分的同调代表元部分与可缩部分，并显式收缩所有含可缩因子的 tensor summands。对两个二项复形，
  $$
  H_1(\mathcal A\otimes_k\mathcal B)
  \cong
  \ker A\otimes_k\operatorname{coker}B
  \oplus
  \operatorname{coker}A\otimes_k\ker B,
  $$
  在 $\mathbb F_2$ 上取维数得到 $K=k_Ak_B^T+k_A^Tk_B$。PID 上的标准结论是含 $\operatorname{Tor}_1$ 的自然短正合列，其 splitting 一般不自然；一般交换环使用 bounded derived Künneth spectral sequence，不能把高阶 $\operatorname{Tor}$ 直接读成额外直和。
- 当前笔记只保留：比较映射的良定义、域上 complement/contracting-homotopy 证明、二项复形的 degree-$1$ 特化、PID 与一般环边界，以及 $R_2=\mathbb F_2[\varepsilon]/(\varepsilon^2)$ 上比较映射失败的反例。
- 写新内容时引用它：推导 HGP 逻辑比特数、解释 kernel/cokernel 两个逻辑扇区，或判断域上的 product-homology 公式能否用于 LP 时引用这里；只写 HGP／LP 校验矩阵、乘积方向、cyclic lift 或 S007 执行时不必先引用。
- 不要在当前笔记重复：product differential 平方为零引用 [[Cochain complex 的 tensor product]]；HGP blocks、CSS 对易和距离引用 [[Hypergraph product code]]；LP 的 balanced relation、环值 blocks 与二进制展开引用 [[Lifted product code]]。
- 边界：域上的 $\kappa_n$ 自然，但证明使用的链级补空间分裂不自然；“系数环不是域”只表示直接和公式不再自动成立，不表示每个实例必有非零 $\operatorname{Tor}$。非交换系数环还须固定右模与左模侧别。它不作为 HGP／LP 构造或 S007 分层执行的强制前置。
- 状态：已整理。

---
## Balanced tensor product 与 coinvariant quotient

- 主笔记：[[Balanced tensor product 与 coinvariant quotient]]，路径 `Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md`。
- 前置依赖：读者应先知道 ordinary tensor product 和 [[Cochain complex 的 tensor product]] 中的 total degree、product coboundary。
- 已有结论：对含幺结合 $k$-algebra $R$、右模 $M_R$ 与左模 ${}_RN$，
  $$
  M_R\otimes_R{}_RN
  =
  \frac{M\otimes_kN}
  {\langle(mr)\otimes n-m\otimes(rn)\rangle}.
  $$
  若 $M$ 还是 $(S,R)$-bimodule ${}_S M_R$，而 $N$ 是 $(R,T)$-bimodule ${}_R N_T$，则中间的 $R$-作用用于 balanced quotient，两个外侧作用使
  $$
  {}_S M_R\otimes_R{}_R N_T
  $$
  成为 $(S,T)$-bimodule。
  若 $R=k[G]$，则同一个对象也是 anti-diagonal action
  $$
  g\cdot(m,n)=(mg^{-1},gn)
  $$
  的 coinvariant quotient：
  $$
  M_R\otimes_{k[G]}{}_RN
  \cong
  (M\otimes_kN)_G.
  $$
  若有限群 $H$ 通过 degree-preserving cochain automorphisms 作用在 cochain complex $M$ 上，则
  $$
  \delta^p(W_H^p)\subseteq W_H^{p+1},
  \qquad
  \delta_H^p([v]_H)=[\delta^pv]_H,
  $$
  所以 coinvariant quotient $M_H$ 仍是 cochain complex；这一结论不要求 basis-preserving 或 free action。
  Balanced/coinvariant quotient 先改变 cochain complex 本身，cohomology quotient 随后在新 complex 内取 cocycles modulo coboundaries；一般没有
  $$
  H^\ast(M_H)\cong (H^\ast M)_H.
  $$
  三重 product 需要 $M_R,{}_RN_R,{}_RP$；两个 interfaces 合成 $G^2$-作用
  $$
  (g,h)\cdot(m_1,m_2,m_3)
  =
  (m_1g^{-1},gm_2h^{-1},hm_3).
  $$
  对 regular basis $G^3$，该作用自由，orbits 由有序乘积 $g_1g_2g_3$ 标记。Regular bimodule 的乘法同构
  $$
  R\otimes_RR\otimes_RR\cong R
  $$
  只需要结合律，不需要 $R$ 交换。
- 当前笔记只保留：right/left module 类型、balanced relation、anti-diagonal coinvariants、balanced-product complex、三重 bimodule interfaces、regular-module orbit 与乘法同构。
- 写新内容时引用它：定义 balanced product、解释 balanced product 与 coinvariant quotient 是同一构造、使用 $G^2$ interfaces、或区分 balanced quotient 与 cohomology quotient 时引用这里。
- 边界：Balanced quotient 的定义不需要 free action；free basis action 只用于 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]] 中的 averaging transport。
- 状态：已整理。

---
## Hypergraph product code

- 主笔记：[[Hypergraph product code]]，路径 `Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 前置依赖：[[Chain complex 与 cochain complex]]、[[CSS码中的cochain complex]] 与 [[Cochain complex 的 tensor product]]；固定 chain convention $H_X=\partial_1,H_Z=\partial_2^T$，其对偶是本库 $H_X^T\to H_Z$ 的 cochain convention。只有逻辑空间的两个扇区及简洁维数公式把 [[Künneth 分解]] 作为可选依赖。
- 已有结论：对
  $$
  A\in\mathbb F_2^{m_A\times n_A},
  \qquad
  B\in\mathbb F_2^{m_B\times n_B},
  $$
  两个二项 chain complexes 的 product 中间项是
  $$
  C_1=\mathbb F_2^{n_Am_B}\oplus\mathbb F_2^{m_An_B},
  $$
  并给出
  $$
  H_X=[A\otimes I_{m_B}\mid I_{m_A}\otimes B],
  \qquad
  H_Z=[I_{n_A}\otimes B^T\mid A^T\otimes I_{n_B}],
  $$
  $$
  H_XH_Z^T=A\otimes B+A\otimes B=0.
  $$
  若 $k_A=\dim\ker A$、$k_A^T=\dim\ker A^T$，并类似定义 $B$ 的记号，则
  $$
  N=n_Am_B+m_An_B,
  \qquad
  K=k_Ak_B^T+k_A^Tk_B.
  $$
  $A,B$ 的行重和列重统一有界时才得到 qLDPC family。等尺度、线性经典距离的标准选择可给出常数率和 $d=\Theta(\sqrt N)$；这不是任意 HGP 输入的统一距离公式。
- 当前笔记只保留：二项 product complex 到 CSS blocks 的转换、两个 physical-qubit sectors、与 S007 式 (1) 的 convention 转换、四类 Tanner 边、行／列一维分解，以及 $N/K$ 和标准平方根距离基准。
- 写新内容时引用它：出现 HGP blocks、乘积坐标、四类边、row/column decomposition、product-slice logical、HGP 与 LP/GB/surface code 的关系，或把 $\sqrt N$ 作为乘积码距离基准时引用这里。
- 不要在当前笔记重复：一般 product differential 引用 [[Cochain complex 的 tensor product]]；Künneth 同构及其 kernel/cokernel 推导引用 [[Künneth 分解]]；CSS logical quotient 引用 [[CSS码中的cochain complex]]；群坐标的 balancing 引用 [[Balanced tensor product 与 coinvariant quotient]]。
- 状态：已整理。

---
## Lifted product code

- 主笔记：[[Lifted product code]]，路径 `Notes/07-Lifted-Product Code/Lifted product code.md`。
- 前置依赖：[[Hypergraph product code]]、[[Balanced tensor product 与 coinvariant quotient]] 与 [[CSS码中的cochain complex]]；[[Künneth 分解]] 只用于逻辑维数与一般系数同调边界。循环 lift 使用 $Pe_t=e_{t+1}$，所以 $x^s\mapsto P^s$ 表示 $v_t\leftrightarrow c_{t+s}$。
- 已有结论：在最常见的交换情形，$R$ 是具有 transpose-compatible involution 的有限维 $\mathbb F_2$-代数，$A\in R^{m_A\times n_A}$、$B\in R^{m_B\times n_B}$。在 $R$ 上取两个二项 complexes 的 balanced tensor product，并令
  $$
  \widehat H_X=[A\otimes I_{m_B}\mid I_{m_A}\otimes B],
  \qquad
  \widehat H_Z=[I_{n_A}\otimes B^*\mid A^*\otimes I_{n_B}].
  $$
  因 $A,B$ 的系数交叉对易、$\mathbb B(M^*)=\mathbb B(M)^T$，二进制展开
  $$
  H_X=\mathbb B(\widehat H_X),
  \qquad
  H_Z=\mathbb B(\widehat H_Z)
  $$
  满足 CSS 对易。若 $\dim_{\mathbb F_2}R=\ell$，则
  $$
  N=\ell(n_Am_B+m_An_B),
  \qquad
  K=N-\operatorname{rank}_{\mathbb F_2}H_X-\operatorname{rank}_{\mathbb F_2}H_Z.
  $$
  一般没有统一的简洁 $K$ 公式；对 QC 特例 $B=[1+x]$，
  $$
  K=\dim_{\mathbb F_2}\ker A(1)
  +\dim_{\mathbb F_2}\ker\!\bigl(A(1)^T\bigr).
  $$
  当 $R=\mathbb F_2[G]$ 且选定基上的群作用相容、自由时，$\otimes_R$ 等价于 expanded HGP complex 对
  $$
  h\cdot(g_1,g_2)=(g_1h^{-1},hg_2)
  $$
  的 anti-diagonal quotient，长度由 $\ell^2Q$ 降为 $\ell Q$。非阿贝尔情形在抽象层分别使用自由 right/left $R$-modules，满足 $(ua)\otimes v=u\otimes(av)$；二进制层按原论文 Appendix B 单独采用 $A\mapsto(\rho_a)$、$B\mapsto(\lambda_b)$ 的块替换，其中 $\rho_a(u)=ua$、$\lambda_b(u)=bu$ 只是 $\mathbb F_2$-线性块，CSS 对易来自 $\rho_a\lambda_b=\lambda_b\rho_a$。
- 当前笔记只保留：HGP outer product 与 inner lift 的区分、循环 lift 的可核对例子、反对合与二进制展开、LP 块矩阵、自由反对角 quotient、QC $1+x$ 特例、距离直觉、已证明的渐近参数和解码适用范围。
- 写新内容时引用它：解释 base edge 与 lift label、使用 QC/QA/非阿贝尔 lifted product、比较 expanded HGP 与 LP 长度、解释近线性或渐近良好 qLDPC 码族，或讨论 LP 解码时引用这里。
- 不要在当前笔记重复：域上 product homology 与一般环的 Künneth 边界引用 [[Künneth 分解]]；HGP 的完整推导引用 [[Hypergraph product code]]；一般 balanced relation 和 coinvariant quotient 引用 [[Balanced tensor product 与 coinvariant quotient]]；三因子构造引用 [[Tricycle complex 的 balanced-product 构造]]。
- 边界：LP 只自动保证相容条件下的 CSS 构造。只有二进制行重和列重统一有界时才是 qLDPC；低重量 stabilizers 不自动给出二维几何局域性；近线性距离、线性距离与解码保证都属于附带扩张性等假设的特定子族。
- 状态：已整理。

---
## S007 中 LP 码的分层执行

- 主笔记：[[S007 中 LP 码的分层执行]]，路径 `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`。
- 前置依赖：[[Hypergraph product code]] 中的乘积坐标、四类边与行／列分解，以及 [[Lifted product code]] 中 outer product／inner lift、循环环和 $x^k$ shift convention。
- 已有结论：S007 arXiv v1 第 6 节把式 (2) 的 $3\times7$ 单项式 seed base matrix、$\ell=45$ 的 lift 和图 12 的 lift-level graph 接到四阶段执行：提升间重排、提升内重排、门执行、定向转移。每个单项式只作为一条已给 base edge 的 cyclic-shift label；表 3 的时间分解只验证该实例分别统计这些执行层级。
- 当前笔记只保留：S007 论文特例中的 outer product、inter-lift、intra-lift 与硬件执行接口，不承担一般 LP 定义。
- 写新内容时引用它：解释 S007 第 6 节、式 (2)、图 12 或该实例的分层执行时引用这里；一般 LP blocks 与 lift 代数仍引用 [[Lifted product code]]。
- 来源关系：[S007 全文译本](Translations/S007.full.zh-CN.md) §2.2、图 1、§3.1、§6、式 (2)、图 12 与表 3；[S007 本地 PDF](Papers/S007_2026_Liu_architecture_compilation_codesign.pdf) pp.12–13，版本为 arXiv v1。
- 边界：S007 只展示矩阵 $A$，没有给出可供本库重建完整 LP 两因子数据与 data／$X$-check／$Z$-check sector 映射的第二因子；$[\![2610,744,d\le16]\!]$ 是来源给定参数，不在这里推导。图 12 的 node roles、diagonal parking 和性能结果都是论文实例信息。
- 状态：已整理。

---
## Tricycle balanced-product cochain complex

- 主笔记：[[Tricycle complex 的 balanced-product 构造]]，路径 `Notes/06-CCZ Distillation/Tricycle complex 的 balanced-product 构造.md`。
- 前置依赖：读者应先知道 [[Cochain complex 的 tensor product]] 中的 total degree 与 product coboundary、[[Balanced tensor product 与 coinvariant quotient]] 中的三重 interfaces 与 regular-module 乘法同构，以及 [[CSS码中的cochain complex]] 中 $H_X,H_Z$ 与 cochain maps 的 row/column convention。
- 已有结论：Menon 取有限 Abelian 群 $G$ 和交换群代数 $R=\mathbb F_2[G]$。Seed maps
  $$
  \delta_x(r)=xr,\qquad x\in\{a,b,c\},
  $$
  总是右 $R$-linear，并因 $R$ 交换而同时左 $R$-linear。三个二项 seed complexes 的三重 balanced product 给出
  $$
  R\xrightarrow{\delta^0}R^3\xrightarrow{\delta^1}R^3\xrightarrow{\delta^2}R,
  $$
  其中
  $$
  \delta^0=\begin{bmatrix}a\\ b\\ c\end{bmatrix},\qquad
  \delta^1=
  \begin{bmatrix}
  c&0&a\\
  0&c&b\\
  b&a&0
  \end{bmatrix},\qquad
  \delta^2=\begin{bmatrix}b&a&c\end{bmatrix}.
  $$
  在 coefficient-column convention 下，$B_G(x)$ 表示左乘 $r\mapsto xr$，而
  $$
  \delta^0=H_X^T,
  \qquad
  \delta^1=H_Z,
  \qquad
  \delta^2=H_{\mathrm{meta}}.
  $$
  因此 $H_X=[A^T\ B^T\ C^T]$ 中的转置来自 CSS row/column convention，而不是左右 regular action 的转换。
- 当前笔记只保留：Menon Abelian specialization、seed-map side compatibility、$1,3,3,1$ sectors、四项 complex、regular-representation convention 与 CSS/metacheck 对应。
- 写新内容时引用它：使用 Menon 的 $H_X,H_Z,H_{\mathrm{meta}}$、解释 metacheck 来源、或需要 $C^0\to C^1\to C^2\to C^3$ 对象对应时引用这里。
- 边界：该笔记只构造 code complex；logical $CCZ$ 还需要 inherited operation、integrated Leibniz 与 [[Symmetric triple cup-product]]。
- 状态：已整理。

---
## Cup product 与 Leibniz rule

- 主笔记：[[Cup product 与 Leibniz rule]]，路径 `Notes/06-CCZ Distillation/Cup product 与 Leibniz rule.md`。
- 前置依赖：读者应先知道 [[Chain complex 与 cochain complex]] 中的 $C^i,\delta^i$、cocycle/coboundary 和 quotient，以及 [[Cochain complex 的 tensor product]] 中的 degree 与 Koszul sign 约定。需要 physical-support 解释时再读 [[CSS码中的cochain complex]]。
- 已有结论：cochain complex 本身只给出 $C^i$ 和 $\delta^i$；cup product 是额外的双线性乘法
  $$
  \cup:C^p\times C^q\to C^{p+q}.
  $$
  一般系数下的 Leibniz rule 为
  $$
  \delta(x\cup y)=(\delta x)\cup y+(-1)^p x\cup(\delta y),
  \qquad x\in C^p.
  $$
  在 $\mathbb F_2$ 系数下简化为
  $$
  \delta(x\cup y)=(\delta x)\cup y+x\cup(\delta y)
  $$
  保证 cocycle 的乘积仍是 cocycle，并保证某个 representative 改变一个 coboundary 时，乘积只改变一个 coboundary；因此 $[x]\cup[y]=[x\cup y]$ 在 cohomology 上良定义。若乘法不结合，多重 cup product 必须先固定括号。固定括号的多重乘积落在 $C^q$ 后，取线性泛函
  $$
  \lambda:C^q\to\mathbb F_2
  $$
  只有在
  $$
  \lambda(\operatorname{im}\delta^{q-1})=0
  $$
  时才给出不依赖 degree-$q$ cohomology representative 的数值读数；在选择这样的 $\lambda$ 以前，三个 $1$-cochains 的乘积仍只是 $C^3$ cochain。
- 当前笔记只保留：cup product 的 degree、Leibniz rule、固定括号的多重乘积、cocycle 与 representative invariance，以及一般线性泛函如何把 cohomology class 读成标量。
- 写新内容时引用它：讨论 cup product 如何在 cohomology 上良定义、固定非结合乘积的括号，或解释 degree-$q$ cochain 何时能由一般 $\lambda$ 读成 representative-independent 标量时引用这里。
- 不要在当前笔记重复：classical two-term complex 的 in/out/free preorientation、seed parity integral 与 ordinary tensor-product integrated Leibniz 放在 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]；balanced quotient 上的 inherited operation 放在 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；Menon 的具体 $\int_R$、position-dependent symmetric bracketing 和 physical-basis $CCZ$ 判据放在 [[Symmetric triple cup-product]]。
- 边界：这里的 $\lambda$ 是一般 cohomology 数值读数；“integral”在具体构造中还可能承担额外的乘积相位解释。本文不证明 Menon 的 preorientation constraints 或 integrated-Leibniz 条件。
- 状态：已整理。

---
## Preorientation 与 ordinary tensor product 上的 integrated Leibniz

- 主笔记：[[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]，路径 `Notes/06-CCZ Distillation/Preorientation 与 ordinary tensor product 上的 integrated Leibniz.md`。
- 前置依赖：读者应先知道 [[Cochain complex 的 tensor product]] 中的 total degree、product coboundary 与 Koszul sign，以及 [[Cup product 与 Leibniz rule]] 中 fixed-bracketing product 和 representative 改变如何产生 coboundary。应用到量子码时，再使用 [[CSS码中的cochain complex]] 对 $C^1$ 与 $H^1(C)$ 的解释。
- 已有结论：对 classical two-term complex
  $$
  C^0(X;\mathbb F_2)\xrightarrow{\delta}C^1(X;\mathbb F_2),
  $$
  记 $N(u)=\operatorname{supp}(\delta u)$。Preorientation 是 disjoint decomposition
  $$
  N(u)=N_{\mathrm{in}}(u)\sqcup N_{\mathrm{out}}(u)\sqcup N_{\mathrm{free}}(u),
  $$
  并定义 mixed-degree local product
  $$
  u\cup x=x\ \text{if }x\in N_{\mathrm{out}}(u),
  \qquad
  x\cup u=x\ \text{if }x\in N_{\mathrm{in}}(u),
  $$
  否则为 $0$。$N_{\mathrm{free}}$ 不进入这两条局部读数，但进入 integrated Leibniz 的完整 coboundary 检查。对 $\ell$ 个 two-term seeds，本文采用 $\ell$-ary local product，并在 ordinary tensor product 的 top degree $\ell$ 上取 product integral。各 seed 的 check support 为偶重量时，seed parity integral 杀掉 coboundaries；各 seed 的 $\ell$-ary local product 满足 integrated-Leibniz identity 时，ordinary tensor product 继承相同 identity。两组条件共同保证数值函数
  $$
  F_{\underline C}(z_1,\ldots,z_\ell)
  =
  \int_\ell z_1\cup\cdots\cup z_\ell
  $$
  对 $z_m\mapsto z_m+\underline\delta a_m$ 不变，因此下降到 $H^1(\underline C)^{\times\ell}$。
- 当前笔记只保留：parity integral、in/out/free 局部读数、position-dependent 多重乘积、seed support-parity 判据、定向图例子、ordinary tensor-product fixed-factor 继承证明，以及 integrated Leibniz 推出 cohomology representative invariance 的一般消去引理。
- 写新内容时引用它：解释 preorientation 是否改变 code、free part 为什么仍需检查、ordinary tensor product 怎样继承 integrated Leibniz，或使用一般 representative-invariance 消去引理时引用这里。
- 不要在当前笔记重复：balanced quotient 的 invariants/coinvariants、averaging/orbit-sum 和 inherited product；这些放在 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]。Balanced tensor 与 anti-diagonal quotient 的定义放在 [[Balanced tensor product 与 coinvariant quotient]]。Menon 的具体 bracketing 与 physical $CCZ$ 判据放在 [[Symmetric triple cup-product]]。
- 边界：本文在 $\mathbb F_2$ 上展开 fixed-factor 证明；一般系数下需要恢复 Koszul signs。Integrated Leibniz 是积分后的条件，不等于完整 cochain-level Leibniz；它是当前 representative-invariance 证明的充分条件，不是已经证明的必要条件。
- 状态：已整理。

---
## Balanced quotient 上的 inherited product 与 integrated Leibniz

- 主笔记：[[Balanced quotient 上的 inherited product 与 integrated Leibniz]]，路径 `Notes/06-CCZ Distillation/Balanced quotient 上的 inherited product 与 integrated Leibniz.md`。
- 前置依赖：读者应先知道 [[Balanced tensor product 与 coinvariant quotient]] 中 $M_H$ 的来源，以及 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]] 中的 ordinary multilinear operation、integral 和 integrated Leibniz。
- 已有结论：若有限群 $H$ 通过 basis-preserving cochain automorphisms 作用，则非归一化 orbit-sum map 为
  $$
  \operatorname{avg}([m]_H)=\sum_{h\in H}h\cdot m
  $$
  在 basis orbit $O_x$ 对应的一维 summand 上是乘以
  $$
  s_x=|\operatorname{Stab}_H(x)|1_k.
  $$
  因此 averaging 是 cochain-complex isomorphism，当且仅当 $s_x\ne0$ 对所有 degrees 的所有 basis orbits 成立；degreewise free action 给出 $s_x=1$，是不依赖 $\operatorname{char}k$ 的充分条件。关于共同 $H$-作用等变的 $m$-linear map $\mu$ 可由
  $$
  \mu_H
  =
  \operatorname{avg}^{-1}
  \circ\mu\circ
  \operatorname{avg}^{\times m}
  $$
  定义 coinvariants 上的 operation；展开后是所有 relative translates 的 classes 之和，其中 identity-translate 项只是 $[\mu(y_1,\ldots,y_m)]_H$。若 $\mu$ 在每个 argument 上分别尊重 coinvariant relations，使 representativewise operation $\mu_H^{\mathrm{dir}}$ 良定义，则
  $$
  \mu_H
  =
  \bigl(|H|^{m-1}1_k\bigr)\mu_H^{\mathrm{dir}}.
  $$
  特别地，$m=1$ 时两者相等。因此 direct descent 与 averaging transport 不能混同。关于 $H$-作用不变的 integral 则直接下降为
  $$
  \lambda_H([v]_H)=\lambda(v),
  $$
  并满足
  $$
  \lambda\circ\operatorname{avg}
  =
  (|H|1_k)\lambda_H.
  $$
  因此 $\lambda_H$ 一般不等于 $\lambda\circ\operatorname{avg}$。在当前 $\mathbb F_2$ 无符号约定下，若 ordinary $(\mu,\lambda)$ 满足 integrated Leibniz，则对每个固定 relative-translate tuple 调用 ordinary identity，得到 inherited $(\mu_H,\lambda_H)$ 的 integrated Leibniz；该证明不产生 $|H|$ 因子。若 $z_i\in Z^{p_i}(M_H)$，$\mu_H$ 为 degree-additive，并且 $q=\sum_i p_i$ 是 $\lambda_H:(M_H)^q\to k$ 读取的 degree，则
  $$
  F_H(z_1,\ldots,z_m)
  =
  \lambda_H\mu_H(z_1,\ldots,z_m)
  $$
  在相应 integrated-Leibniz 假设下诱导
  $$
  \bar F_H:
  \prod_{i=1}^m H^{p_i}(M_H)
  \longrightarrow k,
  $$
  因而只依赖各 arguments 的 cohomology classes。Menon 的 $H=G^2$ regular-basis action 满足 free-action 假设，group-algebra augmentation 满足不变性；具体 trilinear $CCZ$ 应用见 [[Symmetric triple cup-product]]。
- 当前笔记只保留：basis-orbit averaging 的可逆判据、relative-translate inherited operation、invariant integral 的直接下降、direct descent 与 averaging transport 的区别，以及二者共同继承 integrated Leibniz 的一般证明。
- 写新内容时引用它：解释 orbit sum、representativewise direct descent 需要的逐 argument 条件、它与 averaging relative-translate operation 的区别、free group action 的用途、invariant functional 为什么下降，或 local integrated Leibniz 怎样继承到 balanced complex 时引用这里。
- 不要在当前笔记重复：balanced relation 与 $G^2$ interfaces 放在 [[Balanced tensor product 与 coinvariant quotient]]；四项 complex 与矩阵 entries 放在 [[Tricycle complex 的 balanced-product 构造]]；seed support-parity 推导放在 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]；Menon 的 preorientation sufficient conditions、physical-basis $CCZ$ formula 与 logical connectivity tensor 放在 [[Symmetric triple cup-product]]。
- 边界：Balanced quotient 本身不要求 free action；free action 只保证本构造中的 averaging 是同构。当前 integrated-Leibniz 展开使用 $\mathbb F_2$ 的无符号公式；一般系数需恢复相应 Koszul signs。本文不假设 $H^\ast(C_H)=(H^\ast C)_H$。
- 状态：已整理。

---
## Symmetric triple cup-product 与 logical CCZ

- 主笔记：[[Symmetric triple cup-product]]，路径 `Notes/06-CCZ Distillation/Symmetric triple cup-product.md`。
- 前置依赖：读者应先知道 [[Tricycle complex 的 balanced-product 构造]] 中的四项 complex、$C^1=R^3$ sector 结构、$H^1(C)=\ker\delta^1/\operatorname{im}\delta^0$；[[Cup product 与 Leibniz rule]] 中 representative 改变如何产生 coboundary；[[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]] 中的 integral、in/out/free 局部读数和 seed integrated Leibniz；以及 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]] 中的 relative-translate inherited operation、自由 $G^2$-作用与 augmentation。若读者卡在 module tensor、anti-diagonal quotient 或三重 interfaces，应先读 [[Balanced tensor product 与 coinvariant quotient]]。
- 已有结论：physical $CCZ$ circuit 可由三线性 $0/1$ 选择函数
  $$
  f_{\mathrm{CCZ}}:C^1\times C^1\times C^1\to\mathbb F_2
  $$
  表示。它要成为良定义的 logical gate，必须对 coboundary 方向消失；例如对 $u\in C^0$ 和 $y,z\in\ker\delta^1$，
  $$
  f_{\mathrm{CCZ}}(\delta^0u,y,z)=0,
  $$
  另外两条输入腿同理。这样才能诱导
  $$
  \bar f_{\mathrm{CCZ}}:H^1(C)^{\times3}\to\mathbb F_2.
  $$
  在 Menon complex 中，total degree 为 $3$ 的部分是 $C^3=R$，STCP 使用
  $$
  \int_R\left(\sum_{g\in G}r_g\,g\right)=\sum_{g\in G}r_g\pmod2
  $$
  把三重 cup product 读成 $\mathbb F_2$ 数。若 $\mu_C:C^{\times3}\to C$ 是 balanced complex 上 inherited symmetric trilinear operation，则
  $$
  f_{\mathrm{CCZ}}
  =
  \lambda_C\circ\left.\mu_C\right|_{(C^1)^{\times3}},
  \qquad
  \lambda_C=\int_R.
  $$
  $\mu_C$ 的 relative-translate construction、$\lambda_C$ 的 invariant descent 以及 integrated Leibniz 的继承统一引用 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；Menon 在此基础上指定 local products、sector rules 与 preorientation conditions，进而得到 $f_{\mathrm{CCZ}}$。
  Symmetric local product 的 degree rule 使 nonzero physical basis triples 必须分别来自 sectors $100,010,001$，次序任意；重复 sectors 仍属于 domain，但被送到 $0$。因此 physical formula 带有 pairwise-distinct indicator $\mathbf 1_{\mathrm{pd}}(i,j,k)$。
  对 ordered arguments $(p_i,q_j,r_k)$，degree-$0$ argument 位于唯一 degree-$1$ argument 左侧时读取 out、位于右侧时读取 in。Internal factors $C_{\alpha_i},C_{\alpha_j},C_{\alpha_k}$ 的 local degree patterns 依次为 $(1,0,0),(0,1,0),(0,0,1)$，所以按 group coordinate 收集得到
  $$
  \beta_r
  =
  r\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}},
  \qquad
  \beta_q
  =
  q\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}},
  \qquad
  \beta_p
  =
  p\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}.
  $$
  于是
  $$
  f_{\mathrm{CCZ}}(p_i,q_j,r_k)
  =
  \mathbf 1_{\mathrm{pd}}(i,j,k)
  \sum_{h\in G}
  \operatorname{coeff}_h(\beta_r)
  \operatorname{coeff}_h(\beta_q)
  \operatorname{coeff}_h(\beta_p)
  \pmod2,
  $$
  等价地读取三个 $\beta$ supports 的三重交集奇偶。
  当 $\alpha^{\mathrm{free}}=0$ 时，记
  $$
  I_t=\operatorname{supp}(\alpha^{\mathrm{in}}t),
  \qquad
  O_t=\operatorname{supp}(\alpha^{\mathrm{out}}t).
  $$
  Local integrated-Leibniz 左端在 basis triple $(u_f,u_g,u_h)$ 上化为
  $$
  |I_f\cap I_g\cap I_h|
  +
  |O_f\cap O_g\cap O_h|
  \pmod2.
  $$
  $f,g,h$ 全相等、恰取两个不同 group elements、两两不同这三种 equality patterns 分别给出 weight、pair-overlap、triple-overlap conditions；共同右平移把第一个 label 归一化为 $e$。
  对三块 code 的 logical $X$ bases，
  $$
  T_{\mu\nu\rho}^{\mathrm{log}}
  =
  \bar f_{\mathrm{CCZ}}
  ([l_\mu^{(1)}],[l_\nu^{(2)}],[l_\rho^{(3)}])
  $$
  因 coboundary invariance 而不依赖 representatives；这只保证 $T^{\mathrm{log}}$ 良定义，不保证它非零。
- 当前笔记只保留：physical $CCZ$ 选择函数、$C^3=R$ 上的 $\int_R$、symmetric integrated Leibniz/coboundary invariance、sector 与 preorientation 如何进入 physical-basis 判据，以及 logical connectivity tensor 的来源。
- 写新内容时引用它：讨论 Menon 的 STCP physical $CCZ$ circuit、coboundary invariance、physical hyperedge 判据或 logical connectivity tensor $T^{\mathrm{log}}$ 时引用这里。不要在 hypergraph magic state、subrank 或 single-shot factory 笔记中重新证明 $f_{\mathrm{CCZ}}$ 为什么能下降到 $H^1$。
- 不要在当前笔记重复：balanced/coinvariant quotient、averaging、relative translates 与 invariant integral 的下降证明引用 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；一般 cup product 与 $\lambda$ 读数引用 [[Cup product 与 Leibniz rule]]；generic preorientation 与 ordinary inheritance 引用 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]。
- 边界：这里的 “symmetric” 只表示括号随唯一 degree-$1$ argument 的位置改变，不表示三个 arguments 具有 permutation symmetry。上述 weight/pair/triple-overlap 化简只适用于 $\alpha^{\mathrm{free}}=0$；free part 非空时必须使用完整 in/out/free constraints。该笔记不负责 single-shot preparation、decoder soundness、scheduled depth 或 $K_{\mathrm{CCZ}}$ subrank。
- 状态：已整理。

---
## Menon Magic Tricycles 的 single-shot CCZ factory

- 主笔记：[[Menon 2025 Magic Tricycles]]，路径 `Notes/06-CCZ Distillation/Menon 2025 Magic Tricycles.md`。
- 前置依赖：[[CSS码中的cochain complex]] 中的 logical $X$ quotient 与 metacheck、[[Tricycle complex 的 balanced-product 构造]] 中的四项 complex，以及 [[Symmetric triple cup-product]] 中的 physical $CCZ$ 判据与 logical connectivity tensor。资源态的消费方式见 [[State injection]]。
- 已有结论：该方案不是从 noisy input magic states 得到更少、更干净输出的传统 $n\to k$ distillation。其 factory 骨架是：用 $Z$-syndrome metachecks、single-shot distance 与 soundness 准备三块 tricycle code 的 logical $|+\rangle_L^{\otimes K}$；施加 bounded-degree physical $CCZ$ circuit；得到由 $T^{\mathrm{log}}$ 指定的 logical hypergraph magic state。若 $T^{\mathrm{log}}$ 含有大小为 $K_{\mathrm{CCZ}}$ 的 identity-like diagonal subtensor，便可抽取相应数量的互不重叠 $|CCZ\rangle$ resources。STCP 提供解析的 $CCZ$ hyperedge construction；Numerical Leibniz Rule 直接搜索 group-equivariant trilinear functions，可能降低 circuit degree，但不对任意 code 保证低-degree 解。
- 当前笔记只保留：论文版本与作者约定、code construction、physical $CCZ$、state preparation 三部分如何组成完整 factory、STCP 与 NLR 的分工、论文报告的 finite-block 参数与模拟证据，以及与传统 distillation 的资源口径差异。
- 写新内容时引用它：介绍或比较 Menon qLDPC $CCZ$ factory，引用论文的 $N,K,D,K_{\mathrm{CCZ}}$、maximum degree / schedule、single-shot 或 simulation 结果，或讨论 logical hypergraph resource 的完整协议语境时引用这里。与传统 code-space distillation 或 compact $CCZ$ factory 比较时，分别外链 [[Distillation protocol]] 与 [[SAT搜索紧凑蒸馏工厂]]。
- 不要在当前笔记重复：$H_X,H_Z,H_{\mathrm{meta}}$ 的矩阵推导归 [[Tricycle complex 的 balanced-product 构造]]；balanced quotient、preorientation、inherited product 与 integrated-Leibniz 证明沿 [[Symmetric triple cup-product]] 的上游链路引用；physical hyperedge 公式与 coboundary invariance 归 [[Symmetric triple cup-product]]。
- 边界：maximum degree 不等于实际 scheduled depth；文中 $K_{\mathrm{CCZ}}$ 是 MIP 找到的 tensor-subrank 下界，不是最优值证明；现有 circuit-level simulation 主要是 syndrome-extraction/memory proxy，不是完整 logical-$CCZ$ fidelity simulation；selective logical initialization 与向 computation code teleport 仍是架构问题；严格 single-shot soundness 只覆盖特定条件，不能把更广的数值证据写成普遍定理。
- 状态：已整理。

---
## 逻辑基态的陪集、投影与仿射支撑

- 主笔记：[[逻辑基态的表示]]，路径 `Notes/01-量子纠错基础/逻辑基态的表示.md`。
- 已有结论：只有 $X$ 稳定子时，逻辑基态是陪集态
  $$
  |C+t\rangle=\frac1{\sqrt{|C|}}\sum_{c\in C}|c\oplus t\rangle.
  $$
  CSS 码中逻辑信息由商空间 $C_Z^\perp/C_X$ 标记，逻辑基态可写成
  $$
  |\overline{x}\rangle
  =
  \frac1{\sqrt{|C_X|}}
  \sum_{c\in C_X}|c\oplus t(x)\rangle.
  $$
  一般稳定子逻辑基态可由稳定子和逻辑 $Z$ 的投影算符唯一给出；指定逻辑 $Z$ 本征值后得到最大稳定子态，其计算基支撑是仿射子空间
  $$
  \operatorname{supp}(\psi)=t+A,
  \qquad
  |\psi\rangle=\frac1{\sqrt{|A|}}\sum_{a\in A}q(a)|t\oplus a\rangle.
  $$
- 写新内容时引用它：凡是需要“逻辑基态是陪集态”“CSS 逻辑空间是 $C_Z^\perp/C_X$”“一般稳定子态支撑为仿射子空间”时引用这里。只有在当前协议要代入具体 $C_X,C_Z,A,t_x$ 时才写展开式。
- 边界：$D=A^\perp$ 的证明依赖最大稳定子态维数 $\dim M=n$；只对 code stabilizer 一般只能得 $D\subseteq A^\perp$。

---
## 稳定子态的二次相位

- 主笔记：[[逻辑基态的二次相位]]，路径 `Notes/02-Clifford与稳定子形式/逻辑基态的二次相位.md`。
- 已有结论：一般稳定子态的相位可写为 $q(a)=i^{Q(a)}$，其中
  $$
  Q(a)=c+\sum_i\lambda_i a_i+2\sum_{i<j}\mu_{ij}a_ia_j\pmod4.
  $$
  常数项是整体相位；一次项对应单比特 Clifford 相位；二次项只能是 $CZ$ 型 $(-1)^{a_i a_j}$，不能出现 controlled-$S$ 型二次非 Clifford 相位。
- 写新内容时引用它：分析一般稳定子态计算基相位、解释“稳定子相位最多是一次加 $CZ$ 型二次项”时引用这里，不再从 Pauli 稳定子递推相位函数。

---
## 汉明重量展开与 XOR 多项式

- 主笔记：[[汉明重量展开]]，路径 `Notes/05-Magic State Distillation/汉明重量展开.md`。
- 已有结论：多比特 XOR 可作为整数多项式展开，
  $$
  x_1\oplus\cdots\oplus x_n
  =
  \sum_i x_i
  -2\sum_{i<j}x_ix_j
  +4\sum_{i<j<k}x_ix_jx_k-\cdots.
  $$
  若 $v(u)=\bigoplus_a u_a h_a$，则
  $$
  |v(u)|
  =
  \sum_a u_a|h_a|
  -2\sum_{a<b}u_au_b|h_a\wedge h_b|
  +4\sum_{a<b<c}u_au_bu_c|h_a\wedge h_b\wedge h_c|
  +\cdots.
  $$
- 写新内容时引用它：横向 $T$ 的模 $8$ 相位、triorthogonal 条件、repetition-code parity phase 展开都引用这里。当前笔记只保留模 $8$ 截断或特定行重叠条件。

---
## CPTP 映射与 Kraus 表示

- 主笔记：[[CPTP映射与Kraus表示]]，路径 `Notes/03-Magic State基础/CPTP映射与Kraus表示.md`。
- 已有结论：CPTP 表示完全正且保迹的量子信道；Kraus 形式
  $$
  \mathcal E(\rho)=\sum_aK_a\rho K_a^\dagger
  $$
  自动给出 CP，保迹条件是
  $$
  \sum_aK_a^\dagger K_a=I.
  $$
  postselection 分支是 trace non-increasing，对应 $\sum_aK_a^\dagger K_a\le I$。trace preserving 与 unital 不同。
- 写新内容时引用它：写 twirling、Pauli channel、postselection 或测量分支概率时引用这里；不再重复解释 CPTP、CP、TP、Kraus 完备关系。

---
## State injection 与 T injection

- 主笔记：[[State injection]]，路径 `Notes/04-Magic State Injection/State injection.md`。
- 已有结论：资源态 $|U\rangle=U|+\rangle$ 通过 gate teleportation 实现 $U$。in-place gadget 的规范选择为
  $$
  R_U=ZUZU^\dagger,
  \qquad
  C_U=UXU^\dagger X.
  $$
  若 $U$ 为 $Z$ 基对角门，则 $R_U=I$；若进一步 $U\in\mathcal C_3$，条件校正 $C_U$ 是 Clifford。对 $T=\operatorname{diag}(1,e^{i\pi/4})$，
  $m=1$ 分支只需 $S$ correction。资源态上的 $Z$ 错误直接成为数据上的 $Z$ 错误；$X$ 型资源错误在 syndrome measurement 前是相干错误，经过能区分 $Z$ 错误的检查后才可按随机 $Z$ 错误处理。
- 写新内容时引用它：说明每个 noisy $|T\rangle$ 如何变成一次 $T$ 或 parity-phase injection、解释 byproduct correction 或 magic-state error 如何进入数据时引用这里。不要重新画单比特 teleportation 推导，除非当前笔记专门比较线路约定。

---
## MGT 的反向传播与稳定子码构造

- 主笔记：[[MGT 的反向传播与稳定子码构造]]，路径 `Notes/04-Magic State Injection/MGT 的反向传播与稳定子码构造.md`。
- 已有结论：物理末端投影 $\Delta_{\boldsymbol m}$ 可沿 Clifford $V$ 回拉为
  $$
  \Pi_{\boldsymbol m}=V^\dagger\Delta_{\boldsymbol m}V,
  \qquad
  M_k=V^\dagger(Z_{R,k}\otimes I_D)V.
  $$
  这与利用
  $$
  [\Pi_{\boldsymbol m},U_R(\boldsymbol\theta)\otimes I_D]=0
  $$
  把资源分解中的 $U_R$ 移到测量分支之后，是条件不同的两次代数变换。前者用于 $V\mapsto\mathcal M$ 的线路分析；一般构造则先选 $\mathcal M$，再综合满足 $VM_kV^\dagger=Z_{R,k}$ 的解码器 $V$。
- 通过 Clifford 变换分离由稳定子固定的 $|0\rangle$ 因子，再对这些因子做结果确定的 $Z$ 测量并停用相应量子比特，可以得到只保留非稳定子部分的资源态；逆向只需制备 $|0\rangle$ 并施加逆 Clifford。把保留态的量子比特数重记为 $n$ 后，$\nu(|\eta\rangle)=n$。若交换旋转子群的独立生成元数为 $g$，二进制对易矩阵的秩—零化度计数给出
  $$
  \nu(|\eta\rangle)\le g\le n,
  $$
  因而 $g=n$。选择
  $$
  M_k=G_k^{(R)}\otimes G_k^{(D)}
  $$
  得到一个 $[\![2n,n]\!]$ 分支码。令
  $$
  E_{\boldsymbol m}
  :=
  \Pi_{\boldsymbol m}(|s\rangle_R\otimes I_D),
  $$
  则完整联合投影满足
  $$
  E_{\boldsymbol m}^\dagger E_{\boldsymbol m}=2^{-n}I,
  \qquad
  W_{\boldsymbol m}=2^{n/2}E_{\boldsymbol m},
  $$
  所以每个结果概率为 $2^{-n}$，且 $W_{\boldsymbol m}$ 是不泄露任意输入信息的等距编码。
- 若
  $$
  P_\alpha=\prod_{k\in\mathcal I_\alpha}G_k,
  \qquad
  q_\alpha=\left(\sum_{k\in\mathcal I_\alpha}m_k\right)\bmod2,
  $$
  则 $I_R\otimes P_\alpha^{(D)}$ 是本构造所需的逻辑 Pauli 代表，但不是完整逻辑 Pauli 群。资源旋转在分支码上实现
  $$
  U_{\boldsymbol m}
  =
  \prod_\alpha
  P_\alpha\left((-1)^{q_\alpha}\theta_\alpha\right),
  $$
  确定性前馈可取
  $$
  F_{\boldsymbol m}
  =
  \prod_\alpha
  \left[P_\alpha(2\theta_\alpha)\right]^{q_\alpha}.
  $$
  若 $U_{\boldsymbol0}\in\mathcal C_\ell$，则 $F_{\boldsymbol m}\in\mathcal C_{\ell-1}$；特别地，$\mathcal C_3$ 目标具有 Clifford 前馈。
- 写新内容时引用它：讨论一般 MGT、反向传播联合测量、测量分支稳定子码、commuting-Pauli 资源态或 MGT 前馈层级时引用这里。必须区分两次换序、压缩前后的量子比特数，并把 $I\otimes P_\alpha$ 称为所需逻辑代表而不是所有逻辑 Pauli。

---
## Twirling 与 magic-state 错误模型

- 主笔记：[[Clifford Twirling 与魔态错误模型]]，路径 `Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md`。
- 已有结论：Pauli twirling 得到 Pauli channel，full Clifford twirling 得到 depolarizing channel；针对 $|T\rangle$ 的 magic-state twirling 不是 full Clifford twirling，而是用
  $$
  A=\frac{X+Y}{\sqrt2}
  $$
  的本征基把 noisy $|T\rangle$ 对角化为
  $$
  \rho_T(p)=(1-p)|T\rangle\langle T|+pZ|T\rangle\langle T|Z.
  $$
  局域 twirling 对多输入只消去 error-pattern 间相干，得到 $\sum_xp_xZ(x)|T\rangle\langle T|^{\otimes n}Z(x)$；它不推出 i.i.d.，独立同分布是额外噪声假设。
- 写新内容时引用它：任何 distillation 输入错误模型、$p^{|x|}(1-p)^{n-|x|}$、“随机 $Z$ 错误”或“correlated error 会破坏阶数”的讨论都应引用这里。

---
## Triorthogonal distillation 的统一接口

- 主笔记：[[Distillation protocol]]，路径 `Notes/05-Magic State Distillation/Distillation protocol.md`。
- 已有结论：给定
  $$
  G=\begin{pmatrix}G_1\\G_0\end{pmatrix}\in\mathbb F_2^{(k+m_x)\times n},
  $$
  $G_1$ 的奇重量行承载 $k$ 个输出，$G_0$ 的偶重量行给出 $m_x$ 个 $X$ 检查。第 $j$ 列 $c_j$ 对应一个 parity-phase gate
  $$
  P(c_j)=\exp\left[\frac{i\pi}{8}(I-Z(c_j))\right].
  $$
  输入错误模式 $e\in\mathbb F_2^n$ 在紧凑寄存器上变成
  $$
  Z(Ge^T).
  $$
  接受条件和输出逻辑错误分别为
  $$
  G_0e^T=0,
  \qquad
  \ell=G_1e^T.
  $$
  接受概率、输出错误分布和 yield 为
  $$
  P_{\mathrm{acc}}
  =
  \sum_{G_0e^T=0}w(e),
  \qquad
  Y=\frac{kP_{\mathrm{acc}}}{n}.
  $$
- 写新内容时引用它：任何 $n\to k$ distillation protocol 都先引用这里的 $G_0/G_1$ 接口，再给特例矩阵、距离、leading coefficient。不要在特例笔记里重新推导 syndrome 和 yield。
- 边界：$n$ 是每次尝试消耗的 noisy magic states，$k+m_x$ 是紧凑寄存器宽度，完整硬件峰值 qubit 数和 surface-code spacetime volume 需要另算。

---
## 横向 T、三正交条件与逻辑矩阵判据

- 主笔记：[[三正交码与横向逻辑T门]]，路径 `Notes/05-Magic State Distillation/三正交码与横向逻辑T门.md`。
- 已有结论：一般稳定子码中，横向 $T^{\otimes n}$ 的逻辑矩阵元为
  $$
  K_{yx}
  =
  \frac1{|A|}
  \sum_{z\in W_x\cap W_y}q_y(z)^*q_x(z)\omega^{|z|}.
  $$
  编码空间保持条件是 $K^\dagger K=I$；若允许 Clifford 修正，目标门判据是
  $$
  KT_{\mathrm{target}}^\dagger
  \in\mathrm{Clifford}_L
  $$
  up to global phase。CSS 情形中，三正交条件来自 [[汉明重量展开]] 的模 $8$ 截断：稳定子行需偶重量，逻辑 $T$ 行需奇重量，任意两行和任意三条不同的行重叠为偶数，避免 controlled-$S$ 和 $CCZ$ 型额外非 Clifford 相位。
- 写新内容时引用它：解释 triorthogonality 为什么足以支持横向 $T/T^\dagger$、判断一般稳定子码横向 $T$ 是否保持编码空间、比较 Clifford correction 时引用这里。

---
## Reed-Muller 15-to-1 distillation

- 主笔记：[[Reed-Muller码]]，路径 `Notes/05-Magic State Distillation/Reed-Muller码.md`。
- 已有结论：punctured $RM(1,4)$ 的 $5\times15$ 矩阵给出量子 Reed-Muller $[\![15,1,3]\!]$ CSS 码。偶重量行 $G_0$ 生成 $X$ stabilizer，$C_Z=\operatorname{rowspan}(G)^\perp$。码距分解为
  $$
  d_X=7,\qquad d_Z=3,\qquad d=3.
  $$
  在该笔记约定下，
  $$
  T^{\otimes15}|_{\mathcal Q}=T_L^\dagger,
  \qquad
  (T^\dagger)^{\otimes15}=T_L.
  $$
  i.i.d. 随机 $Z$ 输入模型下，接受条件是 $G_0x^T=0$，接受的奇重量错误造成逻辑错误。接受概率和条件输出错误率为
  $$
  P_{\mathrm{acc}}=\frac{1+15(1-2p)^8}{16},
  $$
  $$
  p_{\mathrm{out}}
  =
  \frac{
  1-15(1-2p)^7+15(1-2p)^8-(1-2p)^{15}
  }{
  2[1+15(1-2p)^8]
  }
  =
  35p^3+O(p^4).
  $$
- 写新内容时引用它：15-to-1 的矩阵、方向约定、$35p^3$、weight enumerator、阈值和 yield 都引用这里；不要只写“码距为 3 所以是 $35p^3$”，因为系数来自重量为 3 的 accepted logical patterns 数。

---
## Repetition code 上的逻辑 T 与 compact distillation 矩阵

- 主笔记：[[重复码上的逻辑T门]]，路径 `Notes/05-Magic State Distillation/重复码上的逻辑T门.md`。
- 已有结论：phase-flip repetition code
  $$
  |+_L\rangle=|+\rangle^{\otimes N},
  \qquad
  |-_{L}\rangle=|-\rangle^{\otimes N}
  $$
  只检测 $Z$ 型 phase flip；无 syndrome 的 $Z$ 图样只有 $0$ 和全重逻辑 $\bar Z$。朴素 decode--$T$--encode 不容错，因为单个 $Z_1$ injection error 可变成 $\bar Z$。相位恒等式给出
  $$
  E T_1E^\dagger
  =
  \prod_iT_i
  \prod_{i<j}CS^\dagger_{ij}
  \prod_{i<j<k}CCZ_{ijk}.
  $$
  Pauli product rotation support $\alpha^k$ 满足 singleton、pair、triplet 奇覆盖条件即可实现逻辑 $T$ up to Clifford correction。解码差分
  $$
  \beta_1^k=\alpha_1^k,
  \qquad
  \beta_i^k=\alpha_i^k\oplus\alpha_{i-1}^k
  $$
  把逻辑门线路转为 distillation 矩阵 $G$，并把全重逻辑错误映到输出线 $e_1$。
- 写新内容时引用它：需要从 repetition-code logical gate 过渡到 triorthogonal compact distillation matrix、解释 $\alpha\mapsto\beta$、或说明距离为何来自若干 faulty supports 异或成全重图样时引用这里。

---
## Canonical compact distillation family

- 主笔记：[[Canonical distillation family]]，路径 `Notes/05-Magic State Distillation/Canonical distillation family.md`。
- 已有结论：在 support Boolean lattice 上，选择函数 $f(A)$ 与覆盖次数
  $$
  g(B)=\sum_{A\supseteq B}f(A)\pmod2
  $$
  互为 zeta/Möbius 变换。canonical choice 取
  $$
  g_0(B)=1\quad(1\le |B|\le3),
  \qquad
  g_0(B)=0\quad(|B|>3).
  $$
  反演后只出现 weight $1,2,3$ 的 supports，具体选哪些由 $N\bmod4$ 决定：
  $$
  n=
  \begin{cases}
  \binom N1+\binom N2+\binom N3, & N\equiv0\pmod4,\\
  \binom N1+\binom N3, & N\equiv1\pmod4,\\
  \binom N2+\binom N3, & N\equiv2\pmod4,\\
  \binom N3, & N\equiv3\pmod4.
  \end{cases}
  $$
  距离为
  $$
  d(F_N^0)=
  \begin{cases}
  \lceil N/3\rceil, & N\ \mathrm{even},\\
  \min\{t\in2\mathbb Z+1:t\ge N/3\}, & N\ \mathrm{odd}.
  \end{cases}
  $$
  该笔记还登记了附录 C 原文在一个奇数构造句子中的笔误，并给出可行修正。
- 写新内容时引用它：使用 Jacinto canonical family、support coverage、Möbius inversion、$N\bmod4$ 选支撑、距离公式或 $\sqrt T$ 推广时引用这里。不要在协议特例中重新解释 incidence algebra。

---
## SAT 搜索 compact factories

- 主笔记：[[SAT搜索紧凑蒸馏工厂]]，路径 `Notes/05-Magic State Distillation/SAT搜索紧凑蒸馏工厂.md`。
- 已有结论：SAT 变量表示 Pauli product rotation 的 support 是否被选。逻辑 $T$ 约束是 singleton、pair、triplet 的 XOR 奇覆盖；距离约束是禁止少于 $d_{\min}$ 个已选 supports 异或成全重逻辑错误。SAT 表示存在性构造，UNSAT 才是在给定变量空间内的不存在证明，timeout 或未找到解不是证明。无对称、全排列对称、Young subgroup、cyclic subgroup 是不同搜索子族。
- 已有结果摘录：无对称搜索得到 $N=10$ 的 $80T\to1T$ 距离 $4$ 方案；cyclic subgroup 子族得到 $N=10$ 的 $64T\to1T$ 距离 $4$ 和 $N=11$ 的 $65T\to1T$ 距离 $5$ 方案。该笔记也整理了 $nT\to1CCZ$ 的 SAT 约束与代表结果。
- 写新内容时引用它：讨论 compact factory 搜索、对称化变量、T-count 最小化、SAT/UNSAT 语义、leading coefficient 搜索结果或 CCZ factory 搜索约束时引用这里。不要把“搜索没找到”写成“不存在”。

---
## 已有结论的常用引用模板

- CSS 逻辑基态：按照 [[逻辑基态的表示]] 中的 CSS 陪集态表示，逻辑空间由 $C_Z^\perp/C_X$ 标记。
- 稳定子态相位：按照 [[逻辑基态的二次相位]]，稳定子态计算基相位只有一次项和 $CZ$ 型二次项。
- 横向 $T$ 的模 $8$ 来源：完整重量展开见 [[汉明重量展开]]，这里仅使用其模 $8$ 截断。
- triorthogonal 相位条件：按照 [[三正交码与横向逻辑T门]]，偶/奇行和二重、三重重叠条件保证额外非 Clifford 相位消失。
- noisy input 模型：随机 $Z$ 输入模型来自 [[Clifford Twirling 与魔态错误模型]] 和 [[State injection]]，独立性是额外假设。
- distillation syndrome：按照 [[Distillation protocol]]，错误模式 $e$ 的 syndrome 是 $G_0e^T$，接受后的输出逻辑错误是 $G_1e^T$。
- 15-to-1 常数：$p_{\mathrm{out}}=35p^3+O(p^4)$ 和 $P_{\mathrm{acc}}$ 公式引用 [[Reed-Muller码]]，不要从“距离为 3”直接推出系数。
- compact family：canonical support 反演和 $N\bmod4$ 选支撑规则引用 [[Canonical distillation family]]；搜索优化和 SAT 语义引用 [[SAT搜索紧凑蒸馏工厂]]。
