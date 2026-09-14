---
task_id: 20260914-state-injection-xor
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: 77ce1cc7d99a4940b7cd67292b9a5089
target_files:
  - Notes/04-Magic State Injection/State injection.md
---

# 用户目标

重写整篇《State injection》，让读者学会一套可复用的“基标签异或 → 求和换元 → 测量分支算符 → 条件校正”方法，用它贯穿单比特 teleportation、一般 U、in-place gadget、T injection 和资源错误传播。用户希望避开原文后半部分反复把 U 写成 a,b,c,d、资源态写成 u0,u1,v0,v1、逐项矩阵相乘的冗长计算；不是只把第一节换成 XOR、后面照旧，也不是用更密的记号跳过理由。

用户已理解的切入：所有 x,y,m 为比特，CNOT_{a→d}|x>_d|y>_a=|x⊕y>_d|y>_a；在输入 sum_x c_x|x>_d 与 |+>_a 上，令 m=x⊕y、y=x⊕m，得到 (1/sqrt(2)) sum_m |m>_d X_a^m|psi>_a。振幅 c_x 保持不变，换的是求和标签；m 在测量前是指标，测量后才是记录。可以引入 J_{a←d}=sum_x |x>_a< x|_d 和分支算符，但请判断符号是否确实减少认知负担。

# 必读材料

以下仓库文件使用 Browser 指定的同一个 GitHub commit；指定局部章节的无需全文读：

- 本任务 TASK.md；Notes/WRITING_GUIDE.md；Notes/OBSIDIAN_MATH.md；Notes/PRO_OUTPUT_PROTOCOL.md。
- Notes/04-Magic State Injection/State injection.md：全文，包含之前追加的两处注释。
- CANONICAL_KNOWLEDGE.md 的“State injection 与 T injection”条目；Notes/00-index.md 的第 4 路线。只核对归属，不把维护信息写入正文。
- Papers/SOURCES.md 的 S001 登记；主来源 Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf 第 3–4 页，Sec. II.B、式 (2)–(3)、Sec. III 开头。若 GitHub App 无法读取 PDF，可读取同一版本 https://arxiv.org/pdf/2606.07734v1 或 https://arxiv.org/html/2606.07734v1 相关部分；至少一种方式实际读到来源，不能只凭当前笔记猜测论文。
- Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md：§6（单资源 twirling）、§9.2（独立性是额外条件）。只借用结论与连接，不重写其一般理论。
- Notes/05-Magic State Distillation/Distillation protocol.md：§1–§3 的协议对象与 CSS checks，用于区分注入、inner protection 与 outer checks，不搬运完整蒸馏推导。

# 读者与教学要求

读者能使用单比特计算基、张量积、线性性、Pauli X/Z、伴随与酉性、投影测量。异或、X 基标签、分支算符、跨线空间对应和 Clifford 层级只可在正文建立所需含义后使用，不预设读者掌握 tensor-network、ZX calculus、Choi 同构或一般量子通道理论。

请自行规划完整的教学结构。开头建立注入要完成的动作与复用方法；先清楚推一次异或求和换元。后续复用同一规则、算符共轭或 X 基标签，例如 |s_X>=Z^s|+>；选择真正简洁的推导，不强迫每一行都出现 ⊕。关键等式必须有可跟随的桥梁，不能用“化简得”掩盖 R_U、K_m 的来源。复杂段落先说明为何要计算、先固定哪个约束、结果如何用于下一步。把用户此前的疑惑自然融入正文，删除被替代的长矩阵计算和重复补丁；关键证明不藏在可跳过的 callout 里。

保留两种输出位置的线路或等价清楚描述，明确 d⊗a、两种 CNOT 方向、测量哪条线与校正哪条线。保持研究笔记的适当细度，不为了短而只罗列公式；也不扩成一般量子信息百科。

# 必须由你核验并处理的数学边界

1. 一般 U 主构造限定单比特酉门。跨线态标签要解释；未归一化分支 K_m|psi>、概率和归一化条件态分开。由 K_m†K_m 得出概率，不先假定所有资源或噪声分支都是 1/2。
2. 一般 U 的传态恒等式涉及 W_U=(I⊗U)CNOT_{a→d}(I⊗U†) 与 UX^mU† 校正。不能据此声称任意 U 的资源态加 Clifford 操作即可实现 U；受控 Clifford 也不自动是 Clifford。
3. 原位线路以 d 的 X 基控制未知辅助门 R，然后 CNOT_{d→a}，测量 a。需用符号推理建立约束 R|U>=ZU|->，解释 R_U=ZUZU† 是一个酉延拓而非唯一解，并建立 K_m=X^mUX^m/sqrt(2)、C_U=UXU†X 与 C_U^mK_m=U/sqrt(2)。这些是验收对象，不应凭请求直接当成已证明公式。可用 |s_X> 作用、CNOT 的 XOR 和相位配对来避免四元矩阵展开。理想资源态上同样有效的不同延拓不自动具有相同错误传播。
4. [U,Z]=0 消去该 R_U；进一步 U∈C3 才保证校正 Clifford。T=diag(1,ω)、ω=e^(iπ/4)、S=diag(1,i)，需推得 C_T=ω^(-1)S 与 S^mK_m=ω^mT/sqrt(2)。标清可忽略的分支整体相位；受控操作内的相对相位不能随意丢。相位指数是整数/实数计算，不能把 ω^(x⊕m) 无条件改成 ω^(x+m)。
5. 对 T 线路的资源 Z/X 错误，优先用 Pauli 传播或基标签推导分支映射，核验 K_m^(Z)=(-1)^m ZK_m 与 K_m^(X)=K_(m⊕1)，不再重做每个 2×2 矩阵。原文有待纠正的推论：测量位 m 已知，并不代表未知资源 X 错误是否发生也已知；不能仅凭 m 把只有 X-fault 分支才有的额外 Z 当成已知 byproduct 更新 frame。请对照 S001 式 (3) 说明其简写/条件，而不是照抄原文解释。
6. 严格区分固定测量记录下的相干错误、丢弃记录后的混合通道、真正的 syndrome 投影。若以 stabilizer 区分 |phi> 与 Z|phi>，需该检查对理想 |phi> 有确定本征值且与相应 Z 反对易。inner code 的稳定子不能检测同一 inner code 的逻辑 Z；结合 S001 §III 开头说明 outer checks 的层次。不要无条件写“只有 syndrome 后才可能得到随机 Z 模型”。引用 twirling 的现有 owner，且独立输入仍是额外假设。
7. 收紧泛化：多比特 CCZ 可以产生相关 Z 字符串，不能照搬单比特等概率结论；sqrt(T) 的校正未必 Clifford。保持单比特主线，不为泛化另写大章。保留 state injection 与物理态编码注入的术语区别，以及 distillation 接口。

旧正文在上述条件上的不严谨处可在当前文件中据核验修正。来源措辞简略时明确具体线路与模型，不能把论文摘要当普遍结论。如出现无法用来源和推导解决的冲突，按协议准确返回，不猜测。

# 写作权限与交付

唯一 allowlist 是 target_files。可全文重写、重排章节和替换冗余段落；不能输出或修改 TASK、其它正式笔记、索引、canonical 或文献登记。不得删除、移动、重命名、合并或拆分正式文件。无需新前置笔记；现有 canonical ownership 与主要公式保持。

连续复读全稿，确认每个新符号有用途、后文确实复用前面方法、必要理由充分而没有恢复冗长分量展开。返回可直接替换的完整中文 Markdown；不返回设计稿、diff、自评或建议列表。严格遵守协议的 binding、COMPLETE、至少五反引号文件块和 END_RESPONSE。数学用原始 Obsidian $ / $$，不使用 TeX 外层分隔符；不要在 END_RESPONSE 后追加文字。不要修改 GitHub。
