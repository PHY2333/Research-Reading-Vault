# State injection

在未知数据态上执行一个门，与事先制备一个固定的辅助态，是两种不同的任务。门注入利用这种区别：先独立制备资源态，再让它与数据相互作用，通过测量和按记录执行的校正，消耗这个资源来实现目标门。

要理解这一过程，首先需要看清测量留下了什么，而不是先猜校正门。下面先研究只转移未知态的 one-bit teleportation，再直接构造 $T$ 注入。完成这个具体例子后，才讨论把 $T$ 换成一般酉门 $U$ 时，哪些操作需要改变。最后固定实际使用的 $T$ 线路，分析资源错误怎样进入数据，以及这些错误怎样接入蒸馏协议。

## 1. One-bit teleportation：先学会读出测量分支

### 1.1 按将被测量的标签重新组织求和

设数据量子比特为 $d$，辅助量子比特为 $a$。全文采用 $d\otimes a$ 的张量积顺序。**张量因子的排列顺序，与 CNOT 的控制方向是两项不同的约定。**

写未知输入为

$$
|\psi\rangle_d=\sum_{x=0}^1c_x|x\rangle_d,
\qquad
\sum_x|c_x|^2=1.
$$

先不执行额外的目标门，只要求把同一组未知振幅转移到辅助线上。

所有计算基指标都取值于 $\{0,1\}$。异或 $x\oplus y$ 是模 $2$ 加法，满足

$$
x\oplus x=0,
\qquad
x\oplus0=x,
\qquad
X^m|x\rangle=|x\oplus m\rangle.
$$

准备辅助态

$$
|+\rangle_a=\frac{|0\rangle_a+|1\rangle_a}{\sqrt2},
$$

并使用辅助线控制数据线的 CNOT：

$$
\operatorname{CNOT}_{a\to d}
|x\rangle_d|y\rangle_a
=
|x\oplus y\rangle_d|y\rangle_a.
$$

这里第二个张量因子是控制端；它的标签 $y$ 保持不变，第一个因子上的标签被翻转。由线性性，

$$
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a
=
\frac1{\sqrt2}
\sum_{x,y}c_x
|x\oplus y\rangle_d|y\rangle_a.
$$

接下来要在计算基测量数据线 $d$，所以需要按 $d$ 上的标签分组。令

$$
m=x\oplus y.
$$

对每个固定的 $x$，这个关系唯一反解为

$$
y=x\oplus m.
$$

因此，遍历 $(x,y)$ 与遍历 $(x,m)$ 一一对应；换元没有遗漏或重复任何项。代入得到

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

振幅仍然是原来的 $c_x$。改变的是求和标签，以及辅助线上对应的基矢；没有把输入振幅 $c_x$ 换成 $c_{x\oplus m}$。

记

$$
|\psi\rangle_a:=\sum_xc_x|x\rangle_a,
$$

也就是把同一组系数写在辅助空间的计算基上，便得到

$$
\boxed{
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a
=
\frac1{\sqrt2}
\sum_{m=0}^1
|m\rangle_dX_a^m|\psi\rangle_a
}.
$$

这里的跨线记号只是在对应两个空间的计算基，不表示另外执行了一道交换门。

### 1.2 从未归一化向量得到概率和校正

在测量发生之前，$m$ 只是联合态中的求和指标。测量 $d$ 并实际读到 $m$ 后，才得到一个经典记录，并留下辅助线上的未归一化向量

$$
\frac1{\sqrt2}X_a^m|\psi\rangle_a.
$$

其范数平方就是该记录的概率：

$$
p_m
=
\left\|
\frac1{\sqrt2}X_a^m|\psi\rangle_a
\right\|^2
=
\frac12.
$$

除以 $\sqrt{p_m}$ 后，归一化条件态为

$$
X_a^m|\psi\rangle_a.
$$

根据已读出的 $m$，再对辅助线执行 $X_a^m$。因为 $X^{2m}=I$，输出恢复为 $|\psi\rangle_a$。

这条线路的实际顺序是：准备 $|+\rangle_a$，执行 $\operatorname{CNOT}_{a\to d}$，在计算基测量数据线 $d$，按记录校正辅助线 $a$。输出位于辅助线；数据线已经被测量，并没有同时保留第二份未知输入。

这属于 **one-bit teleportation**。在 Zhou、Leung 和 Chuang 的命名中，它是式 (7) 的 X-teleportation：辅助线先制备成 $|+\rangle$，测量后使用 $X$ 校正。这个名称并不表示要在数据的 $X$ 基中测量。它与标准远程隐形传态也有不同的操作前提：标准协议使用预共享 Bell 对和两位经典测量结果，不再要求发送端与接收端执行联合量子门；这里则允许 $d$ 与 $a$ 直接进行 CNOT，只使用一个辅助量子比特和一位测量记录。[^S010]

到这里，转移未知态的问题已经解决，计算始终只用了计算基和 XOR。

## 2. 直接构造 $T$ 注入：让资源相位作用在数据上

### 2.1 为什么要改变 CNOT 方向和测量位置

现在提出一个新的目标：不只转移 $|\psi\rangle$，而是实现

$$
|\psi\rangle_d\longmapsto T|\psi\rangle_d,
$$

并把输出保留在原数据线。

固定约定

$$
T=\operatorname{diag}(1,\omega),
\qquad
\omega=e^{i\pi/4},
$$

所以

$$
T|x\rangle=\omega^x|x\rangle.
$$

事先准备资源态

$$
|T\rangle_a
=
T|+\rangle_a
=
\frac1{\sqrt2}\sum_y\omega^y|y\rangle_a.
$$

它与 $|+\rangle$ 的区别，是资源计算基分量上的相对相位。我们需要让这个相位变成依赖数据标签 $x$ 的相位，同时不能测掉要保留的数据线。

仅仅把上一节的测量位置改到辅助线，还不能达到这一目标。保留原来的 $\operatorname{CNOT}_{a\to d}$ 时，测得辅助线为 $m$，留下

$$
{}_a\langle m|
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|T\rangle_a
=
\frac{\omega^m}{\sqrt2}X_d^m|\psi\rangle_d.
$$

消掉 $X^m$ 后仍然只有 $|\psi\rangle$。资源相位变成了只依赖记录的整体相位 $\omega^m$，没有成为所需的 $\omega^x$。

因此改用数据线控制辅助线：

$$
\operatorname{CNOT}_{d\to a}
|x\rangle_d|y\rangle_a
=
|x\rangle_d|y\oplus x\rangle_a.
$$

这样，测量辅助线得到 $m$ 时，会选中 $y=x\oplus m$；资源原有的相位 $\omega^y$ 就变成与数据标签有关的 $\omega^{x\oplus m}$。

**这里确实更换了实际线路：CNOT 的计算基控制方向由 $a\to d$ 改为 $d\to a$，测量位置由数据线改为辅助线。它不是同一个 CNOT 的等价表示。**

### 2.2 用同一次 XOR 换元读出两个分支

对任意输入，

$$
\begin{aligned}
\operatorname{CNOT}_{d\to a}
|\psi\rangle_d|T\rangle_a
&=
\frac1{\sqrt2}
\sum_{x,y}c_x\omega^y
|x\rangle_d|y\oplus x\rangle_a\\
&=
\frac1{\sqrt2}
\sum_{m,x}c_x\omega^{x\oplus m}
|x\rangle_d|m\rangle_a.
\end{aligned}
$$

第二行仍然只是使用一一换元

$$
m=y\oplus x,
\qquad
y=x\oplus m.
$$

测得辅助线为 $m$ 后，数据线上的未归一化输出为

$$
\frac1{\sqrt2}
\sum_xc_x\omega^{x\oplus m}|x\rangle_d.
$$

把这个从输入数据到剩余数据的线性映射记为 $K_m$，称为该记录的**分支算符**：

$$
\boxed{
K_m
=
\frac1{\sqrt2}
\sum_x\omega^{x\oplus m}|x\rangle\langle x|
}.
$$

于是

$$
K_m|x\rangle
=
\frac{\omega^{x\oplus m}}{\sqrt2}|x\rangle.
$$

分支算符保存了尚未归一化的输出，因而也保存了概率。一般地，对归一化输入 $|\psi\rangle$，

$$
p_m=\|K_m|\psi\rangle\|^2
=\langle\psi|K_m^\dagger K_m|\psi\rangle.
$$

当 $p_m>0$ 时，归一化条件态才是

$$
\frac{K_m|\psi\rangle}{\sqrt{p_m}}.
$$

本例每个对角系数的模都是 $1/\sqrt2$，所以

$$
K_m^\dagger K_m=\frac12I,
\qquad
p_m=\frac12.
$$

这一步说明测量记录与未知输入的振幅无关；它不是在读取 $|\psi\rangle$ 的某个计算基值。

### 2.3 为什么校正是 $S^m$

先分别读出两个分支：

$$
K_0=\frac{T}{\sqrt2},
\qquad
K_1=\frac{\omega}{\sqrt2}T^\dagger.
$$

零记录已经给出目标门。记录为 $1$ 时，需要把 $T^\dagger$ 变为 $T$。定义

$$
S:=T^2=\operatorname{diag}(1,i),
$$

便有

$$
ST^\dagger=T.
$$

因此，测量后按记录执行 $S^m$ 即可。

为了同时核对两个分支及其相位，把校正直接作用到计算基上：

$$
S^mK_m|x\rangle
=
\frac{\omega^{2mx+(x\oplus m)}}{\sqrt2}|x\rangle.
$$

这里相位指数按整数计算。对比特 $x,m$，有整数恒等式

$$
x\oplus m=x+m-2xm,
$$

所以

$$
2mx+(x\oplus m)=x+m.
$$

于是

$$
\boxed{
S^mK_m=\frac{\omega^m}{\sqrt2}T
}.
$$

不能直接把 $\omega^{x\oplus m}$ 换成 $\omega^{x+m}$：当 $x=m=1$ 时，两者分别为 $1$ 和 $i$。正是 $S^m$ 提供的相位补偿，使上面的等式成立。

每个记录的概率都是 $1/2$。归一化并校正后，条件态为

$$
\omega^mT|\psi\rangle.
$$

此时 $m$ 已经是经典记录，$\omega^m$ 是该条件态的整体相位，不影响其物理状态。

因此，标准 $T$ 注入线路已经完整得到：**准备 $|T\rangle_a$，执行 $\operatorname{CNOT}_{d\to a}$，在计算基测量辅助线 $a$，对数据线执行 $S^m$。** 这就是 Jacinto 等人式 (2) 使用的线路。[^S001]

### 2.4 这条线路为什么有用

Clifford 门是通过酉共轭把 Pauli 算符仍映为 Pauli 算符的门。这里的 Pauli 算符由 $X$、$Z$ 及其乘积和相位组成，其中 $Y=iXZ$。

CNOT 是 Clifford 门；$S$ 也满足

$$
SXS^\dagger=Y,
\qquad
SZS^\dagger=Z.
$$

所以，当资源 $|T\rangle$ 已经备好后，剩余线路只使用 Clifford 门、计算基测量和经典前馈。这里的“前馈”就是根据已经读出的 $m$ 选择是否执行单比特门 $S$，不是在测量前额外执行一个相干的受控 $S$ 门。

$S$ 不是 Pauli。可以实际执行它，也可以在能够相应调整后续门和测量的 Clifford frame 中记录它；只记录待校正 Pauli 的 Pauli frame，不能直接代替这一 $S$ 校正。

这个具体构造已经不需要更多表示变换。接下来的问题不是补完 $T$ 注入，而是辨认它的哪些性质能推广到一般 $U$。

## 3. 一般 $U$：先把目标门接入辅助线输出的传态

### 3.1 资源中放入 $U$，为什么相互作用也要改变

现在令 $U$ 为任意单比特酉门，并准备

$$
|U\rangle:=U|+\rangle.
$$

$T$ 的计算只涉及计算基相位，而一般 $U$ 还可能混合计算基方向，不能直接照搬那段相位计算。最直接的起点，是第一节已经证明的传态恒等式：先允许输出位于辅助线，再问怎样使它成为 $U|\psi\rangle_a$。

如果在第一节的 CNOT 之后对辅助线施加 $U$，联合态会变为

$$
\frac1{\sqrt2}
\sum_m|m\rangle_dU_aX_a^m|\psi\rangle_a.
$$

但我们的目标是把 $U$ 放进事先制备的资源，而不是等未知数据传过来以后再直接执行 $U$。为此，需要找一个双比特算符 $W_U$，使

$$
W_U(I_d\otimes U_a)
=
(I_d\otimes U_a)\operatorname{CNOT}_{a\to d}.
$$

右乘 $I_d\otimes U_a^\dagger$，就确定了

$$
\boxed{
W_U
=
(I_d\otimes U_a)
\operatorname{CNOT}_{a\to d}
(I_d\otimes U_a^\dagger)
}.
$$

这不是假定 $U$ 可以穿过 CNOT，而是用共轭确定穿过去以后应当使用的新算符。由定义，

$$
\begin{aligned}
W_U|\psi\rangle_d|U\rangle_a
&=
(I_d\otimes U_a)
\operatorname{CNOT}_{a\to d}
|\psi\rangle_d|+\rangle_a\\
&=
\frac1{\sqrt2}
\sum_m|m\rangle_dU_aX_a^m|\psi\rangle_a.
\end{aligned}
$$

测量位置仍然是数据线 $d$，输出位置仍然是辅助线 $a$。测得 $m$ 后，未归一化输出为

$$
\frac1{\sqrt2}UX^m|\psi\rangle_a.
$$

如果显式区分输入空间与输出空间，可以写出计算基对应

$$
J_{a\leftarrow d}
=
\sum_x|x\rangle_a\,{}_d\langle x|,
$$

以及从数据空间到辅助空间的分支算符

$$
L_m(U)
=
\frac1{\sqrt2}U_aX_a^mJ_{a\leftarrow d}.
$$

$J_{a\leftarrow d}$ 只记录相同坐标怎样写到另一条线上，不是另外执行的 SWAP。因为

$$
J_{a\leftarrow d}^\dagger J_{a\leftarrow d}=I_d,
$$

所以

$$
L_m(U)^\dagger L_m(U)=\frac12I_d.
$$

两个记录仍各以概率 $1/2$ 出现，归一化条件态是 $UX^m|\psi\rangle_a$。按记录在辅助线上施加 $UX^mU^\dagger$，便有

$$
(UX^mU^\dagger)(UX^m|\psi\rangle)
=
U|\psi\rangle.
$$

至此，一般 $U$ 的辅助线输出恒等式已经证明，仍没有使用数据 $X$ 基。

### 3.2 现在为什么值得改写 CNOT

上面的证明回答了“线路怎样才会实现 $U$”，却没有回答“$W_U$ 是否容易实现”。若照定义直接在线执行 $U^\dagger$、CNOT 和 $U$，就未必减少了实现目标门的困难。

现在需要看清：**对辅助线做 $U$ 共轭，究竟把 CNOT 中的哪一部分变成了什么？** 为此，希望把数据端的算符保持固定，让辅助端只出现简单的 $I$ 和 $Z$。数据 $X$ 基的投影分解正好能做到这一点。

定义

$$
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2},
\qquad
P_+=|+\rangle\langle+|,
\qquad
P_-=|-\rangle\langle-|.
$$

因为 $|+\rangle$、$|-\rangle$ 是 $X$ 的正负本征态，

$$
I=P_++P_-,
\qquad
X=P_+-P_-.
$$

在固定的 $d\otimes a$ 顺序下，原来的 CNOT 是

$$
\operatorname{CNOT}_{a\to d}
=
I_d\otimes|0\rangle\langle0|_a
+
X_d\otimes|1\rangle\langle1|_a.
$$

将上述 $I$、$X$ 分解代入，再按 $P_+$、$P_-$ 合并：

$$
\begin{aligned}
\operatorname{CNOT}_{a\to d}
&=
(P_++P_-)_d\otimes|0\rangle\langle0|_a
+
(P_+-P_-)_d\otimes|1\rangle\langle1|_a\\
&=
P_{+,d}\otimes
\bigl(|0\rangle\langle0|+|1\rangle\langle1|\bigr)_a\\
&\quad+
P_{-,d}\otimes
\bigl(|0\rangle\langle0|-|1\rangle\langle1|\bigr)_a\\
&=
\boxed{P_{+,d}\otimes I_a+P_{-,d}\otimes Z_a}.
\end{aligned}
$$

这一步只改写了**同一个算符**，没有插入换基门，没有测量数据的 $X$，也没有把计算基 CNOT 换成 $\operatorname{CNOT}_{d\to a}$。

它也说明了这里的相位回踢：当数据处于 $|-\rangle_d$ 时，辅助端控制的数据 $X$ 作用贡献本征值 $-1$，表现为辅助态中 $|1\rangle_a$ 分量相对 $|0\rangle_a$ 分量多一个负号，即辅助端的 $Z$。

现在对辅助端做共轭，数据投影不动，立即得到

$$
\begin{aligned}
W_U
&=
(I\otimes U)
(P_+\otimes I+P_-\otimes Z)
(I\otimes U^\dagger)\\
&=
\boxed{
P_+\otimes I+P_-\otimes UZU^\dagger
}.
\end{aligned}
$$

改写的收益已经出现：一般 $U$ 把辅助端的 $Z$ 变成了 $UZU^\dagger$；不需要对整个双比特算符逐分量展开。

这里应分清两件事。把 CNOT 写成 $P_+\otimes I+P_-\otimes Z$，没有改变原来的门；用 $UZU^\dagger$ 替换其中的 $Z$，才得到一般不同于原 CNOT 的新门 $W_U$。

两个投影描述的是相干的量子控制，不是测量已经产生的两种经典结果。若数据处于两个 $X$ 基态的叠加，$W_U$ 必须对整个叠加保持线性作用。

### 3.3 恒等式成立，不等于只消耗资源就能低成本实现

若 $[U,Z]=0$，则 $UZU^\dagger=Z$，从而

$$
W_U=\operatorname{CNOT}_{a\to d}.
$$

这时相互作用确实简化。但对一般 $U$，仍须实现 $W_U$，并执行测量后的 $UX^mU^\dagger$ 校正。即使 $UZU^\dagger$ 本身是 Clifford，也不能据此认定它的相干受控版本 $W_U$ 是 Clifford。

因此，任意 $U$ 都满足上述线路恒等式，但不能由此断言任意 $U$ 都能只靠一个 $U|+\rangle$ 资源和 Clifford 操作实现。资源制备、相干相互作用和测后校正的代价，需要分别检查。

## 4. 一般 $U$ 的原位构造

现在重新要求输出位于数据线 $d$，构造另一条实际线路：测量辅助线，并保留数据线。

第二节已经给出一个成功的特例：资源为 $|T\rangle$ 时，使用 $\operatorname{CNOT}_{d\to a}$ 和辅助线测量即可。下面把资源换成 $|U\rangle$，先检查这条简单候选线路哪里正确、哪里不正确，再决定要补什么门。

### 4.1 先算候选线路在零测量记录下留下什么

先用计算基写出候选线路的输出。设数据态和辅助态分别为

$$
|\psi\rangle_d=\sum_xc_x|x\rangle_d,
\qquad
|\eta\rangle_a=\sum_y\eta_y|y\rangle_a,
$$

二者均已归一化。暂时保留任意辅助态 $|\eta\rangle$，这样得到的规则也能用于稍后经过补偿的资源。沿用第二节的 XOR 换元，测量前的联合态为

$$
\begin{aligned}
\operatorname{CNOT}_{d\to a}
|\psi\rangle_d|\eta\rangle_a
&=
\sum_{x,y}c_x\eta_y
|x\rangle_d|y\oplus x\rangle_a\\
&=
\sum_{m,x}c_x\eta_{x\oplus m}
|x\rangle_d|m\rangle_a.
\end{aligned}
$$

这里 $m=y\oplus x$，所以 $y=x\oplus m$。测得辅助线为 $m$ 后，数据线留下的未归一化向量为

$$
{}_a\langle m|
\operatorname{CNOT}_{d\to a}
|\psi\rangle_d|\eta\rangle_a
=
\boxed{
\sum_xc_x\eta_{x\oplus m}|x\rangle_d
}.
$$

先看 $m=0$。测量选中 $y=x$，输出变为

$$
\sum_xc_x\eta_x|x\rangle_d.
$$

数据的振幅 $c_x$ 逐项乘在辅助态的振幅 $\eta_x$ 上。若取 $c_0=c_1=1/\sqrt2$，即数据输入为 $|+\rangle$，两个辅助振幅就都只乘上同一个因子。因此

$$
{}_a\langle0|
\operatorname{CNOT}_{d\to a}
|+\rangle_d|\eta\rangle_a
=
\frac1{\sqrt2}\sum_x\eta_x|x\rangle_d
=
\frac1{\sqrt2}|\eta\rangle_d.
$$

其中 $|\eta\rangle_d$ 表示把辅助态的同一组系数写到数据空间。现在代入实际资源 $|\eta\rangle=|U\rangle=U|+\rangle$，就得到

$$
{}_a\langle0|
\operatorname{CNOT}_{d\to a}
|+\rangle_d|U\rangle_a
=
\frac1{\sqrt2}U|+\rangle_d.
$$

这说明候选线路在零测量分支下，已经把数据输入 $|+\rangle$ 变成了目标输出。接下来检查正交方向 $|-\rangle$：它与 $|+\rangle$ 构成一组基，能够用来判断线路是否对任意输入都正确。选择这两个 $X$ 基态，是因为前面的计算已经找到了其中一个正确的输入方向。

### 4.2 固定零测量记录后，只需补偿哪个输入方向

仍固定 $m=0$。数据输入换成 $|-\rangle$ 时，$c_x=(-1)^x/\sqrt2$；代入上一节的零分支公式，对任意辅助态都有

$$
{}_a\langle0|
\operatorname{CNOT}_{d\to a}
|-\rangle_d|\eta\rangle_a
=
\frac1{\sqrt2}\sum_x(-1)^x\eta_x|x\rangle_d
=
\frac1{\sqrt2}Z_d|\eta\rangle_d.
$$

取 $|\eta\rangle=|U\rangle=U|+\rangle$，暂时省略共同的因子 $1/\sqrt2$，就能比较候选线路与目标：

| 数据输入 | 候选线路的零分支输出 | 目标门的输出 |
|---|---|---|
| $\lvert+\rangle$ | $U\lvert+\rangle$ | $U\lvert+\rangle$ |
| $\lvert-\rangle$ | $ZU\lvert+\rangle$ | $U\lvert-\rangle=UZ\lvert+\rangle$ |

这是**同一个测量记录 $m=0$ 下，对两个不同基输入的比较**，不是在比较两个测量结果。

$|+\rangle$ 输入已经正确；$|-\rangle$ 输入却把所需的 $UZ$ 变成了 $ZU$。一般 $U$ 不与 $Z$ 对易，失配就在这里。

因此，只在数据的 $|-\rangle$ 分量上修改辅助资源：让它在进入 CNOT 前变为 $R|U\rangle$，而在 $|+\rangle$ 分量上仍保持 $|U\rangle$。根据上一节的测量规则，修改后的负输入在零记录下给出

$$
\frac1{\sqrt2}ZR|U\rangle.
$$

要得到 $U|-\rangle/\sqrt2$，需要且只需要

$$
\boxed{
R|U\rangle=ZU|-\rangle
}.
$$

共同的分支振幅 $1/\sqrt2$ 已经由正确的正输入确定；两个输入方向还必须保持正确的相对相位，不能分别只在“忽略各自相位”的意义下匹配。

所需操作是相干受控门

$$
\Lambda_X(R)
:=
P_{+,d}\otimes I_a
+
P_{-,d}\otimes R_a.
$$

它不改变数据的 $X$ 基标签，只按该标签决定是否修改资源。一般若无条件执行 $R$，会同时改变已经正确的正输入；若先测量数据的 $X$ 再按结果执行 $R$，则会丢失两个输入分量之间的相干，不能替代这个门。

如果 $[U,Z]=0$，表中两行原本就都正确，可以取 $R=I$。所以，$R$ 是针对这套候选线路的失配而引入的补偿，**不是“输出改回数据线”所必需支付的一项固定代价**。

一个直接满足约束的酉选择是

$$
\boxed{
R_U:=ZUZU^\dagger
}.
$$

各因子均为酉算符，而且

$$
R_U|U\rangle
=
ZUZU^\dagger U|+\rangle
=
ZU|-\rangle.
$$

于是，待核验的完整顺序为：先执行 $\Lambda_X(R_U)$，再执行 $\operatorname{CNOT}_{d\to a}$，随后测量辅助线，最后按记录校正数据线。

### 4.3 另一测量记录留下什么，以及怎样校正

零测量记录下，两个基输入已经按同一分支振幅得到目标输出。现在还需检查 $m=1$，并找出测量后的校正。为了统一处理两个输入方向，定义

$$
|s_X\rangle
:=
Z^s|+\rangle
=
\frac1{\sqrt2}
\sum_x(-1)^{sx}|x\rangle,
\qquad
s\in\{0,1\}.
$$

$s=0$ 表示 $|+\rangle$，$s=1$ 表示 $|-\rangle$，并且

$$
X|s_X\rangle=(-1)^s|s_X\rangle.
$$

这里 $s$ 标记输入的相干基分量，$m$ 仍表示辅助线的测量记录。将 $c_x=(-1)^{sx}/\sqrt2$ 代入 §4.1 已得到的一般测量分支，便有

$$
\begin{aligned}
{}_a\langle m|
\operatorname{CNOT}_{d\to a}
|s_X\rangle_d|\eta\rangle_a
&=
\frac1{\sqrt2}
\sum_x(-1)^{sx}\eta_{x\oplus m}|x\rangle_d\\
&=
\frac1{\sqrt2}Z_d^sX_d^m|\eta\rangle_d.
\end{aligned}
$$

$X^m$ 翻转辅助态的系数标签，$Z^s$ 补上输入基态带来的符号。下面把这条规则用于经过受控 $R_U$ 处理的资源。

令这条原位线路的分支算符为 $K_m$：

$$
K_m|\psi\rangle_d
:=
{}_a\langle m|
\operatorname{CNOT}_{d\to a}
\Lambda_X(R_U)
\bigl(|\psi\rangle_d|U\rangle_a\bigr).
$$

输入和输出现在都属于数据空间，不需要跨线映射 $J$。

先看受控门怎样作用在基输入上。$s=0$ 时辅助端执行 $I$，$s=1$ 时执行 $R_U$，所以

$$
\Lambda_X(R_U)
\bigl(|s_X\rangle_d|U\rangle_a\bigr)
=
|s_X\rangle_d\bigl(R_U^s|U\rangle_a\bigr).
$$

此时数据基态仍是 $|s_X\rangle$，进入 CNOT 的辅助态变为 $R_U^s|U\rangle$。对 $s=0$，这个辅助态是 $U|+\rangle$；对 $s=1$，上一节的资源约束给出 $R_U|U\rangle=ZU|-\rangle$。二者统一写成

$$
R_U^s|U\rangle=Z^sU|s_X\rangle.
$$

这里的指数只是在 $I$ 与 $R_U$ 之间选择，不要求 $R_U^2=I$。在前面的辅助线测量规则中，代入 $|\eta\rangle=R_U^s|U\rangle$，便得到第一步：

$$
\begin{aligned}
K_m|s_X\rangle
&=
\frac1{\sqrt2}Z^sX^m\bigl(R_U^s|U\rangle\bigr)\\
&=
\frac1{\sqrt2}Z^sX^mZ^sU|s_X\rangle.
\end{aligned}
$$

此处辅助态的系数已按测量规则写到数据空间，右边所有算符都作用于剩下的数据态。

接下来化简相邻的三个 Pauli 因子。由 $ZX=-XZ$，且 $s,m\in\{0,1\}$，

$$
Z^sX^m=(-1)^{sm}X^mZ^s.
$$

只有 $s=m=1$ 时需要交换一次 $Z$ 与 $X$，产生负号；其余情况至少有一个因子是 $I$。再在右侧乘上 $Z^s$，利用 $Z^{2s}=I$，得到

$$
\begin{aligned}
Z^sX^mZ^s
&=
(-1)^{sm}X^mZ^sZ^s\\
&=
(-1)^{sm}X^mZ^{2s}\\
&=
(-1)^{sm}X^m.
\end{aligned}
$$

因此

$$
K_m|s_X\rangle
=
\frac{(-1)^{sm}}{\sqrt2}X^mU|s_X\rangle.
$$

最后处理标量符号 $(-1)^{sm}$。由于 $|s_X\rangle$ 是 $X$ 的本征态，

$$
X|s_X\rangle=(-1)^s|s_X\rangle,
\qquad
X^m|s_X\rangle=(-1)^{sm}|s_X\rangle.
$$

利用 $X^mU$ 的线性性，可以先把标量乘到输入态上，再用这个本征态等式替换：

$$
\begin{aligned}
K_m|s_X\rangle
&=
\frac{(-1)^{sm}}{\sqrt2}X^mU|s_X\rangle\\
&=
\frac1{\sqrt2}X^mU\bigl((-1)^{sm}|s_X\rangle\bigr)\\
&=
\frac1{\sqrt2}X^mU\bigl(X^m|s_X\rangle\bigr)\\
&=
\frac1{\sqrt2}X^mUX^m|s_X\rangle.
\end{aligned}
$$

最右侧的 $X^m$ 来自它对输入基态的本征值作用；这一步只移动了标量符号，并未交换 $U$ 与 $X^m$。由于等式对 $|+\rangle$、$|-\rangle$ 这一组基都成立，由线性性得到

$$
\boxed{
K_m=\frac1{\sqrt2}X^mUX^m
}.
$$

因此，真正的两个测量分支是

$$
K_0=\frac{U}{\sqrt2},
\qquad
K_1=\frac{XUX}{\sqrt2}.
$$

零记录不需要再校正。对于记录 $1$，寻找 $C_U$ 使

$$
C_U(XUX)=U.
$$

右乘 $XUX$ 的逆，便得到

$$
\boxed{
C_U
=
U(XUX)^\dagger
=
UXU^\dagger X
}.
$$

于是

$$
\boxed{
C_U^mK_m=\frac{U}{\sqrt2}
}.
$$

同样，$C_U^m$ 只表示根据比特 $m$ 选择 $I$ 或 $C_U$，不意味着 $C_U$ 是二阶门。

最后核对概率：

$$
K_m^\dagger K_m
=
\frac12(X^mUX^m)^\dagger(X^mUX^m)
=
\frac12I.
$$

两个记录各以概率 $1/2$ 出现。归一化前的校正输出都是 $U|\psi\rangle/\sqrt2$，归一化后的输出都是 $U|\psi\rangle_d$。

这条一般原位线路因此被确定为

$$
\boxed{
\Lambda_X(R_U)
\;\longrightarrow\;
\operatorname{CNOT}_{d\to a}
\;\longrightarrow\;
\text{测量辅助线 }a
\;\longrightarrow\;
\text{在数据线执行 }C_U^m
}.
$$

其中第一项是测量前的量子控制，最后一项是测量后的经典前馈。它与第三节的辅助线输出构造，是测量位置和相互作用都不同的两条线路。

### 4.4 哪些条件使一般构造退化为简单的注入线路

现在才需要判断一般构造中的两个附加要求是否昂贵：相干受控门 $\Lambda_X(R_U)$，以及测后的 $C_U$。

如果 $U$ 在计算基中对角，即 $[U,Z]=0$，则

$$
R_U=ZUZU^\dagger=UZZU^\dagger=I.
$$

相干受控门完全消失，剩下第二节那种 CNOT、辅助线测量和数据线校正。

接下来判断测后校正是否为 Clifford。对角门可以用相位函数表示：

$$
U=D_f,
\qquad
D_f|x\rangle=e^{2\pi i f(x)}|x\rangle,
\qquad
f:\{0,1\}\to\mathbb R.
$$

沿用 [[对角相位门的Clifford层级#3. 共轭一个翻转，会出现相位差分|对角相位门的 Clifford 层级 §3]] 的约定，定义沿比特翻转的有限差分

$$
\Delta f(x)=f(x)-f(x\oplus1).
$$

该节式 (5) 已证明 $D_fXD_f^\dagger X=D_{\Delta f}$，恰好就是本线路需要的校正算符：

$$
\boxed{
C_U=UXU^\dagger X=D_{\Delta f}
}.
$$

因此，**对角门注入的测后校正，对应于原相位函数的一次有限差分。** 这里用这个结论识别校正门，其层级由该笔记中的差分判据判断。

记 Clifford 群为 $\mathcal C_2$；第三层 $\mathcal C_3$ 是将每个 Pauli 共轭为 Clifford 门的酉门集合。该笔记 §3 式 (7) 给出：对角门属于 $\mathcal C_3$，当且仅当所有翻转方向的差分门都属于 $\mathcal C_2$。对于当前的单比特，只有不翻转与翻转一次两种方向；前者的差分为零，对应恒等门，后者就是 $C_U$。所以

$$
\boxed{
U\in\mathcal C_3
\quad\Longleftrightarrow\quad
C_U\in\mathcal C_2
}
\qquad
\text{（单比特对角 }U\text{）}.
$$

在这套原位线路中，对角性使测量前的受控门消失，第三层条件则恰好保证测后的校正是 Clifford。因此，单比特对角 $U\in\mathcal C_3$ 的资源准备好后，剩余操作只需 Clifford 门、计算基测量和经典前馈。

以 $T=\operatorname{diag}(1,e^{i\pi/4})$ 和 $\sqrt T=\operatorname{diag}(1,e^{i\pi/8})$ 为例，直接对相位函数作差分：

| 目标门 | 相位函数 $f(x)$ | 差分 $\Delta f(x)$ | 校正门 $C_U=D_{\Delta f}$ |
|---|---|---|---|
| $T$ | $x/8$ | $x/4-1/8$ | $e^{-i\pi/4}S$ |
| $\sqrt T$ | $x/16$ | $x/8-1/16$ | $e^{-i\pi/8}T$ |

表中的 $x/4$、$x/8$ 分别给出 $S$、$T$，常数项则给出所写出的整体相位。校正是在测量后按经典记录执行的，这些整体相位不影响相应条件态。

按 [[对角相位门的Clifford层级#5. 下界：构造一串不会过早成为全局相位的差分|对角相位门的 Clifford 层级 §5]] 的最低层数结论，对 $f(x)=x/2^q$（$q\ge1$ 为整数），支持大小为 $1$，最低层数为 $q+1-1=q$。因此 $S$、$T$、$\sqrt T$ 的最低层数分别为 $2$、$3$、$4$。$T$ 的校正是 Clifford 门 $S$，与第二节一致；$\sqrt T$ 的校正仍含非 Clifford 门 $T$，所以这套线路消费 $\sqrt T$ 资源时仍需非 Clifford 前馈。

以上等价判据限定在单比特对角门。对于一般非对角 $U$，单独知道 $C_U$ 是 Clifford，不足以判定所有 Pauli 的共轭像；还须检查测量前的相干受控门。即使 $R_U$ 本身是 Clifford，也不能自动把 $\Lambda_X(R_U)$ 当作 Clifford。

### 4.5 为什么理想线路没有唯一确定受控门的全部作用

原位构造最初只要求

$$
R\,U|+\rangle=ZU|-\rangle.
$$

这是对一个向量的约束，不是对辅助空间全部向量的规定。

输入侧的 $U|+\rangle,U|-\rangle$ 是一组正交归一基，输出侧的 $ZU|-\rangle,ZU|+\rangle$ 也是。因此，对任意实数 $\theta$，规定

$$
R_\theta U|+\rangle=ZU|-\rangle,
\qquad
R_\theta U|-\rangle=e^{i\theta}ZU|+\rangle,
$$

都会得到满足同一资源态约束的酉门。$\theta=0$ 给出前面选择的 $R_U$。

对于理想资源 $U|+\rangle$，这些延拓在受控门中实际用到的作用相同，所以给出相同的 $K_m$。但资源一旦偏离这个理想向量，受控门就可能作用到其正交方向；不同延拓在这个方向上的相位不同，错误传播也可能不同。理想分支相同，不足以保证噪声行为相同。

这种延拓自由度，也不同于给整个 $R$ 随便乘一个相位。若替换为 $e^{i\chi}R$，受控门变为

$$
\Lambda_X(e^{i\chi}R)
=
P_+\otimes I
+
e^{i\chi}P_-\otimes R.
$$

相位只乘在数据的负输入分量上，是尚未测量的联合态中的相对相位，不能丢弃。第二节在测量后忽略 $\omega^m$，则是在每个已经确定的经典记录下忽略整个条件态的整体相位，两者不是同一个操作。

## 5. 回到标准 $T$ 线路：资源故障怎样进入数据

以下固定使用第二节的标准 $T$ 线路，即 $R_T=I$。资源故障发生在资源制备之后、CNOT 之前；CNOT、测量和实际采用的 $S^m$ 前馈均假定理想。$K_m$ 重新表示这条标准线路使用理想 $|T\rangle$ 时的分支。

这个固定十分重要：不能仅凭一般原位构造的理想输出相同，就把下面的错误传播公式移用于不同的受控门延拓或前馈规则。

### 5.1 先检查故障是否改变测量概率

第二节的等概率结论来自资源的具体振幅，不是所有辅助态的普遍性质。

若资源换成

$$
|\eta\rangle_a=\sum_y\eta_y|y\rangle_a,
$$

把第二节求和中的 $\omega^y/\sqrt2$ 换成 $\eta_y$，同一次 XOR 换元给出

$$
K_m[\eta]
=
\sum_x\eta_{x\oplus m}|x\rangle\langle x|.
$$

于是

$$
K_m[\eta]^\dagger K_m[\eta]
=
\sum_x|\eta_{x\oplus m}|^2|x\rangle\langle x|.
$$

它未必等于 $I/2$。例如资源为 $|0\rangle$ 时，

$$
K_m[0]=|m\rangle\langle m|,
$$

线路实际上在读取数据的计算基信息，而不是以两个等概率酉分支实现目标门。

下面分别讨论资源上的 Pauli $Z$ 和 $X$ 故障。将资源换成 $P|T\rangle$ 后的分支记为 $K_m^{(P)}$。

对于 $\operatorname{CNOT}_{d\to a}$，目标端的 Pauli 传播关系为

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

第一条也可从标签直接理解：输入资源的符号 $(-1)^y$，在输出标签为 $x$ 与 $x\oplus y$ 时写成

$$
(-1)^y=(-1)^x(-1)^{x\oplus y}.
$$

第二条则因为在目标标签上先翻转一次，或在 XOR 后再翻转一次，结果相同。

随后取辅助线测量分支，并使用

$$
\langle m|Z=(-1)^m\langle m|,
\qquad
\langle m|X=\langle m\oplus1|,
$$

得到

$$
\boxed{
K_m^{(Z)}=(-1)^mZK_m
},
\qquad
\boxed{
K_m^{(X)}=K_{m\oplus1}
}.
$$

由理想分支的 $K_m^\dagger K_m=I/2$ 可知，这两类故障下也分别有

$$
\bigl(K_m^{(P)}\bigr)^\dagger K_m^{(P)}=\frac12I,
\qquad P=X,Z.
$$

因此，理想资源、单独的资源 $Z$ 故障和单独的资源 $X$ 故障，都产生两个等概率记录。这是针对这些故障逐一得到的结论。

### 5.2 资源 $Z$ 故障直接成为输出 $Z$ 故障

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

归一化并忽略分支整体相位后，两个记录都给出

$$
ZT|\psi\rangle.
$$

资源上的 $Z$ 故障变成了目标门之后的数据 $Z$ 故障。原来的前馈只消除了理想线路的随机分支差别，并没有消除资源错误。

### 5.3 资源 $X$ 故障交换分支，但测量记录不报告这个故障

发生资源 $X$ 故障时，实验仍然只能按真实读到的 $m$ 执行 $S^m$。不能因为分析中知道有故障，就改用另一套前馈：

$$
S^mK_m^{(X)}=S^mK_{m\oplus1}.
$$

代入理想分支，

$$
S^0K_0^{(X)}
=
\frac{\omega}{\sqrt2}T^\dagger,
\qquad
S^1K_1^{(X)}
=
\frac1{\sqrt2}ST.
$$

令理想输出为

$$
|\phi\rangle:=T|\psi\rangle.
$$

利用 $T^\dagger=S^\dagger T$，归一化后的两个故障分支，忽略各自整体相位，为

$$
m=0:\quad S^\dagger|\phi\rangle,
\qquad
m=1:\quad S|\phi\rangle.
$$

因为 $S^\dagger=ZS$，这两个故障分支之间确实差一个 $Z$。但这个关系是在“资源已经发生 $X$ 故障”的条件下推导的。实际记录 $m$ 不会同时告诉我们故障是否发生：

$$
\Pr(m\mid\text{无资源故障})
=
\Pr(m\mid X\text{ 资源故障})
=
\frac12.
$$

所以，不能只凭 $m$，就把仅在故障情形中出现的 $Z^{1-m}$ 当成已知副产物更新 frame。若对所有 $m=0$ 的实验都额外补一个 $Z$，反而会把没有资源故障时本来正确的输出改错。

Jacinto 等人式 (3) 使用了表达式[^S001]

$$
S|\phi\rangle
=
\frac{\omega}{\sqrt2}(I-iZ)|\phi\rangle.
$$

在本文固定的记录标签和 $S^m$ 前馈下，它对应上述 $X$ 故障的 $m=1$ 条件态；$m=0$ 的条件态则是

$$
S^\dagger|\phi\rangle
=
\frac{\omega^{-1}}{\sqrt2}(I+iZ)|\phi\rangle.
$$

这两个表达式都只含 $I$ 与 $Z$，但仍是具有确定相对相位的相干组合。要把它们变成随机错误描述，还需要说明保留了哪些记录，或者实际执行了什么平均与测量。

## 6. 什么时候可以使用随机 $Z$ 错误模型

### 6.1 按记录前馈后，再忽略注入记录

先看固定记录下的状态。写成

$$
\frac{\omega}{\sqrt2}(I-iZ)|\phi\rangle
$$

不等于已经以一半概率选择 $|\phi\rangle$、一半概率选择 $Z|\phi\rangle$。两项之间有确定的相对相位，而且这两个向量未必正交。例如 $|\phi\rangle=|0\rangle$ 时，$Z|\phi\rangle=|\phi\rangle$，它们根本不是两个可区分状态。

为了讨论不保留记录的情况，用密度算符

$$
\sigma=|\phi\rangle\langle\phi|
$$

表示理想输出。若以概率 $r_j$ 产生状态 $\sigma_j$ 而不保留标签 $j$，状态就用加权平均 $\sum_jr_j\sigma_j$ 描述。

资源 $X$ 故障在完成实际 $S^m$ 前馈后，两个归一化条件态的密度算符为

$$
\sigma_0=S^\dagger\sigma S,
\qquad
\sigma_1=S\sigma S^\dagger.
$$

利用

$$
S
=
\frac{I+Z}{2}
+i\frac{I-Z}{2}
=
\frac{\omega}{\sqrt2}(I-iZ),
$$

以及其伴随，得到

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
\boxed{
\frac12\sigma+\frac12Z\sigma Z
}.
\end{aligned}
$$

两个条件态中的交叉项符号相反，平均后抵消。因此，**对这条线路中的资源 $X$ 故障，先按记录完成前馈，再忽略记录，就已经得到随机 $Z$ 的边缘输出，不需要先测量 syndrome。**

这里的 $1/2$ 是条件于该资源 $X$ 故障后的有效混合权重，不是在宣称实际资源总有一半概率出错。

保留 $m$ 时，状态仍分别是 $S^\dagger\sigma S$ 和 $S\sigma S^\dagger$。一般不能把整个带记录的过程替换成与 $m$ 无关的同一个随机 $Z$ 模型，尤其在后续还要利用 $m$ 时。

### 6.2 实际检查怎样把相干项分到不同 syndrome

另一种方式是实际测量一个能够区分 $|\phi\rangle$ 与 $Z|\phi\rangle$ 的检查。这里 $|\phi\rangle$ 可以表示包含其他量子比特在内的完整理想输出，$Z$ 则表示其中待检测的特定 Pauli 错误。

设检查 $G$ 是本征值为 $\pm1$ 的厄米 Pauli 算符，并满足

$$
G|\phi\rangle=|\phi\rangle,
\qquad
GZ=-ZG.
$$

这两个条件缺一不可：理想输出必须本来就有确定检查值，而错误必须翻转该值。于是

$$
GZ|\phi\rangle=-Z|\phi\rangle.
$$

两个向量属于不同本征空间，因而正交。检查的投影算符是

$$
\Pi_\pm=\frac{I\pm G}{2}.
$$

以 $S|\phi\rangle$ 为例，

$$
\Pi_+S|\phi\rangle
=
\frac{\omega}{\sqrt2}|\phi\rangle,
\qquad
\Pi_-S|\phi\rangle
=
-\frac{i\omega}{\sqrt2}Z|\phi\rangle.
$$

两个未归一化向量的范数平方各为 $1/2$。这次检查确实把相干组合分到不同的 syndrome，即不同检查结果中；忽略检查结果时，得到相应概率混合。对 $S^\dagger|\phi\rangle$，分量相位不同，但检查概率相同。

不能只因为某个检查“含有 $X$”就套用这个结论。若理想输出不是它的确定本征态，测量可能改变本来正确的状态；若它不与待检测错误反对易，也不能区分上述两项。

因此，在编码协议中不能在每次单独的 $T$ 注入之后随意测量原有 $X$ 检查。应在理想协议及必要校正保证检查值确定的位置测量，或者测量按协议正确传播后的检查。

### 6.3 在资源输入端先建立随机模型

还可以在注入前，直接整理已经制备好的资源噪声。定义

$$
A:=TXT^\dagger=\omega^{-1}SX.
$$

它是厄米 Clifford 酉算符，并满足

$$
A|T\rangle=|T\rangle,
\qquad
AZ=-ZA.
$$

因此，两个正交资源态 $|T\rangle$ 与 $Z|T\rangle$ 分别具有 $A$ 的本征值 $+1$ 和 $-1$。

对已制备的单资源状态 $\rho_R$，等概率施加 $I$ 或 $A$，并对随机选择取平均：

$$
\mathcal T_A(\rho_R)
=
\frac12(\rho_R+A\rho_RA).
$$

两个本征态之间的相干项在 $A$ 共轭下反号，对角权重则保持不变，所以平均后得到

$$
\mathcal T_A(\rho_R)
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

这就是这里需要的资源态 twirling。它保持对目标态的保真度，并没有提高单个资源的质量。它不是完整 Clifford 群的通道平均，也不是一次用于报告错误的 syndrome 检测；完整推导见 [[Clifford Twirling 与魔态错误模型]] §6。

将这个混合资源送入理想 $T$ 注入线路。理想资源与 $Z$ 故障资源对任意 $m$ 都有概率 $1/2$，所以条件于 $m$ 后，两个资源分量的相对权重仍为 $1-p$ 和 $p$。校正后的条件输出因此是

$$
\boxed{
\sigma_m=(1-p)\sigma+pZ\sigma Z
}.
$$

这里不必丢弃注入记录，随机 $Z$ 模型就在每个记录下成立；它来自输入端已经建立的概率混合。相比之下，上一节资源 $X$ 故障的随机模型来自对不同注入记录取平均，而 syndrome 投影又是一项实际检查操作。

若真正实施 twirling，随机 Clifford 门的误差也必须计入。若没有实施，而只在分析中用 twirled 模型替换真实资源，则需要说明这种替换为何适用于正在研究的量，不能将其视为每个带记录过程的自动物理等价。

## 7. 从注入错误到蒸馏检查：究竟由哪一层码检测

### 7.1 内码不能检测自己的逻辑 $Z$

前面的每条量子线都可以代表一个已经编码的逻辑量子比特。这时，线路中的 $X$、$Z$、CNOT、$S$ 和测量，都应理解为相应逻辑操作。

内码把一个线路量子比特编码在一块物理量子比特中，其稳定子检查用于控制物理噪声，帮助实现可靠的逻辑操作。分析资源错误时把 Clifford 部分近似为理想，是一种噪声模型，不表示编码后所有故障都严格消失。

尤其要区分物理 $Z$ 与内码逻辑 $\overline Z$。逻辑 $\overline Z$ 保持内码空间，并与该内码的全部稳定子对易，因此同一个内码的稳定子不能检测它自己的逻辑 $\overline Z$。

所以，若注入计算中的输出 $Z$ 已经代表内码逻辑错误，就不能直接调用该内码的稳定子，来充当上一节要求的反对易检查。

### 7.2 外层检查比较多个内码块

蒸馏协议在多个受保护的线路量子比特之上，再组织一层错误检测结构。每块内码提供一个逻辑量子比特，这些逻辑量子比特共同参与外层蒸馏协议。

例如，跨两块内码的外层检查可以是

$$
\overline X_1\overline X_2.
$$

它与第一块上的 $\overline Z_1$ 反对易。如果理想协议状态对这个检查有确定本征值，它就能检测该错误。这里检测的是跨块关系的变化，不是第一块内码自身的稳定子 syndrome。

Jacinto 等人 Sec. III 开头使用的正是这种分工：内码提供受保护的实现，资源注入提供带噪的非 Clifford 操作，外层蒸馏结构的检查与解码筛选相应错误。[^S001]

在 [[Distillation protocol]] §1–§3 的 CSS 码空间描述中，$G_0$ 的行指定外层 $X$ 型检查。协议先准备外层编码态，用多个资源实现规定的 $T/T^\dagger$ 层，并执行协议要求的已知 Clifford 校正；然后在理想检查值应当确定的位置测量这些检查，接受满足条件的记录，再解码得到输出资源。横向层的方向、校正及检查位置，都由具体协议决定。

因此，注入与蒸馏解决的是不同问题。注入把一个资源消耗为一次门操作，也把资源错误带入数据；蒸馏把多次有噪注入组织成带检查和后选择的过程，在相应输入误差范围与噪声假设下，提高被接受输出的质量。

### 7.3 单资源随机化不保证多个资源独立

即使每个资源都已经有随机 $Z$ 描述，不同资源之间仍可能相关。要进一步写成

$$
\rho_{\mathrm{in}}=\rho_T(p)^{\otimes n},
$$

必须额外假设各输入相互独立，并具有同一个错误率 $p$。

局域 twirling 可以消去不同联合错误模式之间的量子相干，却不会自动把联合概率分解为单体概率的乘积。例如，同一个制备故障可能同时在三个资源上产生 $Z$；这个三资源事件的概率由同一个故障决定，不一定是三个单资源错误率的乘积。相关条件和反例见 [[Clifford Twirling 与魔态错误模型]] §9.2。

因此，蒸馏中的高次错误率抑制不能仅由“每个资源都做过 twirling”推出。实际分析还可能需要加入内码逻辑故障、测量和前馈错误、泄漏以及跨资源关联；这些不在本文理想 Clifford 部分的单资源计算之内。

## 8. 向多比特门和编码资源延伸时保留哪些区别

### 8.1 $CCZ$：相位标签仍可用，错误却可能是相关字符串

前面的一般 $U$ 构造是单比特构造。对角门的相位标签方法可以用于多比特，但单比特中的“两种记录”或“两个错误分量各为 $1/2$”不能直接照搬。

例如，

$$
CCZ|x_1x_2x_3\rangle
=
(-1)^{x_1x_2x_3}|x_1x_2x_3\rangle,
$$

对应资源

$$
|CCZ\rangle=CCZ|+\rangle^{\otimes3}.
$$

让数据逐位控制资源的 CNOT，并在计算基测量三个资源量子比特。考虑测量记录全为零、不需额外零分支校正的情况：XOR 约束把各资源标签选为相应数据标签。

若资源第一位在 CNOT 前发生 $X$ 故障，它把资源相位中的 $x_1$ 换成 $x_1\oplus1$。相对于理想 $CCZ$，额外相位为

$$
\begin{aligned}
(-1)^{(x_1\oplus1)x_2x_3-x_1x_2x_3}
&=
(-1)^{(1-2x_1)x_2x_3}\\
&=
(-1)^{x_2x_3}.
\end{aligned}
$$

因此，该记录下的残余操作是作用于另外两位的

$$
CZ_{23}
=
\frac12\left(I+Z_2+Z_3-Z_2Z_3\right).
$$

其中已经出现相关的 $Z_2Z_3$ 字符串。这仍是相干的算符展开，不能只看系数就把它解释成几个互斥随机错误；具体记录、前馈和检查能否区分各项，都要另行计算。

更一般的资源消费、联合检查和测量分支构造见 [[MGT 的反向传播与稳定子码构造]]。上述例子只说明相位标签方法怎样继续使用，以及为何多比特错误不能压缩成单比特的等概率 $I/Z$ 选择。

### 8.2 门注入与物理资源的编码注入

本文讨论的 state injection 是门注入，也常称 gate teleportation：消耗资源态，通过测量及校正，在未知数据上实现目标门。对于一般 $U$，还必须检查与 $U$ 有关的相互作用和校正能否按所需代价实现。

文献中的“state injection”还可能指另一项任务：把物理层或低编码层的资源态转移到目标逻辑编码空间，例如

$$
\rho_{T,\mathrm{physical}}
\longrightarrow
\rho_{T,L},
$$

其中 $L$ 表示目标逻辑编码。

这种编码注入可以为本文的逻辑门注入提供资源，但它需要具体量子码、状态制备和测量方案，不能由两量子比特的门恒等式直接代替。

无论在哪一层实现，都应先固定实际线路，再读出测量分支。已知记录决定的校正、未知资源故障留下的错误、忽略记录得到的概率模型，以及实际检查所能区分的错误，是不同阶段的对象。把它们分别落实到所作用的量子线、算符和条件上，才能将单次注入可靠地接入更大的纠错与蒸馏协议。

[^S001]: H. Jacinto, X. Valcarce, V. Barizien, É. Gouzien, and N. Sangouard, [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>), arXiv:2606.07734v1 (2026)，Sec. II.B，PDF 第 3–4 页，式 (2)–(3)，以及 Sec. III 开头。本文按明确写出的 CNOT 方向、测量标签和前馈计算分支；式 (3) 与两个有记录故障分支的对应关系见 §5.3。

[^S010]: X. Zhou, D. W. Leung, and I. L. Chuang, [*Methodology for quantum logic gate construction*](<../../Papers/S010_2000_Zhou_one_bit_teleportation.pdf>), arXiv:quant-ph/0002039v2 (2000)，Sec. II，PDF 第 2–3 页，尤其式 (7) 的 X-teleportation。这里采用其 one-bit teleportation 的线路与术语定位，不把特定门的低成本构造无条件推广到任意酉门。
