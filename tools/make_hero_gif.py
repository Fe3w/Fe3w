"""Builds assets/hero.gif and assets/light/hero.gif: the hero.svg banner with the
animated hourglass (art by @Ki11_5trike) composited into its frame.
Run after gen_assets.py:  python tools/make_hero_gif.py   (needs playwright + pillow)"""
import os
from PIL import Image, ImageDraw, ImageSequence
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
ART = os.path.join(HERE, "hero-hourglass.gif")
PX, PY, PW, PH, R = 912, 14, 216, 332, 14


def render(svg_path, png_path):
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 360})
        pg.goto("file://" + os.path.abspath(svg_path))
        pg.wait_for_timeout(8000)  # let the SVG intro animations finish
        pg.screenshot(path=png_path, omit_background=True)
        b.close()


def build(svg_path, out_path, page_bg):
    tmp = out_path + ".png"
    render(svg_path, tmp)
    shot = Image.open(tmp).convert("RGBA")
    base = Image.new("RGBA", shot.size, page_bg)  # GitHub page colour behind the rounded corners
    base.alpha_composite(shot)
    os.remove(tmp)
    mask = Image.new("L", (PW, PH), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, PW - 1, PH - 1), R, fill=255)
    art = Image.open(ART)
    frames, durs = [], []
    for fr in ImageSequence.Iterator(art):
        f = fr.convert("RGBA").resize((PW, PH), Image.LANCZOS)
        img = base.copy()
        img.paste(f, (PX, PY), mask)
        frames.append(img.convert("RGB"))
        durs.append(fr.info.get("duration", art.info.get("duration", 40)))
    # one shared palette keeps the static text crisp and the file small
    pal = frames[len(frames) // 2].quantize(colors=255, method=Image.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.FLOYDSTEINBERG) for f in frames]
    q[0].save(out_path, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)
    print(out_path, os.path.getsize(out_path) // 1024, "KB")


if __name__ == "__main__":
    build(os.path.join(ASSETS, "hero.svg"), os.path.join(ASSETS, "hero.gif"), "#0d1117")
    build(os.path.join(ASSETS, "light", "hero.svg"), os.path.join(ASSETS, "light", "hero.gif"), "#ffffff")
