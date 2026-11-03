# 全部文献索引（55 篇）

> 以研究分支检索的完整文献清单；主要阅读顺序参见 [README](../README.md) 与 [技术演进](evolution.md)。年份以源目录记录的归档/报告年份为基础，会议见单独列。

**引用来源：** [springli07/awesome-cryptanalytic-extraction](https://github.com/springli07/awesome-cryptanalytic-extraction/blob/main/README_zh-CN.md)。本仓库为独立的技术演进视角重编，不声称完整核验每篇论文版本。

## 基础工作（3 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2016 | [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) | USENIX Security 2016 | prediction API | 模型窃取与方程求解早期研究 |
| 2019 | [Reverse-Engineering Deep ReLU Networks](https://arxiv.org/abs/1910.00744) | ICML 2020 | real-valued queries | 利用 ReLU 分段线性边界几何逆向恢复网络 |
| 2019 | [High Accuracy and High Fidelity Extraction of Neural Networks](https://arxiv.org/abs/1909.01838) | USENIX Security 2020 | raw outputs / predictions | 区分高准确率与高保真度提取 |

## 原始输出 ReLU 主线（8 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2020 | [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) | CRYPTO 2020 | raw outputs | 临界点、签名、符号与逐层恢复的经典流程 |
| 2023 | [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526) | EUROCRYPT 2024 | raw outputs | SOE 与 Neuron Wiggle 等多项式符号恢复 |
| 2024 | [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011) | NeurIPS 2024 | raw outputs | 优化符号恢复实际性能并识别整体瓶颈 |
| 2026 | [Navigating the Deep: End-to-End Extraction on Deep Neural Networks](https://eprint.iacr.org/2026/296) | EUROCRYPT 2026 | raw outputs | 优化深层 ReLU 端到端恢复流程 |
| 2026 | [Beyond Scalar Probes: Exploiting Vector-Valued Outputs in ReLU Networks For Signature Extraction](https://arxiv.org/abs/2609.35487) | Preprint | raw vector outputs | 秩一 Jacobian 差与 SVD 签名估计；非完整攻击 |
| 2026 | [Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption](https://arxiv.org/abs/2609.14379) | Preprint | raw outputs | 利用签名模式推断未知架构 ReLU MLP 隐藏宽度 |
| 2026 | [Geometric Critical Point Screening: Clustering-Free Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2026/1025) | Withdrawn 2026-09-19 | raw outputs | 撤回历史记录；临界点几何筛选 |
| 2026 | [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Limited Architecture Knowledge Setting](https://eprint.iacr.org/2026/2127) | Withdrawn 2026-10-01 | raw logits | 撤回历史记录；有限架构先验下的恢复 |

## 仅标签 ReLU 主线（7 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2024 | [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403) | ASIACRYPT 2024 | top-1 label | 基于决策边界几何的仅标签提取 |
| 2024 | [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) | EUROCRYPT 2025 / Journal of Cryptology 2026 | top-1 label | 双点签名、符号恢复与条件化多项式性 |
| 2025 | [Extracting Some Layers of Deep Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2025/1118) | LATINCRYPT 2025 | top-1 label | 在结构条件下恢复部分层而非无条件全网 |
| 2025 | [Is the Hard-Label Cryptanalytic Model Extraction Really Polynomial?](https://eprint.iacr.org/2025/1868) | CRYPTO 2026 | top-1 label | 死亡/持久神经元与跨层恢复、复杂度假设审视 |
| 2026 | [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751) | Preprint | top-1 label | 法向量对齐改进符号恢复；非完整攻击 |
| 2026 | [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](https://eprint.iacr.org/2026/1164) | Preprint | top-1 label | 代数签名与聚类；涵盖部分 max-pooling CNN 实验 |
| 2026 | [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/abs/2609.21941) | Preprint | top-1 label | 复用几何信息改进符号恢复并展示特定 MLP 端到端结果 |

## CNN 与池化扩展（5 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Convolutional Neural Networks](https://eprint.iacr.org/2026/139) | ACISP 2026 | top-1 label | 利用卷积共享结构提取平均池化 CNN |
| 2026 | [Algebraic Attack on Convolutional Neural Networks with Max Pooling](https://eprint.iacr.org/2026/241) | CRYPTO 2026 | raw outputs | 以代数技术处理 max-pooling 切换 |
| 2026 | [Model Extraction of Convolutional Neural Networks with Max-Pooling](https://eprint.iacr.org/2026/464) | ToSC 2026 | raw outputs | 利用池化信息和感受野结构 |
| 2026 | [End-to-End Polynomial-Time Cryptanalytic Extraction of Convolutional Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/902) | Preprint | top-1 label | 已知架构等条件下平均池化 CNN 端到端流程 |
| 2026 | [Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting](https://arxiv.org/abs/2609.27427) | Preprint | raw outputs / top-1 labels | 由已恢复向量的空间结构推断 CNN 架构 |

## 激活函数扩展（4 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2025 | [Delving into Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2025/1970) | ASIACRYPT 2025 | raw outputs / top-m probabilities | PReLU 权重与斜率恢复 |
| 2026 | [Cryptanalytic Extraction of Neural Networks with Various Activation Functions](https://eprint.iacr.org/2026/178) | ToSC 2026 | variant-dependent | 推广至 PReLU/LeakyReLU/HardTanh/Step 等 |
| 2026 | [Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2026/1066) | Preprint | top-1 label | 放宽 PReLU 硬标签提取的斜率与结构限制 |
| 2026 | [Cryptanalytic Extraction of Deep Neural Networks with Non-Linear Activations](https://eprint.iacr.org/2026/253) | CRYPTO 2026 | raw outputs | 高阶与近线性几何研究非线性激活恢复 |

## RNN 与 GNN 扩展（2 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2026 | [Beyond Feedforward Networks: Cryptanalytic Extraction of RNNs](https://eprint.iacr.org/2026/168) | Preprint | raw outputs / top-1 labels | 利用时间展开与循环参数共享 |
| 2026 | [Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/719) | Preprint | top-1 label | 图消息传递结构下的条件化提取 |

## 注意力与 GLU 扩展（5 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2026 | [Provably Learning Attention with Queries](https://arxiv.org/abs/2601.16873) | ICML 2026 | chosen real-valued queries | 注意力模块查询学习理论 |
| 2026 | [Provably Learning Multi-Head Attention with Queries](https://arxiv.org/abs/2608.03294) | Preprint | chosen real-valued queries | 由单头相关结果扩展到多头注意力 |
| 2026 | [Cryptanalytic Extraction of Multi-Head Softmax Attention Models](https://eprint.iacr.org/2026/1678) | Preprint | raw outputs / chosen inputs | 规范等价意义下的多头 softmax attention 恢复 |
| 2026 | [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631) | Preprint | isolated module oracle | 对踵输入分离孤立无偏置 GLU 模块 |
| 2026 | [Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks](https://arxiv.org/abs/2608.28843) | Preprint | chosen FFN internal inputs | Hessian 曲率估计 GELU/SiLU FFN 首层方向，非完整 Transformer |

## LLM 部分恢复（2 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2024 | [Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) | ICML 2024 | restricted logprobs / logit-bias | 恢复 LLM 输出投影的部分结构 |
| 2024 | [Logits of API-Protected LLMs Leak Proprietary Information](https://arxiv.org/abs/2403.09539) | COLM 2024 | restricted logprobs | 泄露输出空间与隐藏维度信息 |

## PPML 与侧信道（6 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2018 | [CSI Neural Network: Using Side-channels to Recover Your Artificial Neural Network Information](https://arxiv.org/abs/1810.09076) | USENIX Security 2019 | power / EM | 物理侧信道恢复模型结构与信息 |
| 2020 | [SNIFF: Reverse Engineering of Neural Networks with Fault Attacks](https://arxiv.org/abs/2002.11021) | IEEE Transactions on Reliability | fault injection | 故障注入泄漏参数信息 |
| 2024 | [A Divide-and-Conquer Strategy for Hard-Label Extraction of Deep Neural Networks via Side-Channel Attacks](https://eprint.iacr.org/2024/1870) | TCHES 2026 | labels + side channel | 物理泄漏辅助的分治提取；不等同纯仅标签 |
| 2025 | [Activation Functions Considered Harmful: Recovering Neural Network Weights through Controlled Channels](https://arxiv.org/abs/2503.19142) | Preprint | SGX controlled channels | 利用受控侧信道恢复部分神经网络参数 |
| 2026 | [Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning](https://eprint.iacr.org/2026/848) | Preprint | fixed-point / finite ring inference | 在隐私保护推理实现下研究提取 |
| 2026 | [Extraction meets Distillation - cryptanalytic techniques to recover parameters from a Deep Neural Network](https://arxiv.org/abs/2610.33671) | Preprint | privileged intermediate information | 内部信息辅助的参数恢复与蒸馏重建，不是纯黑盒 |

## 有限精度与防御（3 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2025 | [Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks](https://arxiv.org/abs/2509.16546) | NeurIPS 2025 | defense | 训练时约束以降低参数提取风险 |
| 2026 | [Finite-Precision Error Analysis of Cryptanalytic Model Extraction](https://eprint.iacr.org/2026/1943) | Preprint | finite-precision raw outputs | 分析密码分析原语对有限精度误差的敏感性 |
| 2026 | [Output Rounding Is Not a Free Defense Against Cryptanalytic Neural Network Extraction](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | MIT course report 2026 | rounded raw outputs | 输出舍入及适应性攻击的小模型实验 |

## 相关理论与替代恢复（8 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2018 | [Model Reconstruction from Model Explanations](https://arxiv.org/abs/1807.05185) | FAT* 2019 | explanation / gradient | 梯度解释预言机强于普通预测 API |
| 2021 | [An Exact Poly-Time Membership-Queries Algorithm for Extraction a three-Layer ReLU Network](https://arxiv.org/abs/2105.09673) | ICLR 2023 | membership queries | 特定三层 ReLU 网络的多项式查询恢复 |
| 2022 | [Finite Sample Identification of Wide Shallow Neural Networks with Biases](https://arxiv.org/abs/2211.04589) | Preprint | finite samples | 宽浅层有偏置网络的有限样本可辨识性 |
| 2023 | [Reverse Engineering Deep ReLU Networks An Optimization-based Algorithm](https://arxiv.org/abs/2312.04675) | Preprint | input-output queries | 基于优化的 ReLU 网络逆向工程 |
| 2023 | [Expand-and-Cluster: Parameter Recovery of Neural Networks](https://arxiv.org/abs/2304.12794) | ICML 2024 | input-output samples | 过参数化学生网络与聚类恢复 |
| 2024 | [Model Stealing for Any Low-Rank Language Model](https://arxiv.org/abs/2411.07536) | Preprint | conditional queries | 低秩语言模型分布学习，不是通用 Transformer 权重恢复 |
| 2024 | [Provably learning a multi-head attention layer](https://arxiv.org/abs/2402.04084) | STOC 2025 | random examples | 样本学习条件下多头注意力层可恢复性 |
| 2025 | [Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries](https://arxiv.org/abs/2511.20312) | UniReps 2025 | input-output samples | 通过数据增强改进 Expand-and-Cluster |

## 综述（2 篇）

| 年份 | 论文 | 会议/状态 | 访问条件 | 研究贡献与边界 |
|---|---|---|---|---|
| 2025 | [A Systematic Survey of Model Extraction Attacks and Defenses: State-of-the-Art and Perspectives](https://arxiv.org/abs/2508.15031) | Survey | multiple | 广义模型窃取攻击与防御综述 |
| 2025 | [A Survey on Model Extraction Attacks and Defenses for Large Language Models](https://arxiv.org/abs/2506.22521) | Survey | multiple | LLM 模型提取攻击与防御综述 |

