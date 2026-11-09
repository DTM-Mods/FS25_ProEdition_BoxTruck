# Top-view scale drawing: flatbed 2.38 m clear (now) vs 2.44 m clear (ProfiLiner's UAL load width).
# Euro pallet 1.20 x 0.80. Run: python -I wide_deck_v2.py <out.png>
import sys
from PIL import Image, ImageDraw, ImageFont
S = 110; DECK_L = 6.70; PL, PS = 1.20, 0.80
try:
    F = ImageFont.truetype("arial.ttf", 24); FB = ImageFont.truetype("arialbd.ttf", 30); FS = ImageFont.truetype("arial.ttf", 20)
except OSError:
    F = FB = FS = ImageFont.load_default()

def panel(clear, title):
    W, H = 640, 1060
    im = Image.new("RGB", (W, H), (238, 238, 232)); d = ImageDraw.Draw(im)
    d.text((24, 16), title, fill=(30, 30, 30), font=FB)
    sideways = 2 * PL <= clear
    pw, pl = (PL, PS) if sideways else (PS, PL)        # across, along
    cols = int(clear // pw); rows = int(DECK_L // pl)
    cx, top = 220, 110
    d.rectangle([cx - (clear / 2 + .035) * S, top - 4, cx + (clear / 2 + .035) * S, top + DECK_L * S + 4], fill=(70, 70, 75))
    d.rectangle([cx - clear / 2 * S, top, cx + clear / 2 * S, top + DECK_L * S], fill=(120, 90, 60))
    x0 = cx - cols * pw / 2 * S
    for r in range(rows):
        for c in range(cols):
            px, py = x0 + c * pw * S, top + r * pl * S
            d.rectangle([px + 2, py + 2, px + pw * S - 2, py + pl * S - 2], fill=(190, 160, 110), outline=(120, 95, 60), width=2)
    d.text((cx - 30, top - 40), "cab", fill=(30, 30, 30), font=F)
    d.text((cx - 70, top + DECK_L * S + 14), f"clear {clear:.2f} m", fill=(40, 90, 200), font=F)
    tx = 400
    for i, t in enumerate([("long side ACROSS" if sideways else "long side front-back"),
                           f"{cols} across x {rows} long", f"= {cols * rows} pallets / layer",
                           f"needs {2 * PL:.2f} m for 2 sideways", f"spare {clear - cols * pw:.2f} m"]):
        d.text((tx, top + 20 + i * 40), t, fill=(210, 60, 30) if i == 0 and not sideways else (30, 30, 30), font=FS)
    return im

a = panel(2.38, "BEFORE (now)"); b = panel(2.44, "AFTER (= ProfiLiner)")
out = Image.new("RGB", (a.width * 2 + 20, a.height), (255, 255, 255))
out.paste(a, (0, 0)); out.paste(b, (a.width + 20, 0)); out.save(sys.argv[1]); print("saved", sys.argv[1])
