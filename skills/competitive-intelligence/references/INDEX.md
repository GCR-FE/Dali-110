# Competitive Intelligence — Reference Data Index

> **Read this first.** This file routes the CI agent to the correct reference material.
> Source: copied from `knowledge/wiki/Compete/` + `knowledge/wiki/Battlecards/`.
> Last synced: 2026-05-18

---

## What's Here

```
references/
├── INDEX.md          ← YOU ARE HERE
├── compete/          ← per-vendor positioning pages
│   ├── AliCloud.md   — 阿里云全面竞争分析 (中国+海外)
│   ├── Azure.md      — Azure/21VCA-E 竞争分析 (含商务模型+1-pager)
│   └── Huawei.md     — 华为云竞争分析
└── battlecards/      ← scenario-based talk tracks
    ├── AWS-vs-Local-CSP-China.md   — 中国 CSP 本土对比 (韧性/隐私/网络/创新)
    ├── China-CSP-Overseas.md       — 中国 CSP 海外覆盖 (GCR外/ESG/关停史)
    ├── E2E-Data-Architecture.md    — 端到端数据架构对比 (Lake Formation vs MaxCompute)
    ├── FSI-Fraud-AI.md             — FSI 反欺诈 AI 对比 (MS/Google/中国CSP)
    └── GPU-Competitive.md          — GPU/AI 算力对比 (H200/H100/B200+定价)
```

---

## Routing: "I need X — where do I look?"

| Need | Read |
|------|------|
| AliCloud positioning, pricing model, weaknesses | `compete/AliCloud.md` |
| Azure / 21Vianet positioning, EA dynamics | `compete/Azure.md` |
| Huawei Cloud positioning, org model weaknesses | `compete/Huawei.md` |
| China local CSP vs AWS (sovereignty, resilience) | `battlecards/AWS-vs-Local-CSP-China.md` |
| Chinese CSP going overseas — why AWS wins | `battlecards/China-CSP-Overseas.md` |
| Data platform compete (Redshift/Glue vs MaxCompute) | `battlecards/E2E-Data-Architecture.md` |
| FSI fraud/financial-crime AI compete | `battlecards/FSI-Fraud-AI.md` |
| GPU/AI compute compete (NVIDIA instances, pricing) | `battlecards/GPU-Competitive.md` |

---

## Reading Order

1. **Read this INDEX.md** — identify which vendor(s) and scenario(s) match the user's request
2. **Read the relevant `compete/` page** — overall vendor positioning, strengths, weaknesses, pricing
3. **Read matching `battlecards/`** — scenario-specific depth, talk tracks, counter-tactics
4. **Synthesize** into the output format defined in `SKILL.md`

---

## Coverage Gaps (be honest about these)

The following competitors/scenarios are NOT covered in this reference set:

- **GCP / Google Cloud** — no curated page yet
- **Oracle / OCI** — no curated page yet
- **Snowflake** — no curated page yet
- **Databricks** — no curated page yet
- **VMware / Broadcom** — no curated page yet
- **OpenAI / Microsoft Copilot (standalone)** — partially covered in Azure.md
- **CoreWeave / Lambda Labs / Nebius / Crusoe** — no curated page yet

If the user requests compete analysis for a vendor not covered here, **state the gap explicitly** in Coverage Honesty. Do not fabricate data.

---

## Sync & Maintenance

These files are copies from `knowledge/wiki/Compete/` and `knowledge/wiki/Battlecards/`.
When the knowledge base is updated, re-copy the affected files here.

To sync all:
```bash
cp knowledge/wiki/Compete/*.md Dali/skills/competitive-intelligence/references/compete/
cp knowledge/wiki/Battlecards/*.md Dali/skills/competitive-intelligence/references/battlecards/
```

---

*INDEX.md — last synced 2026-05-18*
