# RAG Search Quality Guardrails (RAG 检索质量护栏)

The `./references/` data corpus is accessed through a RAG (retrieval-augmented generation) system. RAG retrieves by semantic similarity, not by truth or relevance — so every retrieval must pass the following guardrails before being included in the compete brief. Silent retrieval failures — stale content presented as current, paraphrased claims that overstate the source, single-source positioning — are the #1 cause of sellers getting burned in customer meetings.

## Guardrail 1 — Query Decomposition Per Dimension (分维度查询分解)

For each of the seven dimensions, execute a **minimum of 3 independent queries**:

1. **Competitor-direct query** — `[specific competitor product/service] [AWS competing service] battlecard` / `playbook` / `benchmark` (named SKUs, not general labels)
2. **Workload-specific query** — `[workload] [competitor] vs [AWS]` / `[workload] displacement playbook [competitor]`
3. **Industry-contextualized query** — `[customer industry] [region] [competitor] compete` / `[industry regulation e.g. APRA / HIPAA] [competitor] [AWS]`

Never send a single broad query. "Azure compete" is too broad and will return everything from outdated Office 365 positioning to M365 Copilot enterprise agreements. Name the specific competitor product (Azure OpenAI, Azure Fabric, Azure Arc) and the specific workload.

## Guardrail 2 — Metadata Pre-Filter (元数据过滤)

Before ranking any retrieval, filter the knowledge base corpus on hard metadata:

- **Freshness:** `last_reviewed_date >= today - 12 months` by default; Stale (>12mo) only included when no current content exists and explicitly flagged
- **Competitor metadata:** `competitor_tag IN [specific competitor product]` — not the generic parent company tag
- **Content type:** `content_type IN [battlecard, displacement_playbook, benchmark, win_loss_analysis, objection_handler, pricing_combat, architecture_comparison]` — reject generic marketing decks
- **Region:** `region IN [customer_region, global]` when data sovereignty, regulation, or local content is in scope
- **Reviewing team:** prefer content with `reviewing_team IN [Product Marketing, PMT, Field CI]` over unreviewed field uploads

If the metadata filter returns zero results for a dimension, state so explicitly in the Coverage Honesty section rather than loosening the filter silently.

## Guardrail 3 — Cross-Dimensional Triangulation (跨维度交叉验证)

Every claim in the **Positioning Frame** (Section 2) and every objection rebuttal (Section 4) must appear in **≥2 of the 7 dimensions**. Single-dimension claims are labeled **Single-source — unverified** and flagged for user review before inclusion in customer-facing material.

Example: If the battlecard claims "Bedrock Guardrails outperforms Azure Content Safety on APRA-aligned workloads," that same claim must also appear in the Proof Points dimension (published benchmark) or the Architecture dimension (documented capability difference). If only the battlecard says it, it's a single-source claim — label it.

## Guardrail 4 — Freshness Tier Labeling (新鲜度分级)

Every retrieved knowledge base artifact carries a freshness tier based on `last_reviewed_date`:

| Tier | Age | Confidence multiplier | Treatment |
|------|-----|-----------------------|-----------|
| Current | <6 months | 1.0 | Use as-is |
| Recent | 6–12 months | 0.8 | Use, label as Recent |
| Stale | 12–18 months | 0.5 | Use only if no Current/Recent exists, flag as Stale, recommend CI team refresh |
| Expired | >18 months | 0 | Exclude; note in Coverage Gap |

Apply the multiplier to the final ranking. A slightly-less-specific Current battlecard beats a perfectly-specific Expired one — competitors move too fast for 2-year-old positioning to be safe.

## Guardrail 5 — Citation Validation (引用验证)

After generating the compete brief, **re-fetch every knowledge base URL** in the Proof Point Table (Section 11) and confirm:

- The claimed customer name / anonymized descriptor actually appears in the source
- The claimed outcome metric (e.g., "40% cost reduction", "3x faster inference") actually appears in the source with the same methodology
- The claimed quote from a rebuttal actually appears in the source verbatim
- The last-reviewed date displayed matches the source metadata

If the source does not support the claim:

- **Drop the claim** — do not rephrase and keep
- **Note the drop** in Coverage Honesty
- Do not invent a replacement proof point

## Guardrail 6 — Pricing Math Re-Calculation (价格二次核算)

The Pricing Combat Pack (Section 5) is the #1 area where RAG content causes seller credibility damage, because procurement teams verify pricing math down to the cent. For every pricing claim:

- **Re-calculate the side-by-side comparison** from raw unit prices, do not quote an aggregate in the source
- **Show the math inline** in the output — instance types, region, hours, discount tier, term
- **Validate discount-tier assumptions** against the most recent pricing page referenced in the source
- **Flag any claim where the source does not show the underlying math** — "source asserts 30% lower TCO but does not show calculation" is honest; fabricating the math is not

If the source pricing page is stale (>6 months for competitor pricing — faster decay than other content types), flag and recommend refresh.

## Guardrail 7 — Benchmark Number Methodology Verification (跑分方法学验证)

Every benchmark number surfaced in the Architecture & Benchmark Guidance (Section 6) must trace to a source that includes:

- The instance types / service SKUs on each side
- The workload or dataset used
- The metric measured (latency, throughput, cost-per-token, accuracy)
- The test environment (region, time period, configuration)

If any of these is missing from the source, **do not cite the number**. Instead, give the SA benchmark guidance — "recommend running X benchmark with Y configuration, expected differential based on architecture" — without a specific number.

## Guardrail 8 — Coverage Honesty Disclosure (覆盖诚实度披露)

Section 12 (Coverage Honesty) is expanded to a **mandatory structural disclosure**, not a best-effort note. It must state:

- Which of the 7 dimensions returned Strong / Moderate / Thin / None
- Which queries returned zero results
- Which freshness tiers were available per dimension
- Which claims were dropped during citation validation and why
- Which benchmark numbers were excluded for missing methodology
- Any metadata filter that was relaxed, and why

Silent gaps break the seller in the meeting. A seller who knows "we have no current Alibaba Cloud pricing content for your Indonesia customer" can plan around it; a seller who receives silently-substituted China content labeled "Alibaba pricing" will embarrass themselves and AWS.

## Required Confidence Labels Per Dimension

Every dimension in the final output must carry a confidence label:

- **Strong** — ≥2 queries returned Current or Recent content, citation validated, triangulated across ≥2 dimensions
- **Moderate** — ≥2 queries returned Recent or Stale content, citation validated, appears in 1 other dimension
- **Thin** — single-query retrieval, OR only Stale content, OR citation partially validated
- **None** — zero results after metadata filtering; no content cited in this dimension, disclosed in Coverage Honesty
