# Final report

- task_id: 20260915-state-injection-controlled-r-motivation
- route: codex-only，用户明确授权
- status: DONE
- branch: codex/state-injection-r-motivation-20260915
- target_files: Notes/04-Magic State Injection/State injection.md
- checks: pass; 实际段落独立数学复核、Obsidian 数学检查及 git diff --check
- merge_to_main: not performed

将原位受控 R 的动机接入 §3 的主线：先考察无补偿的候选线路，使用 §3.1 测量规则，比较两个 X 基输入的零测量分支。正输入已正确，负输入得到 ZU 而目标是 UZ，因此只在负输入分支预处理辅助资源。随后引入相干受控 R 并接回原有 K_m、分支振幅与 R 约束推导；解释一般不能无条件补偿、不能以数据 X 测量替代相干控制，以及对角 U 可取 R=I。

改动放在首次引入 R 之前，使门的作用先于形式定义出现。不新增前置笔记、不改索引或 canonical、不改文献管理信息，无翻译和截图。新任务目录保留三份记录，原任务目录保留，无临时响应。已有 §1.2 和 §2.1 修改完整保留为未提交状态，不纳入本次提交。

无待核对、TODO：补引用或待补推导。任务分支的 Git 提交保存本轮精确变更。
