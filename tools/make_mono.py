"""Black-and-white profile graphics (square corners, framed groups, Inter + DejaVu Sans Mono).
Builds:
  assets/hero.gif        banner, with the animated hourglass (art by @Ki11_5trike) in its frame
  assets/terminal.png    whoami / now / bench panel
  assets/stack.png       the stack, top to bottom
Run:  python tools/make_mono.py      (needs playwright, pillow)
"""
import os
from PIL import Image, ImageSequence
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
ART = os.path.join(HERE, "hero-hourglass.gif")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;color:#111;font-family:Inter,sans-serif;width:1600px}
.mono{font-family:'DejaVu Sans Mono',monospace}
.page{padding:40px}
.frame{position:relative;border:4px solid #111;background:#fff}
.tab{position:absolute;top:-17px;left:28px;background:#fff;padding:0 14px;font:700 24px 'DejaVu Sans Mono';letter-spacing:.12em;white-space:nowrap}
.kicker{font:600 24px 'DejaVu Sans Mono';letter-spacing:.08em;color:#444}
.take{font:800 34px Inter;margin-top:34px;padding-top:28px;border-top:4px solid #111}
.seq{display:flex;align-items:center;gap:16px}
.chev{font:700 38px Inter}
"""


def page(body, extra=""):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}{extra}</style></head><body><div class=page>{body}</div></body></html>"


HERO_CSS = """
.hero{display:grid;grid-template-columns:1fr 292px;column-gap:72px;padding:64px 72px 60px;margin-top:18px}
h1{font:800 104px/1.02 Inter;letter-spacing:-.02em;margin-top:22px}
.sub{font:34px Inter;color:#333;margin-top:22px}
.hero .seq{margin-top:40px}
.step{border:3px solid #111;padding:12px 18px;font:24px 'DejaVu Sans Mono'}
.step.last{background:#111;color:#fff}
#art{width:292px;height:440px;border:4px solid #111;position:relative;background:#ddd}
.credit{font:18px 'DejaVu Sans Mono';color:#555;margin-top:10px;text-align:right}
"""


def hero_html():
    steps = ' <span class=chev>›</span> '.join(
        f'<span class="step{" last" if i == 3 else ""}">{s}</span>'
        for i, s in enumerate(["autonomous systems", "CUDA kernels", "LLVM IR", "silicon"]))
    return page(f"""
<div class="frame hero"><div class=tab>~/fe3w · README.md</div>
<div><div class=kicker>COMPILERS · CPU/GPU PERFORMANCE · AUTONOMOUS SYSTEMS</div>
<h1>Abhishek<br>Singh</h1>
<div class=sub>Working down the stack, from robots to silicon.</div>
<div class=seq>{steps}</div></div>
<div><div id=art></div><div class=credit>art · @Ki11_5trike</div></div>
</div>""", HERO_CSS)


TERM_CSS = """
.term{padding:56px 48px 40px;margin-top:18px;font:26px/1.55 'DejaVu Sans Mono'}
.p{font-weight:700}
.o{color:#333;padding-left:38px}
.gap{height:22px}
.item{display:grid;grid-template-columns:1fr auto;padding-left:38px;color:#333}
.tag{border:2px solid #111;padding:0 12px;font-size:20px;align-self:center;background:repeating-linear-gradient(135deg,#fff 0 6px,#ccc 6px 8px)}
b{color:#111}
.cur{display:inline-block;width:16px;height:30px;background:#111;vertical-align:-5px}
"""


def terminal_html():
    items = ["llvm loop-optimization advisor · new-PM analysis pass",
             "mini C-like compiler → LLVM IR → native executable",
             "neuro-symbolic VLM sorting · Isaac Sim + Dobot Magician"]
    rows = "".join(f'<div class=item><span>· {i}</span><span class=tag>in progress</span></div>' for i in items)
    return page(f"""
<div class="frame term"><div class=tab>TERMINAL · abhishek@fe3w</div>
<div class=p>$ whoami</div>
<div class=o>abhishek singh — from autonomous systems down to compilers &amp; silicon</div>
<div class=gap></div><div class=p>$ cat now.txt</div>{rows}
<div class=gap></div><div class=p>$ ./bench gemm --best</div>
<div class=o>cpu 0.707 → <b>86.03 GFLOP/s (121.6×)</b> · gpu tf32 <b>2,679 GFLOP/s (3.7×)</b> · max rel err 0.0686%</div>
<div class=gap></div><div class=p>$ <span class=cur></span></div>
</div>""", TERM_CSS)


STACK_CSS = """
.head{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:28px;border-bottom:4px solid #111}
h1{font:800 54px Inter;margin-top:10px}
.legend{display:flex;flex-direction:column;gap:12px;font:22px 'DejaVu Sans Mono'}
.legend span{display:flex;align-items:center;gap:14px}
.sw{width:30px;height:30px;border:2px solid #111;display:inline-block}
.stk{padding:60px 36px 40px;margin-top:56px}
.card{width:312px;height:190px;border:3px solid #111;padding:20px 22px;display:flex;flex-direction:column}
.card .n{font:22px 'DejaVu Sans Mono';color:#555}
.card .t{font:800 40px Inter;margin-top:14px}
.card .d{font:21px 'DejaVu Sans Mono';margin-top:auto}
.card.hw{background:#111;color:#fff}.card.hw .n{color:#bbb}
.axis{display:flex;justify-content:space-between;font:22px 'DejaVu Sans Mono';color:#555;margin-top:26px}
"""


def stack_html():
    cards = [("01", "Autonomy", "VLMs · ROS 2", ""),
             ("02", "Kernels", "CUDA · OpenMP", ""),
             ("03", "Compilers", "LLVM IR · passes", ""),
             ("04", "Silicon", "SMs · Tensor Cores", "hw")]
    seq = ' <span class=chev>›</span> '.join(
        f'<div class="card {c}"><div class=n>{n}</div><div class=t>{t}</div><div class=d>{d}</div></div>' for n, t, d, c in cards)
    return page(f"""
<div class=head><div><div class=kicker>THE STACK</div><h1>Where I work, top to bottom</h1></div>
<div class=legend><span><i class=sw></i>software</span><span><i class=sw style="background:#111"></i>hardware</span></div></div>
<div class="frame stk"><div class=tab>HIGHER LEVEL › CLOSER TO THE METAL</div><div class=seq>{seq}</div>
<div class=axis><span>what runs</span><span>how fast it runs</span></div></div>
<div class=take>Higher levels decide what runs; lower levels decide how fast it runs.</div>""", STACK_CSS)


def shoot(html, png, want_art=False):
    tmp = png + ".html"
    open(tmp, "w").write(html)
    box = None
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1600, "height": 10})
        pg.goto("file://" + os.path.abspath(tmp))
        pg.wait_for_timeout(300)
        if want_art:
            r = pg.eval_on_selector("#art", "e=>{const r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]}")
            box = [round(v) for v in r]
        pg.screenshot(path=png, full_page=True)
        b.close()
    os.remove(tmp)
    return box


def hero():
    base_png = os.path.join(ASSETS, "_hero_base.png")
    x, y, w, h = shoot(hero_html(), base_png, want_art=True)
    base = Image.open(base_png).convert("RGB")
    os.remove(base_png)
    k = 1200 / base.width                                 # GitHub shows ~880px; 1200 keeps it sharp and small
    base = base.resize((1200, round(base.height * k)), Image.LANCZOS)
    ix, iy, iw, ih = [round(v * k) for v in (x + 4, y + 4, w - 8, h - 8)]  # inside the 4px border
    art = Image.open(ART)
    frames, durs = [], []
    for fr in ImageSequence.Iterator(art):
        f = fr.convert("RGB").resize((iw, ih), Image.LANCZOS)
        img = base.copy()
        img.paste(f, (ix, iy))
        frames.append(img)
        durs.append(fr.info.get("duration", art.info.get("duration", 40)))
    crops = [f.crop((ix, iy, ix + iw, iy + ih)) for f in (frames[0], frames[len(frames) // 3], frames[2 * len(frames) // 3])]
    sample = Image.new("RGB", (iw * 3, ih))
    for k, c in enumerate(crops):
        sample.paste(c, (iw * k, 0))
    art_pal = sample.quantize(colors=192, method=Image.MEDIANCUT).getpalette()[:192 * 3]
    greys = [v for g in range(0, 256, 4) for v in (g, g, g)][:63 * 3] + [255, 255, 255]
    pal = Image.new("P", (1, 1))
    pal.putpalette(greys + art_pal)
    q = []
    for f in frames:
        flat = f.quantize(palette=pal, dither=Image.Dither.NONE)
        flat.paste(f.quantize(palette=pal, dither=Image.Dither.FLOYDSTEINBERG).crop((ix, iy, ix + iw, iy + ih)), (ix, iy))
        q.append(flat)
    out = os.path.join(ASSETS, "hero.gif")
    q[0].save(out, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)
    print(out, os.path.getsize(out) // 1024, "KB")


if __name__ == "__main__":
    hero()
    shoot(terminal_html(), os.path.join(ASSETS, "terminal.png")); print("terminal.png")
    shoot(stack_html(), os.path.join(ASSETS, "stack.png")); print("stack.png")
