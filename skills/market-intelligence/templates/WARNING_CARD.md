# Warning Card — Contract + Template

This document is the single source of truth for the Warning Card output format. It contains:
1. **Renderer rules** — the HTML renderer enforces these; violating them breaks rendering
2. **Fill-in template** — copy and fill with customer content
3. **Reasoning appendix structure** — for the second-page deliverable

---

## Part 1: Renderer Contract

The Warning Card HTML renderer (`templates/WARNING_CARD_REFERENCE.html`) expects markdown source in **exactly** the structure defined in Part 2 below. Deviating from the structure breaks rendering. Do not add sections, rename headings, or reorder.

Two files are required per customer per run:

1. **`MI_{Customer}_{YYYY-MM-DD}.md`** — the Warning Card
2. **`MI_{Customer}_reasoning.md`** — the reasoning appendix (page 2)

### Rules the HTML renderer enforces

- **Signal blocks**: the heading must match `**排名 #N · {tag}**` exactly. `N` is the rank (1, 2, 3). Each signal block must contain a `推理：` line before the `源：` line. The HTML renders the reasoning as an inline `.reason` strip between the signal body and the source links; the source list renders as clickable markdown links.
- **Source lines**: must start with `源：` and contain only markdown links separated by ` · `. Raw URLs are not permitted.
- **CoI line**: the first `$X–YM` figure is treated as Year 1 ARR; the second is treated as 3-year contract value. Both must be present. The HTML renders them as a dedicated CoI callout inside the Urgency Layer.
- **Opportunity table**: must be a GitHub-flavored 3-column table with header `| AWS 能力 | 匹配需求 | ARR（估算） |` and right-aligned numeric column.
- **Bullet labels**: sections 2 / 4 / 5 / 6 bullets use `- **label：** value` format. The `：` (fullwidth colon) is required. Each of sections 2, 4, 5, 6 must include a `- **推理：** ...` bullet. The HTML renders the `推理：` bullet as a `.reason-note` strip after the layer's content.
- **Layer 3 reasoning**: a single-line `推理：` paragraph must appear after the `独特优势` line. The HTML renders it as a `.reason-note` strip below the opportunity table.
- **Section count**: exactly sections 1–6. The Internal Data Inventory is working-memory only — **never rendered as a section** in the HTML/PDF.

### Forbidden

- Do not render Year-1 and 3-Year ARR as a single concatenated figure
- Do not include raw URLs in source lines
- Do not add sections outside the 6 required layers
- Do not render the Internal Data Inventory as a section — it is working-memory only
- Do not use emoji as structural markers — typography does that
- Do not use `**...**` inside the ARR table cells (the renderer strips it)

---

## Part 2: Warning Card Fill-in Template

Copy everything below this line, replace all `{placeholders}` with real content.

```yaml
---
customer: {Customer Name in Chinese (English translation)}
industry: {industry / sub-sector}
date: {YYYY-MM-DD}
owner: {alias or [待 AWSentral 补]}
---
```

```markdown
# 客户策略变化预警器

> AWSentral 未连接 — 内部数据字段均标 `[估算]`，外部信号全部带源。

## 预警卡 #1 · {Customer Short Name}

### 1. 信号层

**排名 #1 · {dimension tag}**
{Signal body. 2–3 sentences. Fact-based. Named figures, named events.}
推理：{One sentence — which Business Acumen dimensions this hits hardest and why this event forces a near-term decision. Inline a source label if the reasoning itself cites new evidence.}
源：[{Publication · YYYY-MM-DD}]({url}) · [{Publication · YYYY-MM-DD}]({url})

**排名 #2 · {dimension tag}**
{Signal body. 2–3 sentences.}
推理：{One sentence reasoning linking signal to dimensions.}
源：[{Publication · YYYY-MM-DD}]({url}) · [{Publication}]({url})

**排名 #3 · {dimension tag}**
{Signal body. 2–3 sentences.}
推理：{One sentence reasoning linking signal to dimensions.}
源：[{Publication · YYYY-MM-DD}]({url}) · [{Publication · YYYY-MM-DD}]({url})

观察清单：{次级信号，单行。包含观察的变化 + 可选源链接}

### 2. 影响层

- **谁：** {Named titles: X CTO + Y VP · Z CIO · ...}
- **影响：** {Specific decisions, systems, budgets reshaped by the signal(s)}
- **时间线：** {Milestone-anchored timeline}
- **推理：** {One sentence — cite Layer 1 signal rank (e.g., "来自 #1 · 并购整合 deadline")，说明 KPI 归属 → 受影响系统 → milestone 的推导链。}

### 3. 机会层 `[估算 — 需内部数据验证]`

| AWS 能力 | 匹配需求 | ARR（估算） |
|---|---|---:|
| {AWS service 1} | {Customer need} | $X–YM |
| {AWS service 2} | {Customer need} | $X–YM |
| {AWS service 3} | {Customer need} | $X–YM |
| {AWS service 4} | {Customer need} | $X–YM |
| {AWS service 5} | {Customer need} | $X–YM |

独特优势 vs {Named competitors}：{1–2 sentences on AWS differentiation grounded in customer context}

推理：{One sentence — how the ARR range was sized (analog customer / TAS 百分比 / 内部 deal registry 基准) and which internal data items are needed to validate.}

### 4. 紧迫性层

- **窗口：** {Time window anchored to a real decision event}
- **竞对：** {Competitor moves with names}
- **衰减：** {Decay curve: what happens if the window closes}
- **不行动成本（CoI）：** 本周不动 → {consequence}，首年 ARR 折损 **$X–YM · 3 年 $X–YM `[估算]`**
- **时间线推演：** 本周动 → {outcome} · 1–3 月内 → {outcome} · 过 Q{N} → {outcome}
- **推理：** {One sentence — 窗口锚在哪个事件、衰减曲线为何是这个斜率、CoI 数字如何算出；引用外部来源时内嵌标签。}

### 5. 心理层

- **状态：** {1 line on decision-maker state}
- **motion：** **{Challenger / SPIN / JOLT / Value-Based}** — {one-line rationale}
- **避坑：** {pit 1} · {pit 2} · {pit 3}
- **话术钩子：** "{One quotable sentence, in the seller's voice, referencing signal #1.}"
- **推理：** {One sentence — 为什么这个 motion 比其他三种更匹配；引用 Public Speech Summary 语录或 Layer 1 信号特征作为依据。}

### 6. 行动层 `[估算 — 需内部数据验证]`

- **本周第一步：** {One sentence: who to contact, by what channel, with what pretext.}
- **开场（引用 #1 信号）：** "{2–4 sentences of opening script. Quote a specific fact from signal #1.}"
- **核心：** ①{teaching point 1} ②{teaching point 2} ③{diagnostic question}
- **升级：** {step 1} → {step 2} → {step 3} → {step 4} → {step 5} → {final commitment}
- **推理：** {One sentence — 第一步与升级路径是 Layer 5 motion × Layer 4 窗口的直接产物；说明引用的是 #N 信号哪一事实。}

<!-- Internal Data Inventory is working-memory only — never rendered as a section in the HTML/PDF. -->

---

**下游：** 触发 `business-insight`（内含 PESTLE + Porter's 5F + BMC → SWOT/TOWS → Top Initiatives）。

*Kiro · 首席企业顾问 · 市场情报 · {YYYY-MM-DD}*
```

---

## Part 3: Reasoning Appendix Structure

### Frontmatter (required)

```yaml
---
title: 推理与逻辑
subtitle: 三个信号如何推导出本周行动
customer: {Customer Name in Chinese (English translation)}
date: {YYYY-MM-DD}
---
```

### Body structure

The appendix is composed of 5–7 sections. Each section follows this exact shape:

```markdown
## §0N · {ENGLISH_TITLE} · {中文标题}

{Optional: a paragraph or two of prose.}

| {header 1} | {header 2} | {header 3} |
|---|---|---|
| row | row | row |

- {Optional bullet} — hyphen, space, content. Bullets may contain bold with **...**
- {Optional bullet}

1. {Optional numbered step}
2. {Optional numbered step}
```

### Required reasoning sections

The canonical reasoning appendix has 7 sections. The renderer will layout whatever you give it, but for consistency across customers keep this list:

1. **§01 · THE THREE SIGNALS · 三个信号的分工** — table of signal / role / contribution
2. **§02 · WHY SIGNAL #1 · 为什么入口是 #1** — bullets on deadline / buyer / commitment / concreteness
3. **§03 · WHY {motion} · 为什么选 {motion}** — compare alternative motions
4. **§04 · THE COMPETITIVE ANGLE · {角度中文}** — explicit vs. implicit framing
5. **§05 · ESCALATION LOGIC · 升级路径的逻辑** — numbered 6-step sequence
6. **§06 · HOW THE ARR CAME FROM · {figures} 怎么来的** — estimation logic + internal data needed
7. **§07 · INTEGRITY NOTE · 可信度说明** — what must be validated before delivery

### Rules

- Section markers must be `§01`, `§02`, `§03`, ... with the `§` glyph.
- Section header format: `## §0N · ENGLISH_TITLE · 中文标题`. The three dots are `·` (middle dot, U+00B7), not hyphen/pipe.
- Tables are optional. Numbered lists and bullets coexist in a section.
- Keep paragraphs to 3–4 sentences; the renderer reserves vertical space for each section.

---

## Authoring Workflow

Copy the template in Part 2, fill in the fields, validate with a dry render, then deliver. For the reasoning appendix, use `templates/REASONING_TEMPLATE.md` as a starting point.
