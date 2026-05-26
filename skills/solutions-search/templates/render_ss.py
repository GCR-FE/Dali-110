#!/usr/bin/env python3
"""
Solutions Search HTML Renderer — fills the Jinja2 template with structured data and outputs rendered HTML.

Usage:
    python render_ss.py input.json output.html

Input: JSON file with the Solutions Search data structure (see DATA_SCHEMA below).
Output: Rendered HTML file (MD3 styled, self-contained).

DATA SCHEMA (what the agent produces):
{
    "customer_name": "海尔智家 Haier Smart Home",
    "industry": "消费电子",
    "date": "2026-05-12",
    "upstream_source": "business-insight（3 个战略倡议）",
    "coverage_summary": {
        "initiatives_count": 3,        // Number of Strategic Initiatives searched
        "references_count": 9             // Total references across all initiatives
    },
    "initiatives": [
        {
            "number": 1,                                     // Initiative sequence (1-3)
            "title": "北美供应链 IT 重塑入口",               // Initiative title from business-insight
            "subtitle": "Tariff-aware forecasting + ...",    // AWS capability / approach
            "potential_opportunity": "$8–15M Y1 ...",        // Deal shape estimate
            "queries_executed": [                            // All search queries for this initiative
                "consumer electronics supply chain AWS ...",
                "manufacturing supply chain pattern ...",
                "Oracle ERP migration AWS ...",
                "supply chain CxO executive briefing ..."
            ],
            "references": [
                {
                    "title": "AWS Supply Chain Dev Guide",   // Reference document title
                    "url": "https://...",                    // Source URL
                    "match_type": "direct",                  // One of: direct, pattern, displacement, inspirational
                    "match_type_label": "Direct Match",    // Display label for pill badge
                    "match_strength": "Strong",              // Strong / Moderate / Thin
                    "freshness_tier": "Current",             // Current / Recent / Stale
                    "citation_validated": "Yes",             // Yes / Partial / No
                    "icon": "rocket_launch",                 // Material Symbols icon name
                    "description": "...",                    // 1-2 sentence summary
                    "tags": ["tag1", "tag2"]                 // Source + match metadata tags
                }
            ],
            "next_step": "申请 Workshop ...",                // Single actionable next step for AM/SA
            "coverage_gap": "none"                           // Per-initiative coverage gap disclosure
        }
    ]
}

MATCH_TYPE VALUES:
- "direct"        → pill-direct (purple)  — same industry + same capability
- "pattern"       → pill-pattern (green)  — adjacent industry, same architectural pattern
- "displacement"  → pill-displacement (amber) — displacement / migration playbook
- "inspirational" → pill-inspirational (grey) — novel approach from unrelated domain

ICON VALUES (Material Symbols Outlined):
- "rocket_launch" — Direct Match
- "architecture"  — Pattern Match
- "swap_horiz"    — Displacement
- "check_circle"  — Inspirational
"""

import json
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


def render_ss(data: dict, template_dir: str = None) -> str:
    """Render Solutions Search data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    template = env.get_template("solutions-search.html.j2")
    return template.render(**data)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = render_ss(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
