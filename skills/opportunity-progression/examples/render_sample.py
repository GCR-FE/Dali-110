#!/usr/bin/env python3
"""
Render examples/sample-data.json into examples/sample-report.html using
templates/opportunity-progression.html.j2.

Purpose:
- Validates the Jinja2 template at every change
- Produces a visual preview file that can be opened in a browser

Usage:
    python3 examples/render_sample.py
    # → writes examples/sample-report.html
"""
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT / "templates"
DATA_FILE = ROOT / "examples" / "sample-data.json"
OUT_FILE = ROOT / "examples" / "sample-report.html"


def render() -> Path:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("opportunity-progression.html.j2")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = template.render(**data)
    OUT_FILE.write_text(html, encoding="utf-8")
    return OUT_FILE


if __name__ == "__main__":
    out = render()
    print(f"✅ Rendered: {out}")
