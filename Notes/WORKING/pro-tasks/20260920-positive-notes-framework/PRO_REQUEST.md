---
task_id: 20260920-positive-notes-framework
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: 2060de553a4b7e6b393a600e6de9870f
target_files:
  - AGENTS.md
  - Notes/AGENTS.md
  - Notes/WRITING_GUIDE.md
  - Notes/PRO_WORKFLOW.md
  - Notes/PRO_OUTPUT_PROTOCOL.md
  - Notes/OBSIDIAN_MATH.md
  - Notes/WORKING/README.md
  - Notes/TEMPLATES/APPLY_REPORT.md
  - Notes/TEMPLATES/BROWSER_AUTHOR_PROMPT.md
  - Notes/TEMPLATES/BROWSER_REVIEW_PROMPT.md
  - Notes/TEMPLATES/FINAL_REPORT.md
  - Notes/TEMPLATES/PRO_REQUEST.md
  - Notes/TEMPLATES/REVIEW_REQUEST.md
  - Notes/TEMPLATES/TASK.md
  - Notes/WORKING/pro-tasks/20260920-positive-notes-framework/FRAMEWORK_ANALYSIS.md
---

# 用户真实目标

用户原话：“目前仓库让pro写出的问题notes有很明显的问题，就是大量的‘不是....而是’这种类似的句式，就像是防御性写作一样，‘不能理解为....’很影响阅读的连贯性，应该让pro的写作正向引导减少这种否定句式，乃至于框架本身也需要这样写，用正向规定。让pro分析给出新的框架文件和更新提示词，codex更新本地文件。”

请实际诊断规则、请求、审查如何诱发防御性写作，直接交付新的完整框架和模板，Codex 负责应用。希望读者沿对象、关系、条件、推导和用途连续形成理解。每条规范尽量直接说明作者应建立什么、怎样完成、读者由此能做什么；框架自身示范这种语体。

# 本次产物与权限

allowlist 中前 14 个文件是现有活动框架/提示模板，最后一个 FRAMEWORK_ANALYSIS.md 是本任务内分析产物。请返回全部 15 个完整文件。保持路径和各文件职责，公共写作原则由 WRITING_GUIDE 统一承担，其余模板在实际使用位置简短调用。可把一致的框架版本更新到 1.2。

正式主题 Notes 本轮作为诊断材料，后续写作使用新框架。它们的正文、数学、文件边界、canonical ownership、索引、来源登记和历史任务保持当前状态。所有文件完整输出，真实协议样例保留原语法；Codex 正在兼容 payload 内协议样例。

# 必须读取的同一 checkpoint 材料

- 本任务 TASK.md、PRO_REQUEST.md、REVIEW_REQUEST.md。
- allowlist 中已存在的全部 14 个框架/模板文件。
- Notes/04-Magic State Injection/State injection.md：开头、§3 一般 U 引入和 §4 原位构造中的对比语句（约前 1050 行），重点看各句前后的推理作用。
- Notes/07-Lifted-Product Code/Lifted product code.md：开头约 110 行、约 215–240 行、约 475–505 行。
- Notes/06-CCZ Distillation/Tensor product 对 direct sum 的分配律.md：约前 115 行。
- Notes/WORKING/pro-tasks/20260915-state-injection-narrative/PRO_REQUEST.md：用于观察上一轮反馈怎样进入请求。

以上数学笔记用于语言诊断。分析引用现有句子时保持原意；本次成果是规范及提示模板。

# 期望的新写作机制

由 Pro 自行组织规则和模板，以下是验收目标：

1. 默认直接陈述对象是什么、怎样构造、关系如何成立、条件与用途是什么。开头和段落推进由当前真实问题及已建立内容衔接。
2. 每段按实际需要完成清楚的教学动作。正向陈述保持自然行文与章节连续性，句式、顺序和节奏依据内容变化。
3. 对数学否定、反例、必要排除、来源适用范围、真实读者误解，明确其信息价值和适用位置，保留准确性。用具体条件、分叉及后果表达有用对比，主线承接正面构造。
4. 专门处理‘不是…而是’、‘不能理解为…’、‘不要以为…’等修辞：从读者和段落作用判断是否有实际待澄清对象，并展示如何把规则和正文写成连续正向说明。少量例子放 WRITING_GUIDE，具体诊断及改写演示放任务分析；其余文件简短引用统一标准。
5. 写作、请求、审查共同关注连贯性。请求用已知起点、正文待建立内容、事实支持范围、输出范围等正向信息组织；审查先确认主线与信息是否完整，再依据实际影响修订。
6. 完稿检查用可判断的质量标准：知识和数学信息保留、条件清楚、必要对比有具体对象和推理用途、读者能继续下一步。词频检索仅供人工复读定位。质量以语义和连续阅读判断。
7. 修改旧笔记的反馈通过相关段落及衔接整合，避免在正文积累维护对话。规则自身应同样以正向行动和验收标准组织。

# 需要保持的运行含义

Pro 承担教学性/数学性/语义性成文，Codex 承担本地/Git、完整性和上下文格式规范化。任务分支内现有自动连续授权、R01/R02、隐藏 binding、固定 checkpoint、staging、allowlist、完整文件、消息状态、END_RESPONSE、失败保留与成功清理均保持可执行含义。

Pro 通过已连接 GitHub 实际读取材料并输出文本；本地应用与 Git 写入由 Codex 执行。正式文件结构变更、来源冲突、数学歧义、越权路径和需要合并主分支等按现有入口处理。根 AGENTS 的 Papers/Translations 分流、冲突权威、知识唯一归属和交付回执保留实质。权限规定可正向写清责任、前提与下一步，仍须清晰可执行。

格式与 parser 的机器字段、状态枚举及标记保持兼容。模板中的占位符保持可复用。TASK 的 review_policy 与请求模板保持一致关系，若统一枚举需说明迁移方式，历史任务按原值解释。当前 remote 名称和分支前缀应由具体仓库确定，避免把 origin 作为唯一实际配置；分支命名默认 codex/。

# FRAMEWORK_ANALYSIS.md 内容

中文简述：发现的诱发机制和已读文件证据、改动与职责分配、少量有代表性的规则及正文正向改写例、保留数学/流程边界的方法、后续任务的使用与验收。正文样例仅放在该分析稿，应用范围保持框架文件。请对根因作适度判断，将文本观察与模型因果推测分清。

# 交付

R01 依据当前 checkpoint 的 PRO_OUTPUT_PROTOCOL 输出；用足够长的外层 Markdown fence 包含协议自身的 fence 样例，保证 payload 完整。先在内部完成分析和设计，然后输出 allowlist 中 15 份可直接替换文件。FRAMEWORK_ANALYSIS.md 承担分析内容，其他文件只保留各自活动职责。
