"""Renders the GPU-project result graphics (mono style) to PNG:
  assets/media/results-speedup.png    speedup per kernel (log) + GEMM throughput steps
  assets/media/results-profiler.png   Nsight Compute SM vs DRAM utilisation
Only measured numbers from the project report / videos. Edit DATA and re-run:
  python tools/make_results_png.py      (needs playwright; fonts: Inter + DejaVu Sans Mono)
"""
import math
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "media")

SPEEDUP = [  # kernel, arithmetic intensity, CPU speedup, GPU speedup, GPU note
    ("Vector add", "0.083 FLOP/byte", 12.7, 1.0, "GPU: memory-bound, DRAM ~92% busy"),
    ("Dot product", "0.25 FLOP/byte", 13.3, 28.7, "GPU: tree reduction removes the serial chain"),
    ("GEMM", "170.7 FLOP/byte", 121.6, 3.7, "CPU: cache blocking + OpenMP + AVX2/FMA"),
]
GEMM_STEPS = {
    "CPU": [("baseline", "0.707"), ("optimised", "86.03")],
    "GPU": [("naive", "730"), ("tiled", "934"), ("Tensor Cores", "2,679")],
}
PROFILE = [  # kernel, SM %, DRAM %, verdict
    ("Vector add", 11, 92, "memory-bound"),
    ("GEMM · naive", 99, 1, "compute-bound (FP32 pipe)"),
    ("GEMM · Tensor Cores", 50, 8, "Tensor Cores busy only ~10%: starved of data"),
]

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;color:#111;font-family:Inter,sans-serif;width:1600px}
.page{padding:72px 80px 64px}
.mono{font-family:'DejaVu Sans Mono',monospace}
.kicker{font:600 22px 'DejaVu Sans Mono';letter-spacing:.08em;color:#444}
h1{font:800 54px Inter;letter-spacing:-.01em;margin-top:10px}
.head{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:28px;border-bottom:4px solid #111}
.sub{font:22px 'DejaVu Sans Mono';color:#444;margin-top:14px}
.legend{display:flex;flex-direction:column;gap:12px;font:22px 'DejaVu Sans Mono';color:#222}
.legend span{display:flex;align-items:center;gap:14px}
.sw{width:30px;height:30px;border:2px solid #111;display:inline-block}
.frame{position:relative;border:4px solid #111;padding:56px 40px 40px;margin-top:56px}
.tab{position:absolute;top:-17px;left:28px;background:#fff;padding:0 14px;font:700 24px 'DejaVu Sans Mono';letter-spacing:.12em}
.row{display:grid;grid-template-columns:400px 1fr;align-items:center;column-gap:24px;padding:26px 0;border-bottom:2px solid #ddd}
.row:last-child{border-bottom:0}
.name{font:700 34px Inter}
.ai{font:22px 'DejaVu Sans Mono';color:#555;margin-top:8px}
.bars{position:relative}
.bar{display:flex;align-items:center;height:46px;margin:8px 0}
.lab{width:72px;font:22px 'DejaVu Sans Mono';color:#333}
.track{position:relative;flex:1;height:100%;margin-right:120px}
.fill{z-index:1;position:absolute;left:0;top:4px;bottom:4px;border:2px solid #111}
.val{position:absolute;top:50%;transform:translateY(-50%);font:700 28px Inter;white-space:nowrap;padding-left:14px}
.note{font:22px Inter;color:#444;margin:6px 0 0 72px}
.grid{position:absolute;top:0;bottom:0;border-left:2px dashed #c8c8c8}
.tick{position:absolute;top:8px;transform:translateX(-50%);font:20px 'DejaVu Sans Mono';color:#555}
.black{background:#111}.grey{background:#bdbdbd}.white{background:#fff}
.hatch{background:repeating-linear-gradient(135deg,#fff 0 7px,#777 7px 9px)}
.steps{display:grid;grid-template-columns:110px 1fr;align-items:center;row-gap:28px}
.dev{font:700 26px 'DejaVu Sans Mono'}
.seq{display:flex;align-items:center;gap:18px}
.box{width:260px;border:3px solid #111;padding:16px 20px}
.box.last{background:#111;color:#fff}
.box .k{font:22px 'DejaVu Sans Mono'}
.box .n{font:700 38px Inter;margin-top:6px}
.chev{font:700 40px Inter}
.verdict{font:600 24px Inter;margin:8px 0 0 72px}
.cap{font:22px Inter;color:#444;margin-top:40px}
.take{font:800 34px Inter;margin-top:30px;padding-top:28px;border-top:4px solid #111}
"""


def logw(v, vmax=150.0):
    return 100 * math.log10(max(v, 1.0)) / math.log10(vmax) if v > 1 else 0.6


def page(body):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=page>{body}</div></body></html>"


def speedup_html():
    TICKS = (1, 10, 100)
    gl = "".join(f'<div class=grid style="left:{logw(t) if t > 1 else 0}%"></div>' for t in TICKS)
    ticks = "".join(f'<div class=tick style="left:{logw(t) if t > 1 else 0}%">{t}×</div>' for t in TICKS)
    rows = ""
    for name, ai, c, g, note in SPEEDUP:
        def bar(lbl, v, cls):
            w = logw(v)
            return (f'<div class=bar><div class=lab>{lbl}</div><div class=track>'
                    f'{gl}<div class="fill {cls}" style="width:{w}%"></div><div class=val style="left:{w}%">{v:.1f}×</div></div></div>')
        rows += (f'<div class=row><div><div class=name>{name}</div><div class=ai>{ai}</div></div>'
                 f'<div class=bars>{bar("CPU", c, "grey")}{bar("GPU", g, "black")}<div class=note>{note}</div></div></div>')
    steps = ""
    for dev, seq in GEMM_STEPS.items():
        boxes = ' <div class=chev>›</div> '.join(
            f'<div class="box{" last" if i == len(seq) - 1 else ""}"><div class=k>{k}</div><div class=n>{n}</div></div>'
            for i, (k, n) in enumerate(seq))
        steps += f'<div class=dev>{dev}</div><div class=seq>{boxes}</div>'
    body = f"""
<div class=head><div><div class=kicker>MEASURED RESULTS · i7-13650HX · RTX 4060 LAPTOP</div>
<h1>Same effort, very different payoff</h1>
<div class=sub>speedup = best version ÷ own baseline, same device</div></div>
<div class=legend><span><i class="sw grey"></i>CPU</span><span><i class="sw black"></i>GPU</span></div></div>
<div class=frame><div class=tab>SPEEDUP · LOG SCALE</div>
<div class=row style="padding:0;border:0;margin-top:-30px"><div></div><div class=bar style="height:40px;margin:0"><div class=lab></div><div class=track>{ticks}</div></div></div>
{rows}</div>
<div class=frame><div class=tab>GEMM THROUGHPUT · GFLOP/s</div><div class=steps>{steps}</div></div>
<div class=cap>Every optimised output validated against a reference implementation. TF32 GEMM max relative error 0.0686%.</div>
<div class=take>The bottleneck decides the payoff: GEMM gains 121.6× on the CPU, memory-bound vector add 1.0× on the GPU.</div>"""
    return page(body)


def profiler_html():
    gl = "".join(f'<div class=grid style="left:{t}%"></div>' for t in (0, 50, 100))
    rows = ""
    for name, sm, dram, verdict in PROFILE:
        def bar(lbl, v, cls):
            return (f'<div class=bar><div class=lab>{lbl}</div><div class=track>'
                    f'{gl}<div class="fill {cls}" style="width:{max(v, 0.6)}%"></div><div class=val style="left:{v}%">{v}%</div></div></div>')
        rows += (f'<div class=row><div><div class=name>{name}</div></div>'
                 f'<div class=bars>{bar("SM", sm, "black")}{bar("DRAM", dram, "hatch")}<div class=verdict>→ {verdict}</div></div></div>')
    grid = "".join(f'<div class=tick style="left:{t}%">{t}%</div>' for t in (0, 50, 100))
    body = f"""
<div class=head><div><div class=kicker>NSIGHT COMPUTE · RTX 4060 LAPTOP</div>
<h1>The profiler names the bottleneck</h1>
<div class=sub>utilisation, % of peak</div></div>
<div class=legend><span><i class="sw black"></i>SM (compute)</span><span><i class="sw hatch"></i>DRAM (memory traffic)</span></div></div>
<div class=frame><div class=tab>GPU KERNELS · % OF PEAK</div>
<div class=row style="padding:0;border:0;margin-top:-30px"><div></div><div class=bar style="height:40px;margin:0"><div class=lab></div><div class=track>{grid}</div></div></div>
{rows}</div>
<div class=cap>Measured with NVIDIA Nsight Compute on the same kernels as the speedup chart.</div>
<div class=take>Vector add waits on DRAM, naive GEMM on the FP32 pipe, Tensor-Core GEMM on data supply.</div>"""
    return page(body)


def render(html, path):
    tmp = path + ".html"
    open(tmp, "w").write(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1600, "height": 900})
        pg.goto("file://" + os.path.abspath(tmp))
        pg.wait_for_timeout(300)
        pg.screenshot(path=path, full_page=True)
        b.close()
    os.remove(tmp)
    print(path)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    render(speedup_html(), os.path.join(OUT, "results-speedup.png"))
    render(profiler_html(), os.path.join(OUT, "results-profiler.png"))
