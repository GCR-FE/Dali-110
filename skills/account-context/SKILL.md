---
name: "account-context"
description: "Machine-to-machine foundation skill. Given a customer name and industry, produces structured context (org chart, relationship map, IT landscape, competitive landscape, other-cloud/GenAI footprint, buying behavior) for downstream skills to consume. Invoked only by other skills (business-insight, solutions-search, competitive-intelligence, bttroc, market-intelligence, opportunity-progression) — not exposed as a user-facing trigger. Sources are public web research and caller-provided input only — no internal AWS systems."
---

# account-context

Machine-readable customer context provider. Output is structured data for other agents to consume — not a human-facing deliverable.

This skill produces facts and named gaps. Interpretation (SWOT, TOWS, strategic actions, CXO narrative) belongs to downstream skills.

Internally split into two procedures:
- **Procedure 1 — Analysis** (Steps 1–5): research, mapping, hypothesis generation, filtering.
- **Procedure 2 — Output** (JSON schema, persistence, downstream contract).

## Operating Constraints

- **Foundation, not analysis.** Surface facts and gaps. No interpretation.
- **Gaps are findings.** Every Unknown / `[未公开披露]` / `[AI推断]` field is a discovery action returned in the output, not padding.
- **Industry standard before current state.** For each ambiguous dimension, generate the typical pattern for the customer's industry + size, then map known data against it. The delta is the discovery plan.
- **Evidence with confidence.** Every claim carries a source and a confidence tag (`[销售确认]` / `[AI推断]` / `[网络搜索]`).
- **Public + caller-provided only.** All facts come from public web research or inputs the calling skill passes in. This skill does not call internal AWS systems (no internal CRM, no internal commercial data) and does not interact with end users directly. If a downstream skill needs internal data, it must call the appropriate internal-tools skill itself.

## Recency Mandate (BINDING)

### Rule 1 — General sources: 90-day window

Every public source (news, conference talks, press releases, blog posts, LinkedIn, analyst commentary, vendor announcements, government/regulator filings) must have been published within the last 90 days from `report_run_date`.

- Source older than 90 days → drop or tag `[未公开披露 · not publicly disclosed]`.
- Citation label `[Publication · YYYY-MM-DD]` is the verification anchor.
- Customer-website pages without a clear date are exempt **only if** they describe stable structural facts (HQ city, founding year, brand portfolio composition). For anything that could change (executive names, headcount, financial figures, partnerships), require a dated source within 90 days or tag.

### Rule 2 — Financial reporting: most recent filing only

Revenue, profit, segment splits, headcount, R&D spend, balance-sheet items, share count, ownership, executive comp, dividend policy, and any other figure from official financial reporting:

- Use only the most recent official filing — latest annual (10-K / A 股年报 / H 股年报) or interim (10-Q / 半年报 / 季报), whichever is more recent.
- Do not blend figures across filings unless explicitly comparing year-over-year and citing both.
- If most recent filing is older than 6 months, record `most_recent_filing_date` so downstream consumers can calibrate.
- Investor-relations summaries, analyst-paraphrased numbers, aggregator pages (MarketScreener, Tipranks, Yahoo Finance) are NOT substitutes. Cite the original filing URL on the regulator or company website.
- Canonical disclosure venues:
  - **A 股**: SSE / SZSE (`sse.com.cn` / `szse.cn`)
  - **H 股**: HKEXnews (`hkexnews.hk`)
  - **US listing**: SEC EDGAR (`sec.gov/edgar`)
  - **EU listing**: home regulator's filing system

### Exceptions

- **Stable structural facts** — HQ city, founding year, brand portfolio composition (when no reorganization in last 90 days) — exempt with `[结构事实]` tag, treated as a sub-form of `[网络搜索]`.
- **`[AI推断]` inference chains** — not subject to 90-day rule (inference, not citation). Inference X must itself carry a source.
- **`[销售确认]` caller-provided data** — exempt from the 90-day rule. The calling skill is responsible for the timeliness of data it passes in.

## Source Attribution

Every value in the output carries a `confidence` field with one of three primary tags, plus a `source` string with provenance.

### Three confidence tags (primary)

| Tag | Meaning | Downstream guidance |
|---|---|---|
| `[销售确认]` | Sales / AE confirmed via the calling skill's `known_contacts` or `known_notes` | Use directly. Trust this tier. |
| `[AI推断]` | AI inference / analysis (industry-standard reasoning, role-archetype hypothesis, signal triangulation) | Suggest verification before customer-facing use. |
| `[网络搜索]` | Public web research (news, IR, LinkedIn, conference talks, blog posts, vendor case studies) | Trust subject to recency window. |

### Two special tags (used alongside, not instead of, the primary three)

| Tag | Meaning | When |
|---|---|---|
| `[未公开披露]` | Information not publicly available | Field is null but documented as a known gap. |
| `[结构事实]` | Stable structural fact exempt from 90-day rule | HQ city, founding year, brand composition. Sub-form of `[网络搜索]`. |

### Field format

Every output value carries:

```
{
  "value": "...",
  "confidence": "[销售确认]" | "[AI推断]" | "[网络搜索]" | "[未公开披露]",
  "source": "..."   // see source format per confidence tag below
}
```

**Source string format by tag:**

- `[销售确认]` → `"Caller-provided · {date_caller_supplied_it}"` (e.g., the date the caller's user shared this data).
- `[AI推断]` → `"because [X] → therefore [Y]"`. X must itself carry a source. Example: `"because the company is a NEV manufacturer with public IPO → therefore standard Auto C-suite hierarchy"`.
- `[网络搜索]` → one of:
  - `"[Publication · YYYY-MM-DD] [URL]"` for general web sources (must be ≤90 days)
  - `"[Filing type · venue · YYYY-MM-DD] [URL]"` for financial filings (must be most recent filing)
  - `"[结构事实] · [URL]"` for stable structural facts (exempt from 90-day window)
- `[未公开披露]` → `"[未公开披露 · not publicly disclosed]"` with optional `attempted_sources: []` showing what searches were tried.

### Hard rules

- No bare numbers, no bare claims, no unattributed names.
- When `[销售确认]` and `[网络搜索]` data conflict on the same entity:
  - If `[网络搜索]` source's `Last Verified` date is newer than the caller's supply date → public version wins.
  - Otherwise → `[销售确认]` wins.
  - Both versions surface in `dropped_claims` with reason `"caller-public conflict, [winner] kept"`.

---

═══════════════════════════════════════════════════════════
PROCEDURE 1 — ANALYSIS
═══════════════════════════════════════════════════════════

## How to Use This Skill

### Step 1: Inputs

Inputs are passed as a structured dict (JSON object) by the calling skill's invocation framework. This skill does not parse free-text user messages directly. If any required field is missing, return error `inputs_missing` with the missing field list.

**Required:**
- `customer_name` (string)
- `industry` (string)

**Optional:**
- `sector` (string) — narrower industry segment; inferred from industry if absent
- `known_contacts` (list) — stakeholder contacts the caller has already gathered (name, title, role, sentiment, source). Tagged `[销售确认]` per Source Attribution.
- `known_notes` (string or list) — free-text customer notes the caller has accumulated. Tagged `[销售确认]`.
- `language` (string, default `en`) — output language for narrative fields. Allowed: `en` / `zh-CN` / `zh-TW`. Affects free-text fields (e.g., `power_dynamics.architecture_influencer` description, `dropped_claims.reason`); does NOT affect enum values, tag literals (`[销售确认]` etc. stay in source form), filenames, or proper nouns (customer name, AWS service names).
- `run_id` (string) — caller may supply; if absent, this skill generates one (UUID-style format; uniqueness within session scope is sufficient — opaque identifier, not required to be cryptographically random).

---

### Step 2: Account Foundation

Use web search for the following research.

**Company Fundamentals:**
- Annual reports, investor presentations, 10-K/10-Q filings, financial reports from company website
- Company website (About, Products, Careers, Press pages)
- Recent earnings call transcripts or summaries

**Market Position:**
- Industry reports and market share data
- Analyst coverage and ratings
- Competitive landscape (cross-reference with market-intelligence peer/competitor section)

**Technology & Digital:**
- CTO/CIO interviews, conference talks, blog posts
- Job postings (reveal tech stack and priorities)
- Technology partnerships and vendor relationships
- Patent filings and R&D investments

**Organization & People:**
- Leadership team bios and recent changes
- Organizational structure (from annual reports, LinkedIn, press)
- Employee count, growth rate, key hiring areas
- Glassdoor/culture signals

**Competitive Landscape at the Account:** Capture structural/commercial competitive position at the account from public sources only. (Internal commercial data — actual contract values, AWS-side discount programs, internal POC trackers — is out of scope for this skill; downstream skills with access to internal systems will layer those in.)

- **Existing cloud agreements** — Azure EA, GCP committed-use agreement, Alibaba Cloud frame contract, Oracle Cloud ULA, etc. — contract type, scope, approximate value if public, renewal/expiry if known
- **Preferred-vendor or strategic-supplier status** — public preferred-vendor lists, joint press releases, co-branded case studies
- **Active competitor POCs / pilots** — publicly disclosed Azure, GCP, Snowflake, Databricks, OpenAI, Alibaba POCs running now
- **Competitor account-level investment** — named executive sponsorships, co-innovation labs, co-marketing commitments
- **Procurement / vendor-consolidation posture** — public statements, board-level commitments

| Dimension | Current State | Evidence | Source | Implication for AWS |
|-----------|---------------|----------|--------|--------------------|
| Existing cloud agreements | | | | |
| Preferred-vendor status | | | | |
| Active competitor POCs | | | | |
| Competitor exec sponsorship | | | | |
| Consolidation posture | | | | |

**Other Cloud & GenAI Footprint:** Research the customer's existing non-AWS cloud and GenAI usage.

- `"[Company] Azure" OR "[Company] Google Cloud" OR "[Company] Alibaba Cloud" OR "[Company] Oracle Cloud"` — incumbent hyperscalers
- `"[Company] OpenAI" OR "[Company] Anthropic" OR "[Company] Gemini" OR "[Company] Databricks" OR "[Company] Snowflake Cortex"` — GenAI platforms and LLM vendors
- `"[Company] GenAI" OR "[Company] LLM" OR "[Company] generative AI" OR "[Company] AI platform"` — internal AI initiatives and announced partnerships
- Conference talks, case studies, vendor announcements naming the customer
- Record: vendor, workload/use case, confidence (`[销售确认]` / `[AI推断]` / `[网络搜索]`), source URL

**Customer Buying Behavior:** Research how this customer buys technology.

- `"[Company] RFP" OR "[Company] procurement" OR "[Company] vendor selection"` — procurement patterns
- `"[Company] technology contract" OR "[Company] multi-year agreement"` — contract structure preferences
- `"[Company] preferred vendor" OR "[Company] strategic supplier"` — vendor consolidation tendencies
- Public evidence of decision cycles, POC requirements, consensus vs. top-down buying, risk tolerance, signing authority
- Record: buying pattern, evidence, source URL, implication for AWS engagement

Store all findings with source URLs. Every claim must trace back to a source.

---

### Step 3: Organization Chart Mapping

#### Approach: Industry Standard → Current State (Public + Caller-Provided) → Gap Identification

**Step 3.1: Generate Industry Standard Org Chart**

Based on customer's industry, size, and business model, generate the typical org chart:
- C-suite roles and reporting lines
- Key VP/Director-level functions
- Technology organization structure (CTO vs. CIO, platform teams, data teams, security)
- Business unit structure

| Level | Role | Reports To | Key Responsibilities | Typical Headcount Range |
|-------|------|-----------|---------------------|------------------------|

**Step 3.2: Map Current Known Org Chart**

Use **public web research and caller-provided inputs only**.

1. **Public research:** annual reports, press releases, company website leadership pages, LinkedIn, conference speaker pages, earnings call participant lists.
   - `"[Company Name] leadership team"`
   - `"[Company Name] CTO" OR "[Company Name] CIO" OR "[Company Name] VP Engineering"`
   - `"[Company Name] organizational structure"`
   - `"[Company Name] executive team"`
2. **Market-intelligence cross-reference:** check the market-intelligence output for any leadership changes (new CEO/CTO/CIO, executive departures) in the last 6 months and incorporate.
3. **Caller-provided:** if the caller passed in `known_contacts`, include those entries.

| Level | Name | Title | Reports To | Source | Last Verified |
|-------|------|-------|-----------|--------|---------------|

Mark the source per entry: `[网络搜索] (URL)`, `[网络搜索] Market-Intelligence`, or `[销售确认]`.

**Step 3.3: Identify Gaps**

| Expected Role | Current Status | Gap Type | Impact on AWS Sales | Recommended Action |
|---------------|---------------|----------|--------------------|--------------------|

Gap Types:
- **Unknown** — role likely exists but we don't know who fills it
- **Missing** — role may not exist in this organization
- **New** — recently created role (signals strategic priority)
- **Vacant** — role is open (hiring signal)

---

### Step 4: Relationship Map

#### Approach: Standard Categories → Map Known (Public + Caller-Provided) → Analyze

**Step 4.1: Stakeholder Categories**

For the customer's industry and size, identify standard stakeholder categories relevant to AWS:

| Category | Typical Roles | Why They Matter for AWS |
|----------|--------------|------------------------|
| Technical Decision Makers | CTO, CIO, VP Engineering, Chief Architect | Architecture decisions, vendor selection |
| Business Line Owners | GM, VP Product, VP Operations | Workload owners, business case sponsors |
| Influencers | Enterprise Architects, Lead Engineers, Data Scientists | Technical evaluation, POC execution |
| Champions | Cloud Architects, DevOps Leads, Innovation Managers | Internal advocates, day-to-day partners |
| Blockers (potential) | Security Officers, Compliance Heads, incumbent vendor advocates | Can slow or stop deals |

**Step 4.2: Map Known Relationships**

Use **public web research, market-intelligence output, and caller-provided inputs only** (`known_contacts`, `known_notes`).

| Name | Title | Category | Relationship Strength (1-5) | Last Engagement | Engagement Channel | Sentiment | Notes |
|------|-------|----------|---------------------------|-----------------|-------------------|-----------|-------|

Relationship Strength:
- 5 = Strong advocate, regular engagement, trusts AWS
- 4 = Positive, engaged, open to AWS
- 3 = Neutral, limited engagement
- 2 = Skeptical or disengaged
- 1 = Hostile or actively blocking

**Step 4.3: Relationship Gap Analysis**

| Critical Role | Current Coverage | Gap | Risk Level | Recommended Action |
|---------------|-----------------|-----|------------|-------------------|

**Step 4.4: Power Dynamics Summary**

Structured fields:
- `architecture_influencer` — who influences technical architecture choices
- `potential_champion` — who could champion an AWS deal internally
- `potential_blocker` — who could block, with reason
- `decision_culture` — `consensus` | `top_down` | `committee`

---

### Step 5: Customer IT Landscape

#### Approach: Hypothesis Generation → Validation

This is the hardest data to obtain. Generate an educated hypothesis from public signals.

**Step 5.1: Public Signal Collection**

- **Job postings:** `"[Company] careers" AND ("AWS" OR "Azure" OR "GCP" OR "Kubernetes" OR "Terraform" OR "Java" OR "Python" OR ".NET")`
- **Engineering blogs:** `"[Company] engineering blog" OR "[Company] tech blog"`
- **Conference talks:** `"[Company]" AND ("re:Invent" OR "KubeCon" OR "QCon" OR "tech conference")`
- **GitHub/Open source:** `"[Company]" site:github.com`
- **Technology partnerships:** `"[Company] partner" AND ("technology" OR "cloud" OR "platform")`
- **Vendor case studies:** `"[Company]" case study` on Snowflake, Databricks, MongoDB, Confluent, etc.
- **BuiltWith/Wappalyzer signals** when web presence available

**Step 5.2: IT Landscape Hypothesis**

| Layer | Hypothesized Technology | Confidence | Evidence | Source |
|-------|------------------------|------------|----------|--------|
| Cloud Platform(s) | | | | |
| Compute | | | | |
| Database | | | | |
| Data & Analytics | | | | |
| AI/ML & GenAI | | | | |
| DevOps/CI-CD | | | | |
| Security | | | | |
| Networking | | | | |
| Application Stack | | | | |
| Collaboration | | | | |
| CRM/ERP | | | | |
| Monitoring | | | | |

Confidence tags (per Source Attribution):
- `[销售确认]` — caller passed it in via `known_contacts` / `known_notes`. Use directly.
- `[网络搜索]` — multiple independent public sources confirm, OR single strong signal (job posting, blog, vendor case study) within 90-day window.
- `[AI推断]` — inferred from industry norm or role-archetype hypothesis only; no direct source. Suggest verification.

---

═══════════════════════════════════════════════════════════
PROCEDURE 2 — OUTPUT
═══════════════════════════════════════════════════════════

## Output Format

Return a single JSON object with the following top-level keys. Every value carries a `source` field per Source Attribution rules.

```
{
  "meta": {
    "skill_name": "account-context",
    "run_id": "uuid-v4-string",
    "customer_name": "...",
    "industry": "...",
    "sector": "...",
    "report_run_date": "YYYY-MM-DD",
    "most_recent_filing_date": "YYYY-MM-DD" | null,
    "schema_version": "1.0"
  },
  "company_snapshot": [...],
  "industry_vs_current": [...],
  "org_chart": {
    "industry_standard": [...],
    "current_known": [...],
    "gaps": [...]
  },
  "relationship_map": {
    "stakeholders": [...],
    "gaps": [...],
    "power_dynamics": {
      "architecture_influencer": "...",
      "potential_champion": "...",
      "potential_blocker": "...",
      "decision_culture": "consensus" | "top_down" | "committee"
    }
  },
  "it_landscape": {
    "cloud_platform": { "tech": "...", "confidence": "[销售确认]"|"[AI推断]"|"[网络搜索]", "evidence": "...", "source": "..." },
    "compute": {...},
    "database": {...},
    "data_analytics": {...},
    "ai_ml_genai": {...},
    "devops_cicd": {...},
    "security": {...},
    "networking": {...},
    "application_stack": {...},
    "collaboration": {...},
    "crm_erp": {...},
    "monitoring": {...}
  },
  "competitive_landscape": {
    "existing_agreements": [...],
    "preferred_vendor_status": [...],
    "active_competitor_pocs": [...],
    "competitor_exec_sponsorship": [...],
    "consolidation_posture": [...]
  },
  "other_cloud_genai_footprint": [
    { "vendor": "...", "workload": "...", "confidence": "[销售确认]"|"[AI推断]"|"[网络搜索]", "source": "..." }
  ],
  "buying_behavior": [
    { "pattern": "...", "evidence": "...", "source": "...", "implication_for_aws": "..." }
  ],
  "coverage_per_section": {
    "company_snapshot": "Strong" | "Moderate" | "Thin" | "None",
    ...
  },
  "dropped_claims": [
    { "claim": "...", "reason": "stale > 90 days" | "source unsupported" | "..." }
  ]
}
```

## Output Persistence

Default behavior: write the JSON to disk so downstream skills can consume it across sessions.

**Path:**
```
~/.kiro/cache/account-context/data/{customer_slug}/account-context_{customer_slug}_{YYYY-MM-DDTHH-MM-SSZ}.json
~/.kiro/cache/account-context/data/{customer_slug}/account-context_{customer_slug}_latest.json   # mirror of newest
```

- **Slug:** lowercase Latin chars, spaces → hyphens, Chinese characters preserved, strip path-unsafe characters (`/ \ : * ? " < > |`), truncate to 60 chars.
- **Timestamp:** ISO 8601 in UTC with `:` replaced by `-` for filesystem safety (e.g., `2026-05-18T10-32-15Z`). Second-level resolution; multiple runs in the same day produce distinct files.
- **Latest mirror:** `account-context_{customer_slug}_latest.json` is overwritten with each run; downstream skills should read this path when they need "the most recent context for this customer".
- **Self-describing payload:** the JSON `meta` block carries `skill_name`, `customer_name`, `report_run_date`, `run_id` (UUID v4), `schema_version` so downstream consumers do not parse filenames for routing.
- **Retention:** caller may keep all historical runs; this skill does not delete. Future Kiro maintenance may add automatic prune (e.g., keep most recent 10 + latest mirror per customer).
- **Return value:** the absolute path of the written timestamped JSON, the absolute path of `latest.json`, and the JSON object itself.

**Failure modes:**
- Primary path permission denied / read-only filesystem → fall back to the current working directory; surface the actually-written paths in the return value.
- Write fails entirely (disk full, fs error) → return error `output_persist_failed`; the JSON object is still returned for in-context consumption by the caller.

**Forward compatibility:** This path convention will be unified with other Kiro skills in a future revision (likely a flat shared root or env-var-driven). Downstream skills should read the path from this skill's return value, not hardcode `~/.kiro/cache/account-context/`.

## Downstream Consumers

The following skills consume this skill's output:

- `business-insight` — SWOT/TOWS interpretation
- `solutions-search` — reference architecture matching
- `competitive-intelligence` — Mode B compete brief per incumbent
- `bttroc` — CXO conversation synthesis
- `business-insight` — block-level BMC analysis
- `market-intelligence` — peer/competitor cross-reference
- `opportunity-progression` — MEDDPICC qualification (downstream of bttroc)

Note: this skill was renamed from `account-information` to `account-context` to reflect its machine-to-machine role. Downstream skills still reference the old name in their SKILL.md text; that will be updated in a future refactor.
