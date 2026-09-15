# State injection

给定未知数据态 $|\psi\rangle$，我们希望在它上面执行一个单比特酉门 $U$。一种做法是直接对数据施加 $U$；另一种做法是事先独立准备资源态

$$
|U\rangle:=U|+\rangle,
\qquad
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
$$

再让数据与资源相互作用，通过测量和条件校正，把资源消耗为一次作用在数据上的门。这是本文讨论的 state injection，也称门注入或 gate teleportation。

这里要分别解决两个问题：**线路是否确实实现 $U$，以及实现这条线路还需要哪些门。** 对一般 $U$，资源态 $|U\rangle$ 并不自动把其余操作变成 Clifford 操作；对 $T$ 等满足额外条件的门，才会得到只需 Clifford 操作、测量和经典前馈的注入线路。

下面采用 Jacinto 等人 Sec. II.B 的线路约定，但不从图中猜测测量后的答案，而是持续使用同一套计算方法：先跟踪计算基标签，再按将被测量的标签重新组织求和，读出每个测量分支的线性算符，最后确定条件校正。[^S001]

## 1. 用异或把传态读成测量分支

### 1.1 CNOT 改变的是基标签

设数据量子比特为 $d$，辅助量子比特为 $a$。全文采用 $d\otimes a$ 的张量积顺序；**哪个因子排在前面，与哪个量子比特充当控制没有必然关系。**

写输入为

$$
|\psi\rangle_d=\sum_{x=0}^1 c_x|x\rangle_d,
\qquad
\sum_x|c_x|^2=1.
$$

所有计算基指标都是比特。异或 $x\oplus y$ 表示模 $2$ 加法：两位相同时为 $0$，不同时为 $1$。因此

$$
x\oplus x=0,
\qquad
x\oplus0=x,
\qquad
X^m|x\rangle=|x\oplus m\rangle.
$$

先使用以辅助线为控制、数据线为目标的门：

$$
\operatorname{CNOT}_{a\to d}
|x\rangle_d|y\rangle_a
=
|x\oplus y\rangle_d|y\rangle_a.
$$

控制位 $y$ 保持不变，目标位 $x$ 变为 $x\oplus y$。把辅助态准备成 $|+\rangle_a$，由线性性得到

$$
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a
=
\frac1{\sqrt2}
\sum_{x,y}c_x
|x\oplus y\rangle_d|y\rangle_a.
$$

接下来要在计算基测量 $d$，所以应该按 $d$ 上的标签来分组。令

$$
m=x\oplus y.
$$

对每个固定的 $x$，这个关系都能唯一反解为

$$
y=x\oplus m.
$$

于是，遍历 $(x,y)$ 与遍历 $(x,m)$ 完全等价：每一项仍恰好出现一次，只是换了求和标签。代入便得到

$$
\begin{aligned}
\frac1{\sqrt2}
\sum_{x,y}c_x
|x\oplus y\rangle_d|y\rangle_a
&=
\frac1{\sqrt2}
\sum_{m,x}c_x
|m\rangle_d|x\oplus m\rangle_a\\
&=
\frac1{\sqrt2}
\sum_m|m\rangle_d
X_a^m
\left(\sum_xc_x|x\rangle_a\right).
\end{aligned}
$$

这里振幅始终是 $c_x$，没有把它改成另一个输入振幅。改变的是基标签：辅助线上出现了 $|x\oplus m\rangle_a$，这恰好可以用 $X_a^m|x\rangle_a$ 表示。

因此

$$
\boxed{
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a
=
\frac1{\sqrt2}
\sum_{m=0}^1
|m\rangle_d X_a^m|\psi\rangle_a
}.
$$

**测量前，$m$ 只是求和指标；在 $d$ 上完成计算基测量后，实际读出的 $m$ 才成为经典记录。** 不能在测量前就把联合态当成其中某个分支。

### 1.2 跨线态标签与分支算符

上式中的

$$
|\psi\rangle_a=\sum_xc_x|x\rangle_a
$$

表示：把相同的一组系数 $c_x$ 放在辅助线的计算基上。它与 $|\psi\rangle_d$ 属于不同的单比特空间，并不是两个原本就在同一空间中的向量。

为了明确后面的映射方向，记

$$
J_{a\leftarrow d}
=
\sum_x|x\rangle_a\,{}_d\langle x|.
$$

它把数据空间的计算基对应到辅助空间的计算基，满足

$$
J_{a\leftarrow d}|\psi\rangle_d=|\psi\rangle_a,
\qquad
J_{a\leftarrow d}^{\dagger}J_{a\leftarrow d}=I_d.
$$

这个符号记录的是空间之间的基对应，不是在联合线路中额外执行的 SWAP 门。

测得 $d=m$ 时，对联合态取 ${}_d\langle m|$，留下辅助线上的未归一化向量

$$
L_m|\psi\rangle_d,
\qquad
L_m=\frac1{\sqrt2}X_a^mJ_{a\leftarrow d}.
$$

这样的 $L_m$ 称为分支算符：输入是测量前的数据态，输出是相应记录下尚未归一化的剩余态。它同时保存了条件态和发生概率的信息：

$$
p_m
=
\|L_m|\psi\rangle_d\|^2
=
{}_d\langle\psi|L_m^\dagger L_m|\psi\rangle_d.
$$

只有在 $p_m>0$ 时，归一化条件态才是

$$
\frac{L_m|\psi\rangle_d}{\sqrt{p_m}}.
$$

本例中

$$
L_m^\dagger L_m
=
\frac12J_{a\leftarrow d}^\dagger J_{a\leftarrow d}
=
\frac12I_d,
$$

所以两个记录的概率都是 $1/2$，归一化条件态为 $X_a^m|\psi\rangle_a$。再对辅助线施加 $X_a^m$，由 $X^{2m}=I$ 恢复 $|\psi\rangle_a$。

这条线路的输出位于辅助线：**先执行 $\operatorname{CNOT}_{a\to d}$，测量数据线 $d$，再按记录校正辅助线 $a$。** 数据线已经被测量，并没有同时保留下第二份未知输入态。

## 2. 同一 CNOT 的 $X$ 基描述与一般 $U$

### 2.1 改变控制描述，不等于反转 CNOT

后面要构造的门会在数据线的 $X$ 基上受到控制，因此先给这组基一个比特标签：

$$
|s_X\rangle
:=
Z^s|+\rangle
=
\frac{|0\rangle+(-1)^s|1\rangle}{\sqrt2},
\qquad
s\in\{0,1\}.
$$

其中 $|0_X\rangle=|+\rangle$、$|1_X\rangle=|-\rangle$，并且

$$
X|s_X\rangle=(-1)^s|s_X\rangle.
$$

现在让辅助线处于计算基态 $|y\rangle_a$。原来的 $\operatorname{CNOT}_{a\to d}$ 对数据施加 $X_d^y$，于是

$$
\begin{aligned}
\operatorname{CNOT}_{a\to d}
|s_X\rangle_d|y\rangle_a
&=
(-1)^{sy}|s_X\rangle_d|y\rangle_a\\
&=
|s_X\rangle_d Z_a^s|y\rangle_a.
\end{aligned}
$$

这在一组联合空间的基上确定了同一个算符：

$$
\boxed{
\operatorname{CNOT}_{a\to d}
=
|+\rangle\langle+|_d\otimes I_a
+
|-\rangle\langle-|_d\otimes Z_a
}.
$$

它既可以描述为“在 $a$ 的计算基上控制 $d$ 的 $X$”，也可以描述为“在 $d$ 的 $X$ 基上控制 $a$ 的 $Z$”。后一种描述同时改变了控制基和被控操作，**并没有把门换成 $\operatorname{CNOT}_{d\to a}$，也没有额外执行换基门。**

> [!note]+ 用投影算符代入并合并：两种控制描述如何相等
>
> 固定张量顺序为 $d\otimes a$。从“辅助线为 $0$ 时不操作，为 $1$ 时对数据线施加 $X$”的定义出发，
>
> $$
> \operatorname{CNOT}_{a\to d}
> =I_d\otimes|0\rangle\langle0|_a
> +X_d\otimes|1\rangle\langle1|_a.
> $$
>
> 定义数据线的 $X$ 本征空间投影算符
>
> $$
> P_{\pm,d}:=|\pm\rangle\langle\pm|_d
> =\frac{I_d\pm X_d}{2}.
> $$
>
> 于是 $I_d=P_{+,d}+P_{-,d}$，$X_d=P_{+,d}-P_{-,d}$。**代入并按 $P_{+,d}$、$P_{-,d}$ 合并**：
>
> $$
> \begin{aligned}
> \operatorname{CNOT}_{a\to d}
> &=(P_{+,d}+P_{-,d})\otimes|0\rangle\langle0|_a
> +(P_{+,d}-P_{-,d})\otimes|1\rangle\langle1|_a\\
> &=P_{+,d}\otimes\bigl(|0\rangle\langle0|_a+|1\rangle\langle1|_a\bigr)
> +P_{-,d}\otimes\bigl(|0\rangle\langle0|_a-|1\rangle\langle1|_a\bigr)\\
> &=P_{+,d}\otimes I_a+P_{-,d}\otimes Z_a.
> \end{aligned}
> $$
>
> 最后一步把辅助线上的两个括号分别识别为 $I_a$ 和 $Z_a$。因此，同一个门在数据线的 $+$ 本征空间中对辅助线施加 $I_a$，在 $-$ 本征空间中施加 $Z_a$。整个过程只是代入恒等式并合并算符项，张量顺序和门都没有改变。
>
> 当数据线固定为 $|-\rangle_d$ 时，目标上的 $X$ 本征值 $-1$ 就表现为控制端的 $Z_a$：辅助态中 $|1\rangle_a$ 分量相对 $|0\rangle_a$ 分量多一个负号。这就是这里的相位回踢，控制方向仍为 $a\to d$。

### 2.2 通过共轭把目标门接入传态

现在希望输出不只是 $|\psi\rangle$，而是 $U|\psi\rangle$。把辅助态准备成 $|U\rangle=U|+\rangle$，并定义

$$
W_U
=
(I_d\otimes U_a)
\operatorname{CNOT}_{a\to d}
(I_d\otimes U_a^\dagger).
$$

算符从右向左作用。最右侧的 $U_a^\dagger$ 与资源中的 $U_a$ 抵消，因此可以直接复用上一节的传态恒等式：

$$
\begin{aligned}
W_U|\psi\rangle_d|U\rangle_a
&=
(I_d\otimes U_a)
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a\\
&=
\frac1{\sqrt2}
\sum_m|m\rangle_d
U_aX_a^m|\psi\rangle_a.
\end{aligned}
$$

由 $X$ 基描述，同一个 $W_U$ 也可以写成

$$
W_U
=
\sum_{s=0}^1
|s_X\rangle\langle s_X|_d
\otimes U_aZ_a^sU_a^\dagger.
$$

也就是说，$d$ 处于 $|-\rangle$ 时，对辅助线执行 $UZU^\dagger$；处于 $|+\rangle$ 时不执行。

测量 $d$ 得到 $m$ 后，从数据空间到辅助空间的分支算符为

$$
L_m(U)
=
\frac1{\sqrt2}
U_aX_a^mJ_{a\leftarrow d}.
$$

由酉性，

$$
L_m(U)^\dagger L_m(U)=\frac12I_d.
$$

所以归一化条件态是 $UX^m|\psi\rangle_a$。它与目标 $U|\psi\rangle_a$ 的差别，可以由辅助线上的门 $UX^mU^\dagger$ 消除：

$$
(UX^mU^\dagger)(UX^m|\psi\rangle)
=
U|\psi\rangle.
$$

**这条一般 $U$ 线路的输出仍在辅助线。** 准备 $|\psi\rangle_d|U\rangle_a$，执行 $W_U$，在计算基测量 $d$，最后在 $a$ 上执行 $UX^mU^\dagger$。

这证明了一个传态恒等式，但尚未证明它是一种低成本实现。除了准备 $|U\rangle$，还必须实现 $W_U$ 及条件校正；这些操作本身都依赖于 $U$。不能仅凭这个恒等式就断言，任意单比特酉门都能由一个 $U|+\rangle$ 资源态加 Clifford 操作实现。

## 3. 从测量分支确定原位线路

如果希望输出保留在原数据线，就不能继续测量并丢弃这条线。下面改为测量辅助线，并从这个要求反推线路中的门。

考虑如下操作顺序：先以数据的 $X$ 基控制辅助门 $R$，再执行计算基中的 $\operatorname{CNOT}_{d\to a}$，然后在计算基测量辅助线 $a$，最后按记录 $m$ 校正数据线 $d$。两个输入仍是 $|\psi\rangle_d$ 和 $|U\rangle_a$。

这里的受控门记为

$$
\Lambda_X(R)
=
\sum_{s=0}^1
|s_X\rangle\langle s_X|_d\otimes R_a^s.
$$

指数 $s$ 只是在 $I$ 与 $R$ 之间选择，不要求 $R^2=I$。

我们先确定零测量分支对 $R$ 的要求，再选择一个酉门满足这个要求，最后检查另一个分支如何校正。这样不必预先猜出 $R$ 的完整矩阵。

### 3.1 一条可复用的辅助线测量规则

设辅助线上有任意态

$$
|\eta\rangle_a=\sum_y\eta_y|y\rangle_a.
$$

如果数据处于 $|s_X\rangle_d$，那么在执行 $\operatorname{CNOT}_{d\to a}$ 后，辅助线的计算基标签由 $y$ 变为 $y\oplus x$。测得辅助线为 $m$，就选中了

$$
y=x\oplus m.
$$

因此

$$
\begin{aligned}
{}_a\langle m|
\operatorname{CNOT}_{d\to a}
\bigl(|s_X\rangle_d|\eta\rangle_a\bigr)
&=
\frac1{\sqrt2}
\sum_x(-1)^{sx}\eta_{x\oplus m}|x\rangle_d\\
&=
\frac1{\sqrt2}
Z_d^sX_d^m|\eta\rangle_d.
\end{aligned}
$$

最后一行仍使用前面的跨线态标签约定：$|\eta\rangle_d$ 表示把系数 $\eta_y$ 放在数据空间的计算基上。这里没有额外的交换操作。

这条规则把两件事分开了：测量标签决定辅助振幅应取 $\eta_{x\oplus m}$，而数据的 $X$ 基标签贡献相位 $(-1)^{sx}$。

### 3.2 先让零分支实现目标门

定义原位线路的分支算符 $K_m(R)$：

$$
\begin{aligned}
K_m(R)|\psi\rangle_d
:={}_a\langle m|\,
\operatorname{CNOT}_{d\to a}
\Lambda_X(R)
\bigl(|\psi\rangle_d|U\rangle_a\bigr).
\end{aligned}
$$

这里输入和输出都属于数据空间，不再需要跨线映射 $J_{a\leftarrow d}$。

因为 $m=0$ 时不打算施加额外校正，先要求

$$
K_0(R)=\lambda U,
$$

其中 $\lambda$ 是与输入无关的分支振幅。我们不先假定它的大小，而是从线路本身确定它。

当输入为 $|+\rangle_d$ 时，受控门不执行 $R$。上一条测量规则给出

$$
K_0(R)|+\rangle
=
\frac1{\sqrt2}|U\rangle
=
\frac1{\sqrt2}U|+\rangle.
$$

由于 $U|+\rangle$ 非零，必须有

$$
\lambda=\frac1{\sqrt2}.
$$

再把输入取为 $|-\rangle_d$。这次辅助态先变为 $R|U\rangle$，零分支为

$$
K_0(R)|-\rangle
=
\frac1{\sqrt2}Z\bigl(R|U\rangle\bigr).
$$

要使它等于 $U|-\rangle/\sqrt2$，必须满足

$$
\boxed{
R|U\rangle=ZU|-\rangle
}.
$$

这里两端均可写在辅助空间中；前面的测量规则负责把相同的坐标送回数据空间。

由于 $|+\rangle$、$|-\rangle$ 构成一组基，这个条件连同已经自动满足的 $|+\rangle$ 分支，足以保证

$$
K_0(R)=\frac{U}{\sqrt2}.
$$

因此，零分支最初确定的只是 **$R$ 对资源态这个向量的作用**，而不是 $R$ 在整个辅助空间上的唯一形式。

### 3.3 选择一个酉延拓

一个直接可用的选择是

$$
\boxed{
R_U:=ZUZU^\dagger
}.
$$

它是酉算符，因为各因子都是酉算符，并且

$$
R_U|U\rangle
=
ZUZU^\dagger U|+\rangle
=
ZU|-\rangle.
$$

这就把所需的单个态映射延拓为了整个单比特空间上的酉门。

这个延拓并不唯一。输入侧的

$$
U|+\rangle,\qquad U|-\rangle
$$

是一组正交归一基，输出侧的

$$
ZU|-\rangle,\qquad ZU|+\rangle
$$

也是。对任意实数 $\theta$，规定

$$
R_\theta U|+\rangle=ZU|-\rangle,
\qquad
R_\theta U|-\rangle=e^{i\theta}ZU|+\rangle,
$$

都会定义一个满足同样资源态约束的酉门；$\theta=0$ 就给出 $R_U$。这些门在理想资源上的原位线路相同，但在资源偏离 $|U\rangle$ 时，可能对其正交方向产生不同作用，因而**不能自动沿用同一套错误传播结论**。

还要区分这种延拓自由度与“随便丢掉 $R$ 的整体相位”。若把整个 $R$ 替换成 $e^{i\theta}R$，则

$$
\Lambda_X(e^{i\theta}R)
=
|+\rangle\langle+|\otimes I
+
e^{i\theta}|-\rangle\langle-|\otimes R.
$$

相位只出现在一个控制分支中，已经是联合态的相对相位，不能当作整条线路的整体相位忽略。

### 3.4 两个分支与条件校正

以下固定使用 $R_U$，并记 $K_m:=K_m(R_U)$。

对 $s=0,1$，刚才的构造可以统一写成

$$
R_U^s|U\rangle=Z^sU|s_X\rangle.
$$

把它代入辅助线测量规则。右端按相同计算基坐标写在数据空间中，得到

$$
\begin{aligned}
K_m|s_X\rangle
&=
\frac1{\sqrt2}
Z^sX^mZ^sU|s_X\rangle\\
&=
\frac{(-1)^{sm}}{\sqrt2}
X^mU|s_X\rangle\\
&=
\frac1{\sqrt2}
X^mUX^m|s_X\rangle.
\end{aligned}
$$

第二步只用了

$$
Z^sX^mZ^s=(-1)^{sm}X^m,
$$

第三步只用了

$$
X^m|s_X\rangle=(-1)^{sm}|s_X\rangle.
$$

没有把 $X$ 或 $Z$ 无条件穿过一般的 $U$。由于等式对两个 $X$ 基矢都成立，由线性性得到

$$
\boxed{
K_m=\frac1{\sqrt2}X^mUX^m
}.
$$

也就是

$$
K_0=\frac{U}{\sqrt2},
\qquad
K_1=\frac{XUX}{\sqrt2}.
$$

现在零分支已经完成目标；另一个分支需要一个门 $C_U$ 满足

$$
C_U(XUX)=U.
$$

因为 $XUX$ 是酉门，直接右乘其逆得到

$$
\boxed{
C_U=U(XUX)^\dagger=UXU^\dagger X
}.
$$

于是

$$
C_U(XUX)=UXU^\dagger XXUX=U,
$$

并且两个分支可以统一写成

$$
\boxed{
C_U^mK_m=\frac{U}{\sqrt2}
}.
$$

这里 $C_U^m$ 仍只是按比特 $m$ 选择 $I$ 或 $C_U$，不意味着 $C_U$ 是二阶门。

最后再由分支算符计算概率：

$$
K_m^\dagger K_m
=
\frac12(X^mUX^m)^\dagger(X^mUX^m)
=
\frac12I.
$$

所以在理想资源和酉门假设下，每个记录的概率都是 $1/2$，归一化并校正后的输出恒为 $U|\psi\rangle_d$。

**原位线路因此被完整确定：** 在 $d$ 的 $X$ 基上控制 $a$ 的 $R_U$，执行 $\operatorname{CNOT}_{d\to a}$，测量辅助线 $a$，再在数据线 $d$ 上执行 $C_U^m$。它与前面的输出到辅助线的线路，不仅测量位置不同，所用计算基 CNOT 的方向也不同。

## 4. 对角门与 $T$ 注入

### 4.1 对角性消去受控门，第三层条件控制校正代价

一般原位线路仍有一个依赖 $U$ 的相干受控门。若 $U$ 在计算基中对角，则

$$
[U,Z]=0,
$$

因此所选延拓满足

$$
R_U=ZUZU^\dagger=UZZU^\dagger=I.
$$

这时整个 $\Lambda_X(R_U)$ 消失，线路只剩下 $\operatorname{CNOT}_{d\to a}$、辅助线的计算基测量，以及数据线上的条件校正 $C_U^m$。

接下来还要检查 $C_U$ 是否容易实现。这里需要 Clifford 层级的最短定义。Pauli 算符由 $X$、$Z$ 及其乘积和相位组成，其中 $Y=iXZ$。Clifford 门组成第二层 $\mathcal C_2$：它们通过共轭把 Pauli 算符仍映为 Pauli 算符。第三层 $\mathcal C_3$ 的酉门则通过共轭把每个 Pauli 算符映为 Clifford 门。

若进一步有 $U\in\mathcal C_3$，则

$$
UXU^\dagger\in\mathcal C_2.
$$

Clifford 门对乘法封闭，而 $X$ 本身是 Clifford，所以

$$
C_U=(UXU^\dagger)X\in\mathcal C_2.
$$

因此，对于这里的**单比特对角第三层门**，原位注入确实只需 Clifford 操作、测量、经典前馈和资源态 $|U\rangle$。

这两个条件承担不同作用：对角性消去相干受控门，第三层条件保证剩下的条件校正是 Clifford。对一般非对角 $U$，即使某个被控算符本身是 Clifford，也不能据此认定其相干受控版本是 Clifford；量子控制不能与测量后的经典条件选择混为一谈。

### 4.2 用相位标签计算 $T$ 的分支

固定

$$
T=\operatorname{diag}(1,\omega),
\qquad
\omega=e^{i\pi/4},
\qquad
S=\operatorname{diag}(1,i).
$$

它们对计算基的作用是

$$
T|x\rangle=\omega^x|x\rangle,
\qquad
S|x\rangle=i^x|x\rangle.
$$

资源态为

$$
|T\rangle
=
\frac1{\sqrt2}\sum_y\omega^y|y\rangle.
$$

由于 $T$ 对角，取 $R_T=I$。线路是：数据线控制资源线的 CNOT，随后测量资源线，最后校正数据线；这就是主来源式 (2) 的 $T$ 注入线路。[^S001]

先从一般公式求精确校正。对基矢 $|x\rangle$，$TXT^\dagger X$ 中的两个 $X$ 先后把标签翻转再翻回，所以

$$
\begin{aligned}
C_T|x\rangle
&=
TXT^\dagger X|x\rangle\\
&=
\omega^{x-(x\oplus1)}|x\rangle\\
&=
\omega^{2x-1}|x\rangle\\
&=
\omega^{-1}i^x|x\rangle.
\end{aligned}
$$

因此

$$
\boxed{
C_T=\omega^{-1}S
}.
$$

再用异或直接读出测量分支。对任意输入，

$$
\begin{aligned}
\operatorname{CNOT}_{d\to a}
|\psi\rangle_d|T\rangle_a
&=
\frac1{\sqrt2}
\sum_{x,y}c_x\omega^y
|x\rangle_d|x\oplus y\rangle_a\\
&=
\frac1{\sqrt2}
\sum_{m,x}c_x\omega^{x\oplus m}
|x\rangle_d|m\rangle_a.
\end{aligned}
$$

于是

$$
\boxed{
K_m|x\rangle
=
\frac{\omega^{x\oplus m}}{\sqrt2}|x\rangle
}.
$$

这里与第一节一样，先由测量标签固定 $y=x\oplus m$，再读取该项原有的振幅；不需要重新展开四个矩阵元素。

施加实际使用的校正 $S^m$ 后，

$$
S^mK_m|x\rangle
=
\frac{\omega^{2mx+x\oplus m}}{\sqrt2}|x\rangle.
$$

此处相位指数按整数计算。对比特 $x,m$，有整数恒等式

$$
x\oplus m=x+m-2xm,
$$

所以

$$
2mx+(x\oplus m)=x+m.
$$

由此得到

$$
\boxed{
S^mK_m=\frac{\omega^m}{\sqrt2}T
}.
$$

不能无条件把 $\omega^{x\oplus m}$ 改成 $\omega^{x+m}$；例如 $x=m=1$ 时，两者分别是 $1$ 和 $i$。在上面的正确计算中，正是校正 $S^m$ 提供的 $\omega^{2mx}$ 补偿了差别。

两个未校正分支也可以读成

$$
K_0=\frac{T}{\sqrt2},
\qquad
K_1=\frac{\omega}{\sqrt2}T^\dagger.
$$

因此，$m=0$ 时已经实现 $T$；$m=1$ 时先得到与 $T^\dagger$ 相差整体相位的条件态，再用 $ST^\dagger=T$ 校正。

由 $SXS^\dagger=Y$、$SZS^\dagger=Z$ 可知 $S$ 是 Clifford。又因为

$$
TXT^\dagger=C_TX=\omega^{-1}SX,
\qquad
TZT^\dagger=Z,
$$

$T$ 的 Pauli 共轭像属于 Clifford，符合第三层条件。

在测量已完成、$m$ 已成为经典记录后，$\omega^m$ 是各自条件态的整体相位，可以忽略。这与在相干受控门内部丢弃一个控制分支的相位不同。

$S$ 不是 Pauli。可以实际执行它，也可以在支持相应后续门和测量适配的 Clifford frame 中跟踪；只记录 Pauli frame，不能直接视为已经处理了 $S$ 校正。

对角性本身仍不保证校正是 Clifford。例如采用

$$
\sqrt T=\operatorname{diag}(1,e^{i\pi/8})
$$

时，同样的相位标签计算给出

$$
C_{\sqrt T}=e^{-i\pi/8}T.
$$

受控 $R_{\sqrt T}$ 虽然消失，条件校正却仍含非 Clifford 门 $T$。

## 5. 从资源故障读出输出算符

下面固定讨论上一节的标准 $T$ 线路，即 $R_T=I$，并假定 CNOT、测量和 $S^m$ 前馈本身理想。资源错误发生在资源制备之后、进入 CNOT 之前。改变线路、资源约定或前馈规则后，需要重新计算分支。

先注意：理想资源下的等概率结果不是任意资源的普遍性质。若资源换成

$$
|\eta\rangle_a=\sum_y\eta_y|y\rangle_a,
$$

同一次异或换元直接给出

$$
K_m[\eta]
=
\sum_x\eta_{x\oplus m}|x\rangle\langle x|.
$$

因此

$$
K_m[\eta]^\dagger K_m[\eta]
=
\sum_x|\eta_{x\oplus m}|^2|x\rangle\langle x|,
$$

它未必等于 $I/2$。例如资源为 $|0\rangle$ 时，$K_m[0]=|m\rangle\langle m|$，线路在读取输入的计算基信息，而不是以两个等概率酉分支实现 $T$。

### 5.1 先传播 Pauli，再读取测量记录

仍用 $K_m$ 表示理想 $|T\rangle$ 的分支。将资源换成 $P|T\rangle$ 后，相应分支记为 $K_m^{(P)}$。

对以数据为控制、辅助为目标的 CNOT，计算基标签规则给出两条传播关系：

$$
\operatorname{CNOT}_{d\to a}(I_d\otimes Z_a)
=
(Z_d\otimes Z_a)\operatorname{CNOT}_{d\to a},
$$

$$
\operatorname{CNOT}_{d\to a}(I_d\otimes X_a)
=
(I_d\otimes X_a)\operatorname{CNOT}_{d\to a}.
$$

第一条表示目标端的 $Z$ 相位传播到控制和目标两端；第二条表示目标端的 $X$ 可以直接穿过 CNOT。

随后对辅助线取 $\langle m|$。利用

$$
\langle m|Z=(-1)^m\langle m|,
\qquad
\langle m|X=\langle m\oplus1|,
$$

立即得到

$$
\boxed{
K_m^{(Z)}=(-1)^mZK_m
},
\qquad
\boxed{
K_m^{(X)}=K_{m\oplus1}
}.
$$

这两条关系已经包含了所需错误传播信息，无需为每个错误重新计算一个 $2\times2$ 矩阵。

它们也给出

$$
\bigl(K_m^{(Z)}\bigr)^\dagger K_m^{(Z)}
=
\bigl(K_m^{(X)}\bigr)^\dagger K_m^{(X)}
=
\frac12I.
$$

因此，理想资源、单独的资源 $Z$ 故障和单独的资源 $X$ 故障，在这条线路中都产生两个等概率记录。这个结论来自各自的分支算符，而不是对一般噪声的预设。

### 5.2 资源 $Z$ 故障成为数据 $Z$ 故障

因为 $S$ 与 $Z$ 对易，

$$
\begin{aligned}
S^mK_m^{(Z)}
&=
(-1)^mZS^mK_m\\
&=
\frac{(-1)^m\omega^m}{\sqrt2}ZT.
\end{aligned}
$$

所以归一化并忽略分支整体相位后，两个记录都给出

$$
ZT|\psi\rangle.
$$

资源上的 $Z$ 故障直接变为目标门之后的数据 $Z$ 故障。测量前馈消除了理想线路的随机分支差别，却没有消除这次资源错误。

### 5.3 资源 $X$ 故障交换分支，但不会报告故障标签

对资源 $X$ 故障，实际前馈仍按真实读到的 $m$ 执行 $S^m$，不能按未知的故障情况另选规则。因此

$$
S^mK_m^{(X)}
=
S^mK_{m\oplus1}.
$$

代入已经求出的理想分支，

$$
S^0K_0^{(X)}
=
\frac{\omega}{\sqrt2}T^\dagger,
\qquad
S^1K_1^{(X)}
=
\frac1{\sqrt2}ST.
$$

利用

$$
T^\dagger=S^\dagger T=ZST,
$$

令理想输出为 $|\phi\rangle:=T|\psi\rangle$，则归一化后的两个故障分支，至多相差整体相位，为

$$
m=0:\quad S^\dagger|\phi\rangle=ZS|\phi\rangle,
$$

$$
m=1:\quad S|\phi\rangle.
$$

两个分支之间确实差一个 $Z$，但这个结论是在分析“资源已发生 $X$ 故障”这一情形时得到的。实验中的记录 $m$ 并不同时告诉我们该故障是否发生，因为

$$
\Pr(m\mid\text{无资源故障})
=
\Pr(m\mid X\text{ 资源故障})
=
\frac12.
$$

因此，不能仅凭已知 $m$ 就把上述只在故障情形中出现的 $Z^{1-m}$ 当成已知 byproduct 更新 frame。若无条件执行这个额外更新，则在没有资源故障的 $m=0$ 分支中，反而会把正确的 $|\phi\rangle$ 改成 $Z|\phi\rangle$。

主来源式 (3) 写出[^S001]

$$
S|\phi\rangle
=
\frac{\omega}{\sqrt2}(I-iZ)|\phi\rangle.
$$

这条算符等式可由 $Z$ 的两个本征投影直接读出：

$$
S
=
\frac{I+Z}{2}
+i\frac{I-Z}{2}
=
\frac{\omega}{\sqrt2}(I-iZ).
$$

在本文固定的 CNOT 方向、记录标签和 $S^m$ 前馈约定下，式 (3) 直接对应 $X$ 故障的 $m=1$ 分支；$m=0$ 分支则是

$$
S^\dagger|\phi\rangle
=
\frac{\omega^{-1}}{\sqrt2}(I+iZ)|\phi\rangle.
$$

若要把两个有记录分支都写成 $S|\phi\rangle$，还需说明如何处理二者之间的 $Z$ 差别，例如另有信息确认故障事件并作相应修正。仅知道注入测量位，不提供这种信息。另一方面，在对记录取平均或执行合适检查后，两种相干组合又可能产生相同的随机错误描述；这是下一节要区分的对象。

## 6. 相干分支、丢弃记录与 syndrome 投影

### 6.1 固定记录下的相干组合，不等于两个随机选项

对固定的 $X$ 故障分支，输出一般包含

$$
|\phi\rangle
\quad\text{与}\quad
Z|\phi\rangle
$$

之间确定的相对相位。写成 $(I-iZ)|\phi\rangle/\sqrt2$，并不意味着线路已经以一半概率选择 $I$、一半概率选择 $Z$。

这两个向量甚至未必正交。例如 $|\phi\rangle=|0\rangle$ 时，$Z|\phi\rangle=|\phi\rangle$，根本不是两个可区分的错误状态。若要把相干项变成概率，必须说明发生了哪一种平均或哪一次能够区分它们的测量。

先看不再保留注入记录的情形。用密度算符

$$
\sigma=|\phi\rangle\langle\phi|
$$

表示理想输出；如果以概率 $r_j$ 产生状态 $\sigma_j$ 而不保留标签 $j$，相应状态就是加权平均 $\sum_jr_j\sigma_j$。

对资源 $X$ 故障，在执行 $S^m$ 前馈以后，两个归一化条件态的密度算符是

$$
\sigma_0=S^\dagger\sigma S,
\qquad
\sigma_1=S\sigma S^\dagger.
$$

它们的概率已经由分支算符证明为 $1/2$。因此，不再利用 $m$ 的边缘输出为

$$
\begin{aligned}
\overline{\sigma}_X
&=
\frac12S^\dagger\sigma S
+
\frac12S\sigma S^\dagger\\
&=
\frac14(I+iZ)\sigma(I-iZ)
+
\frac14(I-iZ)\sigma(I+iZ)\\
&=
\boxed{\frac12\sigma+\frac12Z\sigma Z}.
\end{aligned}
$$

第二行中的交叉项符号相反，平均后恰好抵消。于是，**对这条具体线路中的资源 $X$ 故障，先按记录完成前馈、再忽略记录，就已经得到一个随机 $Z$ 的边缘通道，并不需要先测量 syndrome。**

但它只是忽略 $m$ 后的描述。保留 $m$ 时，条件态仍分别是 $S^\dagger\sigma S$ 和 $S\sigma S^\dagger$，一般不能把整个带记录过程替换成与 $m$ 无关的随机 $Z$ 模型。若后续还要按 $m$ 采取其他操作，必须保留这一区别。

### 6.2 真正的 syndrome 投影需要什么条件

另一种消除相干项的方式，是测量一个能区分 $|\phi\rangle$ 与 $Z|\phi\rangle$ 的检查。

这里 $|\phi\rangle$ 可以表示包含其他量子比特在内的完整理想输出，$Z$ 表示其中待检测的特定 Pauli 错误。设待测的厄米 Pauli 检查为 $G$，必须同时满足

$$
G|\phi\rangle=|\phi\rangle,
\qquad
GZ=-ZG.
$$

第一个条件保证理想输出本来就有确定的检查值；第二个条件保证该错误翻转检查值。于是

$$
GZ|\phi\rangle=-Z|\phi\rangle.
$$

两个向量属于不同本征空间，所以正交。相应投影为

$$
\Pi_\pm=\frac{I\pm G}{2}.
$$

以 $S|\phi\rangle$ 分支为例，

$$
\Pi_+S|\phi\rangle
=
\frac{\omega}{\sqrt2}|\phi\rangle,
\qquad
\Pi_-S|\phi\rangle
=
-\frac{i\omega}{\sqrt2}Z|\phi\rangle.
$$

两个未归一化向量的范数平方各为 $1/2$，所以检查确实以一半概率得到理想态，一半概率得到 $Z$ 错误态。$S^\dagger|\phi\rangle$ 分支只改变这些分量的相位，检查概率相同。

这才是具有错误区分作用的 syndrome 投影。不能只因为某个检查“含有 $X$”就套用结论：若理想 $|\phi\rangle$ 对它没有确定本征值，测量本身就可能改变本来正确的输出。

在编码协议中，也不能在每次单独的 $T$ 注入后随意测量原有 $X$ 检查。应在理想协议及必要校正保证检查值已确定的位置测量，或者使用相应传播后的检查。

### 6.3 随机 $Z$ 模型也可以在资源输入端建立

还可以在注入以前，对资源态进行保持目标 $|T\rangle$ 的随机化。令

$$
A=TXT^\dagger=\omega^{-1}SX.
$$

它是厄米 Clifford 酉算符，并满足

$$
A|T\rangle=|T\rangle,
\qquad
AZ=-ZA.
$$

对已经制备好的单比特资源态 $\rho_R$，等概率施加 $I$ 或 $A$ 并对随机选择取平均，得到

$$
\mathcal T_A(\rho_R)
=
\frac12(\rho_R+A\rho_RA)
=
\rho_T(p),
$$

其中

$$
\rho_T(p)
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z,
$$

$$
p=1-\langle T|\rho_R|T\rangle.
$$

这一单资源 twirling 的推导和适用条件见 [[Clifford Twirling 与魔态错误模型]] §6。它保持对目标态的保真度，只消除 $|T\rangle$ 与 $Z|T\rangle$ 之间的相干；它不是完整 Clifford 群的通道平均，也不是一次 syndrome 检测。

将这个资源混合送入本文的理想注入线路。理想资源与 $Z$ 故障资源对每个 $m$ 都给出概率 $1/2$，因此条件于任意注入记录，二者的相对权重仍分别为 $1-p$ 与 $p$。校正后的输出为

$$
\sigma_m=(1-p)\sigma+pZ\sigma Z.
$$

这里甚至不必丢弃 $m$，随机 $Z$ 的条件输出模型就已经成立；它来自资源端已建立的混合模型。

若实际实施 twirling，随机 Clifford 操作的误差也应计入噪声。若没有实施，只在分析中用 twirled 模型替换真实资源态，则须说明为何这种替换适合当前所研究的量，而不能把它当成每个有记录分支的自动物理等价。

## 7. Inner code、outer checks 与蒸馏接口

### 7.1 先明确线路中的 $X$、$Z$ 属于哪一层

前面的每条量子线都可以代表一个已经编码的逻辑量子比特。在这种实现中，$X$、$Z$、CNOT 和 $S$ 都按内码的逻辑操作理解。

内码把一条线路量子比特编码在一块物理量子比特中。定义内码空间的稳定子检查用于发现物理噪声，使逻辑 Clifford 操作、逻辑测量和相关控制流程足够可靠。把这部分近似为理想，是分析资源噪声时采用的模型，而不是说编码后所有错误都严格消失。

尤其要区别物理错误与逻辑错误。一个已经成为内码逻辑 $\overline Z$ 的错误保持该内码空间，并与所有内码稳定子对易。因此，**同一个内码的稳定子不能检测它自己的逻辑 $\overline Z$**。

这意味着，若注入线路中传播到数据上的 $Z$ 指的是内码逻辑 $Z$，就不能直接调用内码稳定子来完成上一节要求的反对易检查。

### 7.2 外层检查检测内码逻辑量子比特之间的错误

蒸馏协议在多个内码逻辑量子比特之上再组织一层错误检测结构：每块内码提供一个受保护的线路量子比特，而这些线路量子比特共同承担外层蒸馏码。

例如，外层检查可以包含两块内码的逻辑算符乘积

$$
\overline X_1\overline X_2.
$$

它与第一块上的 $\overline Z_1$ 反对易，因此能够在理想状态具有确定检查值时检测这个错误。这并不违背内码稳定子检测不到 $\overline Z_1$：前者是跨内码块的外层检查，后者是单个内码内部的检查。

主来源 §III 开头正是以这种分工组织协议：内码提供受保护的 Clifford 操作，资源注入提供带噪非 Clifford 操作，外层蒸馏码的检查与解码负责筛选相应错误。[^S001]

在 [[Distillation protocol]] 的 CSS 码空间描述中，$G_0$ 的行指定外层 $X$ 型检查。协议先准备外层编码态，通过多次资源注入实现所需相位层，并施加规定的 Clifford 校正；随后在理想检查值应当确定的位置测量这些检查，只接受满足条件的结果，再解码得到输出资源。

因此，注入与蒸馏不是同一个动作。注入把一个资源转换为一次门操作，资源错误会随之进入数据；蒸馏则把多次有噪注入组织成带检查和后选择的过程，在相应噪声假设下提高被接受输出的质量。

### 7.3 随机化不自动给出独立输入

即使每个资源都已被整理为随机 $Z$ 模型，不同资源之间仍可能有经典关联。要把 $n$ 个输入写成

$$
\rho_{\mathrm{in}}=\rho_T(p)^{\otimes n},
$$

还需要额外假设它们独立且具有相同错误率。

局域 twirling 可以消去不同资源错误模式之间的量子相干，却不会自动把联合概率分解为单体概率的乘积。这个区别见 [[Clifford Twirling 与魔态错误模型]] §9.2。蒸馏分析中的高次错误率抑制，需要根据实际输入模型判断，不能仅由“每个输入都做了 twirling”推出。

实际注入与蒸馏还可能包含内码逻辑故障、测量错误、前馈错误、泄漏及跨资源关联；这些都不由本文假定理想 Clifford 部分的单资源计算覆盖。

## 8. 泛化与术语边界

本文的一般 $U$ 构造是单比特构造。对角门的相位标签方法可以用于多比特，但不能直接搬用单比特的“两种结果或错误各为 $1/2$”结论。

例如，三比特门

$$
CCZ|x_1x_2x_3\rangle
=
(-1)^{x_1x_2x_3}|x_1x_2x_3\rangle
$$

对应资源 $CCZ|+\rangle^{\otimes3}$。在数据逐位控制资源的 CNOT 注入中，考虑辅助测量全为零的分支：资源第一位上的 $X$ 把资源相位中的 $x_1$ 换成 $x_1\oplus1$，相对于理想门额外产生

$$
(-1)^{(x_1\oplus1)x_2x_3-x_1x_2x_3}
=
(-1)^{x_2x_3}.
$$

因此残余操作可以是

$$
CZ_{23}
=
\frac12\left(I+Z_2+Z_3-Z_2Z_3\right),
$$

其中已经包含相关的 $Z_2Z_3$ 字符串。具体记录、校正和检查如何作用，仍须逐一计算；不能把这个多比特相干组合直接解释成单比特的等概率 $I/Z$ 选择。更一般的资源消费与测量分支结构见 [[MGT 的反向传播与稳定子码构造]]。

最后，“state injection”在文献中有两种需要区分的用法。本文讨论的是

$$
\text{消耗资源态 }|U\rangle
\quad\longrightarrow\quad
\text{在数据上实现门 }U.
$$

另一种用法是把物理层或低编码层的资源态转移到目标逻辑编码空间：

$$
\rho_{T,\mathrm{physical}}
\quad\longrightarrow\quad
\rho_{T,L}.
$$

后一种是物理态的编码注入，需要根据具体量子码和测量方案设计。它可以为本文的门注入提供逻辑资源，但不能由这里的两量子比特门恒等式直接代替。

在这些不同语境中，可复用的计算顺序保持一致：先固定基标签和实际线路，用可逆的求和换元选出测量分支，由分支算符计算概率，再判断哪些条件校正可实现、哪些剩余算符是真实错误。错误是否已知、是否已被平均成随机模型，以及是否受到某一层检查的检测，都需要在相应步骤分别说明。

[^S001]: H. Jacinto, X. Valcarce, V. Barizien, É. Gouzien, and N. Sangouard, [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>), arXiv:2606.07734v1 (2026)，Sec. II.B，PDF 第 3–4 页，式 (2)–(3)，以及 Sec. III 开头。本文的测量分支均按所写出的控制方向、资源态和前馈约定计算；式 (3) 与两个有记录分支的对应关系见 §5.3。
