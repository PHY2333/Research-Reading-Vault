# 对角相位门的 Clifford 层级

一个对角门只给计算基态乘上相位，不改变它的比特标签。相位角越细、参与相位条件的比特越多，这个门的 Clifford 层级是否就越高？对下面这一类单项式相位门，答案可以精确写成

$$
\boxed{k=m+r-1.}
$$

这里 $2^m$ 是相位中的分母，$r$ 是实际参与相位乘积的比特数。这个公式见 S008 §2.1 式 (1)；其一般分类背景是 Cui–Gottesman–Krishna 的对角 Clifford 层级定理。[^S008][^CGK17] 本文只处理比特上的非恒定单项式，直接从递归定义证明公式，不把一般分类定理当作证明的前提。

证明分成两个方向：先证明这个门属于第 $m+r-1$ 层，再证明它不可能属于更低层。两部分都围绕同一个计算展开：**对角门共轭一个比特翻转时，出现的是翻转前后的相位差。** 上界需要控制所有 Pauli 所产生的相位差；最低层数则要找出一串相位差，证明它不会过早变成全局相位。

## 1. 门的参数分别表示什么

固定 $n\ge1$ 个比特，以

$$
|\boldsymbol x\rangle=|x_1,\ldots,x_n\rangle,
\qquad x_j\in\{0,1\},
$$

标记计算基。记号 $\mathbb F_2^n$ 在这里表示这些二进制标签，不要求有限域扩张的知识。

给定 $\boldsymbol a=(a_1,\ldots,a_n)\in\mathbb F_2^n$，定义它的**支持**与**汉明重量**：

$$
A=\operatorname{supp}(\boldsymbol a)
=\{j:a_j=1\},
\qquad
r=\operatorname{wt}(\boldsymbol a)=|A|.
$$

支持记录哪些位置参与，汉明重量记录参与的位置有多少个。把相位中的乘积记为

$$
q_A(\boldsymbol x)=\prod_{j\in A}x_j.
$$

当 $A\ne\varnothing$ 时，$q_A$ 恰好在所有参与比特均为 $1$ 时取 $1$，其余时候取 $0$。因此，

$$
U_{m,\boldsymbol a}|\boldsymbol x\rangle
=
\exp\!\left(\frac{2\pi i}{2^m}q_A(\boldsymbol x)\right)
|\boldsymbol x\rangle,
\qquad m\ge1,
$$

就是只在这个条件满足时施加相位 $e^{2\pi i/2^m}$ 的门。由于门只取决于支持，也简写为 $U_{m,A}$。

例如，在十个比特中取 $A=\{2,7\}$，相位只由 $x_2x_7$ 决定。此时 $n=10$，但 $r=2$；另外八个比特不参与相位条件，不能把它们算进公式中的 $r$。

### 二进制标签不意味着相位按模 $2$ 运算

标签的逐位加法记作 XOR，使用符号 $\oplus$。相位中的乘积、加减法和分母则按普通整数或实数运算。例如，

$$
x_j\oplus1=1-x_j,
\qquad
x\oplus y=x+y-2xy,
\qquad x,y\in\{0,1\}.
$$

第二个等式是整数等式。不能在含有分母 $2^m$ 的相位中直接用 $x+y$ 替代 $x\oplus y$：在 $x=y=1$ 时，两者相差 $2$；若 $m=2$，这会让指数中的相位相差 $\pi$，并不是同一个门。

为统一处理这些相位，给定实值函数 $f:\mathbb F_2^n\to\mathbb R$，记

$$
D_f|\boldsymbol x\rangle
=e^{2\pi i f(\boldsymbol x)}|\boldsymbol x\rangle.
$$

于是

$$
f_{m,A}(\boldsymbol x)=\frac{q_A(\boldsymbol x)}{2^m},
\qquad
U_{m,A}=D_{f_{m,A}}.
$$

相位函数具有周期性：

$$
D_f=D_g
\quad\Longleftrightarrow\quad
f(\boldsymbol x)-g(\boldsymbol x)\in\mathbb Z
\quad\text{对每个 }\boldsymbol x.
$$

所以后文可以把相位函数按模 $1$ 比较，但不能无条件把它改成模 $2$ 的多项式。若 $f-g$ 模 $1$ 是同一个常数，则两个门只相差全局相位。

## 2. “最低第 $k$ 层”需要证明什么

### 从多比特 Pauli 到递归定义

令 $X_j$ 翻转第 $j$ 个比特，$Z_j$ 按该比特的取值加上符号：

$$
X_j|\boldsymbol x\rangle
=|\boldsymbol x\oplus\boldsymbol e_j\rangle,
\qquad
Z_j|\boldsymbol x\rangle
=(-1)^{x_j}|\boldsymbol x\rangle,
$$

其中 $\boldsymbol e_j$ 只有第 $j$ 个分量是 $1$。对于二进制向量 $\boldsymbol u,\boldsymbol v$，定义

$$
X^{\boldsymbol u}=\prod_{j=1}^nX_j^{u_j},
\qquad
Z^{\boldsymbol v}=\prod_{j=1}^nZ_j^{v_j}.
$$

它们分别翻转 $\boldsymbol u$ 指定的位置、施加 $\boldsymbol v$ 指定的 $Z$ 相位。所有多比特 Pauli 可以写为

$$
\mathcal P_n
=
\left\{
 i^tX^{\boldsymbol u}Z^{\boldsymbol v}:
 t\in\{0,1,2,3\},\quad
 \boldsymbol u,\boldsymbol v\in\mathbb F_2^n
\right\}.
$$

同一比特上 $X_jZ_j=-Z_jX_j$，不同位置的操作交换。因此 Pauli 的乘积仍是 Pauli，Pauli 共轭另一个 Pauli 也仍是 Pauli。

本文忽略全局相位，并采用把任意全局相位纳入第一层的约定：[^CGK17]

$$
\mathcal C_1
=
\{e^{i\phi}P:\phi\in\mathbb R,\ P\in\mathcal P_n\},
$$

$$
\mathcal C_k
=
\left\{
U\text{ 为酉算符}:
UPU^\dagger\in\mathcal C_{k-1}
\text{ 对所有 }P\in\mathcal P_n
\right\},
\qquad k\ge2.
$$

第二层就是 Clifford 门：共轭任何 Pauli 后仍得到 Pauli，允许相差全局相位。第三层要求共轭任何 Pauli 后得到 Clifford 门。这里的层数衡量这种**递归共轭条件**，不是线路深度，也不是门的数量。

这些层彼此包含。首先，Pauli 共轭保持 Pauli，故 $\mathcal C_1\subseteq\mathcal C_2$。若已经知道 $\mathcal C_{j-1}\subseteq\mathcal C_j$，则 $U\in\mathcal C_j$ 的所有 Pauli 共轭像都在 $\mathcal C_{j-1}$，也就在 $\mathcal C_j$，所以 $U\in\mathcal C_{j+1}$。归纳得到

$$
\mathcal C_1\subseteq\mathcal C_2\subseteq\mathcal C_3\subseteq\cdots.
$$

因而，本文的目标不只是一个包含关系，而是对 $A\ne\varnothing$ 证明

$$
U_{m,A}\in\mathcal C_{m+|A|-1},
$$

并且在 $m+|A|-1>1$ 时证明

$$
U_{m,A}\notin\mathcal C_{m+|A|-2}.
$$

排除紧邻的下一低层，就排除了所有更低层。若 $m=1$、$|A|=1$，门就是某个 $Z_j$，最低编号直接是 $1$。

### 全局相位单独处理

按空乘积约定 $q_{\varnothing}=1$，$\boldsymbol a=0$ 给出

$$
U_{m,0}=e^{2\pi i/2^m}I.
$$

它只是恒等门的全局相位版本，属于所有正整数编号的层。若也为它记录最低正整数编号，该编号是 $1$；不能把非空支持的公式套过来，称它的最低层数为 $m-1$。

后文凡谈单项式门的最低层数，都限定 $A\ne\varnothing$。中间计算仍允许出现空支持项，但把它们作为全局相位处理。

### 一个稍后要用的乘法事实

递归中会反复出现“一个对角门右乘一个 Pauli”。对每个整数 $\ell\ge1$，确实有

$$
V\in\mathcal C_\ell
\quad\Longleftrightarrow\quad
VQ\in\mathcal C_\ell,
\qquad Q\in\mathcal P_n.
\tag{1}
$$

当 $\ell=1$ 时，这是 Pauli 乘法封闭性。对 $\ell\ge2$，若 $V\in\mathcal C_\ell$，则对任意 Pauli $P$，

$$
(VQ)P(VQ)^\dagger
=V(QPQ^\dagger)V^\dagger
\in\mathcal C_{\ell-1},
$$

因为括号中的 $QPQ^\dagger$ 仍是 Pauli。反向推论只需再右乘 $Q^\dagger$。

注意，这里只证明了**右乘 Pauli**不改变层级归属，没有把任意两个同层门的乘积当作同层门。后面的上界证明也不会假定 $k\ge3$ 的整个 $\mathcal C_k$ 是群。

## 3. 共轭一个翻转，为什么出现相位差分

对任意对角门 $D_f$，按照从右到左的算符作用顺序计算：

$$
\begin{aligned}
D_fX^{\boldsymbol u}D_f^\dagger|\boldsymbol x\rangle
&=e^{-2\pi i f(\boldsymbol x)}
  D_f|\boldsymbol x\oplus\boldsymbol u\rangle\\
&=e^{2\pi i[f(\boldsymbol x\oplus\boldsymbol u)-f(\boldsymbol x)]}
  |\boldsymbol x\oplus\boldsymbol u\rangle.
\end{aligned}
\tag{2}
$$

我们希望把结果写成“一个对角门，再乘一个翻转”的矩阵形式。为此定义

$$
\Delta_{\boldsymbol u}f(\boldsymbol x)
=f(\boldsymbol x)-f(\boldsymbol x\oplus\boldsymbol u).
\tag{3}
$$

这是沿比特翻转方向 $\boldsymbol u$ 的**有限差分**，不是连续变量的导数。式 (2) 中相位用输入标签 $\boldsymbol x$ 表示，而左侧对角因子要在翻转后的标签上取值，因此

$$
\Delta_{\boldsymbol u}f(\boldsymbol x\oplus\boldsymbol u)
=f(\boldsymbol x\oplus\boldsymbol u)-f(\boldsymbol x).
$$

于是准确的算符等式是

$$
\boxed{
D_fX^{\boldsymbol u}D_f^\dagger
=D_{\Delta_{\boldsymbol u}f}X^{\boldsymbol u}.
}
\tag{4}
$$

特别地，右乘 $X^{\boldsymbol u}$ 后，翻转被消去：

$$
D_{\Delta_{\boldsymbol u}f}
=D_fX^{\boldsymbol u}D_f^\dagger X^{\boldsymbol u}.
\tag{5}
$$

这固定了本文所有差分的正负号与共轭次序。

由于 $D_f$ 与每个 $Z_j$ 交换，对任意 $P=i^tX^{\boldsymbol u}Z^{\boldsymbol v}$ 还有

$$
D_fPD_f^\dagger
=D_{\Delta_{\boldsymbol u}f}P.
\tag{6}
$$

结合右乘 Pauli 的性质 (1)，递归定义转化为

$$
\boxed{
D_f\in\mathcal C_k
\quad\Longleftrightarrow\quad
D_{\Delta_{\boldsymbol u}f}\in\mathcal C_{k-1}
\text{ 对所有 }\boldsymbol u\in\mathbb F_2^n,
}
\qquad k\ge2.
\tag{7}
$$

必要性来自取 $P=X^{\boldsymbol u}$ 后去掉右侧 Pauli；充分性来自式 (6)，它已经覆盖所有 Pauli，而不只是单比特生成元。

相位函数换一个模 $1$ 的代表，不影响这个判据：整数值函数的差分仍是整数值函数。给原门增加全局相位对应于给 $f$ 加一个常数，而常数的差分直接为零。

### 先看一个参与比特的翻转

记 $\Delta_j=\Delta_{\boldsymbol e_j}$。若 $j\notin A$，$f_{m,A}$ 不依赖 $x_j$，所以 $\Delta_jf_{m,A}=0$。若 $j\in A$，则

$$
\begin{aligned}
\Delta_jf_{m,A}(\boldsymbol x)
&=\frac{x_j-(1-x_j)}{2^m}
  q_{A\setminus\{j\}}(\boldsymbol x)\\
&=\frac{2x_j-1}{2^m}
  q_{A\setminus\{j\}}(\boldsymbol x)\\
&=\frac{q_A(\boldsymbol x)}{2^{m-1}}
  -\frac{q_{A\setminus\{j\}}(\boldsymbol x)}{2^m}.
\end{aligned}
\tag{8}
$$

这一步出现了两种变化。第一项保留原来的支持，但分母少一个 $2$；第二项保留分母，但支持少一个位置。若暂时把

$$
w(m,A)=m+|A|-1
$$

视为一个待验证的计数，那么在去掉整数相位和常数相位后，每个保留下来的单项式项的计数都少 $1$。这正是它可能与递归层数一致的原因。

两个边界也能直接从式 (8) 读出。若 $m=1$，第一项是整数值函数 $q_A$，对应恒等相位；若 $|A|=1$，第二项是常数 $-1/2^m$，只产生全局相位。它们都不需要引入新的非平凡门。

例如，对 $T=\operatorname{diag}(1,e^{i\pi/4})$，有 $f(x)=x/8$。此处只有一个比特，记 $\Delta=\Delta_1$，于是

$$
\Delta f(x)=\frac{x}{4}-\frac18,
\qquad
TXT^\dagger=e^{-i\pi/4}SX,
\qquad
S=\operatorname{diag}(1,i).
\tag{9}
$$

这里分母从 $8$ 降到了 $4$，其余部分只是一个全局相位和右侧的 Pauli $X$。这展示了式 (8) 中“分母减少”的分支，但还不是一般上界的完整证明：多个位置同时翻转时会发生什么？产生多个相位项后，为什么它们的乘积仍符合所需的层级条件？

## 4. 上界：所有 Pauli 都使相位计数下降

这一节补齐刚才的两个问题。先直接计算任意翻转方向，而不是从单比特生成元未经证明地推广；再用一个稍强的归纳命题，同时控制共轭后出现的有限个相位项。

### 4.1 同时翻转若干位

固定 $\boldsymbol u$，把原支持分成

$$
H=A\cap\operatorname{supp}(\boldsymbol u),
\qquad
J=A\setminus H,
\qquad
h=|H|.
$$

$H$ 是参与相位、又被翻转的位置；$J$ 是参与相位、但没有被翻转的位置。支持以外的翻转不会改变相位。

翻转后，$H$ 中每个 $x_j$ 变成 $1-x_j$。按整数乘法展开，得到

$$
\begin{aligned}
q_A(\boldsymbol x\oplus\boldsymbol u)
&=q_J(\boldsymbol x)\prod_{j\in H}(1-x_j)\\
&=\sum_{B\subseteq H}(-1)^{|B|}
  q_{J\cup B}(\boldsymbol x).
\end{aligned}
\tag{10}
$$

展开中的每一项都来自：在 $H$ 的一部分位置选择 $-x_j$，其余位置选择 $1$。其中 $B=H$ 的一项保留完整支持 $A$。把它与原来的 $q_A$ 合并：

$$
\Delta_{\boldsymbol u}f_{m,A}
=
\frac{1-(-1)^h}{2^m}q_A
-
\frac{1}{2^m}
\sum_{B\subsetneq H}(-1)^{|B|}q_{J\cup B}.
\tag{11}
$$

若 $H=\varnothing$，右边为零。若 $H\ne\varnothing$，保留完整支持的系数 $1-(-1)^h$ 只能是 $0$ 或 $2$：它要么消失，要么把分母从 $2^m$ 降为 $2^{m-1}$；当 $m=1$ 时，后一种情况也是整数相位，仍可去掉。

例如，若相位乘积是 $x_1x_2$，同时翻转这两个位置，则

$$
x_1x_2-(1-x_1)(1-x_2)=x_1+x_2-1.
$$

完整的二次项恰好抵消，留下两个单点支持项和一个常数。这是 $h=2$ 时式 (11) 的具体样子。

其余各项中 $B\subsetneq H$，故

$$
|J\cup B|\le |A|-1.
$$

因此它们虽然保留分母 $2^m$，支持却至少少一个位置。若 $J\cup B=\varnothing$，该项只贡献常数相位。

这证明了一个不依赖层级分类的计算事实：**对任意方向 $\boldsymbol u$，一个计数为 $w$ 的单项式相位经过差分后，模 $1$ 可以写成常数加若干整数倍的非空支持单项式相位，而每个剩余项的计数至多是 $w-1$。** 当 $w=1$ 时，只剩常数相位。

### 4.2 为什么这些相位项可以合起来使用

现在对正整数 $k$ 证明下面的上界命题：若

$$
F(\boldsymbol x)
=\gamma+
\sum_{\alpha=1}^{N}
 c_\alpha\frac{q_{A_\alpha}(\boldsymbol x)}{2^{m_\alpha}},
$$

其中 $\gamma\in\mathbb R$、$c_\alpha\in\mathbb Z$、$m_\alpha\ge1$、$A_\alpha\ne\varnothing$，并且每一项都满足

$$
m_\alpha+|A_\alpha|-1\le k,
\tag{12}
$$

那么

$$
D_F\in\mathcal C_k.
\tag{13}
$$

这里 $N$ 有限，也允许为零。整数系数容纳重复相乘和逆门，因为

$$
D_F=e^{2\pi i\gamma}
\prod_{\alpha=1}^{N}U_{m_\alpha,A_\alpha}^{c_\alpha}.
$$

把归纳命题扩大到这样的有限和，是因为一次差分就会产生有限和；这不是预先假定同层乘法封闭。

**归纳起点 $k=1$。** 由于 $m_\alpha\ge1$、$|A_\alpha|\ge1$，条件 (12) 迫使每一项都是 $x_j/2$ 的整数倍。合并同一位置的项后，

$$
F(\boldsymbol x)
=\gamma+\frac12\sum_{j=1}^n b_jx_j,
\qquad b_j\in\mathbb Z.
$$

所以

$$
D_F=e^{2\pi i\gamma}\prod_{j=1}^n Z_j^{b_j}
\in\mathcal C_1.
$$

**归纳步骤。** 设命题已对 $k-1$ 成立，考虑满足 (12) 的 $F$。对任意 $\boldsymbol u$，差分逐项作用：

$$
\Delta_{\boldsymbol u}F
=
\sum_{\alpha=1}^{N}
 c_\alpha\Delta_{\boldsymbol u}f_{m_\alpha,A_\alpha}.
$$

由上一小节，每一项都能改写为常数加计数至多 $k-1$ 的单项式相位之和。合起来仍是归纳假设允许的形式，因此

$$
D_{\Delta_{\boldsymbol u}F}\in\mathcal C_{k-1}
\quad\text{对所有 }\boldsymbol u.
$$

相位差分判据 (7) 随即给出 $D_F\in\mathcal C_k$。上界命题证明完毕。

最后取 $N=1$、$c_1=1$、$\gamma=0$，就得到原来需要的结论：

$$
\boxed{U_{m,A}\in\mathcal C_{m+|A|-1}.}
\tag{14}
$$

至此，所有 Pauli、多个相位项的合并，以及 $m=1$ 或单点支持产生的特殊项，都已包含在同一个上界证明中。但“至多在这一层”还没有排除相位抵消导致更低层的可能性。

## 5. 下界：构造一串不会过早成为全局相位的差分

### 5.1 低层门经过足够多次差分后必须成为全局相位

先从第一层看。一个对角的第一层门必为

$$
D_f=e^{i\phi}Z^{\boldsymbol v}.
$$

因为若 Pauli 中的 $X^{\boldsymbol u}$ 有非零翻转，它就会改变某些计算基标签，不能是对角矩阵。利用式 (5)，

$$
D_{\Delta_{\boldsymbol u}f}
=D_fX^{\boldsymbol u}D_f^\dagger X^{\boldsymbol u}
=(-1)^{\sum_jv_ju_j}I.
$$

所以第一层对角门经过一次任意方向的差分，就成为全局相位。

若 $D_f\in\mathcal C_s$ 且 $s\ge2$，由判据 (7)，一次差分后的对角门在 $\mathcal C_{s-1}$；继续应用同一个判据，经过 $s-1$ 次差分后在 $\mathcal C_1$，再差分一次便是全局相位。因此，

$$
\boxed{
\begin{gathered}
D_f\in\mathcal C_s\quad\Longrightarrow\\
\Delta_{\boldsymbol u_s}\cdots\Delta_{\boldsymbol u_1}f
\text{ 在模 }1\text{ 意义下为常数}\\
\text{（对任意方向序列）}.
\end{gathered}
}
\tag{15}
$$

这里允许方向重复。“模 $1$ 为常数”指它给每个计算基态相同的相位，不要求所选实值代表逐点相等。我们也没有把全局相位另行编号为第 $0$ 层。

现在令

$$
k=m+r-1>1.
$$

若原门其实属于 $\mathcal C_{k-1}$，那么任意 $k-1$ 次差分都必须满足 (15)。所以只要找到一串恰好 $k-1$ 次的差分，使结果仍有非平凡的相对相位，就排除了这个可能性。

### 5.2 先沿不同位置差分，再沿最后一个位置重复差分

把非空支持依次记为

$$
A=\{j_1,\ldots,j_r\},
$$

并定义取值为 $\pm1$ 的函数

$$
\sigma_j(\boldsymbol x)=2x_j-1.
$$

最关键的两个单变量计算是

$$
\Delta_jx_j=2x_j-1=\sigma_j,
\qquad
\Delta_j\sigma_j=2\sigma_j.
\tag{16}
$$

第一个等式把一个比特变量变成符号；第二个等式说明沿同一位置继续差分时，符号不会消失，而是多出一个因子 $2$。这就是为什么只数多项式的普通次数不够，相位分母也必须进入层级公式。

先依次沿 $j_1,\ldots,j_{r-1}$ 差分，每个位置一次。尚未作用的变量在相应差分中保持不动，因此逐次得到

$$
\Delta_{j_{r-1}}\cdots\Delta_{j_1}f_{m,A}
=
\frac{x_{j_r}}{2^m}
\prod_{t=1}^{r-1}\sigma_{j_t}.
\tag{17}
$$

若 $r=1$，这一步不做任何差分，空乘积等于 $1$，式 (17) 就是原函数。

**情形一：$m=1$。** 此时 $k-1=r-1$，式 (17) 已完成所需的全部差分。因为符号乘积只有 $+1$ 或 $-1$，而

$$
-\frac{x_{j_r}}2\equiv\frac{x_{j_r}}2\pmod1,
$$

所以结果满足

$$
\Delta_{j_{r-1}}\cdots\Delta_{j_1}f_{1,A}
\equiv\frac{x_{j_r}}2\pmod1.
\tag{18}
$$

固定其余比特，让 $x_{j_r}$ 从 $0$ 变成 $1$，所得相位从 $1$ 变成 $-1$。这不是全局相位。因此当 $r>1$ 时，$U_{1,A}\notin\mathcal C_{r-1}$。剩下的 $r=1$ 正是已经处理的 $Z_j$，最低层数为 $1$。

**情形二：$m\ge2$。** 在式 (17) 之后，再沿最后一个位置 $j_r$ 连续差分 $m-1$ 次。由式 (16)，对任意整数 $t\ge1$ 有

$$
\Delta_{j_r}^{\,t}x_{j_r}
=2^{t-1}\sigma_{j_r}.
$$

因此，

$$
\begin{aligned}
\Delta_{j_r}^{\,m-1}
\Delta_{j_{r-1}}\cdots\Delta_{j_1}f_{m,A}
&=\frac{2^{m-2}}{2^m}\prod_{j\in A}\sigma_j\\
&=\frac14\prod_{j\in A}\sigma_j.
\end{aligned}
\tag{19}
$$

总差分次数恰好是

$$
(r-1)+(m-1)=k-1.
$$

由于 $A\ne\varnothing$，翻转其中任何一个比特都会改变符号乘积。式 (19) 的相位因而在

$$
e^{2\pi i(1/4)}=i,
\qquad
e^{2\pi i(-1/4)}=-i
$$

之间改变。这两个相位不相等，乘上任何统一的全局相位也不能让它们相等。因此，结果不是模 $1$ 的常数，$U_{m,A}\notin\mathcal C_{k-1}$。

两个情形都展示了具体的相对相位，而不只是得到一个非零的常数相位。它们排除了相位抵消和全局相位带来的假障碍。证明只在支持内选择方向，所以加入不参与相位的比特也不会改变下界。

结合上界 (14)，最终得到

$$
\boxed{
\begin{gathered}
m\ge1,\qquad
\boldsymbol a\ne0,\qquad
r=\operatorname{wt}(\boldsymbol a),\\
U_{m,\boldsymbol a}\text{ 的最低 Clifford 层级为 }
\ k=m+r-1.
\end{gathered}
}
\tag{20}
$$

## 6. 用六种常见门校准公式

下表只列参与门作用的比特，未列出的比特均不参与相位。所有对角矩阵都按通常的二进制计算基顺序排列。

| 门 | 参与比特上的对角矩阵 | 相位函数 $f$ | $m$ | $r$ | 最低层数 |
|---|---|---|---:|---:|---:|
| $Z$ | $\operatorname{diag}(1,-1)$ | $x_1/2$ | 1 | 1 | 1 |
| $S$ | $\operatorname{diag}(1,i)$ | $x_1/4$ | 2 | 1 | 2 |
| $T$ | $\operatorname{diag}(1,e^{i\pi/4})$ | $x_1/8$ | 3 | 1 | 3 |
| $\mathrm{CZ}$ | $\operatorname{diag}(1,1,1,-1)$ | $x_1x_2/2$ | 1 | 2 | 2 |
| $\mathrm{CS}$ | $\operatorname{diag}(1,1,1,i)$ | $x_1x_2/4$ | 2 | 2 | 3 |
| $\mathrm{CCZ}$ | $\operatorname{diag}(1,1,1,1,1,1,1,-1)$ | $x_1x_2x_3/2$ | 1 | 3 | 3 |

例如，$S$ 与 $\mathrm{CZ}$ 虽然分别作用于一个、两个比特，却同在第二层；$T$、$\mathrm{CS}$、$\mathrm{CCZ}$ 则分别用分母与支持的不同组合得到第三层。

### $\mathrm{CS}$ 的共轭把两种下降机制同时展示出来

取 $f=x_1x_2/4$。沿第一个位置差分，式 (8) 给出

$$
\Delta_1 f
=\frac{x_1x_2}{2}-\frac{x_2}{4}.
$$

第一项是 $\mathrm{CZ}$ 的相位，第二项是第二个比特上 $S^\dagger$ 的相位，所以

$$
\mathrm{CS}\,X_1\,\mathrm{CS}^\dagger
=\mathrm{CZ}\,S_2^\dagger X_1.
\tag{21}
$$

这不是“共轭后只剩一个受控次数更少的门”：实际上出现了两个对角因子，一个减少相位分母，一个减少支持。第 4 节的有限和归纳保证它们合起来属于第二层；任意翻转方向也已由同一证明处理，所以 $\mathrm{CS}\in\mathcal C_3$。

再检查它为什么不能是 Clifford。沿第二个位置继续差分，

$$
\Delta_2\Delta_1f
=\frac{(2x_1-1)(2x_2-1)}4.
$$

当 $(x_1,x_2)=(0,0)$ 时相位是 $i$，当 $(x_1,x_2)=(0,1)$ 时相位是 $-i$。第二层对角门经过任意两次差分都应成为全局相位，而这里没有，因此 $\mathrm{CS}\notin\mathcal C_2$。这正是一般下界证明在 $m=2,r=2$ 时的实例。

同样，$m=1$ 时式 (8) 的整数项消失，直接得到

$$
\mathrm{CZ}\,X_1\,\mathrm{CZ}^\dagger
=Z_2X_1,
$$

$$
\mathrm{CCZ}\,X_1\,\mathrm{CCZ}^\dagger
=\mathrm{CZ}_{23}X_1.
\tag{22}
$$

这两式展示了分母已经是 $2$ 时，层级下降主要表现为支持减少。它们与 $T$ 的式 (9)、$\mathrm{CS}$ 的式 (21) 一起，对应了同一个差分公式，而不是四种互不相干的门技巧。

## 7. 公式说明了什么，又没有说明什么

对于这里系数为 $1$、分母为 $2^m$、支持非空的单项式，相位差分有两种计数下降方式：分母减少一个 $2$，或支持减少一个位置。上界证明说明所有 Pauli 都受这个计数约束；下界证明则说明，确实存在差分序列不能更早变成全局相位。这两个方向合起来，才把计数 $m+r-1$ 确定为最低层数。

对于多个相位项，第 4 节只给出按各项计数最大值计算的**上界**，没有证明最低层数总等于这个最大值。例如，两个 $T$ 相乘时，

$$
\frac{x}{8}+\frac{x}{8}=\frac{x}{4},
\qquad
T^2=S,
$$

最低层数从 $3$ 降为 $2$。系数合并、分母约化、整数相位和全局相位都可能影响最低层数，不能把单项式结论未经检查地推广到任意相位多项式。

同理，在固定 $m$ 的这个门族中，给乘积增加一个新的比特变量会使 $r$ 增加 $1$，从而使最低层数增加 $1$；这不等于已经证明“任意门每加一个控制都升一层”。$\mathrm{CZ}$ 与 $\mathrm{CS}$ 的对比也说明，仅知道相位是二次式，不足以判断它是不是 Clifford，必须同时保留相位系数与周期。稳定子态中允许的相位结构是另一个相关问题，见 [[逻辑基态的二次相位]]。

本文出现的 $UX_jU^\dagger X_j$ 也与 [[State injection]] 中的校正算子形式相连：若 $U\in\mathcal C_3$，递归定义和右乘 Pauli 的性质已经保证该算子是 Clifford。这里证明的是这个层级事实；资源态怎样通过测量和前馈实现门操作，则是门传态线路需要另行说明的问题。

[^S008]: Anqi Gong, Christopher A. Pattison, Patrick Rall, Adam Wills, *Magic State Distillation via Codes over Binary Extension Fields*, arXiv:2608.09727v1 (2026)，§2.1 式 (1) 及其后的门例子。译文见 [[Translations/S008.full.zh-CN#2.1 Clifford 层级中的对角门|S008 译文 §2.1]]。该处给出层级公式，本文的逐步证明不是该段译文的转述。https://arxiv.org/abs/2608.09727v1

[^CGK17]: Shawn X. Cui, Daniel Gottesman, Anirudh Krishna, *Diagonal gates in the Clifford hierarchy*, **Physical Review A 95**, 012329 (2017)，doi:10.1103/PhysRevA.95.012329。本文核对的原始版本为 arXiv:1608.06596v1：§II 给出全局相位约定与递归定义；§IV 的 Definitions 4–6 定义单项式门及其生成的分层对角群，Theorem 3 将其与对应层的对角子集等同，Lemmas 3–4 分别证明两向包含。其计数为 $(p-1)(m-1)+\sum_j a_j$；在 $p=2$ 时，$\sum_j a_j$ 就是汉明重量。本文独立展开比特单项式的上界和最低层数证明，不要求使用一般素维分类。https://arxiv.org/html/1608.06596v1
