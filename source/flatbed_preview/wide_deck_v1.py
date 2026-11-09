# Before/after scale drawing: flatbed clear width 2.38 m (2 pallets across) vs 2.75 m (3 across).
# Goat milk pallet (NF Marsch): 0.9 m across x 1.3 m long, 2x2 cans. Run: python -I wide_deck_v1.py <out.png>
import sys
from PIL import Image, ImageDraw, ImageFont

S = 90  # px per metre
CAB_W, CAB_L = 2.50, 2.30
DECK_L = 6.85
PAL_W, PAL_L = 0.90, 1.30
LAYER_H = 0.88          # floor 1.62 -> two layers reach 3.38 (can lids)
FLOOR_Y = 1.62
STAKE_H = 0.90

try:
    F = ImageFont.truetype("arial.ttf", 22); FB = ImageFont.truetype("arialbd.ttf", 30); FS = ImageFont.truetype("arial.ttf", 18)
except OSError:
    F = FB = FS = ImageFont.load_default()

BG, CAB, DECK, STAKE, PAL, CAN, TXT, DIM, WARN = (238, 238, 232), (200, 30, 110), (120, 90, 60), (70, 70, 75), (190, 160, 110), (175, 180, 188), (30, 30, 30), (40, 90, 200), (210, 60, 30)

def cans(d, x0, y0, w, l):
    r = min(w, l) / 4 * S * 0.85
    for i in range(2):
        for j in range(2):
            cx = x0 + (i + 0.5) * w / 2 * S; cy = y0 + (j + 0.5) * l / 2 * S
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CAN, outline=(90, 90, 95), width=2)

def dim(d, x1, x2, y, text):
    d.line([x1, y, x2, y], fill=DIM, width=2)
    for x in (x1, x2): d.line([x, y - 8, x, y + 8], fill=DIM, width=2)
    tw = d.textlength(text, font=FS); d.text(((x1 + x2) / 2 - tw / 2, y - 26), text, fill=DIM, font=FS)

def panel(clear_w, cols, title):
    deck_w = clear_w + 0.07          # stakes/boards ~3.5 cm each side
    W, H = 760, 1500
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.text((30, 20), title, fill=TXT, font=FB)
    # ---- top view
    cx = 250; top = 110
    d.text((30, 70), "Top view", fill=TXT, font=F)
    d.rectangle([cx - CAB_W / 2 * S, top, cx + CAB_W / 2 * S, top + CAB_L * S], fill=CAB, outline=TXT, width=2)
    d.text((cx - 18, top + CAB_L * S / 2 - 12), "cab", fill=(255, 255, 255), font=F)
    dt = top + CAB_L * S + 6
    d.rectangle([cx - deck_w / 2 * S, dt, cx + deck_w / 2 * S, dt + DECK_L * S], fill=DECK, outline=STAKE, width=4)
    rows = int((6.70) // PAL_L)
    x0 = cx - cols * PAL_W / 2 * S
    for r in range(rows):
        for c in range(cols):
            px = x0 + c * PAL_W * S; py = dt + 0.08 * S + r * PAL_L * S
            d.rectangle([px + 2, py + 2, px + PAL_W * S - 2, py + PAL_L * S - 2], fill=PAL, outline=(120, 95, 60), width=2)
            cans(d, px + 2, py + 2, PAL_W - 0.04, PAL_L - 0.04)
    dim(d, cx - CAB_W / 2 * S, cx + CAB_W / 2 * S, top - 14, f"cab {CAB_W:.2f} m")
    yb = dt + DECK_L * S + 30
    dim(d, cx - deck_w / 2 * S, cx + deck_w / 2 * S, yb + 10, f"outside {deck_w:.2f} m")
    spare = clear_w - cols * PAL_W
    d.text((470, dt + 20), f"{cols} across x {rows} long", fill=TXT, font=F)
    d.text((470, dt + 55), f"= {cols * rows} per layer", fill=TXT, font=F)
    d.text((470, dt + 90), f"= {cols * rows * 2} with 2 layers", fill=TXT, font=F)
    d.text((470, dt + 140), f"clear width {clear_w:.2f} m", fill=TXT, font=FS)
    d.text((470, dt + 165), f"pallets use {cols * PAL_W:.2f} m", fill=TXT, font=FS)
    d.text((470, dt + 190), f"spare {spare:.2f} m", fill=TXT, font=FS)
    if deck_w > CAB_W:
        d.text((470, dt + 230), f"sticks out {(deck_w - CAB_W) / 2 * 100:.0f} cm", fill=WARN, font=FS)
        d.text((470, dt + 252), "past the cab each side", fill=WARN, font=FS)
    # ---- rear view
    base = 1440; rc = 380; m = S * 0.85
    d.text((30, yb + 50), "Rear view", fill=TXT, font=F)
    gy = base
    d.line([40, gy, W - 40, gy], fill=TXT, width=2)
    d.rectangle([rc - CAB_W / 2 * m, gy - 3.45 * m, rc + CAB_W / 2 * m, gy - 1.2 * m], fill=CAB, outline=TXT, width=2)  # cab behind
    for sx in (-1, 1):
        d.rectangle([rc + sx * 0.75 * m - 0.30 * m, gy - 1.05 * m, rc + sx * 0.75 * m + 0.30 * m, gy], fill=(35, 35, 35))
        d.rectangle([rc + sx * 1.05 * m - 0.30 * m, gy - 1.05 * m, rc + sx * 1.05 * m + 0.30 * m, gy], fill=(35, 35, 35))
    fy = gy - FLOOR_Y * m
    d.rectangle([rc - deck_w / 2 * m, fy, rc + deck_w / 2 * m, fy + 0.18 * m], fill=DECK, outline=TXT, width=2)
    for sx in (-1, 1):
        x = rc + sx * deck_w / 2 * m
        d.rectangle([x - 4, fy - STAKE_H * m, x + 4, fy], fill=STAKE)
    x0 = rc - cols * PAL_W / 2 * m
    for layer in range(2):
        for c in range(cols):
            px = x0 + c * PAL_W * m; py = fy - (layer + 1) * LAYER_H * m
            d.rectangle([px + 2, py, px + PAL_W * m - 2, py + LAYER_H * m], fill=PAL, outline=(120, 95, 60), width=2)
            for k in range(2):
                ccx = px + (k + 0.5) * PAL_W / 2 * m
                d.rectangle([ccx - 0.17 * m, py + 0.14 * m, ccx + 0.17 * m, py + LAYER_H * m - 0.05 * m], fill=CAN, outline=(90, 90, 95))
    dim(d, rc - deck_w / 2 * m, rc + deck_w / 2 * m, gy + 30, f"{deck_w:.2f} m")
    d.text((rc + 1.7 * m, fy - 2 * LAYER_H * m - 10), "3.38 m", fill=TXT, font=FS)
    return im

a = panel(2.38, 2, "BEFORE  (now)")
b = panel(2.75, 3, "AFTER  (widened)")
out = Image.new("RGB", (a.width * 2 + 20, a.height), (255, 255, 255))
out.paste(a, (0, 0)); out.paste(b, (a.width + 20, 0))
out.save(sys.argv[1]); print("saved", sys.argv[1])
