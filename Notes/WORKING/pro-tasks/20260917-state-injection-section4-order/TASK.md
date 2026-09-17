---
task_id: 20260917-state-injection-section4-order
route: codex-only
status: DONE
target_files:
  - Notes/04-Magic State Injection/State injection.md
git:
  remote: main
  branch: codex/state-injection-section4-order-20260917
  base_commit: 1398c73d631173a8328bdfb59745c3840f2b8fec
---

# 用户授权与范围

用户明确要求“保持前三节与本地保持一致，把原文第四节的论述顺序改一改，codex直接修改试试”。这是对本次作者与范围的明确指定，优先于 Notes/AGENTS.md 的默认 Pro 路由；由 Codex 直接调整，不启动 Pro。

只重排第四节导言及 §4.1–4.3。先由任意数据与辅助态的 XOR 换元得到测量分支，再从零分支的逐项振幅观察到 c0=c1=1/√2 时保留辅助态，代入资源 U|+〉确认正输入正确；随后检查负输入失配并引入受控 R；最后才定义 s，以统一两输入和两测量记录。§4.4–4.5 及后文不变。

# 本地保留与提交

开始时已有用户未提交修改。编辑前保存本地完整快照，并在编辑后逐字节核验：第四节之前全部一致，§4.4 起至文件末尾全部一致。仅第四节最终文本纳入本次笔记提交；前三节原有修改保留在工作区，不纳入本次提交。

沿用既有 canonical note，不新增前置笔记、不改索引或 canonical。无文献来源、版本、阅读状态、主辅关系、翻译或截图变化。任务目录保留三份工作流记录，核验临时快照在成功推送后删除。不合并 main。

# 完成检查

实际 §4.1–4.3 已通过独立局部数学复核；完整目标的 Obsidian 数学检查通过。本次 diff 与 staged diff 进行空白检查，用户范围外的原样本地编辑不作为本轮修复对象。无新增待核对、TODO：补引用或待补推导。
