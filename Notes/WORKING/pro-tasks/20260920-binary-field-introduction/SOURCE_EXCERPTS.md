# S008 机械来源摘取

原文：`Papers/S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf`

版本：arXiv:2608.09727v1；85 页；印刷页码 = PDF 页序。

PDF SHA-256：`af8d5cf4bb56206b9ac6aa50481476916bd26d8c914009e2c5f9e56f48961eae`

以下 PDF 文本逐页由 pypdf 提取，保留原始文本而未改写数学；上下标与分式可能线性化。PDF 字体映射产生的 C0 控制字符已逐字符转写为可见的 `\uXXXX`，未猜测其数学含义；相关公式对照所附译本及原 PDF。译本选段按当前 UTF-8 文件逐行复制。页 15–16 已由 Codex 渲染核对；图形请查看原 PDF/既有截图。此文件是任务来源材料，不是正式笔记。

## PDF page 1

```text
Magic State Distillation via Codes over Binary Extension Fields
Anqi Gong 1,3, Christopher A. Pattison 2, Patrick Rall 3, and Adam Wills 4,3
1ETH Zürich 2UC Berkeley 3IBM Quantum 4MIT
August 11, 2026
Abstract
Fault-tolerant quantum computation architectures are frequently bottlenecked by the overhead
of producing high-fidelity magic states. In this work, we use algebraic geometric techniques to
construct codes over binary extension fieldsF2s, thus discovering new protocols for the distillation
of qubit magic states, where our focus is on the regime of practical qubit-based quantum computing
architectures. To do this, we show that multi-qubit gates of interest such as CS, CCZ, and TOF# =
CCZ123CCZ345, can be packaged into simple gates over the larger fields, and we derive simple
algebraic conditions in the extension fields allowing the distillation of these gates. Because they are
derived from Galois qudits, the corresponding qubits codes naturally handle the correlated errors
present on such multi-qubit states. Moreover, the protocols we discover are extremely compact;
for example, we show that4CS states can be distilled to1CS state at distance2, using only4
logical qubits.
For a case study, we consider the distillation of CS and CCZ states from injectedTand CS
states. When optimized for magic state production per unit time, or logical spacetime volume,
we find that our protocols outperform the state-of-the-art in almost every situation, both at input
error rates10 −3 (direct injection), and10−6 (allowing some cultivation pre-injection).
Contents
1 Introduction 2
1.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Relation to Prior Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3.1 Catalogue of Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3.2 Spacetime Footprints for Distillation Tasks . . . . . . . . . . . . . . . . . . . . 4
1.4 Open Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.5 Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2 Preliminaries 10
2.1 Diagonal Gates in the Clifford hierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2 Introduction to rings, finite fields and Reed-Muller codes . . . . . . . . . . . . . . . . . 11
2.3 Affine and projective space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3 Galois Qudits over GF(2s)13
3.1 Galois Qudits and their Implementation in Qubits . . . . . . . . . . . . . . . . . . . . 13
3.2 Expansion of gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.1 Qudit-CCZ gate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.2 Control-Sgate in GF(4). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.2.3 The norm gate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.2.4 Classification of the diagonal Galois qudit Clifford hierarchy with real phases . 18
3.2.5U 7 gate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
1
arXiv:2608.09727v1  [quant-ph]  10 Aug 2026
```

## PDF page 2

```text
4 Distillation: transversality conditions and protocol constructions 24
4.1 Generalized triorthogonality on qubit codes and TOF#protocols . . . . . . . . . . . . 24
4.2 Qudit CCZ gate protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3U 7 gate protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.4 Norm gate protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.5 Qubit CS protocols fromF 4-linear codes . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5 Protocols from Algebraic Geometry Codes 37
5.1 Introduction to algebraic curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.1.1 Genus of a smooth plane curve . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.1.2 Curves over finite fields with many points . . . . . . . . . . . . . . . . . . . . . 38
5.2 Introduction to one-point codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.3 Qudit distillation protocols from punctured one-point codes . . . . . . . . . . . . . . . 43
5.4 Distillation without puncturing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.5 Protocols based on trace codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Acknowledgments 50
Appendix A Orthogonality condition for the CS gate 56
A.1 Method 1: Embedded code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
A.2 Method 2: Direct calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
A.3 Concatenated[[4,1,2]] 4 and decreasing monomial code . . . . . . . . . . . . . . . . . . 60
A.4 Optimality of asymptotic overhead two in d=2 CS-to-CS distillation . . . . . . . . . . 62
Appendix B Algebraic curves: definitions and applications 64
B.1 Advanced preliminaries / Formal Algebraic Geometry Code definitions . . . . . . . . . 64
B.2 Calculation of metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
B.2.1 Klein quartic codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
B.2.2 Elliptic curve codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
B.2.3 One-point codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
B.3 Multiplication in binary extension fields . . . . . . . . . . . . . . . . . . . . . . . . . . 70
Appendix C Building Distillation Circuits 72
C.1 Distillation protocols and Pauli-based computation (PBC) . . . . . . . . . . . . . . . . 72
C.1.1 Galois qudit gates as measurements . . . . . . . . . . . . . . . . . . . . . . . . 73
C.1.2 Realization of Distillation Protocols on Fewer Qudits . . . . . . . . . . . . . . . 75
Appendix D Time, Space, and Error Calculations 77
D.1 Time and Space Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
D.2 Error Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
D.3 Tables of Schemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
1 Introduction
1.1 Overview
Gate teleportation is a common way to achieve a universal quantum gateset. Most commonly, the
teleportedgateisinthethirdleveloftheCliffordhierarchy(termeda“third-levelgate”)wheretheinput
resource state is known as amagic state. The usual recipe for the preparation of magic states is to first
prepare encoded noisy magic states anddistillthem to high-fidelity magic states, which requires only
Clifford operations and measurements. In the standard procedure for magic state distillation [BK05;
BH12], a quantum error-detecting stabilizer code encodingkqubits intonqubits with a transversal
third-level gate can be used to construct a magic state distillation protocol by 1) preparing a codestate,
2) applying the noisy transversal third-level gateUusing input noisy magic states, 3) measuring the
syndrome of the code, and 4) outputting the unencoded state if the syndrome is trivial. If the action
2
```

## PDF page 3

```text
of the third-level gate is Clifford-equivalent to encodedV⊗k for some third-level gateV, then this
protocol turnsnnoisy magic states forUintokless-noisy magic states forV.
In this paper, we construct magic state distillation protocols leveraging algebraic geometry codes
over binary extension fields, with a focus on using novel theory to construct practical protocols. A
binary extension field is a finite field of size2s, denotedF 2s. A CSS code overF2s is also a CSS code
overF 2 [Wil26]. However, by working directly with the extension field, one is often able to construct
qubit codes with desirable properties that would have been very difficult to construct by working
directly over qubits. This intuition has been leveraged for magic state distillation before [WHY25;
GG25a; Ngu25; NP25], although this is the first time these techniques have been considered in a truly
practical setting. The main messages of this paper are as follows:
1. Multi-qubit gates of interest, including CS and CCZ, may be neatly packaged into gates for
single Galois qudits.1 It was previously unknown that such widely-considered multi-qubit gates
admitted such neat algebraic descriptions in the Galois qudit picture. With these descriptions,
we can prove conditions for Galois qudit codes to admit these gates transversally, thus allowing
their distillation.
2. Moving to codes over binary extension fields offers richer algebraic structures, allowing for better
code parameters than are possible than by working with the binary field directly, including in
the small-size regime of practicality, ultimately resulting in record-breaking protocols.
3. Working with Galois qudit codes allows us to naturally handle the multi-qubit errors present on
the corresponding multi-qubit states. This is the same intuition that has led to the wide-spread
use of codes over larger alphabets to handle burst errors in classical communication and storage.
4. Constructing codes with novel algebraic techniques often leads to the possibility of distilling
exotic magic states. If such an exotic magic state is called for in a particular algorithm, it will
often be more efficient to use a specialized magic state distillation protocol for that state, rather
than using generic schemes that distill states such as|T⟩, and synthesizing the gate.
Let us give some examples of the above points in our work. For point 1, in Section 4.5, we show that
the well-known two-qubit CS gate can be written into a natural form as a single-qudit gate overF4,
and that its transversality can be achieved using a simple three-orthogonality condition. Using the
Reed-Solomon code overF4, we use this to construct a protocol that distills4|CS⟩states into1|CS⟩
state at distance2, that can be run on4logical qubits. Moving to something slightly larger, by using
theF 8 Klein quartic algebraic curve, we show that24|CCZ⟩states can be distilled to4|CCZ⟩states
at distance3. For some context here, prior to this work, we are not aware of any way to perform magic
state distillation with rate1/6at distance3, let alone at such small sizes (outside of very pathological
and/or large-qudit magic states). There are several examples of such breakthroughs in our catalogue.
Note that, in the two examples mentioned above, the notion ofdistanceis the correct one for this
situation — that is — the distance is the minimum number of input magic states that must have
errors to cause an undetectable logical failure. Because multi-qubit states like|CS⟩and|CCZ⟩can
have correlated errors, this is the correct notion of distance, rather than the usual qubit distance of
a code; this is the content of point 3 above. For an example of a more exotic distillation protocol
as mentioned in point 4 above, we will show using theF4 Hermitian algebraic curve that8|CS⟩
states may be distilled into the5-qubit magic state for the TOF#gate, which is CCZ 123CCZ345.
This gate is Clifford-equivalent to a shared-controlled-SWAP, which is used in fermionic Hamiltonian
simulation [Bab+18], and other algorithmic subroutines [Chi+03]. We show our full catalogue of new
protocols in Section 1.3.1. Following that, in Section 1.3.2, we show that our novel protocols turn out
to be exceed the state-of-the-art in a very broad sense, when considering natural distillation tasks, as
well as sizes, states, and error rates relevant to realistic quantum computation architectures.
1Galois qudits are the quantum systems that encode finite extension fields likeF2s. Such a Galois qudit is equivalent
to a set ofsqubits [Wil26]. Throughout this work, when we refer to a qudit, it is left implicit that we simply mean a
Galois qudit, that is, a set of qubits. Moreover, whenever we refer to a quantum code for qudits, we mean a CSS code
overF 2s.
3
```

## PDF page 11

```text
the Clifford hierarchy is defined in [CH17] to be theminimumnumber ofTgates required to synthesize
the gate unitarily withTgates, CNOT gates, andSgates, and using no ancillas. The ancilla-freeT
count of CCZ is7. Such transformations can be discovered by manipulating phase polynomials. For
example, considering variablesxi ∈ {0,1}, one verifies the identity
4x1x2x3 ≡x 1 +x 2 +x 3 −(x 1 ⊕x 2)−(x 1 ⊕x 3)−(x 2 ⊕x 3) + (x1 ⊕x 2 ⊕x 3),(4)
where+denotes regular integer addition, and⊕denotes integer addition modulo2. 6 It follows from
this identity that the CCZ state (or gate) can be unitarily synthesized using7Tgates, as well as
CNOT operations, by considering variousUm,a gates withn= 3andm= 3. Becausem >1, we must
differentiate between regular integer addition and addition modulo2. Explicitly, we have
exp
\u00122πi
2m (x1 +x 2)
\u0013
̸= exp
\u00122πi
2m (x1 ⊕x 2)
\u0013
form >1.(5)
This is unlike when we consider products of CCZ gates like the TOF#gate, in which case addition
in the phase polynomial is both regular integer addition and modulo2addition. For example, for the
TOF#gate, exp (πi(x1x2x3 +x 3x4x5)) = exp (πi(x1x2x3 ⊕x 3x4x5)).(6)
It is also found in [CH17] that the ancilla-freeTcount of the TOF#gate mentioned above is11.
We note that this is less than twice the ancilla-freeTcount of twice that of CCZ, showing that it is
more efficient to directly synthesize TOF#than to synthesize two CCZ gates separately, at least in
this setting. Synthillation techniques [CH17] also allow one to distill12Tgates to1TOF#gate at
distance2(see App.C for the explicit example).
Hadamard gates and measurement-and-feedback add more power over merely using CNOT+T.
The most famous example is Jones’ construction of a CCZ gate from fourTgates [Jon13a]. An
interpretation [Bev+20] is that, applyingHSH=
√
Xon the third qubit on the|CCZ CS 1,2⟩=
CCZ CS12|+++⟩state (can be unitarily synthesized using CNOTs and fourT) leads to the|CCZ⟩
state [Bev+20, Fig. 12(b)], which can be further teleported to realize a CCZgate. As another example,
while unitary synthesis of a CCZ gate (using CNOT+CS) requires3CS gates, only2CS gates are
required for the|CCZ⟩state [Bev+20, Fig. 13].
2.2 Introduction to rings, finite fields and Reed-Muller codes
We now give a brief introduction to rings and finite fields. The following definitions and facts can be
found in many textbooks such as [LN96]; we thus state the most relevant ones without proof.
Aringis a setRequipped with two binary operations+(addition) and·(multiplication) such
that:Ris an abelian group with respect to+;·is associative, that is,(a·b)·c=a·(b·c),∀a, b, c∈R;
multiplication is distributive over addition,a·(b+c) =a·b+a·cand(b+c)·a=b·a+c·a. In
this work, we only work with commutative rings (those for whicha·b=b·afor alla, b∈R) with a
(multiplicative) identity (those containing an element called1satisfying1·a=afor alla∈R).
Given a positive integernandr∈R, we writenrfor the element ofRobtained by summingr n
times. If, for a ringR, there exists a positive integernsuch thatnr= 0for everyr∈R, then the
least such positive integernis called thecharacteristicofR.
In a ring, multiplicative inverses are not required to exist. A ring in which every nonzero element
has a multiplicative inverse is called afield. A subset of fields are integral domains, which are integral
domains. These are rings in which there are no zero divisors, meaning that ifab= 0, thena= 0
orb= 0. Given an integral domainR, one may construct a field from it called its fraction field,
Frac(R), which contains a copy ofR. The elements of the fraction field are the equivalence classes
ofR×(R\ {0}), under the equivalence relation(a, b)∼(c, d)⇐ ⇒ad=bc. Canonically, the
equivalence class of(a, b)is denoted a
b, and the operations of addition and multiplication are defined
via a
b + c
d = ad+bc
bc , and a
b · c
d = ac
bd.
An example of a field isFp ={0,1, . . . , p−1}for a primep, where the operations are achieved by
arithmetic modulop. More generally, a finite field (also known as a Galois field)Kmust haveq=ps
elements for somes∈N, where the primep:=charKis the characteristic ofK, andsis theextension
6The minimality of the various ancilla-freeTcounts is established by a relation to the decoding of a Reed-Muller
code [AM19].
11
```

## PDF page 12

```text
degreeofKoverF p. For all primespands∈N,F ps exists and it is unique up to isomorphism. It is
canonical to denote the correspondingKasF q or alternatively GF(q). Themultiplicative groupF ×
q
of nonzero elements ofFq is cyclic, meaning that there exists at least oneprimitive elementαsuch
thatF q ={0, α, α 2, . . . , αq−1 = 1}. Since any power of1is1itself, one hasγ q−1 =
(
1γ∈K ×
0γ= 0 , and
hence alsoγ q =γ,∀γ∈F q.qis called theorderof the finite fieldF q.
A subsetFofKthat is itself a field is called asubfieldofK, andKis called anextension fieldof
F. It turns out that everysubfieldofF ps′ has orderp s, wheresis a positive integer dividings ′. Let
q=p s andm=s ′/sin the following.
A field isomorphism is a bijective map from one field to another that preserves multiplication and
addition. A field automorphism on a fieldKis a field isomorphism fromKto itself. The group of
automorphisms ofF qm that fix every element ofFq (q=p s) is also referred to as theGalois groupof
Fqm overF q, and it is generated cyclically by theFrobenius transformσ1 :α7→α q (α∈F qm). To be
more explicit, we can write the elements of the Galois group as the mappingsσ0, σ1, . . . , σm−1 defined
byσ j(α) =α qj
forα∈F qm. The imagesσj(α)are called the Galoisconjugatesofα. Note that indeed
σj(γ) =γforγ∈F q.
Thetracetr Fqm /Fq(α)ofα∈F qm is the sum of the conjugates ofα, i.e.,
trFqm /Fq(α) =α+α q +α q2
+· · ·+α qm−1
.(7)
The trace maps intoFq surjectively. The trace function trFqm /Fq isF q-linear,
trFqm /Fq(γ1α1 +γ 2α2) =γ 1trFqm /Fq(α1) +γ 2trFqm /Fq(α2),∀γ 1, γ2 ∈F q and∀α 1, α2 ∈F qm ,(8)
where the additivity follows from the fact that(a+b)p =a p +b p (and hence(a+b) pi
=a pi
+b pi
) for
a, b∈F ps since
\u0000p
i
\u0001
= p!
i!(p−i)! ≡0 modpfori= 1,2. . . , p−1. We have tr Fqm /Fq(αq) =tr Fqm /Fq(α).
A further, less trivial fact, is that trFqm /Fq(α) = 0if and only ifα=β q −βfor someβ∈F qm.
ThenormNm Fqm /Fq ofαis the product of of all its conjugates:
NmFqm /Fq(α) =α·α q · · · · ·α qm−1
=α (qm−1)/(q−1) .(9)
The norm function is multiplicative: NmFqm /Fq(αβ) =Nm Fqm /Fq(α)NmFqm /Fq(β),∀α, β∈F qm. As
for the trace, NmFqm /Fq(αq) =Nm Fqm /Fq(α), and the norm function maps intoFq surjectively.
For a general ring (not necessarily a field), an idealIof a ringRis a subset ofRthat is itself a ring
and, moreover,∀a∈Iandr∈Rwe havear=ra∈I. We will only be working with finitely generated
ideals. Such ideals are formed by considering{a1, . . . , ak}a subset ofR, and the ideal generated by
them is(a 1, . . . , ak) :={a 1r1 +. . . a krk | ∀r 1, . . . , rk ∈R}. We will sometimes use⟨a 1, . . . , ak⟩to
denote the ideal generated by{a1, . . . , ak}.
R/Iis thequotient ringofRby the idealI. Its addition and multiplication are given by(r+
I) + (s+I) = (r+s) +I,(r+I)·(s+I) =rs+I. In the quotient ring whenI=⟨a 1, . . . , ak⟩, it is
convenient to writeR/I=R/(a 1, . . . , ak). In this quotient ring, one can identifya1 = 0, . . . , ak = 0.
In coding theory, e.g., when defining the Reed-Muller codes, we will frequently deal withpolynomial
ringsand their quotient rings. Lettingxbe an indeterminate variable, the polynomial ringR[x]is
the set of formal sumsanxn +· · ·+a 1x+a 0 under usual addition and multiplication. Multivariate
polynomial rings are defined inductively byR[x1, x2, . . . , xn] :=R[x 1, x2, . . . , xn−1][xn]. In the case
thatR=Kfor some fieldKof characteristicp, we have thatptimes anything equals zero.
To define Reed-Muller codes, we consider the quotient ring
Fq[x1, . . . , xm]/(xq
1 −x 1, . . . , xq
m −x m), q= 2 s.
The following definitions and facts about Reed-Muller codes may be found in [MS77]. Theq-ary Reed-
Muller code inmvariables of degreeris denotedRM q(r, m), and is the length-qm code overFq formed
by evaluating all polynomials in the above ring of degree at mostrat all points(x1, x2, . . . , xm)∈F m
q .
Becauseη q =ηfor allη∈F q, quotienting by the terms(x q
i −x i)in the above ring allows us to
identify the given polynomials with the corresponding codewords of the Reed-Muller code in a one-
to-one fashion. For example, note that the degree of any individual variable in any polynomial in the
quotient ring does not exceedq−1.
For Reed-Muller codes, a particularly important example for us will be the binary Reed-Muller
12
```

## PDF page 13

```text
code withq= 2, defined over the quotient ring
F2[x1, . . . , xm]/(x2
1 −x 1, . . . , x2
m −x m).
The distance of RM2(r, m)turns out to be2m−r; indeed, one may quickly see that it must be at most
this by considering the degree-rpolynomialx 1x2 . . . xr, whose evaluation has weight2m−r. We may
denote byev(f)the codeword corresponding to the polynomialf. Then we have that the coordinate-
wise multiplication ofev(f)andev(g)isev(f g). More generally, one can see that the weight of a
codeword corresponding to the evaluation of a monomial formed from the product ofvvariables is
2m−v. The code dual to RM2(r, m)is RM2(m−r−1).
Analogous facts hold more generally forq-ary Reed-Muller codes. For example, the distance of
RMq(r, m)is(µ+ 1)q ν, if we write(q−1)m−r=ν(q−1) +µfor0≤µ < q−1. The coordinate-wise
multiplication ofev(f)andev(g)isev(f g)in the generalq-ary case, also.
More general codes, calledaffine monomial codes, can be considered by evaluating different sets
of polynomials (than those of degree at mostr) at the points ofF m
q . A key example for us will
be the hyperbolic codes. These can be obtained from Reed-Muller codes by deleting parity checks,
increasing the code dimension while keeping the same minimum distance [HLP98, Ch. 4.4]. Concretely,
a basis of the hyperbolic code of designed distancedis formed by the monomialsXα1
1 . . . Xαm
m whereQm
i=1(αi + 1)< d. A more general class of affine monomial codes will be considered in App. A.3.
2.3 Affine and projective space
Theaffine spaceover the fieldK, is simply the vector spaceKn overK; this is usually denotedAn
K or
justA n when the fieldKis implicit. We write all its elements asAn
K ={(x 1, . . . , xn)|x i ∈K}. The
projective spaceover a fieldK, denoted asPn
K, or justPn whenKis implicit, is defined by quotienting
Kn+1 by scalar multiplication by elements ofK× =K\{0}. Explicitly,
Pn = (K n+1\{0})/∼,
where the equivalence relation∼onK n+1 is defined as
(x0 :· · ·:x n)∼(λx 0 :· · ·:λx n)∀λ∈K ×.
TakeP 2
F4 as an example, one can enumerate all its elements in the following way:{(1 :y:z)|y, z∈
F4} ∪ {(0 : 1 :z)|z∈F 4} ∪ {(0 : 0 : 1)}.
LetU i ⊂P n be the subset of points(X0 :· · ·:X n)withX i ̸= 0. Then onUi the ratiosxj =X j/Xi
are well-defined and give a bijectionUi ∼= An. Notice thatU0, . . . , Un together coverPn. We will later
refer toU i as theX i = 1affine chart coveringP n.
A homogeneous polynomial is a polynomial for which all terms have a common degree. An example
would be f h(x0, x1, x2) =x 2
0x1x2 +x 3
1x2,
which is a homogeneous polynomial of degree4. Notice that ifFis a homogeneous polynomial of
degreedthen f h(λx0, λx1, . . . , λxn) =λ d ·f h(x0, x1, . . . , xn).(10)
Such functions are not in general well-defined functions onPn, but what is well-defined, because of
Eq. (10), is the zero locus of such functions. The zero locus ofFis
V(F) :={(x 0 :· · ·:x n)∈P n :f h(x0, x1, . . . , xn) = 0}.
Clearly, given any polynomial on the affine spaceA n, the polynomial is a genuinely well-defined
function onA n, and it always makes sense to talk about the zero locus. Later, we will use capitalized
variables likeX, Y, Zto emphasize that they are variables taking values in a projective space, see for
example Construction 4.10, but lower-case variables likex, yto emphasize that they take values in
affine space, see for example Construction 4.11.
3 Galois Qudits over GF(2s)
3.1 Galois Qudits and their Implementation in Qubits
A Galois qudit over the finite field GF(2s) =F 2s is a2 s-dimensional qudit with a choice of Pauli
group deliberately made to encode the arithmetic of the finite fieldF2s. In making this choice, the
13
```

## PDF page 14

```text
2s-dimensional qudit is made equivalent to a set ofsqubits in its states, Pauli group and Clifford hier-
archy [Got24; Wil26]. Building quantum codes for Galois qudits over GF(2s)with desirable properties
often allows one to build qubit codes with similarly desirable properties [WHY25; GG25a; Ngu25;
NP25; He+25c; He+25b]. In particular, by constructing qudit codes over GF(2s)with transversal
third-level gates, we can construct distillation protocols for qubit magic states that only require qubit
Clifford operations [WHY25; NP25] to execute on qubits. Thus, we study qubit magic state distillation
protocols by constructing and analyzing quantum codes overF2s.
The mapping between the2s-dimensional Galois qudit and the set ofsqubits goes via a “qudit-
to-qubit mapping”, for which all the details are laid out in [Wil26]. In particular, isomorphisms may
be constructed for the states of the two systems, CSS codes on them, as well as the levels of the
Clifford hierarchy, which specialises to diagonal gates in each level of the Clifford hierarchy. All of
these isomorphisms are compatible with each other in the natural ways. Accordingly, by constructing
distillation protocols for Galois qudits, we obtain distillation protocols for qubits. We make this part
of the transformation explicit shortly.
Throughout, we specify distillation protocols via CSS codes, where the CSS codes are specified by
matrices in a way that is now standard [BH12], where the rows of the given matrix specify theX-
logical operators in its firstkrows, and its remaining rows specifyXstabilizer generators. This is an
important enough notion for us that we give it a name here. One may see [Wil26] for the construction
of Galois qudit CSS codes from spaces ofXandZstabilizers/logical operators. In what follows, two
vectorsx, y∈F n
q are said to beorthogonalif⟨x, y⟩ ≡ P
i xiyi = 0.
Definition 3.1(X-generator matrix).AnX-generator matrix for a quantum CSS code is some matrix
G∈F m×n
q , with an associated positive integer1≤k≤m. We require thatGis full rank overF q.
This matrix defines a quantum CSS code where the firstkrows are non-trivial logicalXoperators
(referred to as logical rows), and the remaining rows areXstabilizer generators. Formally, letGbe
theF q-vector space generated by the rows ofG, andG0 be theF q-vector space generated by the latter
m−krows ofG. The CSS code hasXstabilizers given by the spaceG 0 andZstabilizers given by the
spaceG ⊥.
It is straightforward to compute code properties from theX-generator matrix.
Proposition 3.2.LetG∈F m×n
q be anX-generator matrix for a quantum CSS code overFq withk
logical rows. The quantum CSS code hasklogical qudits andnphysical qudits. ItsZ-distance is equal
to the minimum Hamming weight of a nonzero vector inFn
q orthogonal to all of the latterm−krows
ofG, but not orthogonal to at least one of the firstkrows ofG.
Proof.In the notation of Definition 3.1, the number of logical qudits of the corresponding CSS code
isdim Fq G −dim Fq G0 =m−(m−k) =k, where the first equality follows from the requirement that
Gis full rank. TheZdistance is then the minimum Hamming weight of an element ofG⊥
0 \ G ⊥. By
linearity, a vectorz∈F n
q is inG ⊥
0 \ G⊥ if and only if it is orthogonal to every row ofG0, but not every
row ofG.
For distilling magic states of diagonal gates, only theZ-distance is relevant, since one can twirl
the magic states [BK05; BH12].
Proposition 3.3(Generalization of [BK05; BH12] twirling).LetUbe a diagonal third-levels-qubit
operator. Fora∈F s
2, define the operatorsM a ≡U X aU † and states|A a⟩ ≡Z aU|+⟩ s. Then, for
any state,ρ, its twirl with respect to(M a)a∈F2 picked uniformly at random is 1
2s
P
a∈Fs
2
MaρM †
a =P
a∈Fs
2
ρa |Aa⟩ ⟨Aa|A a whereρ a ≡ ⟨A a|ρ|A a⟩.
Proof.First, note that⟨A a|A b⟩=⟨+| s Za+b |+⟩s =δ ab, so the states(|Aa⟩)a∈Fs
2 form an orthonormal
basis. Additionally, they are eigenvectors of the operators(M a)a∈F2 with eigenvaluesM a |Ab⟩=
U XaU †ZbU|+⟩ s = (−1) a·b |Ab⟩. For an arbitrary density matrix, we can expand it in the basis
ρ= P
a,b∈F2 ρab|Aa⟩⟨Ab|, whereρab =⟨A a|ρ|A b⟩. Afterpassingthisstatethroughthetwirlingchannel,
14
```

## PDF page 15

```text
we get
1
2s
X
a∈Fs
2
MaρM †
a = 1
2s
X
c∈Fs
2
X
a,b∈Fs
2
ρabMc|Aa⟩⟨Ab|M †
c
= 1
2s
X
c∈Fs
2
X
a,b∈Fs
2
ρab(−1)c·(a+b)|Aa⟩⟨Ab|
=
X
a∈Fs
2
ρaa|Aa⟩⟨Aa|
Typically, we will refer to the rows ofGasg1, . . . ,gm, and thej-th entry of thei-th row asg ij.
We will usually think ofGas a generator matrix for a classical code, i.e., the rows ofGform a basis
for the code. We restrict ourselves toF2s-linear codes, i.e., ifg1,g 2 ∈F n
2s are codewords, then so is
γ1g1 +γ 2g2 for allγ 1, γ2 ∈F 2s.
IfGis a binary matrix, one immediately has a quantum CSS code for qubits. Ifs >1, then we
may binarize the matrixGas follows to produce a qubit code.7 Consider some basisB= (α i)s
i=1 for
F2s overF 2, i.e., everyγ∈F 2s can be written uniquely asγ= Ps
i=1 biαi forb i ∈F 2,i= 1, . . . , n.
The generator matrixG∈F m×n
2s may be expanded into a binary matrix inFms×ns
2 , simply by taking
any entryγofGand replacing it with anF s×s
2 matrix whose(i, j)-th entry is tr(γαiαj)[MS77] 8. The
resultant binary matrix specifies a qubit CSS code with its firstksrows being logicalXoperators and
its latter(m−k)srows beingXstabilizer generators.
One may use different basesBfor the mapping of qudits to qubits. This yields different isomor-
phisms between the qudits and qubits. Changing the basisBused in the mapping is equivalent to
performing a CNOT circuit on thesqubits making up the qudit. A particularly convenient choice
of basis is aself-dual basis, one for which tr(αiαj) =δ ij. Such a basis exists for alls, and can be
found in polynomial time using Lempel factorization [SL80]. It is particularly convenient to extract
the components of a field element in a self-dual basis:
F2s ∋γ=
sX
i=1
biαi, b i =tr(γα i)∈F 2 .(11)
Using this expression and the phase polynomial language, we can build up the connection between
qudit and qubit diagonal gates. In the rest of this section, we will study particular qudit gates,
including the qudit-CCZ gates acting on three qudits, as well as single qudit gates that include CS
(specifically overF 4), norm gates andU 7 gates for arbitrary binary extension fields. These are all
non-Clifford gates. The aim is therefore to construct qudit codes, encoded in matricesG∈F m×n
2s ,
having these gates transversal, in order to distill their magic states. This immediately gives us qubit
protocols distilling the equivalent of these gates under the qudit-to-qubit mapping.
Before proceeding, however, let us state some simple observations about the Clifford hierarchy for
Galois qudits of dimension2 s (regardless of the extension degrees). We focus particularly on the
operations that perform arithmetic overF2s, for which we note that the level of the Clifford hierarchy
are very different to arithmetic overZ, originating from the fact that addition does not cause “carrying”
inF 2s.
Remark 3.4.Clifford hierarchy of arithmetic operations in binary extension fields.
1. In-place addition overF2s, that is,|x⟩ |y⟩ 7→ |x⟩ |x+y⟩forx, y∈F 2s, is a Clifford operation.
2. Multiplying an element inF2s by a known constantβ∈F ×
2s is a Clifford operation. This can be
also seen as a change of basis, i.e., from(αi)s
i=1 to(βα i)s
i=1. There are many more changes of
basis than these, however, and they are all Clifford.
3. Multiplication of two unknown elementsx, y∈F 2s, that is,|x⟩ |y⟩ |0⟩ 7→ |x⟩ |y⟩ |xy⟩, is in the
third level of the Clifford hierarchy. We will see this explicitly in subsection 3.2.1.
7It is equivalent to construct a qudit code from the matrix overF2s, and binarize the code itself [Wil26].
8One can think of thisγ7→(tr(γα iαj))s
i,j=1 mapping as multiplying each codeword of theF2s-linear code byαi and
then subsequently binarizing each entry; see [Wil26] for more details on mapping qudit codes to qubit codes.
15
```

## PDF page 16

```text
4. The in-place Frobenius transform|γ⟩ 7→ |γ2⟩is a Clifford operation. A way to see this is to expand
in the normal basis9 αi =α 2i
for some primitive elementαofF 2s. Writingγ= Ps
i=1 biαi, we
haveγ 2 = (Ps
i=1 biαi)2 =Ps
i=1 b2
i α2
i =Ps
i=1 biαi+1 (mods+1) , and so the Frobenius transform is
just cyclically shifting thesqubits making up the qudit (with this basisB), which is Clifford.10
3.2 Expansion of gates
3.2.1 Qudit-CCZ gate
As mentioned, gates on GF(2s)qudits can be expanded into qubit gates as well, where diagonal gates
are mapped to diagonal gates, and they retain their level in the Clifford hierarchy. Let us examine
this further. Full details can be found in [Wil26], but we give the idea here as well. Let us start with
the example of the three-qudit CCZ gate [GG25a; Ngu25], defined as follows forx, y, z∈GF(2s):
CCZ:|x⟩|y⟩|z⟩ 7→(−1) tr(xyz) |x⟩|y⟩|z⟩(12)
For simplicity, letB= (α i)s
i=1 be a self-dual basis forFq overF 2. To expand the gate, first expand
x, y, zintheself-dualbasis:x= Ps
i=1 xiαi,y= Ps
i=1 yiαi, andz= Ps
i=1 ziαi, wherexi, yi, zi ∈ {0,1}.
The computational basis states|x⟩ |y⟩ |z⟩on3qudits can be expanded to computational basis states
on3squbits by writingx, y, zout in their components. Next, using the fact that tr(·)isF 2-linear:
tr(xyz) =tr


sX
i,j,k=1
xiyjzk αiαjαk

 =
sX
i,j,k=1
xiyjzktr(αiαjαk).(13)
When we expand CCZ to a3s-qubit gate, it gives a phase tr(xyz) =Ps
i,j,k=1 xiyjzktr(αiαjαk)to the
computational basis state|x⟩ |y⟩ |z⟩. Therefore, at the qubit level, this qudit CCZ gate applies a qubit
CCZ to every triplet(xi, yj, zk)for which tr(αiαjαk) = 1.
Let us show an explicit example of the qudit CCZ gate forF4 ={0,1, ω, ω 2}, where arithmetic in
this field is specified byω+ω 2 = 1. One can check that(ω, ω2)forms a self-dual basis. The left side
of figure 4 denotes the example of theF4-qudit CCZ gate expanded in this basis. Claim 3.5 shows
that the qudit CCZ gate can be used to coherently multiply elements in the fieldFq on a quantum
computer.
(a) (b)
Figure 4: (a)F 4-qudit CCZ expanded as qubit CCZs. Expandx=x 1ω+x 2ω2, wherex 1, x2 ∈F 2,
and similarly fory, z. (b) The magic state corresponding toF 4-CCZ can be consumed to perform
multiplication inF 4 – one just needs to conjugate the third pair of qubits by Hadamard gates.
Claim 3.5.TheF 2s-qudit CCZ gate allows one to multiply two elements in that field on a quan-
tum computer. That is, one use of a CCZ gate, and Clifford operations, is sufficient to perform the
arithmetic operation|x⟩ |y⟩ |0⟩ 7→ |x⟩ |y⟩ |xy⟩, wherex, y∈F 2s, and each ket is ans-qubit register
(equivalently, a one2s-dimensional qudit register. Fig. 4(b) shows an example forF4.
Proof.We will show that the following sequence of operations executes the desired operation on the
3-qudit state|x⟩ |y⟩ |0⟩:
9A normal basis ofF qm overF q, which is a basis of the form{α, αq, . . . , αqm−1
}, always exists, see e.g. [LN96,
Thm. 2.35]. As we commented before, forF2s overF 2, a self-dual basis always exists; however, a self-dual normal basis
exists if and only ifsis not divisible by4. [MP13]
10Recall that picking a different basisBforF q overF 2 yields different isomorphisms from qudits to qubits, however
each give valid isomorphisms of the diagonal gates in each level of the Clifford hierarchy. Thus, we may choose a
particular basisB, establish the level of the corresponding qubit gate, and conclude the level of the initial qudit gate.
16
```

## PDF page 17

```text
1. Perform Hadamard on every qubit making up the third register, which all begin in the|0⟩state;
2. Perform the qudit CCZ gate on the three qudits (3squbits);11
3. Perform Hadamard again on allsqubits making up the last register.
A fact we will be using is that
H ⊗s |z⟩= 1√
2s
X
t∈F2s
(−1)tr(zt) |t⟩.(14)
Here,|z⟩denotes the qudit computational basis state corresponding toz∈Fq, butH ⊗s corresponds to
performing the qubit Hadamard operation on thesqubits making up the qudit. To see this equation,
consider expandingz∈F 2s in a self-dual basis(α i)s
i=1 asz=z 1α1 +· · ·+z sαs; one also expands
t∈F 2s ast=t 1α1 +. . . , t sαs:z i, ti ∈ {0,1}. Then,H ⊗s |z⟩is a uniform superposition over|T⟩with
phase(−1) z1t1+···+zsts. This exponent is exactly
tr(zt) =tr

(
X
i
ziαi) (
X
j
tjαj)

 =
X
i,j
zitjtr(αiαj) =
X
i
ziti .
The desired circuit is then performed as follows:
|x⟩|y⟩|0s⟩ H ⊗s onz− − − − − − → |x⟩|y⟩1√
2s
X
z∈F2s
|z⟩
Qudit CCZ
− − − − − − − →1√
2s
X
z
(−1)tr(xyz) |x⟩|y⟩|z⟩.(15)
ApplyH ⊗s again on thez-register:
H ⊗s
 
1√
2s
X
z
(−1)tr(xyz) |z⟩
!
= 1√
2s
X
z
(−1)tr(xyz)
 
1√
2s
X
t
(−1)tr(zt)|t⟩
!
= 1
2s
X
t
 X
z
(−1)tr
\u0000
z(xy+t)
\u0001!
|t⟩
=|xy⟩,
where in the last step, we have used
X
z∈F2s
(−1)tr(zu) =
(
2s,ifu= 0,
0,ifu̸= 0.
This multiplication in the binary extension field finds usage in, for example, decoded quantum
interferometry [Jor+25]. In particular, [Kha+25] provides a detailed resource analysis for solving
the optimal polynomial intersection problem in binary extension fields. The binary extension field
multiplication might also be useful in preparing certain catalyst states [Kim25].
Later, we will only present qudit-CCZ distillation protocols (Table 3) up toF64. For multiplication
in larger binary extension fields, e.g.,F2163, one can reduce the problem into many multiplications in
small binary extension fields by paying with some additional CNOT gates [CC88; CÖ10]. We present
an example of this reduction in App. B.3, after introducing relevant concepts for algebraic curves in
Sec. 5.2 and App. B.1.
Note that, as a consequence of remark 3.4, the qudit CCZ gates CCZβ1 and CCZβ2 are Clifford
equivalent for anyβ1, β2 ∈F ×
2s, where
CCZβ|η1⟩|η2⟩|η3⟩= (−1) tr(βη1η2η3)|η1⟩|η2⟩|η3⟩.(16)
This is because an equivalent way of doing CCZβ1 is to perform multiplication on the first qudit12
|η1⟩ 7→ | β2
β1
η1⟩before applying CCZ β2. This fact will later play a role in Sec. 5.3 when we distill
qudit-CCZ gates.
11This step can also be performed by consuming a|CCZ⟩state, and using Clifford operations.
12In fact, any of the three qudits work.
17
```

## 当前译本 lines 1–34

# 通过二元扩域上的码实现魔法态蒸馏

## 译文信息

- 文献 ID：S008
- 原文：[S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf](../Papers/S008_2026_Gong_magic_state_distillation_binary_extension_fields.pdf)
- 原文版本：arXiv:2608.09727v1 [quant-ph]（提交于 2026-08-10；论文题头日期为 2026-08-11）
- 翻译类型：全文翻译
- 覆盖范围：所登记 PDF 的全部 85 页，包括题名、作者、单位、摘要、目录、正文第 1–5 节、脚注、全部公式与编号、图表说明及必要图内文字、致谢、参考文献、附录 A–D；不含单独的 supplementary material、ancillary files、网页附加内容或其他版本
- 印刷页码：有；1–85
- PDF 页序：从 1 开始；1–85
- 页码对应关系：印刷页码与 PDF 页序一一对应，即印刷页码 $p$ = PDF 页序 $p$
- 状态：已核对
- 待核对项：无

| 原文章节 | 印刷页码 | PDF 页序 | 状态 | 待核对 |
|---|---:|---:|---|---|
| Title, Authors, Affiliations, Abstract, Contents | 1–2 | 1–2 | 已核对 | 无 |
| 1 Introduction | 2–9 | 2–9 | 已核对 | 无 |
| 1.1 Overview | 2–4 | 2–4 | 已核对 | 无 |
| 1.2 Relation to Prior Work | 4 | 4 | 已核对 | 无 |
| 1.3 Results | 4–8 | 4–8 | 已核对 | 无 |
| 1.3.1 Catalogue of Protocols | 4 | 4 | 已核对 | 无 |
| 1.3.2 Spacetime Footprints for Distillation Tasks | 4–8 | 4–8 | 已核对 | 无 |
| 1.4 Open Questions | 8–9 | 8–9 | 已核对 | 无 |
| 1.5 Organization | 9 | 9 | 已核对 | 无 |
| 2 Preliminaries | 10–13 | 10–13 | 已核对 | 无 |
| 2.1 Diagonal Gates in the Clifford hierarchy | 10–11 | 10–11 | 已核对 | 无 |
| 2.2 Introduction to rings, finite fields and Reed-Muller codes | 11–13 | 11–13 | 已核对 | 无 |
| 2.3 Affine and projective space | 13 | 13 | 已核对 | 无 |
| 3 Galois Qudits over GF($2^s$) | 13–24 | 13–24 | 已核对 | 无 |
| 3.1 Galois Qudits and their Implementation in Qubits | 13–16 | 13–16 | 已核对 | 无 |
| 3.2 Expansion of gates | 16–24 | 16–24 | 已核对 | 无 |
| 3.2.1 Qudit-CCZ gate | 16–18 | 16–18 | 已核对 | 无 |

## 当前译本 lines 191–212

## 1 引言

### 1.1 概述

门传态是实现通用量子门集的一种常见方法。最常见的情形是，被传态的门位于 Clifford 层级的第三层（称为“第三层门”），此时输入资源态称为魔法态。制备魔法态的通常做法，是先制备带噪声的编码魔法态，再仅用 Clifford 操作和测量将其蒸馏成高保真魔法态。在标准的魔法态蒸馏流程 [BK05; BH12] 中，若一个量子检错稳定子码把 $k$ 个量子比特编码进 $n$ 个量子比特，并具有横向第三层门，则可以按如下步骤构造魔法态蒸馏协议：1）制备一个码态；2）利用输入的带噪魔法态施加带噪的横向第三层门 $U$；3）测量该码的综合征；4）若综合征平凡，则输出解编码后的态。如果该第三层门的作用与某个第三层门 $V$ 的编码作用 $V^{\otimes k}$ Clifford 等价，那么这一协议便把 $n$ 个用于 $U$ 的带噪魔法态转化为 $k$ 个用于 $V$、噪声更小的魔法态。

本文利用二元扩域上的代数几何码构造魔法态蒸馏协议，重点在于以新理论构造实际可用的协议。二元扩域是大小为 $2^s$ 的有限域，记作 $\mathbb F_{2^s}$。$\mathbb F_{2^s}$ 上的 CSS 码同时也是 $\mathbb F_2$ 上的 CSS 码 [Wil26]。然而，直接在扩域上工作，往往可以构造出具有理想性质的量子比特码，而直接以量子比特为对象构造这样的码会非常困难。这一直觉此前已被用于魔法态蒸馏 [WHY25; GG25a; Ngu25; NP25]，但这些技术在真正实际的设定中得到考察，本文尚属首次。本文的主要信息如下：

1. CS 和 CCZ 等重要多量子比特门可以简洁地封装成单个伽罗瓦 qudit 上的门。[^1] 此前尚不清楚，这些受到广泛研究的多量子比特门在伽罗瓦 qudit 图景中竟能具有如此简洁的代数描述。有了这些描述，我们便能证明伽罗瓦 qudit 码横向容许这些门的条件，从而蒸馏相应的态。

2. 转向二元扩域上的码会带来更丰富的代数结构，因而能够取得优于直接在二元域上工作的码参数；即使在具有实际意义的小规模区间也是如此，并最终产生破纪录的协议。

3. 使用伽罗瓦 qudit 码，使我们能够自然地处理相应多量子比特态中的多量子比特错误。这与经典通信和存储中广泛使用较大字母表上的码来处理突发错误，是同一个直觉。

4. 利用新颖代数技术构造码，往往也带来蒸馏奇异魔法态的可能。如果某个特定算法需要这样的奇异魔法态，那么为该态使用专门的魔法态蒸馏协议，通常会比使用蒸馏 $|T\rangle$ 等状态的通用方案再综合所需门更高效。

下面用本文中的一些例子说明这些要点。就第 1 点而言，我们在第 4.5 节证明，著名的双量子比特 CS 门可在 $\mathbb F_4$ 上写成一种自然的单 qudit 门形式，而一种简单的三正交条件即可实现它的横向性。利用 $\mathbb F_4$ 上的 Reed-Solomon 码，我们据此构造出一个协议：它以距离 2 将 4 个 $|\mathrm{CS}\rangle$ 态蒸馏成 1 个 $|\mathrm{CS}\rangle$ 态，并且只需在 4 个逻辑量子比特上运行。再考虑稍大的例子：利用 $\mathbb F_8$ Klein 四次代数曲线，我们证明，可以以距离 3 将 24 个 $|\mathrm{CCZ}\rangle$ 态蒸馏成 4 个 $|\mathrm{CCZ}\rangle$ 态。作为参照，在本工作之前，据我们所知，人们尚无任何办法以距离 3 和 $1/6$ 的产率进行魔法态蒸馏，更不用说在如此小的规模下做到这一点了（极为病态和／或高维 qudit 的魔法态除外）。我们的协议目录中还有若干类似的突破。

请注意，在上述两个例子中，“距离”正是适用于此情形的概念——也就是说，距离是导致不可检测逻辑错误所需的最少带错输入魔法态数。由于 $|\mathrm{CS}\rangle$ 和 $|\mathrm{CCZ}\rangle$ 等多量子比特态可能带有关联错误，因此正确的距离概念应当是这个，而不是码通常的量子比特距离；这正是上述第 3 点的内容。至于第 4 点所说的更奇异的蒸馏协议，我们将利用 $\mathbb F_4$ Hermitian 代数曲线证明，可以把 8 个 $|\mathrm{CS}\rangle$ 态蒸馏成 $\mathrm{TOF}\#$ 门的五量子比特魔法态，其中 $\mathrm{TOF}\#=\mathrm{CCZ}_{123}\mathrm{CCZ}_{345}$。该门与共享控制-SWAP Clifford 等价；后者用于费米子哈密顿量模拟 [Bab+18] 和其他算法子程序 [Chi+03]。第 1.3.1 节给出我们新的协议目录。随后，第 1.3.2 节表明，在考虑自然的蒸馏任务以及与现实量子计算架构相关的规模、状态和错误率时，我们的新协议在非常广泛的意义上都优于当前最佳方案。

[^1]: 伽罗瓦 qudit 是对 $\mathbb F_{2^s}$ 这类有限扩域进行编码的量子系统。一个这样的伽罗瓦 qudit 等价于一组 $s$ 个量子比特 [Wil26]。全文中提到 qudit 时，我们默认只指伽罗瓦 qudit，也就是一组量子比特。此外，每当提到 qudit 的量子码时，我们所指的都是 $\mathbb F_{2^s}$ 上的 CSS 码。


## 当前译本 lines 505–682

### 2.2 环、有限域与 Reed-Muller 码简介

下面简要介绍环与有限域。以下定义和事实可见于 [LN96] 等许多教材，因此这里只陈述最相关的内容而不证明。

**环**是一个集合 $R$，配备两个二元运算 $+$（加法）和 $\cdot$（乘法），并满足：$R$ 关于 $+$ 构成阿贝尔群；$\cdot$ 满足结合律，即对所有 $a,b,c\in R$，有 $(a\cdot b)\cdot c=a\cdot(b\cdot c)$；乘法对加法满足分配律，即 $a\cdot(b+c)=a\cdot b+a\cdot c$ 且 $(b+c)\cdot a=b\cdot a+c\cdot a$。本工作只考虑交换环（即对所有 $a,b\in R$ 都有 $a\cdot b=b\cdot a$）以及带有乘法单位元的环（即包含一个称为 $1$ 的元素，对所有 $a\in R$ 都有 $1\cdot a=a$）。

给定正整数 $n$ 和 $r\in R$，用 $nr$ 表示在 $R$ 中把 $r$ 相加 $n$ 次所得的元素。如果对环 $R$ 存在一个正整数 $n$，使得每个 $r\in R$ 都满足 $nr=0$，那么满足这一条件的最小正整数 $n$ 称为 $R$ 的**特征**。

环不要求乘法逆元存在。每个非零元素都存在乘法逆元的环称为**域**。域属于整环；**整环**是不存在零因子的环，也就是说，若 $ab=0$，则 $a=0$ 或 $b=0$。

> [!note] 译注
> 原文关于域与整环的句子出现重复且疑似笔误；这里按标准包含关系“域属于整环”翻译。

给定整环 $R$，可以从它构造一个称为**分式域**的域 $\operatorname{Frac}(R)$，其中包含 $R$ 的一个副本。分式域的元素是 $R\times(R\setminus\{0\})$ 在等价关系

$$
(a,b)\sim(c,d)\quad\Longleftrightarrow\quad ad=bc
$$

下的等价类。通常把 $(a,b)$ 的等价类记作 $a/b$；加法与乘法定义为

$$
\frac ab+\frac cd=\frac{ad+bc}{bc},
\qquad
\frac ab\cdot\frac cd=\frac{ac}{bd}.
$$

> [!note] 译注
> 上式加法分母按原文转写为 $bc$；标准分式加法的分母应为 $bd$，原文疑似有笔误。

域的一个例子是素数 $p$ 对应的 $\mathbb F_p=\{0,1,\ldots,p-1\}$，其中运算由模 $p$ 算术给出。更一般地，一个有限域（也称伽罗瓦域）$K$ 必须有 $q=p^s$ 个元素，其中素数 $p:=\operatorname{char}K$ 是 $K$ 的特征，$s$ 是 $K$ 相对于 $\mathbb F_p$ 的**扩张次数**。对所有素数 $p$ 和 $s\in\mathbb N$，$\mathbb F_{p^s}$ 都存在，而且在同构意义下唯一。通常把相应的 $K$ 记作 $\mathbb F_q$，也记作 $\mathrm{GF}(q)$。$\mathbb F_q$ 的非零元素所成的**乘法群** $\mathbb F_q^\times$ 是循环群，也就是说，至少存在一个**本原元** $\alpha$，使得

$$
\mathbb F_q=\{0,\alpha,\alpha^2,\ldots,\alpha^{q-1}=1\}.
$$

由于 $1$ 的任意次幂仍为 $1$，有

$$
\gamma^{q-1}=
\begin{cases}
1,&\gamma\in K^\times,\\
0,&\gamma=0,
\end{cases}
$$

从而对所有 $\gamma\in\mathbb F_q$ 都有 $\gamma^q=\gamma$。$q$ 称为有限域 $\mathbb F_q$ 的**阶**。

$K$ 中自身构成域的子集 $F$ 称为 $K$ 的**子域**，而 $K$ 称为 $F$ 的**扩域**。事实证明，$\mathbb F_{p^{s'}}$ 的每个子域的阶都是 $p^s$，其中正整数 $s$ 整除 $s'$。下文令 $q=p^s$、$m=s'/s$。

域同构是两个域之间保持乘法与加法的双射。域 $K$ 上的域自同构是从 $K$ 到自身的域同构。$\mathbb F_{q^m}$ 上固定 $\mathbb F_q$ 每个元素的自同构群，也称 $\mathbb F_{q^m}$ 相对于 $\mathbb F_q$ 的**伽罗瓦群**；它由 **Frobenius 变换** $\sigma_1:\alpha\mapsto\alpha^q$（$\alpha\in\mathbb F_{q^m}$）循环生成。更明确地，伽罗瓦群的元素可以写成映射 $\sigma_0,\sigma_1,\ldots,\sigma_{m-1}$，其中

$$
\sigma_j(\alpha)=\alpha^{q^j},\qquad \alpha\in\mathbb F_{q^m}.
$$

像 $\sigma_j(\alpha)$ 称为 $\alpha$ 的伽罗瓦**共轭元**。注意，对 $\gamma\in\mathbb F_q$，确有 $\sigma_j(\gamma)=\gamma$。

$\alpha\in\mathbb F_{q^m}$ 的**迹** $\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)$ 是其所有共轭元之和，即

$$
\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)
=
\alpha+\alpha^q+\alpha^{q^2}+\cdots+\alpha^{q^{m-1}}.
\tag{7}
$$

迹满射到 $\mathbb F_q$。迹函数 $\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}$ 是 $\mathbb F_q$-线性的：

$$
\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\gamma_1\alpha_1+\gamma_2\alpha_2)
=
\gamma_1\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha_1)
+\gamma_2\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha_2),
\quad
\forall\gamma_1,\gamma_2\in\mathbb F_q,
\ \forall\alpha_1,\alpha_2\in\mathbb F_{q^m}.
\tag{8}
$$

这里的可加性源于：对 $a,b\in\mathbb F_{p^s}$，有 $(a+b)^p=a^p+b^p$，因而 $(a+b)^{p^i}=a^{p^i}+b^{p^i}$；这是因为当 $i=1,2,\ldots,p-1$ 时，

$$
\binom pi=\frac{p!}{i!(p-i)!}\equiv0\pmod p.
$$

还有 $\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha^q)=\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)$。另一个不那么平凡的事实是，$\operatorname{tr}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)=0$ 当且仅当存在 $\beta\in\mathbb F_{q^m}$，使 $\alpha=\beta^q-\beta$。

$\alpha$ 的**范数** $\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)$ 是其全部共轭元之积：

$$
\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)
=
\alpha\cdot\alpha^q\cdots\alpha^{q^{m-1}}
=
\alpha^{(q^m-1)/(q-1)}.
\tag{9}
$$

范数函数具有乘法性：对所有 $\alpha,\beta\in\mathbb F_{q^m}$，

$$
\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha\beta)
=
\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)
\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\beta).
$$

与迹类似，$\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha^q)=\operatorname{Nm}_{\mathbb F_{q^m}/\mathbb F_q}(\alpha)$，而且范数函数满射到 $\mathbb F_q$。

对一般的环（不一定是域），环 $R$ 的**理想** $I$ 是 $R$ 的一个子集，它自身是环，并且对所有 $a\in I$ 和 $r\in R$ 都有 $ar=ra\in I$。本文只处理有限生成理想。给定 $R$ 的子集 $\{a_1,\ldots,a_k\}$，由它们生成的理想为

$$
(a_1,\ldots,a_k)
:=
\{a_1r_1+\cdots+a_kr_k\mid \forall r_1,\ldots,r_k\in R\}.
$$

有时也用 $\langle a_1,\ldots,a_k\rangle$ 表示由 $\{a_1,\ldots,a_k\}$ 生成的理想。

$R/I$ 是 $R$ 关于理想 $I$ 的**商环**，其中加法和乘法为

$$
(r+I)+(s+I)=(r+s)+I,
\qquad
(r+I)\cdot(s+I)=rs+I.
$$

在 $I=\langle a_1,\ldots,a_k\rangle$ 时，为方便起见，可把商环写作 $R/I=R/(a_1,\ldots,a_k)$。在此商环中，可以认同 $a_1=0,\ldots,a_k=0$。

在编码理论中，例如定义 Reed-Muller 码时，我们会频繁处理**多项式环**及其商环。令 $x$ 为不定元，多项式环 $R[x]$ 是所有形式和 $a_nx^n+\cdots+a_1x+a_0$ 的集合，并采用通常的加法和乘法。多元多项式环递归定义为

$$
R[x_1,x_2,\ldots,x_n]
:=
R[x_1,x_2,\ldots,x_{n-1}][x_n].
$$

当 $R=K$，其中 $K$ 是特征为 $p$ 的域时，任意元素的 $p$ 倍都等于零。

为定义 Reed-Muller 码，考虑商环

$$
\mathbb F_q[x_1,\ldots,x_m]
\big/
(x_1^q-x_1,\ldots,x_m^q-x_m),
\qquad q=2^s.
$$

以下 Reed-Muller 码的定义与事实可见 [MS77]。$m$ 个变量、次数 $r$ 的 $q$ 元 Reed-Muller 码记作 $\mathrm{RM}_q(r,m)$；它是 $\mathbb F_q$ 上长度为 $q^m$ 的码，由上述环中次数至多为 $r$ 的所有多项式，在全部点 $(x_1,x_2,\ldots,x_m)\in\mathbb F_q^m$ 上求值得到。由于对所有 $\eta\in\mathbb F_q$ 都有 $\eta^q=\eta$，在上述环中模去 $(x_i^q-x_i)$，可以把给定多项式与 Reed-Muller 码的相应码字一一对应起来。例如，商环中任何多项式的任一变量次数都不超过 $q-1$。

对 Reed-Muller 码而言，一个对我们特别重要的例子是 $q=2$ 的二元 Reed-Muller 码，它定义在商环

$$
\mathbb F_2[x_1,\ldots,x_m]
\big/
(x_1^2-x_1,\ldots,x_m^2-x_m)
$$

上。$\mathrm{RM}_2(r,m)$ 的距离是 $2^{m-r}$；事实上，只要考虑 $r$ 次多项式 $x_1x_2\cdots x_r$，其求值的权重是 $2^{m-r}$，便能立即看出距离至多为此值。用 $\operatorname{ev}(f)$ 表示多项式 $f$ 对应的码字，则 $\operatorname{ev}(f)$ 与 $\operatorname{ev}(g)$ 的逐坐标乘积为 $\operatorname{ev}(fg)$。更一般地，由 $v$ 个变量乘积形成的单项式，其求值对应的码字权重是 $2^{m-v}$。$\mathrm{RM}_2(r,m)$ 的对偶码是 $\mathrm{RM}_2(m-r-1,m)$。

类似事实对一般的 $q$ 元 Reed-Muller 码也成立。例如，若把

$$
(q-1)m-r=\nu(q-1)+\mu,
\qquad 0\leq\mu<q-1,
$$

则 $\mathrm{RM}_q(r,m)$ 的距离是 $(\mu+1)q^\nu$。在一般 $q$ 元情形下，$\operatorname{ev}(f)$ 与 $\operatorname{ev}(g)$ 的逐坐标乘积同样是 $\operatorname{ev}(fg)$。

还可以在 $\mathbb F_q^m$ 的各点上，对不同于“次数至多为 $r$ 的多项式集合”的其他多项式集合求值，由此得到更一般的码，称为**仿射单项式码**。一个对我们很重要的例子是双曲码。它们可以从 Reed-Muller 码中删除奇偶校验得到，从而在保持同一最小距离的同时提高码维数 [HLP98, Ch. 4.4]。具体而言，设计距离为 $d$ 的双曲码有一组基，由所有满足

$$
\prod_{i=1}^m(\alpha_i+1)<d
$$

的单项式 $X_1^{\alpha_1}\cdots X_m^{\alpha_m}$ 构成。附录 A.3 将考察一类更一般的仿射单项式码。


## 当前译本 lines 743–1122

## 3 $\mathrm{GF}(2^s)$ 上的伽罗瓦 qudit

### 3.1 伽罗瓦 qudit 及其量子比特实现

有限域 $\mathrm{GF}(2^s)=\mathbb F_{2^s}$ 上的伽罗瓦 qudit，是一个 $2^s$ 维 qudit；它的泡利群经过特意选取，以编码有限域 $\mathbb F_{2^s}$ 的算术。借助这一选择，这个 $2^s$ 维 qudit 在状态、泡利群和 Clifford 层级方面，都等价于一组 $s$ 个量子比特 [Got24; Wil26]。为 $\mathrm{GF}(2^s)$ 上的伽罗瓦 qudit 构造具有理想性质的量子码，往往能让人构造出具有类似理想性质的量子比特码 [WHY25; GG25a; Ngu25; NP25; He+25c; He+25b]。特别地，通过构造 $\mathrm{GF}(2^s)$ 上具有横向第三层门的 qudit 码，我们可以构造量子比特魔法态蒸馏协议，而在量子比特上执行这些协议只需要量子比特 Clifford 操作 [WHY25; NP25]。因此，我们通过构造并分析 $\mathbb F_{2^s}$ 上的量子码，来研究量子比特魔法态蒸馏协议。

$2^s$ 维伽罗瓦 qudit 与一组 $s$ 个量子比特之间的映射通过一种“qudit-to-qubit 映射”给出，完整细节见 [Wil26]。具体而言，可以为两个系统的状态、其上的 CSS 码以及 Clifford 层级的各层构造同构；在每一层上，它还专门对应对角门。所有这些同构都以自然方式彼此相容。因此，构造伽罗瓦 qudit 的蒸馏协议，也就得到了量子比特的蒸馏协议。下面很快会把这一变换的一部分明确写出。

全文都用 CSS 码指定蒸馏协议，而 CSS 码又用现在已成为标准方式的矩阵来指定 [BH12]：给定矩阵的前 $k$ 行指定 $X$ 逻辑算子，其余各行指定 $X$ 稳定子生成元。这个概念对本文足够重要，因而在此为它命名。关于从 $X$ 与 $Z$ 稳定子／逻辑算子空间构造伽罗瓦 qudit CSS 码的方法，可参见 [Wil26]。下文称两个向量 $\boldsymbol x,\boldsymbol y\in\mathbb F_q^n$ **正交**，若

$$
\langle\boldsymbol x,\boldsymbol y\rangle
\equiv
\sum_i x_i y_i=0.
$$

**定义 3.1（$X$-生成矩阵）。** 量子 CSS 码的一个 **$X$-生成矩阵**是某个矩阵 $G\in\mathbb F_q^{m\times n}$，并带有一个相关的正整数 $1\leq k\leq m$。要求 $G$ 在 $\mathbb F_q$ 上满秩。该矩阵定义一个量子 CSS 码，其中前 $k$ 行是非平凡逻辑 $X$ 算子（称为**逻辑行**），其余各行是 $X$ 稳定子生成元。形式化地，令 $\mathcal G$ 为 $G$ 的各行生成的 $\mathbb F_q$ 向量空间，令 $\mathcal G_0$ 为 $G$ 的后 $m-k$ 行生成的 $\mathbb F_q$ 向量空间。该 CSS 码的 $X$ 稳定子由空间 $\mathcal G_0$ 给出，$Z$ 稳定子由空间 $\mathcal G^\perp$ 给出。

从 $X$-生成矩阵计算码的性质很直接。

**命题 3.2。** 设 $G\in\mathbb F_q^{m\times n}$ 是 $\mathbb F_q$ 上某个量子 CSS 码的 $X$-生成矩阵，并有 $k$ 个逻辑行。该量子 CSS 码有 $k$ 个逻辑 qudit 和 $n$ 个物理 qudit。它的 $Z$ 距离等于下述非零向量的最小 Hamming 权重：该向量属于 $\mathbb F_q^n$，与 $G$ 的后 $m-k$ 行全都正交，但至少与 $G$ 的前 $k$ 行之一不正交。

**证明。** 沿用定义 3.1 的记号，相应 CSS 码的逻辑 qudit 数为

$$
\dim_{\mathbb F_q}\mathcal G-
\dim_{\mathbb F_q}\mathcal G_0
=m-(m-k)=k,
$$

其中第一个等号来自 $G$ 满秩这一要求。$Z$ 距离就是 $\mathcal G_0^\perp\setminus\mathcal G^\perp$ 中元素的最小 Hamming 权重。由线性性，向量 $\boldsymbol z\in\mathbb F_q^n$ 属于 $\mathcal G_0^\perp\setminus\mathcal G^\perp$，当且仅当它与 $\mathcal G_0$ 的每一行正交，但并非与 $\mathcal G$ 的每一行都正交。$\square$

对角门的魔法态蒸馏只与 $Z$ 距离有关，因为可以对魔法态施行 twirling [BK05; BH12]。

**命题 3.3（[BK05; BH12] twirling 的推广）。** 设 $U$ 是一个对角的第三层 $s$ 量子比特算子。对 $\boldsymbol a\in\mathbb F_2^s$，定义算子 $M_{\boldsymbol a}\equiv UX^{\boldsymbol a}U^\dagger$ 与状态 $|A_{\boldsymbol a}\rangle\equiv Z^{\boldsymbol a}U|+\rangle^{\otimes s}$。那么，对任意状态 $\rho$，相对于均匀随机选取的 $(M_{\boldsymbol a})_{\boldsymbol a\in\mathbb F_2^s}$ 作 twirling，得到

$$
\frac1{2^s}
\sum_{\boldsymbol a\in\mathbb F_2^s}
M_{\boldsymbol a}\rho M_{\boldsymbol a}^\dagger
=
\sum_{\boldsymbol a\in\mathbb F_2^s}
\rho_{\boldsymbol a}
|A_{\boldsymbol a}\rangle\langle A_{\boldsymbol a}|,
\qquad
\rho_{\boldsymbol a}\equiv
\langle A_{\boldsymbol a}|\rho|A_{\boldsymbol a}\rangle.
$$

> [!note] 译注
> 原文命题陈述的求和指标有一处漏写上标 $s$，且右端投影之后多排了一个 $A_{\boldsymbol a}$；上式按紧随其后的证明恢复为一致形式。

**证明。** 首先注意，

$$
\langle A_{\boldsymbol a}|A_{\boldsymbol b}\rangle
=
\langle+|^{\otimes s}Z^{\boldsymbol a+\boldsymbol b}|+\rangle^{\otimes s}
=\delta_{\boldsymbol a\boldsymbol b},
$$

因此状态族 $(|A_{\boldsymbol a}\rangle)_{\boldsymbol a\in\mathbb F_2^s}$ 构成一组标准正交基。此外，它们是算子族 $(M_{\boldsymbol a})_{\boldsymbol a\in\mathbb F_2^s}$ 的本征向量，并满足

$$
M_{\boldsymbol a}|A_{\boldsymbol b}\rangle
=UX^{\boldsymbol a}U^\dagger Z^{\boldsymbol b}U|+\rangle^{\otimes s}
=(-1)^{\boldsymbol a\cdot\boldsymbol b}|A_{\boldsymbol b}\rangle.
$$

对任意密度矩阵，可以在此基中展开为

$$
\rho=
\sum_{\boldsymbol a,\boldsymbol b\in\mathbb F_2^s}
\rho_{\boldsymbol a\boldsymbol b}
|A_{\boldsymbol a}\rangle\langle A_{\boldsymbol b}|,
\qquad
\rho_{\boldsymbol a\boldsymbol b}
=\langle A_{\boldsymbol a}|\rho|A_{\boldsymbol b}\rangle.
$$

让该态通过 twirling 信道后，得到

$$
\begin{aligned}
\frac1{2^s}\sum_{\boldsymbol a\in\mathbb F_2^s}
M_{\boldsymbol a}\rho M_{\boldsymbol a}^\dagger
&=
\frac1{2^s}
\sum_{\boldsymbol c\in\mathbb F_2^s}
\sum_{\boldsymbol a,\boldsymbol b\in\mathbb F_2^s}
\rho_{\boldsymbol a\boldsymbol b}
M_{\boldsymbol c}|A_{\boldsymbol a}\rangle
\langle A_{\boldsymbol b}|M_{\boldsymbol c}^\dagger\\
&=
\frac1{2^s}
\sum_{\boldsymbol c\in\mathbb F_2^s}
\sum_{\boldsymbol a,\boldsymbol b\in\mathbb F_2^s}
\rho_{\boldsymbol a\boldsymbol b}
(-1)^{\boldsymbol c\cdot(\boldsymbol a+\boldsymbol b)}
|A_{\boldsymbol a}\rangle\langle A_{\boldsymbol b}|\\
&=
\sum_{\boldsymbol a\in\mathbb F_2^s}
\rho_{\boldsymbol a\boldsymbol a}
|A_{\boldsymbol a}\rangle\langle A_{\boldsymbol a}|.
\end{aligned}
$$

$\square$

通常把 $G$ 的各行记作 $\boldsymbol g_1,\ldots,\boldsymbol g_m$，把第 $i$ 行第 $j$ 个条目记作 $g_{ij}$。我们一般把 $G$ 看成经典码的生成矩阵，即 $G$ 的各行构成该码的一组基。本文限于 $\mathbb F_{2^s}$-线性码：若 $\boldsymbol g_1,\boldsymbol g_2\in\mathbb F_{2^s}^n$ 是码字，那么对所有 $\gamma_1,\gamma_2\in\mathbb F_{2^s}$，$\gamma_1\boldsymbol g_1+\gamma_2\boldsymbol g_2$ 也都是码字。

若 $G$ 是二元矩阵，便立即得到一个量子比特 CSS 码。若 $s>1$，则可按如下方式把矩阵 $G$ 二元化，以产生量子比特码。[^7] 取 $\mathbb F_{2^s}$ 在 $\mathbb F_2$ 上的一组基 $B=(\alpha_i)_{i=1}^s$，即每个 $\gamma\in\mathbb F_{2^s}$ 都能唯一写成

$$
\gamma=\sum_{i=1}^s b_i\alpha_i,
\qquad b_i\in\mathbb F_2.
$$

> [!note] 译注
> 原文在此把分量指标范围排作 $i=1,\ldots,n$；由基含 $s$ 个元素及随后矩阵维数可知，此处应为 $i=1,\ldots,s$。

生成矩阵 $G\in\mathbb F_{2^s}^{m\times n}$ 可以展开成 $\mathbb F_2^{ms\times ns}$ 中的二元矩阵：把 $G$ 的每个条目 $\gamma$ 替换为一个 $\mathbb F_2^{s\times s}$ 矩阵，其第 $(i,j)$ 个条目是 $\operatorname{tr}(\gamma\alpha_i\alpha_j)$ [MS77]。[^8] 所得二元矩阵指定一个量子比特 CSS 码，其中前 $ks$ 行是逻辑 $X$ 算子，后 $(m-k)s$ 行是 $X$ 稳定子生成元。

qudit-to-qubit 映射可以使用不同的基 $B$，从而得到 qudit 与量子比特之间不同的同构。改变映射中使用的基 $B$，等价于在构成该 qudit 的 $s$ 个量子比特上执行一个 CNOT 电路。一个尤其方便的选择是**自对偶基**，即满足 $\operatorname{tr}(\alpha_i\alpha_j)=\delta_{ij}$ 的基。这样的基对所有 $s$ 都存在，而且可以使用 Lempel 分解 [SL80] 在多项式时间内找到。用自对偶基提取域元素的分量尤其方便：

$$
\mathbb F_{2^s}\ni\gamma
=\sum_{i=1}^s b_i\alpha_i,
\qquad
b_i=\operatorname{tr}(\gamma\alpha_i)\in\mathbb F_2.
\tag{11}
$$

利用这一表达式和相位多项式语言，可以建立 qudit 对角门与量子比特对角门之间的联系。本节余下部分将研究若干特定的 qudit 门，包括作用于三个 qudit 的 qudit-CCZ 门，以及单 qudit 门；后者包括 CS（特指 $\mathbb F_4$ 上）、范数门和任意二元扩域上的 $U_7$ 门。这些全都是非 Clifford 门。因此，我们的目标是构造由矩阵 $G\in\mathbb F_{2^s}^{m\times n}$ 编码、并以这些门为横向门的 qudit 码，从而蒸馏相应的魔法态。通过 qudit-to-qubit 映射，这会立即给出量子比特协议，用于蒸馏这些门的等价门。

不过在继续之前，先陈述一些关于维数 $2^s$ 的伽罗瓦 qudit（不论扩张次数如何）的 Clifford 层级的简单观察。我们尤其关注在 $\mathbb F_{2^s}$ 上执行算术的操作；值得注意的是，它们所在的 Clifford 层级与 $\mathbb Z$ 上算术操作大不相同，其根源在于 $\mathbb F_{2^s}$ 中的加法不会产生“进位”。

**备注 3.4（二元扩域中算术操作的 Clifford 层级）。**

1. $\mathbb F_{2^s}$ 上的原位加法，即对 $x,y\in\mathbb F_{2^s}$ 执行

   $$
   |x\rangle|y\rangle\longmapsto|x\rangle|x+y\rangle,
   $$

   是 Clifford 操作。

2. 把 $\mathbb F_{2^s}$ 中一个元素乘以已知常数 $\beta\in\mathbb F_{2^s}^\times$，是 Clifford 操作。这也可以看成从 $(\alpha_i)_{i=1}^s$ 到 $(\beta\alpha_i)_{i=1}^s$ 的基变换。不过，基变换远不止这些，而且它们全都是 Clifford 操作。

3. 两个未知元素 $x,y\in\mathbb F_{2^s}$ 的乘法，即

   $$
   |x\rangle|y\rangle|0\rangle
   \longmapsto
   |x\rangle|y\rangle|xy\rangle,
   $$

   位于 Clifford 层级的第三层。第 3.2.1 小节会明确说明这一点。

4. 原位 Frobenius 变换 $|\gamma\rangle\mapsto|\gamma^2\rangle$ 是 Clifford 操作。一种看法是，在正规基[^9]中展开，其中对 $\mathbb F_{2^s}$ 的某个本原元 $\alpha$，取 $\alpha_i=\alpha^{2^i}$。写成 $\gamma=\sum_{i=1}^s b_i\alpha_i$，则

   $$
   \gamma^2
   =\left(\sum_{i=1}^s b_i\alpha_i\right)^2
   =\sum_{i=1}^s b_i^2\alpha_i^2
   =\sum_{i=1}^s b_i\alpha_{i+1},
   $$

   其中最后一个下标按正规基循环理解。因此，Frobenius 变换只是循环移位构成 qudit 的 $s$ 个量子比特（对这一基 $B$ 而言），所以它是 Clifford 操作。[^10]

   > [!note] 译注
   > 原文将最后一个下标写作 $i+1\pmod{s+1}$；正规基含 $s$ 个元素，这里按上下文译为在这 $s$ 个基元之间循环。

[^7]: 等价地，可以先由 $\mathbb F_{2^s}$ 上的矩阵构造 qudit 码，再把码本身二元化 [Wil26]。

[^8]: 可以把映射 $\gamma\mapsto(\operatorname{tr}(\gamma\alpha_i\alpha_j))_{i,j=1}^s$ 理解为：先把 $\mathbb F_{2^s}$-线性码的每个码字乘以 $\alpha_i$，随后把每个条目二元化；关于把 qudit 码映射为量子比特码的更多细节，见 [Wil26]。

[^9]: $\mathbb F_{q^m}$ 在 $\mathbb F_q$ 上的正规基，即形如 $\{\alpha,\alpha^q,\ldots,\alpha^{q^{m-1}}\}$ 的基，总是存在；例如见 [LN96, Thm. 2.35]。如前所述，对 $\mathbb F_{2^s}$ 在 $\mathbb F_2$ 上的扩张，自对偶基总是存在；但自对偶正规基存在，当且仅当 $s$ 不能被 4 整除 [MP13]。

[^10]: 回想一下，为 $\mathbb F_q$ 在 $\mathbb F_2$ 上选择不同的基 $B$，会得到从 qudit 到量子比特的不同同构；不过每种选择都给出 Clifford 层级各层中对角门的有效同构。因此，可以选择一个特定的基 $B$，确定相应量子比特门所在的层，并由此得出初始 qudit 门所在的层。

### 3.2 门的展开

#### 3.2.1 Qudit-CCZ 门

如前所述，$\mathrm{GF}(2^s)$ qudit 上的门也可以展开成量子比特门，其中对角门映射为对角门，而且保留它们所在的 Clifford 层级。下面进一步考察这一点。完整细节见 [Wil26]，这里也给出基本思路。先从三 qudit CCZ 门 [GG25a; Ngu25] 的例子开始；对 $x,y,z\in\mathrm{GF}(2^s)$，其定义如下：

$$
\mathrm{CCZ}:\quad
|x\rangle|y\rangle|z\rangle
\longmapsto
(-1)^{\operatorname{tr}(xyz)}
|x\rangle|y\rangle|z\rangle.
\tag{12}
$$

为简单起见，令 $B=(\alpha_i)_{i=1}^s$ 为 $\mathbb F_q$ 在 $\mathbb F_2$ 上的一组自对偶基。要展开这个门，先在自对偶基中展开 $x,y,z$：

$$
x=\sum_{i=1}^s x_i\alpha_i,
\qquad
y=\sum_{i=1}^s y_i\alpha_i,
\qquad
z=\sum_{i=1}^s z_i\alpha_i,
\qquad
x_i,y_i,z_i\in\{0,1\}.
$$

三个 qudit 上的计算基态 $|x\rangle|y\rangle|z\rangle$，可以通过写出 $x,y,z$ 的各个分量，展开成 $3s$ 个量子比特上的计算基态。接着利用 $\operatorname{tr}(\cdot)$ 的 $\mathbb F_2$-线性性：

$$
\operatorname{tr}(xyz)
=
\operatorname{tr}\!\left(
\sum_{i,j,k=1}^s
x_i y_j z_k\,\alpha_i\alpha_j\alpha_k
\right)
=
\sum_{i,j,k=1}^s
x_i y_j z_k\operatorname{tr}(\alpha_i\alpha_j\alpha_k).
\tag{13}
$$

把 CCZ 展开成 $3s$ 量子比特门时，它会给计算基态 $|x\rangle|y\rangle|z\rangle$ 赋予相位

$$
\operatorname{tr}(xyz)
=
\sum_{i,j,k=1}^s
x_i y_j z_k\operatorname{tr}(\alpha_i\alpha_j\alpha_k).
$$

因此在量子比特层面上，对每一个满足 $\operatorname{tr}(\alpha_i\alpha_j\alpha_k)=1$ 的三元组 $(x_i,y_j,z_k)$，这个 qudit CCZ 门都会施加一个量子比特 CCZ 门。

下面给出 $\mathbb F_4=\{0,1,\omega,\omega^2\}$ 上 qudit CCZ 门的一个明确例子，其中域算术由 $\omega+\omega^2=1$ 指定。可以验证，$(\omega,\omega^2)$ 构成一组自对偶基。图 4 左侧表示按此基展开的 $\mathbb F_4$-qudit CCZ 门。断言 3.5 表明，qudit CCZ 门可以在量子计算机上相干地乘出域 $\mathbb F_q$ 中的元素。

![原文图 4：$\mathbb F_4$-qudit CCZ 的量子比特展开与乘法线路，印刷页码 16、PDF 页序 16](Snapshots/S008/p016-01-fig-4-qudit-ccz-circuits.png)

**图 4。**（a）把 $\mathbb F_4$-qudit CCZ 展开成量子比特 CCZ。展开 $x=x_1\omega+x_2\omega^2$，其中 $x_1,x_2\in\mathbb F_2$；$y,z$ 同理。（b）可以消耗与 $\mathbb F_4$-CCZ 对应的魔法态，在 $\mathbb F_4$ 中执行乘法——只需用 Hadamard 门共轭第三对量子比特。图中文字与线路标记为 $x,y,z$、其二元分量 $x_1,x_2,y_1,y_2,z_1,z_2$，输入 $|+\rangle|+\rangle$、输出 $|xy\rangle$，以及两个 $H$ 门。

**断言 3.5。** $\mathbb F_{2^s}$-qudit CCZ 门使人能够在量子计算机上乘出该域中的两个元素。也就是说，一次 CCZ 门配合 Clifford 操作，足以执行算术操作

$$
|x\rangle|y\rangle|0\rangle
\longmapsto
|x\rangle|y\rangle|xy\rangle,
$$

其中 $x,y\in\mathbb F_{2^s}$，每个 ket 都是一个 $s$ 量子比特寄存器（等价地，一个 $2^s$ 维 qudit 寄存器）。图 4(b) 给出 $\mathbb F_4$ 的例子。

**证明。** 我们证明，依次执行以下操作，会在三 qudit 态 $|x\rangle|y\rangle|0\rangle$ 上实现所需变换：

1. 对构成第三个寄存器的每个量子比特施加 Hadamard；这些量子比特起初全处于 $|0\rangle$ 态。

2. 对三个 qudit（即 $3s$ 个量子比特）施加 qudit CCZ 门。[^11]

3. 再次对构成最后一个寄存器的全部 $s$ 个量子比特施加 Hadamard。

后面要用到如下事实：

$$
H^{\otimes s}|z\rangle
=
\frac1{\sqrt{2^s}}
\sum_{t\in\mathbb F_{2^s}}
(-1)^{\operatorname{tr}(zt)}|t\rangle.
\tag{14}
$$

这里，$|z\rangle$ 表示与 $z\in\mathbb F_q$ 对应的 qudit 计算基态，而 $H^{\otimes s}$ 对应于在构成该 qudit 的 $s$ 个量子比特上施加量子比特 Hadamard。要看出此式，在自对偶基 $(\alpha_i)_{i=1}^s$ 中展开 $z\in\mathbb F_{2^s}$：

$$
z=z_1\alpha_1+\cdots+z_s\alpha_s;
$$

同样把 $t\in\mathbb F_{2^s}$ 展开为 $t=t_1\alpha_1+\cdots+t_s\alpha_s$，其中 $z_i,t_i\in\{0,1\}$。于是 $H^{\otimes s}|z\rangle$ 是所有 $|t\rangle$ 的均匀叠加，其相位为 $(-1)^{z_1t_1+\cdots+z_st_s}$。这个指数恰好是

$$
\begin{aligned}
\operatorname{tr}(zt)
&=
\operatorname{tr}\!\left[
\left(\sum_i z_i\alpha_i\right)
\left(\sum_j t_j\alpha_j\right)
\right]\\
&=
\sum_{i,j}z_it_j\operatorname{tr}(\alpha_i\alpha_j)
=
\sum_i z_it_i.
\end{aligned}
$$

因此所需电路的执行过程如下：

$$
|x\rangle|y\rangle|0^s\rangle
\xrightarrow{\ H^{\otimes s}\ \text{作用于 }z\ }
|x\rangle|y\rangle
\frac1{\sqrt{2^s}}
\sum_{z\in\mathbb F_{2^s}}|z\rangle
\xrightarrow{\ \text{qudit CCZ}\ }
\frac1{\sqrt{2^s}}
\sum_z(-1)^{\operatorname{tr}(xyz)}
|x\rangle|y\rangle|z\rangle.
\tag{15}
$$

再对 $z$ 寄存器施加 $H^{\otimes s}$：

$$
\begin{aligned}
H^{\otimes s}
\left(
\frac1{\sqrt{2^s}}
\sum_z(-1)^{\operatorname{tr}(xyz)}|z\rangle
\right)
&=
\frac1{\sqrt{2^s}}
\sum_z(-1)^{\operatorname{tr}(xyz)}
\left(
\frac1{\sqrt{2^s}}
\sum_t(-1)^{\operatorname{tr}(zt)}|t\rangle
\right)\\
&=
\frac1{2^s}
\sum_t
\left(
\sum_z(-1)^{\operatorname{tr}(z(xy+t))}
\right)|t\rangle\\
&=|xy\rangle,
\end{aligned}
$$

其中最后一步使用了

$$
\sum_{z\in\mathbb F_{2^s}}
(-1)^{\operatorname{tr}(zu)}
=
\begin{cases}
2^s,&u=0,\\
0,&u\ne0.
\end{cases}
$$

$\square$

这种二元扩域乘法可用于例如解码量子干涉测量 [Jor+25]。特别地，[Kha+25] 针对求解二元扩域上的最优多项式求交问题，给出了详细的资源分析。二元扩域乘法还可能有助于制备某些催化剂态 [Kim25]。

后文只给出不超过 $\mathbb F_{64}$ 的 qudit-CCZ 蒸馏协议（表 3）。对于更大的二元扩域，例如 $\mathbb F_{2^{163}}$ 中的乘法，可以付出一些额外 CNOT 门，把问题归约成小二元扩域中的多次乘法 [CC88; CÖ10]。在第 5.2 节和附录 B.1 引入代数曲线的相关概念之后，我们会在附录 B.3 给出这种归约的一个例子。

注意，备注 3.4 的一个推论是：对任意 $\beta_1,\beta_2\in\mathbb F_{2^s}^\times$，qudit CCZ 门 $\mathrm{CCZ}^{\beta_1}$ 与 $\mathrm{CCZ}^{\beta_2}$ Clifford 等价，其中

$$
\mathrm{CCZ}^{\beta}
|\eta_1\rangle|\eta_2\rangle|\eta_3\rangle
=
(-1)^{\operatorname{tr}(\beta\eta_1\eta_2\eta_3)}
|\eta_1\rangle|\eta_2\rangle|\eta_3\rangle.
\tag{16}
$$

这是因为，按照原文所述，执行 $\mathrm{CCZ}^{\beta_1}$ 的一种等价方式，是先在第一个 qudit 上执行乘法[^12]

$$
|\eta_1\rangle
\longmapsto
\left|\frac{\beta_2}{\beta_1}\eta_1\right\rangle,
$$

再施加 $\mathrm{CCZ}^{\beta_2}$。这一事实稍后将在第 5.3 节蒸馏 qudit-CCZ 门时发挥作用。

> [!note] 译注
> 原文在上述基变换中写的是 $\beta_2/\beta_1$。按备注 3.4 的乘法约定和式 (16) 直接代入，若要由 $\mathrm{CCZ}^{\beta_2}$ 实现 $\mathrm{CCZ}^{\beta_1}$，该比例应为 $\beta_1/\beta_2$。译文保留原文的 $\beta_2/\beta_1$，并在此指出这一疑似笔误。

[^11]: 这一步也可以通过消耗一个 $|\mathrm{CCZ}\rangle$ 态并使用 Clifford 操作来执行。

[^12]: 事实上，三个 qudit 中任取一个都可以。

