#!/usr/bin/env python3
"""
Contact Profile HTML Renderer — fills the Jinja2 template with structured data
and outputs rendered HTML.

Usage:
    python render_cp.py input.json output.html

Input: JSON file with the Contact Profile data structure (see DATA_SCHEMA below).
Output: Rendered HTML file.

DATA SCHEMA (what the agent produces):
{
  "contact_name": "张总",
  "contact_title": "总经理",
  "company": "海尔卡奥斯",
  "purpose": "overview",                      # overview / pre-visit / ebc-prep / relationship-review / objection-handling / custom
  "purpose_label": "总览",                    # 中文标签
  "updated_at": "2026-05-19",
  "rendered_at": "2026-05-19T22:30:00+08:00",
  "contact_count": 1,
  "overall_confidence": "只能给方向",
  "confidence_pct": 33,                       # 0-95
  "confidence_pct_label": "只能给方向",
  "confidence_pct_color": "low",              # high / medium / low / unknown
  "confidence_basis": [                       # 每条 1 句自然语言
    "接触 1 次(+10%)",
    "3 条信号,可靠度构成:R3:2 条、R4:1 条",
    "仅 1 个场景的孤证(−10%)"
  ],
  "sections": [
    {
      "key": "portrait",                      # 9 个标准 key 之一
      "title": "对他的整体描述",
      "icon": "account_circle",               # Material Symbols icon name
      "html": "<p>...</p>"                    # Markdown 已转 HTML 的内容
    },
    ...
  ]
}

9 个标准 section key + 默认 icon:
  confidence_narrative (verified)            — 这份报告的准确度
  portrait (account_circle)                  — 对他的整体描述
  situation (info)                           — 他的一些基本信息
  actions (history)                          — 他的一些行为记录
  habits_and_reasons (psychology)            — 他的做事习惯和可能的原因
  identity (favorite)                        — 他可能内心关注的
  relationship (handshake)                   — 和他目前的关系状态
  action_guidance (compass_calibration)      — 建议做什么 / 慎重做什么
  next_observations (visibility)             — 下一步的观察建议
"""

import json
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Standard section title + icon mapping (V2.0 wording)
# ---------------------------------------------------------------------------

SECTION_TITLE_ZH = {
    "confidence_narrative": "这份报告的准确度",
    "portrait":             "对他的整体描述",
    "situation":            "他的一些基本信息",
    "actions":              "他的一些行为记录",
    "habits_and_reasons":   "他的做事习惯和可能的原因",
    "identity":             "他可能内心关注的",
    "relationship":         "和他目前的关系状态",
    "action_guidance":      "建议做的 / 避免做的(参考)",
    "next_observations":    "下一步的观察建议",
}

SECTION_ICON = {
    "confidence_narrative": "verified",
    "portrait":             "account_circle",
    "situation":            "info",
    "actions":              "history",
    "habits_and_reasons":   "psychology",
    "identity":             "favorite",
    "relationship":         "handshake",
    "action_guidance":      "compass_calibration",
    "next_observations":    "visibility",
}

PURPOSE_LABEL_ZH = {
    "overview":            "总览",
    "pre-visit":           "拜访准备",
    "ebc-prep":            "EBC 准备",
    "relationship-review": "关系复盘",
    "objection-handling":  "异议应对",
    "custom":              "自由目的",
}


def normalize_data(data: dict) -> dict:
    """Fill in defaults for icon / title / labels if not provided."""
    # Default purpose label
    if "purpose_label" not in data and "purpose" in data:
        data["purpose_label"] = PURPOSE_LABEL_ZH.get(data["purpose"], data["purpose"])

    # Default section title + icon if not provided
    for sec in data.get("sections", []):
        if "title" not in sec and "key" in sec:
            sec["title"] = SECTION_TITLE_ZH.get(sec["key"], sec["key"])
        if "icon" not in sec and "key" in sec:
            sec["icon"] = SECTION_ICON.get(sec["key"], "article")

    return data


def render_cp(data: dict, template_dir: str = None) -> str:
    """Render Contact Profile data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    data = normalize_data(data)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
    )
    template = env.get_template("contact-profiling.html.j2")
    return template.render(**data)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = render_cp(data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
