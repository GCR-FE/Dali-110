#!/usr/bin/env python3
"""
Executive Briefing HTML Renderer — fills the Jinja2 template with structured data and outputs rendered HTML.

Usage:
    python render_eb.py input.json output.html

Input: JSON file with the EB data structure (see DATA_SCHEMA below).
Output: Rendered HTML file.

DATA SCHEMA (what the agent produces):
{
    "customer_name": "瑞安集团",
    "meeting_title": "Executive Briefing Center",
    "meeting_date": "2026-04-10",
    "meeting_time": "10:00-11:30",
    "meeting_format": "On-site (EBC)",
    "opportunity_name": "Enterprise Digital Transformation",
    "opp_stage": "Business Validation",
    "who_requested_and_why": "...",
    "aws_team": [
        {"name": "...", "role": "...", "purpose": "..."}
    ],
    "customer_attendees": [
        {
            "name": "陈总",
            "title": "CEO",
            "stance": "Neutral",
            "background_paragraph": "..."
        }
    ],
    "company_profile": "...",
    "objectives": [
        {
            "objective": "...",
            "context": "...",
            "talking_points": "...",
            "asks": ["..."]
        }
    ],
    "success_definition": "...",
    "strategic_alignment": "...",
    "anticipated_concerns": [
        {
            "concern": "...",
            "acknowledge": "...",
            "pivot": "...",
            "elevate": "..."
        }
    ],
    "landmines": ["..."],
    "proposed_next_steps": {
        "ideal": "...",
        "acceptable": "...",
        "minimum": "..."
    },
    "account_background": {
        "geo": "...",
        "segment": "...",
        "current_spend": "...",
        "expected_spend": "...",
        "ppa_status": "...",
        "account_summary": "..."
    },
    "appendix": {
        "previous_meeting_notes": "...",
        "customer_success_stories": "...",
        "competitive_intelligence": "..."
    },
    "last_updated": "2026-05-14"
}
"""

import json
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


def render_eb(data: dict, template_dir: str = None) -> str:
    """Render Executive Briefing data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    template = env.get_template("executive-briefing.html.j2")
    return template.render(**data)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = render_eb(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
