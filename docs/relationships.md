# 论文继承与技术关系

> 关系类别分为 **方法改进 / 技术延伸 / 威胁模型扩展 / 假设审视 / 问题推进**。同一研究主题不自动意味着直接引用。下表首先呈现高度相关的技术承接，但“直接引用或明确声明的前作”需要逐篇查原文确认。

| 上游论文 | 下游论文 | 关系 | 解决或扩展的问题 |
|---|---|---|---|
| [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) | [High Accuracy and High Fidelity Extraction of Neural Networks](https://arxiv.org/abs/1909.01838) | 问题推进 | 从预测 API 窃取到高保真目标 |
| [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526) | 方法改进 | 优化 ReLU 网络符号恢复的复杂度 |
| [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011) | 方法改进 | 重实现并优化经典攻击流水线 |
| [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526) | [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011) | 方法改进 | 改善已有符号恢复的实际效率 |
| [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | [Navigating the Deep: End-to-End Extraction on Deep Neural Networks](https://eprint.iacr.org/2026/296) | 技术延伸 | 改进深层 ReLU 端到端恢复 |
| [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | [Beyond Scalar Probes: Exploiting Vector-Valued Outputs in ReLU Networks For Signature Extraction](https://arxiv.org/abs/2609.35487) | 技术延伸 | 改进 Jacobian 签名估计原语 |
| [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403) | 威胁模型扩展 | 从原始输出转向仅标签决策边界 |
| [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403) | [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) | 方法改进 | 双点签名和条件化多项式时间恢复 |
| [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) | [Is the Hard-Label Cryptanalytic Model Extraction Really Polynomial?](https://eprint.iacr.org/2025/1868) | 假设审视 | 持久/死亡神经元影响复杂度结论 |
| [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) | [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751) | 技术延伸 | 法向对齐改进符号判定 |
| [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) | [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/abs/2609.21941) | 技术延伸 | 组合前序恢复原语与新符号恢复 |
| [Delving into Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2025/1970) | [Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2026/1066) | 技术延伸 | 放宽硬标签 PReLU 斜率及结构条件 |
| [Provably Learning Attention with Queries](https://arxiv.org/abs/2601.16873) | [Provably Learning Multi-Head Attention with Queries](https://arxiv.org/abs/2608.03294) | 技术延伸 | 从注意力查询学习拓展至多头 |
| [Expand-and-Cluster: Parameter Recovery of Neural Networks](https://arxiv.org/abs/2304.12794) | [Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries](https://arxiv.org/abs/2511.20312) | 方法改进 | 数据增强改善过参数化学生网络的聚类恢复 |

## 如何判定“继承”

1. **明确继承**：正文写明采用/改进某个方法，并有直接引用（需逐篇查验方法与 Related Work）。
2. **技术延伸**：借鉴相同原语或扩大任务条件，但尚未核实严格算法依赖。
3. **平行路线**：相同对象下独立解决不同子问题，不画有向直接继承箭头。
4. **假设审视**：后作分析前作定理或实验隐含前提，不必采用同一算法。

**当前状态**：上述表格是技术关系索引，尚未完成逐篇论文的引用核验，因此不标注“确认直接引用”。若有一手证据，请在数据中增加 `evidence_url` 和章节。
