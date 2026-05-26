# 中国版 CXO Personas — 设计决策与变更记录

**Date:** 2026-05-12  
**Author:** Hermes Agent + Demi  
**Status:** In Progress

---

## 一、文件结构设计

```
cxo-personas/
├── SKILL.md                    ← 现有全球版 skill（不动）
├── SKILL-CHINA.md              ← 新增中国版 skill
├── references/                 ← 现有19个全球 personas（不动）
│   └── INDEX.md
├── references-china/           ← 新增19个中国 personas
│   ├── INDEX.md                ← 中国版索引 + 角色变更说明
│   └── *.md                    ← 19个 persona 文件
├── research/
│   ├── china-research-notes.md ← 中国市场基础研究
│   ├── framework-sections-ablation-test.md ← 框架模块消融测试
│   └── china-personas-design-decisions.md  ← 本文档
```

### 为什么独立文件夹而非混合

1. **并行使用** — 全球版和中国版是并行关系，不是替代。同一用户可能跑全球客户也跑中国客户
2. **Agent 路由清晰** — 单独 SKILL-CHINA.md 让 AI agent 知道什么时候用哪套（检测到中国客户/中文场景加载中国版）
3. **避免索引冲突** — 两套角色名不同（中国版有出海VP、政府关系VP等），混在一起 agent 会混淆
4. **独立迭代** — 中国版可以独立更新，不影响全球版稳定性

---

## 二、角色列表（19个）

| # | Persona (EN) | 中文名 | 来源客户 |
|---|-------------|--------|---------|
| 1 | CEO / Founder | 创始人/CEO | 全部12家 |
| 2 | CFO | 首席财务官 | 全部 |
| 3 | CTO | 首席技术官 | 海康、ByteDance、理想、WeBull、猎豹 |
| 4 | COO | 首席运营官 | 海尔、Cathay、Shein |
| 5 | CMO | 首席营销官/品牌VP | Anker、海尔、Shein |
| 6 | CIO | 首席信息官 | 海尔、Cathay、港交所 |
| 7 | CISO | 信息安全负责人 | 港交所、WeBull、海康 |
| 8 | VP of Supply Chain | 供应链VP | Anker、Shein、理想、海尔 |
| 9 | VP of International (出海VP) | 出海/国际化VP | Anker、Shein、ByteDance、WeBull、腾讯Game |
| 10 | VP of AI | AI负责人 | ByteDance、海康、理想、猎豹 |
| 11 | VP of Government Relations | 政府关系VP | ByteDance、海康、港交所、Shein |
| 12 | Chief Compliance Officer | 合规负责人 | WeBull、港交所、Shein、Cathay |
| 13 | CPO (Product) | 首席产品官 | ByteDance、WeBull、禾观、猎豹 |
| 14 | VP of Manufacturing | 智能制造VP | 海尔、海康、理想 |
| 15 | BU Head / 事业群总裁 | 事业群负责人 | ByteDance、海康、腾讯Game、海尔 |
| 16 | CDO (Data) | 首席数据官 | 港交所、ByteDance、Cathay |
| 17 | General Counsel | 总法律顾问 | Shein、WeBull、港交所 |
| 18 | CHRO | 人力资源VP | 海尔、ByteDance、Cathay |
| 19 | CRO (Risk) | 首席风险官 | 港交所、WeBull、Cathay |

---

## 三、vs 全球版变更说明

### 新增的中国特有角色（3个）

| 角色 | 为什么需要 |
|------|-----------|
| **出海VP** | 中国企业"出海"是独立战略职能，不等于西方的"国际业务"。涉及双栈架构(国内云vs海外云)、多法域合规、品牌本地化、TikTok/关税等地缘政治风险。12家中8家有明确出海战略。 |
| **政府关系VP** | 政策驱动占中国CXO议程30-50%。信创、版号、数据安全法、招投标、补贴申报——都需要专人对接。西方GR是lobbying，中国GR是生存必需。 |
| **事业群总裁** | 中国大型科技公司（ByteDance、腾讯、海康）的核心决策层。不同于西方BU Head，事业群总裁拥有独立P&L、独立战略权，更像"内部CEO"。 |

### 移除的全球版角色（3个）

| 角色 | 为什么不适用 |
|------|------------|
| **CAIO (Chief AI Officer)** | 中国几乎不设此title。AI归CTO或单设"AI VP/负责人"。已用"VP of AI"替代。 |
| **CDxO (Chief Digital Officer)** | 中国企业的数字化转型通常归CIO或CTO。CDO(数据官)政策要求设置，但CDxO极少存在。 |
| **CINO (Chief Innovation Officer)** | 中国企业创新由CEO/CTO直接驱动，不设独立创新官。 |

### 调整的角色

| 角色 | 变更 |
|------|------|
| **Head of Procurement → VP of Supply Chain** | 中国企业更强调"供应链"整体管理而非单纯采购。Shein的小单快反、理想的电池供应、海尔的COSMOPlat都是供应链创新。 |
| **VP of Sales → 不设** | 中国用"商务VP"或归入事业群，不作为独立persona。销售决策由CEO/事业群总裁直接管。 |
| **VP of Manufacturing → 智能制造VP** | 强调中国"智能制造"政策导向（灯塔工厂、工业互联网）。 |
| **CRO (Revenue) → CRO (Risk)** | 中国不设Chief Revenue Officer，但金融/交易类公司必设Chief Risk Officer。 |

---

## 四、研究客户基础（12个账户）

| # | 客户 | 行业 | 企业类型 | 核心CXO结构特征 |
|---|------|------|----------|----------------|
| 1 | Anker (安克创新) | 制造/DTC | 上市民企 | 创始人中心化，品牌出海标杆，数据驱动 |
| 2 | 海康威视 | 制造/AI | 央企控股混合制 | 党委+市场化管理并存，信创核心受益者 |
| 3 | 海尔 | 制造/IoT | 上市民企 | 人单合一模式，极度去中心化 |
| 4 | 理想汽车 | 汽车/NEV | 美股+港股上市 | 极端创始人驱动，全栈自研文化 |
| 5 | Shein | 电商/快时尚 | 未上市（拟IPO）| 创始人低调控制，国际化管理层，合规压力极大 |
| 6 | ByteDance | 电商/内容 | 未上市 | 多事业群，AI全面转型，出海风险（TikTok）|
| 7 | 禾观科技 | 电商SaaS | 初创 | 小团队，技术创始人（ex-Google），出海赛道 |
| 8 | Cathay Pacific | 交通/航空 | 港股上市 | 英资+中资混合治理，保守决策文化 |
| 9 | WeBull | FinTech | 美股上市(SPAC) | 中国研发+全球运营，多法域合规 |
| 10 | 港交所 | 金融/交易所 | 港股上市 | 政府影响+商业运营双重角色，技术现代化 |
| 11 | 猎豹移动 | ISV/AI机器人 | 美股上市 | CEO思想领袖型，从工具到AI的大转型 |
| 12 | 腾讯Game | Gaming | 港股上市(母公司) | 事业群制，全球投资+自研并行，版号政策敏感 |

---

## 五、Persona 格式要求

每个 persona 文件遵循全球版结构：

1. **标题 + 元信息表格**（Title, Category, Reports to, Buying Role, Direct Reports）
2. **Reader Note + Data Usage Instruction**
3. **What a [Role] Actually Is** — 角色本质描述
4. **§1 Role Definition**
   - Archetypes（中国化：按企业类型×角色分）
   - Three Time Horizons（适配中国政策周期：五年规划、两会、Q4冲刺）
   - Four-Way Pull（适配中国权力结构：政府/党委、创始人/董事会、监管、组织）
5. **§2 Priorities** — 中国市场特有优先级（信创、出海、合规三法等）
6. **§3 KPIs & Metrics**
7. **§4 Pain Points & Objections**
8. **§5 Buying Dynamics & Decision Process**（含招投标、党委审批等中国特色）
9. **§6 Communication Style & Discovery Questions**

### 框架模块中国化适配

| 全球版概念 | 中国版适配 |
|-----------|-----------|
| Archetypes by posture | Archetypes by 企业类型×角色（央企Controller vs 出海Growth型）|
| Time Horizons: Quarterly/3Y/10Y | 季度考核 / 五年规划周期 / 政策窗口期（两会→Q4）|
| Four-Way Pull: Board+Investors+Regulators+Enterprise | 政府/党委 + 创始人/董事会 + 监管机构 + 组织/团队 |
| Information Sources: 10-K, Earnings calls | 企查查 + 招标公告 + 政策文件 + 公众号 + 行业峰会 |

---

## 六、实施计划

1. ✅ 研究12个客户（完成）
2. ✅ 确定19个角色列表（完成）
3. ✅ 设计决策文档（本文档）
4. ⬜ 撰写19个 persona 文件
5. ⬜ 创建 SKILL-CHINA.md
6. ⬜ 创建 references-china/INDEX.md
7. ⬜ 推送到 GitHub

---

*End of design decisions document.*
