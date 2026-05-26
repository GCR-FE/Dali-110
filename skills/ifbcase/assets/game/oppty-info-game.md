# 商机情报 - GAME

> 此文档面向 Account Team & Manager，所有人可见。
> 内容来源：基于 `Dummy Case/ai-opportunities/Game - 腾讯游戏/` 下的 OP-*.md 与 README.md 合并整理。
> 客户：**腾讯游戏**

---

## 商机矩阵速览


### Gio · 业务类商机（3 条）

| # | Opportunity | Stage | EB | PPT 关键出处 |
|---|---|---|---|---|
| [OP-01](./OP-01-AI-NPC实时自由对话.md) | AI NPC 实时自由对话系统 | Qualified | Gloria（已识别） | Slide 7 DeepSeek 接入 + Slide 24/29 NPC 节 + Slide 29 紫色字 KPI |
| [OP-02](./OP-02-全球AI实时翻译与本地化.md) | 全球上线的 AI 实时翻译与本地化 | Prospect | 未识别 | Slide 24/29 翻译方向 + Slide 4 海外 + Slide 5 Intl SDK 战略 |
| [OP-03](./OP-03-玩家舆情分析与个性化推荐.md) | 玩家舆情分析与个性化推荐 | Prospect | 未识别 | Slide 24/29 舆情与推荐节 + Slide 29 紫色字 KPI + Slide 6 长青游戏战略 |

### Garman · 技术类商机（3 条）

| # | Opportunity | Stage | EB | PPT 关键出处 |
|---|---|---|---|---|
| [OP-04](./OP-04-AIBOT陪玩系统基础设施.md) | AIBOT 陪玩系统训练与推理基础设施 | Qualified | Gloria（已识别） | Slide 25/30 AIBOT 部门业务 + Slide 30 紫色字 3 条成本 KPI + AWS Graviton 适配 |
| [OP-05](./OP-05-多智能体强化学习训练平台.md) | 多智能体强化学习训练平台 | Qualified | 候选待确定（Gloria / Gabriel） | Slide 25/30 MARL 节 + Slide 30 紫色字 75% 拟真 + Slide 7 智能体决策训练 |
| [OP-06](./OP-06-大模型部署与成本优化.md) | 大模型部署与成本优化 | Prospect | 未识别 | Slide 25/30 成本节 + Graviton + Spot 已有适配 + Slide 29 Gio 侧部署成本 -50% |


---

# OP-01 — AI NPC 实时自由对话系统

**类型：业务商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — AI NPC Real-Time Dialog System | — |
| **Stage** | Qualified | — |
| **Expected Closing Date** | 2027 Q1 | — |
| **Expected Revenue (ARR)** | US$ 5M *（培训模拟值）* | — |
| **Solution Products** | Amazon Bedrock + Amazon SageMaker + AWS Graviton | — |
| **M — Metrics** | NPC 对话满意度评分 +40%；玩家与 NPC 互动时长 +35%；游戏沉浸感评分 +25% | Slide 29 Gio Manager Coach 紫色字 KPI |
| **E — Economic Buyer** | **Gloria** — Tech & Engineering VP（Gio 直属汇报对象） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | 某 FPS 作为首款接入 DeepSeek 大模型的手游成为行业案例；"游戏正在成为 AI 最好的训练场"；推理并发至少数百个 NPC 同时运行 | Slide 7 行业趋势 + Slide 24/29 NPC 系统 |
| **CH — Champion** | **Gio** — AI 算法中心高级经理（NLP + 国际知名 AI 研究实验室研究科学家背景） | Slide 24 / 29 Persona 原文 |
| **CP — Competition** | G-Cloud 内部云（享"成本价"，Slide 2）；DeepSeek 大模型（友商首款手游已接入） | Slide 2 + Slide 7 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 7** | 行业趋势："**游戏正在成为 AI 最好的训练场**""某款 FPS 作为首款接入 **DeepSeek 大模型**的手游，将推出**可指挥的 AI 队友**、**可实时自由对话的 NPC**""巨人网络、米哈游旗下 Anuttacon 等公司也率先在推理类、冒险类游戏中测试 AI 原生玩法" |
| **Slide 24 / 29** | Gio："智能 NPC 是 AI 技术能够显著提升游戏体验的关键领域""团队正在开发基于**大语言模型和强化学习**的 NPC 行为系统""Gio 特别关注 NPC 系统的**可扩展性和效率**，确保即使在大型多人在线游戏中也能支持**数百个智能 NPC 同时运行**" |
| **Slide 29** | Gio Manager Coach 紫色字："他设定了开发新一代 AI NPC 系统，使 **NPC 对话满意度评分提高 40%**，**玩家与 NPC 互动时长增加 35%**，**游戏沉浸感评分提升 25%** 的目标" |
| **Slide 24 / 29** | Gio："团队已成功开发了专门用于游戏对话生成的**轻量级模型**，该模型在**保持 90% 性能**的同时，将**推理成本降低了 70%**""NPC 对话的连贯性、情感表达的丰富度和游戏术语的准确理解" |
| **Slide 24 / 29** | Gio 部门定位："AI NPC 开发则致力于创造更智能、更具个性的游戏角色，提升玩家沉浸感和互动体验""每月活跃用户超过 1 亿" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Gio** — AI 算法中心高级经理（Slide 24） | AI NPC 为其四大业务方向之一；NLP 背景对口 |
| EB | **Gloria** — Tech & Engineering VP（Slide 9） | Gio 直属汇报对象；技术决策层 |
| 技术协作 | **Garman** — 机器学习部门总监（Slide 25） | AIBOT 行为系统（OP-04）与 NPC 对话需共享推理基础设施 |
| 业务承载 | **Greg** — X Studio 总监（Slide 11） | FPS 全球一体化发行项目是 NPC 对话首个落地场景 |

---

## 商机痛点（业务描述）

Slide 7 PPT 原文明确把"可实时自由对话的 NPC"作为行业拐点——某 FPS 手游首款接入 DeepSeek 大模型，这不是营销宣传，是竞品先发了。在这个行业背景下，Slide 29 紫色字明确 Gio 的 KPI 是让 NPC 对话满意度提升 40%、玩家与 NPC 互动时长增加 35%、沉浸感评分提升 25%——三个数字刻度非常清晰，且它们不是内部效率指标，而是直接对应用户体验和留存的业务指标。

Gio 面临的业务压力：

1. **竞品先发 + CEO 明确"新生代游戏公司层出不穷"的压力**：Slide 6 引用 CEO 原话"新生代游戏公司层出不穷，从玩法类到内容类的转变一时无所适从，友商不断产出新品，我们好像毫无建树"。米哈游 + 游戏科学（黑神话悟空）已经构成了外部压力，如果连 NPC 对话这种"AI 原生玩法"都落后，腾讯游戏的"长青游戏"战略叙事会进一步被稀释。
2. **数百个 NPC 同时运行的并发 + 成本双重挑战**：Slide 24/29 原文"确保即使在大型多人在线游戏中也能支持数百个智能 NPC 同时运行"。这意味着 NPC 对话不是"几个 NPC 用大模型"，而是要让每场多人游戏的全部 NPC 都具备对话能力——对推理成本和延迟提出严苛要求。
3. **长青游戏战略里 NPC 对话是留存的新杠杆**：Slide 6 CEO 叙事"基于头部大 DAU 游戏的持续增长才是带动业绩增长的关键"——长青游戏要长青，需要不断给老游戏注入新体验，AI NPC 对话是最低实现成本、最高感知价值的 update。
4. **推理成本已有方法但待规模化**：Slide 24/29 明确 Gio 团队已有轻量级模型"保持 90% 性能的同时，推理成本降低 70%"，但这是实验室数据，还需要在"每月活跃用户超过 1 亿"（Slide 24/29）规模下验证经济可行性。
5. **海外发行节奏压力**：Slide 5 FPS 游戏计划 2025 年底启动正式发行，NPC 对话需要覆盖全球多语种玩家——这与 OP-02 翻译本地化形成技术底座共享诉求，但 NPC 业务侧立项可以先行。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| NPC 对话满意度评分 +40%、互动时长 +35%、沉浸感评分 +25% | Slide 29 紫色字 KPI 原文 |
| 在 1 亿月活规模下支持数百 NPC 同时对话，推理成本保持 70% 降幅 | 对齐 Slide 24/29 轻量模型成果 + 月活规模 |
| 长青游戏的"AI 原生玩法"叙事可成形，回应友商竞争叙事 | 对齐 Slide 6 CEO 长青游戏战略 |
| FPS 全球发行（2025 年底）首发即具备 AI NPC 对话能力 | 对齐 Slide 5 全球发行节奏 |
| 为 Gio "至少 3 个 AI 项目从 PoC 到全面部署"KPI 贡献首个落地 | Slide 29 紫色字 KPI |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

# OP-02 — 全球上线的 AI 实时翻译与本地化

**类型：业务商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — Real-Time AI Translation & Localization for Global Launch | — |
| **Stage** | Prospect | — |
| **Expected Closing Date** | 2027 Q3 | — |
| **Expected Revenue (ARR)** | US$ 3M *（培训模拟值）* | — |
| **Solution Products** | Amazon Translate + Amazon Bedrock + Amazon Polly | — |
| **M — Metrics** | 各区域玩家留存率差异控制在 5% 以内；付费转化率达到行业平均 1.2 倍；玩家满意度 ≥ 4.5/5（经由 X Studio Greg 的 KPI 承载） | Slide 16 Greg Manager Coach 紫色字 |
| **E — Economic Buyer** | **未识别**（Prospect 阶段典型状态；候选触达路径 = Gio → Gloria + Gemma 持 GenAI 战略业务预算） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | FPS 计划 2025 年底全球发行；目标市场含东南亚 + 欧洲 + 中东 + 南美 + 北非 + 澳洲，多语种本地化从"锦上添花"变"入门门槛" | Slide 5 战略方向 |
| **CH — Champion** | **Gio** — AI 算法中心高级经理（实时翻译与本地化翻译为其明确四大业务方向之二） | Slide 24 / 29 Persona 原文 |
| **CP — Competition** | 平台服务（北美/欧洲/新加坡）= Azure + GCP；G-Cloud 内部云 | Slide 7 IT 供应商表 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 24 / 29** | Gio 部门业务："**实时翻译服务**支持多语言玩家之间的无障碍交流；**本地化翻译技术**帮助游戏内容更准确地适应不同文化背景" |
| **Slide 24 / 29** | Gio："AI 算法中心与公司的**国际部门**密切合作，直接**获取海外市场的丰富数据资源**，这为 AI 模型训练提供了素材" |
| **Slide 4** | 市场分析："**积极布局出海**""海外市场方面，**北美、日本以及东南亚增长较为明显**，中国游戏企业在美术表现、**AI 运营**等方面具有差异化优势""全行业总收入突破 387 亿元" |
| **Slide 5** | 战略方向："为此，公司成立了国际发行部，不仅提供全面的发行渠道，还构建了持续提供 **Intl SDK 平台**和全生命周期的先进数据组，并且**制定了 GenAI 战略，助力游戏发行**""游戏发行重点在东南亚、欧洲和中东，但面对 FPS 类游戏，需要全球玩家流量，因此还在尝试更偏远地区，如**南美、北非、澳洲**等地区" |
| **Slide 11** | Greg（X Studio 总监）："全球一体化运营与本地化平衡：如何在保持游戏核心体验一致性的同时，满足不同地区玩家的文化偏好和游戏习惯""**重视本地化质量，不仅包括语言翻译，还包括文化元素、游戏节奏和经济系统的适应性调整**" |
| **Slide 16** | Greg Manager Coach 紫色字："各区域玩家的**留存率差异控制在 5% 以内**，**付费转化率达到行业平均水平的 1.2 倍**，**玩家满意度评分不低于 4.5/5 分**" |
| **Slide 17** | Gavin Manager Coach 紫色字："**全球网络延迟控制在 50ms 以内**…**P95 响应时间控制在 100ms 以内**" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Gio** — AI 算法中心高级经理（Slide 24） | 翻译与本地化为其明确四大业务方向之二 |
| EB | **未识别**（Prospect 阶段） | 候选触达路径：Gio → Gloria（技术决策）+ Gemma（国际发行部 GM，GenAI 战略业务预算持有） |
| 业务买单方 | **Greg** — X Studio 总监（Slide 11） | 留存率差 ≤5% 等跨区域 KPI 直接依赖本地化质量 |
| 技术协作 | **Gavin** — 技术运营高级经理（Slide 12） | 50ms 全球延迟 + P95 ≤100ms 的 SLA 承载方 |

---

## 商机痛点（业务描述）

Slide 5 明确了 FPS 计划 2025 年底全球发行，目标市场覆盖东南亚 + 欧洲 + 中东 + 南美 + 北非 + 澳洲——这不是"中文游戏加个英文 UI"，是一款需要同时服务多语种玩家实时对战、跨文化本地化的游戏。Slide 4 也指出海外收入增长主要来自北美、日本、东南亚，说明 AI 翻译和本地化是"海外营收增长"的支撑技术之一。

Gio 和 X Studio 面临的业务压力：

1. **本地化质量不等于语言翻译**：Slide 11 Greg 原文"重视本地化质量，不仅包括语言翻译，还包括文化元素、游戏节奏和经济系统的适应性调整"——这意味着 AI 不仅要翻译文本，还要理解文化上下文。对于 FPS 这类需要实时交流的游戏，语音 / 文字消息翻译的延迟、准确度、文化适配度都是玩家体验的核心。
2. **跨区域 KPI 绑定**：Slide 16 Greg 紫色字明确各区域留存率差异 ≤ 5%、付费转化达到行业平均的 1.2 倍、满意度 ≥ 4.5——这些 KPI 要在覆盖东南亚到北非的多时区 / 多语言 / 多监管环境下达成，AI 翻译质量差哪怕 5% 都会体现在留存数据上。
3. **实时对战的延迟天花板**：Slide 17 Gavin 紫色字"全球网络延迟 ≤50ms、P95 ≤100ms"——实时翻译的推理延迟必须塞进这 100ms 里，否则游戏内语音 / 文字消息的翻译会破坏对战节奏，玩家直接弃坑。
4. **本地化节奏与上市窗口**：Slide 5 FPS 计划 2025 年底正式发行，留给本地化的时间窗口有限。传统外包式本地化（文本发给翻译公司 → 翻译回来 → 嵌入 → 测试）一轮 3–6 个月，6 个语种并行就是 18 人月——在 2025 Q4 上市节奏下来不及。
5. **GenAI 战略业务预算已到位**：Slide 5 原文"制定了 GenAI 战略，助力游戏发行"——国际发行部 Gemma 持有 GenAI 战略预算，Gio 的本地化项目天然是这笔预算的候选支出方向。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| FPS 全球发行首发即具备主流 10+ 语种实时翻译能力 | 对齐 Slide 5 目标市场列表 |
| 本地化周期从 3–6 个月缩短到 2–4 周 | 对齐 Slide 5 "2025 年底正式发行"节奏 |
| 各区域留存率差异 ≤ 5% KPI 可达成 | 对齐 Slide 16 Greg 紫色字 |
| 实时翻译推理延迟塞进 50ms 全球网络 + 100ms P95 | 对齐 Slide 17 Gavin 紫色字 SLA |
| 海外 AI 运营差异化优势兑现 | 对齐 Slide 4 "中国游戏企业在美术表现、AI 运营方面具有差异化优势" |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

# OP-03 — 玩家舆情分析与个性化推荐

**类型：业务商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — Player Sentiment Analysis & Personalized Recommendation | — |
| **Stage** | Prospect | — |
| **Expected Closing Date** | 2027 Q4 | — |
| **Expected Revenue (ARR)** | US$ 2.5M *（培训模拟值）* | — |
| **Solution Products** | Amazon Comprehend + Amazon Personalize + Amazon Bedrock | — |
| **M — Metrics** | 至少 5 个游戏项目 DAU +10% 以上；业务部门 AI 解决方案满意度 ≥ 4.5/5；至少 3 个 AI 项目从 PoC 到全面部署 | Slide 29 Gio Manager Coach 紫色字 KPI |
| **E — Economic Buyer** | **未识别**（Prospect 阶段典型状态；候选触达路径 = Gio → Gloria + 业务 Studio VP） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | CEO 原话"大 DAU 游戏的持续增长才是带动业绩增长的关键"；个性化推荐测试阶段玩家留存率 +15%，但舆情场景无量化 KPI | Slide 6 CEO 战略 + Slide 24/29 推荐测试数据 |
| **CH — Champion** | **Gio** — AI 算法中心高级经理（舆情分析为其明确四大业务方向之一） | Slide 24 / 29 Persona 原文 |
| **CP — Competition** | G-Cloud 内部云（享"成本价"）；Azure + GCP 平台服务；业务部门自研 | Slide 2 + Slide 7 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 24 / 29** | Gio 部门业务："**舆情分析系统**帮助公司实时监控和分析全球玩家对游戏的反馈" |
| **Slide 24 / 29** | Gio："团队面临的首要挑战是向业务部门证明 AI 技术的实际价值""正在推动建立'**AI 价值评估框架**'""他特别关注短期可见的成果，优先开发能够在 3-6 个月内展示明显效果的 AI 应用，**如个性化游戏内容推荐系统，该系统已在测试阶段将玩家留存率提高了 15%**" |
| **Slide 29** | Gio Manager Coach 紫色字："通过 AI 技术应用，**帮助至少 5 个游戏项目实现 DAU（日活跃用户数）10% 以上的提升**；**将业务部门对 AI 解决方案的满意度评分提高到 4.5/5 以上**；**实现至少 3 个 AI 项目从概念验证到全面部署的转化**" |
| **Slide 6** | 业务挑战：CEO 原话"G-Games CEO 曾表示，中国游戏市场已趋成熟，相较于追求短期的爆款，**基于头部大 DAU（日活用户）游戏的持续增长才是带动业绩增长的关键**""聚焦'长青游戏'战略一定程度上是成功的" |
| **Slide 6** | 业务挑战：CEO 原话"新生代游戏公司层出不穷，从玩法类到内容类的转变一时无所适从""米哈游《原神》+ 游戏科学《黑神话：悟空》" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Gio** — AI 算法中心高级经理（Slide 24） | 舆情 + 推荐为四大业务方向之一；证明 AI 商业价值是其核心议题 |
| EB | **未识别**（Prospect 阶段） | 候选触达路径：Gio → Gloria（技术）+ 业务 Studio VP（DAU 受益方：George X Studio / Gwen Y Studio） |
| 业务买单方 | **George** — X Studio VP + **Gwen** — Y Studio VP（Slide 9） | DAU +10% KPI 的最终受益方和验证方 |
| 业务运营 | **Griffin** — 国际发行部产品发行总监（Slide 9） / **Gemma** — 国际发行部 GM（Slide 9） | 海外舆情监控与推荐的业务链条 |
| 数据技术协作 | **Garman** — 机器学习部门总监（Slide 25） | "玩家行为数据持续优化 AI 模型"共享训练底座（OP-05/06） |

---

## 商机痛点（业务描述）

Slide 24/29 Gio 的部门定位里把"舆情分析系统"和"AI NPC 开发"并列为四大业务方向之一。Slide 29 紫色字的 KPI 又明确三项要求："**至少 5 个游戏项目 DAU +10%、业务部门对 AI 满意度 ≥4.5/5、至少 3 个 AI 项目从 PoC 到全面部署**"——注意这组 KPI 是 Gio 作为 AI 算法中心高级经理的**年度绩效目标**，其中"业务部门对 AI 满意度"这项背后隐含着一个深层痛点：**业务部门对 AI 的成功案例还在持观望态度**（Slide 24/29 原文"团队面临的首要挑战是向业务部门证明 AI 技术的实际价值"）。

Gio 面临的业务压力：

1. **AI 价值证明是政治议题，不是技术议题**：Slide 24/29 原文"团队面临的首要挑战是向业务部门证明 AI 技术的实际价值""业务部门仍然需要看到具体的投资回报"。这在腾讯游戏这种"业务为王"的组织里意味着：如果 Gio 不能在 3–6 个月内拿出业务部门满意的成果，AI 算法中心的预算会被挤压。
2. **长青游戏战略 = 个性化推荐的业务锚**：Slide 6 CEO 原话"基于头部大 DAU（日活用户）游戏的持续增长才是带动业绩增长的关键"。长青游戏不能靠新内容堆砌，要靠"让每个玩家看到最对味的游戏内容"——个性化推荐是 CEO 战略的具体技术承载。
3. **测试数据证明了价值，但规模化需要基础设施**：Slide 24/29 明确"个性化游戏内容推荐系统，该系统已在测试阶段将玩家留存率提高了 15%"——这是已经被测试验证过的数据。挑战是从"测试阶段"扩展到"至少 5 个游戏项目"需要配套的推理基础设施、数据治理、多租户隔离、A/B 测试平台。
4. **舆情分析的价值结构更复杂**：Slide 24/29 仅用一句话带过"舆情分析系统实时监控和分析全球玩家对游戏的反馈"，没给出舆情侧量化 KPI。这意味着 Gio 的舆情项目属于"战略级投入但业务 KPI 尚不清晰"的项目，需要在 Discovery 阶段和业务部门共建量化框架（响应时延、话题覆盖量、情感分类准确率等）。
5. **友商竞争节奏倒逼响应速度**：Slide 6 CEO 原话"米哈游《原神》+ 游戏科学《黑神话：悟空》"意味着腾讯游戏在内容创意上已被友商追赶。舆情分析是"快速听到用户声音"的必备能力，响应速度比模型精度更关键。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| 至少 5 个游戏项目 DAU +10% | Slide 29 紫色字 KPI 原文 |
| 业务部门对 AI 解决方案满意度 ≥ 4.5/5 | Slide 29 紫色字 KPI 原文 |
| 至少 3 个 AI 项目从 PoC 到全面部署 | Slide 29 紫色字 KPI 原文 |
| 个性化推荐从"测试阶段留存 +15%"扩展到全线游戏 | 对齐 Slide 24/29 已验证数据 |
| 舆情响应从"发现问题"到"业务决策"时延从周级压缩到小时级 | 对齐 Slide 6 CEO 长青游戏战略的"持续运营"要求 |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

# OP-04 — AIBOT 陪玩系统训练与推理基础设施

**类型：技术商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — AIBOT Companion System Training & Inference Infra | — |
| **Stage** | Qualified | — |
| **Expected Closing Date** | 2026 Q4 | — |
| **Expected Revenue (ARR)** | US$ 8M *（培训模拟值）* | — |
| **Solution Products** | AWS Graviton + Amazon EC2 Spot + Amazon SageMaker HyperPod | — |
| **M — Metrics** | 每次 AI 调用成本 -30%；模型训练时间 -40%；资源利用率 +25%（Slide 30 紫色字三项 KPI） | Slide 30 Garman Manager Coach 紫色字 |
| **E — Economic Buyer** | **Gloria** — Tech & Engineering VP（Garman 直属汇报对象） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | AIBOT 每天服务 500 万活跃用户 + 2000 万场 AI 对战；"云极其昂贵"；裸金属方案弹性扩展、资源调度、维护成本存在局限 | Slide 25/30 Garman |
| **CH — Champion** | **Garman** — 机器学习部门总监（CMU CS 博士 · 强化学习与博弈论；AIBOT 为其部门旗舰产品） | Slide 25 / 30 Persona 原文 |
| **CP — Competition** | 裸金属服务器（现有，"性价比最佳"认知）；G-Cloud 内部云（享"成本价"）；Garman 本人对云有"云极其昂贵"疑虑 | Slide 2 + Slide 25/30 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 25 / 30** | Garman 部门业务："**该部门的旗舰产品是面向 MOBA 和 FPS 游戏的 AIBOT 系统**""AIBOT 系统采用分布式架构，**通常与游戏战斗服部署在一起，以减少网络传输的流量费用**""**每天服务超过 500 万活跃用户，处理超过 2000 万场 AI 对战**" |
| **Slide 25 / 30** | Garman 成本挑战："作为机器学习部门的负责人，Garman 面临的首要挑战是如何在有限的预算内最大化 AI 性能""**AIBOT 系统需要大量计算资源进行训练和推理**，而游戏行业的利润率要求控制技术成本" |
| **Slide 25 / 30** | Garman 当前部署："**倾向于使用裸金属服务器**，认为这能提供最佳的性价比""**云极其昂贵**""尽管团队已经在 AWS 上部署了部分业务，但他仍然担忧长期成本问题" |
| **Slide 25 / 30** | Garman AWS 合作："Garman 的团队与 **AWS 已经在上一个项目中建立了合作关系**""团队曾考虑过使用 **AWS Graviton 处理器和 Spot 实例**进行系统改造，并已完成相关适配工作，**部分业务已经在 AWS 上成功上线**" |
| **Slide 30** | Garman Manager Coach 紫色字 KPI："**将每次 AI 调用的成本降低 30%**""**将模型训练时间缩短 40%**""**实现资源利用率提升 25%**" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Garman** — 机器学习部门总监（Slide 25） | AIBOT 为其部门旗舰产品；AWS 已有合作关系 |
| EB | **Gloria** — Tech & Engineering VP（Slide 9） | Garman 直属汇报对象；大模型/ML/计费平台分支决策层 |
| 技术协作 | **Gavin** — 技术运营高级经理（Slide 12） | 战斗服与 AIBOT 共机部署；50ms 延迟 + 75% 利用率 SLA 承载 |
| 业务场景 | **Greg** — X Studio 总监（Slide 11） | FPS 全球项目是 AIBOT 陪玩的首个业务场景 |
| 对话层协作 | **Gio** — AI 算法中心高级经理（Slide 24） | NPC 对话系统（OP-01）与 AIBOT 行为系统需共享推理基础设施 |

---

## 商机痛点（技术描述）

Slide 25/30 PPT 原文明确告诉我们：**AIBOT 是机器学习部门的旗舰产品，每天服务超过 500 万活跃用户、处理超过 2000 万场 AI 对战**。这个规模级业务的当前技术选择是"**与游戏战斗服部署在一起、减少网络传输流量费用**"——采用裸金属分布式架构。Slide 30 紫色字又给出了 Garman 的 3 条硬 KPI：**每次 AI 调用成本 -30%、模型训练时间 -40%、资源利用率 +25%**。

Garman 团队面临的技术压力：

1. **裸金属方案在弹性扩展 + 资源调度 + 维护成本三项上天花板明显**：Slide 25/30 原文"这种方案虽然成本较低，但**在弹性扩展、资源调度和维护成本方面存在局限**"——Garman 本人也承认裸金属有结构性短板。游戏上线初期玩家匹配困难的场景（AIBOT 陪玩的核心价值）正是峰谷差最大的时段，弹性扩展不足意味着要么超买资源养着（利用率低）、要么峰值时玩家匹配不上 AIBOT（体验差）。
2. **训练与推理算力消耗双重压力**：Slide 25/30 原文"**AIBOT 系统需要大量计算资源进行训练和推理**"。训练侧是 MARL 模型离线训练，推理侧是 2000 万场/天对战的在线调用——两边都是资源大户，且资源使用特征完全不同（训练是连续高利用率 GPU，推理是突发低延迟 CPU+GPU 混合）。在单一裸金属集群上优化两种负载几乎不可能，自然驱动混合云思路。
3. **Garman 对云的成本怀疑是 Discovery 的核心议题**：Slide 25/30 原文"**Garman 对第三方云服务持怀疑态度，认为'云极其昂贵'**"——这不是客气话，是 Champion 最直接的异议。任何 AWS 方案必须用他已经接受的 Graviton + Spot 口径讲经济账，而不是讲"弹性""敏捷"这些他不买账的价值。
4. **AWS 已有 Graviton + Spot 适配经验是最短路径**：Slide 25/30 原文"**团队曾考虑过使用 AWS Graviton 处理器和 Spot 实例进行系统改造，并已完成相关适配工作**，部分业务已经在 AWS 上成功上线"——意味着 AWS 不是从零开始说服，而是在一个已经有成功试点的基础上扩展。这是整个 Game Case 的 6 个 OP 中 CH + P + CP 组合起点最高的商机。
5. **海外发行场景需要 AWS 的地缘覆盖**：Slide 7 IT 供应商表明确"**海外游戏发行业务 = AWS**"——FPS 全球发行（Slide 5）上线后 AIBOT 要服务全球玩家，AWS 的全球 Region 覆盖是裸金属 + G-Cloud 方案难以对标的结构性优势。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| 每次 AI 调用的成本 -30% | Slide 30 紫色字 KPI 原文 |
| 模型训练时间 -40% | Slide 30 紫色字 KPI 原文 |
| 资源利用率 +25% | Slide 30 紫色字 KPI 原文 |
| 500 万 DAU / 2000 万场对战的业务规模在相同或更低成本下持续扩展 | 对齐 Slide 25/30 现有业务规模 |
| FPS 全球发行（2025 年底）首发即具备 AIBOT 陪玩覆盖海外玩家 | 对齐 Slide 5 全球发行节奏 + Slide 7 AWS 海外发行位点 |
| 裸金属 + 云的混合架构正式纳入部门技术战略 | 回应 Slide 25/30 Garman "正在评估混合云策略" |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

# OP-05 — 多智能体强化学习训练平台

**类型：技术商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — Multi-Agent Reinforcement Learning Training Platform | — |
| **Stage** | Qualified | — |
| **Expected Closing Date** | 2027 Q2 | — |
| **Expected Revenue (ARR)** | US$ 6M *（培训模拟值）* | — |
| **Solution Products** | Amazon SageMaker HyperPod + AWS Trainium + Amazon FSx for Lustre | — |
| **M — Metrics** | 玩家无法区分 AI 与真人玩家的比例从 45% 提升至 75%；AI 策略多样性指数 +50%；AI 适应性学习速度 +60% | Slide 30 Garman Manager Coach 紫色字 KPI |
| **E — Economic Buyer** | **候选待确定**：Gloria（Tech & Engineering VP）或 Gabriel（G-Cloud VP；若 MARL 平台涉及内部云与 AWS 混合架构） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | "简单的规则型 AI 已无法满足市场需求"；大规模训练数据收集与标注、复杂模型训练效率、游戏平衡性是主要工程挑战 | Slide 25/30 Garman |
| **CH — Champion** | **Garman** — 机器学习部门总监（CMU CS 博士 · **强化学习与博弈论学术背景**；依靠 RL 构建了国内顶级 AIBOT 产品） | Slide 25 / 30 Persona 原文 |
| **CP — Competition** | 裸金属服务器；G-Cloud 内部云；现有 AIBOT 训练基础设施（本身即为 MARL 场景） | Slide 2 + Slide 25/30 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 25 / 30** | Garman 技术方向："随着玩家期望的提高，**简单的规则型 AI 已无法满足市场需求**""Garman 面临的技术挑战是如何**提升 AIBOT 的拟人化水平**，使 AI 行为更加自然、多样化且具有学习能力" |
| **Slide 25 / 30** | Garman："**Garman 的团队正在研发基于多智能体强化学习的新一代 AIBOT 系统**""该系统不仅能模仿人类玩家的操作习惯和决策模式，还能展现**情绪反应和社交行为，如团队协作、战术沟通**等""团队正在**探索将大规模预训练模型与强化学习相结合**" |
| **Slide 25 / 30** | Garman 工程挑战："这项工作面临的挑战包括**大规模训练数据的收集和标注、复杂模型的训练效率、以及如何在保持游戏平衡性的同时提供足够挑战性的 AI 体验**""特别关注如何**利用玩家行为数据持续优化 AI 模型，同时确保数据隐私和合规性**" |
| **Slide 25 / 30** | Garman 背景："拥有**卡内基梅隆大学的计算机科学博士学位，专攻强化学习和博弈论**""加入腾讯后，他带领团队**依靠强化学习技术，构建起了国内顶级的 AIBOT 产品**" |
| **Slide 30** | Garman Manager Coach 紫色字："**玩家无法区分 AI 与真人玩家的比例从现有的 45% 提升至 75%**""**AI 策略多样性指数提高 50%**""**AI 适应性学习速度提升 60%**" |
| **Slide 7** | 行业趋势："业内人士认为，游戏有着丰富的场景以及众多的玩家需求。在**智能体的决策训练、场景识别**、3D 生成内容和无限叙事等方面，游戏都给 AI 的发展与应用带来了更多想象的空间""AI 投入从'工具赋能'向'原生融合'的关键转折点" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Garman** — 机器学习部门总监（Slide 25） | MARL 为其学术 DNA；团队正在研发新一代系统 |
| EB | **候选待确定**（Slide 9） | Gloria（技术路径）或 Gabriel G-Cloud VP（混合云路径） |
| 数据源协作 | **Gio** — AI 算法中心高级经理（Slide 24） | "基于强化学习开发过多款创新 AI 产品"，MARL 训练底座与 Gio 跨部门共享 |
| 算力协作 | **Gavin** — 技术运营高级经理（Slide 12） | MARL 训练对 GPU 集群调度与混合云资源的承载人 |

---

## 商机痛点（技术描述）

Slide 25/30 PPT 原文明确 Garman 团队**"正在研发基于多智能体强化学习的新一代 AIBOT 系统"**。这不是简单的模型升级，是从"规则型 AI"跨到"具备情绪反应、社交行为、团队协作、战术沟通"的拟人化 AI——这类模型的训练工程难度远超单智能体 RL，对训练基础设施要求是质变。Slide 30 紫色字的硬指标是：**玩家无法区分 AI 与真人玩家的比例从 45% 提升到 75%**（即图灵式通过率 +30 pp），同时策略多样性 +50%、学习速度 +60%。

Garman 团队面临的技术压力：

1. **MARL 训练的工程复杂度是单智能体的 N² 级**：多智能体强化学习涉及 N 个 agent 同时与环境交互、彼此博弈，训练样本规模、模型参数、梯度同步复杂度都呈 N² 级增长。Slide 25/30 原文"**大规模训练数据的收集和标注、复杂模型的训练效率**"是 Garman 自己点出的核心挑战。
2. **大规模预训练 + RL 的融合是新范式**：Slide 25/30 原文"**团队正在探索将大规模预训练模型与强化学习相结合**"——这是当前 AI 前沿方向（DeepMind / OpenAI / Anthropic 都在做），工程路径未成熟，计算资源消耗巨大。需要能支撑大参数量 pretrain + RL finetuning 的统一训练平台。
3. **数据隐私与合规性硬约束**：Slide 25/30 原文"**特别关注如何利用玩家行为数据持续优化 AI 模型，同时确保数据隐私和合规性**"——玩家行为数据属于敏感类别，MARL 训练平台需要解决数据访问控制、模型训练过程可审计、跨境数据合规等企业级问题。这比单纯的"大模型训练"要求更高。
4. **训练效率直接转化为业务速度**：Slide 30 紫色字"**AI 适应性学习速度 +60%**"——这不只是技术指标，是产品竞争力。友商（DeepSeek 接入 FPS、米哈游）在 AI 原生玩法上已经发出信号（Slide 7），Garman 团队如果训练平台不快，新 AIBOT 行为迭代就会慢一拍。
5. **Champion 的学术 DNA 驱动技术标尺**：Slide 25/30 明确 Garman "CMU CS 博士，专攻强化学习和博弈论"——他会以国际顶级 RL 研究团队的技术栈作为 DC 标尺（Ray RLlib、OpenAI Gym / Gymnasium、DeepMind Lab 等），而不是国内平台的 baseline。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| 玩家无法区分 AI 与真人玩家的比例从 45% → 75% | Slide 30 紫色字 KPI 原文 |
| AI 策略多样性指数 +50% | Slide 30 紫色字 KPI 原文 |
| AI 适应性学习速度 +60% | Slide 30 紫色字 KPI 原文 |
| MARL 训练任务从天级缩短到小时级；单次训练可并行支持数百 agent | 对齐 Slide 25/30 训练效率挑战 |
| 玩家行为数据训练可审计、可脱敏、跨境合规架构前置 | 对齐 Slide 25/30 数据隐私与合规原文 |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

# OP-06 — 大模型部署与成本优化

**类型：技术商机**

---

## Opportunity Description（CRM 登记卡片）

| Field | Value | PPT 出处 |
|---|---|---|
| **Opportunity Name** | G-Games — LLM Deployment & TCO Optimization (Graviton + Trainium/Inferentia) | — |
| **Stage** | Prospect | — |
| **Expected Closing Date** | 2027 Q3 | — |
| **Expected Revenue (ARR)** | US$ 4M *（培训模拟值）* | — |
| **Solution Products** | AWS Graviton + AWS Trainium + AWS Inferentia + Amazon EC2 Spot | — |
| **M — Metrics** | 每次 AI 调用成本 -30%；模型部署成本 -50%；模型训练时间 -40%；资源利用率 +25% | Slide 30 Garman 紫色字 + Slide 29 Gio 紫色字 |
| **E — Economic Buyer** | **未识别**（Prospect 阶段典型状态；候选触达路径 = Garman → Gloria，涉及 G-Cloud 混合架构则需 Gabriel 联合决策） | Slide 9 组织架构图 |
| **I — Implicate the Pain** | "云极其昂贵"认知下，AIBOT + NPC + 翻译等多条 AI workload 叠加使训练/推理成本成为部门天花板；G-Cloud 享"成本价"是最大阻力 | Slide 2 + Slide 25/30 |
| **CH — Champion** | **Garman** — 机器学习部门总监（AWS 已有 Graviton + Spot 适配经验，对云成本效益最敏感） | Slide 25 / 30 Persona 原文 |
| **CP — Competition** | G-Cloud 内部云（享"成本价"，最大阻力）；裸金属服务器（Garman 认为性价比最佳）；Azure + GCP（计费 / 平台服务位点） | Slide 2 + Slide 7 |

---

## Opportunity Source（PPT 出处）

| Slide | 原文片段 |
|---|---|
| **Slide 25 / 30** | Garman 成本挑战："**游戏行业的利润率要求控制技术成本**""**云极其昂贵**""尽管团队已经在 AWS 上部署了部分业务，但他仍然担忧长期成本问题" |
| **Slide 25 / 30** | Garman："**正在评估混合云策略，考虑将高峰负载分配到云端，同时保持核心训练工作在内部基础设施上进行**。他特别关注 **AWS Graviton 处理器的性价比和 Spot 实例的成本优势**，但仍需更多数据来证明云迁移的长期经济效益" |
| **Slide 25 / 30** | Garman 现有部署："团队曾考虑过使用 **AWS Graviton 处理器和 Spot 实例**进行系统改造，并已完成相关适配工作，**部分业务已经在 AWS 上成功上线**" |
| **Slide 30** | Garman Manager Coach 紫色字："**将每次 AI 调用的成本降低 30%**""**将模型训练时间缩短 40%**""**实现资源利用率提升 25%**" |
| **Slide 24 / 29** | Gio 侧大模型成本证据："团队已成功开发了专门用于游戏对话生成的轻量级模型，该模型**在保持 90% 性能的同时，将推理成本降低了 70%**" |
| **Slide 29** | Gio Manager Coach 紫色字："开发至少 2 个游戏行业专用 AI 模型，在特定任务上性能超越通用模型 30% 以上，**同时将模型部署成本降低 50%**" |
| **Slide 2** | 集团战略定位："**云与 AI 产业部，是国内头部公有云和 AI 服务商，集团内业务优先使用自己的云和 AI，并享受成本价**""技术工程部…**大量投入云平台建设运营及 AI 能力的提升**" |
| **Slide 7** | IT 供应商表："**全球骨干网互联 \| AWS**""**海外游戏发行业务 \| AWS**""**国内游戏发行业务 \| G-Cloud**" |

---

## 相关人物

| 角色 | 姓名 / 来源 | 在此商机中的定位 |
|---|---|---|
| Champion | **Garman** — 机器学习部门总监（Slide 25） | 对成本最敏感；Graviton + Spot 已有适配经验；"AWS 已经在上一个项目中建立了合作关系" |
| EB | **未识别**（Prospect 阶段） | 候选路径：Garman → Gloria；若涉及 G-Cloud 混合则需 Gabriel（G-Cloud VP）联合决策 |
| 大模型共享方 | **Gio** — AI 算法中心高级经理（Slide 24） | 游戏对话模型部署成本 -50% 是其紫色字 KPI；共享底座诉求 |
| 技术架构协作 | **Gavin** — 技术运营高级经理（Slide 12） | "平台组件云迁移与改造""评估 Amazon ElastiCache、DynamoDB 等替代方案""迁移后数据库性能损失不超过 5%，服务可用性 99.99%" |
| G-Cloud 关联方 | **Gabriel** — G-Cloud VP（Slide 9） | 内部云持有人；OP-06 的内部阻力/协作对象 |

---

## 商机痛点（技术描述）

Slide 25/30 PPT 把 Garman 面对的核心议题讲得非常直白：**"游戏行业的利润率要求控制技术成本"+ "云极其昂贵"+ "部分业务已经在 AWS 上成功上线"+ "仍需更多数据来证明云迁移的长期经济效益"**。这四句话叠加——Garman 是一个"已经用过、但被长期成本疑虑牵绊"的潜在 AWS 客户。紫色字给出了硬指标：**调用成本 -30%、训练时间 -40%、利用率 +25%、部署成本 -50%**。

Garman 团队面临的技术压力：

1. **多条 AI workload 叠加使成本成为部门天花板**：AIBOT（OP-04，500 万 DAU / 2000 万场 AI 对战）+ MARL 训练（OP-05）+ NPC 对话（OP-01，亿级月活）+ 翻译（OP-02）同时跑，单一 workload 的成本优化不足以支撑部门整体经济可持续。需要跨 workload 的统一成本治理。
2. **G-Cloud 的"成本价"是最大内部阻力**：Slide 2 原文"**集团内业务优先使用自己的云和 AI，并享受成本价**"——这是所有进入腾讯集团的外部云厂商面临的基础阻力。AWS 的差异化不能只是"我便宜"，必须是"我能做 G-Cloud 不能做的事"（例如海外全球部署、Graviton 架构、Trainium/Inferentia 专用加速器）。
3. **混合云策略已被 Garman 明确"在评估"**：Slide 25/30 原文"**正在评估混合云策略，考虑将高峰负载分配到云端，同时保持核心训练工作在内部基础设施上进行**"——这是 Garman 给的明确技术窗口，AWS 不需要推动"全量上云"，只需要赢得"高峰负载"这块蛋糕即可。
4. **Graviton + Spot 是已验证的切入点**：Slide 25/30 原文"**团队曾考虑过使用 AWS Graviton 处理器和 Spot 实例进行系统改造，并已完成相关适配工作**"——Graviton 的 ARM 架构性价比、Spot 实例的浮动定价，Garman 作为 CMU CS 博士能读懂，是"AWS 讲成本时他会认真听"的两个 AWS-specific 武器。
5. **Inferentia / Trainium 在 PPT 未被提及**：Slide 25/30 只提到 Garman 关注 Graviton + Spot，但未提及 AWS 的专用 AI 加速器 Inferentia（推理）和 Trainium（训练）。这是 AWS sales 在 Discovery 阶段要主动引入的"新信息"——这两款芯片正是针对 Garman 3 条紫色字 KPI 的精准武器。
6. **海外 AI workload 是 G-Cloud 覆盖不到的战略纵深**：Slide 7 明确 AWS 在"全球骨干网 + 海外游戏发行"两个位点——海外 AI 训练/推理是 G-Cloud 成本优势无法延伸的场景，AWS 的地缘覆盖是结构性优势。

---

## 商机业务成果（培训用假设值）

| 业务成果 | 测算逻辑 |
|---|---|
| 每次 AI 调用成本 -30% | Slide 30 紫色字 KPI 原文 |
| 模型训练时间 -40% | Slide 30 紫色字 KPI 原文 |
| 资源利用率 +25% | Slide 30 紫色字 KPI 原文 |
| 模型部署成本 -50%（大模型侧） | Slide 29 Gio 紫色字 KPI |
| 高峰负载上云 + 核心训练留内部基础设施，混合云技术战略落地 | Slide 25/30 Garman 原文"正在评估混合云策略" |
| 海外 AI workload 作为 AWS 在集团的战略纵深，避开 G-Cloud 成本价压力 | 对齐 Slide 2 + Slide 7 格局 |

*以上成果为培训模拟用假设值，不代表客户真实采购意向或内部数据。*

---

