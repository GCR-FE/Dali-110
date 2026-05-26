#!/usr/bin/env python3
"""
EP HTML Renderer — fills the Jinja2 template with structured data and outputs rendered HTML.

Usage:
    python render_ep.py input.json output.html

Input: JSON file with the EP data structure (see DATA_SCHEMA below).
Output: Rendered HTML file.

DATA SCHEMA (what the agent produces):
{
    "customer_name": "GlobalRetail Inc.",
    "opportunity_name": "Cloud Migration - Data Center Exit",
    "deal_value": "$3.2M TCV",
    "industry": "Retail",
    "current_stage": "Technical Validation",
    "current_stage_index": 2,  // 0=Prospect, 1=Qualified, 2=Tech Val, 3=Biz Val, 4=Committed, 5=Closed
    "target_launch_date": "Q2 2026",
    "customer_type": "Existing Customer",
    "why_now": "...",
    "deal_objective": "...",
    "win_strategy": "...",
    "key_risks": "...",
    "estimate_best_milestones": 5,
    "estimate_best_timeline": "10 weeks",
    "estimate_worst_milestones": 8,
    "estimate_worst_timeline": "16 weeks",
    "stakeholders": [
        {
            "name": "Sarah Chen",
            "title": "CTO",
            "stance": "Champion",  // Maps to CSS class: pill-champion, pill-supporter, pill-neutral, pill-non-supporter, pill-adversary, pill-economic-buyer
            "engagement_priority": "Must Meet — ...",
            "role_in_deal": "Technical Evaluator — ...",
            "what_they_care_about": "...",
            "what_we_need": "...",
            "how_to_win": "..."
        }
    ],
    "roadmap": [
        {
            "number": 1,
            "target_window": "Week 1-2",
            "description": "...",
            "key_stakeholders": "CTO, IT Director",
            "aws_team": "AM, SA",
            "status": "Done"  // Done, Next, Planned, Skipped
        }
    ],
    "stakeholder_risks": [
        {
            "stakeholder": "CTO 王总",
            "red_flag": "Contact Not Made — ...",
            "leverage_source": "IT Director 赵工 (Sponsor) — ...",
            "plan_b": "..."
        }
    ],
    "milestone_risks": [
        {
            "milestone": "#2 CTO架构评审",
            "risk_item": "🧑 CTO 缺席/拒绝评审",
            "trigger": "两周内三次正式邀约均未获回应",
            "impact": "+2-3 weeks",
            "plan_b": "...",
            "severity": "high"  // high, medium, low
        }
    ],
    "next_milestone": {
        "title": "Technical POC Completion",
        "target_date": "March 28, 2026",
        "aws_team": "SA Team + ProServ",
        "objective": "...",
        "attendees": [
            {
                "name": "王总",
                "title": "CTO",
                "target_outcome": "当前 Neutral → Supporter: ..."
            }
        ],
        "key_questions": [
            "贵司今年的核心业务增长目标对底层基础设施有什么新要求？",
            "..."
        ]
    },
    "execution_log": [
        {
            "number": 1,
            "date": "2026-02-15",
            "attendees": "CTO, IT Director",
            "planned": "...",
            "actual": "...",
            "people_updates": "...",
            "key_learnings": "...",
            "plan_adjustment": "..."
        }
    ],
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


def render_ep(data: dict, template_dir: str = None) -> str:
    """Render EP data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    template = env.get_template("engagement-plan.html.j2")
    return template.render(**data)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = render_ep(data)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
