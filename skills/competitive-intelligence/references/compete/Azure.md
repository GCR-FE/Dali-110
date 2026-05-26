---
title: Azure 中国（21Vianet 运营）竞争分析
type: compete
competitor: azure-china
sources:
  - raw/CI Database/Azure中国地域竞争概览-Compete Overview.pdf
  - raw/CI Database/Azure Compete Guide.pdf
  - raw/CI Database/AWS中国地域相对本土友商的竞争优势 - Compete Battlecard.pdf
last_updated: 2026-05-13
data_as_of: 2026-03-18
status: stable
tags: [compete, azure, china, 21vianet, microsoft]
internal_only: true
---

# Azure 中国（由世纪互联运营）竞争分析

> ⚠️ **CI 内部使用条款**：仅限 AWS 内部使用。与客户沟通保持客观，对比数据**仅限 1对1 口头**引用。

---

## TL;DR — 三句话讲完 Azure 中国

1. **市场地位**：由世纪互联（21Vianet）运营，2014 年商用，5 个区域；2025H1 IDC 数据：AWS 中国在 IaaS+PaaS 市场份额都领先 Azure；Gartner 2025 SCPS MQ 中 AWS 排名亦高于 Azure。
2. **核心弱点**：**北 1 / 东 1 区域 2026 年 7 月 1 日强制退役**（巨大打击点）+ **运营团队收缩**（Wicresoft 撤出中国）+ **跨境延迟约全球 region 的 3 倍** + **Azure OpenAI 仅限企业申请** + **Microsoft Sentinel 2026 年 8 月退休** + **不支持 Spot 实例**。
3. **AWS 切入点**：稳定持续投资 + 本地团队规模 + 强制迁移痛点（捆绑 MAP 资金 + 现代化机会） + 摆脱 Microsoft 许可锁定（Database Freedom + OLA） + GenAI 模型多样性（Bedrock vs OpenAI 单选）。

---

## 1. Azure 中国 12 年时间轴

| 年份 | 事件 |
|---|---|
| 2012-11 | 微软与世纪互联签署协议，计划合作运营 Azure 公有云 |
| 2014-03 | Azure 中国正式商用，覆盖**北 1 / 东 1** |
| 2014-04 | Office 365 落地中国 |
| 2018-03 | 北京/上海各新增 1 个区域（**北 2 / 东 2**）|
| 2019-05 | Dynamics 365 落地中国（"三朵云"齐聚）|
| 2021-03 | 侯阳接替柯睿杰任微软大中华区董事长 |
| 2022-03 | **北 3 区域**正式启用（张家口）|
| 2023-07 | **新商务模式 21VCA-E** 商用 |
| **2025-05** | **微软通知客户：北 1 / 东 1 于 2026/7/1 起停服** |

> **关键销售时机**：北 1/东 1 客户被迫迁移——这是 AWS 切入的**最大窗口期**。

[来源: Azure中国地域竞争概览.pdf · Page 5]

---

## 2. Azure 中国客户画像

### 2.1 谁在用 Azure 中国

| 类型 | 特点 |
|---|---|
| **跨国企业在华业务（MNC China Operations）** | 总部统一 IT 策略要求用 Azure，中国区落地执行 |
| **微软生态深度用户** | 重度依赖 .NET / SQL Server / Dynamics 365 |
| **受监管行业头部客户** | 外资银行、合资汽车制造、跨国医药研发中心 |

### 2.2 决策链特征

- **CIO / IT 总监主导**
- 通常由 IT 部门基于合规或微软协议**统一采购**
- 业务部门话语权较弱

### 2.3 ⚠️ Azure 客户的 5 大痛点信号（销售要主动挖掘）

| 痛点 | 描述 | AWS 切入话术 |
|---|---|---|
| **1. 区域退役压力** | 北 1 / 东 1 强制迁移时间表 | "既然要迁，何不评估更稳定的平台？" |
| **2. AI 服务企业准入限制** | Azure OpenAI **仅限企业客户申请** | Bedrock 任何客户都可用，模型多样性更好 |
| **3. 跨境网络延迟瓶颈** | 比全球 region 高约 **3 倍** | AWS 全球 region + 中国双 region 一致体验 |
| **4. 关键服务 Gap** | **不支持 Spot 实例**；**Microsoft Sentinel 2026/8 退休** | Spot 节省 70-90% 成本；Security Lake / GuardDuty 替代 |
| **5. EA 续签锁定感** | 续签时感到技术绑定和商务僵化 | AWS 灵活定价模式 + Database Freedom |

[来源: Azure中国地域竞争概览.pdf · Page 6]

---

## 3. 中国区基础设施对比（最具杀伤力的章节）

### 3.1 区域对比

| 维度 | AWS 中国 | Azure 中国 |
|---|---|---|
| **区域数量** | 2（BJS 2014 + ZHY 2017）| 5（北 1/东 1/北 2/东 2/北 3）|
| **多 AZ 区域** | **全部 2 个** | **仅北 3 1 个** |
| **AZ 数量** | 每个 region **至少 3 个** | 大多区域**单 AZ** |
| **容量状况** | 充足 | **除北 3 外，4 个区域都面临容量限制** |
| **AZ 定义透明度** | 官方明确发布（100km 内、冗余光纤、加密同步）| **没有 AZ 距离描述** |
| **整合风险** | 无 | **存在区域进一步整合的风险** |

### 3.2 强制迁移的销售故事

> **2025-05** 微软通知北 1/东 1 客户：**2026/7/1 起停服**

**对客户意味着什么**：
- 跨区域迁移（北 1 → 北 3）**技术复杂度接近全新部署**
- 不同区域间存在**服务可用性差异**（某些 AI 服务、数据库 SKU 在不同区域支持程度不同）
- 网络架构、安全配置需要**重新规划**
- 应用依赖关系需要**重新验证**

> **销售话术**："既然要花 6-12 个月做大规模迁移，何不一次评估清楚——是迁到北 3 继续踩坑，还是迁到一个**稳定持续投资**、**多 AZ 默认**、**全球一致**的平台？"

### 3.3 各区域服务部署不一致

例如：
- 较新代次的实例 **Daldsv6** 仅在北 2/东 2/东 3 可用
- 较新代次的实例 **Ddsv6** 仅在北 3 可用

> 客户做架构选型时要在区域之间反复对照——**复杂度高，错配风险大**。

[来源: Azure中国地域竞争概览.pdf · Pages 11-12]

---

## 4. 商务模式：21VCA-E（新模式）vs OSPA（旧模式）

### 4.1 21VCA-E 是什么

2023 年 7 月商用的新商务模式，统一 portal.azure.cn 体验，新增成本管理 + 计费功能。

**支持 RI / Savings Plans 的服务**：
| 类型 | 服务 |
|---|---|
| **预留 RI** | Cosmos DB、MySQL、PostgreSQL、Redis、SQL DB、SQL MI、应用服务、虚拟机、Databricks、Synapse、Data Factory v2、ADX、备份、存储、Defender、AI Search |
| **Savings Plan** | 容器实例、应用服务、虚拟机、函数、容器应用 |

### 4.2 21VCA-E vs OSPA 关键差异

| 维度 | OSPA（旧）| 21VCA-E（新）|
|---|---|---|
| **协议期** | 3 年合同，**到期续签** | 单次签约，**无到期日** |
| **合作伙伴** | 1 个 deal package 对应 1 个合作伙伴 | 允许多个合作伙伴采购 |
| **产品覆盖** | 4 个 deal package（Azure / O365 / D365 / PP）| 1 个合同覆盖多产品（当前阶段仅 Azure）|
| **条款** | 自定义 T&C | **模块化 + 数字化**附加条款 |

### 4.3 价格对比（含税）

| 对比 | 倍数关系 |
|---|---|
| **AWS BJS** vs Azure 东 2/北 2/北 3 | AWS 1.0 : Azure 1.64 |
| **AWS ZHY** vs Azure 东 2/北 2/北 3 | AWS 1.0 : Azure 1.07 |
| **AWS NURI** vs Azure CPP（旧 RI）| AWS 1.0 : Azure 1.74 |
| **AWS NURI** vs Azure RI | AWS 1.0 : Azure 1.14 |

> **结论**：BJS 比 Azure 北/东区域**便宜 64%**；ZHY 仍便宜 7%。

[来源: Azure中国地域竞争概览.pdf · Pages 8-9]

---

## 5. 服务对标 — 关键陷阱

### 5.1 计算实例 mapping

| 不要这样做 | 应该这样做 |
|---|---|
| 只看 vCPU + RAM | **结合 CPU 代次** mapping |
| AWS C/M/R 系列 | Azure F/D/E 系列 |
| AWS R5(1:8) | Azure Ev4/Esv4 |
| AWS R6i(1:8) | Azure Ev5/Esv5 |
| AWS M5(1:4) | Azure Dv4/Dsv4 |
| AWS M6i(1:4) | Azure Dv5/Dsv5 |
| AWS C5(1:2) | Azure Fsv2 |
| AWS C7i(Sapphire Rapids) | Azure Dlsv5 |

> **陷阱**：不要用 Azure 带 local storage 的实例 mapping AWS 不带 local storage 的实例（如 i4i.2xlarge ≠ L8sv3 - 这是错的）。

### 5.2 对象存储

| 服务 | 价格（¥/GB/月）|
|---|---|
| Azure Blob Hot ZRS | 0.250 |
| Amazon S3 Standard @BJS | 0.195 |
| Amazon S3 Standard @ZHY | 0.175 |
| Azure Blob Hot LRS | 0.140 |

> Azure LRS（单数据中心，仅 3 副本）比 AWS 便宜，但**抵御区域性灾难能力最弱**——对比要看冗余级别。

### 5.3 块存储：Azure Premium SSD 的陷阱

| 维度 | AWS gp3 | Azure Premium SSD v2 |
|---|---|---|
| 最大 size | 16 TB | 64 TB |
| 最大 IOPS | 16,000 | 80,000 |
| 最大吞吐 | 1000 MB/s | 1200 MB/s |
| Latency | < 10 ms | **< 1 ms** |
| **持久性** | **3 个 9** | **11 个 9** |
| **支持 OS 盘** | **是** | **否** |
| **可用区域** | 全部 | **仅北 3** |

> Azure Premium SSD 仅支持**固定大小**（如 P20=512GB），**性能与容量绑定** → 客户为了 IOPS 不得不买更大磁盘 = **存储浪费**。

### 5.4 限时折扣陷阱

某些短期限时调价直接显示在 azure.cn 价格计算器中，**未附促销说明**——客户误以为是持续价格。

[来源: Azure中国地域竞争概览.pdf · Pages 17-20]

---

## 6. 1-Pager 差异化要点（高层对话用）

| 维度 | AWS | Azure | Reference |
|---|---|---|---|
| **市场份额** | 全球第一 | 全球第二 | Gartner 2025 MQ；IDC 2025H1 中国 IaaS+PaaS AWS 领先 |
| **长期运营承诺** | 稳定持续投资 | **多次调整导致客户被迫迁移** | 2025/5 北 1/东 1 退役通知；2023 年北 2/东 2 容量限制要求迁北 3 |
| **中国区本地团队** | 人数上千 | **支持团队撤出信号** | Microsoft venture **Wicresoft** to halt China operations |
| **基础设施稳定性** | 故障数最少 | 故障风险较高 | Frost & Sullivan《What Determines Cloud Resilience》 |
| **R&D / AI 投入** | 持续高于微软 | 低于亚马逊 | CNBC 25/10/31：AWS 2025 AI CapEx $125B（前为 $118B），微软 FY26 CapEx $94B+ |

[来源: Azure中国地域竞争概览.pdf · Page 22]

---

## 7. 三大客户异议 + 标准话术

### 7.1 异议一：区域退役顾虑

**客户说**：
> "我们收到了 Azure 北 1/东 1 退役通知，但迁移太麻烦了，我们想尽量拖到最后再看。"
>
> "担心换云风险大，毕竟在 Azure 上跑了几年了。"

**AWS 回应**：
> "完全理解。Azure 中国跨区域迁移（北 1 → 北 3）**技术复杂度接近全新部署**：服务可用性差异、网络架构、安全配置、应用依赖都要重新做。
>
> 既然如此，何不借此机会评估云平台选择？AWS 可以提供：
> - **Migration Evaluator**：免费迁移评估，量化 TCO 对比
> - **MAP 资金**：迁移补贴
> - **架构现代化机会**：消除 Windows Server / SQL Server 许可依赖（容器化 + 开源替代）；优化性能（Graviton 等新实例）
>
> AWS MAP 已帮助数千家企业完成类似迁移，包括从 Azure 迁移的成功案例（**麦当劳中国**）。"

### 7.2 异议二：微软生态依赖

**客户说**：
> "我们全是 Windows Server 和 SQL Server，用 Azure 肯定兼容性最好，原厂支持最放心。"

**AWS 回应**：
> - "AWS **运行 Windows 的历史比 Azure 还早**——我们从 **2008 年**就开始支持 Windows Server，比 Azure **早了近两年**。
> - **更关键的是 AWS 提供摆脱许可锁定的路径**：
>   - **Database Freedom Program**：从商业数据库迁移到开源方案，技术 + 资金双支持
>   - **AWS OLA**（Optimization and Licensing Assessment）：识别许可优化机会
> - 真正实现技术选择的自由，不再被单一厂商绑定。"

### 7.3 异议三：AI / OpenAI 创新

**客户说**：
> "我们看重 Azure 的 OpenAI 能力，未来想做大模型应用。"

**AWS 回应**：
> "OpenAI 确实不错，但**您是否考虑过模型多样性**？
> - AWS Bedrock 支持 **Claude, Llama, Titan, Nova, Mistral** 等多种顶级模型
> - **数据隐私保护更严格**——你的 prompt/数据不会用于训练
> - 你可以根据业务场景**灵活切换模型**，而不是被锁在 GPT 这一个选项上
> - **Azure OpenAI 仅限企业客户申请**，准入门槛和等待周期都比 Bedrock 高"

### 7.4 异议四：折扣价格

**客户说**：
> "微软给了我们 EA 协议，算下来折扣很深，AWS 能匹配吗？"

**AWS 回应**：
> "**折扣只是冰山一角**，建议做一个 3 年 TCO 详细测算：
>
> **定价层面**：
> - AWS 宁夏与 Azure 北/东区域**基本持平**，某些服务（计算+存储）AWS **更具优势**
> - AWS 中国提供 **Spot 实例**节省 70-90%，**Azure 中国不支持 Spot**
>
> **Azure 隐形成本**：
> - 用 **Azure Hybrid Benefits** 把本地许可证迁上云，必须有 **SA（软件保障）**
> - SA 年费约许可证价格的 **25-30%**（Windows 25%，SQL Server 30%）
> - **3 年 EA 周期内**：实际为 SQL Server 支付的总成本达到许可证价格的 **1.9 倍**，Windows Server 达到 **1.75 倍**
> - 这些持续许可成本**必须纳入 TCO 对比**"

[来源: Azure中国地域竞争概览.pdf · Page 24]

---

## 8. 给 Dawei 的 4 条实战提醒

1. **北 1/东 1 退役是黄金窗口**：直接 SQL 客户名单，找出 Azure 北 1/东 1 用户，**主动出击**——他们已经在被迫做迁移决策
2. **MNC 中国客户是难啃的硬骨头**：总部统一 IT 策略卡死了。突破口是**业务部门出海/AI 创新**——绕过 IT 决策链
3. **价格对话要看 Total Cost**：别被 Azure 表面的低价或 EA 折扣吓住——SA 成本 + 限时折扣陷阱 + 持续许可费用，3 年下来 TCO 差距可能 60%+
4. **AI 创新是核武器**：客户讨论 GenAI 时，**模型多样性 + Bedrock 准入零门槛** 是 Azure OpenAI 的死穴

---

## 9. 进一步资料（CI 高 spot 资源）

| 类别 | 内容 |
|---|---|
| Commercial | Microsoft Azure - GTM and Commercial Structure Compete Briefing |
| Service | Mastering Cloud Differentiation: AWS and Azure |
| Service | Why Customers Choose AWS（Call High 维度）|
| Service | Competing with Microsoft Azure（典型打法）|
| Service | MSFT Azure Compete（综合产品对比）|
| Service | EC2 vs Azure VM Compete Battlecard |
| Infra | Global Infrastructure Compete Battlecard |
| Service Avail | Product Availability by Region（公开）|
| Cost | Azure Pricing Calculator（公开）|
| Service | Azure VM size and series naming（公开）|
| Service | 中国区 Azure Playbook |

需要 Strategic Deal Support 时通过 SpecReq 开 compete case，CI SA / BDM 1:1 支持。

---

## 关联页面

- [[Compete/AliCloud]] — 阿里云
- [[Compete/Huawei]] — 华为云
- [[Battlecards/AWS-vs-Local-CSP-China]] — 中国本土友商整合
- [[Methodology/MEDDPICC-2026]] — Co (Competition) 字段评估

---

*v1.0 — 2026-05-13 整理自 Azure 中国地域竞争概览（数据截止 2026-03-18）*
