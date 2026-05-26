# Solutions Search — Reference Data Index

> **Read this first.** This file routes the solutions-search agent to the correct reference material.
> Source: copied from `knowledge/wiki/Industries/`.
> Last synced: 2026-05-18

---

## What's Here

```
references/
├── INDEX.md          ← YOU ARE HERE
└── industries/       ← per-industry solution maps, asset cards, customer references
    ├── 金融.md               — FSI (12 Asset Cards, 联络中心生态, 印闪科技案例)
    ├── 汽车.md               — Auto (6 Asset Cards, 50K Solution Map, 14 业务场景)
    ├── 游戏.md               — Game (8 Asset Cards, Build/Run/Grow 三态, Kuro/Zenjoy/miHoYo)
    ├── 媒体娱乐与广告.md      — M&E (Solution Map, Newsbreak/Sumzap/点点互动)
    ├── 零售和快消.md          — Retail/CPG (Solution Map + 客户案例)
    ├── 生命科学与大健康.md    — HCLS (LS Solution Map)
    ├── 制造.md               — Manufacturing (Manuf Solution Map)
    └── 教育.md               — Education (⚠️ 内容稀薄, Highspot SPA 居多)
```

---

## Routing: "Customer is in X industry — where do I look?"

| Customer Industry | File | Content Highlights |
|---|---|---|
| 金融 / FSI / Banking / Insurance / Securities | `industries/金融.md` | 12 类 Asset (量化/投顾/KYC/GenBI/反欺诈等), 联络中心生态, 案例 |
| 汽车 / Automotive | `industries/汽车.md` | 6 Asset Cards + KPI, Solution Map (14 业务场景) |
| 游戏 / Gaming | `industries/游戏.md` | 8 Asset Cards + KPI (GCSC/GMM/GVOP/TCM/DMG等), 案例 |
| 媒体娱乐与广告 / Media & Entertainment | `industries/媒体娱乐与广告.md` | M&E Solution Map, 案例 |
| 零售和快消 / Retail & CPG | `industries/零售和快消.md` | Solution Map + 客户案例 |
| 生命科学与大健康 / Healthcare & Life Sciences | `industries/生命科学与大健康.md` | LS Solution Map |
| 制造 / Manufacturing | `industries/制造.md` | Manuf Solution Map |
| 教育 / Education | `industries/教育.md` | ⚠️ 稀薄 — Highspot SPA 居多, 建议补强 |

---

## Reading Order

1. **Read this INDEX.md** — identify which industry matches the customer
2. **Read the relevant `industries/<industry>.md`** — extract:
   - Solution Map (业务场景 → AWS 服务映射)
   - Asset Cards (per-solution KPI + 适用客户画像)
   - Customer references (公开案例 + 案例亮点)
   - AWS services involved
3. **Match to the Strategic Initiative** — find which Asset Card / Solution Map entry aligns with the requested AWS capability
4. **Synthesize** into the output format defined in `SKILL.md`

---

## Cross-Industry Pattern Matching

When direct-industry match is thin, use these adjacency patterns:

| Pattern | Industries that share it |
|---|---|
| Real-time inference / anti-fraud | 金融 ↔ 游戏 (anti-cheat) ↔ 零售 (fraud) |
| IoT + predictive maintenance | 制造 ↔ 汽车 ↔ 生命科学 (设备监控) |
| Content delivery / streaming | 游戏 ↔ 媒体娱乐与广告 |
| Document processing / IDP | 金融 ↔ 生命科学 ↔ 教育 |
| Personalization / recommendation | 零售 ↔ 媒体娱乐与广告 ↔ 游戏 |
| Connected vehicle / edge | 汽车 ↔ 制造 (工业边缘) |
| GenAI / LLM applications | 全行业通用 — check each industry page for GenAI-specific assets |

---

## Coverage Gaps (be honest about these)

- **教育 (Education)** — content is thin (mostly Highspot SPA pages with no extractable body text)
- **Solutions catalog (per-architecture detail)** — the `knowledge/wiki/Solutions/` layer has NOT been ingested yet. These industry pages contain Solution Maps and Asset Cards but not full per-solution architecture docs
- **Telco / Telecom** — no curated industry page exists in the current set
- **Energy / Utilities** — no curated industry page exists
- **Public Sector / Government** — no curated industry page exists

If the customer is in an uncovered industry, **state the gap explicitly**. Do not fabricate references.

---

## Sync & Maintenance

These files are copies from `knowledge/wiki/Industries/`.
When the knowledge base is updated, re-copy the affected files here.

To sync all:
```bash
cp knowledge/wiki/Industries/*.md Dali/skills/solutions-search/references/industries/
```

---

*INDEX.md — last synced 2026-05-18*
