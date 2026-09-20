使用已连接的 GitHub App 读取以下固定项目快照，并在全新的 ChatGPT Pro 会话中完成独立全文审查。

repository: <owner/repo>
branch: <task-branch>
commit: <review-checkpoint-commit>
request_path: <REVIEW_REQUEST.md path>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path、protocol_path、同任务的 PRO_REQUEST.md 和 TASK.md，再读取审查请求及原始请求指定的完整候选、统一标准和必要来源。请求指定其它固定协议提交时，同时读取该提交中的 protocol_path，以其生成本轮外层响应。

从本轮 REVIEW_REQUEST.md 读取 task_id、request_id 和 binding_id。本消息保留 binding_id 的隐藏状态。绑定和材料缺项按适用协议处理。

以固定 commit 的实际文件为审查对象，按照 Notes/WRITING_GUIDE.md 连续阅读：先确认原始目标、数学信息与理解主线，再根据实际影响修订。已清楚、准确且连续的内容保持；纯格式问题由 Codex 在应用层处理。

实质内容通过时按协议返回 REVIEW_PASS；需要修订时返回 COMPLETE 和全部受影响目标的完整修正版。文件内容围栏长于内部围栏；包含七反引号协议样例时使用八个反引号作为外层文件内容围栏。

Pro 负责审查与文本交付；本地应用和 Git 写入由 Codex 完成。回复在协议规定的 END_RESPONSE 标记处结束。
