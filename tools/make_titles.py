"""Section title bars for the profile README.

Each title gets two static SVGs: a black bar with white text (shown in
GitHub's light theme) and a white bar with black text (dark theme).
Run: python tools/make_titles.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

TITLES = [
    ("01", "GPU & CPU Performance Optimization for AI Workloads"),
    ("02", "Vision-Language-Action Pipeline & Vision-Language Model Fine-Tuning for Robotics"),
    ("03", "Systolic-Array GEMM Hardware Accelerator"),
    ("04", "AI Research Agent & Voice-Activated Notes, Running on Local LLMs"),
    ("05", "LLVM 20 Loop Vectorization Analyzer"),
    ("06", "Design Lead & Team Co-Head · DD Robocon 2026 National Finals"),
    ("07", "Robotics Builds: Computer Vision, ROS 2 & CAD"),
    ("08", "About Me"),
    ("09", "Skills"),
    ("10", "Contact"),
]
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
THEMES = {"light": ("#0d1117", "#ffffff", "#8b949e"),  # bar, text, number
          "dark": ("#ffffff", "#0d1117", "#57606a")}

MAX_CHARS = 64  # longer titles wrap onto a second line


def wrap(text):
    if len(text) <= MAX_CHARS:
        return [text]
    words = text.split(" ")
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) <= MAX_CHARS and len(b) <= MAX_CHARS:
            score = abs(len(a) - len(b))
            if best is None or score < best[0]:
                best = (score, [a, b])
    return best[1]


def svg(num, text, bar, fg, dim):
    lines = [escape(l) for l in wrap(text)]
    size = min(26, int(860 / (0.56 * max(len(l) for l in wrap(text)))))
    h = 64 + 36 * (len(lines) - 1)
    body = "".join(
        f"<text x='76' y='{42 + 36 * i}' font-family=\"{FONT}\" font-size='{size}' font-weight='700' fill='{fg}'>{l}</text>"
        for i, l in enumerate(lines))
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='960' height='{h}' viewBox='0 0 960 {h}' role='img'>"
            f"<title>{num} · {escape(text)}</title>"
            f"<rect width='960' height='{h}' rx='8' fill='{bar}'/>"
            f"<text x='28' y='41' font-family=\"{MONO}\" font-size='20' font-weight='700' fill='{dim}'>{num}</text>"
            f"{body}</svg>\n")


out = Path(__file__).resolve().parent.parent / "assets" / "titles"
out.mkdir(parents=True, exist_ok=True)
for num, text in TITLES:
    for theme, colors in THEMES.items():
        (out / f"{num}-{theme}.svg").write_text(svg(num, text, *colors))
