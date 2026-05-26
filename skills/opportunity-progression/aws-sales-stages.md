# AWS Sales Stages (AWOS) — Exit Criteria → MEDDPICC / EDDIC Mapping

**MEDDPICC source of truth:** `MEDDPICC - Sales Stage 1.xlsx` (GCR Field Enablement). Each row in this file corresponds 1:1 to a row in the Excel's three-column table (AWOS 阶段 / Exit Criteria 推进标准 / 元素协同). Text is preserved verbatim from the Excel.

**EDDIC source:** EDDIC-AWS Stage synergy reference (Slide 5–6).

**Mapping granularity (CRITICAL):** Each row is ONE exit-criterion → element mapping. When a single exit criterion maps to multiple elements, the Excel lists it as multiple rows; this file preserves that row granularity. Phase 3 evaluates each row individually when scoring exit criterion completion and element alignment.

**Tier selection rule:** Simple (EDDIC) analysis reads the **EDDIC Stage Mapping** section. Strategic (MEDDPICC) analysis reads the **MEDDPICC Stage Mapping** section. Do not mix — EDDIC at Simple tier does not analyze M / P / CH dimensions.

**Abbreviation note:** The source Excel uses **CP** for Competition and **PP** for Paper Process. Canonical abbreviations across this skill are **CP** (Competition — aligned with Excel) and **P** (Paper Process). Downstream SKILL.md phases read PP ≡ P; legacy external MEDDPICC training materials that use "CO" for Competition are treated as synonyms of CP during parsing (see meddpicc-framework.md terminology note).

---

# MEDDPICC Stage Mapping (Strategic tier, 8 elements)

All 32 rows below map 1:1 to `MEDDPICC - Sales Stage 1.xlsx`.

| # | AWOS 阶段 | Exit Criteria 推进标准 | 元素协同 |
|---|---|---|---|
| 1 | Prospect | 已发现客户机会 | **I (Implicate the Pain):** 识别潜在痛点/需求 ； 客户的迫切事件 |
| 2 | Prospect | 机会拥有具有有效估计价值产品（非零美元价值） | **E (Economic Buyer):** 初步预算方向 |
| 3 | Prospect | 机会拥有具有有效估计价值产品（非零美元价值） | **M (Metrics):** 建立有依据的机会价值估算 |
| 4 | Prospect | 已安排与客户的初次会面 | **DP (Decision Process):** 启动对接过程，谁来负责落实战略方案 |
| 5 | Prospect | 已安排与客户的初次会面 | **CH (Champion):** 评估这个接触人是否有可能成为 Champion |
| 6 | Qualified | 客户愿意寻求解决方案 | **I (Implicate the Pain):** 已验证的痛点；买家期望的业务成果是什么？ |
| 7 | Qualified | 客户愿意寻求解决方案 | **M (Metrics):** 已定义初始业务成功指标 |
| 8 | Qualified | 已确定客户客户内部支持者/决策者 | **CH (Champion):** 已确认客户内部支持者 |
| 9 | Qualified | 已确定客户客户内部支持者/决策者 | **DP (Decision Process):** 清楚知道预算和时间框架 |
| 10 | Qualified | 已确定客户客户内部支持者/决策者 | **E (Economic Buyer):** 已识别最终决策者 |
| 11 | Qualified | 已确定交付合作伙伴策略（合作伙伴和/或 ProServe) | **CP (Competition):** 已确定竞争策略 |
| 12 | Qualified | 已确定交付合作伙伴策略（合作伙伴和/或 ProServe) | **DP (Decision Process):** 实施方法明确；技术决策过程涉及哪些步骤和相关人员？ |
| 13 | Technical Validation | 客户和 AWS 对解决方案的架构、实施和流程有共同的认识。 | **DC (Decision Criteria):** 技术需求已达成一致 |
| 14 | Technical Validation | 客户和 AWS 对解决方案的架构、实施和流程有共同的认识。 | **DP (Decision Process):** 实施流程已确定 |
| 15 | Technical Validation | 客户和 AWS 对解决方案的架构、实施和流程有共同的认识。 | **M (Metrics):** 技术成功指标已建立 |
| 16 | Technical Validation | 已最终确定技术解决方案设计，并且和客户达成一致。 | **DC (Decision Criteria):** 技术成功评估指标已设立已经排除了不采取行为的选择 |
| 17 | Technical Validation | 已最终确定技术解决方案设计，并且和客户达成一致。 | **CH (Champion):** 获得技术客户内部支持者的认同 |
| 18 | Technical Validation | 已最终确定技术解决方案设计，并且和客户达成一致。 | **M (Metrics):** 技术指标已确认 |
| 19 | Business Validation | 取得了客户方的相关审批 | **E (Economic Buyer):** 最终决策者批准 |
| 20 | Business Validation | 取得了客户方的相关审批 | **DP (Decision Process):** 已审查成交计划并确认成交日期；已解决可能会影响采购的决策 |
| 21 | Business Validation | 取得了客户方的相关审批 | **P (Paper Process):** 了解客户的采购步骤；初始审批文件 _(Excel 原写 "PP")_ |
| 22 | Business Validation | 与客户共同审查交易的各项内容，并就商务条款和成单计划达成一致 | **M (Metrics):** 财务指标已确认 |
| 23 | Business Validation | 与客户共同审查交易的各项内容，并就商务条款和成单计划达成一致 | **P (Paper Process):** 合同流程已确定 _(Excel 原写 "PP")_ |
| 24 | Business Validation | 与客户共同审查交易的各项内容，并就商务条款和成单计划达成一致 | **E (Economic Buyer):** 商务条款已达成一致 |
| 25 | Committed | 客户解决方案开始迁移到 AWS，或者客户使用量达到机会 MRR 价值（实用程序和已经确认合同）的10% (GCR Practice: 80%) | **M (Metrics):** 迁移方案能满足业务指标 |
| 26 | Committed | 客户解决方案开始迁移到 AWS，或者客户使用量达到机会 MRR 价值（实用程序和已经确认合同）的10% (GCR Practice: 80%) | **DC (Decision Criteria):** 明确了部署时间表 |
| 27 | Committed | 客户已签署协议（私有定价协议） | **P (Paper Process):** 合同条款已完成谈判并执行 _(Excel 原写 "PP")_ |
| 28 | Committed | 客户已签署协议（私有定价协议） | **E (Economic Buyer):** 最终获得最终决策者合同确认 |
| 29 | Closed / Launched | Closed/Launched 是商机推进的最后一个阶段，表明已赢得该商机。 | **DP (Decision Process):** 满足项目决策流程要求 |
| 30 | Closed / Launched | Closed/Launched 是商机推进的最后一个阶段，表明已赢得该商机。 | **M (Metrics):** 实施后能满足之前的业务指标 |
| 31 | Closed / Launched | Closed/Launched 是商机推进的最后一个阶段，表明已赢得该商机。 | **DC (Decision Criteria):** 满足项目决策标准 |
| 32 | Closed / Launched | Closed/Launched 是商机推进的最后一个阶段，表明已赢得该商机。 | **P (Paper Process):** 交付相关文件已完成签署 _(Excel 原写 "PP")_ |

---

# EDDIC Stage Mapping (Simple tier, 5 elements)

Use this mapping when the opportunity is classified as **Simple (EDDIC)**. Only 5 elements are in scope: **I, E, DC, DP, CP** (Competition). M, P, CH are not assessed at this tier.

**Note:** EDDIC mapping is NOT in the MEDDPICC Excel. It follows the EDDIC-AWS Stage synergy reference (Slide 5–6). Same row-per-mapping granularity as MEDDPICC.

| # | AWOS 阶段 | Exit Criteria 推进标准 | 元素协同 |
|---|---|---|---|
| 1 | Prospect | 已发现客户机会 | **I (Implicate the Pain):** 识别潜在痛点/需求；客户的迫切事件 |
| 2 | Prospect | 机会拥有具有有效估计价值产品（非零美元价值） | **E (Economic Buyer):** 初步预算方向 — EDDIC 在 Prospect 阶段就要求初始预算方向，缺失即 foundation gap |
| 3 | Prospect | 已安排与客户的初次会面 | **DP (Decision Process):** 启动对接过程，谁来负责落实战略方案 |
| 4 | Qualified | 客户愿意寻求解决方案 | **I (Implicate the Pain):** 已验证的痛点；买家期望的业务成果 |
| 5 | Qualified | 已确定客户内部支持者/决策者 | **DP (Decision Process):** 清楚知道预算和时间框架 |
| 6 | Qualified | 已确定客户内部支持者/决策者 | **E (Economic Buyer):** 已识别最终决策者 |
| 7 | Qualified | 已确定交付合作伙伴策略（合作伙伴和/或 ProServe) | **CP (Competition):** 已确定竞争策略 |
| 8 | Qualified | 已确定交付合作伙伴策略（合作伙伴和/或 ProServe) | **DP (Decision Process):** 实施方法明确 |
| 9 | Technical Validation | 客户和 AWS 对解决方案的架构、实施和流程有共同的认识 | **DC (Decision Criteria):** 技术需求已达成一致 |
| 10 | Technical Validation | 客户和 AWS 对解决方案的架构、实施和流程有共同的认识 | **DP (Decision Process):** 实施流程已确定 |
| 11 | Technical Validation | 已最终确定技术解决方案设计，并且和客户达成一致 | **DC (Decision Criteria):** 技术成功评估指标已设立；已排除"不采取行动"的选项 |
| 12 | Business Validation | 取得了客户方的相关审批 | **E (Economic Buyer):** 最终决策者批准 |
| 13 | Business Validation | 取得了客户方的相关审批 | **DP (Decision Process):** 已审查成交计划并确认成交日期 |
| 14 | Business Validation | 与客户共同审查交易的各项内容，并就商务条款和成单计划达成一致 | **E (Economic Buyer):** 商务条款已达成一致 |
| 15 | Committed | 客户解决方案开始迁移到 AWS，或者客户使用量达到机会 MRR 价值的 10% | **DC (Decision Criteria):** 明确了部署时间表 |
| 16 | Committed | 客户已签署协议（私有定价协议） | **E (Economic Buyer):** 最终获得最终决策者合同确认 |
| 17 | Closed / Launched | Closed/Launched — 已赢得该商机 | **DP (Decision Process):** 满足项目决策流程要求 |
| 18 | Closed / Launched | Closed/Launched — 已赢得该商机 | **DC (Decision Criteria):** 满足项目决策标准 |

---

## EDDIC vs MEDDPICC — Key Structural Differences

1. **No Champion scoring:** Internal supporter presence is a Phase 5 relationship sanity check in EDDIC, not a scored element.
2. **Prospect stage has an E gate:** Unlike MEDDPICC where E becomes critical at Qualified, EDDIC requires initial budget direction at Prospect. Zero E at Prospect = foundation gap.
3. **CP terminology:** Competition is abbreviated **CP** across the skill, Excel template, and EDDIC documentation. Legacy external MEDDPICC training materials that use "CO" are treated as synonyms of CP; downstream output always emits CP. Similarly, Excel "PP" ≡ SKILL.md "P".
4. **Only relevant EDDIC elements scored per stage:** At each stage, only the elements explicitly mapped to that stage's exit criteria are scored. Elements not in the mapping remain at their prior-stage score.

---

# Stage Progression Gates (Strategic / MEDDPICC tier only)

Beyond the per-stage exit criteria above, AWS imposes additional **progression gates** that an opportunity must satisfy when advancing to a more advanced stage. These gates are policy-level — they can override even a strong exit-criteria aggregate when key signals are missing.

**Scope:** Strategic (MEDDPICC) tier only. Simple (EDDIC) tier does not impose these gates because M, P, CH are not assessed at Simple tier.

**Evaluation cadence:** Always evaluated in Phase 2.5 alongside the Stakeholder Gate and Exit Criteria Gate. The gate that applies is the one whose **source stage matches the current_stage** — i.e., this gate evaluates whether the opportunity, as it stands at the reported stage, is qualified to advance to the next stage.

| # | Source Stage | Target Stage | Required Conditions (all must be satisfied) |
|---|---|---|---|
| 1 | Qualified | Tech Validation | (a) Total Score ≥ 65 / 100 · (b) E 第 1 条陈述（"已与 EB 接触并提及该项目"）= Yes · (c) I = 100% · (d) CH = 100% |
| 2 | Tech Validation | Business Validation | Same as row 1 (Total ≥ 65, E S1 = Yes, I = 100%, CH = 100%) |
| 3 | Business Validation | Committed | (a) Total Score ≥ 80 / 100 · (b) E = 100% (all 3 statements = Yes) |

**Notes:**

- Rows 1 and 2 share the same gate by design — the policy authority requires Tech and Business Validation entry to clear the same minimum bar.
- Row 3's stricter Total ≥ 80 reflects the policy that contract-level commitment requires substantially higher overall opportunity health.
- "E 第 1 条陈述" and "E = 100%" both reference the MEDDPICC Scorecard's Economic Buyer element. The first is statement-level (a single Yes/No), the second is element-level (all 3 statements = Yes, 13/13 score).
- These gates are **diagnostic**, not enforcement — Phase 2.5 surfaces a Stage Progression Gate result; the analyst decides how to act. The result joins the existing Stakeholder Gate and Exit Criteria Gate in the alignment card.

**Source:** GCR Field Enablement policy (transcribed verbatim into structured form here for use by M.12 in `SKILL.md`).
