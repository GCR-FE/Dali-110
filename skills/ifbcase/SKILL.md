---
name: "ifbcase"
description: "Use this skill when the user wants to read customer information about ifbcase. Trigger words 'ifbcase'. 
---


# IFBCase — Industry Field Business Case Data

This folder is the central data source for customer and opportunity
information used by other skills (e.g., `business-insight`, `bttroc`,
`competitive-intelligence`, ...).

## How to Use

When a skill needs customer context, follow these two steps.

### Step 1: Confirm the Industry

Ask the user which industry the case belongs to. The supported industries are:

| Code | Industry |
|------|----------|
| `mfg` | Manufacturing |
| `auto` | Automotive |
| `lshc` | Life Sciences & Healthcare |
| `fsi` | Financial Services & Insurance |
| `retail` | Retail & E-commerce |
| `me` | Media & Entertainment |
| `game` | Gaming |
| `hksmb` | Hong Kong SMB |
| `hkent` | Hong Kong Enterprise |

### Step 2: Read the Relevant Files

Once the industry is confirmed, navigate to the corresponding folder under
`assets/` and read the files:

```
IFBcase/assets/<industry_code>/
├── customer-info-<industry_code>.md   # Customer overview, financials,
│                                      # business challenges, IT vendor
│                                      # landscape, strategy. References the
│                                      # diagrams below inline.
├── oppty-info-<industry_code>.md      # Opportunity details and context.
├── tech-architecture.jpg              # IT architecture / technology stack
│                                      # diagram.
├── org-chart.jpg                      # Organizational structure & key
│                                      # decision-makers.
└── industry-trend-N.jpg               # Optional. Only present when the
                                        # source case includes dedicated
                                        # industry-trend pages (LSHC has
                                        # `industry-trend-1.jpg` and
                                        # `industry-trend-2.jpg`).
```

**Example for Automotive:**

```
IFBcase/assets/auto/
├── customer-info-auto.md
├── oppty-info-auto.md
├── tech-architecture.jpg
└── org-chart.jpg
```

## File Descriptions

| File | Contents |
|------|----------|
| `customer-info-<code>.md` | Customer background, financial snapshot, business challenges, strategic direction, current IT vendor matrix. References `tech-architecture.jpg` and `org-chart.jpg` inline so a vision-capable LLM can pull the picture only when needed. |
| `oppty-info-<code>.md` | Opportunity matrix and per-OP details — deal context, stakeholders, technical requirements, and current status. |
| `tech-architecture.jpg` | Visual diagram of the customer's IT architecture / technology stack (rendered from the source PPT). |
| `org-chart.jpg` | Visual diagram of the customer's organizational structure and key decision-makers. |
| `industry-trend-N.jpg` | Industry-trend pages from the source PPT, kept as images because they are dense visual layouts. Only present for cases that have such pages (e.g. LSHC). |

## Notes

- Always confirm the industry with the user before reading files.
- If the user does not specify an industry, present the table above and ask them to choose.
- The `.md` files are the primary data source. The `.jpg` files provide supplementary visual context — read them when you need to ground in the picture.
- To regenerate any file in this folder from the source `.pptx`, see the workspace skill at `.kiro/skills/pptx-to-ifbcase/`. It is also responsible for keeping naming consistent with this README.
