"""Builds assets/hero.gif and assets/light/hero.gif: the hero.svg banner with the
animated hourglass (art by @Ki11_5trike) composited into its frame.
Run after gen_assets.py:  python tools/make_hero_gif.py   (needs playwright + pillow)"""
import os
import numpy as np
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


def tint(img):
    """Shift the art's neutral grey background toward deep purple; leave colourful pixels alone."""
    a = np.asarray(img.convert("RGB")).astype(np.float32)
    mx, mn = a.max(2), a.min(2)
    sat = (mx - mn) / (mx + 1e-3)
    k = np.clip(1 - sat * 3.0, 0, 1)[..., None]
    tinted = a * np.array([0.78, 0.55, 1.15]) + np.array([6, 0, 14])
    out = np.clip(a * (1 - k) + tinted * k, 0, 255).astype(np.uint8)
    return Image.fromarray(out).convert("RGBA")


def border(img, accent, accent2):
    """Gradient (accent -> accent2) rounded border around the art frame."""
    g = Image.new("RGBA", (PW, PH))
    c1, c2 = Image.new("RGBA", (1, 1), accent).getpixel((0, 0)), Image.new("RGBA", (1, 1), accent2).getpixel((0, 0))
    for y in range(PH):
        t = y / (PH - 1)
        ImageDraw.Draw(g).line([(0, y), (PW, y)], fill=tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(4)))
    ring = Image.new("L", (PW, PH), 0)
    d = ImageDraw.Draw(ring)
    d.rounded_rectangle((0, 0, PW - 1, PH - 1), R, fill=200)
    d.rounded_rectangle((2, 2, PW - 3, PH - 3), R - 2, fill=0)
    img.paste(g, (PX, PY), ring)


def build(svg_path, out_path, page_bg, accent, accent2):
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
        f = tint(fr.convert("RGBA").resize((PW, PH), Image.LANCZOS))
        img = base.copy()
        img.paste(f, (PX, PY), mask)
        border(img, accent, accent2)
        frames.append(img.convert("RGB"))
        durs.append(fr.info.get("duration", art.info.get("duration", 40)))
    # one shared palette keeps the static text crisp and the file small
    # palette built from the static banner + a few art frames so accent colours stay exact
    sample = Image.new("RGB", (1200, 360 * 4))
    sample.paste(base.convert("RGB"), (0, 0))
    for i, k in enumerate((0, len(frames) // 3, 2 * len(frames) // 3)):
        sample.paste(frames[k], (0, 360 * (i + 1)))
    pal = sample.quantize(colors=255, method=Image.MEDIANCUT)
    # no dithering on the flat banner (crisp text), dithering only inside the art frame
    box = (PX - 2, PY - 2, PX + PW + 2, PY + PH + 2)
    q = []
    for f in frames:
        flat = f.quantize(palette=pal, dither=Image.Dither.NONE)
        flat.paste(f.quantize(palette=pal, dither=Image.Dither.FLOYDSTEINBERG).crop(box), box[:2])
        q.append(flat)
    q[0].save(out_path, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)
    print(out_path, os.path.getsize(out_path) // 1024, "KB")


if __name__ == "__main__":
    build(os.path.join(ASSETS, "hero.svg"), os.path.join(ASSETS, "hero.gif"), "#0d1117", "#c4a7ff", "#ff6fb5")
    build(os.path.join(ASSETS, "light", "hero.svg"), os.path.join(ASSETS, "light", "hero.gif"), "#ffffff", "#7c3aed", "#c0267d")
