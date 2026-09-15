---
task_id: 20260915-state-injection-narrative
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: 814a837778844e4483ff51e3f6344ec5
target_files:
  - Notes/04-Magic State Injection/State injection.md
---

# 要解决的读者问题

用户已经让 Pro 用异或方法重写过整篇笔记，又连续请求局部补充，但仍无法理解为什么要改变描述和线路。最新原话：“我不理解为什么要把 CNOT 改成数据比特的 X 基下的描述，这样问题不是复杂化了吗？”随后要求：“让 pro 理解这个问题，重新组织文章，这样很容易混乱”。

请真正重新组织全文，使读者在每次引入对象之前知道当前目标、已有方法的限制、下一步的收益。不是仅在 §2.1 前加一句“为了后面方便”，也不是在旧结构上继续叠加问答或 callout。先在内部做教学判断，再直接写最终笔记；由你决定合适的结构，不把下列诊断当作指定目录。

# 真实反馈链与当前基线

- 读者最早把 d⊗a 的张量顺序与 a→d 控制方向混淆。
- 传态公式突然出现，使其觉得像先知道答案；用户认可 m=x⊕y、y=x⊕m 的一一换元，要求全文避免反复逐分量矩阵展开。
- 用户强调“代入 I=P_++P_-、X=P_+−P_-，再按 P_± 合并”才是 CNOT 等价改写的关键。需要此改写时，应把关键代数桥梁融入正文，避免只给等号或只说相位回踢。
- 读者追问为何改为数据线输出需要辅助 R、为何还要数据 X 基控制。当前 §3.2 的候选线路失配比较已经回答部分动机，但随后 K_0、λ、两基矢又重复同一比较。
- 读者询问 §1 是否是量子隐形传态；现基线已将标题改为 One-bit teleportation，但正文仍需自然定位其与标准远程 Bell 对协议的区别。
- 最新困惑是：基础异或传态已完成，为什么又学习数据 X 基？当前 §2.1 “后面会用到”并未建立实际需求。

当前 checkpoint 保存了用户最新手工修改，包括删去旧投影 callout、压缩相位回踢段、补入辅助测量前的求和行。它们提示读者需要自然正文和可跟随的关键中间步；不要机械恢复历史补丁。允许为了全文一致性重写这些内容，但应保留其解决的问题。

# 必须由新结构解决的混淆

1. 基础 one-bit teleportation 在计算基用 XOR 已可完成，并不以数据 X 基改写为先决条件。何时需要 X 基，应先有当前要完成的目标，例如把 U 引入辅助资源并处理共轭。将数据投影保持固定、把辅助端写成 I/Z，才让 UZU† 的作用直接可读。若仍采用这条一般 U 路径，先使这种需要成立，再引入投影分解和表示。
2. 区分三个动作：同一 CNOT 的等价表示；引入一般 U 后的新算符 W_U；改 CNOT 方向和测量位置的原位新线路。不能让读者以为只是连续“换一种写法”。输出位置、测量位置、量子控制与经典前馈随相应动作明确交代。
3. s 是相干的 X 基标签，m 是实际测量记录；“正负分支”与“测量的两个分支”不可含混。未归一化输出、概率与条件态在适用处闭合。
4. 对原位构造，先指出固定 m=0 时 + 输入已对、− 输入得到 ZU|+〉而目标是 UZ|+〉，再说明为何只补偿 − 输入以及为什么必须保持相干控制；R 不是改变输出位置的普遍固定代价，对角 U 可取 I。
5. 判断一般 U、J、整族 R_θ 延拓、Clifford 层级和具体 T 线路的主次与引入时机。无需沿用当前顺序；可将较深的一般化或技术补充放在同一文件的后部，但必需的动机与关键证明不能藏入可跳过的注释。保留一般 U 的明确结论、条件和完整必要推导，不得用删去难点代替重组。
6. 前半部分形成可继续使用的计算方法，后半部分错误传播与蒸馏接口也必须延续问题驱动的主线。保留重要边界，同时避免它们全部挤成新的术语目录或泛化百科。

# 读者起点

可依赖计算基、张量积、线性性、Pauli X/Z、酉性/伴随及投影测量。已认可二进制指标与 XOR，但仍需首次使用处交代定义和标签意义。不预设掌握一般量子通道、Choi、ZX calculus 或 tensor network。新符号必须有即时用途，不以 J、K、s 的堆叠替代解释。

# 必须读取

以下仓库文件须读 Browser 固定的同一 commit：

- 本任务 TASK.md；Notes/WRITING_GUIDE.md；Notes/OBSIDIAN_MATH.md；Notes/PRO_OUTPUT_PROTOCOL.md。
- Notes/04-Magic State Injection/State injection.md：全文。
- CANONICAL_KNOWLEDGE.md 中“State injection 与 T injection”条目；Notes/00-index.md 第 4 路线。只用于核对归属和接口，不把维护内容写入读者正文。
- Papers/SOURCES.md 的 S001、S010；Papers/RELATIONS.md 中 S001/S010 辅助范围。
- S001：Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf 第 3–4 页 Sec. II.B、式 (2)–(3) 及 Sec. III 开头；GitHub App 若不能读 PDF，使用 https://arxiv.org/pdf/2606.07734v1 或 https://arxiv.org/html/2606.07734v1 的同版相关内容。
- S010：Papers/S010_2000_Zhou_one_bit_teleportation.pdf 的 Sec. II（PDF 第 2–3 页，尤其式 (7)）；或 https://arxiv.org/pdf/quant-ph/0002039v2 同版内容。它用于 one-bit teleportation 名称、X-teleportation 线路和远程协议的区别，不把其中特殊门构造无条件推广为任意 U 的低成本实现。
- Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md：§6、§9.2。
- Notes/05-Magic State Distillation/Distillation protocol.md：§1–§3 的协议对象与 CSS checks；Notes/04-Magic State Injection/MGT 的反向传播与稳定子码构造.md 的开头、§8“适用边界”与“与其它笔记的连接”。

不能只凭 Codex 的说明代替实际读取必需来源。来源未读到时按协议说明具体缺项。

# 数学与范围验收

- d⊗a 与 CNOT 方向分开；XOR 换元一一对应、c_x 不变，保留关键求和中间步；之后复用规则、投影或相位标签，不回到一般 U 四矩阵元逐分量计算。
- 正确保留辅助线输出的 W_U=(I⊗U)CNOT_{a→d}(I⊗U†)、分支 UX^m/√2（必要时含跨线 J）及 UX^mU† 校正。一般 U 的线路恒等式不等于只消耗资源就可低成本实现；受控 Clifford 不自动是 Clifford。
- 原位规范选择 R_U=ZUZU†，约束 R|U〉=ZU|−〉，K_m=X^mUX^m/√2，C_U=UXU†X。建立而非只列这些式子；说明单态约束、酉延拓不唯一、不同延拓的错误传播未必相同。可压缩冗长参数化，不能忽略受控门内部的相对相位。
- [U,Z]=0 消去 R_U；U∈C3 才保证相关校正是 Clifford。T=diag(1,ω)、ω=e^(iπ/4)，C_T=ω^(−1)S，S^mK_m=ω^m T/√2；相位指数按整数计算，不能无条件把 x⊕m 替成 x+m。sqrt(T) 的校正仍含 T。
- 标准 T 线路中，资源故障位于资源制备后、CNOT 前；K_m^(Z)=(−1)^m ZK_m、K_m^(X)=K_(m⊕1)。未知资源 X 故障不是被测量位 m 揭示的事件，不能凭 m 把只在故障情况下才有的 Z 当已知 byproduct 入 frame。
- 资源 X 故障在实际 S^m 前馈后、固定记录时分别为 S†σS 与 SσS†；忽略记录得到 (σ+ZσZ)/2。这与实际 syndrome 投影、资源端 twirling 是不同过程；保留记录时不可无条件换成同一个随机模型。
- syndrome 区分需理想态对检查有确定本征值且错误与检查反对易；inner stabilizer 检测不了自身 logical Z，outer checks 跨 inner blocks。输入独立性额外假设；相邻主笔记承担一般理论。
- 保留 CCZ 相关 Z 字符串的外推边界、物理编码注入与门注入的术语区别、蒸馏接口；不要将单比特等概率结论不加条件推广到多比特。

这些验收对象主要来自已核验的当前笔记。可以重组和压缩重复表达，保持实际线路、条件和数学含义明确。若出现无法通过来源与推导消解的冲突，按协议返回具体问题。

# 输出权限

唯一 allowlist 为 target_files。直接输出可替换的完整中文 Markdown，不输出提纲、建议、局部 patch 或自评，不修改 GitHub。不新增、删除、移动、重命名、合并或拆分正式笔记，不修改索引、canonical、来源登记或任务文件；如确实需要上述结构变化，返回 DECISION_REQUIRED。

从头连续复读完整稿，判断每次改变表示或线路之前，读者是否已知道原因。只有章节顺序和推理桥梁真正改善才算完成。保持 Obsidian 数学格式，遵守隐藏 binding 和完整文件协议，END_RESPONSE 后不得续写。
