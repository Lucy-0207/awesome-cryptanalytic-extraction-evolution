# 研究脉络：按问题—方法—瓶颈—突破组织

[返回首页](../README.md) · [全部论文](papers.md) · [继承关系](relationships.md)

## A. 原始输出 ReLU：从边界几何到深层恢复

**背景（2016—2020）**：Tramèr 2016 建立预测 API 模型窃取问题；Jagielski 2020 强调函数保真度；Rolnick & Kording 2020 从 ReLU 激活区域边界逆向理解深层网络。三者是问题与技术背景，**不宜误画成严格算法调用链**。

1. **Carlini et al., CRYPTO 2020** — 建立临界点发现（critical points）→ 签名恢复（signature recovery）→ 符号恢复（sign recovery）→ 逐层重建的密码分析提取框架。问题：符号恢复、深层可见性和数值稳定性。
2. **Canales-Martínez et al., EUROCRYPT 2024** — 继承框架，针对符号枚举复杂度提出 SOE、Neuron Wiggle 等方法，在相应假设下获得多项式时间恢复。问题：多项式复杂度不等于实际低查询成本。
3. **Foerster et al., NeurIPS 2024** — 基于 2020/2024 方案优化实现和实际符号恢复效率，发现其他阶段可能反而成为瓶颈。
4. **Navigating the Deep, EUROCRYPT 2026** — 继续改进深层 ReLU 的临界点筛选、签名归类与端到端流程。
5. **并行优化：Beyond Scalar Probes (2026)** — 借助向量输出的秩一 Jacobian 差与 SVD 改善签名估计；**仅改进一个原语**，不是全网完整攻击。
6. **放宽先验：Without Known Architecture (2026)** — 使用签名模式推断隐藏宽度，但只针对论文研究的 ReLU MLP 条件。

> 源目录另有 **Geometric Critical Point Screening** 与 **Limited Architecture Knowledge** 两篇已撤回预印本，保留在完整目录作为历史文献，不列入现行未撤回成果。

## B. 仅标签 ReLU：从决策边界到复杂度反思

1. **Chen et al., ASIACRYPT 2024** — 原始数值输出不可见，改为通过类别变化定位决策边界并恢复结构信息；受限于可观察事件、规模与效率。
2. **Carlini et al., EUROCRYPT 2025** — 双点签名及新的符号恢复；在给定条件下推进多项式时间仅标签恢复。注意全黑盒端到端与白盒辅助实验的区别。
3. **Extracting Some Layers, LATINCRYPT 2025** — 研究特定条件下部分层与输出层的恢复，不等同于一般端到端算法。
4. **Is the Hard-Label ... Really Polynomial?, CRYPTO 2026** — 质疑过强的复杂度解读，指出 persistent/dead neurons 对可观测性与跨层识别的影响。
5. **Normal Alignment (2026)** — 使用边界法向量与签名对齐改进符号恢复；不是完整网络提取。
6. **Algebraic Hard-Label (2026)** — 用代数签名与聚类改进恢复原语，附带特定 CNN 结构实验。
7. **End-to-End Hard-Label (2026)** — 复用先前几何信息、改进符号恢复，在特定已知架构 MLP 上展示端到端结果；不等价于普遍精确恢复。

## C. 架构扩展：不是一条单向链

- **CNN / 池化**：从平均池化卷积核恢复到 max-pooling 的切换结构，再到部分已知/未知架构与端到端流程。两篇 max-pooling 原始输出论文是平行技术路线，除非有原文明确引用证据，不标为直接继承。
- **激活函数**：ReLU/PReLU/LeakyReLU 保留分段线性泄漏；对 GELU/SiLU 等光滑函数，研究转向 Hessian 曲率与高阶几何。不同原语与假设不能互换。
- **RNN / GNN**：时间共享与消息传递结构为恢复带来不同约束。
- **Attention / GLU**：模块级选择输入、原始输出和规范等价恢复，不等于通过一般 LLM token API 恢复完整模型。

## D. 理论、数值与防御的横向脉络

- **优化与可辨识性**：Expand-and-Cluster (2023/2024) → Data Augmentation (2025) 是明确的方法改进路径；三层精确恢复与有限样本辨识属于相关理论。
- **部分 LLM 恢复**：restricted logprobs/logit-bias 泄露输出投影或子空间，与纯标签 ReLU 参数恢复在预言机上不同。
- **PPML 与侧信道**：有限环/定点推理、物理泄漏、故障注入等攻击者能力不同，需独立分类。
- **有限精度与训练期防御**：检验理想实数 oracle 下的算法在真实舍入、噪声、限流与防御中的可行性。

## 阅读时建议固定回答四个问题

每篇论文至少回答：**继承了什么对象或原语？解决了哪个具体瓶颈？增加/削弱了什么 oracle、架构或数值假设？完成的是参数方向、符号、部分层、函数等价还是端到端网络？**

关系为本仓库的研究性梳理，并非自动生成的精确引用图。详见 [关系判定规则](relationships.md)。
