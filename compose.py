#!/usr/bin/env python3
"""Compose the entry image for news-image-20261121.

Builds a one-page newspaper front page for Saturday 21 November 2026:
a masthead naming the day, a standfirst, and four illustrated stories
whose pictures are quadrants of the freshly generated lead artwork
(lead-art.png, drawn this session, no text in it), plus a strip of
short items. All lettering is rendered here with PIL so every word
stays crisp and legible. Output: entry.png, 1024x1024, under 1 MiB.

Run: python3 compose.py  (reads lead-art.png beside this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
LEAD = os.path.join(HERE, "lead-art.png")
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (25, 25, 25)
RED = (163, 29, 29)
GREY = (110, 102, 86)
RULE = (150, 140, 118)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting width."""
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def tracked(draw, cx, y, text, fnt, fill, tracking=3):
    """Draw centred text with letter tracking."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking


def quadrant(lead, qx, qy, tw, th):
    """Crop one quadrant of the lead art to the target aspect."""
    qw, qh = 960, 640
    box = (qx * qw + 14, qy * qh + 14, (qx + 1) * qw - 14, (qy + 1) * qh - 14)
    crop = lead.crop(box)
    cw, ch = crop.size
    target = tw / th
    if cw / ch > target:  # too wide: trim sides
        nw = int(ch * target)
        x0 = (cw - nw) // 2
        crop = crop.crop((x0, 0, x0 + nw, ch))
    else:  # too tall: trim top/bottom
        nh = int(cw / target)
        y0 = (ch - nh) // 2
        crop = crop.crop((0, y0, cw, y0 + nh))
    return crop.resize((tw, th), Image.LANCZOS)


STORIES = [
    # (quadrant x, quadrant y, kicker, headline, body)
    (0, 0, "SHENZHEN SUMMIT",
     "Three leaders sign peace pact",
     "Trump, Xi and Putin meet and sign a four-point declaration "
     "\u2014 one that says nothing about Ukraine."),
    (1, 0, "THE HAGUE",
     "Myanmar guilty of genocide",
     "The World Court finds Myanmar responsible for genocide "
     "against the Rohingya \u2014 a historic first."),
    (0, 1, "MARKETS",
     "AI sell-off rattles the world",
     "Fears AI spending will not pay off drive a broad rout: "
     "the S&P 500 falls 3.7%, Japan's Nikkei 5.1%."),
    (1, 1, "UKRAINE",
     "Strikes hit Zelenskyy's hometown",
     "A Russian missile kills two and wounds 60 in Kryvyi Rih; "
     "another lands in Poland during NATO drills."),
]

SHORTS = [
    ("MEXICO", "FBI most-wanted cartel boss \u2018El Chapo Isidro\u2019 "
     "captured in Sinaloa; gun battles follow the arrest."),
    ("CLIMATE", "COP31 talks in Antalya run past their deadline "
     "in a standoff over fossil fuels."),
    ("SPACE", "BepiColombo reaches Mercury orbit after "
     "an eight-year journey."),
]


def main():
    lead = Image.open(LEAD).convert("RGB")
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)

    # --- masthead ---------------------------------------------------
    d.text((W // 2, 22), "THE WORLD IN ONE DAY", font=font(SERIF_B, 46),
           fill=INK, anchor="ma")
    d.line([(30, 82), (W - 30, 82)], fill=RULE, width=2)
    tracked(d, W // 2, 92, "SATURDAY  \u00b7  21 NOVEMBER 2026",
            font(SANS_B, 25), RED, tracking=4)
    d.line([(30, 132), (W - 30, 132)], fill=RULE, width=2)

    # --- standfirst -------------------------------------------------
    d.text((W // 2, 144),
           "Shenzhen pact  \u00b7  Hague genocide verdict  \u00b7  Markets plunge  \u00b7  Strikes on Kryvyi Rih",
           font=font(SERIF, 20), fill=INK, anchor="ma")
    d.line([(30, 178), (W - 30, 178)], fill=INK, width=3)

    # --- four illustrated stories ----------------------------------
    gx, gy = 30, 196
    cw, gap = 472, 20
    thumb_h = 180
    row_h = 330
    for i, (qx, qy, kicker, headline, body) in enumerate(STORIES):
        x = gx + (i % 2) * (cw + gap)
        y = gy + (i // 2) * row_h
        page.paste(quadrant(lead, qx, qy, cw, thumb_h), (x, y))
        d.rectangle([x, y, x + cw - 1, y + thumb_h - 1], outline=INK, width=2)
        ty = y + thumb_h + 10
        d.text((x, ty), kicker, font=font(SANS_B, 17), fill=RED)
        hy = ty + 26
        hlines = wrap(d, headline, font(SERIF_B, 27), cw)
        for j, ln in enumerate(hlines):
            d.text((x, hy + j * 32), ln, font=font(SERIF_B, 27), fill=INK)
        by = hy + 32 * len(hlines)
        for j, ln in enumerate(wrap(d, body, font(SANS, 18), cw)[:2]):
            d.text((x, by + 4 + j * 23), ln, font=font(SANS, 18), fill=INK)

    # --- short items strip ------------------------------------------
    sy = gy + 2 * row_h + 12
    d.line([(30, sy), (W - 30, sy)], fill=INK, width=3)
    sw = 302
    for i, (kick, text) in enumerate(SHORTS):
        x = 30 + i * (sw + 20)
        d.text((x, sy + 12), kick, font=font(SANS_B, 17), fill=RED)
        for j, ln in enumerate(wrap(d, text, font(SANS, 16), sw)[:3]):
            d.text((x, sy + 38 + j * 21), ln, font=font(SANS, 16), fill=INK)

    # --- footer ------------------------------------------------------
    d.line([(30, 984), (W - 30, 984)], fill=RULE, width=1)
    d.text((W // 2, 992), "Saturday 21 November 2026  \u00b7  Sources: AP, Reuters, NYT, BBC",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    page.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}: {page.size}, {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
