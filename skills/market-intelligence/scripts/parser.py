"""Warning Card markdown parser and data model.

Parses the Warning Card markdown (MI_{Customer}_{YYYY-MM-DD}.md) and the
Reasoning appendix (MI_{Customer}_reasoning.md) into structured Python
objects that the HTML injector can consume.

This module is pure Python — no rendering dependencies, no font paths,
no platform-specific code. It runs identically on macOS, Linux, and Windows.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class SourceLink:
    label: str
    url: str


@dataclass
class Signal:
    rank: int
    dimension: str
    text: str
    reasoning: str = ""
    sources: List[SourceLink] = field(default_factory=list)


@dataclass
class OpportunityRow:
    capability: str
    need: str
    arr: str


@dataclass
class Card:
    customer: str = ""
    industry: str = ""
    date: str = ""
    owner: str = ""
    note: str = ""
    signals: List[Signal] = field(default_factory=list)
    observation: str = ""
    observation_links: List[SourceLink] = field(default_factory=list)
    impact_who: str = ""
    impact_detail: str = ""
    impact_timeline: str = ""
    impact_reasoning: str = ""
    urgency_window: str = ""
    urgency_competitor: str = ""
    urgency_decay: str = ""
    urgency_coi: str = ""
    urgency_sim_good: str = ""
    urgency_sim_warn: str = ""
    urgency_sim_bad: str = ""
    urgency_reasoning: str = ""
    coi_headline: str = ""
    coi_y3: str = ""
    coi_detail: str = ""
    psychology_state: str = ""
    psychology_motion: str = ""
    psychology_pits: str = ""
    psychology_hook: str = ""
    psychology_reasoning: str = ""
    opportunity_rows: List[OpportunityRow] = field(default_factory=list)
    opportunity_advantage: str = ""
    opportunity_caption: str = ""
    opportunity_reasoning: str = ""
    action_first_step: str = ""
    action_opening: str = ""
    action_core: str = ""
    action_escalation: str = ""
    action_reasoning: str = ""
    internal_data: str = ""


@dataclass
class ReasoningSection:
    marker: str       # e.g. "§01"
    title_en: str
    title_cn: str
    paragraphs: List[str] = field(default_factory=list)
    table_rows: List[List[str]] = field(default_factory=list)
    bullets: List[str] = field(default_factory=list)
    numbered: List[str] = field(default_factory=list)


@dataclass
class Reasoning:
    title: str = ""
    subtitle: str = ""
    customer: str = ""
    date: str = ""
    sections: List[ReasoningSection] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------

INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def strip_code(s: str) -> str:
    """Remove backtick code markers."""
    return re.sub(r"`([^`]+)`", r"\1", s)


def strip_bold(s: str) -> str:
    """Remove markdown bold markers."""
    return re.sub(r"\*\*(.+?)\*\*", r"\1", s)


def extract_links(s: str) -> Tuple[str, List[SourceLink]]:
    """Extract all markdown links from text, return (cleaned_text, links)."""
    links: List[SourceLink] = []
    def sub(m):
        links.append(SourceLink(label=m.group(1), url=m.group(2)))
        return ""
    text = INLINE_LINK.sub(sub, s)
    return text, links


GLYPH_REPLACE = {
    "⚠️": "", "⚠": "", "❌": "—", "✅": "✓",
    "📋": "", "🔴": "", "🟠": "", "🟡": "", "🟢": "",
    "—": "—", "→": "→",
}


def sanitize(text: str) -> str:
    """Clean emojis and normalize special characters."""
    for k, v in GLYPH_REPLACE.items():
        text = text.replace(k, v)
    return text


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> Tuple[dict, str]:
    """Parse YAML frontmatter. Returns (metadata_dict, body_text)."""
    meta = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            fm = text[4:end]
            body = text[end + 4:].lstrip("\n")
            for line in fm.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, body
    return meta, text


# ---------------------------------------------------------------------------
# Bullet parsing
# ---------------------------------------------------------------------------

def parse_bullet(raw: str) -> Tuple[str, str]:
    """Parse a bullet line into (label, value). Handles **label：** value format."""
    raw = raw.strip()
    if raw.startswith("- "):
        raw = raw[2:]
    m = re.match(r"\*\*(.+?)[:：]\*\*\s*(.*)$", raw)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    m = re.match(r"(.+?)[:：]\s*(.*)$", raw)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", raw


# ---------------------------------------------------------------------------
# Warning Card parsing
# ---------------------------------------------------------------------------

def parse_markdown(md: str) -> Card:
    """Parse a Warning Card markdown file into a Card dataclass."""
    md = md.replace("\r\n", "\n")
    meta, body = parse_frontmatter(md)

    card = Card()
    card.customer = meta.get("customer", "")
    card.industry = meta.get("industry", "")
    card.date = meta.get("date", "")
    card.owner = meta.get("owner", "")

    lines = body.split("\n")
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("> "):
            card.note = s[2:].strip()
        if s.startswith("## 预警卡"):
            i += 1
            break
        i += 1

    current = None
    buf: List[str] = []

    def flush(section, buf):
        if section == 1:
            _parse_signals(buf, card)
        elif section == 2:
            _parse_impact(buf, card)
        elif section == 3:
            _parse_opportunity(buf, card)
        elif section == 4:
            _parse_urgency(buf, card)
        elif section == 5:
            _parse_psychology(buf, card)
        elif section == 6:
            _parse_action(buf, card)

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()

        if s.startswith("### "):
            if current is not None:
                flush(current, buf)
                buf = []
            title = s[4:].strip()
            m = re.match(r"^(\d+)\.\s*(.*)", title)
            if m:
                current = int(m.group(1))
            else:
                current = 99 if "内部数据清单" in title else 0
            i += 1
            continue

        if s.startswith("---") or s.startswith("***"):
            i += 1
            continue

        if current == 99:
            if s and not s.startswith("#"):
                card.internal_data += (" " if card.internal_data else "") + s
        elif current is not None:
            buf.append(raw)
        i += 1

    if current is not None:
        flush(current, buf)

    return card


def _parse_signals(buf: List[str], card: Card):
    """Parse Layer 1: Signal layer."""
    text = "\n".join(buf).strip()
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith("观察清单"):
            line = block.replace("\n", " ")
            cleaned, links = extract_links(line)
            card.observation = cleaned.strip(" —·：:")
            card.observation_links = links
            continue
        block_lines = [ln.rstrip() for ln in block.split("\n") if ln.strip()]
        if not block_lines:
            continue
        heading = block_lines[0].strip()
        m = re.match(r"\*\*排名\s*#\s*(\d+)\s*·\s*(.+?)\*\*", heading)
        if not m:
            continue
        rank = int(m.group(1))
        dim = m.group(2).strip()
        parts, sources = [], []
        reasoning = ""
        for ln in block_lines[1:]:
            ln_stripped = ln.strip()
            if ln_stripped.startswith("源：") or ln_stripped.startswith("源:"):
                _, links = extract_links(ln_stripped)
                sources.extend(links)
            elif ln_stripped.startswith("推理：") or ln_stripped.startswith("推理:"):
                reasoning = ln_stripped.split("：", 1)[-1].split(":", 1)[-1].strip()
                if not reasoning and "：" in ln_stripped:
                    reasoning = ln_stripped.split("：", 1)[-1].strip()
            else:
                parts.append(ln_stripped)
        text_all = " ".join(p.strip() for p in parts).strip()
        card.signals.append(Signal(
            rank=rank, dimension=dim, text=text_all,
            reasoning=reasoning, sources=sources
        ))
    card.signals.sort(key=lambda s: s.rank)


def _parse_impact(buf: List[str], card: Card):
    """Parse Layer 2: Impact layer."""
    for ln in buf:
        s = ln.strip()
        if not s.startswith("- "):
            continue
        label, body = parse_bullet(s)
        body = strip_code(strip_bold(body))
        if "谁" in label:
            card.impact_who = body
        elif "影响" in label and "时间" not in label:
            card.impact_detail = body
        elif "时间线" in label or "时间" in label:
            card.impact_timeline = body
        elif "推理" in label:
            card.impact_reasoning = body


def _parse_urgency(buf: List[str], card: Card):
    """Parse Layer 4: Urgency layer."""
    for ln in buf:
        s = ln.strip()
        if not s.startswith("- "):
            continue
        label, body = parse_bullet(s)
        body = strip_code(strip_bold(body))
        if "窗口" in label:
            card.urgency_window = body
        elif "竞对" in label:
            card.urgency_competitor = body
        elif "衰减" in label:
            card.urgency_decay = body
        elif "不行动" in label or "CoI" in label.upper() or "成本" in label:
            card.urgency_coi = body
            # Extract Y1 ($X–YM) and 3Y ($X–YM) as separate figures
            dollar_matches = re.findall(r"\$[\d,.\-–]+\s*[MBK]\b", body)
            if len(dollar_matches) >= 2:
                card.coi_headline = dollar_matches[0]
                card.coi_y3 = dollar_matches[1]
            elif len(dollar_matches) == 1:
                card.coi_headline = dollar_matches[0]
                card.coi_y3 = ""
            else:
                card.coi_headline = "—"
                card.coi_y3 = ""
            # Extract the consequence detail
            clean_body = re.sub(r"\[估算\]", "", body).strip()
            m3 = re.search(r"→\s*([^，。\n]+)", clean_body)
            if m3:
                card.coi_detail = m3.group(1).strip(" ·。")
            else:
                card.coi_detail = clean_body[:80].strip(" ·。")
        elif "时间线推演" in label or "推演" in label:
            # Parse simulation: 本周动 → X · 1–3 月内 → Y · 过 QN → Z
            parts = re.split(r"\s*·\s*", body)
            for p in parts:
                if "本周" in p:
                    card.urgency_sim_good = re.sub(r"^.*?→\s*", "", p).strip()
                elif "月内" in p or "1–3" in p:
                    card.urgency_sim_warn = re.sub(r"^.*?→\s*", "", p).strip()
                elif "过" in p:
                    card.urgency_sim_bad = re.sub(r"^.*?→\s*", "", p).strip()
        elif "推理" in label:
            card.urgency_reasoning = body


def _parse_psychology(buf: List[str], card: Card):
    """Parse Layer 5: Psychology layer."""
    for ln in buf:
        s = ln.strip()
        if not s.startswith("- "):
            continue
        label, body = parse_bullet(s)
        body = strip_code(strip_bold(body))
        if "状态" in label:
            card.psychology_state = body
        elif "motion" in label.lower() or "接触" in label or "推荐" in label:
            card.psychology_motion = body
        elif "避" in label and "坑" in label:
            card.psychology_pits = body
        elif "话术" in label or "钩子" in label:
            card.psychology_hook = body.strip('"').strip('"').strip('"')
        elif "推理" in label:
            card.psychology_reasoning = body


def _parse_opportunity(buf: List[str], card: Card):
    """Parse Layer 3: Opportunity layer."""
    lines = [ln.rstrip() for ln in buf]
    rows, table_start = [], None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("|") and ("AWS" in ln or "能力" in ln):
            table_start = i
            break
    if table_start is not None:
        # Skip header + separator
        j = table_start + 2
        while j < len(lines):
            s = lines[j].strip()
            if not (s.startswith("|") and s.endswith("|")):
                break
            cells = [c.strip().strip("*") for c in s.strip("|").split("|")]
            if len(cells) >= 3:
                rows.append(OpportunityRow(cells[0], cells[1], cells[2]))
            j += 1
        # Parse remaining lines for advantage, reasoning, caption
        rest_lines = [ln.strip() for ln in lines[j:] if ln.strip()]
        for rl in rest_lines:
            if rl.startswith("独特优势") or rl.startswith("**独特优势"):
                # Strip the prefix
                adv = re.sub(r"^\*?\*?独特优势[^：:]*[：:]\*?\*?\s*", "", rl)
                card.opportunity_advantage = strip_bold(strip_code(adv))
            elif rl.startswith("推理") or rl.startswith("**推理"):
                reason = re.sub(r"^\*?\*?推理[^：:]*[：:]\*?\*?\s*", "", rl)
                card.opportunity_reasoning = strip_bold(strip_code(reason))
            else:
                card.opportunity_caption = strip_code(rl)
    card.opportunity_rows = rows


def _parse_action(buf: List[str], card: Card):
    """Parse Layer 6: Action layer."""
    for ln in buf:
        s = ln.strip()
        if not s.startswith("- "):
            continue
        label, body = parse_bullet(s)
        body = strip_code(strip_bold(body))
        if "本周第一步" in label or "第一步" in label:
            card.action_first_step = body
        elif "开场" in label:
            body = body.strip('"').strip('"').strip('"')
            card.action_opening = body
        elif "核心" in label:
            card.action_core = body
        elif "升级" in label:
            card.action_escalation = body
        elif "推理" in label:
            card.action_reasoning = body


# ---------------------------------------------------------------------------
# Reasoning appendix parsing
# ---------------------------------------------------------------------------

def parse_reasoning(md: str) -> Reasoning:
    """Parse a Reasoning appendix markdown file into a Reasoning dataclass."""
    md = md.replace("\r\n", "\n")
    meta, body = parse_frontmatter(md)

    r = Reasoning()
    r.title = meta.get("title", "")
    r.subtitle = meta.get("subtitle", "")
    r.customer = meta.get("customer", "")
    r.date = meta.get("date", "")

    lines = body.split("\n")
    current: Optional[ReasoningSection] = None
    in_table = False
    buf_para: List[str] = []

    def flush_para():
        nonlocal buf_para
        if current and buf_para:
            text = " ".join(p.strip() for p in buf_para).strip()
            text = strip_bold(text)
            text = strip_code(text)
            if text:
                current.paragraphs.append(text)
        buf_para = []

    for raw in lines:
        s = raw.rstrip()
        stripped = s.strip()

        # Section marker: ## §0N · ...
        if stripped.startswith("## "):
            flush_para()
            if current is not None:
                r.sections.append(current)
            header = stripped[3:].strip()
            m = re.match(r"(§\d+)\s*·\s*(.+?)\s*·\s*(.+)", header)
            if m:
                current = ReasoningSection(
                    marker=m.group(1).strip(),
                    title_en=m.group(2).strip(),
                    title_cn=m.group(3).strip(),
                )
            else:
                m = re.match(r"(§\d+)\s*·?\s*(.+)", header)
                if m:
                    current = ReasoningSection(
                        marker=m.group(1).strip(),
                        title_en=m.group(2).strip(),
                        title_cn="",
                    )
                else:
                    current = ReasoningSection(marker="", title_en=header, title_cn="")
            in_table = False
            continue

        if current is None:
            continue

        # Table row?
        if stripped.startswith("|"):
            if not in_table:
                flush_para()
                in_table = True
            # Skip the separator line
            if re.match(r"^\|[\s:|\\-]+\|$", stripped):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            current.table_rows.append(cells)
            continue
        else:
            if in_table:
                in_table = False

        # Bullet `- ...`
        if stripped.startswith("- "):
            flush_para()
            current.bullets.append(strip_code(strip_bold(stripped[2:].strip())))
            continue

        # Numbered `1. ...`
        m_num = re.match(r"^\d+\.\s+(.+)$", stripped)
        if m_num:
            flush_para()
            current.numbered.append(strip_code(strip_bold(m_num.group(1).strip())))
            continue

        # Blank line separates paragraphs
        if not stripped:
            flush_para()
            continue

        buf_para.append(stripped)

    flush_para()
    if current is not None:
        r.sections.append(current)

    return r
