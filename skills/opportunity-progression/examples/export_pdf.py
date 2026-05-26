#!/usr/bin/env python3
"""
Export a rendered report HTML file to PDF, preserving the Material Design 3
styling (Tailwind CDN + Google Fonts + Material Symbols).

Why headless Chrome, not WeasyPrint:
    Tailwind CSS via CDN uses a JIT engine that REQUIRES JavaScript execution
    in a real browser to compile class names into CSS. WeasyPrint (a pure
    Python renderer) cannot run JS, so it produces an unstyled document. A
    headless Chromium engine is the correct choice for fidelity.

Priority order:
    1. Playwright (pip install playwright && playwright install chromium)
       — cleanest API, isolated Chromium install.
    2. System Chrome / Chromium via subprocess — zero extra install on
       machines that already have Chrome.

Usage:
    python3 examples/export_pdf.py examples/sample-report.html
    # → writes examples/sample-report.pdf next to the source file

Optional:
    python3 examples/export_pdf.py path/to/report.html path/to/out.pdf
"""
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional


def _export_via_playwright(src: Path, out: Path) -> bool:
    """Try Playwright first. Returns True on success, False if unavailable."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            # domcontentloaded + explicit font/network waits — CDN Tailwind and
            # Google Fonts need time to finish before we capture a print layout.
            page.goto(src.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(500)  # extra buffer for Material Symbols glyphs

            page.pdf(
                path=str(out),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"},
            )
            browser.close()
        return True
    except Exception as e:
        print(f"⚠️  Playwright attempt failed: {e}", file=sys.stderr)
        return False


def _find_chrome() -> Optional[str]:
    """Locate a Chrome/Chromium binary on common macOS and Linux paths."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    return next((c for c in candidates if c and Path(c).exists()), None)


def _export_via_system_chrome(src: Path, out: Path) -> bool:
    """Fall back to system Chrome via `--print-to-pdf`."""
    chrome = _find_chrome()
    if not chrome:
        return False

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--virtual-time-budget=8000",  # allow CDN assets to finish
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={out}",
        src.as_uri(),
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=60)
        return out.exists()
    except Exception as e:
        print(f"⚠️  System Chrome attempt failed: {e}", file=sys.stderr)
        return False


def export(src: Path, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)

    if _export_via_playwright(src, out):
        return out
    print("→ Playwright unavailable, trying system Chrome...", file=sys.stderr)

    if _export_via_system_chrome(src, out):
        return out

    raise RuntimeError(
        "No PDF engine available. Install one of:\n"
        "  pip install playwright && playwright install chromium\n"
        "  — or —\n"
        "  install Google Chrome / Chromium so this script can invoke it."
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 examples/export_pdf.py <input.html> [output.pdf]")
        sys.exit(2)

    src = Path(sys.argv[1]).resolve()
    if not src.exists():
        print(f"❌ Source HTML not found: {src}")
        sys.exit(1)

    out = Path(sys.argv[2]).resolve() if len(sys.argv) >= 3 else src.with_suffix(".pdf")

    result = export(src, out)
    print(f"✅ PDF exported: {result}")
