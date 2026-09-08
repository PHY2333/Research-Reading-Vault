---
note_type: reference
entry_mode: guided
status: reviewed
---

超图乘积（hypergraph product, HGP）构造从两张经典二进制校验矩阵出发，产生一对共享同一组物理量子比特列的 CSS 校验矩阵。本文不把最终公式当作需要记忆的结论，而是沿着下面这条路线把它们构造出来：

$$
\text{经典矩阵}
\longrightarrow
\text{两个二项链复形}
\longrightarrow
\text{三项乘积链复形}
\longrightarrow
H_X,H_Z
\longrightarrow
\text{对易与 Tanner 图}.
$$

前半部分完成一般 HGP 主线：先说明为什么经典矩阵可以放入链复形，再由总次数得到三个链群，由乘积边界逐块推出 $H_X,H_Z$，最后从四个 Kronecker 块读出 Tanner 邻接。后半部分讨论长度、逻辑支撑、qLDPC 条件和参数边界。S007 记号、Künneth 分解、平方根距离基准以及 HGP 到 LP 的接口分别放在独立的选读节；跳过任一选读节都不影响一般构造。

## 从 CSS 对易条件确定构造目标

先取任意一对二进制 CSS 校验矩阵

$$
H_X\in\mathbb F_2^{r_X\times N},
\qquad
H_Z\in\mathbb F_2^{r_Z\times N}.
$$

两张矩阵的列都由同一组 $N$ 个物理量子比特编号。$H_X$ 的一行给出一个 $X$ 型校验的支撑，$H_Z$ 的一行给出一个 $Z$ 型校验的支撑。

设第 $a$ 个 $X$ 型校验和第 $b$ 个 $Z$ 型校验共同作用于 $w_{ab}$ 个量子比特。每个共同位置贡献一次 $XZ=-ZX$，因此两者交换当且仅当 $w_{ab}$ 为偶数。另一方面，

$$
(H_XH_Z^{\mathsf T})_{ab}
=
\sum_{q=1}^N H_X(a,q)H_Z(b,q)
\pmod 2
$$

正是这两个行支撑的重叠数模 $2$。所以全部异型校验彼此对易等价于

$$
\boxed{
H_XH_Z^{\mathsf T}=0
}.
$$

这个条件可以重新组织成一串线性映射。令

$$
C_2=\mathbb F_2^{r_Z},
\qquad
C_1=\mathbb F_2^N,
\qquad
C_0=\mathbb F_2^{r_X},
$$

并取

$$
C_2
\xrightarrow{\ \partial_2=H_Z^{\mathsf T}\ }
C_1
\xrightarrow{\ \partial_1=H_X\ }
C_0.
$$

这里三个空间各有直接的 CSS 含义：

- $C_2$ 的坐标标记写出的 $Z$ 型校验；
- $C_1$ 的坐标标记物理量子比特；
- $C_0$ 的坐标标记写出的 $X$ 型校验。

若 $u\in C_2$ 选择若干个 $Z$ 型校验相乘，那么 $H_Z^{\mathsf T}u\in C_1$ 是所得 $Z$ 型稳定子的物理支撑。再乘以 $H_X$，就是检查这个支撑与每个 $X$ 型校验的重叠奇偶性。于是

$$
\partial_1\partial_2=0
$$

翻译回 CSS 语言就是：任意 $Z$ 型稳定子都与全部 $X$ 型校验交换。

因此 HGP 的核心任务可以说得很具体：从两张经典矩阵构造出三个空间和两支映射，使

$$
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0
$$

自动满足 $\partial_1\partial_2=0$，然后取

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^{\mathsf T}.
$$

## 从两张经典校验矩阵开始

取两张任意二进制矩阵

$$
A\in\mathbb F_2^{m_A\times n_A},
\qquad
B\in\mathbb F_2^{m_B\times n_B}.
$$

把 $A$ 看成线性映射时，它从列坐标空间送到行坐标空间：

$$
A:\mathbb F_2^{n_A}\longrightarrow\mathbb F_2^{m_A}.
$$

经典编码语言中，定义域的 $n_A$ 个基向量标记变量节点，陪域的 $m_A$ 个基向量标记校验节点。若 $v\in\mathbb F_2^{n_A}$ 是一个变量取值向量，那么 $Av$ 给出各行校验的奇偶结果。

现在只给这两个空间添加次数，并在两端补零空间：

$$
\mathcal A:\qquad
0
\longrightarrow
A_1=\mathbb F_2^{n_A}
\xrightarrow{\ A\ }
A_0=\mathbb F_2^{m_A}
\longrightarrow
0.
$$

这里下标 $1,0$ 是次数标签，不是维数。矩阵 $A$ 把次数降低一阶，从 $A_1$ 送到 $A_0$。两端没有别的非零映射，所以所有“连续取两次边界”的复合都是

$$
A\circ 0=0,
\qquad
0\circ A=0.
$$

因此任意矩阵都可以这样成为二项链复形；不需要先对 $A$ 施加额外方程。矩阵本身仍然做原来的事情，新增的只是“列坐标在次数 $1$、行坐标在次数 $0$”这一层组织。

同样，把 $B$ 写成

$$
\mathcal B:\qquad
0
\longrightarrow
B_1=\mathbb F_2^{n_B}
\xrightarrow{\ B\ }
B_0=\mathbb F_2^{m_B}
\longrightarrow
0.
$$

为什么选择从次数 $1$ 指向次数 $0$，而不把箭头反过来？原因不是形式偏好，而是我们想让两份二项复形的乘积恰好产生前一节需要的三层结构：

$$
C_2\longrightarrow C_1\longrightarrow C_0.
$$

在这个方向下，最高层来自“变量坐标乘变量坐标”，最低层来自“校验坐标乘校验坐标”，而中间层有“变量乘校验”和“校验乘变量”两种来源。后者正好会成为 HGP 的两类物理量子比特坐标。

为便于后面展开指标，固定以下记号：

$$
i\in[m_A],
\qquad
j\in[n_A],
$$

分别标记 $A$ 的行和列；并令

$$
\alpha\in[m_B],
\qquad
\beta\in[n_B],
$$

分别标记 $B$ 的行和列。这里 $[s]=\{1,\ldots,s\}$。

## 总次数如何产生三个链群

### 先看总次数的定义

令乘积链复形为

$$
\mathcal C=\mathcal A\otimes\mathcal B.
$$

普通张量积先产生双指标空间 $A_p\otimes B_q$。为了把这些方格重新排成一条链，给简单张量规定总次数

$$
\deg(a_p\otimes b_q)=p+q.
$$

于是乘积链复形在次数 $r$ 的链群定义为

$$
C_r
=
\bigoplus_{p+q=r}A_p\otimes B_q.
$$

这里内层的张量积把两个因子的基方向两两配对；外层的直和把总次数相同、但来源不同的空间并列保存。总次数是乘积复形的分层规则，不是由维数计算倒推出的结论。

两份种子复形都只在次数 $1$ 和 $0$ 非零，所以可能出现的总次数只有 $2,1,0$。

### 次数 $2$：变量坐标乘变量坐标

总次数 $2$ 只有一种分解：

$$
2=1+1.
$$

因此

$$
\begin{aligned}
C_2
&=A_1\otimes B_1\\
&=\mathbb F_2^{n_A}\otimes\mathbb F_2^{n_B}\\
&\cong\mathbb F_2^{n_An_B}.
\end{aligned}
$$

它的一组基由成对指标

$$
(j,\beta)\in[n_A]\times[n_B]
$$

标记。按照本文的 CSS 约定，$C_2$ 最终标记 $Z$ 型校验；把相应基标签记为

$$
z_{j,\beta}.
$$

这里的 $z_{j,\beta}$ 首先只是一个校验坐标名，不是已经写出的 Pauli 算符。它对应哪一些物理量子比特，要由稍后的 $\partial_2$ 决定。

### 次数 $1$：两种来源形成直和

总次数 $1$ 有两种分解：

$$
1=1+0,
\qquad
1=0+1.
$$

所以

$$
\begin{aligned}
C_1
&=(A_1\otimes B_0)\oplus(A_0\otimes B_1)\\
&\cong
\mathbb F_2^{n_Am_B}
\oplus
\mathbb F_2^{m_An_B}.
\end{aligned}
$$

把第一分量记为

$$
Q_1=A_1\otimes B_0,
$$

它的基标签为

$$
q^{(1)}_{j,\alpha},
\qquad
(j,\alpha)\in[n_A]\times[m_B].
$$

把第二分量记为

$$
Q_2=A_0\otimes B_1,
$$

它的基标签为

$$
q^{(2)}_{i,\beta},
\qquad
(i,\beta)\in[m_A]\times[n_B].
$$

按照链复形到 CSS 码的解释，$C_1$ 是物理支撑空间。因此每个 $q^{(1)}_{j,\alpha}$ 和 $q^{(2)}_{i,\beta}$ 都标记一个物理量子比特，物理比特总数为

$$
\boxed{
N=n_Am_B+m_An_B
}.
$$

这里必须区分“物理扇区”和“逻辑分量”。直和

$$
C_1=Q_1\oplus Q_2
$$

在施加任何闭合条件、也没有商掉任何稳定子之前就已经存在。它只是说一个物理支撑向量可以唯一写成

$$
v=(v_1,v_2),
\qquad
v_1\in Q_1,
\quad
v_2\in Q_2.
$$

所以 $Q_1,Q_2$ 是两类物理坐标。逻辑算符则要先满足校验，再把相差稳定子的支撑视为同一类；那是后面由核与商空间得到的对象。两处虽然都可能出现“两个分量”，但它们处在完全不同的构造阶段。

### 次数 $0$：校验坐标乘校验坐标

总次数 $0$ 也只有一种分解：

$$
0=0+0.
$$

于是

$$
\begin{aligned}
C_0
&=A_0\otimes B_0\\
&=\mathbb F_2^{m_A}\otimes\mathbb F_2^{m_B}\\
&\cong\mathbb F_2^{m_Am_B}.
\end{aligned}
$$

它的基由

$$
(i,\alpha)\in[m_A]\times[m_B]
$$

标记。按照本文约定，$C_0$ 最终标记 $X$ 型校验；相应标签记为

$$
x_{i,\alpha}.
$$

至此，三个空间已经逐项得到：

$$
\boxed{
C_2=\mathbb F_2^{n_An_B}
}
$$

$$
\boxed{
C_1=
\mathbb F_2^{n_Am_B}
\oplus
\mathbb F_2^{m_An_B}
}
$$

$$
\boxed{
C_0=\mathbb F_2^{m_Am_B}
}.
$$

下一步不是猜测两张量子校验矩阵，而是把种子边界 $A,B$ 合成为乘积边界。

## 从乘积边界逐块导出 $H_X$ 和 $H_Z$

这一节的目标是从同一条乘积边界公式推出四个 Kronecker 块。推导顺序如下：

1. 写出链复形张量积的边界公式；
2. 分别计算 $\partial_1:C_1\to C_0$ 在两个物理扇区上的作用；
3. 计算 $\partial_2:C_2\to C_1$ 落入两个物理扇区的分量；
4. 令 $H_X=\partial_1$，再把 $\partial_2$ 转置成以校验为行、物理量子比特为列的 $H_Z$。

### 乘积边界公式与符号

对齐次元素 $a_p\in A_p$、$b_q\in B_q$，一般系数下的乘积边界是

$$
\partial(a_p\otimes b_q)
=
\partial_{\mathcal A}a_p\otimes b_q
+
(-1)^p a_p\otimes\partial_{\mathcal B}b_q.
$$

第一项沿 $A$ 因子降低次数，第二项沿 $B$ 因子降低次数。系数 $(-1)^p$ 是 Koszul 符号；它保证两条先后次序相反的路径带相反符号。

本文在 $\mathbb F_2$ 上工作，而

$$
-1=1
\qquad\text{在 }\mathbb F_2\text{ 中}.
$$

所以最终二进制矩阵里正负号相同。这个省略只在特征 $2$ 中成立；不能把它推广成一般系数下的乘积边界公式。

### Kronecker 积的指标读法

若

$$
M\in\mathbb F_2^{r\times c},
\qquad
N\in\mathbb F_2^{s\times t},
$$

那么

$$
M\otimes N:
\mathbb F_2^c\otimes\mathbb F_2^t
\longrightarrow
\mathbb F_2^r\otimes\mathbb F_2^s
$$

的尺寸为 $rs\times ct$，并满足

$$
(M\otimes N)_{(a,u),(b,v)}
=
M_{a,b}N_{u,v}.
$$

当其中一个因子是恒等矩阵时，它给出一个 Kronecker delta。例如

$$
(A\otimes I_{m_B})_{(i,\alpha),(j,\alpha')}
=
A_{i,j}\delta_{\alpha,\alpha'}.
$$

这意味着 $A$ 改变第一因子的坐标 $j\to i$，而 $I_{m_B}$ 强制第二因子的坐标保持 $\alpha=\alpha'$。后面所有“固定哪个坐标”的结论都来自这种 delta，而不是从图形方向猜出。

### 从张量积的泛性质到 Kronecker 矩阵

上面的指标公式为什么对应“分别作用于两个因子”？这里要区分三个对象：向量空间 $V\otimes W$、纯张量 $x\otimes y$，以及作用在张量积空间上的线性映射 $T\otimes S$。Kronecker 积是最后这张映射选基后的矩阵表示。

沿用上一小节的尺寸，令

$$
T:V=\mathbb F_2^c\longrightarrow V'=\mathbb F_2^r,
\qquad
S:W=\mathbb F_2^t\longrightarrow W'=\mathbb F_2^s,
$$

其标准基下的矩阵分别为 $M,N$。我们希望得到线性映射 $T\otimes S$，把 $x\otimes y$ 送到 $T(x)\otimes S(y)$。但一般张量的纯张量分解不唯一，例如

$$
(x_1+x_2)\otimes y=x_1\otimes y+x_2\otimes y.
$$

因此，仅给出纯张量的像还不够；必须保证按不同分解计算时得到同一个结果。

张量积的泛性质恰好保证这一点：对任意向量空间 $E$，每张双线性映射 $g:V\times W\to E$ 都唯一分解为一张线性映射 $\widetilde g:V\otimes W\to E$，满足 $\widetilde g(x\otimes y)=g(x,y)$。在这里取 $E=V'\otimes W'$，并定义

$$
\beta:V\times W\longrightarrow V'\otimes W',
\qquad
\beta(x,y)=T(x)\otimes S(y).
$$

因为 $T,S$ 线性，且目标空间中的张量符号对两个变量分别线性，所以 $\beta$ 双线性。例如

$$
\beta(x_1+x_2,y)
=(T(x_1)+T(x_2))\otimes S(y)
=\beta(x_1,y)+\beta(x_2,y),
$$

第二个变量的加法与两个变量的标量关系也同样成立。于是泛性质给出唯一的线性映射

$$
T\otimes S:V\otimes W\longrightarrow V'\otimes W',
\qquad
(T\otimes S)(x\otimes y)=T(x)\otimes S(y).
$$

这一步解决了良定义性：线性扩张后的结果不依赖所选的纯张量分解。这里使用的正是 [[张量积与直和泛性质的 HGP-Künneth 接口#空间、纯张量与诱导映射是三个层次|空间、纯张量与诱导映射的区分]] 中的构造；接下来把它用于上一小节的矩阵元。

分别记 $V,W$ 的标准基为 $e_b$、$f_v$，$V',W'$ 的标准基为 $e'_a$、$f'_u$，其中 $b\in[c]$、$v\in[t]$、$a\in[r]$、$u\in[s]$。按矩阵的列表示基向量的像，

$$
T(e_b)=\sum_{a=1}^r M_{a,b}e'_a,
\qquad
S(f_v)=\sum_{u=1}^s N_{u,v}f'_u.
$$

因此

$$
\begin{aligned}
(T\otimes S)(e_b\otimes f_v)
&=T(e_b)\otimes S(f_v)\\
&=\sum_{a=1}^r\sum_{u=1}^s
M_{a,b}N_{u,v}\,e'_a\otimes f'_u.
\end{aligned}
$$

源空间的张量积基为 $e_b\otimes f_v$，目标空间的张量积基为 $e'_a\otimes f'_u$。两边都按“固定第一指标，让第二指标先变化”的顺序排列，则输入 $(b,v)$ 是第 $(b-1)t+v$ 列，输出 $(a,u)$ 是第 $(a-1)s+u$ 行。上式给出的矩阵元正是 $M_{a,b}N_{u,v}$；固定 $a,b$ 而让 $u,v$ 变化，就得到一个完整的块 $M_{a,b}N$。所以

$$
[T\otimes S]
=M\otimes N
=\begin{pmatrix}
M_{1,1}N&\cdots&M_{1,c}N\\
\vdots&\ddots&\vdots\\
M_{r,1}N&\cdots&M_{r,c}N
\end{pmatrix}.
$$

这说明“把 $M$ 的每个元素替换成相应倍数的 $N$”来自映射在张量积基上的展开。**Kronecker 积的矩阵公式不是泛性质本身，而是泛性质诱导出的映射在指定基序下的坐标表达。**

同一个构造也解释了后文使用的乘法规则。若 $U:V_0\to V$、$R:W_0\to W$ 是可复合的线性映射，那么

$$
(T\otimes S)\circ(U\otimes R)
=(T\circ U)\otimes(S\circ R),
$$

因为两边都把每个 $x_0\otimes y_0$ 送到 $T(U(x_0))\otimes S(R(y_0))$，而纯张量张成 $V_0\otimes W_0$。这称为张量积的函子性；在相容的张量积基下，它就是 $(M\otimes N)(P\otimes Q)=(MP)\otimes(NQ)$，其中 $P,Q$ 分别是 $U,R$ 的矩阵。回到 HGP，取其中一个映射为恒等映射，就得到下一步所需的“只沿一个因子作用”的 Kronecker 块。

### $\partial_1$ 的第一块：作用于 $Q_1=A_1\otimes B_0$

先取第一物理扇区中的基向量

$$
q^{(1)}_{j,\alpha}
=
e_j^A\otimes e_\alpha^B
\in A_1\otimes B_0.
$$

因为 $B_0$ 后面只有零映射，乘积边界只沿 $A$ 因子作用：

$$
\partial_1
\bigl(e_j^A\otimes e_\alpha^B\bigr)
=
Ae_j^A\otimes e_\alpha^B.
$$

因此这一扇区到 $C_0=A_0\otimes B_0$ 的矩阵是

$$
A\otimes I_{m_B}.
$$

它的完整类型为

$$
A\otimes I_{m_B}:
A_1\otimes B_0
\longrightarrow
A_0\otimes B_0,
$$

尺寸为

$$
(m_Am_B)\times(n_Am_B).
$$

其矩阵元为

$$
(A\otimes I_{m_B})_{(i,\alpha),(j,\alpha')}
=
A_{i,j}\delta_{\alpha,\alpha'}.
$$

所以这块有三层含义：

- 它只作用于第一物理扇区 $q^{(1)}_{j,\alpha'}$；
- 它按 $A_{i,j}$ 把 $A$ 的列坐标 $j$ 连接到行坐标 $i$；
- 它固定 $B$ 的行坐标 $\alpha$。

### $\partial_1$ 的第二块：作用于 $Q_2=A_0\otimes B_1$

再取第二物理扇区中的基向量

$$
q^{(2)}_{i,\beta}
=
e_i^A\otimes e_\beta^B
\in A_0\otimes B_1.
$$

这次 $A_0$ 后面只有零映射，所以边界只沿 $B$ 因子作用：

$$
\partial_1
\bigl(e_i^A\otimes e_\beta^B\bigr)
=
e_i^A\otimes Be_\beta^B.
$$

因此第二块是

$$
I_{m_A}\otimes B.
$$

它的类型为

$$
I_{m_A}\otimes B:
A_0\otimes B_1
\longrightarrow
A_0\otimes B_0,
$$

尺寸为

$$
(m_Am_B)\times(m_An_B).
$$

指标展开为

$$
(I_{m_A}\otimes B)_{(i,\alpha),(i',\beta)}
=
\delta_{i,i'}B_{\alpha,\beta}.
$$

所以它只作用于第二物理扇区，按 $B_{\alpha,\beta}$ 改变 $B$ 坐标 $\beta\to\alpha$，并固定 $A$ 的行坐标 $i$。

由于 $C_1$ 按

$$
C_1=Q_1\oplus Q_2
$$

排列，两个分量上的映射要横向拼接。于是

$$
\partial_1
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right].
$$

按本文的 CSS 约定，

$$
\boxed{
H_X=\partial_1
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
}.
$$

它的行由 $x_{i,\alpha}$ 标记，列先由所有 $q^{(1)}_{j,\alpha}$ 标记，再由所有 $q^{(2)}_{i,\beta}$ 标记；总尺寸为

$$
H_X\in
\mathbb F_2^{m_Am_B\times(n_Am_B+m_An_B)}.
$$

### $\partial_2$ 的第一分量：从 $C_2$ 落入 $Q_1$

取

$$
z_{j,\beta}
=
e_j^A\otimes e_\beta^B
\in A_1\otimes B_1.
$$

若先沿 $B$ 因子取边界，就得到

$$
e_j^A\otimes Be_\beta^B
\in A_1\otimes B_0=Q_1.
$$

在一般系数下，这一项带 $(-1)^1=-1$；在 $\mathbb F_2$ 中负号消失。因此落入第一物理扇区的块是

$$
I_{n_A}\otimes B.
$$

其类型为

$$
I_{n_A}\otimes B:
A_1\otimes B_1
\longrightarrow
A_1\otimes B_0,
$$

尺寸为

$$
(n_Am_B)\times(n_An_B).
$$

矩阵元是

$$
(I_{n_A}\otimes B)_{(j,\alpha),(j',\beta)}
=
\delta_{j,j'}B_{\alpha,\beta}.
$$

所以它固定 $A$ 的列坐标 $j$，按 $B$ 改变第二因子的坐标 $\beta\to\alpha$。

### $\partial_2$ 的第二分量：从 $C_2$ 落入 $Q_2$

若沿 $A$ 因子取边界，则

$$
Ae_j^A\otimes e_\beta^B
\in A_0\otimes B_1=Q_2.
$$

对应块为

$$
A\otimes I_{n_B}.
$$

其类型为

$$
A\otimes I_{n_B}:
A_1\otimes B_1
\longrightarrow
A_0\otimes B_1,
$$

尺寸为

$$
(m_An_B)\times(n_An_B).
$$

矩阵元为

$$
(A\otimes I_{n_B})_{(i,\beta),(j,\beta')}
=
A_{i,j}\delta_{\beta,\beta'}.
$$

所以它按 $A$ 改变第一因子的坐标 $j\to i$，并固定 $B$ 的列坐标 $\beta$。

两个结果落入 $C_1$ 的两个直和分量，因此要竖直堆叠：

$$
\partial_2
=
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}
\qquad
\text{（系数域为 }\mathbb F_2\text{）}.
$$

若保留一般系数下的 Koszul 符号，并继续采用当前直和顺序，则第一块应写成 $-I_{n_A}\otimes B$。二进制 HGP 中这与上式相同。

### 为什么 $H_Z$ 是 $\partial_2$ 的转置

矩阵 $\partial_2$ 的列由 $C_2$ 的 $Z$ 型校验标签 $z_{j,\beta}$ 编号，行由 $C_1$ 的物理量子比特编号。稳定子校验矩阵采用相反的排布：每一行是一条校验，每一列是一个物理量子比特。因此必须取转置：

$$
H_Z=\partial_2^{\mathsf T}.
$$

逐块转置给出

$$
\boxed{
H_Z
=
\left[
I_{n_A}\otimes B^{\mathsf T}
\;\middle|\;
A^{\mathsf T}\otimes I_{n_B}
\right]
}.
$$

第一块的类型和尺寸为

$$
I_{n_A}\otimes B^{\mathsf T}:
Q_1
\longrightarrow
C_2,
$$

$$
(n_An_B)\times(n_Am_B),
$$

并且

$$
(I_{n_A}\otimes B^{\mathsf T})_{(j,\beta),(j',\alpha)}
=
\delta_{j,j'}B_{\alpha,\beta}.
$$

它作用于第一物理扇区，固定 $A$ 的列坐标 $j$，并用 $B^{\mathsf T}$ 把 $B$ 的行坐标 $\alpha$ 与列坐标 $\beta$ 相连。

第二块的类型和尺寸为

$$
A^{\mathsf T}\otimes I_{n_B}:
Q_2
\longrightarrow
C_2,
$$

$$
(n_An_B)\times(m_An_B),
$$

并且

$$
(A^{\mathsf T}\otimes I_{n_B})_{(j,\beta),(i,\beta')}
=
A_{i,j}\delta_{\beta,\beta'}.
$$

它作用于第二物理扇区，固定 $B$ 的列坐标 $\beta$，并用 $A^{\mathsf T}$ 把 $A$ 的行坐标 $i$ 与列坐标 $j$ 相连。

最终，

$$
H_Z\in
\mathbb F_2^{n_An_B\times(n_Am_B+m_An_B)}.
$$

两张矩阵现在拥有完全相同的 $N$ 列，而且每一块的来源、目标、尺寸、转置和固定坐标都由乘积边界确定，而不是事后补上的规则。

## 两条乘积路径为什么保证 CSS 对易

这一节要证明

$$
H_XH_Z^{\mathsf T}=0.
$$

由于

$$
H_X=\partial_1,
\qquad
H_Z^{\mathsf T}=\partial_2,
$$

只需证明

$$
\partial_1\partial_2=0.
$$

### 先看证明地图

从 $C_2=A_1\otimes B_1$ 到 $C_0=A_0\otimes B_0$ 有两条路径：

$$
\begin{array}{ccccc}
&&A_1\otimes B_1&&\\
&\overset{I\otimes B}{\swarrow}&&
\overset{A\otimes I}{\searrow}&\\
A_1\otimes B_0&&&&A_0\otimes B_1\\
&\underset{A\otimes I}{\searrow}&&
\underset{I\otimes B}{\swarrow}&\\
&&A_0\otimes B_0&&
\end{array}
$$

左路先沿 $B$ 因子，再沿 $A$ 因子；右路的次序相反。因为两张矩阵作用在不同张量因子上，两条路径得到同一个线性映射 $A\otimes B$。一般系数下，Koszul 符号让两份贡献一正一负；在 $\mathbb F_2$ 中，正负相同，但同一个二进制贡献出现两次仍然等于零。

### 用块矩阵计算

代入前面的两个边界矩阵：

$$
\begin{aligned}
\partial_1\partial_2
&=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}\\
&=
(A\otimes I_{m_B})(I_{n_A}\otimes B)
+
(I_{m_A}\otimes B)(A\otimes I_{n_B}).
\end{aligned}
$$

Kronecker 积满足

$$
(M\otimes N)(P\otimes Q)
=
(MP)\otimes(NQ),
$$

只要普通矩阵乘法的尺寸相容。因此

$$
(A\otimes I_{m_B})(I_{n_A}\otimes B)
=
A\otimes B,
$$

并且

$$
(I_{m_A}\otimes B)(A\otimes I_{n_B})
=
A\otimes B.
$$

在 $\mathbb F_2$ 中，

$$
A\otimes B+A\otimes B=0,
$$

所以

$$
\boxed{
\partial_1\partial_2=0
}
$$

以及

$$
\boxed{
H_XH_Z^{\mathsf T}=0
}.
$$

### 用单个指标检查两条路径

块计算可以再落到一个具体矩阵元上。固定起点 $z_{j,\beta}$ 和终点 $x_{i,\alpha}$。

沿第一条路径，$B$ 先把 $\beta$ 连到 $\alpha$，贡献 $B_{\alpha,\beta}$；随后 $A$ 把 $j$ 连到 $i$，贡献 $A_{i,j}$。总贡献是

$$
A_{i,j}B_{\alpha,\beta}.
$$

沿第二条路径，$A$ 先贡献 $A_{i,j}$，$B$ 再贡献 $B_{\alpha,\beta}$，总贡献仍是

$$
A_{i,j}B_{\alpha,\beta}.
$$

因此每个起点—终点对都收到两份相同贡献。模 $2$ 相加后它们逐项消失。这正是“乘积复形的边界连续作用两次为零”在 HGP 指标中的具体内容，也是 HGP 构造自动保证 CSS 对易的原因。

## 从四个 Kronecker 块读出 Tanner 图

现在矩阵已经构造完成，可以把非零矩阵元翻译成 Tanner 邻接。这里讨论的是抽象校验图：一侧是物理量子比特节点，另一侧是校验节点。具体综合征提取电路是否为每条校验配置一个辅助量子比特、使用几个辅助量子比特以及怎样调度门，是额外的实现选择。

回顾四类节点：

$$
q^{(1)}_{j,\alpha}
\in Q_1,
\qquad
q^{(2)}_{i,\beta}
\in Q_2,
$$

$$
x_{i,\alpha}
\in C_0,
\qquad
z_{j,\beta}
\in C_2.
$$

### 由 $A_{i,j}=1$ 产生的两类边

第一类来自 $H_X$ 的块 $A\otimes I_{m_B}$。其非零条件是

$$
A_{i,j}=1,
\qquad
\alpha=\alpha'.
$$

所以对每个固定的 $\alpha\in[m_B]$，

$$
x_{i,\alpha}
\longleftrightarrow
q^{(1)}_{j,\alpha}.
$$

这条边改变 $A$ 坐标 $j\leftrightarrow i$，固定 $B$ 的行坐标 $\alpha$。

第二类来自 $H_Z$ 的块 $A^{\mathsf T}\otimes I_{n_B}$。对每个固定的 $\beta\in[n_B]$，

$$
z_{j,\beta}
\longleftrightarrow
q^{(2)}_{i,\beta}.
$$

它仍由同一个非零元 $A_{i,j}=1$ 决定，只是 $A^{\mathsf T}$ 使校验矩阵的行由 $j$ 编号、列由 $i$ 编号。它改变 $A$ 坐标，固定 $B$ 的列坐标 $\beta$。

因此一条种子 Tanner 边 $i\leftrightarrow j$ 在 HGP 中复制成两族边：一族进入 $X$ 型校验与第一物理扇区之间，另一族进入 $Z$ 型校验与第二物理扇区之间。

### 由 $B_{\alpha,\beta}=1$ 产生的两类边

第三类来自 $H_X$ 的块 $I_{m_A}\otimes B$。对每个固定的 $i\in[m_A]$，

$$
x_{i,\alpha}
\longleftrightarrow
q^{(2)}_{i,\beta}.
$$

这条边改变 $B$ 坐标 $\beta\leftrightarrow\alpha$，固定 $A$ 的行坐标 $i$。

第四类来自 $H_Z$ 的块 $I_{n_A}\otimes B^{\mathsf T}$。对每个固定的 $j\in[n_A]$，

$$
z_{j,\beta}
\longleftrightarrow
q^{(1)}_{j,\alpha}.
$$

它也由 $B_{\alpha,\beta}=1$ 决定，改变 $B$ 坐标并固定 $A$ 的列坐标 $j$。

把四类边合在一起，可以写成紧凑的索引规则：

$$
A_{i,j}=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\alpha}&\longleftrightarrow q^{(1)}_{j,\alpha}
&&\text{对每个 }\alpha,\\
z_{j,\beta}&\longleftrightarrow q^{(2)}_{i,\beta}
&&\text{对每个 }\beta,
\end{aligned}
\right.
$$

$$
B_{\alpha,\beta}=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\alpha}&\longleftrightarrow q^{(2)}_{i,\beta}
&&\text{对每个 }i,\\
z_{j,\beta}&\longleftrightarrow q^{(1)}_{j,\alpha}
&&\text{对每个 }j.
\end{aligned}
\right.
$$

### 行与列的乘积方向

固定 $\alpha$ 时，节点

$$
\{x_{i,\alpha}\}_i
\quad\text{和}\quad
\{q^{(1)}_{j,\alpha}\}_j
$$

之间的邻接就是 $A$ 的 Tanner 图的一份副本。固定 $\beta$ 时，

$$
\{z_{j,\beta}\}_j
\quad\text{和}\quad
\{q^{(2)}_{i,\beta}\}_i
$$

之间也具有同一个 $A$ 关联模式。

同理，固定 $i$ 或固定 $j$ 时，另外两类边分别给出 $B$ Tanner 图的副本。因此一般 HGP 图天然分成两个乘积方向：

- $A$ 方向：只改变 $A$ 坐标，固定一个 $B$ 坐标；
- $B$ 方向：只改变 $B$ 坐标，固定一个 $A$ 坐标。

把两个方向画到平面上时，可以把它们命名为“行方向”和“列方向”，也可以命名为“水平”和“竖直”。这些名称来自布局选择；HGP 的内禀结论只是“每条边只改变一个因子坐标”。

四个块中总有一个恒等矩阵，所以每条边都固定一个坐标。不存在一条基本 Tanner 边同时把

$$
(j,\alpha)
\longrightarrow
(i,\beta)
$$

中的两个坐标都改变。换句话说，HGP 的四类边没有相对于乘积坐标的“对角边”。这项结构正是把大图拆成种子图副本的原因。

## 选读：与 S007 式 (1) 的记号转换

本节只用于阅读 S007，可直接跳到“长度、校验数与逻辑支撑”。一般 HGP 构造已经在 $A,B$ 记号下闭合。

S007 把两张经典种子矩阵写成

$$
H_1^{\mathrm{S007}}
\in\mathbb F_2^{r_1\times n_1},
\qquad
H_2^{\mathrm{S007}}
\in\mathbb F_2^{r_2\times n_2}.
$$

论文的式 (1) 是

$$
\mathcal H_X
=
\left[
H_1^{\mathrm{S007}}\otimes I_{n_2}
\;\middle|\;
I_{r_1}\otimes
\left(H_2^{\mathrm{S007}}\right)^{\mathsf T}
\right],
$$

$$
\mathcal H_Z
=
\left[
I_{n_1}\otimes H_2^{\mathrm{S007}}
\;\middle|\;
\left(H_1^{\mathrm{S007}}\right)^{\mathsf T}
\otimes I_{r_2}
\right].
$$

要与本文的公式逐块一致，应取

$$
A=H_1^{\mathrm{S007}},
\qquad
B=\left(H_2^{\mathrm{S007}}\right)^{\mathsf T}.
$$

于是尺寸对应为

$$
m_A=r_1,
\qquad
n_A=n_1,
\qquad
m_B=n_2,
\qquad
n_B=r_2.
$$

注意第二因子的方向发生了转置：本文把 $B$ 本身视为次数 $1$ 到次数 $0$ 的边界，而 S007 在 $\mathcal H_X$ 的第二块中直接写 $H_2^{\mathsf T}$。

在这组转换下，本文的节点标签对应为

$$
q^{(1)}_{j,\alpha}
\longleftrightarrow
q^A_{j,\ell},
\qquad
\alpha=\ell\in[n_2],
$$

$$
q^{(2)}_{i,\beta}
\longleftrightarrow
q^B_{i,m},
\qquad
\beta=m\in[r_2],
$$

$$
x_{i,\alpha}
\longleftrightarrow
x_{i,\ell},
\qquad
z_{j,\beta}
\longleftrightarrow
z_{j,m}.
$$

因此 S007 的四类边正是前一节规则的改名：

$$
H_1^{\mathrm{S007}}(i,j)=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\ell}&\longleftrightarrow q^A_{j,\ell},\\
z_{j,m}&\longleftrightarrow q^B_{i,m},
\end{aligned}
\right.
$$

$$
H_2^{\mathrm{S007}}(m,\ell)=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\ell}&\longleftrightarrow q^B_{i,m},\\
z_{j,m}&\longleftrightarrow q^A_{j,\ell}.
\end{aligned}
\right.
$$

S007 的图 1(b) 进一步把 $H_1$ 方向画成水平组，把 $H_2$ 方向画成竖直组，并把校验节点实现为综合征提取中的校验辅助量子比特。这些都是论文所选中性原子布局和电路模型中的物理语义。ONEX 怎样分别求解行、列一维重排，属于从 Tanner 图到硬件执行计划的下一层问题；它不改变 HGP 的代数定义，也不能反过来说明一般 HGP 必须采用水平／竖直布局或一校验一辅助量子比特的实现。

S007 第 6 节的 LP 示例同样是来源特定的执行案例。它展示的单项式种子矩阵可以用来读取循环移位标签，但没有同时展示一般 LP 记号中的完整第二因子；因此不能只凭该矩阵重建完整 LP 校验矩阵、全部扇区或实例参数。具体执行层次见 [[S007 中 LP 码的分层执行]]。

## 长度、校验数与逻辑支撑

从 $C_1=Q_1\oplus Q_2$ 已经得到物理比特数

$$
N=n_Am_B+m_An_B.
$$

写出的 $X$ 型校验行数和 $Z$ 型校验行数分别为

$$
R_X=m_Am_B,
\qquad
R_Z=n_An_B.
$$

这里是“写出的行数”，不一定等于独立稳定子数。若校验行之间存在二进制线性关系，矩阵秩会小于行数。

因为 $X$ 型与 $Z$ 型生成元在二进制辛表示中占据不同分量，而两类生成元又满足 CSS 对易，独立稳定子数为

$$
\operatorname{rank}H_X+\operatorname{rank}H_Z.
$$

所以逻辑比特数可以直接由展开后的二进制矩阵计算：

$$
\boxed{
K
=
N-\operatorname{rank}H_X-\operatorname{rank}H_Z
}.
$$

这个秩公式对任意有限 HGP 实例都可直接使用，不需要先知道 Künneth 分解。

在本文的链方向

$$
C_2
\xrightarrow{H_Z^{\mathsf T}}
C_1
\xrightarrow{H_X}
C_0
$$

中，逻辑 $Z$ 支撑类是

$$
\boxed{
H_1(\mathcal C)
=
\frac{\ker H_X}
{\operatorname{im}H_Z^{\mathsf T}}
}.
$$

分子先选出与所有 $X$ 型校验交换的 $Z$ 支撑，分母再把 $Z$ 型稳定子支撑视为平凡方向。把各链群对偶化并反转箭头，得到对偶上链复形 $\mathcal C^\vee$；它的一阶上同调给出逻辑 $X$ 支撑类：

$$
\boxed{
H^1(\mathcal C^\vee)
=
\frac{\ker H_Z}
{\operatorname{im}H_X^{\mathsf T}}
}.
$$

这两个商空间都是二进制的 Pauli 支撑类空间，不是编码 Hilbert 空间本身。若它们的共同维数为 $K$，编码子空间的复维数才是 $2^K$。

它们也不能与 $Q_1,Q_2$ 混同。$Q_1,Q_2$ 是取核和取商之前的两类物理坐标；同调或上同调则是在整个 $C_1$ 中施加检查并商掉稳定子以后得到的逻辑类。关于 CSS 商空间的更完整解释见 [[CSS码中的cochain complex]]。

## 选读：Künneth 给出的两个逻辑来源

本节回答一个已经出现的问题：能否不对大矩阵直接求秩，而是从两份种子复形看出逻辑 $Z$ 支撑来自哪里？只关心一般构造、Tanner 图或 qLDPC 条件时，可以跳过本节。

在域 $\mathbb F_2$ 上，Künneth 同构给出

$$
\boxed{
H_1(\mathcal A\otimes\mathcal B)
\cong
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B
}.
$$

这里

$$
\operatorname{coker}A=A_0/\operatorname{im}A,
\qquad
\operatorname{coker}B=B_0/\operatorname{im}B.
$$

第一项把 $A$ 方向的闭合变量向量与 $B$ 行坐标中的余类配对，可以在第一物理扇区 $A_1\otimes B_0$ 中选择代表元；第二项交换两个因子的角色，可以在第二物理扇区 $A_0\otimes B_1$ 中选择代表元。这里说的是逻辑类的两个来源，不是说整个物理扇区都由逻辑算符组成。给代表元加上边界以后，它也可能同时占据两个物理扇区。

定义

$$
k_A=\dim\ker A,
\qquad
k_A^{\mathsf T}=\dim\ker A^{\mathsf T},
$$

$$
k_B=\dim\ker B,
\qquad
k_B^{\mathsf T}=\dim\ker B^{\mathsf T}.
$$

有限维对偶给出

$$
\dim\operatorname{coker}A=k_A^{\mathsf T},
\qquad
\dim\operatorname{coker}B=k_B^{\mathsf T}.
$$

因此

$$
\boxed{
K
=
k_Ak_B^{\mathsf T}
+
k_A^{\mathsf T}k_B
}.
$$

这条公式与前面的二进制秩公式计算同一个 $K$，但额外显示了两个同调来源。完整的比较映射、域上证明和一般系数边界见 [[Künneth 分解]]。

“系数是域”不能省略。LP 码通常先在环或群代数上作模张量积；一般环上的乘积同调可能涉及 $\operatorname{Tor}$、谱序列微分和扩张问题，所以上面的直和与维数公式不能无条件搬到 LP 码。

## HGP 何时形成 qLDPC 码族

HGP 构造对任意 $A,B$ 都给出一个 CSS 码，但“是 CSS 码”不等于“是量子低密度奇偶校验码”。

对一族种子矩阵，定义最大行重和最大列重：

$$
r_A=\max_i\operatorname{wt}(A_{i,*}),
\qquad
c_A=\max_j\operatorname{wt}(A_{*,j}),
$$

$$
r_B=\max_\alpha\operatorname{wt}(B_{\alpha,*}),
\qquad
c_B=\max_\beta\operatorname{wt}(B_{*,\beta}).
$$

先看量子校验的行重。一个 $X$ 型校验 $x_{i,\alpha}$ 在第一扇区沿 $A$ 的第 $i$ 行取邻居，在第二扇区沿 $B$ 的第 $\alpha$ 行取邻居。两个扇区不重叠，所以

$$
\operatorname{wt}(H_X\text{ 的第 }(i,\alpha)\text{ 行})
=
\operatorname{wt}(A_{i,*})
+
\operatorname{wt}(B_{\alpha,*})
\le r_A+r_B.
$$

一个 $Z$ 型校验 $z_{j,\beta}$ 在第一扇区读取 $B$ 的第 $\beta$ 列，在第二扇区读取 $A$ 的第 $j$ 列，因此

$$
\operatorname{wt}(H_Z\text{ 的第 }(j,\beta)\text{ 行})
=
\operatorname{wt}(B_{*,\beta})
+
\operatorname{wt}(A_{*,j})
\le c_B+c_A.
$$

再看每个物理量子比特参与多少校验。对第一扇区的 $q^{(1)}_{j,\alpha}$：

$$
\operatorname{wt}(H_X\text{ 的第 }(j,\alpha)\text{ 列})
=
\operatorname{wt}(A_{*,j})
\le c_A,
$$

$$
\operatorname{wt}(H_Z\text{ 的第 }(j,\alpha)\text{ 列})
=
\operatorname{wt}(B_{\alpha,*})
\le r_B.
$$

对第二扇区的 $q^{(2)}_{i,\beta}$：

$$
\operatorname{wt}(H_X\text{ 的第 }(i,\beta)\text{ 列})
=
\operatorname{wt}(B_{*,\beta})
\le c_B,
$$

$$
\operatorname{wt}(H_Z\text{ 的第 }(i,\beta)\text{ 列})
=
\operatorname{wt}(A_{i,*})
\le r_A.
$$

因此，一个直接的充分条件是：随着码长增长，$A,B$ 的行重和列重都由与规模无关的常数统一限制。此时 $H_X,H_Z$ 的校验重量和每个物理量子比特参与的校验数也都统一有界，所得 HGP 家族才是 qLDPC 家族。

若种子矩阵稠密，HGP 仍然是合法 CSS 构造，但输出一般不是 qLDPC。稀疏性本身也不推出正编码率或大码距；这些还取决于种子秩、核维数和距离。

## 选读：条件化的 $\sqrt N$ 距离基准

文献中经常用

$$
d=\Theta(\sqrt N)
$$

概括标准等尺度 HGP 家族的距离基准。下面只说明这个尺度关系在什么附加条件下成立；本文不从四块公式证明一条普遍的 HGP 距离定理。

先取一族

$$
A\in\mathbb F_2^{m\times n},
\qquad
B=A^{\mathsf T},
\qquad
m<n,
$$

并假设

$$
m=\Theta(n),
\qquad
k=n-m=\Theta(n),
$$

以及 $A$ 满行秩。由尺寸公式可直接得到

$$
N=n^2+m^2=\Theta(n^2).
$$

在这个满秩对称特例中，两张量子校验矩阵都具有秩 $mn$，因此

$$
K
=
n^2+m^2-2mn
=
(n-m)^2
=
k^2
=
\Theta(N).
$$

所以长度和编码率结论只需要线性代数与尺度假设。

距离还需要独立输入。设所选种子族具有一个线性增长的经典距离尺度

$$
d_{\mathrm{cl}}=\Theta(n),
$$

并且已经由适用于该种子族的距离定理或显式逻辑算符分析证明，存在与 $n$ 无关的常数 $c,C>0$，使量子距离满足

$$
c\,d_{\mathrm{cl}}
\le d
\le
C\,d_{\mathrm{cl}}.
$$

这时才可以推出

$$
d=\Theta(n)=\Theta(\sqrt N).
$$

上面的两侧距离比较是本节的额外假设，不是本文已经证明的结论。若只知道种子的经典距离是线性的，却没有证明相应 HGP 量子距离与它同阶，就不能仅凭乘积形式写出 $d=\Theta(\sqrt N)$；更不能把某个特例中的精确等式推广到任意 $A,B$。

若还要求这一家族是 qLDPC，则必须另外检查 $A$ 的行重和列重是否统一有界。于是“常数率”“平方根距离”和“qLDPC”分别来自秩、距离比较和稀疏性三组条件，不能相互替代。

## 选读：从 HGP 到 LP 的安全接口

HGP 的三项复形、两个中间物理扇区和四块排列是理解提升乘积（lifted-product, LP）码的入口。不过，“把二进制条目换成环元素”只是一句方向提示，还不足以保证得到合法 CSS 块。

在常见写法中，先取有限维 $\mathbb F_2$-代数 $R$，并用环值矩阵

$$
A\in R^{m_A\times n_A},
\qquad
B\in R^{m_B\times n_B}.
$$

要把它们变成二进制矩阵，还需给出保持所需代数运算的块表示

$$
\Phi:R\longrightarrow
\operatorname{Mat}_{\ell\times\ell}(\mathbb F_2).
$$

一个系数对应什么二进制块，取决于它在 $R$ 中的类型：

- 循环单项式或群基元素通常对应一个置换块；
- 多项式或一般群代数元素对应若干置换块在 $\mathbb F_2$ 中的和，重合项可能抵消；
- 任意有限维代数中的一般元素只保证对应一个线性块，不必是置换，也不必具有单一移位的图像。

因此不能把“环元素”“群代数元素”和“一个置换”当作同义词。

HGP 的四块骨架只有在模结构和块表示彼此相容时才能保留。在交换、特征为 $2$ 的常见情形，还需要系数交叉对易，并需要一个与二进制转置相容的反对合，才能把两路径相消翻译成 CSS 对易。非交换情形则必须区分右模与左模，并用彼此交换的右乘、左乘作用控制乘法次序；仅仅把转置改写成一个形式符号 $*$ 并不足够。

即使 CSS 对易已经成立，LP 也不会自动继承域上 HGP 的全部结论：二进制行重和列重是否有界、编码率和距离是否良好、Künneth 维数公式是否适用，都需要额外条件。完整的循环展开、反对合、左右模和平衡张量积（balanced tensor product）见 [[Lifted product code]]。

S007 第 6 节展示的是单项式循环标签的特例，所以其中每个已展示条目可以读成一条原型边携带的循环移位。但该节没有同时给出完整第二因子，不能仅由那张矩阵重建完整 LP 校验矩阵、全部扇区或参数；其提升间重排、提升内重排、门执行和方向切换也属于具体中性原子编译方案，而不是一般 LP 定义。

## 回收整条构造链

HGP 的结构可以按下面的因果顺序读取。

两张经典矩阵先被放进

$$
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
\qquad
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0.
$$

总次数把它们的张量积排成

$$
C_2=A_1\otimes B_1,
$$

$$
C_1=(A_1\otimes B_0)\oplus(A_0\otimes B_1),
$$

$$
C_0=A_0\otimes B_0.
$$

中间直和给出两类物理量子比特坐标。乘积边界在两个因子上分别作用，得到

$$
H_X
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right],
$$

$$
H_Z
=
\left[
I_{n_A}\otimes B^{\mathsf T}
\;\middle|\;
A^{\mathsf T}\otimes I_{n_B}
\right].
$$

从 $C_2$ 到 $C_0$ 的两条路径都给出 $A\otimes B$；一般系数下它们符号相反，在 $\mathbb F_2$ 中则是两份相同贡献相加为零。因此

$$
H_XH_Z^{\mathsf T}=0.
$$

四个块中的恒等矩阵固定一个乘积坐标，另一张种子矩阵只改变另一个坐标，于是 Tanner 图分成 $A$ 方向和 $B$ 方向的种子图副本，并且没有同时改变两个坐标的基本边。

这套构造自动给出 CSS 对易。qLDPC、正编码率、平方根距离和 LP 的良好参数都不是自动结果；每一项都需要在相应位置加入额外假设。

## 来源与延伸

- [[Chain complex 与 cochain complex]]：链复形、边界、同调与上同调的基础解释。
- [[CSS码中的cochain complex]]：CSS 逻辑 Pauli 支撑商空间以及链／上链方向的区分。
- [[Tensor product 对 direct sum 的分配律]]：张量积如何把两个直和分解成双指标分量。
- [[Cochain complex 的 tensor product]]：总次数、直和展开和乘积微分；其中采用升次数写法，本文使用其降次数链版本。
- [[Künneth 分解]]：域上的完整证明、HGP 的两个逻辑同调来源以及一般系数环的边界。
- [[Lifted product code]]：环值块、循环提升、反对合、二进制展开、左右模和平衡张量积。
- [[S007 中 LP 码的分层执行]]：S007 的外层乘积与内层提升两层执行语义。
- [S007 全文译本](../../Translations/S007.full.zh-CN.md)：式 (1)、四类边、图 1(b)、第 3.1 节和第 6 节。
- [S007 来源登记](../../Papers/SOURCES.md#S007)：arXiv:2608.20164 v1 的版本与本地文件信息。
