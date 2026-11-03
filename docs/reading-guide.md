# 阅读路线与术语说明

## 三条入门路径

**结构逆向：** Rolnick 2020 → Carlini 2020 → EUROCRYPT 2024 → Navigating the Deep 2026。

**仅标签：** Chen 2024 → EUROCRYPT 2025 → CRYPTO 2026 → Normal Alignment / End-to-End 2026。

**实际攻击与部署假设：** Foerster 2024 → Finite-Precision 2026 → Output Rounding 2026 → Train to Defend 2025。

## 术语

- **Raw outputs**：完整实值输出或 logits；不等同于仅访问 softmax 概率，更不同于只拿 top-1 标签。
- **Soft label**：通常指概率向量；可能含截断、top-k、温度或舍入。请逐篇核对 oracle。
- **Hard label**：通常指 top-1 分类结果。
- **Signature**：神经元权重方向及相关相对信息，往往存在比例、符号与排列歧义。
- **Sign recovery**：消除权重方向符号不确定性的一步，不等于整体恢复。
- **Polynomial time**：依赖论文明确前提；必须同时评估实际查询、运行时间、精度与失败条件。
- **Exact / functional equivalence**：还需考虑缩放、排列等网络对称性；样本集上高一致率不证明全输入等价。

建议每篇笔记固定格式：问题 → 前作的限制 → 本文关键原语 → 访问条件 → 恢复对象 → 证明与实验边界 → 仍未解决的问题。
