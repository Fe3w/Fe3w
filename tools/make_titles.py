"""Section title bars for the profile README.

Each title gets two static SVGs: a black bar with white text (shown in
GitHub's light theme) and a white bar with black text (dark theme).
Run: python tools/make_titles.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

TITLES = [
    ("01", "GPU & CPU Performance Optimization for AI Workloads"),
    ("02", "VLA & VLM Fine-Tuning for Robotics Tasks"),
    ("03", "Systolic-Array GEMM Hardware Accelerator"),
    ("04", "Local AI Voice Notes & Research Agent"),
    ("05", "LLVM Loop Vectorization Analyzer"),
    ("06", "Leadership · DD Robocon 2026 National Finals"),
    ("07", "Robotics Builds"),
    ("08", "About Me"),
    ("09", "Skills"),
    ("10", "Contact"),
]
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
THEMES = {"light": ("#0d1117", "#ffffff", "#8b949e"),  # bar, text, number
          "dark": ("#ffffff", "#0d1117", "#57606a")}

def svg(num, text, bar, fg, dim):
    t = escape(text)
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='960' height='64' viewBox='0 0 960 64' role='img'>"
            f"<title>{num} · {t}</title>"
            f"<rect width='960' height='64' rx='8' fill='{bar}'/>"
            f"<text x='28' y='41' font-family=\"{MONO}\" font-size='20' font-weight='700' fill='{dim}'>{num}</text>"
            f"<text x='76' y='42' font-family=\"{FONT}\" font-size='26' font-weight='700' fill='{fg}'>{t}</text>"
            f"</svg>\n")

out = Path(__file__).resolve().parent.parent / "assets" / "titles"
out.mkdir(parents=True, exist_ok=True)
for num, text in TITLES:
    for theme, colors in THEMES.items():
        (out / f"{num}-{theme}.svg").write_text(svg(num, text, *colors))
