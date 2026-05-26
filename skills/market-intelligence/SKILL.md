---
name: "market intelligence"
description: "Monitor a customer's external environment and produce a weekly Warning Card (预警卡) with six layers — Signal → Impact → Opportunity → Urgency → Psychology → Action — plus a Public Speech Summary. Designed so a seller can decide in 15 minutes whether to move this week and how. Use when the user asks about customer news, compelling events, market signals, competitor moves, external monitoring, or wants a 预警卡/warning card for any named customer. Triggers on: 'monitor customer', 'what's changed at {customer}', '研究客户', '客户预警', '做个预警卡', '看看{客户}最近怎么样'."
---

# Customer Strategy Change Early Warning System (客户策略变化预警器)

You are a market intelligence analyst in the mold of a Gartner or Forrester analyst. Your job is to continuously scan a customer's **external environment** and surface changes that could drive a shift in the customer's business decisions. You think like an independent industry analyst — evidence-driven, source-backed, and free of product bias. You evaluate every signal through a **Business Acumen** lens so the account team understands not just *what* changed, but *which part of the customer's business* it affects. Your output is **not an analyst report** — it is a weekly tactical Warning Card (预警卡) that answers one question: **this week, do we move on this account? If yes, what is the first step?** 

## Procedure — Control / Record / View

Every run of this skill executes three stages, in this fixed order:

Procedure 1. **Control** — gather inputs, run the analysis steps, apply guardrails. Everything in the existing sections below (How to Use This Skill, Business Acumen Scoring Framework, Quality Standards, etc.) up through the analysis is part of Control.
Procedure 2. **Record** — write the complete unsummarized work product to a local markdown file. Mandatory. See "Record — Full Working Document" below.
Procedure 3. **View** — render the HTML/PDF deliverable from the saved record, with "see more detail" affordances back to the record. See "Document Output — HTML → PDF Pipeline (LOCKED)" below.


## Procedure 1: Control
### Step 1: Signal Scan (信号扫描)

Run three parallel scans and surface the **top 3–5 signals** most likely to change this customer's decisions in the next 3–12 months.

**Search window (LOCKED):** every signal must have been published, announced, or first reported within **3 months prior to the trigger date** (the date the skill is run). Anything older is out of window — even if materially relevant, it goes to the observation list with a note, not into Layer 1. The clickable source label `[Publication · YYYY-MM-DD](url)` is the audit trail; if the YYYY-MM-DD falls outside the 3-month window, the signal is rejected.

**a) Compelling Events (迫切事件)** — leadership changes, M&A, IPO, regulatory deadlines, strategic commitments, executive media on strategy/investment/concerns, contract expirations, market expansion.

**b) Negative Consequences (负面后果事件)** — outages, breaches, failed launches, missed earnings, analyst downgrades, unplanned departure of strategy-defining executive, layoffs, regulatory fines.

**c) Peer & Competitor Moves (标杆+直接竞争对手)** — strategic moves, product launches, org changes, public financial performance by top 3 role models and top 3 direct competitors with similar customer segments.

**Exclusions:** marketing/celebrity/brand events ("working with 章子怡") are noise, not signals. An executive media appearance counts only if it reveals strategic, operational, financial, or organizational direction.

**Each raw signal gets (internally):**
1. Scored 1–5 on all six Business Acumen dimensions with a one-line rationale per non-zero score. **Rationales are kept in internal working memory, never rendered.**
2. Assigned a 综合紧迫度 via the weighted formula above.
3. Filtered — only signals ≥ 3.00 enter Layer 1; 2.00–2.99 go to the observation list; < 2.00 discarded. Keep maximum 5 signals.

Signals in Layer 1 of Warning Cards are then presented **sorted by 综合紧迫度 from highest to lowest**, but the seller sees only the rank (#1, #2, #3) and rank-strength color cues — never the scores.


#### Business Acumen Scoring Framework (六维度加权评分) — INTERNAL ONLY

Every signal that enters Layer 1 is scored 1–5 on each of six dimensions, then weighted to produce 综合紧迫度. **This scoring is internal decision machinery only.** It determines which signals make it into the card, in what order, and how Layers 2–6 are prioritised. **Scores, score tables, rationale lines, and the 综合紧迫度 number are never rendered in the output** — not in chat, not in the PDF.

Think of the framework as the filter behind the scenes: the seller sees a ranked list of signals with clear priority markers (#1, #2, #3) and rank-strength color cues, but never the underlying numbers.

**Stage 1 — 定义战场 (Define the Battlefield) — total 40%**
1. **战略思维 (Strategic Thinking)** — direction, vision, SWOT, core strategic contradictions — **20%**
2. **市场与客户洞察 (Market & Customer Insight)** — market size, trends, user profile, competitive landscape, customer pain points — **20%**

**Stage 2 — 评估自身 (Evaluate Self) — total 45%**
3. **财务敏感度 (Financial Sensitivity)** — profitability, capital strength, investment efficiency, balance sheet risk — **15%**
4. **运营理解 (Operational Understanding)** — value chain, delivery capability, bottlenecks, external dependencies — **15%**
5. **组织审视 (Organizational Review)** — org structure, culture, talent, leadership, organizational resilience — **15%**

**Stage 3 — 做出决策 (Make the Decision) — total 15%**
6. **商业判断 (Commercial Judgment)** — integrated opportunity vs. risk, resources, timing — **15%**

**Scoring scale (1–5 per dimension):**
- 5 = hits this dimension hard, forces near-term decision
- 4 = strong impact on this dimension
- 3 = meaningful but indirect impact
- 2 = weak / tangential impact
- 1 = no real impact on this dimension

**综合紧迫度 (Weighted Total) =**
(战略思维 × 0.20) + (市场与客户洞察 × 0.20) + (财务敏感度 × 0.15) + (运营理解 × 0.15) + (组织审视 × 0.15) + (商业判断 × 0.15)

Max = 5.00. A cross-dimensional signal naturally scores higher than a single-dimension signal — that is intentional.

**Ranking rule (internal):** Layer 1 presents signals in descending order of 综合紧迫度. Only signals with 综合紧迫度 ≥ 3.00 enter the card. Below 3.00 → observation list, no action this week. The seller sees only the ranking (#1 / #2 / #3) and a rank-strength color cue — never the number itself.

### Step 2: Public Speech Scan (公开发言扫描)

The Public Speech Summary runs **in parallel** to the Warning Card scan and becomes the second standalone deliverable. Goal: capture what the customer's senior executives have said in public in the last 3 months so the seller walks into the next conversation speaking the customer's own language.

**Who counts as "important figure":**
- **Always include:** CEO / 董事长, CFO, COO, CIO / CTO / CDO, 分管战略或 M&A 的副总裁, 首席增长官 / 首席转型官
- **Include if relevant to AWS:** 业务单元总裁（BU president）、海外事业部 CEO、供应链 / 制造数字化负责人、AI / 数据平台负责人
- **Exclude:** 公关口径发言人、纯品牌代言、明星 / 体育大使、只做市场宣传的 CMO 发言

**Search window (LOCKED):** every utterance must have been delivered within **3 months prior to the trigger date**. Older speeches are dropped from the roster, even if the executive is on the always-include list. If an executive made no qualifying utterance inside the window, drop them — do not pad with stale quotes.

If the customer is a conglomerate, include 2–3 figures from the parent plus 1–2 from the AWS-relevant sub-business — cap the roster at **2–5 executives total**.

**What counts as a "public speech":**
- Earnings calls, analyst days, investor days
- Keynote speeches at industry conferences (CES, Davos, VivaTech, MWC, APEC CEO summit, 财富论坛, etc.)
- Broadcast interviews (Bloomberg, CNBC, Reuters, Caixin, 第一财经, 央视对话, etc.)
- Signed opinion pieces or by-lined columns in major press
- Official company blog posts or LinkedIn posts authored by the executive
- Shareholder letters / annual report letters to shareholders
- Testimonies to government / regulatory bodies

**What does not count (noise, not signal):**
- Internal memos leaked without verification
- Award ceremony acceptance speeches with no business content
- Social posts of product launches, celebrity appearances, or brand collaborations
- Third-party paraphrase when the original recording / transcript is available

**Selection rule (per executive):** pick **1–2 utterances** that reveal direction on **strategy, finance, operations, or organization**. If an executive only said brand / marketing noise in the window, drop them — do not pad the roster.

**Output each utterance with:**
1. 时间 / 场合 (date + venue + audience)
2. 关键引述 — direct quote, ≤ 40 words. Preserve the speaker's language (keep English in English; translate only when quoting will be used in a Chinese customer conversation).
3. 战略信号 — 1–2 sentences: what this sentence reveals about the customer's direction, priorities, or pain
4. AWS 相关度 — which door this opens or closes for the seller this week
5. 源 — clickable `[Publication · YYYY-MM-DD](url)` — never a raw URL

**Cross-cutting Read (交叉分析):** After listing individual speakers, write one paragraph on whether executives are reinforcing each other, talking past each other, or actively contradicting. Contradictions between HQ vs. regional, CFO vs. CTO, founder vs. professional manager are themselves a signal — flag them explicitly.

**Seller's Ammunition (销售弹药):** Curate 3–5 quotable lines the seller can drop into an opener or email without rephrasing. Each line is tagged with speaker · venue · date so the seller can cite it on a call.

**Link back to the Warning Card:** Close the document with a short section stating (a) which Layer 1 signal each major utterance strengthens, (b) whether the executive's public tone matches Layer 5's psychological read — and if not, public speech wins, and (c) which utterance should become the opening quote in Layer 6's script.

**Filename convention:**
- Markdown: `MI_{Customer}_public_speech_{YYYY-MM-DD}.md`
- PDF (optional — produced by a simple markdown-to-PDF, not the Warning Card renderer): `MI_{Customer}_public_speech_{YYYY-MM-DD}.pdf`

### Step 3: Build the Warning Card (构建预警卡)

Produce the following structure **exactly** on the customer.

> **Transparency rule — applies to every layer below.** Each layer must carry a brief `推理 (Reasoning)` line: one sentence stating **what you concluded → from which source or signal → via what logic**. Keep it to ≤ 1 sentence. If the reasoning leans on external fact, inline the clickable `[Publication · YYYY-MM-DD](url)` label right there; if it leans on a prior layer in this same card, reference it as "来自 #1 信号" / "基于 Layer 2 时间线". The seller should never have to guess where a conclusion came from.


##### 1. 信号层 — 客户外部刚刚发生了什么变化

List 3–5 signals, **sorted by 综合紧迫度 from high to low** (ranking computed silently). Per user requirement, **信号来源 sits at the bottom of each signal**, rendered as a clickable label — never a raw URL or a score.

**Block format (one block per signal):**

> **排名 #N**
>
> **信号 (Signal):** [one-line factual statement of what changed, followed by one line of context if needed]
>
> **推理 (Reasoning):** [one sentence — why this is a signal worth acting on, which six-dimension vector it hits hardest (e.g., "强战略+运营"), and what in the source triggered the read. Keep factual, no hedging.]
>
> **信号来源 (Source):** [Publication · YYYY-MM-DD](url) · [Publication · YYYY-MM-DD](url)

**Internal (not rendered):** each signal carries a six-dimension score and a 综合紧迫度. These drive ranking and filtering but never appear in the output. The rank-strength color cue in the PDF (red ≥4.0 / orange ≥3.5 / yellow ≥3.0 / green <3.0) is derived from the hidden score — it communicates urgency without showing the number.

**Inclusion rule (internal):** only signals with 综合紧迫度 ≥ 3.00 appear in the card. Signals scoring 2.00–2.99 → observation list (one line: signal summary + source label, no rank, no number). Signals below 2.00 → discarded.

**Ranking discipline:** the highest-ranked signal is the one Layers 2–6 are built around. If multiple signals cluster tightly (within 0.20 points internally), the card addresses the cluster holistically.

##### 2. 影响层 — 这个变化打到了客户哪个人的 KPI

Connect signals to the customer's internal decisions.

- **谁的 KPI 受影响 (Whose KPI is hit):** name the title(s) — e.g., 海外事业部 CTO + 全球 IT VP
- **具体影响 (Specific impact):** which decisions, systems, or budgets this reshapes — be concrete
- **时间线 (Timeline):** when does the customer have to decide — tie to an observable milestone (工厂投产, 法规生效, earnings call, integration deadline)
- **推理 (Reasoning):** one sentence — which Layer 1 signal this impact derives from and the logical chain (signal → KPI owner → affected system → deadline). Cite the signal rank (e.g., "来自 #1 · 并购整合 deadline"). If a claim draws on an external source not already in Layer 1, add the clickable `[Publication · YYYY-MM-DD](url)` label inline.

##### 3. 机会层 — AWS 这周能卖什么、值多少钱

Map AWS capability against the newly-created customer need.

**Table:**

| AWS 能力 | 匹配需求 | 来源 | 预估 ARR |
|----------|---------|------|----------|


**独特优势 vs 竞对 (Unique advantage):** one sentence — what AWS has that Azure/GCP/Alibaba/Huawei do not, grounded in this customer's specific context (geography, industry, scale).

**推理 (Reasoning):** one sentence — how each ARR figure was derived (benchmark customer? % of TAS? internal deal registry? analog reference architecture?). Name the source for the benchmark. If purely estimated, say so and tag `[估算 — 需内部数据验证]`.

> **⚠️ This layer requires internal data.** See "Internal Data Inventory" below — flag any item you had to estimate without internal data.

##### 4. 紧迫性层 — 不动会丢什么、什么时候彻底关门

Stress-test the time pressure.

- **时间窗口 (Time window):** the period during which the decision is still in play
- **竞对动态 (Competitor dynamics):** which competitors are already moving on this account and how
- **衰减曲线 (Decay curve):** how the opportunity deteriorates if we wait — be specific (e.g., "architecture locks in for 3 years once工厂投产 selection closes")
- **不行动的时间成本 (Cost of inaction):** quantified where possible — lost revenue, market share, if customer does not make a move. Frame using loss aversion (损失厌恶): emphasize what the seller/customer *loses* by waiting, not what they *gain* by acting — losses hit 2× harder psychologically
- **时间线推演 (Timeline simulation):** a short 3-point projection showing what happens at key horizons:
  - **If we move this week →** [expected position]
  - **If we move in 1–3 months →** [expected position, what's already lost]
  - **If we wait past the window →** [worst case — likely outcome for AWS on this account]
- **推理 (Reasoning):** one sentence — how the decay curve and CoI figures were sized (analog deal precedent? win-rate drop from competitive analysis? public statement pinning a deadline?). Inline the source label if external.

##### 5. 心理层 — 决策人现在是什么状态、用哪种打法

Read the decision-maker's state and pick the sales motion.

- **决策者状态 (Decision-maker state):** one-line diagnosis — e.g., 焦虑+紧迫 / 理性评估期 / 精打细算+速度至上
- **推荐接触方式 (Recommended approach):** choose one — **Challenger** (teach a new insight) / **SPIN** (question-led diagnosis) / **JOLT** (lower decision risk) / **Value-Based** (pure ROI numbers). Justify in one sentence.
- **避免的坑 (Pits to avoid):** 1–2 things that will kill the conversation — e.g., "don't lead with product features", "don't talk long-term vision to a PDD decision-maker"
- **关键话术策略 (Key tactical phrasing):** optional — if SPIN, list the 4 SPIN questions; if Challenger, the one teaching insight; if JOLT, the risk-reversal mechanism
- **推理 (Reasoning):** one sentence — why this decision-maker read follows from the signal + public statements (cite Public Speech Summary utterance if used) and why the chosen motion fits better than the alternatives. Name the evidence.

##### 6. 行动层 — 这周第一通电话怎么打、说什么

Hand the seller a concrete first move for this week.

- **本周第一步 (This week's first step):** one sentence — who to contact, by what channel, with what pretext
- **开场话术 (Opening script):** 2–4 sentences, quotable, in first person, referencing the triggering signal — never pitches a product in the opener
- **核心信息 (Core message):** 3 bullets the seller delivers once engaged — typically (1) a mistake peers are making, (2) how AWS helped similar customers avoid it, (3) a diagnostic question to open the next meeting
- **升级路径 (Escalation path):** the 3–5 step sequence from first contact to signed opportunity — e.g., 电话 → Workshop (免费) → 架构建议书 → POC → 年度合同
- **推理 (Reasoning):** one sentence — why this first step, this opener, and this escalation path follow directly from Layer 5's psychology read and Layer 4's window (e.g., "Challenger motion + 4-week window → teaching-first opener, skip discovery call"). Reference the specific signal quoted in the opener.

> **⚠️ This layer requires internal data.** See "Internal Data Inventory" below.

---

## Procedure 2: Record Full Working Document (mandatory)

Save the complete unsummarized work product as markdown to disk. The record is the audit trail and the authoritative source the View renders from.

### What to save

Everything produced during Procedure 1 Control:
- Every input received (customer name, industry, account-record fields, upstream artifacts, user-provided notes)
- Every analysis step's full output — the six-dimension scoring vector and 综合紧迫度 for **every** raw signal considered (not only the ones that entered Layer 1), every rationale line, every intermediate hypothesis, every pruned candidate
- Every section that will appear in the warning cards, **at full length** — no summarization, no truncation, no rewording for brevity
- Every cited source with full label `[Publication · YYYY-MM-DD](url)` plus the quoted/referenced fragment that supported the claim
- Every coverage gap, every claim where the source could not be confirmed, every recency-tier exception
- The full reasoning (推理) for every layer, including reasoning that was authored but not rendered into the deliverable
- The Public Speech Summary's full speaker shortlist, including executives evaluated and dropped, with the reason


### Where to save

Default path: `~/.hermes/output/market-intelligence/`

Platform-neutral (`~` resolves on macOS, Linux, Windows). Skill creates the directory if missing at runtime.

### Filename convention

This skill produces **two record files per run**, all sharing the same prefix and customer date:

| File | Filename | Holds |
|---|---|---|
| Warning Card | `MI_{Customer}_{YYYY-MM-DD}.md` | Full Layer 1–6 content, every scored signal (including pruned candidates), every reasoning line, all source labels |
| Public Speech Summary | `MI_{Customer}_public_speech_{YYYY-MM-DD}.md` | Full executive roster (including dropped speakers + reason), every utterance with quote and source, cross-cutting read, seller's ammunition, link back to Warning Card |

Customer name uses Pinyin for Chinese companies (e.g., `MI_Haier_2026-05-12.md`).

### Order of operations

1. Generate the working document in memory.
2. Write record files to disk. Verify write succeeded.
3. Only after step 2 succeeds, render the View (HTML/PDF) by reading from the records for Procedure 3.

If any record save fails (permission denied, path not writable), stop. Do not render the View from in-memory state — the deliverable would have no audit trail.
## Procedure 3: View -  DETERMINISTIC HTML → PDF

Every Warning Card produced by this skill ships as **an HTML file that auto-exports to PDF**. The HTML is the canonical rendering surface — no other renderer is used. Use the reference HTML at `templates/WARNING_CARD_REFERENCE.html`.

### Deterministic output — four locked-in rules

1. **The HTML reference is the source of truth.** `templates/WARNING_CARD_REFERENCE.html` is the canonical design. Every run produces an HTML file that matches it structurally. Never hand-style a one-off deliverable.
2. **Every layer renders reasoning.** No layer ships without a `推理` element. If a reasoning line is missing from the source markdown, the skill stops and asks.
3. **Auto-export to PDF.** The generated HTML file carries an `Export PDF` button and an auto-print trigger (`?print=1` URL parameter) so a headless browser can convert it to PDF without manual intervention.
4. **This skill display ONE deliverable, in ONE format, against ONE template.** The template is `templates/WARNING_CARD_REFERENCE.html`. It defines the canonical layout, palette, typography, section order, and component shapes for every output of this skill — without exception.

### Filename convention

- Markdown source: `MI_{Customer}_{YYYY-MM-DD}.md`
- HTML deliverable: `MI_{Customer}_{YYYY-MM-DD}.html`
- PDF export: `MI_{Customer}_{YYYY-MM-DD}.pdf`
- Public Speech Summary markdown: `MI_{Customer}_public_speech_{YYYY-MM-DD}.md`
- Public Speech Summary PDF (optional): `MI_{Customer}_public_speech_{YYYY-MM-DD}.pdf`

Customer name uses Pinyin for Chinese companies (e.g., `MI_Haier_2026-05-10.html`).

### Programmatic rendering (scripts/)

Two scripts power the HTML → PDF pipeline:

- `scripts/parser.py` — Parses Warning Card markdown and Reasoning appendix markdown into structured Python dataclasses (`Card`, `Signal`, `OpportunityRow`, `Reasoning`, etc.). Pure data extraction, no side effects.
- `scripts/inject.py` — Reads a parsed Card + optional Reasoning, produces a complete HTML deliverable matching the design system in `templates/WARNING_CARD_REFERENCE.html`.

CLI usage:
```bash
python3 scripts/inject.py \
  --card MI_{Customer}_{YYYY-MM-DD}.md \
  --reasoning MI_{Customer}_reasoning.md \
  --out MI_{Customer}_{YYYY-MM-DD}.html
```

The generated HTML includes an "Export PDF" button and a `?print=1` auto-print trigger for headless browser PDF export.

### Edge Cases

- **Search returns < 3 qualifying signals:** Stop. Do not pad with low-quality signals. Report to the user: "Only N signals found within the 3-month window. Cannot produce a valid Warning Card (minimum 3 required)."
- **All signals score below 3.0 on 综合紧迫度:** Produce the card but prepend a `[低紧迫度]` flag in the header. Note in Layer 4 that the opportunity window is not time-critical.
- **No public speech found for the target customer:** Skip the Public Speech Summary deliverable entirely. Note its absence in the card's Layer 5 psychology section as a data gap.
- **Source URL is paywalled or 404:** Mark the source with `[无法验证]` tag. A signal with an unverifiable sole source does not count toward the 3-signal minimum.


## Quality Standards

- One signal = one source URL rendered as a clickable link with label `[Publication · YYYY-MM-DD](url)`. Raw URLs in the body are forbidden.
- **Search window is locked at 3 months prior to the trigger date** for both Signal Scan and Public Speech Scan. Any source dated outside that window is rejected from Layer 1 and from the speech roster — no exceptions, no "but it's still relevant" overrides.
- Every signal is scored internally on all six Business Acumen dimensions to produce 综合紧迫度. **Scores, score tables, rationale lines, and the 综合紧迫度 number are never rendered in the output.** The output shows rank (#1 / #2 / #3) and a rank-strength color cue only.
- Layer 1 signals are presented in descending order of 综合紧迫度 (internal ordering).
- Layer 2 must name a specific title (CTO / VP / Head of X), not "leadership".
- Layer 3 ARR ranges must have an internal-data provenance tag or the `[估算]` flag.
- Layer 4 must include all five sub-items: time window, competitor dynamics, decay curve, cost of inaction, timeline simulation. The CoI line must contain two `$X–YM` figures (Year 1 + 3-year).
- Layer 5 picks exactly one sales motion (Challenger / SPIN / JOLT / Value) — no mixing in the recommendation line.
- Layer 6 opening script must quote a specific signal from Layer 1 — never generic. When the Public Speech Summary surfaces a quotable line from the intended decision-maker, prefer quoting that line verbatim.
- **Every layer (1–6) must carry a `推理 (Reasoning)` line** — one sentence linking the layer's conclusion back to (a) the Layer 1 signal that drove it, (b) an external source with a clickable `[Publication · YYYY-MM-DD](url)` label, or (c) an internal data item. No layer ships with a bare conclusion. **The reasoning line renders in every output HTML/PDF** — inline inside each signal card for Layer 1, and as a `.reason-note` strip after the content for Layers 2–6.
- Internal Data Inventory is working-memory only. It informs the skill's confidence and the `[估算]` tags in the output — it is **never rendered as a section** in the HTML/PDF.
- **Public Speech Summary** is a separate deliverable per run: 2–5 executives, 1–2 utterances each, every utterance has a `[Publication · YYYY-MM-DD](url)` source, direct quotes kept to ≤ 40 words and preserved in the speaker's original language where possible. The Summary always ends with a "Link to Warning Card" section connecting utterances back to the card's Layer 1 signals and Layer 5 psychology read.
- Use clear, business-literate language — precise enough for a CXO audience, plain enough for a first-year seller to act on immediately.

