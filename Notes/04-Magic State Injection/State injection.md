State injection 通过消耗资源态

$$
|U\rangle:=U|+\rangle
$$

在数据态上实现难以直接容错执行的门 $U$。其核心是 gate teleportation：量子码负责保护 Clifford 操作，非 Clifford 性则由离线制备的 magic state 提供。

本文主要采用 Jacinto 等人在 [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>) Sec. II.B 中的线路约定。

---
### 1. 从单比特 teleportation 开始

设数据 qubit 为 $d$，辅助 qubit 为 $a$，

$$
|\psi\rangle_d
=
\alpha|0\rangle+\beta|1\rangle,
\qquad
|+\rangle_a
=
\frac{|0\rangle+|1\rangle}{\sqrt2}.
$$

先执行以辅助 qubit 为控制、数据 qubit 为目标的

$$
\operatorname{CNOT}_{a\rightarrow d}.
$$

该门也可以写成“在数据 qubit 的 $X$ 基上控制辅助 qubit 的 $Z$”：

$$
\operatorname{CNOT}_{a\rightarrow d}
=
|+\rangle\langle+|_d\otimes I_a
+|-\rangle\langle-|_d\otimes Z_a.
$$

> [!note]- 同一 CNOT 的两种控制描述
> 这里采用 $d\otimes a$ 的张量积顺序；因子排在前面，并不表示它就是控制 qubit。在这个顺序下，“辅助 $a$ 控制、数据 $d$ 为目标”的标准定义是
>
> $$
> \operatorname{CNOT}_{a\rightarrow d}
> =I_d\otimes|0\rangle\langle0|_a
> +X_d\otimes|1\rangle\langle1|_a.
> $$
>
> 判断是否执行 $X_d$ 的仍然是 $a$ 在计算基中的取值。记 $P_{\pm,d}=|\pm\rangle\langle\pm|_d$，由 $I_d=P_{+,d}+P_{-,d}$ 和 $X_d=P_{+,d}-P_{-,d}$，按数据 qubit 的 $X$ 本征态重新合并各项，得到
>
> $$
> \begin{aligned}
> \operatorname{CNOT}_{a\rightarrow d}
> &=P_{+,d}\otimes\bigl(|0\rangle\langle0|+|1\rangle\langle1|\bigr)_a\\
> &\quad+P_{-,d}\otimes\bigl(|0\rangle\langle0|-|1\rangle\langle1|\bigr)_a\\
> &=P_{+,d}\otimes I_a+P_{-,d}\otimes Z_a.
> \end{aligned}
> $$
>
> 也可以直接看它对态的作用。取任意归一化辅助态 $c_0|0\rangle_a+c_1|1\rangle_a$。当数据处于 $|-\rangle_d$ 时，$X|-\rangle=-|-\rangle$，所以
>
> $$
> \begin{aligned}
> &\operatorname{CNOT}_{a\rightarrow d}
> \left[|-\rangle_d\otimes(c_0|0\rangle_a+c_1|1\rangle_a)\right]\\
> &\qquad=|-\rangle_d\otimes(c_0|0\rangle_a-c_1|1\rangle_a).
> \end{aligned}
> $$
>
> 因而，“$a=1$ 时对 $d$ 做 $X$”表现为辅助态的 $|1\rangle_a$ 分量获得负号，即对 $a$ 做 $Z$；这称为相位回踢（phase kickback）。当数据处于 $|+\rangle_d$ 时，由于 $X|+\rangle=|+\rangle$，辅助态保持不变。
>
> 因此，同一个门既能描述为“在 $a$ 的 $Z$ 基上控制 $d$ 的 $X$”，也能描述为“在 $d$ 的 $X$ 基上控制 $a$ 的 $Z$”。后一种描述同时改变了控制基和被控操作，并不意味着把门换成计算基中的 $\operatorname{CNOT}_{d\rightarrow a}$；这里只是重写算符，没有额外执行换基门。

作用后有

$$
\operatorname{CNOT}_{a\rightarrow d}
|\psi\rangle_d|+\rangle_a
=
\frac{
|0\rangle_d|\psi\rangle_a
+|1\rangle_dX|\psi\rangle_a
}{\sqrt2}.
$$

在 $Z$ 基测量数据 qubit，结果记为 $m\in\{0,1\}$，则辅助 qubit 上的未校正状态为

$$
X^m|\psi\rangle_a.
$$

条件施加 $X^m$ 后，输出恢复为 $|\psi\rangle$。这是一种只使用 CNOT、Pauli 测量和 Pauli correction 的单比特 teleportation。

---
### 2. 把门 $U$ 一起传送

若希望输出 $U|\psi\rangle$，把辅助态从 $|+\rangle$ 换成

$$
|U\rangle=U|+\rangle.
$$

同时将 teleportation 中作用在辅助 qubit 上的算符按 $U$ 共轭：

$$
Z\longmapsto UZU^\dagger,
\qquad
X\longmapsto UXU^\dagger.
$$

定义

$$
W_U
=
(I_d\otimes U_a)
\operatorname{CNOT}_{a\rightarrow d}
(I_d\otimes U_a^\dagger).
$$

它等价于在数据 qubit 的 $X$ 基上控制辅助 qubit 的 $UZU^\dagger$：

$$
W_U
=
|+\rangle\langle+|_d\otimes I_a
+|-\rangle\langle-|_d\otimes UZU^\dagger_a.
$$

由于输入辅助态已经是 $U|+\rangle$，

$$
\begin{aligned}
W_U|\psi\rangle_d|U\rangle_a
&=
(I\otimes U)
\operatorname{CNOT}_{a\rightarrow d}
|\psi\rangle_d|+\rangle_a\\
&=
\frac{
|0\rangle_dU|\psi\rangle_a
+|1\rangle_dUX|\psi\rangle_a
}{\sqrt2}.
\end{aligned}
$$

测量数据 qubit 后：

$$
m=0:\quad U|\psi\rangle,
$$

$$
m=1:\quad UX|\psi\rangle.
$$

在 $m=1$ 分支施加

$$
UXU^\dagger
$$

便有

$$
(UXU^\dagger)(UX|\psi\rangle)
=
U|\psi\rangle.
$$

因此 gate teleportation 用资源态 $|U\rangle$ 和条件校正 $UXU^\dagger$ 实现了 $U$。

---
### 3. 输出保留在原数据线上的 in-place gadget

上述线路把输出传送到辅助 qubit：

```text
data d:      |ψ⟩ ─────●_X──── M_Z
                       │        m
resource a:  |U⟩ ──[UZU†]────[UXU†]^m── U|ψ⟩
```

其中 $\bullet_X$ 表示在数据 qubit 的 $X$ 基上控制资源线上的门。输出位于第二条线。

论文通过加入 SWAP 并化简线路，把输出移回第一条线。化简后的线路形状为

```text
data d:      |ψ⟩ ─────●_X────●────[C_U]^m── U|ψ⟩
                       │      │
resource a:  |U⟩ ────[R_U]───⊕─── M_Z
                                      m
```

这里还不知道方框内应该放什么。可以不依赖图形化简，而是先把受控门记为未知的 $R$，从测量分支本身推出 $R$ 在资源态上的必要作用，再选择一个自然的酉延拓。

先令

$$
U=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad
|U\rangle
=
U|+\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
a+b\\
c+d
\end{pmatrix}.
$$

测量前的未知门以数据 qubit 的 $X$ 基为控制：

$$
\Lambda_X(R)
=
|+\rangle\langle+|_d\otimes I_a
+|-\rangle\langle-|_d\otimes R_a.
$$

执行 $\operatorname{CNOT}_{d\rightarrow a}$ 并在 $Z$ 基测量资源 qubit 后，作用在数据 qubit 上的分支算符为

$$
K_m(R)
=
{}_a\langle m|
\operatorname{CNOT}_{d\rightarrow a}
\Lambda_X(R)
|U\rangle_a.
$$

先只看 $m=0$ 分支。记

$$
|U\rangle
=
\begin{pmatrix}
u_0\\
u_1
\end{pmatrix},
\qquad
R|U\rangle
=
\begin{pmatrix}
v_0\\
v_1
\end{pmatrix}.
$$

把 $\Lambda_X(R)$ 先作用到辅助态上，得到一个“数据算符 $\otimes$ 辅助态”的和：

$$
\Lambda_X(R)|U\rangle_a
=
|+\rangle\langle+|_d\otimes |U\rangle_a
+
|-\rangle\langle-|_d\otimes R|U\rangle_a.
$$

再使用

$$
\operatorname{CNOT}_{d\rightarrow a}
=
|0\rangle\langle0|_d\otimes I_a
+
|1\rangle\langle1|_d\otimes X_a.
$$

对任意辅助态

$$
|\eta\rangle_a=\eta_0|0\rangle_a+\eta_1|1\rangle_a,
$$

有

$$
\begin{aligned}
{}_a\langle0|
\operatorname{CNOT}_{d\rightarrow a}
\left(B_d\otimes|\eta\rangle_a\right)
&=
{}_a\langle0|
\left[
|0\rangle\langle0|B_d\otimes|\eta\rangle_a
+
|1\rangle\langle1|B_d\otimes X|\eta\rangle_a
\right]\\
&=
\eta_0|0\rangle\langle0|B_d
+
\eta_1|1\rangle\langle1|B_d.
\end{aligned}
$$

这里 $B_d$ 是作用在数据线上的任意算符。第二项出现 $\eta_1$，是因为

$$
\langle0|X|\eta\rangle
=
\langle1|\eta\rangle
=
\eta_1.
$$

把这个规则分别用于

$$
B_d=|+\rangle\langle+|,
\quad
|\eta\rangle=|U\rangle,
$$

以及

$$
B_d=|-\rangle\langle-|,
\quad
|\eta\rangle=R|U\rangle,
$$

就得到

$$
\begin{aligned}
K_0(R)
&=
u_0|0\rangle\langle0|\,|+\rangle\langle+|
+v_0|0\rangle\langle0|\,|-\rangle\langle-|\\
&\quad
+u_1|1\rangle\langle1|\,|+\rangle\langle+|
+v_1|1\rangle\langle1|\,|-\rangle\langle-|\\
&=
\left(
u_0|0\rangle\langle0|
+
u_1|1\rangle\langle1|
\right)
|+\rangle\langle+|
+
\left(
v_0|0\rangle\langle0|
+
v_1|1\rangle\langle1|
\right)
|-\rangle\langle-|.
\end{aligned}
$$

最后代入

$$
|+\rangle\langle+|
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
|-\rangle\langle-|
=
\frac12
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

两项矩阵分别是

$$
\left(
u_0|0\rangle\langle0|
+
u_1|1\rangle\langle1|
\right)
|+\rangle\langle+|
=
\frac12
\begin{pmatrix}
u_0&u_0\\
u_1&u_1
\end{pmatrix},
$$

$$
\left(
v_0|0\rangle\langle0|
+
v_1|1\rangle\langle1|
\right)
|-\rangle\langle-|
=
\frac12
\begin{pmatrix}
v_0&-v_0\\
-v_1&v_1
\end{pmatrix}.
$$

相加后得到

$$
\boxed{
K_0(R)
=
\frac12
\begin{pmatrix}
u_0+v_0&u_0-v_0\\
u_1-v_1&u_1+v_1
\end{pmatrix}
}.
$$

因为

$$
u_0=\frac{a+b}{\sqrt2},
\qquad
u_1=\frac{c+d}{\sqrt2},
$$

线路中的条件校正写成 $[C_U]^m$，所以 $m=0$ 分支不再施加额外门；这一分支算符必须已经正比于目标门。按测量概率归一化，要求 $K_0(R)=U/\sqrt2$ 等价于

$$
\begin{aligned}
u_0+v_0&=\sqrt2 a,
&
u_0-v_0&=\sqrt2 b,\\
u_1-v_1&=\sqrt2 c,
&
u_1+v_1&=\sqrt2 d.
\end{aligned}
$$

于是 $m=0$ 分支给出的实际约束不是完整的算符等式，而是 $R$ 在当前资源态上的作用：

$$
R|U\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
a-b\\
d-c
\end{pmatrix}
=
ZU|-\rangle
=
ZUZ|+\rangle.
$$

由于 $|U\rangle=U|+\rangle$，一个规范选择是把这个态映射延拓为

$$
\boxed{
R=R_U:=ZUZU^\dagger
},
$$

因为

$$
R_U|U\rangle
=
ZUZU^\dagger U|+\rangle
=
ZU|-\rangle.
$$

这个选择的好处是它只由 $U$ 和 Pauli $Z$ 给出；当 $U$ 是 $Z$ 基对角门时，$R_U=I$，后面的受控 $R_U$ 会直接消失。

把 $R_U|U\rangle$ 代回分支算符。利用

$$
|+\rangle\langle+|
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\qquad
|-\rangle\langle-|
=
\frac12
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
$$

两个分支算符化为

$$
\begin{aligned}
K_0
&=
\frac1{\sqrt2}
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\frac{U}{\sqrt2},\\
K_1
&=
\frac1{\sqrt2}
\begin{pmatrix}
d&c\\
b&a
\end{pmatrix}
=
\frac{XUX}{\sqrt2}.
\end{aligned}
$$

所以 $m=0$ 分支已经是目标门，而 $m=1$ 分支为 $XUX$。为了把第二个分支也修正成 $U$，需要一个门 $C_U$ 满足

$$
C_U(XUX)=U.
$$

解得

$$
\boxed{
C_U:=UXU^\dagger X
},
$$

因为

$$
(UXU^\dagger X)(XUX)
=
UXU^\dagger UX
=
U.
$$

因此：

- $m=0$ 分支先固定 $R|U\rangle=ZUZ|+\rangle$，$R_U$ 是这个态映射的规范酉延拓；
- $C_U$ 是为了把另一个分支 $XUX$ 校正为同一个 $U$。

记 $K_m:=K_m(R_U)$。图中的 in-place gadget 满足

$$
C_U^mK_m
=
\frac{U}{\sqrt2},
\qquad
m\in\{0,1\}.
$$

两个测量结果的概率均为 $1/2$，归一化后的输出恒为

$$
U|\psi\rangle.
$$

#### 对角门的简化

若 $U$ 在 $Z$ 基中对角，则

$$
[U,Z]=0
$$

并且

$$
R_U
=
ZUZU^\dagger
=
ZZ
=
I.
$$

因此第一个受控门完全消失。线路只剩下

$$
\operatorname{CNOT}_{d\rightarrow a},
\qquad
M_{Z,a},
\qquad
C_U^m.
$$

若进一步有

$$
U\in\mathcal C_3,
$$

则

$$
UXU^\dagger\in\mathcal C_2,
$$

从而

$$
C_U=UXU^\dagger X\in\mathcal C_2.
$$

也就是说，对角的第三层 Clifford-hierarchy 门可以只用 Clifford 线路、测量、经典前馈和资源态 $|U\rangle$ 实现。

---
### 4. T-state injection

采用

$$
T=\operatorname{diag}(1,\omega),
\qquad
\omega=e^{i\pi/4},
$$

以及

$$
|T\rangle
=
T|+\rangle
=
\frac{|0\rangle+\omega|1\rangle}{\sqrt2}.
$$

$T$ 在 $Z$ 基中对角，因此 $R_T=I$。条件校正为

$$
\begin{aligned}
C_T
&=
TXT^\dagger X\\
&=
e^{-i\pi/4}S,
\end{aligned}
$$

其中

$$
S=\operatorname{diag}(1,i).
$$

整体相位 $e^{-i\pi/4}$ 不影响条件校正，所以实际只需在相应测量分支施加 $S$。

线路可写为

```text
data:    |ψ⟩ ───●──────── S^m ─── T|ψ⟩
                │
magic:   |T⟩ ───⊕─── M_Z
                       m
```

这里数据 qubit 是 CNOT 控制，magic-state qubit 是目标。

测量分支算符为

$$
K_m
=
{}_a\langle m|
\operatorname{CNOT}_{d\rightarrow a}
|T\rangle_a.
$$

两个分支分别为

$$
K_0
=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&0\\
0&\omega
\end{pmatrix}
=
\frac{T}{\sqrt2},
$$

$$
\begin{aligned}
K_1
&=
\frac{1}{\sqrt2}
\begin{pmatrix}
\omega&0\\
0&1
\end{pmatrix}\\
&=
\frac{\omega}{\sqrt2}T^\dagger.
\end{aligned}
$$

由于

$$
ST^\dagger=T,
$$

可得

$$
S^mK_m
=
\frac{\omega^m}{\sqrt2}T.
$$

因此

$$
\begin{array}{c|c|c}
m&\text{校正前}&\text{施加 }S^m\text{ 后}\\
\hline
0&T|\psi\rangle&T|\psi\rangle\\
1&T^\dagger|\psi\rangle&T|\psi\rangle
\end{array}
$$

表中忽略了归一化因子和整体相位。每个分支的概率均为

$$
P(m)
=
\langle\psi|K_m^\dagger K_m|\psi\rangle
=
\frac12.
$$

$S$ 是 Clifford 门，因此随机测量结果只产生 Clifford byproduct，不需要再次消耗 magic state。该 byproduct 可以物理执行，也可以在 Clifford frame 中跟踪。

---
### 5. Magic-state 错误如何传播

State injection 不会自动降低资源态的错误。论文特别讨论了 $|T\rangle$ 上的 $Z$ 型和 $X$ 型错误。

#### Z 型错误

把资源态换成

$$
Z|T\rangle.
$$

对应的分支算符满足

$$
K_0^{(Z)}
=
\frac{ZT}{\sqrt2},
$$

$$
SK_1^{(Z)}
=
-\frac{\omega ZT}{\sqrt2}.
$$

因此条件校正的输出均为

$$
ZT|\psi\rangle
$$

至多相差整体相位。因此资源态上的 $Z$ error 直接成为数据上的 $Z$ error。

#### X 型错误

把资源态换成

$$
X|T\rangle.
$$

此时

$$
K_0^{(X)}
=
\frac{\omega T^\dagger}{\sqrt2},
\qquad
SK_1^{(X)}
=
\frac{ST}{\sqrt2}.
$$

利用

$$
T^\dagger=ZST,
$$

两个分支在忽略整体相位后可写为

$$
m=0:\quad ZST|\psi\rangle,
$$

$$
m=1:\quad ST|\psi\rangle.
$$

其中测量结果已知，所以额外的 $Z$ byproduct 可以纳入 Pauli frame；有效错误可统一表示为

$$
ST|\psi\rangle.
$$

论文式 (3) 将它写成

$$
\boxed{
ST|\psi\rangle
=
\frac{e^{i\pi/4}}{\sqrt2}
(I-iZ)T|\psi\rangle
}.
$$

验证只需展开矩阵：

$$
\frac{e^{i\pi/4}}{\sqrt2}(I-iZ)
=
\operatorname{diag}(1,i)
=
S.
$$

这说明 $X$ 型资源错误在 syndrome measurement 之前不是一个随机 $Z$ error，而是

$$
T|\psi\rangle
\quad\text{与}\quad
ZT|\psi\rangle
$$

的相干叠加。

若数据由 QECC 编码，并测量一个能够检测该 $Z$ error 的 $X$ 型 stabilizer，则两个分量具有不同 syndrome。由于它们的振幅模长相同，测量后分别投影到

$$
T|\psi\rangle
$$

或

$$
ZT|\psi\rangle,
$$

概率各为 $1/2$。

因此，在以下假设下：

- Clifford 操作由 inner QECC 保护并视为理想；
- 相应 $X$ syndrome 被测量；
- 已知 Pauli/Clifford byproduct 已纳入 frame；

注入线路的有效输出错误可以只按 $Z$ 型错误处理。这一结论也适用于其它在 $Z$ 基中对角的资源门，例如 $CCZ$ 或 $\sqrt T$。

---
### 6. Inner code 与 distillation 的接口

论文假设 teleportation 线路中的

$$
|\psi\rangle,\qquad |+\rangle,\qquad |T\rangle
$$

都编码在 inner QECC 中。Inner code 的作用是保护：

- Clifford gates；
- Pauli 或 Clifford measurements；
- classical feedforward 与 frame update。

非 Clifford $T$ gate 则通过消耗编码的 $|T\rangle$ 实现。若 injected $T$ states 有噪声，而 Clifford 部分可视为理想，则每次注入只向数据引入有效 $Z$ error。

这正是 [[Distillation protocol]] 的输入模型：使用 $n$ 次 noisy $T$-state injection，实现一个受 $Z$ error 影响的非 Clifford 线路，再通过 $X$ 型检查筛选错误并保留 $k<n$ 个更干净的输出。

---
### 7. 术语边界

本文遵循所引论文的用法，将“state injection”理解为：

$$
\text{消耗 }|U\rangle
\quad\longrightarrow\quad
\text{在数据上实现 }U.
$$

这也常称为 gate injection 或 gate teleportation。

部分文献还用“state injection”表示把物理层或低编码层制备的 magic state 转移到目标逻辑编码空间：

$$
\rho_{T,\mathrm{physical}}
\longrightarrow
\rho_{T,L}.
$$

后一过程依赖具体量子码、code deformation、lattice surgery 和测量方案，不存在与编码无关的唯一线路。两种用法需要根据上下文区分。

---
### 8. 适用范围与易错点

- Canonical teleportation 使用 $\operatorname{CNOT}_{a\rightarrow d}$，而 in-place $T$ injection 使用 $\operatorname{CNOT}_{d\rightarrow a}$；两者方向不同。
- 对角性 $[U,Z]=0$ 用于消去 in-place gadget 中的受控 $R_U=ZUZU^\dagger$。对一般非对角 $U$ 不能直接删除该门。
- $U\in\mathcal C_3$ 保证条件校正 $C_U=UXU^\dagger X$ 是 Clifford；它不意味着 $U$ 本身是 Clifford。
- 对 $T$ injection，$m=1$ 分支需要 $S$ correction。$S$ 不是 Pauli，若不物理执行，必须使用 Clifford-frame tracking。
- $X$ 型 magic-state error 在 stabilizer measurement 前是相干错误；只有经过能区分 $T|\psi\rangle$ 与 $ZT|\psi\rangle$ 的 syndrome measurement 后，才可解释为随机 $Z$ error。
- 改变 CNOT 方向、测量基、measurement-bit 标号或采用 $|T^\dagger\rangle$，都会改变条件校正规则。
- 实际逻辑失败率还包括 inner-code logical fault、measurement error、decoder failure、leakage 和 correlated error。

---
### 与其它笔记的连接

- [[MGT 的反向传播与稳定子码构造]]：把本笔记的单量子比特 $T$ injection 放入 commuting-Pauli 资源态的 MGT 构造，并区分物理线路、反向传播测量，以及在相应对易条件下成立的测量分支码表示。
- [[Clifford Twirling 与魔态错误模型]]：说明何时可以进一步把 coherent error 化为 stochastic $Z$ error，以及独立输入模型需要哪些额外假设。
- [[Distillation protocol]]：从多次 noisy injection 得到 syndrome、输出错误与资源公式。
- [[Reed-Muller码]]：给出 15-to-1 distillation 所使用的具体码与错误阶数。
- [[三正交码与横向逻辑T门]]：说明 transversal $T$ 与 triorthogonality 的关系。

---
### 参考来源

- H. Jacinto, X. Valcarce, V. Barizien, É. Gouzien, and N. Sangouard, [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>), arXiv:2606.07734 (2026), Sec. II.B.
