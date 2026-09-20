BINDING_OK
task_id: 20260920-binary-field-introduction
request_id: R01
binding_id: 88b1136de6724a67926c5ccbd1bfc2ed
based_on_repository: PHY2333/Research-Reading-Vault
based_on_branch: codex/20260920-binary-field-introduction
based_on_commit: a71da739c7833a414130e48d3d2f3ab712427d49
END_BINDING

PRO_STATUS: COMPLETE

BEGIN_FILE::88b1136de6724a67926c5ccbd1bfc2ed
path: Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md
mode: replace

```markdown
# 二元扩域

构造一个扩域，可以从添入一个方程的解开始：保留原来域中的元素和加乘法，再加入一个原来没有的新元素。新元素满足的方程会规定它的高次幂怎样化简，从而让扩大后的算术仍然可以计算。

先在有理数中做一次这样的扩张，再把同样的思路用于 $\mathbb F_2$。由此得到的二元扩域既有域的加乘除法，又能在选定基后写成比特坐标。S008 正是利用这两种描述之间的联系，把一组量子比特上的操作组织成扩域算术。理解这条联系，需要先把域本身构造出来。

## 1. 从添入 $\sqrt2$ 看扩域扩充了什么

方程

$$
t^2=2
$$

在有理数域 $\mathbb Q$ 中没有解。若 $\sqrt2=m/n$ 是最简分数，则 $m^2=2n^2$ 会先迫使 $m$ 为偶数，再迫使 $n$ 为偶数，与最简性矛盾。

现在在实数中考虑集合

$$
E=\{a+b\sqrt2:a,b\in\mathbb Q\}.
$$

其中包含全部有理数：取 $b=0$ 即可。两个这样的数相加，仍然具有同样的形式：

$$
(a+b\sqrt2)+(c+d\sqrt2)
=(a+c)+(b+d)\sqrt2.
$$

相乘时，先按分配律展开，再使用 $(\sqrt2)^2=2$：

$$
\begin{aligned}
(a+b\sqrt2)(c+d\sqrt2)
&=ac+(ad+bc)\sqrt2+bd(\sqrt2)^2\\
&=(ac+2bd)+(ad+bc)\sqrt2.
\end{aligned}
$$

所以，乘法虽然会产生平方项，方程 $(\sqrt2)^2=2$ 会把它重新写回 $1,\sqrt2$ 这两个方向。

非零元素的逆元也留在这个集合中。因为

$$
(a+b\sqrt2)(a-b\sqrt2)=a^2-2b^2,
$$

所以

$$
(a+b\sqrt2)^{-1}
=\frac{a-b\sqrt2}{a^2-2b^2}.
$$

这里分母不会为零：若 $b\ne0$，分母为零就意味着有理数 $a/b$ 的平方等于 $2$；若 $b=0$，非零输入要求 $a\ne0$。因此，逆元的两个系数仍是有理数。例如，

$$
(1+\sqrt2)^{-1}=\sqrt2-1.
$$

结合律、交换律与分配律沿用实数中的运算律，以上计算又验证了加法、乘法和非零求逆的封闭性。因此 $E$ 是一个域，通常记为

$$
\mathbb Q(\sqrt2).
$$

我们称它是 $\mathbb Q$ 的**扩域**，称 $\mathbb Q$ 是它的**子域**。扩张保留了原来的有理数算术，同时加入了 $\sqrt2$ 以及与它一起计算所需的元素。

每个元素的表达式 $a+b\sqrt2$ 还是唯一的。若

$$
a+b\sqrt2=c+d\sqrt2,
$$

且 $b\ne d$，便能把 $\sqrt2$ 写成有理数；所以必有 $b=d$，继而 $a=c$。这说明 $(1,\sqrt2)$ 是 $\mathbb Q(\sqrt2)$ 在 $\mathbb Q$ 上的一组基，其向量空间维数为 $2$。这个维数称为**扩张次数**，记为

$$
[\mathbb Q(\sqrt2):\mathbb Q]=2.
$$

这里的 $2$ 描述两个独立的有理数坐标；由于每个坐标可以取任意有理数，所得域仍有无限多个元素。

这个例子的构造方法已经很具体：添入一个满足方程的新元素，用方程约化它的高次幂，再检查由此得到的算术。下面把坐标系数改为 $\mathbb F_2$ 中的 $0,1$。

## 2. 在 $\mathbb F_2$ 中添入一个新根

在 $\mathbb F_2$ 中，加法满足 $1+1=0$。考虑方程

$$
t^2+t+1=0.
$$

代入 $t=0$ 或 $t=1$，左边都等于 $1$，所以它在 $\mathbb F_2$ 中没有根。我们希望添入一个新元素 $\alpha$，满足

$$
\alpha^2+\alpha+1=0.
$$

在特征 $2$ 中，加法与减法相同，因此这条关系可以写成

$$
\boxed{\alpha^2=\alpha+1}.
$$

这就是新乘法所需的约化规则。凡是出现 $\alpha^2$ 的地方，都可以替换成 $\alpha+1$；更高次幂也可以反复这样处理。因此，我们考虑四种形式

$$
a_0+a_1\alpha,
\qquad a_0,a_1\in\mathbb F_2,
$$

即

$$
0,\qquad 1,\qquad \alpha,\qquad 1+\alpha.
$$

### 先把四种形式上的算术做出来

加法仍然逐系数进行。例如，

$$
(1+\alpha)+\alpha
=1+(\alpha+\alpha)
=1.
$$

乘法按分配律展开，再使用 $\alpha^2=\alpha+1$。例如，

$$
\alpha(1+\alpha)
=\alpha+\alpha^2
=\alpha+(\alpha+1)
=1.
$$

因此 $\alpha$ 与 $1+\alpha$ 互为逆元。连同 $1^{-1}=1$，三个非零形式的逆元都已找到：

$$
1^{-1}=1,
\qquad
\alpha^{-1}=1+\alpha,
\qquad
(1+\alpha)^{-1}=\alpha.
$$

还可以继续算出

$$
\alpha^3=\alpha(\alpha+1)=1,
\qquad
(1+\alpha)^2=1+\alpha^2=\alpha.
$$

把两个一般输入写成

$$
a=a_0+a_1\alpha,
\qquad
b=b_0+b_1\alpha,
$$

则同一套运算给出

$$
a+b=(a_0+b_0)+(a_1+b_1)\alpha,
$$

以及

$$
\begin{aligned}
ab
&=a_0b_0+(a_0b_1+a_1b_0)\alpha+a_1b_1\alpha^2\\
&=(a_0b_0+a_1b_1)
 +(a_0b_1+a_1b_0+a_1b_1)\alpha.
\end{aligned}
$$

所有系数计算都在 $\mathbb F_2$ 中进行。这条乘法公式以后会直接成为两位输入、两位输出的计算规则。

与 $\mathbb Q(\sqrt2)$ 相比，构造动作相同：新元素满足一个二次方程，使乘积可以重新写成两个坐标。区别在于，这次每个坐标只有两种取值，因此一共只有 $2^2=4$ 种形式。

接下来要使这种构造适用于任意次数：怎样严格实现“令一个多项式等于零”？怎样保证不同的低次表达式确实代表不同元素？又怎样从所选方程判断每个非零元素都能求逆？这些问题可以由多项式商一起解决。

## 3. 多项式商：把一条方程变成完整的运算规则

### 3.1 相差约化关系的倍数，就代表同一个元素

固定整数 $s\ge1$，取次数为 $s$ 的首一多项式

$$
f(x)=x^s+c_{s-1}x^{s-1}+\cdots+c_1x+c_0,
\qquad c_i\in\mathbb F_2.
$$

此时先不要求 $f$ 不可约。

我们希望构造一个元素 $\alpha$，使 $f(\alpha)=0$。一旦这条关系成立，对任何多项式 $h$ 都会有

$$
f(\alpha)h(\alpha)=0.
$$

于是，相差 $fh$ 的两个多项式应当给出同一元素。这引出如下等价关系：

$$
p\sim q
\quad\Longleftrightarrow\quad
f\mid p-q.
$$

也就是说，存在 $h\in\mathbb F_2[x]$，使 $p-q=fh$。这个关系具有自反性、对称性与传递性：对应的差分别是 $0$、原来差的相反数，以及两个差的和，它们仍然是 $f$ 的倍数。

用 $[p]$ 表示 $p$ 所在的等价类：

$$
[p]=\{p+fh:h\in\mathbb F_2[x]\}.
$$

一个多项式 $p$ 是这个类的一个**代表元**。同一个类可以有很多代表元；类所记录的是按关系 $f=0$ 计算以后相同的结果。

记

$$
(f)=\{fh:h\in\mathbb F_2[x]\},
$$

则这些类组成的集合写作

$$
K_f=\mathbb F_2[x]/(f).
$$

这里的商记号表示按上述关系合并多项式。它本身已经构造出一个新集合，不需要先在某个更大的域中找到 $f$ 的根。

### 3.2 为什么可以直接用代表元相加、相乘

在这些类上定义

$$
[p]+[q]=[p+q],
\qquad
[p][q]=[pq].
$$

要让它们成为类上的运算，需要验证：换用同一类的其他代表元，结果仍属于同一个类。

设

$$
p'=p+fh,
\qquad
q'=q+fk.
$$

那么

$$
(p'+q')-(p+q)=f(h+k),
$$

而

$$
p'q'-pq=f(pk+hq+fhk).
$$

所以两种运算的结果都只改变了一个 $f$ 的倍数。这证明加法、乘法只依赖输入的类，与代表元的选择无关。

多项式的运算律随之传到这些类上。例如，

$$
([p][q])[r]=[(pq)r]=[p(qr)]=[p]([q][r]),
$$

$$
[p]([q]+[r])
=[p(q+r)]
=[pq]+[pr].
$$

同理可得交换律和加法群的各项性质。因此 $K_f$ 是交换环，其零元与单位元分别为 $[0]$、$[1]$。由于 $f$ 的次数至少为 $1$，它不能整除常数 $1$，所以 $[0]\ne[1]$。

现在令

$$
\alpha=[x].
$$

将常数类 $[0],[1]$ 简写为 $0,1$，便得到

$$
f(\alpha)=[f]=0.
$$

这说明我们确实构造出了满足所需方程的元素。

### 3.3 每个类为什么恰好需要 $s$ 个比特

对任意 $p\in\mathbb F_2[x]$ 作带余除法：

$$
p=hf+r,
\qquad
r=0\ \text{或}\ \deg r<s.
$$

因为 $p-r$ 是 $f$ 的倍数，所以 $[p]=[r]$。因此，每个类都能找到一个次数小于 $s$ 的代表元。

这个低次代表元还是唯一的。若 $r_1,r_2$ 都是这样的代表元且 $[r_1]=[r_2]$，则

$$
f\mid r_1-r_2.
$$

若 $r_1-r_2\ne0$，它的次数小于 $s=\deg f$，不可能被 $f$ 整除。因此只能有 $r_1=r_2$。

于是，每个元素唯一写成

$$
a=a_0+a_1\alpha+\cdots+a_{s-1}\alpha^{s-1},
\qquad a_i\in\mathbb F_2.
$$

这给出两个直接结论。首先，一共有 $2^s$ 个元素。其次，

$$
B_{\mathrm{pol}}=(1,\alpha,\ldots,\alpha^{s-1})
$$

是一组 $\mathbb F_2$-基，称为**多项式基**。当 $s=1$ 时，它只含一个基元素 $1$。

由此得到实际算法：加法逐系数 XOR；乘法先作多项式乘法，再除以 $f$ 取余式。

到这里，即使 $f$ 可约，商环、唯一低次代表元和 $s$ 位坐标也都成立。决定它是否为域的，是接下来的非零求逆。

### 3.4 不可约性怎样保证非零元素可逆

称 $f$ **不可约**，是指它不能分解成两个次数都为正的较低次多项式之积。

假设 $f$ 不可约，取非零元素 $[g]$，其中 $g$ 是其唯一低次代表元。因为

$$
g\ne0,
\qquad
\deg g<s,
$$

所以 $g$ 与 $f$ 没有非常数公因子，即

$$
\gcd(g,f)=1.
$$

这个条件可以转化为求逆算法。对 $f,g$ 反复作带余除法，每次非零余式的次数严格下降，最后得到最大公因式 $1$。再将各步等式倒着代回去，就会得到多项式 $u,v$，满足

$$
ug+vf=1.
$$

这称为多项式的贝祖等式；保留并倒代这些除法步骤的方法称为**扩展欧几里得算法**。

在商中取类，含 $f$ 的项变成零：

$$
[u][g]+[v][f]=[1],
$$

因此

$$
\boxed{[g]^{-1}=[u]}.
$$

每个非零元素都有逆元，所以 $K_f$ 是域。

反过来，若 $f$ 可约，写成

$$
f=gh,
\qquad
0<\deg g,\deg h<s,
$$

则 $[g]$ 和 $[h]$ 都是非零元素，却满足

$$
[g][h]=[f]=0.
$$

它们成为零因子，因而不可能可逆。比如选择 $f=x^2+x=x(x+1)$，商中仍有四个元素，却有

$$
[x][x+1]=0
$$

这一对非零零因子。

所以，对于次数至少为 $1$ 的 $f$，

$$
\boxed{
\mathbb F_2[x]/(f)\text{ 是域}
\quad\Longleftrightarrow\quad
f\text{ 不可约}
}.
$$

前一节的 $x^2+x+1$ 在 $0,1$ 处都不为零。二次多项式若可约，必有一次因子，也就有底域中的根；因此它不可约。由它得到的四元素域就是

$$
\mathbb F_4=\mathbb F_2[x]/(x^2+x+1),
\qquad \alpha=[x].
$$

商构造同时证明了前一节四种形式的不同性和全部运算律。

### 3.5 在八元素域中再求一次逆

取

$$
f(x)=x^3+x+1.
$$

它在 $0,1$ 处同样都取值 $1$。三次多项式若可约，至少有一个一次因子，因此这个 $f$ 也不可约。于是

$$
\mathbb F_2[x]/(x^3+x+1)
$$

是一个八元素域。在这个例子中仍记 $\alpha=[x]$，其关系为

$$
\alpha^3=\alpha+1.
$$

要计算 $1+\alpha$ 的逆元，可以直接除：

$$
x^3+x+1=(x^2+x)(x+1)+1.
$$

所以

$$
1=f(x)+(x^2+x)(x+1),
$$

在商中得到

$$
\boxed{(1+\alpha)^{-1}=\alpha^2+\alpha}.
$$

直接乘回去也能核对：

$$
(1+\alpha)(\alpha^2+\alpha)
=\alpha^3+\alpha
=(\alpha+1)+\alpha
=1.
$$

这里的关键动作与四元素域完全相同：运算由所选多项式决定，求逆由带余除法和倒代完成。

“在底域中无根”对二次、三次多项式足以判定不可约；更高次多项式还可能分成次数都至少为 $2$ 的因子，需要进一步检查。

### 3.6 抽象域与具体模型

有限域的标准存在唯一性定理告诉我们：每个整数 $s\ge1$ 都存在次数为 $s$ 的二元不可约多项式；任意两个含 $2^s$ 个元素的域都同构，即存在保持加法、乘法与单位元的一一对应。这里采用这两个结论，分别用于保证构造总能进行，以及统一所得域的名称。[^finite-fields]

因此，可以把这样的域统一记为

$$
K=\mathbb F_{2^s},
$$

也写成 $\mathrm{GF}(2^s)$。它包含由 $0,1$ 组成的底域 $\mathbb F_2$，扩张次数为

$$
[K:\mathbb F_2]=s.
$$

$s=1$ 时得到底域本身；$s>1$ 时得到真正较大的域。

同构类型唯一，并没有指定实际使用哪个不可约多项式，也没有指定哪个位串代表哪个元素。实际计算仍然要选择多项式模型和坐标基。

此后的一般论述使用 $K=\mathbb F_{2^s}$；未另作说明的具体算例仍使用

$$
\mathbb F_4=\mathbb F_2[x]/(x^2+x+1),
\qquad \alpha^2=\alpha+1.
$$

## 4. 从域元素到比特坐标

### 4.1 基决定一个元素怎样写成位串

多项式基只是可选基的一种。现在取 $K$ 在 $\mathbb F_2$ 上的任意一组基

$$
B=(\alpha_1,\ldots,\alpha_s).
$$

这里的下标是在给基元素编号；$\alpha_i$ 不必是生成元 $\alpha=[x]$ 的某个指定幂。

若

$$
a=\sum_{i=1}^s a_i\alpha_i,
\qquad a_i\in\mathbb F_2,
$$

则用列向量

$$
[a]_B=
\begin{bmatrix}
a_1\\
\vdots\\
a_s
\end{bmatrix}
$$

表示它的坐标。前面的 $[p]$ 表示多项式的等价类，带基下标的 $[a]_B$ 则表示域元素的坐标列。

加法在任意基下都逐位进行：

$$
[a+b]_B=[a]_B+[b]_B.
$$

因此，作为向量空间，$K$ 与 $\mathbb F_2^s$ 同构；域乘法则给这个向量空间增加了进一步的结构。

在 $\mathbb F_4$ 的多项式基 $B=(1,\alpha)$ 下，

$$
[0]_B=
\begin{bmatrix}0\\0\end{bmatrix},
\quad
[1]_B=
\begin{bmatrix}1\\0\end{bmatrix},
\quad
[\alpha]_B=
\begin{bmatrix}0\\1\end{bmatrix},
\quad
[1+\alpha]_B=
\begin{bmatrix}1\\1\end{bmatrix}.
$$

第一位是常数项系数，第二位是 $\alpha$ 的系数。乘法仍由 $\alpha^2=\alpha+1$ 决定。

这也说明为什么仅仅给出位串还不足以指定一个域。若在同样的二位坐标上另外规定逐位相乘，就会有

$$
(1,0)(0,1)=(0,0),
$$

出现非零零因子；而在上述域表示中，$(1,0)$ 代表单位元 $1$，所以它乘以 $(0,1)$ 的结果仍应为 $(0,1)$。两套乘法保持了相同的坐标集合，却给出不同的代数结构。

整数模 $2^s$ 的运算又是另一套结构。$K$ 中始终有 $1+1=0$；当 $s>1$ 时，整数模 $2^s$ 算术中的 $1+1$ 则不为零。

### 4.2 为什么这些坐标适合描述一组量子比特

一组 $s$ 个量子比特有 $2^s$ 个计算基向量：

$$
|a_1\cdots a_s\rangle,
\qquad a_i\in\{0,1\}.
$$

选定基 $B$ 后，可以按域元素重新标记它们：

$$
|a\rangle
\ \longleftrightarrow\
|a_1\cdots a_s\rangle,
\qquad
[a]_B=(a_1,\ldots,a_s)^T.
$$

例如，前面的 $\mathbb F_4$ 可以标记两个量子比特的四个计算基向量。

量子态仍然是这些基向量的复线性组合：

$$
|\psi\rangle=\sum_{a\in K}c_a|a\rangle,
\qquad
c_a\in\mathbb C,
\qquad
\sum_{a\in K}|c_a|^2=1.
$$

有限域承担的是计算基标签的算术；复数 $c_a$ 承担的是量子振幅。这两种运算各有自己的作用。

S008 §3.1 通过这样的基选择，把扩域标签与一组比特相联系，再将扩域上的操作展开为比特操作。[^S008-basis] 从这一角度看，接下来有两个具体问题：一个域运算怎样改变这些坐标？怎样用域内公式从标签读出一个 $0$ 或 $1$，进而指定正负相位？

平方映射和迹会提供第二个问题所需的工具；迹对偶基则会让这个工具同时读出全部坐标。

## 5. 从反复平方得到一个比特：Frobenius 与迹

### 5.1 四元素域中已经出现了一个坐标读数

在贯穿的 $\mathbb F_4$ 例子中，令

$$
a=a_0+a_1\alpha.
$$

由于特征为 $2$，展开平方时的交叉项抵消：

$$
\begin{aligned}
a^2
&=a_0^2+a_1^2\alpha^2\\
&=a_0+a_1(\alpha+1)\\
&=(a_0+a_1)+a_1\alpha.
\end{aligned}
$$

因此

$$
\boxed{a+a^2=a_1}.
$$

结果恰好落在 $\mathbb F_2$ 中，而且读出了当前基下的第二个坐标。我们只用了域中的平方和加法。

要将这种办法推广到 $s$ 维，先看平方映射在一般二元扩域中的行为。

### 5.2 平方是一个可逆的 $\mathbb F_2$-线性映射

定义

$$
\sigma:K\longrightarrow K,
\qquad
\sigma(a)=a^2.
$$

在特征 $2$ 中，

$$
(a+b)^2=a^2+b^2,
\qquad
(ab)^2=a^2b^2,
\qquad
1^2=1.
$$

所以 $\sigma$ 保持加法、乘法和单位元。对 $\lambda\in\mathbb F_2$，还有

$$
(\lambda a)^2=\lambda a^2,
$$

因此它是 $\mathbb F_2$-线性的。

若 $a^2=b^2$，则 $(a+b)^2=0$。域中没有零因子，所以 $a+b=0$，即 $a=b$。这证明 $\sigma$ 单射；有限集合上的单射也是满射，所以它可逆。

这样的可逆、保持域运算的自映射称为域自同构。$\sigma$ 称为 **Frobenius 自同构**。

这里的线性性以 $\mathbb F_2$ 为标量域。若把标量扩大到整个 $K$，则一般只有

$$
\sigma(\lambda a)=\lambda^2\sigma(a),
$$

所以当 $s>1$ 时，它不是一般的 $K$-线性映射。

在 $\mathbb F_4$ 的基 $B=(1,\alpha)$ 中，刚才的计算已经给出

$$
[a^2]_B=S[a]_B,
\qquad
S=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
\qquad
S^2=I.
$$

### 5.3 为什么平方迭代会回到原处

令 $q=2^s$。对任意 $a\ne0$，乘以 $a$ 会置换全部 $q-1$ 个非零元素。记这些非零元素的乘积为 $P$，则 $P\ne0$，并且

$$
P=\prod_{b\in K\setminus\{0\}}(ab)
=a^{q-1}P.
$$

消去 $P$，得到

$$
a^{q-1}=1.
$$

零元素也满足 $0^q=0$，因此对所有 $a\in K$ 都有

$$
\boxed{a^{2^s}=a}.
$$

换成映射语言，就是

$$
\sigma^s=\operatorname{id}.
$$

同一个幂关系还给出另一种求逆公式：

$$
a^{-1}=a^{2^s-2},
\qquad a\ne0.
$$

它与扩展欧几里得算法得到同一个逆元，只是采用了不同的计算路径。

### 5.4 把一轮平方迭代相加

现在定义从 $K$ 到底域 $\mathbb F_2$ 的**绝对迹**：

$$
\boxed{
\operatorname{tr}(a)
=a+a^2+a^{2^2}+\cdots+a^{2^{s-1}}
}.
$$

这些项是连续应用 Frobenius 所得到的像。再平方一次时，各项向前移动，最后一项由 $a^{2^s}=a$ 回到开头。因此

$$
\operatorname{tr}(a)^2
=\sum_{k=1}^{s}a^{2^k}
=\operatorname{tr}(a).
$$

在域中，$t^2=t$ 等价于 $t(t+1)=0$，所以只能有 $t=0$ 或 $1$。这证明

$$
\operatorname{tr}:K\longrightarrow\mathbb F_2.
$$

每个平方迭代都是 $\mathbb F_2$-线性的，它们的和也线性：

$$
\operatorname{tr}(a+b)
=\operatorname{tr}(a)+\operatorname{tr}(b),
$$

$$
\operatorname{tr}(\lambda a)
=\lambda\operatorname{tr}(a),
\qquad \lambda\in\mathbb F_2.
$$

这正是从域元素得到一个比特的域内公式。它只依赖域运算，与选取哪组坐标基无关。迹的标准有限域公式及其推广见 Conrad 的 Theorem 4.6；S008 §2.2 的式 (7)–(8) 使用相同结构。[^finite-fields][^S008-basis]

定义中始终相加 $s$ 项。即使某个元素的平方迭代提前回到自身，也保留重复项。例如，

$$
\operatorname{tr}(1)=s\bmod2.
$$

在 $\mathbb F_4$ 中，

$$
\operatorname{tr}(0)=0,
\qquad
\operatorname{tr}(1)=0,
\qquad
\operatorname{tr}(\alpha)=1,
\qquad
\operatorname{tr}(1+\alpha)=1.
$$

于是恢复了本节开头的结果：

$$
\operatorname{tr}(a_0+a_1\alpha)=a_1.
$$

迹本身不依赖基；“等于第二个坐标”则是当前多项式基中的具体表达。

### 5.5 把同一轮平方迭代相乘：绝对范数

与绝对迹对应，从 $K$ 到 $\mathbb F_2$ 的**绝对范数**定义为

$$
\begin{aligned}
\operatorname{Nm}(a)
&=a\cdot a^2\cdot a^{2^2}\cdots a^{2^{s-1}}\\
&=a^{1+2+\cdots+2^{s-1}}\\
&=a^{2^s-1}.
\end{aligned}
$$

各因子中的 Frobenius 保持乘法，因此

$$
\operatorname{Nm}(ab)
=\operatorname{Nm}(a)\operatorname{Nm}(b).
$$

由前面的幂关系，

$$
\boxed{
\operatorname{Nm}(a)=
\begin{cases}
0,&a=0,\\
1,&a\ne0.
\end{cases}
}
$$

所以这里的绝对范数只区分零与非零。它虽然与基无关且具有乘法性，却不能逐位区分域元素。

“绝对”说明值域取底域 $\mathbb F_2$。对值域更大的子域还可以定义相对迹、相对范数；相对范数的非零值一般不全等于 $1$。本文的 $\operatorname{tr}$、$\operatorname{Nm}$ 始终采用上述绝对版本。[^finite-fields]

## 6. 用迹对偶基读出每一个坐标

迹一次只输出一个比特，但可以先乘一个固定元素，再取迹：

$$
a\longmapsto\operatorname{tr}(ba),
\qquad b\in K.
$$

在 $\mathbb F_4$ 中，$\operatorname{tr}(a)$ 已经读出第二位；我们希望找到另一个固定乘数，读出第一位。一般情形则是寻找 $s$ 个这样的乘数，让每个读数恰好对应所选基的一位。

这要求这些读数足够丰富：每个非零元素都应当能被某个读数识别出来。

### 6.1 迹配对为什么不会漏掉任何非零元素

先证明迹不是恒零函数。考虑多项式

$$
T(X)=X+X^2+\cdots+X^{2^{s-1}}.
$$

它非零，次数为 $2^{s-1}$，小于 $|K|=2^s$。一个域上的非零多项式至多有其次数那么多个不同的根：每出现一个根，就能由带余除法提出一个一次因子，次数随之下降。因此 $T$ 不可能在 $K$ 的全部元素上都为零。

迹又只取 $0,1$，所以存在 $c\in K$，满足

$$
\operatorname{tr}(c)=1.
$$

现在取任意 $a\ne0$，令

$$
b=a^{-1}c,
$$

便得到

$$
\operatorname{tr}(ab)=1.
$$

因此，对称双线性配对

$$
\langle a,b\rangle_{\operatorname{tr}}
=\operatorname{tr}(ab)
$$

是**非退化的**：若一个元素与所有元素配对都得到零，那么它只能是零元素。双线性来自乘法的分配律和迹的线性性，对称性来自域乘法的交换律。

非退化性允许某些非零元素与自身配对为零。例如在 $\mathbb F_4$ 中，

$$
\operatorname{tr}(1\cdot1)=0,
\qquad
\operatorname{tr}(1\cdot\alpha)=1.
$$

关键在于能找到某个检测它的配对对象，而不是要求自身配对非零。

### 6.2 为一组基找到对应的读数

固定

$$
B=(\alpha_1,\ldots,\alpha_s).
$$

我们希望找到 $\beta_1,\ldots,\beta_s$，使

$$
\boxed{
\operatorname{tr}(\alpha_i\beta_j)=\delta_{ij}
},
\qquad 1\le i,j\le s,
$$

其中 $\delta_{ij}$ 在 $i=j$ 时为 $1$，否则为 $0$。这样，与 $\beta_j$ 配对时，只有第 $j$ 个基方向被保留下来。

这些元素可以通过一次二进制矩阵求逆得到。定义迹配对的 Gram 矩阵

$$
G_{ij}=\operatorname{tr}(\alpha_i\alpha_j).
$$

它是可逆的。事实上，若 $Gv=0$，令

$$
b=\sum_{j=1}^s v_j\alpha_j,
$$

便有

$$
\operatorname{tr}(\alpha_i b)=0
$$

对所有基元素成立。任意 $a\in K$ 都是这些基元素的线性组合，因此 $\operatorname{tr}(ab)=0$ 对所有 $a$ 成立。由非退化性，$b=0$，所以 $v=0$。

现在取

$$
\beta_j=\sum_{k=1}^s(G^{-1})_{kj}\alpha_k.
$$

代入可得

$$
\operatorname{tr}(\alpha_i\beta_j)
=\sum_{k=1}^sG_{ik}(G^{-1})_{kj}
=\delta_{ij}.
$$

由于 $G^{-1}$ 可逆，$\beta_1,\ldots,\beta_s$ 本身也组成一组基。满足这些条件的元素是唯一的，因为对应的线性方程组有唯一解。这组基

$$
B^*=(\beta_1,\ldots,\beta_s)
$$

称为 $B$ 的**迹对偶基**。

对任意

$$
a=\sum_{i=1}^s a_i\alpha_i,
$$

有

$$
\operatorname{tr}(a\beta_j)
=\sum_{i=1}^s a_i\operatorname{tr}(\alpha_i\beta_j)
=a_j.
$$

于是，坐标读取与重构公式为

$$
\boxed{
a_i=\operatorname{tr}(a\beta_i),
\qquad
a=\sum_{i=1}^s\operatorname{tr}(a\beta_i)\alpha_i
}.
$$

每个 $\beta_i$ 都有一个明确任务：先乘它，再取迹，就读出第 $i$ 位。

交换两组基的角色，还得到

$$
[a]_{B^*}
=
\begin{bmatrix}
\operatorname{tr}(a\alpha_1)\\
\vdots\\
\operatorname{tr}(a\alpha_s)
\end{bmatrix}
=G[a]_B.
$$

这个等式将在对照不同的二元化约定时使用。

### 6.3 在四元素域中实际算出对偶基

取 $B=(1,\alpha)$。由前面的迹值，

$$
G=
\begin{bmatrix}
\operatorname{tr}(1)&\operatorname{tr}(\alpha)\\
\operatorname{tr}(\alpha)&\operatorname{tr}(\alpha^2)
\end{bmatrix}
=
\begin{bmatrix}
0&1\\
1&1
\end{bmatrix},
$$

而

$$
G^{-1}=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}.
$$

因此

$$
\boxed{B^*=(1+\alpha,1)}.
$$

对 $a=a_0+a_1\alpha$，两个坐标分别是

$$
a_0=\operatorname{tr}((1+\alpha)a),
\qquad
a_1=\operatorname{tr}(a).
$$

这补齐了上一节只读出第二位的计算。比如 $a=1+\alpha$ 时，

$$
\operatorname{tr}((1+\alpha)^2)
=\operatorname{tr}(\alpha)=1,
$$

$$
\operatorname{tr}(1+\alpha)=1,
$$

所以两位都读成 $1$。

### 6.4 自对偶基使读数与坐标方向重合

若一组基等于自己的迹对偶基，即

$$
\operatorname{tr}(\alpha_i\alpha_j)=\delta_{ij},
$$

就称它关于迹配对**自对偶**。此时 $G=I$，坐标公式简化为

$$
a_i=\operatorname{tr}(a\alpha_i).
$$

在 $\mathbb F_4$ 中，考虑

$$
N=(\alpha,\alpha^2)=(\alpha,1+\alpha).
$$

因为 $1=\alpha+\alpha^2$，这两个元素张成整个域，因而是一组基。其迹配对矩阵为

$$
\begin{bmatrix}
\operatorname{tr}(\alpha^2)&\operatorname{tr}(\alpha^3)\\
\operatorname{tr}(\alpha^3)&\operatorname{tr}(\alpha^4)
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}.
$$

所以 $N$ 是自对偶基。在这组基下，写

$$
a=u_1\alpha+u_2\alpha^2,
$$

便有

$$
u_1=\operatorname{tr}(a\alpha),
\qquad
u_2=\operatorname{tr}(a\alpha^2).
$$

S008 p.15 的式 (11) 正是在自对偶基下使用这一简化。对每个 $s\ge1$，二元扩域 $\mathbb F_{2^s}/\mathbb F_2$ 都存在自对偶基；这里采用这个存在性结论。任意给定基的对偶基则已经由上面的 Gram 矩阵构造得到，并不要求原基自对偶。[^S008-basis]

一般基下，迹配对的坐标表达为

$$
\operatorname{tr}(ab)=[a]_B^T G[b]_B.
$$

自对偶基下，它才直接成为通常的二进制点积：

$$
\operatorname{tr}(ab)=[a]_B^T[b]_B.
$$

这正是自对偶基在后面的量子相位计算中方便的原因。

> [!note]- 与子空间正交补的关系
>
> 对一个子空间 $W\subseteq K$，可以定义
>
> $$
> W^\perp=\{b\in K:\operatorname{tr}(wb)=0,\ \forall w\in W\}.
> $$
>
> 整个配对非退化，并不保证 $W\cap W^\perp=\{0\}$，因此也不自动给出 $K=W\oplus W^\perp$。正交补与直和补是两种不同的要求，相关线性代数区别见 [[二进制空间性质]]。

## 7. 域乘法怎样变成二进制矩阵

### 7.1 固定一个乘数，得到线性映射

固定 $\gamma\in K$，考虑

$$
m_\gamma:K\longrightarrow K,
\qquad
a\longmapsto\gamma a.
$$

分配律给出

$$
m_\gamma(a+b)=m_\gamma(a)+m_\gamma(b),
$$

而对 $\lambda\in\mathbb F_2$，

$$
m_\gamma(\lambda a)=\lambda m_\gamma(a).
$$

所以它是 $\mathbb F_2$-线性映射。在所选基 $B$ 下，定义矩阵 $M_\gamma$，使

$$
\boxed{[\gamma a]_B=M_\gamma[a]_B}.
$$

线性映射的矩阵列由基元素的像决定，因此第 $j$ 列是

$$
[\gamma\alpha_j]_B.
$$

现在利用迹对偶基读取这列的第 $i$ 个坐标，就得到

$$
\boxed{
(M_\gamma)_{ij}
=\operatorname{tr}(\beta_i\gamma\alpha_j)
}.
$$

这给出两种等价的计算办法：逐列计算 $\gamma\alpha_j$ 并展开到 $B$ 中；或者直接用迹对偶公式计算每个条目。

### 7.2 四元素域中的乘法矩阵

取 $B=(1,\alpha)$。先直接展开：

$$
\begin{aligned}
\alpha(a_0+a_1\alpha)
&=a_0\alpha+a_1(\alpha+1)\\
&=a_1+(a_0+a_1)\alpha.
\end{aligned}
$$

所以

$$
\boxed{
M_\alpha=
\begin{bmatrix}
0&1\\
1&1
\end{bmatrix}
}.
$$

用对偶基 $B^*=(1+\alpha,1)$ 计算，则得到同一矩阵：

$$
M_\alpha=
\begin{bmatrix}
\operatorname{tr}((1+\alpha)\alpha)&
\operatorname{tr}((1+\alpha)\alpha^2)\\
\operatorname{tr}(\alpha)&
\operatorname{tr}(\alpha^2)
\end{bmatrix}
=
\begin{bmatrix}
0&1\\
1&1
\end{bmatrix}.
$$

域中的加乘关系也会变成矩阵关系。因为

$$
(\gamma+\eta)a=\gamma a+\eta a,
\qquad
(\gamma\eta)a=\gamma(\eta a),
$$

所以

$$
M_{\gamma+\eta}=M_\gamma+M_\eta,
\qquad
M_{\gamma\eta}=M_\gamma M_\eta,
$$

$$
M_0=0,
\qquad
M_1=I.
$$

特别地，

$$
\gamma\ne0
\quad\Longrightarrow\quad
M_\gamma^{-1}=M_{\gamma^{-1}}.
$$

不同域元素也会给出不同矩阵：若 $M_\gamma=M_\eta$，让两个线性映射作用于域元素 $1$，就得到 $\gamma=\eta$。

因此，映射 $\gamma\mapsto M_\gamma$ 将域嵌入一族二进制矩阵中。这一族矩阵彼此交换，而且每个非零矩阵都可逆。

在当前例子中，

$$
M_\alpha^2=I+M_\alpha
=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix},
\qquad
M_\alpha^3=I,
$$

分别对应 $\alpha^2=1+\alpha$ 与 $\alpha^3=1$。更一般地，若 $\gamma=g(\alpha)$，则

$$
M_\gamma=g(M_\alpha),
\qquad
f(M_\alpha)=0,
$$

其中矩阵多项式的常数 $1$ 用 $I$ 表示。

### 7.3 换基同时改变输入坐标和输出坐标

若另一组基为 $B'$，令 $C$ 的各列为 $B'$ 中基元素的 $B$-坐标，则

$$
[a]_B=C[a]_{B'}.
$$

把乘法公式的输入和输出都换成新坐标：

$$
C[\gamma a]_{B'}
=M_\gamma^{(B)}C[a]_{B'}.
$$

所以

$$
\boxed{
M_\gamma^{(B')}
=C^{-1}M_\gamma^{(B)}C
}.
$$

例如在 $\mathbb F_4$ 中，取

$$
B=(1,\alpha),
\qquad
B'=(1,1+\alpha).
$$

此时

$$
C=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
$$

并且

$$
[\alpha]_B=
\begin{bmatrix}0\\1\end{bmatrix},
\qquad
[\alpha]_{B'}=
\begin{bmatrix}1\\1\end{bmatrix}.
$$

乘以同一个 $\alpha$，在新基下的矩阵变为

$$
M_\alpha^{(B')}
=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}.
$$

变化的是描述这个运算的坐标和矩阵，域中的乘积仍是同一个乘积。

### 7.4 对照 S008 的迹矩阵展开

S008 p.15 在展开扩域生成矩阵时使用数组

$$
(A_\gamma)_{ij}
=\operatorname{tr}(\gamma\alpha_i\alpha_j).
$$

要与本文的 $M_\gamma$ 对照，需要保留它的基和读数约定。由

$$
[a]_{B^*}=G[a]_B
$$

可得

$$
[\gamma a]_{B^*}
=GM_\gamma[a]_B.
$$

另一方面，

$$
(GM_\gamma)_{ij}
=\operatorname{tr}(\alpha_i\gamma\alpha_j).
$$

因此，在本文的列坐标约定下，这个数组有明确的含义：

$$
\boxed{
A_\gamma=GM_\gamma,
\qquad
[\gamma a]_{B^*}=A_\gamma[a]_B
}.
$$

它使用 $B$ 作为输入基，并用 $B^*$ 表示输出；等价地，先对各个基方向作乘法，再用 $\operatorname{tr}(\alpha_i\,\cdot)$ 读取结果。S008 的相应展开需要连同 p.15 的坐标语境和脚注 8 阅读。[^S008-basis]

当 $B$ 自对偶时，$G=I$，两种写法合一：

$$
(M_\gamma)_{ij}
=\operatorname{tr}(\alpha_i\gamma\alpha_j).
$$

在任意基下则应保留对偶基。最简单的检查是取 $\gamma=1$：正确的同基乘法矩阵总是 $M_1=I$，而 $A_1=G$。因此，后面的同基运算始终采用

$$
(M_\gamma)_{ij}
=\operatorname{tr}(\beta_i\gamma\alpha_j).
$$

> [!note]- 与一般系数代数的块表示比较
>
> 让一个元素通过左乘作用于整个代数，再取这个线性映射的矩阵，称为正则表示。有限维含幺 $\mathbb F_2$-代数也可以这样表示；结合律保证乘法对应矩阵复合，作用于单位元又保证表示是单射。域的额外性质保证这里每个非零乘法矩阵都可逆。
>
> [[Lifted product code]] 中的循环系数环 $\mathbb F_2[x]/(x^\ell-1)$ 也使用相关的块表示。当 $\ell>1$ 时，$x^\ell-1$ 有一次真因子 $x+1$，因此这个环不是二元扩域。若还要把环内的反对合——反转乘法次序的对合——对应为二进制转置，需要对所选表示另行验证相容性；保留乘法本身并不自动给出这种对应。

### 7.5 两个乘数都变化时，出现双线性项

若两个输入都未知，写成

$$
a=\sum_{i=1}^s a_i\alpha_i,
\qquad
b=\sum_{j=1}^s b_j\alpha_j.
$$

仍然可以写

$$
[ab]_B=M_b[a]_B,
$$

但此时 $M_b$ 随输入 $b$ 改变。由矩阵表示的加法性质，

$$
M_b=\sum_{j=1}^s b_jM_{\alpha_j}.
$$

因此，输出会包含一个 $a$ 坐标与一个 $b$ 坐标的乘积。

令 $(ab)_k$ 表示乘积的第 $k$ 个 $B$-坐标。利用迹对偶公式，

$$
\begin{aligned}
(ab)_k
&=\operatorname{tr}(\beta_kab)\\
&=\sum_{i,j=1}^s
a_i b_j\operatorname{tr}(\beta_k\alpha_i\alpha_j).
\end{aligned}
$$

定义固定的二进制数

$$
c_{ij}^{\,k}
=\operatorname{tr}(\beta_k\alpha_i\alpha_j),
$$

就得到

$$
\boxed{
(ab)_k=\sum_{i,j=1}^s c_{ij}^{\,k}a_i b_j
}.
$$

这些数称为所选基下的**乘法结构常数**，记录每个基元素乘积怎样展开。一旦域模型与基固定，它们就固定。

例如在 $\mathbb F_4$ 的多项式基中，

$$
M_b=b_0I+b_1M_\alpha
=
\begin{bmatrix}
b_0&b_1\\
b_1&b_0+b_1
\end{bmatrix},
$$

从而恢复第 2 节的乘法：

$$
ab=(a_0b_0+a_1b_1)
 +(a_0b_1+a_1b_0+a_1b_1)\alpha.
$$

固定 $b$，这是关于 $a$ 的线性公式；固定 $a$，它也关于 $b$ 线性。这称为乘法的**双线性**。

若把两个输入拼成一个 $2s$ 维二进制向量，一般乘法则不是这个整体输入上的线性映射。令 $m(a,b)=ab$，则

$$
(1,1)=(1,0)+(0,1),
$$

但

$$
m(1,1)=1,
\qquad
m(1,0)+m(0,1)=0.
$$

因此，分别对每个输入线性，与对拼接输入线性，是两个不同的条件。

平方映射仍然线性也由此可以理解：将两个独立输入限制为同一个 $a$ 后，交叉项成对抵消，而比特满足 $a_i^2=a_i$。所以 $a\mapsto a^2$ 的线性性与一般乘法的双线性完全相容。

## 8. S008 中的算术接口：从迹相位到可逆乘法

现在已有域元素、坐标、迹以及乘法结构常数，可以将它们放回第 4 节的量子寄存器中。

这里的操作先在每个计算基向量上定义，再按复线性延拓到任意叠加态。一个计算基的一一置换会给出酉操作；将多个输入覆盖为同一个输出则不能直接成为这样的门。

### 8.1 可逆二进制线性算术

CNOT 门在两个比特上的规则为

$$
|u,v\rangle\longmapsto|u,u+v\rangle,
$$

其中加法在 $\mathbb F_2$ 中进行。SWAP 门交换两位。它们分别完成坐标相加与坐标交换。

对任意可逆二进制矩阵，高斯消元只需要行相加和行交换，因为 $\mathbb F_2$ 中非零主元只有 $1$。将消元步骤倒过来，就能用 CNOT/SWAP 网络实现对应的坐标变换。[^circuits]

于是，前面得到的几类运算都有直接实现。域加法采用保留一个输入的形式：

$$
|a,b\rangle\longmapsto|a,a+b\rangle.
$$

在同一基下，只需对对应位置逐位施加 CNOT。

固定 $\gamma\ne0$ 时，

$$
|a\rangle\longmapsto|\gamma a\rangle
$$

由可逆矩阵 $M_\gamma$ 实现。Frobenius 与两种基编码之间的变换也由可逆二进制矩阵实现。

零常数需要单独区分：$a\mapsto0$ 虽然是线性映射，却不是可逆的原地操作。保留输入、将结果写入另一个寄存器，是另一种计算任务。

这些可逆线性操作属于通常的比特 Clifford 操作。为了说明这个名称及后面的非 Clifford 判断，先建立所需的最小定义。

对 $n$ 位计算基标签 $r\in\mathbb F_2^n$，定义

$$
X(u)|r\rangle=|r+u\rangle,
\qquad
Z(v)|r\rangle=(-1)^{v^Tr}|r\rangle,
$$

其中 $u,v\in\mathbb F_2^n$。它们分别描述指定位置的比特翻转和正负相位。由这些算子及整体相位 $1,-1,i,-i$ 组成比特 Pauli 群。

一个酉操作是 **Clifford 操作**，是指它在共轭下将每个 Pauli 算子仍送到 Pauli 算子。[^circuits]

若可逆二进制矩阵 $A$ 定义

$$
U_A|r\rangle=|Ar\rangle,
$$

则直接作用于计算基可得

$$
U_AX(u)U_A^\dagger=X(Au),
$$

$$
U_AZ(v)U_A^\dagger=Z(A^{-T}v),
$$

其中 $A^{-T}=(A^{-1})^T$。所以这些线性置换确实保持 Pauli 群。域加法、固定非零常数乘法、换基与 Frobenius 的 Clifford 性，都可以由已经建立的线性表示直接看出；它们对应 S008 的 Remark 3.4 中的相关算术操作。[^S008-basis]

### 8.2 三个域标签怎样决定一个相位

给每个计算基向量乘以 $1$ 或 $-1$，会得到一个保持标签的酉操作，称为对角相位门。迹正好可以为相位的指数提供一个比特。

S008 §3.2.1 的式 (12) 定义三寄存器操作

$$
\boxed{
D_K|x,y,z\rangle
=(-1)^{\operatorname{tr}(xyz)}|x,y,z\rangle
},
\qquad x,y,z\in K.
$$

论文称它为扩域上的 qudit-CCZ 门。这里每个域标签对应一个 $s$ 比特寄存器，所以整个操作作用于 $3s$ 个比特。[^S008-phase]

这个公式包含三个已建立的动作：先在 $K$ 中求乘积 $xyz$，再用迹读成 $0$ 或 $1$，最后据此赋予正负相位。

选定基 $B=(\alpha_1,\ldots,\alpha_s)$，展开

$$
x=\sum_i x_i\alpha_i,
\qquad
y=\sum_j y_j\alpha_j,
\qquad
z=\sum_k z_k\alpha_k.
$$

利用迹的线性性，

$$
\boxed{
\operatorname{tr}(xyz)
=\sum_{i,j,k=1}^s
x_i y_j z_k\operatorname{tr}(\alpha_i\alpha_j\alpha_k)
}.
$$

这就是 S008 式 (13) 的展开。该等式在任意基下都成立；论文为后续计算选择了自对偶基。[^S008-phase]

普通三比特 CCZ 门的作用是

$$
|u,v,w\rangle
\longmapsto
(-1)^{uvw}|u,v,w\rangle.
$$

因此，对每个满足

$$
\operatorname{tr}(\alpha_i\alpha_j\alpha_k)=1
$$

的三元组，在第一寄存器第 $i$ 位、第二寄存器第 $j$ 位和第三寄存器第 $k$ 位上施加一个普通 CCZ，就能实现上述展开。指数在 $\mathbb F_2$ 中相加，对应这些正负相位相乘。

这里已经可以看到扩域表达的作用：一条 $\operatorname{tr}(xyz)$ 同时组织了多个比特之间的三次相位关系，具体关系由基元素的乘法和迹决定。

### 8.3 在 $\mathbb F_4$ 中展开一次迹相位

采用前面已经验证为自对偶的基

$$
N=(\alpha,\alpha^2).
$$

写

$$
x=x_1\alpha+x_2\alpha^2,
\qquad
y=y_1\alpha+y_2\alpha^2,
\qquad
z=z_1\alpha+z_2\alpha^2.
$$

因为

$$
\alpha^3=1,
\qquad
\operatorname{tr}(1)=0,
\qquad
\operatorname{tr}(\alpha)=\operatorname{tr}(\alpha^2)=1,
$$

所以三个基因子全取 $\alpha$ 时，其乘积的迹为零；全取 $\alpha^2$ 时也为零。混合选取时，乘积是 $\alpha$ 或 $\alpha^2$，迹为 $1$。

因此，

$$
\begin{aligned}
\operatorname{tr}(xyz)
={}&x_1y_1z_2+x_1y_2z_1+x_2y_1z_1\\
&+x_1y_2z_2+x_2y_1z_2+x_2y_2z_1.
\end{aligned}
$$

每一项都对应三个寄存器中各取一位的 CCZ 相位。这是按迹公式得到的一种直接展开，并不涉及最优线路的判断。

### 8.4 Hadamard 怎样把迹相位变成乘积

要真正计算两个未知输入的乘积，采用完整的可逆操作

$$
\boxed{
U|x,y,c\rangle
=|x,y,c+xy\rangle
}.
$$

它保留 $x,y$，将乘积加到第三个寄存器中。再次施加时，$xy$ 被加两次，因此

$$
U^2=I.
$$

当 $c=0$ 时，第三个寄存器得到 $xy$。

S008 的 Claim 3.5 说明，扩域 qudit-CCZ 配合 Clifford 操作可以完成这个乘法任务。下面保留任意初始目标 $c$，把同一计算写成上述完整可逆门。[^S008-phase]

单比特 Hadamard 门由

$$
H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
H|1\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}
$$

定义。它满足 $H^2=I$，并在共轭下交换单比特 $X$ 与 $Z$，因此是 Clifford 门。

记 $H^{\otimes s}$ 为对一个寄存器中的每一位各施加一次 $H$。在比特坐标中，

$$
H^{\otimes s}|z_1\cdots z_s\rangle
=
\frac1{\sqrt{2^s}}
\sum_{t_1,\ldots,t_s\in\mathbb F_2}
(-1)^{\sum_i z_it_i}|t_1\cdots t_s\rangle.
$$

现在选择自对偶基 $B$。因为

$$
\sum_i z_it_i=\operatorname{tr}(zt),
$$

所以可以将这个变换写成域标签的形式：

$$
\boxed{
H^{\otimes s}|z\rangle
=
\frac1{\sqrt{2^s}}
\sum_{t\in K}(-1)^{\operatorname{tr}(zt)}|t\rangle
}.
$$

这就是 S008 式 (14)。自对偶性用在将比特点积识别为 $\operatorname{tr}(zt)$ 的这一步；在一般基下，迹配对还带有 Gram 矩阵 $G$。[^S008-phase]

固定 $x,y$，先对第三寄存器施加 $H^{\otimes s}$，再施加 $D_K$，得到

$$
|x,y\rangle
\frac1{\sqrt{2^s}}
\sum_{z\in K}
(-1)^{\operatorname{tr}(cz)+\operatorname{tr}(xyz)}
|z\rangle.
$$

再对第三寄存器施加一次 $H^{\otimes s}$，其输出 $|t\rangle$ 的振幅为

$$
\frac1{2^s}
\sum_{z\in K}
(-1)^{\operatorname{tr}(z(c+xy+t))}.
$$

要计算这个和，考虑任意 $u\in K$。若 $u=0$，每一项都等于 $1$。若 $u\ne0$，迹配对的非退化性保证存在 $z_0$，使

$$
\operatorname{tr}(z_0u)=1.
$$

将求和变量由 $z$ 改为 $z+z_0$，求和集合不变，每一项的符号却都翻转。因此这个和等于其相反数，只能为零。这里相加的是复数振幅，而不是域元素。于是

$$
\sum_{z\in K}(-1)^{\operatorname{tr}(zu)}
=
\begin{cases}
2^s,&u=0,\\
0,&u\ne0.
\end{cases}
$$

代入 $u=c+xy+t$，只有 $t=c+xy$ 的振幅为 $1$，其余全部为零。因此，

$$
|x,y,c\rangle
\longmapsto
|x,y,c+xy\rangle.
$$

这就证明：对第三寄存器逐位施加 Hadamard、施加一次扩域 $D_K$、再逐位施加 Hadamard，恰好实现可逆乘法 $U$。计算在每个计算基向量上成立，复线性延拓后也就对任意叠加态成立。

这里的“一次”指一次三寄存器的扩域 qudit-CCZ；它的比特展开由上一小节的迹系数决定，并不表示任意扩张次数都只需一个普通三比特 CCZ。

### 8.5 为什么这个可逆乘法不是 Clifford

一般乘法含有双线性项，因此 $U$ 不能仅由 CNOT/SWAP 网络实现。要进一步判断它不是 Clifford，需要使用前面给出的 Pauli 共轭条件。

记 $Z_{c,k}$ 为第三个寄存器第 $k$ 位上的 $Z$，即

$$
Z_{c,k}|x,y,c\rangle
=(-1)^{c_k}|x,y,c\rangle.
$$

由于 $U^{-1}=U$，直接计算得到

$$
U^\dagger Z_{c,k}U|x,y,c\rangle
=(-1)^{c_k+(xy)_k}|x,y,c\rangle.
$$

一个对角、相位只取 $\pm1$ 的比特 Pauli 算子，其相位只能是

$$
(-1)^{\varepsilon+v^Tr},
$$

其中 $r$ 是全部输入比特，$\varepsilon$ 与 $v$ 固定。因此它的指数是二进制仿射函数，即一个常数加若干一次项。

而 $(xy)_k$ 不是这样的函数。它在 $x=0$ 或 $y=0$ 时恒为零，却在

$$
x=1,
\qquad
y=\alpha_k
$$

时等于 $1$。若它是仿射函数，原点处为零会迫使常数项为零；在两组输入分别为零的子空间上恒零，又会迫使全部一次项为零，从而无法在后一组输入上取 $1$。

因此 $c_k+(xy)_k$ 也不是仿射函数，共轭后的算子不是 Pauli，故

$$
\boxed{U\text{ 不是比特 Clifford 酉操作}}.
$$

$D_K$ 与 $U$ 通过 Hadamard 共轭相联系，所以 $D_K$ 也不是 Clifford。这个结论针对的是已经明确写出的可逆乘法和迹相位门。进一步讨论对角比特门的 Clifford 层级，可接着阅读 [[对角相位门的Clifford层级]]。

当 $s=1$ 时，$K=\mathbb F_2$，迹就是恒等映射。此时 $D_K$ 退化为普通 CCZ，而 $U$ 就是保留前两位、按它们的乘积翻转第三位的 Toffoli 门。

至此，从域到比特操作的计算过程已经闭合：多项式关系规定乘法，基将元素写成比特，迹对偶基读取坐标；固定乘数产生常矩阵，两个未知乘数产生双线性项；同一乘法还可以进入迹相位，并通过 Hadamard 变成寄存器中的乘积。这些正是 S008 相关代数表达能够连接到比特实现的原因。

## 选读一：用幂表示非零元素，本原元与不可约多项式

多项式基便于加法和约化。若主要处理非零元素的乘除，还可以使用幂表示。

有限域的非零乘法群

$$
K^\times=K\setminus\{0\}
$$

是循环群。这里采用乘法群循环性的标准定理。[^finite-fields] 因此存在元素 $\omega$，使每个非零元素唯一写成

$$
\omega^k,
\qquad
0\le k\le2^s-2.
$$

这样的 $\omega$ 称为**本原元**。它的乘法阶，即满足 $\omega^n=1$ 的最小正整数 $n$，为 $2^s-1$。

在这种表示中，

$$
\omega^i\omega^j=\omega^{i+j},
\qquad
(\omega^i)^{-1}=\omega^{-i},
$$

指数按模 $2^s-1$ 计算。零元素另行处理；域加法仍需使用域中的加法规则，不能改成指数相加。

构造域时选择不可约 $f$，保证的是所有非零元素可逆。指定生成元 $\alpha=[x]$ 是否遍历全部非零元素，还要检查它的阶。若 $\alpha\ne0$ 且阶为 $2^s-1$，才称这个不可约 $f$ 为**本原多项式**。其中 $\alpha\ne0$ 这一条件也覆盖 $s=1$ 的情形：例如不可约一次式 $f=x$ 给出的 $\alpha$ 就是零。

在 $\mathbb F_4$ 的例子中，$\alpha$ 的阶为 $3$，所以 $x^2+x+1$ 同时不可约且本原。下面的四次例子则把两者区分开：

$$
f(x)=x^4+x^3+x^2+x+1.
$$

它在 $0,1$ 处都不为零，所以没有一次因子。若可约，就必须分成两个不可约二次因子。$\mathbb F_2$ 上唯一的首一不可约二次式是 $x^2+x+1$，而

$$
f(x)=x^2(x^2+x+1)+(x+1),
$$

说明它不被这个二次式整除。因此 $f$ 不可约。

但在由它构造的 $\mathbb F_{16}$ 中，

$$
(x+1)f(x)=x^5+1
$$

给出

$$
\alpha^5=1.
$$

又因为 $\alpha\ne1$，它的阶为 $5$，而不是 $|\mathbb F_{16}^\times|=15$。所以这个 $f$ 完全可以构造域，却不是本原多项式。

## 选读二：Frobenius 的周期与子域

### Frobenius 的阶恰好等于扩张次数

主线已经证明

$$
\sigma^s=\operatorname{id}.
$$

实际上 $\sigma$ 的阶恰好是 $s$。若某个 $0<k<s$ 满足 $\sigma^k=\operatorname{id}$，那么 $K$ 的全部 $2^s$ 个元素都会满足

$$
a^{2^k}=a.
$$

这使它们全部成为非零多项式 $X^{2^k}-X$ 的根，但该多项式的次数只有 $2^k<2^s$，与根数上界矛盾。

在多项式模型中，每个元素都是 $\alpha=[x]$ 的多项式。因此，一个固定 $\mathbb F_2$ 的域自同构由 $\alpha$ 的像完全确定；这个像又必须是 $f$ 的根，所以这样的自同构至多有 $s$ 个。

而

$$
\operatorname{id},\sigma,\ldots,\sigma^{s-1}
$$

已经给出 $s$ 个不同的自同构，因此它们就是全部。这些映射在复合下组成该有限域扩张的伽罗瓦群：

$$
\operatorname{Gal}(K/\mathbb F_2)
=\langle\sigma\rangle
\cong\mathbb Z/s\mathbb Z.
$$

单次平方固定的元素只有 $0,1$。某个具体元素的平方轨道可以比 $s$ 短；$\sigma$ 的阶为 $s$，描述的是使整个映射同时复原所需的最小正次数。

### 哪些较小的有限域能出现在 $K$ 中

有限域的子域定理给出精确条件：对正整数 $d$，$K=\mathbb F_{2^s}$ 含有大小为 $2^d$ 的子域，当且仅当

$$
d\mid s.
$$

存在时这个子域唯一，并且等于

$$
\boxed{
E_d=\{a\in K:a^{2^d}=a\}
}.
$$

这里采用该定理的存在性与唯一性。[^finite-fields]

整除条件的必要性也能直接从坐标计数看出。若 $E\subseteq K$ 有 $2^d$ 个元素，将 $K$ 看成 $E$ 上的 $r$ 维向量空间，就有

$$
2^s=(2^d)^r,
$$

所以 $s=dr$。

固定点描述则解释了运算封闭性：$\sigma^d$ 保持加法、乘法与非零求逆，因而被它固定的元素也对这些运算封闭。一个任意的二进制子空间通常不具备这些额外封闭性。

这个描述还给出寻找子域的线性代数方法。设平方映射在基 $B$ 中的矩阵为 $S$，即

$$
[a^2]_B=S[a]_B.
$$

则当 $d\mid s$ 时，

$$
\{[a]_B:a\in E_d\}
=\ker(S^d-I).
$$

所以找子域元素可以转化为求一个二进制矩阵的核。

例如，$\mathbb F_{64}$ 的子域大小为

$$
2,\quad4,\quad8,\quad64,
$$

对应 $6$ 的正因子 $1,2,3,6$。它不含 $\mathbb F_{16}$，因为 $4\nmid6$。

## 选读三：让平方变成坐标循环移位——正规基

多项式基适合约化计算；若频繁使用平方，可以寻找另一种基：

$$
N=(\theta,\theta^2,\ldots,\theta^{2^{s-1}}).
$$

当这些 $s$ 个元素在 $\mathbb F_2$ 上线性无关时，它们组成一组**正规基**。有限域扩张的正规基定理保证可以找到这样的 $\theta$；这里采用其存在性结论。[^normal-basis]

若

$$
a=\sum_{i=0}^{s-1}u_i\theta^{2^i},
\qquad u_i\in\mathbb F_2,
$$

则

$$
a^2=\sum_{i=0}^{s-1}u_i\theta^{2^{i+1}}.
$$

每个基元素被平方后移到下一个位置，最后一个由 $\theta^{2^s}=\theta$ 回到开头。因此当 $s>1$ 时，

$$
\boxed{
[a^2]_N=(u_{s-1},u_0,\ldots,u_{s-2})^T
}.
$$

$s=1$ 时唯一的坐标保持不变。

在 $\mathbb F_4$ 中，前面使用的 $(\alpha,\alpha^2)$ 就是一组正规基，平方只需交换两位。这也解释了 S008 Remark 3.4 使用正规基说明 Frobenius 易于实现的思路。[^S008-basis]

选择正规基时，线性无关性是实质条件。本原元控制乘法阶，并不自动保证它的平方共轭组成基。

例如，在

$$
\mathbb F_8=\mathbb F_2[x]/(x^3+x+1)
$$

中，$\alpha=[x]$ 满足 $\alpha^3=\alpha+1$。非零乘法群的阶为素数 $7$，且 $\alpha\ne1$，所以 $\alpha$ 的阶为 $7$，是本原元。但

$$
\alpha^4=\alpha^2+\alpha,
$$

于是

$$
\alpha+\alpha^2+\alpha^4=0.
$$

因此 $(\alpha,\alpha^2,\alpha^4)$ 线性相关，不是正规基。

多项式基、迹对偶基、自对偶基与正规基各自服务于不同的计算：多项式基便于约化，对偶基给出坐标读数，自对偶性将迹配对化为点积，正规基将平方化为循环移位。具体选择可以改善不同操作的表示，但域中的加乘法始终是同一套算术。

## 来源

[^finite-fields]: Keith Conrad, *Finite Fields*, University of Connecticut 讲义。Theorem 1.1：不可约多项式商构造；Lemma 1.6：非零乘法群循环性；Theorem 2.2、Corollary 2.3：有限域与各次数不可约多项式的存在性；Theorem 2.7：同阶有限域同构；Theorem 2.8：子域分类；Theorem 4.6：有限域迹与范数。https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf

[^normal-basis]: J. S. Milne, *Fields and Galois Theory*, version 5.10, September 2022，Definition 5.17 与 Theorem 5.18，p.68：正规基及正规基定理。https://www.jmilne.org/math/CourseNotes/FT.pdf

[^circuits]: Mark Webster, Stergios Koutsioumpas and Dan E. Browne, *Heuristic and Optimal Synthesis of CNOT and Clifford Circuits*, arXiv:2503.14660v1。§§2.1–2.2：可逆二进制线性线路与高斯消元；§3.1：Clifford 的 Pauli 共轭条件。该文使用行标签与列消元，本文固定列坐标，相应使用行消元。https://arxiv.org/abs/2503.14660v1

[^S008-basis]: Anqi Gong, Christopher A. Pattison, Patrick Rall and Adam Wills, *Magic State Distillation via Codes over Binary Extension Fields*, S008，arXiv:2608.09727v1，85 页，印刷页码与 PDF 页序一致。[本地 PDF](../../Papers/S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf)。§2.2，pp.11–13：有限域、迹与范数；§3.1，pp.13–16：扩域寄存器与比特实现；p.15 式 (11)、脚注 8：基坐标、自对偶基与矩阵二元化的语境；pp.15–16 Remark 3.4：加法、固定非零常数乘法、未知输入乘法与 Frobenius。本文的一般同基乘法矩阵采用迹对偶公式；正规基的使用明确包含线性无关条件。

[^S008-phase]: S008，arXiv:2608.09727v1，§3.2.1，pp.16–17。[本地 PDF](../../Papers/S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf)。式 (12)–(13)：三寄存器迹相位及其比特展开；Claim 3.5、式 (14)–(15)：自对偶基中的 Hadamard 变换与乘法实现。本文由同一求和计算写出任意初始目标 $c$ 的完整可逆操作 $|x,y,c\rangle\mapsto|x,y,c+xy\rangle$。
```

END_FILE::88b1136de6724a67926c5ccbd1bfc2ed
END_RESPONSE::88b1136de6724a67926c5ccbd1bfc2ed
