#!/usr/bin/env python3
"""Blog explainer card generator (1536x1024 PNG, Korean).
Usage: python3 make_card.py spec.json out.png
spec = {"headline": str, "sub": str (optional), "cards": [{"label": str, "body": str}, ...2-4],
        "footer": str (optional), "badge": "개념 설명용 이미지"}
"""
import json, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1536, 1024
BG = (250, 248, 243); NAVY = (20, 42, 74); TEAL = (18, 128, 128); MUTED = (95, 105, 120)
CARD = (255, 255, 255); LINE = (222, 226, 232)
ACCENTS = [(18, 128, 128), (43, 103, 200), (214, 137, 16), (190, 70, 70)]
BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

def font(path, size):
    return ImageFont.truetype(path, size, index=1)  # index 1 = KR in the .ttc

def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for ch in text:
        if ch == "\n":
            lines.append(cur); cur = ""; continue
        t = cur + ch
        if draw.textlength(t, font=fnt) > maxw and cur:
            # break at last space if possible
            sp = cur.rfind(" ")
            if sp > 0:
                lines.append(cur[:sp]); cur = cur[sp + 1:] + ch
            else:
                lines.append(cur); cur = ch
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines

def main(spec_path, out):
    s = json.load(open(spec_path, encoding="utf-8"))
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=NAVY)
    y = 80
    for line in wrap(d, s["headline"], font(BOLD, 64), W - 200):
        d.text((100, y), line, font=font(BOLD, 64), fill=NAVY); y += 84
    if s.get("sub"):
        for line in wrap(d, s["sub"], font(REG, 32), W - 200):
            d.text((100, y + 6), line, font=font(REG, 32), fill=MUTED); y += 46
    cards = s["cards"]; n = len(cards)
    gap = 32; top = max(y + 50, 330); bottom = H - 150
    cw = (W - 200 - gap * (n - 1)) / n
    for i, c in enumerate(cards):
        x0 = 100 + i * (cw + gap); x1 = x0 + cw
        d.rounded_rectangle([x0, top, x1, bottom], radius=28, fill=CARD, outline=LINE, width=3)
        acc = ACCENTS[i % len(ACCENTS)]
        d.rounded_rectangle([x0, top, x1, top + 16], radius=8, fill=acc)
        d.ellipse([x0 + 36, top + 50, x0 + 104, top + 118], fill=acc)
        num = str(i + 1); nf = font(BOLD, 40)
        d.text((x0 + 70 - d.textlength(num, font=nf) / 2, top + 58), num, font=nf, fill=(255, 255, 255))
        ly = top + 150
        for line in wrap(d, c["label"], font(BOLD, 42), cw - 72):
            d.text((x0 + 36, ly), line, font=font(BOLD, 42), fill=NAVY); ly += 58
        ly += 14
        for line in wrap(d, c["body"], font(REG, 30), cw - 72):
            d.text((x0 + 36, ly), line, font=font(REG, 30), fill=(55, 62, 75)); ly += 44
    if s.get("footer"):
        d.text((100, H - 110), s["footer"], font=font(BOLD, 32), fill=TEAL)
    badge = s.get("badge", "개념 설명용 이미지"); bf = font(REG, 24)
    bw = d.textlength(badge, font=bf)
    d.rounded_rectangle([W - 100 - bw - 36, H - 112, W - 100, H - 68], radius=20, fill=(235, 238, 242))
    d.text((W - 100 - bw - 18, H - 106), badge, font=bf, fill=MUTED)
    im.save(out, optimize=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
