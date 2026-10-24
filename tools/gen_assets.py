"""Generates every SVG in assets/ (dark) and assets/light/ (light).

Run from the repo root:  python tools/gen_assets.py
Edit the numbers / text below and re-run to update the README graphics.
Animations use CSS + SMIL only (GitHub strips JavaScript), and every animated
element has a sensible static value so it still looks right if animation is off.
"""
import math
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

THEMES = {
    "dark": dict(bg="#0b0f14", panel="#111820", line="#243041", text="#e6edf3",
                 muted="#8b949e", green="#7ee787", orange="#ffa657", blue="#79c0ff",
                 faint="#18212c"),
    "light": dict(bg="#f6f8fa", panel="#ffffff", line="#d0d7de", text="#1f2328",
                  muted="#59636e", green="#1a7f37", orange="#bc4c00", blue="#0969da",
                  faint="#e6eaef"),
}
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">'
            f'<title>{esc(title)}</title>{body}</svg>\n')


def delayed(attr, final, start, dur, total=None, extra=""):
    """SMIL animation that holds 0 until `start`, then animates to `final` over `dur`.
    The element's static attribute keeps `final`, so non-animating renderers show the end state."""
    total = start + dur
    k = start / total
    return (f'<animate attributeName="{attr}" values="0;0;{final}" keyTimes="0;{k:.3f};1" '
            f'dur="{total:.2f}s" fill="freeze"{extra}/>')


# ───────────────────────────── HERO ─────────────────────────────
def hero(t):
    W, H = 1200, 360
    css = f"""<style>
.lane{{fill:{t['green']};fill-opacity:.14;animation:lane 2.8s ease-in-out infinite}}
.wl{{fill:{t['muted']};animation:wl 2.8s ease-in-out infinite}}
@keyframes lane{{0%,100%{{fill-opacity:.14}}10%{{fill-opacity:.95}}32%{{fill-opacity:.14}}}}
@keyframes wl{{0%,100%{{fill:{t['muted']}}}10%{{fill:{t['green']}}}32%{{fill:{t['muted']}}}}}
.cur{{animation:blink 1.1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
</style>"""
    body = [css,
            '<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
            f'<circle cx="2" cy="2" r="1.1" fill="{t["line"]}"/></pattern>'
            f'<radialGradient id="glow" cx="80%" cy="45%" r="45%"><stop offset="0" stop-color="{t["green"]}" stop-opacity=".10"/>'
            f'<stop offset="1" stop-color="{t["green"]}" stop-opacity="0"/></radialGradient></defs>',
            f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>',
            f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#dots)" opacity=".7"/>',
            f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#glow)"/>']
    # left text
    body += [
        f'<text x="56" y="84" font-family="{MONO}" font-size="13" fill="{t["green"]}">~/fe3w $ cat README.md</text>',
        f'<text x="54" y="158" font-family="{SANS}" font-size="64" font-weight="800" fill="{t["text"]}">Abhishek</text>',
        f'<text x="54" y="226" font-family="{SANS}" font-size="64" font-weight="800" fill="{t["text"]}">Prakash Singh<tspan fill="{t["green"]}">.</tspan></text>',
        f'<text x="56" y="272" font-family="{SANS}" font-size="19" fill="{t["muted"]}">Compilers · CPU/GPU performance · Systems software · Physical AI</text>',
        f'<text x="56" y="312" font-family="{MONO}" font-size="13.5" fill="{t["muted"]}">robot arms <tspan fill="{t["green"]}">→</tspan> CUDA kernels '
        f'<tspan fill="{t["green"]}">→</tspan> LLVM IR <tspan fill="{t["green"]}">→</tspan> silicon</text>',
        f'<rect class="cur" x="452" y="300" width="9" height="16" fill="{t["green"]}"/>',
    ]
    # SM / warp scheduler panel
    px, py, pw, ph = 772, 64, 396, 236
    body.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>')
    body.append(f'<text x="{px+18}" y="{py+28}" font-family="{MONO}" font-size="12" fill="{t["muted"]}">SM 00 · warp scheduler</text>')
    body.append(f'<text x="{px+pw-18}" y="{py+28}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t["orange"]}">SIMT</text>')
    size, gap = 16, 5
    cx0, cy0 = px + 42, py + 46
    for r in range(4):
        y = cy0 + r * 30
        d = r * 0.7
        body.append(f'<text class="wl" x="{px+16}" y="{y+13}" font-family="{MONO}" font-size="11" style="animation-delay:{d:.2f}s">w{r}</text>')
        for c in range(16):
            x = cx0 + c * (size + gap)
            body.append(f'<rect class="lane" x="{x}" y="{y}" width="{size}" height="{size}" rx="3" style="animation-delay:{d + c*0.035:.3f}s"/>')
    # memory hierarchy with packets flowing DRAM -> REG
    my = py + 200
    labels = [("REG", px + 40), ("SMEM/L1", px + 140), ("L2", px + 250), ("DRAM", px + 350)]
    body.append(f'<line x1="{px+40}" y1="{my}" x2="{px+350}" y2="{my}" stroke="{t["line"]}" stroke-width="2"/>')
    for name, x in labels:
        body.append(f'<circle cx="{x}" cy="{my}" r="4" fill="{t["panel"]}" stroke="{t["muted"]}"/>')
        body.append(f'<text x="{x}" y="{my+22}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">{name}</text>')
    for i in range(3):
        body.append(f'<circle r="3.5" fill="{t["orange"]}"><animateMotion path="M{px+350} {my} H{px+40}" dur="3s" begin="{i}s" repeatCount="indefinite"/></circle>')
    return svg(W, H, "".join(body), "Abhishek Prakash Singh — compilers, CPU/GPU performance, systems software, physical AI")


# ───────────────────────────── TERMINAL ─────────────────────────────
def terminal():
    W, H = 1200, 352
    bg, bar, txt, mut, grn, org = "#0d1117", "#161b22", "#e6edf3", "#8b949e", "#7ee787", "#ffa657"
    cw = 9.05  # approx char width at 15px mono
    body = [f'<style>.cur{{animation:blink 1.1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}</style>',
            f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{bg}" stroke="#30363d"/>',
            f'<path d="M1 15 a14 14 0 0 1 14 -14 H{W-15} a14 14 0 0 1 14 14 V40 H1 Z" fill="{bar}"/>',
            '<circle cx="26" cy="21" r="6" fill="#ff5f57"/><circle cx="46" cy="21" r="6" fill="#febc2e"/><circle cx="66" cy="21" r="6" fill="#28c840"/>',
            f'<text x="{W/2}" y="26" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{mut}">abhishek@fe3w: ~</text>']
    defs = []

    def cmd(i, y, text, start, dur):
        w = len(text) * cw + 12
        defs.append(f'<clipPath id="c{i}"><rect x="48" y="{y-16}" height="22" width="{w:.0f}">{delayed("width", f"{w:.0f}", start, dur)}</rect></clipPath>')
        body.append(f'<g opacity="1">{delayed("opacity", 1, start - 0.05, 0.05)}'
                    f'<text x="28" y="{y}" font-family="{MONO}" font-size="15" fill="{grn}">$</text>'
                    f'<text x="50" y="{y}" font-family="{MONO}" font-size="15" fill="{txt}" clip-path="url(#c{i})">{esc(text)}</text></g>')

    def out(y, inner, start):
        body.append(f'<g opacity="1">{delayed("opacity", 1, start, 0.35)}'
                    f'<text x="50" y="{y}" font-family="{MONO}" font-size="14" fill="{mut}">{inner}</text></g>')

    cmd(1, 78, "whoami", 0.4, 0.6)
    out(104, f'abhishek prakash singh <tspan fill="{grn}">—</tspan> robotics engineer, working down the stack toward compilers &amp; silicon', 1.2)
    cmd(2, 142, "cat now.txt", 2.0, 0.7)
    items = ["llvm loop-optimization advisor · new-PM analysis pass",
             "mini C-like compiler → LLVM IR → native executable",
             "neuro-symbolic VLM sorting · Isaac Sim + Dobot Magician"]
    for k, it in enumerate(items):
        out(168 + 26 * k, f'<tspan fill="{org}">•</tspan> {esc(it)}<tspan x="720" fill="{org}">[in progress]</tspan>', 2.9 + 0.2 * k)
    cmd(3, 258, "./bench gemm --best", 4.0, 0.9)
    out(284, f'cpu 0.707 → <tspan fill="{grn}">86.03 GFLOP/s (121.6×)</tspan>   gpu tf32 <tspan fill="{grn}">2,679 GFLOP/s (3.7×)</tspan>   max rel err 0.0686%', 5.1)
    body.append(f'<g opacity="1">{delayed("opacity", 1, 5.6, 0.05)}'
                f'<text x="28" y="322" font-family="{MONO}" font-size="15" fill="{grn}">$</text>'
                f'<rect class="cur" x="50" y="308" width="9" height="18" fill="{grn}"/></g>')
    return svg(W, H, "<defs>" + "".join(defs) + "</defs>" + "".join(body), "Terminal: whoami, current projects, benchmark results")


# ───────────────────────────── STACK ─────────────────────────────
def stack(t):
    W, H = 1200, 282
    cards = [("01", "Physical AI", "VLMs · ROS 2 · Isaac Sim", "robots that see and act", t["blue"]),
             ("02", "Kernels", "CUDA · OpenMP · AVX2/FMA", "make the math fast", t["orange"]),
             ("03", "Compilers", "LLVM IR · passes · codegen", "make the code fast", t["green"]),
             ("04", "Silicon", "SMs · caches · Tensor Cores", "know why it's fast", t["text"])]
    body = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>',
            f'<text x="40" y="40" font-family="{MONO}" font-size="13" fill="{t["muted"]}">THE STACK <tspan fill="{t["green"]}">//</tspan> where I work, top to bottom</text>']
    cy = 232
    body.append(f'<line x1="165" y1="{cy}" x2="1035" y2="{cy}" stroke="{t["line"]}" stroke-width="2" stroke-dasharray="4 6"/>')
    for i, (n, title, tools, tag, col) in enumerate(cards):
        x, y = 40 + i * 290, 60
        body += [f'<rect x="{x}" y="{y}" width="250" height="142" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>',
                 f'<rect x="{x+20}" y="{y}" width="50" height="3" rx="1.5" fill="{col}"/>',
                 f'<text x="{x+20}" y="{y+32}" font-family="{MONO}" font-size="12" fill="{t["muted"]}">{n}</text>',
                 f'<text x="{x+20}" y="{y+64}" font-family="{SANS}" font-size="22" font-weight="700" fill="{t["text"]}">{title}</text>',
                 f'<text x="{x+20}" y="{y+94}" font-family="{MONO}" font-size="12.5" fill="{col}">{esc(tools)}</text>',
                 f'<text x="{x+20}" y="{y+120}" font-family="{SANS}" font-size="14" fill="{t["muted"]}">{esc(tag)}</text>',
                 f'<line x1="{x+125}" y1="{y+142}" x2="{x+125}" y2="{cy}" stroke="{t["line"]}" stroke-width="2"/>',
                 f'<circle cx="{x+125}" cy="{cy}" r="5" fill="{t["bg"]}" stroke="{col}" stroke-width="2"/>']
    for k in range(3):
        body.append(f'<circle r="4" fill="{t["green"]}"><animateMotion path="M165 {cy} H1035" dur="4.5s" begin="{k*1.5}s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.08;.92;1" dur="4.5s" begin="{k*1.5}s" repeatCount="indefinite"/></circle>')
    body.append(f'<text x="40" y="{cy+30}" font-family="{MONO}" font-size="11" fill="{t["muted"]}">higher level</text>')
    body.append(f'<text x="{W-40}" y="{cy+30}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{t["muted"]}">closer to the metal →</text>')
    return svg(W, H, "".join(body), "The stack: physical AI, kernels, compilers, silicon")


# ───────────────────────────── SPEEDUP CHART ─────────────────────────────
SPEEDUPS = [  # (label, detail, speedup, device)  -- edit when new results land
    ("CPU · GEMM", "0.707 → 86.03 GFLOP/s", 121.6, "cpu"),
    ("CPU · Dot product", "baseline → optimized · see report", 13.3, "cpu"),
    ("CPU · Vector add", "baseline → optimized · see report", 12.7, "cpu"),
    ("GPU · GEMM (TF32)", "WMMA Tensor Cores · 2,679 GFLOP/s", 3.7, "gpu"),
]


def speedup(t):
    W = 1200
    x0, span, vmax = 380, 700, 150.0
    top, pitch = 100, 62
    H = top + pitch * len(SPEEDUPS) + 52
    body = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>',
            f'<text x="40" y="44" font-family="{MONO}" font-size="13" fill="{t["muted"]}">SPEEDUP OVER OWN BASELINE <tspan fill="{t["green"]}">//</tspan> log scale</text>',
            f'<rect x="{W-420}" y="33" width="12" height="12" rx="3" fill="{t["orange"]}"/>',
            f'<text x="{W-402}" y="44" font-family="{MONO}" font-size="12" fill="{t["muted"]}">CPU · i7-13650HX</text>',
            f'<rect x="{W-250}" y="33" width="12" height="12" rx="3" fill="{t["green"]}"/>',
            f'<text x="{W-232}" y="44" font-family="{MONO}" font-size="12" fill="{t["muted"]}">GPU · RTX 4060 Laptop</text>']
    for tick in (1, 10, 100):
        x = x0 + span * math.log10(tick) / math.log10(vmax)
        body.append(f'<line x1="{x:.1f}" y1="{top-14}" x2="{x:.1f}" y2="{top + pitch*len(SPEEDUPS) - 16}" stroke="{t["line"]}" stroke-dasharray="3 5"/>')
        body.append(f'<text x="{x:.1f}" y="{top-22}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["muted"]}">{tick}×</text>')
    for i, (lab, det, v, dev) in enumerate(SPEEDUPS):
        y = top + i * pitch
        col = t["orange"] if dev == "cpu" else t["green"]
        w = max(span * math.log10(v) / math.log10(vmax), 6)
        st = 0.3 + i * 0.25
        body += [f'<text x="40" y="{y+18}" font-family="{SANS}" font-size="16" font-weight="700" fill="{t["text"]}">{esc(lab)}</text>',
                 f'<text x="40" y="{y+38}" font-family="{MONO}" font-size="11.5" fill="{t["muted"]}">{esc(det)}</text>',
                 f'<rect x="{x0}" y="{y+4}" width="{span}" height="26" rx="5" fill="{t["faint"]}"/>',
                 f'<rect x="{x0}" y="{y+4}" width="{w:.1f}" height="26" rx="5" fill="{col}">{delayed("width", f"{w:.1f}", st, 1.2)}</rect>',
                 f'<text x="{x0 + w + 12:.1f}" y="{y+23}" font-family="{MONO}" font-size="16" font-weight="700" fill="{t["text"]}">{v}×'
                 f'{delayed("opacity", 1, st + 1.1, 0.4)}</text>']
    body.append(f'<text x="40" y="{H-22}" font-family="{MONO}" font-size="11" fill="{t["muted"]}">each bar compares a device against its own baseline — not CPU vs GPU · outputs validated against reference implementations</text>')
    return svg(W, H, "".join(body), "Speedup chart: CPU GEMM 121.6x, dot product 13.3x, vector add 12.7x, GPU TF32 GEMM 3.7x")


# ───────────────────────────── CAT PLACEHOLDER ─────────────────────────────
def placeholder(kind):
    W, H = 960, 540
    bg, line, mut, grn, org, txt = "#11161d", "#3a4552", "#8b949e", "#7ee787", "#ffa657", "#e6edf3"
    badge = {"video": "VIDEO", "image": "IMAGE", "plot": "RESULT / PLOT"}[kind]
    noun = {"video": "video", "image": "image", "plot": "result"}[kind]
    bw = len(badge) * 8.4 + (46 if kind == "video" else 28)
    icon = (f'<polygon points="38,32 38,48 51,40" fill="{org}"/>' if kind == "video" else
            f'<rect x="36" y="34" width="10" height="10" rx="2" fill="{org}"/>')
    tx = 60 if kind == "video" else 54
    blink = '<animate attributeName="ry" values="12;12;1;12" keyTimes="0;.9;.95;1" dur="4.5s" repeatCount="indefinite"/>'
    body = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22" fill="{bg}"/>',
            f'<rect x="10" y="10" width="{W-20}" height="{H-20}" rx="16" fill="none" stroke="{line}" stroke-width="2" stroke-dasharray="10 9">'
            f'<animate attributeName="stroke-dashoffset" from="0" to="-38" dur="2.4s" repeatCount="indefinite"/></rect>',
            f'<rect x="26" y="24" width="{bw:.0f}" height="32" rx="16" fill="#1c2430" stroke="{line}"/>', icon,
            f'<text x="{tx}" y="45" font-family="{MONO}" font-size="13" font-weight="700" fill="{txt}">{badge}</text>',
            f'<text x="{W-30}" y="45" text-anchor="end" font-family="{MONO}" font-size="12" fill="{mut}">placeholder.svg</text>',
            # tail (swishing)
            f'<path d="M560 318 C 620 318 640 270 615 245" fill="none" stroke="{mut}" stroke-width="7" stroke-linecap="round">'
            f'<animateTransform attributeName="transform" type="rotate" values="0 560 318;-10 560 318;0 560 318" dur="2.2s" repeatCount="indefinite"/></path>',
            # head
            f'<path d="M395 255 C 395 202 424 180 440 177 L 432 124 L 471 166 C 477 165 483 165 489 166 L 528 124 L 520 177 '
            f'C 536 180 565 202 565 255 C 565 302 526 322 480 322 C 434 322 395 302 395 255 Z" fill="#1a212b" stroke="{mut}" stroke-width="4" stroke-linejoin="round"/>',
            f'<path d="M440 140 L 446 168 M520 140 L 514 168" stroke="{org}" stroke-width="3" stroke-linecap="round" opacity=".7"/>',
            f'<ellipse cx="451" cy="248" rx="10" ry="12" fill="{grn}">{blink}</ellipse>',
            f'<ellipse cx="509" cy="248" rx="10" ry="12" fill="{grn}">{blink}</ellipse>',
            f'<path d="M474 268 L486 268 L480 276 Z" fill="{org}"/>',
            f'<path d="M480 276 Q472 290 462 283 M480 276 Q488 290 498 283" fill="none" stroke="{mut}" stroke-width="3" stroke-linecap="round"/>',
            f'<path d="M432 272 L372 262 M432 282 L370 288 M528 272 L588 262 M528 282 L590 288" stroke="{mut}" stroke-width="2.5" stroke-linecap="round"/>',
            f'<line x1="330" y1="336" x2="630" y2="336" stroke="{line}" stroke-width="4" stroke-linecap="round"/>',
            f'<ellipse cx="445" cy="330" rx="22" ry="11" fill="#1a212b" stroke="{mut}" stroke-width="4"/>',
            f'<ellipse cx="515" cy="330" rx="22" ry="11" fill="#1a212b" stroke="{mut}" stroke-width="4"/>',
            f'<text x="{W/2}" y="404" text-anchor="middle" font-family="{MONO}" font-size="26" font-weight="700" fill="{grn}">{noun.upper()} PENDING</text>',
            f'<text x="{W/2}" y="440" text-anchor="middle" font-family="{SANS}" font-size="18" fill="{mut}">this cat is holding the spot until the real {noun} arrives</text>']
    if kind == "video":
        body.append(f'<circle cx="{W-70}" cy="{H-70}" r="30" fill="#1c2430" stroke="{line}" stroke-width="2"/>'
                    f'<polygon points="{W-79},{H-86} {W-79},{H-54} {W-54},{H-70}" fill="{org}"/>')
    return svg(W, H, "".join(body), f"Placeholder: {noun} coming soon")


# ───────────────────────────── FOOTER ─────────────────────────────
def footer(t):
    W, H = 1200, 100
    d, x = ["M40 60"], 40
    while x < 1160:
        d.append(f"H{x+20} V30 H{x+40} V60")
        x += 40
    p = " ".join(d)
    body = [f'<path d="{p}" fill="none" stroke="{t["line"]}" stroke-width="2"/>',
            f'<path d="{p}" fill="none" stroke="{t["green"]}" stroke-width="2.5" stroke-dasharray="140 2900" stroke-linecap="round">'
            f'<animate attributeName="stroke-dashoffset" from="3040" to="0" dur="5s" repeatCount="indefinite"/></path>',
            f'<text x="{W/2}" y="90" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["muted"]}">// clk · end of transmission · thanks for scrolling</text>']
    return svg(W, H, "".join(body), "Animated clock signal footer")


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    for name, t in THEMES.items():
        base = ROOT if name == "dark" else os.path.join(ROOT, "light")
        write(os.path.join(base, "hero.svg"), hero(t))
        write(os.path.join(base, "stack.svg"), stack(t))
        write(os.path.join(base, "speedup.svg"), speedup(t))
        write(os.path.join(base, "footer.svg"), footer(t))
    write(os.path.join(ROOT, "terminal.svg"), terminal())
    for k in ("video", "image", "plot"):
        write(os.path.join(ROOT, f"placeholder-{k}.svg"), placeholder(k))
    print("assets written to", os.path.abspath(ROOT))
