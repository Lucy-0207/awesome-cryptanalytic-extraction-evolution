# 贡献指南

欢迎补充论文、代码、勘误与关系证据。新增论文时请在 `data/papers.json` 中补充：题名、年份、稳定链接、会议/状态、预言机、贡献及限制；勿将 arXiv/ePrint 同文不同版本重复计数。新增继承边时请在 `data/relations.json` 填写 `source`、`target`、`relation`、`note`，并尽可能增加 `evidence_url`、页码或章节。

**审稿规则：** 严格区分参数签名、符号、部分层、模块恢复、采样一致率与真正端到端恢复；区分 raw logits、softmax 概率、top-1、梯度/解释、物理侧信道；注明 withdrawn、preprint 和实验额外白盒假设。不上传受版权限制的论文 PDF。

运行 `python scripts/check_catalog.py` 可检查 ID 唯一、关系索引存在及源数据条目数量。
