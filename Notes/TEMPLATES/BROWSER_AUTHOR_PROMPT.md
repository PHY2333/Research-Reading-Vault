使用已连接的 GitHub App 读取以下固定项目快照，并使用 ChatGPT Pro 完成请求中的完整文件写作。

repository: <owner/repo>
branch: <task-branch>
commit: <checkpoint-commit>
request_path: <PRO_REQUEST.md path>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path 和 protocol_path，再读取 request 列出的全部必读材料。请求指定其它固定协议提交时，同时读取该提交中的 protocol_path，按其规定生成本轮外层响应；材料仍以本消息的 commit 为准。

从 request 文件读取 task_id、request_id 和 binding_id。本消息保留 binding_id 的隐藏状态。核对成功后，回复顶部按协议返回绑定区；读取缺项或身份问题按适用协议准确处理。

依据 request 中的读者起点、正文待建立内容、来源支持范围和输出范围，调用 Notes/WRITING_GUIDE.md 的统一标准，自行组织连续、正向的解释。

在同一回复完成 request，并按协议输出所需的全部完整文件。文件内容围栏长于内部围栏；交付包含七反引号协议样例时使用八个反引号作为外层文件内容围栏。

Pro 负责文本交付；本地应用和 Git 写入由 Codex 完成。回复在协议规定的 END_RESPONSE 标记处结束。
