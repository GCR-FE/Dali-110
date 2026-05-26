# Reserved Interfaces

Placeholders for future data source integrations (e.g., via MCP). Renumbered after CRM (legacy #1) was retired and Personas (legacy #5) was converted to a local reference file (`cxo-personas.md`).

| # | Interface | Data Points |
|---|-----------|-------------|
| 1 | Customer Reference | Customer Profile, Reference Details (business results/metrics), Reference Availability by region |
| 2 | Compete Intelligence | Competitor Profiles, Service-by-Service Comparison, Competitive Positioning, Battle Cards |
| 3 | Win/Loss Data | Win themes by competitor, Loss reasons, Win rate trends, Deal size patterns |
| 4 | Pricing & GTM Resources | Pricing Models (RI/SP/Spot/Free Tier/EDP/PPA), GTM Programs & Incentives, Sales Plays |
| 5 | AWS Services | Product Catalog (descriptions, features, regional availability), Service Usage Analysis |
| 6 | Solution Architecture | Reference Architectures, AWS Solutions Library, deployment guides, GitHub repos |
| 7 | Compliance & Regulatory | Regional data privacy (PDPO, PIPL), industry compliance (PCI-DSS, SOC2), AWS certifications by region |
| 8 | Customer Conversation Builder | Preceding skill output: opportunity context, customer pain points, stakeholder mapping, competitive signals — mapped to MEDDPICC Scorecard structure for Phase 1 input |

## Integration Notes

- Phase 1 Step 1: Uses Interface #8 for importing opportunity data from Customer Conversation Builder
- Phase 4 Step 1 (Market Search): delegated to `account-context` + `solutions-search` skills; those skills may internally consume Interface #1 (Customer Reference)
- Phase 4 Step 2 (Compete): delegated to `competitive-intelligence` skill; that skill may internally consume Interface #2 (Compete Intelligence) and Interface #3 (Win/Loss Data)
- Phase 7: Uses internal business proposal templates when available

Note: Phase 5 Step 3 (Stakeholder Profiling) does NOT consume Reserved Interfaces. It delegates to the `contact-profiling` skill and references the local `cxo-personas.md` file.
