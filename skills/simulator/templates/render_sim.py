#!/usr/bin/env python3
"""
Simulator Rehearsal Notes HTML Renderer.

Usage:
    python render_sim.py input.json output.html

DATA SCHEMA:
{
  "contact_name": "张总",
  "contact_title": "总经理",
  "company": "海尔卡奥斯",
  "scenario": "首次方案沟通",
  "difficulty": "medium",                   # low / medium / high
  "difficulty_label": "中",                 # 中文
  "rehearsal_date": "2026-05-19",
  "rendered_at": "2026-05-19T22:30:00+08:00",
  "rounds": 12,
  "trust_trajectory": "flat",               # up / flat / down
  "fidelity": "medium",                     # high / medium / low

  "takeaways": {                            # 0. 开篇价值三件事
    "preparation": "...",
    "what_might_happen": "...",
    "adjustment": "..."
  },

  "sections": [                             # 1-10 段
    {
      "key": "basics",
      "title": "1. 这次模拟的基本情况",
      "html": "..."
    },
    ...
  ]
}

11 段标准结构:
  0. takeaways (开篇价值三件事 — 在 takeaways 字段)
  1. basics                  — 这次模拟的基本情况
  2. customer_style          — 客户这次的风格和表现
  3. pressure_sources        — 他这些反应是哪里来的
  4. did_well                — 你做得好的地方
  5. role_taken              — 你这次是以什么身份去见他的
  6. improvements            — 可以改进的地方(融入三通道留意)
  7. landmines               — 踩雷时刻
  8. relationship_movement   — 关系是往前走了还是退了
  9. next_prep               — 下次真实见面前再准备这几件事
  10. unverified_assumptions — 还没验证的假设
"""

import json
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


SECTION_TITLE_ZH = {
    "basics":                  "1. 这次模拟的基本情况",
    "customer_style":          "2. 客户这次的风格和表现",
    "pressure_sources":        "3. 他这些反应是哪里来的",
    "did_well":                "4. 你做得好的地方",
    "role_taken":              "5. 这次对谈后他很可能会把你看作:",
    "improvements":            "6. 可以改进的地方",
    "landmines":               "7. \"踩雷\"时刻",
    "relationship_movement":   "8. 关系是往前走了还是退了",
    "next_prep":               "9. 下次真实见面前考虑做以下准备",
    "unverified_assumptions":  "10. 还没验证的推测",
}

DIFFICULTY_LABEL_ZH = {
    "low":    "低",
    "medium": "中",
    "high":   "高",
}


def normalize_data(data: dict) -> dict:
    """Fill in defaults for title / labels."""
    if "difficulty_label" not in data and "difficulty" in data:
        data["difficulty_label"] = DIFFICULTY_LABEL_ZH.get(data["difficulty"], data["difficulty"])

    for sec in data.get("sections", []):
        if "title" not in sec and "key" in sec:
            sec["title"] = SECTION_TITLE_ZH.get(sec["key"], sec["key"])

    return data


def render_sim(data: dict, template_dir: str = None) -> str:
    """Render Simulator Rehearsal Notes data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    data = normalize_data(data)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
    )
    template = env.get_template("simulator.html.j2")
    return template.render(**data)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = render_sim(data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
