#!/usr/bin/env python3
"""Warning Card HTML Injector — the canonical renderer.

Reads a Warning Card markdown source file, parses it via parser.py, and
produces an HTML deliverable that matches the structure and design of
templates/WARNING_CARD_REFERENCE.html.

Usage:
    python3 inject.py \
        --card MI_{Customer}_{YYYY-MM-DD}.md \
        --out MI_{Customer}_{YYYY-MM-DD}.html \
        [--reasoning MI_{Customer}_reasoning.md]

The generated HTML includes:
  - An "Export PDF" button (uses window.print())
  - A ?print=1 URL parameter trigger for headless browser PDF export
  - @media print rules for A4 pagination

Design system (from WARNING_CARD_REFERENCE.html):
  - Purple-accent palette (--accent: #6d58e4)
  - Inter + Noto Sans SC fonts
  - Material Icons Outlined
  - Card-based layout with semantic section colors
  - Responsive grid for stats, signals, and action paths
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from typing import List

# Allow import when this script lives in scripts/
sys.path.insert(0, str(Path(__file__).parent))
from parser import (
    Card, Reasoning, ReasoningSection, Signal, SourceLink, OpportunityRow,
    parse_markdown, parse_reasoning, sanitize,
)


def h(text: str) -> str:
    """HTML-escape text."""
    return html.escape(text, quote=True)


# ---------------------------------------------------------------------------
# Component renderers — each returns an HTML fragment string
# ---------------------------------------------------------------------------

def _render_source_links(sources: List[SourceLink]) -> str:
    parts = []
    for s in sources:
        parts.append('<a href="' + h(s.url) + '" target="_blank">' + h(s.label) + '</a>')
    return "<br>\n          ".join(parts)


def _render_signal(sig: Signal, css_class: str) -> str:
    src_html = _render_source_links(sig.sources)
    return (
        '      <div class="sig ' + css_class + '">\n'
        '        <div class="rk-row">\n'
        '          <span class="rk">排名 #' + str(sig.rank) + '</span>\n'
        '          <span class="dim">' + h(sig.dimension) + '</span>\n'
        '        </div>\n'
        '        <div class="body">' + h(sig.text) + '</div>\n'
        '        <div class="reason">\n'
        '          <span class="ico">推理</span>\n'
        '          <span>' + h(sig.reasoning) + '</span>\n'
        '        </div>\n'
        '        <div class="src">\n'
        '          ' + src_html + '\n'
        '        </div>\n'
        '      </div>'
    )


def _render_opp_table(rows: List[OpportunityRow]) -> str:
    lines = []
    for row in rows:
        lines.append(
            "          <tr><td>" + h(row.capability) + "</td>"
            "<td>" + h(row.need) + "</td>"
            "<td>" + h(row.arr) + "</td></tr>"
        )
    return "\n".join(lines)


def _render_escalation(escalation: str) -> str:
    steps = [s.strip() for s in escalation.split("\u2192") if s.strip()]
    if not steps:
        return ""
    nodes = []
    for i, step in enumerate(steps):
        css = ""
        if i == 0:
            css = " active"
        elif i == len(steps) - 1:
            css = " end"
        circle = str(i + 1) if i > 0 else ""
        nodes.append(
            '        <div class="node' + css + '">\n'
            '          <span class="circle">' + circle + '</span>\n'
            '          <span class="t">' + h(step) + '</span>\n'
            '        </div>'
        )
        if i < len(steps) - 1:
            nodes.append('        <div class="bar"></div>')
    return "\n".join(nodes)


def _render_core_messages(core: str) -> str:
    items = re.split(r"[\u2460\u2461\u2462\u2463\u2464]\s*", core)
    items = [it.strip() for it in items if it.strip()]
    if not items:
        items = [core]
    lines = []
    for i, item in enumerate(items, 1):
        ico = chr(0x2460 + i - 1)
        lines.append(
            '      <li><span class="ico">' + ico + '</span>'
            '<div>' + h(item) + '</div></li>'
        )
    return "\n".join(lines)


def _render_reasoning_section(sec: ReasoningSection) -> str:
    parts = []
    title = h(sec.marker) + " \u00b7 " + h(sec.title_en)
    if sec.title_cn:
        title += " \u00b7 " + h(sec.title_cn)
    parts.append(
        '    <div class="card">\n'
        '      <h2><span class="material-icons-outlined">psychology</span>'
        + title + '</h2>'
    )
    for para in sec.paragraphs:
        parts.append(
            '      <p style="font-size:12.5px; color:var(--ink-2); '
            'line-height:1.6; margin:0 0 10px;">' + h(para) + '</p>'
        )
    if sec.table_rows:
        parts.append('      <div class="arr-wrap"><table class="arr"><tbody>')
        for row in sec.table_rows:
            cells = "".join("<td>" + h(c) + "</td>" for c in row)
            parts.append("        <tr>" + cells + "</tr>")
        parts.append("      </tbody></table></div>")
    if sec.bullets:
        parts.append('      <ul style="list-style:disc; padding-left:18px; margin:8px 0;">')
        for b in sec.bullets:
            parts.append(
                '        <li style="font-size:12.5px; color:var(--ink-2); '
                'line-height:1.6; margin-bottom:4px;">' + h(b) + '</li>'
            )
        parts.append("      </ul>")
    if sec.numbered:
        parts.append('      <ol style="padding-left:18px; margin:8px 0;">')
        for n in sec.numbered:
            parts.append(
                '        <li style="font-size:12.5px; color:var(--ink-2); '
                'line-height:1.6; margin-bottom:4px;">' + h(n) + '</li>'
            )
        parts.append("      </ol>")
    parts.append("    </div>")
    return "\n".join(parts)


def _reason_note(text: str) -> str:
    if not text:
        return ""
    return (
        '    <div class="reason-note">\n'
        '      <span class="material-icons-outlined">psychology</span>\n'
        '      <div><strong>推理</strong>' + h(text) + '</div>\n'
        '    </div>'
    )


# ---------------------------------------------------------------------------
# CSS — extracted from WARNING_CARD_REFERENCE.html
# ---------------------------------------------------------------------------

CSS = """:root {
    --ink: #1a1a2e;
    --ink-2: #30304a;
    --muted: #6b6b85;
    --muted-2: #a0a0b5;
    --line: #e8e6f2;
    --line-soft: #f3f1fa;
    --paper: #ffffff;
    --page-bg: #f6f4fb;
    --accent: #6d58e4;
    --accent-dark: #4a3bd0;
    --accent-soft: #eceafa;
    --accent-softer: #f4f2fc;
    --ok: #1e8f56;
    --ok-soft: #dff3e7;
    --warn: #c47610;
    --warn-soft: #fdf1dd;
    --bad: #c53030;
    --bad-soft: #fde4e4;
    --coi: #7c2d12;
    --coi-soft: #fef5e7;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--page-bg); color: var(--ink);
    font-family: "Inter", "Noto Sans SC", -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 13px; line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  .material-icons-outlined {
    font-family: 'Material Icons Outlined'; font-weight: normal; font-style: normal;
    font-size: 20px; line-height: 1; letter-spacing: normal; text-transform: none;
    display: inline-block; white-space: nowrap; word-wrap: normal; direction: ltr;
    -webkit-font-feature-settings: 'liga'; -webkit-font-smoothing: antialiased;
  }
  .export-bar {
    position: sticky; top: 0; z-index: 10; background: #1a1a2e; color: #fff;
    padding: 10px 24px; display: flex; align-items: center; justify-content: space-between;
  }
  .export-bar .brand { font-size: 11px; letter-spacing: 2px; color: #c9c3f5; font-weight: 700; text-transform: uppercase; }
  .export-bar button {
    background: var(--accent); color: #fff; border: 0; border-radius: 6px;
    padding: 7px 14px; font-size: 12px; font-weight: 600; cursor: pointer;
    display: inline-flex; align-items: center; gap: 6px;
  }
  .export-bar button:hover { background: var(--accent-dark); }
  .sheet { max-width: 900px; margin: 28px auto 56px; padding: 0 28px; }
  .head { display: flex; align-items: flex-start; justify-content: space-between; gap: 20px; padding: 8px 8px 20px; }
  .head .kicker { font-size: 11px; font-weight: 700; letter-spacing: 2.4px; text-transform: uppercase; color: var(--accent); margin-bottom: 6px; }
  .head h1 { font-size: 34px; font-weight: 600; letter-spacing: -0.6px; margin: 0 0 6px; color: var(--ink); line-height: 1.1; }
  .head .sub { font-size: 13px; color: var(--muted); }
  .head .pill { display: inline-flex; align-items: center; gap: 8px; background: var(--accent-soft); color: var(--accent-dark); padding: 10px 16px; border-radius: 10px; font-size: 14px; font-weight: 700; white-space: nowrap; }
  .head .pill .material-icons-outlined { font-size: 18px; }
  .card { background: var(--accent-softer); border-radius: 14px; padding: 22px 24px; margin-bottom: 14px; }
  .card h2 { display: flex; align-items: center; gap: 10px; margin: 0 0 16px; font-size: 16px; font-weight: 600; color: var(--ink); letter-spacing: -0.2px; }
  .card h2 .material-icons-outlined { font-size: 20px; color: var(--accent); padding: 6px; background: var(--paper); border-radius: 6px; box-shadow: 0 1px 2px rgba(26,26,46,0.05); }
  .card h2 .est { font-size: 10px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: var(--warn); background: var(--warn-soft); padding: 3px 8px; border-radius: 999px; margin-left: 6px; }
  .sig-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }
  .sig { background: var(--paper); border-radius: 10px; padding: 16px 18px; border-left: 3px solid var(--accent); }
  .sig.r1 { border-left-color: var(--accent); }
  .sig.r2 { border-left-color: var(--muted); }
  .sig.r3 { border-left-color: var(--muted-2); }
  .sig .rk-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
  .sig .rk { font-size: 10px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: var(--accent); background: var(--accent-soft); padding: 2px 8px; border-radius: 999px; }
  .sig.r2 .rk { color: var(--muted); background: var(--line-soft); }
  .sig.r3 .rk { color: var(--muted-2); background: var(--line-soft); }
  .sig .dim { font-size: 11px; color: var(--muted); font-weight: 500; }
  .sig .body { font-size: 12.5px; color: var(--ink-2); line-height: 1.55; margin-bottom: 10px; }
  .sig .reason { display: flex; gap: 8px; align-items: flex-start; font-size: 11.5px; color: var(--muted); line-height: 1.5; background: var(--line-soft); border-radius: 6px; padding: 8px 10px; margin-bottom: 10px; }
  .sig .reason .ico { flex: 0 0 auto; font-size: 9px; font-weight: 700; letter-spacing: 0.6px; color: var(--accent); background: var(--accent-soft); padding: 2px 6px; border-radius: 4px; margin-top: 1px; }
  .sig .src { font-size: 11px; line-height: 1.7; }
  .sig .src a { color: var(--accent); font-weight: 500; }
  .watchlist { margin-top: 14px; padding: 10px 14px; background: var(--paper); border-radius: 8px; font-size: 12px; color: var(--ink-2); display: flex; gap: 8px; align-items: flex-start; }
  .watchlist .material-icons-outlined { font-size: 16px; color: var(--muted); margin-top: 1px; }
  .impact-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .imp { background: var(--paper); border-radius: 10px; padding: 14px 16px; }
  .imp .lab { font-size: 10px; letter-spacing: 1.2px; text-transform: uppercase; font-weight: 700; color: var(--muted); margin-bottom: 6px; }
  .imp .val { font-size: 12.5px; color: var(--ink-2); line-height: 1.5; }
  .reason-note { margin-top: 12px; display: flex; gap: 8px; align-items: flex-start; font-size: 11.5px; color: var(--muted); line-height: 1.5; background: var(--line-soft); border-radius: 8px; padding: 10px 14px; }
  .reason-note .material-icons-outlined { font-size: 16px; color: var(--accent); margin-top: 1px; }
  .arr-wrap { margin-bottom: 12px; overflow-x: auto; }
  .arr { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  .arr th { background: var(--accent); color: #fff; padding: 10px 14px; text-align: left; font-weight: 600; font-size: 12px; }
  .arr th:last-child { text-align: right; }
  .arr td { padding: 10px 14px; border-bottom: 1px solid var(--line-soft); background: var(--paper); color: var(--ink-2); }
  .arr td:last-child { text-align: right; font-weight: 600; color: var(--ink); }
  .advantage { margin: 12px 0; font-size: 12.5px; color: var(--ink-2); display: flex; gap: 10px; align-items: flex-start; }
  .advantage .material-icons-outlined { color: var(--accent); font-size: 18px; margin-top: 1px; }
  .advantage strong { color: var(--ink); margin-right: 4px; }
  .urg-top { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; }
  .urg-top .u { background: var(--paper); border-radius: 10px; padding: 12px 14px; }
  .urg-top .u .lab { font-size: 10px; color: var(--muted); font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 4px; }
  .urg-top .u .val { font-size: 12.5px; color: var(--ink-2); line-height: 1.5; }
  .coi-card { background: var(--coi-soft); border-radius: 10px; padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start; margin-bottom: 12px; }
  .coi-card .material-icons-outlined { color: var(--warn); font-size: 20px; margin-top: 1px; }
  .coi-card .lab { font-size: 10px; letter-spacing: 1.2px; text-transform: uppercase; font-weight: 700; color: var(--warn); display: block; margin-bottom: 2px; }
  .coi-card .val { font-size: 13px; color: var(--ink); }
  .coi-card .val strong { color: var(--coi); }
  .sim { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .sim .s { background: var(--paper); border-radius: 10px; padding: 12px 14px; border-left: 3px solid var(--muted-2); }
  .sim .s.good { border-left-color: var(--ok); }
  .sim .s.warn { border-left-color: var(--warn); }
  .sim .s.bad { border-left-color: var(--bad); }
  .sim .s .when { font-size: 10.5px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 4px; }
  .sim .s.good .when { color: var(--ok); }
  .sim .s.warn .when { color: var(--warn); }
  .sim .s.bad .when { color: var(--bad); }
  .sim .s .what { font-size: 12px; color: var(--ink-2); line-height: 1.45; }
  .psy { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .psy .p { background: var(--paper); border-radius: 10px; padding: 14px 16px; }
  .psy .p .lab { font-size: 10px; letter-spacing: 1.2px; text-transform: uppercase; font-weight: 700; color: var(--muted); margin-bottom: 6px; }
  .psy .p .val { font-size: 12.5px; color: var(--ink-2); line-height: 1.55; }
  .motion-chip { display: inline-flex; align-items: center; gap: 5px; background: var(--accent); color: #fff; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; margin-right: 6px; }
  .motion-chip .material-icons-outlined { font-size: 13px; }
  .hook { margin-top: 12px; background: var(--paper); border-radius: 10px; padding: 14px 18px; border-left: 3px solid var(--accent); font-size: 13px; color: var(--ink); line-height: 1.65; font-style: italic; }
  .hook .lab { display: block; font-style: normal; font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); font-weight: 700; margin-bottom: 4px; }
  .action-snapshot { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; }
  .action-snapshot .stat { background: var(--paper); border-radius: 10px; text-align: left; padding: 14px 16px; }
  .action-snapshot .stat .lab { text-align: left; font-size: 10px; letter-spacing: 1.2px; text-transform: uppercase; font-weight: 700; color: var(--muted); margin-bottom: 4px; }
  .action-snapshot .stat .val { text-align: left; font-size: 12.5px; color: var(--ink-2); font-weight: 500; line-height: 1.45; }
  .core-list { list-style: none; padding: 0; margin: 0; background: var(--paper); border-radius: 10px; overflow: hidden; }
  .core-list li { display: flex; align-items: flex-start; gap: 10px; padding: 11px 16px; border-bottom: 1px solid var(--line-soft); font-size: 12.5px; color: var(--ink-2); line-height: 1.5; }
  .core-list li:last-child { border-bottom: 0; }
  .core-list li .ico { flex: 0 0 auto; width: 22px; height: 22px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: inline-flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; }
  .timeline { background: var(--paper); border-radius: 10px; padding: 16px 14px 12px; display: flex; align-items: center; gap: 0; flex-wrap: wrap; }
  .node { display: flex; flex-direction: column; align-items: center; gap: 4px; min-width: 60px; }
  .node .circle { width: 24px; height: 24px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: inline-flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; }
  .node.active .circle { background: var(--accent); color: #fff; }
  .node.end .circle { background: var(--ok); color: #fff; }
  .node .t { font-size: 10.5px; color: var(--ink-2); text-align: center; line-height: 1.3; }
  .bar { flex: 1; min-width: 20px; height: 2px; background: var(--line); margin: 0 4px; align-self: center; margin-bottom: 18px; }
  .foot { text-align: center; padding: 18px 0 0; font-size: 11px; color: var(--muted-2); letter-spacing: 0.3px; }
  .foot .dl { display: block; font-size: 11.5px; color: var(--muted); margin-bottom: 4px; font-style: italic; }
  .foot .dl strong { color: var(--accent); font-style: normal; }
  @page { size: A4; margin: 12mm 10mm; }
  @media print {
    body { background: #fff; }
    .export-bar { display: none; }
    .sheet { margin: 0; padding: 0; max-width: none; }
    .card { break-inside: avoid; }
    .sig-grid, .impact-grid, .urg-top, .sim, .psy, .timeline, .core-list, .action-snapshot { break-inside: avoid; }
    .card h2 .material-icons-outlined { box-shadow: none; border: 1px solid var(--line); }
  }"""


# ---------------------------------------------------------------------------
# Main generator — builds HTML by list concatenation (no nested f-strings)
# ---------------------------------------------------------------------------

def generate_html(card: Card, reasoning: Reasoning | None = None) -> str:
    """Generate the full HTML deliverable from parsed Card + optional Reasoning."""
    out: List[str] = []

    # --- Head ---
    out.append('<!DOCTYPE html>')
    out.append('<html lang="zh-Hans">')
    out.append('<head>')
    out.append('<meta charset="UTF-8" />')
    out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0" />')
    out.append('<title>市场情报预警卡 · ' + h(card.customer) + '</title>')
    out.append('<link rel="preconnect" href="https://fonts.googleapis.com" />')
    out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />')
    out.append('<link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet" />')
    out.append('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet" />')
    out.append('<style>')
    out.append(CSS)
    out.append('</style>')
    out.append('</head>')
    out.append('<body>')
    out.append('')

    # --- Export bar ---
    out.append('<div class="export-bar">')
    out.append('  <div class="brand">\u25c6 MARKET INTELLIGENCE \u00b7 WARNING CARD</div>')
    out.append('  <button onclick="window.print()">')
    out.append('    <span class="material-icons-outlined" style="font-size:16px;">picture_as_pdf</span>')
    out.append('    Export PDF')
    out.append('  </button>')
    out.append('</div>')
    out.append('')
    out.append('<div class="sheet">')
    out.append('')

    # --- Header ---
    coi_pill = ""
    if card.coi_headline and card.coi_y3:
        coi_pill = "CoI " + card.coi_headline + " / 3Y " + card.coi_y3
    elif card.coi_headline:
        coi_pill = "CoI " + card.coi_headline

    out.append('  <!-- Header -->')
    out.append('  <div class="head">')
    out.append('    <div>')
    out.append('      <div class="kicker">Market Intelligence \u00b7 客户策略变化预警器</div>')
    out.append('      <h1>' + h(card.customer) + '</h1>')
    out.append('      <div class="sub">' + h(card.industry) + ' \u00b7 ' + h(card.date) + ' \u00b7 Owner: ' + h(card.owner or "待 AWSentral 补") + '</div>')
    out.append('    </div>')
    if coi_pill:
        out.append('    <div class="pill">')
        out.append('      <span class="material-icons-outlined">warning_amber</span>')
        out.append('      ' + h(coi_pill))
        out.append('    </div>')
    out.append('  </div>')
    out.append('')

    # --- Signal Layer ---
    out.append('  <!-- Signal Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">sensors</span>Signal Layer \u00b7 信号层</h2>')
    out.append('    <div class="sig-grid">')
    for sig in card.signals[:5]:
        css = "r" + str(sig.rank) if sig.rank <= 3 else "r3"
        out.append(_render_signal(sig, css))
    out.append('    </div>')
    if card.observation:
        obs_links = ""
        if card.observation_links:
            obs_links = " \u2014 " + " \u00b7 ".join(
                '<a href="' + h(s.url) + '" target="_blank">' + h(s.label) + '</a>'
                for s in card.observation_links
            )
        out.append('    <div class="watchlist">')
        out.append('      <span class="material-icons-outlined">visibility</span>')
        out.append('      <div><strong>观察清单</strong>' + h(card.observation) + obs_links + '</div>')
        out.append('    </div>')
    out.append('  </div>')
    out.append('')

    # --- Impact Layer ---
    out.append('  <!-- Impact Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">groups</span>Impact Layer \u00b7 影响层</h2>')
    out.append('    <div class="impact-grid">')
    out.append('      <div class="imp"><div class="lab">谁的 KPI</div><div class="val">' + h(card.impact_who) + '</div></div>')
    out.append('      <div class="imp"><div class="lab">具体影响</div><div class="val">' + h(card.impact_detail) + '</div></div>')
    out.append('      <div class="imp"><div class="lab">时间线</div><div class="val">' + h(card.impact_timeline) + '</div></div>')
    out.append('    </div>')
    if card.impact_reasoning:
        out.append(_reason_note(card.impact_reasoning))
    out.append('  </div>')
    out.append('')

    # --- Opportunity Layer ---
    out.append('  <!-- Opportunity Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">trending_up</span>Opportunity Layer \u00b7 机会层 <span class="est">估算 \u00b7 需内部数据</span></h2>')
    out.append('    <div class="arr-wrap">')
    out.append('      <table class="arr">')
    out.append('        <thead><tr><th>AWS 能力</th><th>匹配需求</th><th>ARR（估算）</th></tr></thead>')
    out.append('        <tbody>')
    out.append(_render_opp_table(card.opportunity_rows))
    out.append('        </tbody>')
    out.append('      </table>')
    out.append('    </div>')
    if card.opportunity_advantage:
        out.append('    <div class="advantage">')
        out.append('      <span class="material-icons-outlined">verified</span>')
        out.append('      <div><strong>独特优势</strong>' + h(card.opportunity_advantage) + '</div>')
        out.append('    </div>')
    if card.opportunity_reasoning:
        out.append(_reason_note(card.opportunity_reasoning))
    out.append('  </div>')
    out.append('')

    # --- Urgency Layer ---
    out.append('  <!-- Urgency Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">schedule</span>Urgency Layer \u00b7 紧迫性层</h2>')
    out.append('    <div class="urg-top">')
    out.append('      <div class="u"><div class="lab">窗口</div><div class="val">' + h(card.urgency_window) + '</div></div>')
    out.append('      <div class="u"><div class="lab">竞对</div><div class="val">' + h(card.urgency_competitor) + '</div></div>')
    out.append('      <div class="u"><div class="lab">衰减</div><div class="val">' + h(card.urgency_decay) + '</div></div>')
    out.append('    </div>')
    # CoI card
    coi_text = card.urgency_coi or card.coi_detail
    out.append('    <div class="coi-card">')
    out.append('      <span class="material-icons-outlined">priority_high</span>')
    out.append('      <div>')
    out.append('        <span class="lab">Cost of Inaction \u00b7 不行动成本</span>')
    out.append('        <span class="val">' + h(coi_text) + '</span>')
    out.append('      </div>')
    out.append('    </div>')
    # Simulation
    sim_good = card.urgency_sim_good or "进入候选"
    sim_warn = card.urgency_sim_warn or "机会缩小"
    sim_bad = card.urgency_sim_bad or "机会归零"
    out.append('    <div class="sim">')
    out.append('      <div class="s good"><div class="when">本周动</div><div class="what">' + h(sim_good) + '</div></div>')
    out.append('      <div class="s warn"><div class="when">1\u20133 月内</div><div class="what">' + h(sim_warn) + '</div></div>')
    out.append('      <div class="s bad"><div class="when">过窗口</div><div class="what">' + h(sim_bad) + '</div></div>')
    out.append('    </div>')
    if card.urgency_reasoning:
        out.append(_reason_note(card.urgency_reasoning))
    out.append('  </div>')
    out.append('')

    # --- Psychology Layer ---
    motion_text = card.psychology_motion or ""
    motion_chip_label = ""
    motion_detail = motion_text
    for m in ["CHALLENGER", "SPIN", "JOLT", "VALUE"]:
        if m.lower() in motion_text.lower():
            motion_chip_label = m
            motion_detail = motion_text.replace(m, "").replace(m.lower(), "").replace(m.title(), "").strip(" \u2014\u00b7-")
            break

    out.append('  <!-- Psychology Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">psychology</span>Psychology Layer \u00b7 心理层</h2>')
    out.append('    <div class="psy">')
    out.append('      <div class="p"><div class="lab">决策者状态</div><div class="val">' + h(card.psychology_state) + '</div></div>')
    motion_val = ""
    if motion_chip_label:
        motion_val = '<span class="motion-chip"><span class="material-icons-outlined">flash_on</span>' + motion_chip_label + '</span>'
    motion_val += h(motion_detail)
    out.append('      <div class="p"><div class="lab">推荐 Motion</div><div class="val">' + motion_val + '</div></div>')
    if card.psychology_pits:
        out.append('      <div class="p" style="grid-column: 1 / -1;"><div class="lab">避坑</div><div class="val">' + h(card.psychology_pits) + '</div></div>')
    out.append('    </div>')
    if card.psychology_hook:
        out.append('    <div class="hook">')
        out.append('      <span class="lab">话术钩子 \u00b7 Opening Hook</span>')
        out.append('      ' + h(card.psychology_hook))
        out.append('    </div>')
    if card.psychology_reasoning:
        out.append(_reason_note(card.psychology_reasoning))
    out.append('  </div>')
    out.append('')

    # --- Action Layer ---
    out.append('  <!-- Action Layer -->')
    out.append('  <div class="card">')
    out.append('    <h2><span class="material-icons-outlined">flag</span>Action Layer \u00b7 行动层 <span class="est">估算 \u00b7 需内部数据</span></h2>')
    out.append('    <div class="action-snapshot">')
    out.append('      <div class="stat"><div class="lab">本周第一步</div><div class="val">' + h(card.action_first_step) + '</div></div>')
    out.append('      <div class="stat"><div class="lab">目标</div><div class="val">教导而非 pitch</div></div>')
    out.append('      <div class="stat"><div class="lab">成功标准</div><div class="val">落地 Workshop</div></div>')
    out.append('    </div>')
    if card.action_opening:
        out.append('    <div class="hook" style="margin-top:0; margin-bottom:12px;">')
        out.append('      <span class="lab">开场话术 \u00b7 引用 #1 信号</span>')
        out.append('      ' + h(card.action_opening))
        out.append('    </div>')
    if card.action_core:
        out.append('    <ul class="core-list">')
        out.append(_render_core_messages(card.action_core))
        out.append('    </ul>')
    if card.action_reasoning:
        out.append(_reason_note(card.action_reasoning))
    if card.action_escalation:
        out.append('    <div style="margin-top:14px;">')
        out.append('      <div style="font-size:10px; letter-spacing:1.2px; text-transform:uppercase; font-weight:700; color:var(--muted); margin-bottom:8px; padding-left:2px;">升级路径 \u00b7 Escalation</div>')
        out.append('      <div class="timeline">')
        out.append(_render_escalation(card.action_escalation))
        out.append('      </div>')
        out.append('    </div>')
    out.append('  </div>')
    out.append('')

    # --- Footer ---
    out.append('  <!-- Footer -->')
    out.append('  <div class="foot">')
    out.append('    <span class="dl">下游 \u00b7 触发 <strong>business-insight</strong>（内含 PESTLE + Porter\'s 5F + BMC → SWOT/TOWS → Top Initiatives）</span>')
    out.append('    Generated by Kiro \u00b7 Market Intelligence \u00b7 ' + h(card.date))
    out.append('  </div>')

    # --- Reasoning appendix (optional) ---
    if reasoning and reasoning.sections:
        out.append('')
        out.append('  <!-- Reasoning Appendix -->')
        out.append('  <div style="margin-top:36px; padding-top:24px; border-top:2px solid var(--line);">')
        out.append('    <div style="font-size:11px; font-weight:700; letter-spacing:2.4px; text-transform:uppercase; color:var(--accent); margin-bottom:6px;">推理与逻辑 \u00b7 Reasoning Appendix</div>')
        subtitle = reasoning.subtitle or "三个信号如何推导出本周行动"
        out.append('    <div style="font-size:13px; color:var(--muted); margin-bottom:20px;">' + h(subtitle) + '</div>')
        for sec in reasoning.sections:
            out.append(_render_reasoning_section(sec))
        out.append('  </div>')

    out.append('')
    out.append('</div>')  # .sheet
    out.append('')
    out.append('<script>')
    out.append("  const params = new URLSearchParams(window.location.search);")
    out.append("  if (params.get('print') === '1') {")
    out.append("    window.addEventListener('load', () => setTimeout(() => window.print(), 400));")
    out.append("  }")
    out.append('</script>')
    out.append('</body>')
    out.append('</html>')

    return "\n".join(out)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def render(md_path: Path, out_path: Path, reasoning_path: Path | None = None) -> Path:
    """Main entry point: parse markdown -> generate HTML -> write to disk."""
    src = sanitize(md_path.read_text(encoding="utf-8"))
    card = parse_markdown(src)

    reasoning = None
    if reasoning_path and reasoning_path.exists():
        r_src = sanitize(reasoning_path.read_text(encoding="utf-8"))
        reasoning = parse_reasoning(r_src)

    html_content = generate_html(card, reasoning)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_content, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Render a Market Intelligence Warning Card as HTML."
    )
    ap.add_argument(
        "--card", required=True, type=Path,
        help="Path to the card Markdown source (e.g. MI_{Customer}_{Date}.md)",
    )
    ap.add_argument(
        "--reasoning", type=Path, default=None,
        help="Optional path to the reasoning appendix Markdown",
    )
    ap.add_argument(
        "--out", required=True, type=Path,
        help="Output HTML path (e.g. MI_{Customer}_{Date}.html)",
    )
    args = ap.parse_args()
    result = render(args.card, args.out, args.reasoning)
    print("HTML: " + str(result))
    print("Open in browser, then Export PDF or use: ?print=1 for headless export")
