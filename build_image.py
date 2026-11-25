#!/usr/bin/env python3
"""Build the v2 broadsheet for Wednesday 25 November 2026, winner template.

THE WORLD IN ONE DAY — a program-drawn broadsheet (PIL, rendered text
and flat vector illustrations, never AI-generated image text):
  1 masthead + giant date + red 3-story lead line
  2 "the day in numbers" strip (6 big figures)
  3 region bar with counts (8 regions, 41 stories)
  4 UTC timeline (6 beats)
  5 three hero stories with flat illustrations + source + HOW SURE tag
  6 ten more illustrated stories (numbered 4-13)
  7 "ALSO ON WEDNESDAY" briefs list (numbered 14-41) with source codes
  8 dotted world map with numbered pins 1-13
  9 DATE CHECK footer naming excluded earlier-day stories with dates
 10 HOW SURE legend (CONFIRMED / OFFICIAL / REPORTED / CLAIM)

Every story was first reported on 25 November 2026; claims are
attributed, never stated as fact; nothing is invented.

Run:  python3 build_image.py   -> writes image.png next to this file.
Deterministic: fixed fonts, fixed layout, no timestamps, no randomness.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "image.png")

W, H = 1024, 1024
PAPER = (253, 253, 247)
INK = (20, 20, 20)
GREY = (96, 96, 96)
RED = (158, 24, 24)
DARKRED = (118, 16, 16)
LIGHT = (238, 236, 228)
PANEL = (240, 241, 235)
OCEAN = (216, 229, 238)
LAND_DOT = (150, 152, 142)
RULE = (40, 40, 40)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_MAST = font(SERIF_B, 30)
F_DATE = font(SERIF_B, 42)
F_LEAD = font(SANS_B, 14)
F_NUM_F = font(SANS_B, 20)
F_NUM_L = font(SANS, 9)
F_REG = font(SANS_B, 12)
F_SEC = font(SANS_B, 13)
F_TL_T = font(SANS_B, 10)
F_TL = font(SANS, 10)
F_HERO_H = font(SANS_B, 14)
F_HERO_F = font(SANS, 11)
F_SRC = font(SANS_B, 9)
F_ILL_H = font(SANS_B, 11)
F_ILL_F = font(SANS, 10)
F_BRIEF = font(SANS, 11)
F_BRIEF_B = font(SANS_B, 11)
F_MAP_T = font(SANS_B, 11)
F_PIN = font(SANS_B, 9)
F_FOOT = font(SANS, 10)
F_FOOT_B = font(SANS_B, 10)

# ---------------------------------------------------------------- data
# (number, region, headline, fact, source, sure, icon, lon, lat)
HEROES = [
    (1, "EUROPE",
     "Ukraine confirms it hit a Russian ship",
     "President Zelenskiy says Kyiv was behind Saturday's drone strike "
     "on a Russian cargo ship; its 16 crew were evacuated, the ship "
     "towed to St Petersburg.",
     "Reuters", "CONFIRMED", "ship", 25, 60),
    (2, "EAST ASIA",
     "Shenzhou-24 carries the first Pakistani into orbit",
     "Zeeshan Ali, 40, joins Tang Hongbo and Wu Yi aboard Tiangong, the "
     "first foreign astronaut on China's station. Launch 08:18 Beijing "
     "time from Jiuquan.",
     "Reuters / AP", "OFFICIAL", "rocket", 99, 40),
    (3, "MIDDLE EAST",
     "Houthis hit Riyadh's tallest tower, 11 wounded",
     "A drone strike hits the capital's tallest tower, the second attack "
     "on it within days, Saudi civil defence says.",
     "Reuters", "REPORTED", "tower", 47, 25),
]

ILLUSTRATED = [
    (4, "EAST ASIA", "Huawei convicted in US trial",
     "Guilty over Iran business; acquitted of racketeering.",
     "Reuters", "OFFICIAL", "chip", 121, 31),
    (5, "NORTH AMERICA", "Dow tops 50,000 as Nasdaq falls",
     "Dow 50,018.70 (+0.85%); Nasdaq -1.48%, Nvidia -5.9%.",
     "Reuters", "CONFIRMED", "chart_up", -74, 41),
    (6, "NORTH AMERICA", "Dell doubles sales on AI demand",
     "Sales $54.9bn, $60.2bn in new AI orders; shares +4.1%.",
     "Reuters", "OFFICIAL", "server", -97, 30),
    (7, "SOUTH ASIA", "Nepal hit by a 5.6 quake",
     "Tremor strikes Koshi province near the China border.",
     "EMSC", "OFFICIAL", "crack", 85, 28),
    (8, "EUROPE", "Sarkozy corruption case sent to trial",
     "Ex-president and Carla Bruni to trial; hearing 1 Apr 2027.",
     "Reuters", "OFFICIAL", "columns", 2, 49),
    (9, "MIDDLE EAST", "Israeli strike kills Hamas security chief",
     "Naim Abu Nahl killed west of Gaza City, AP reports.",
     "AP", "REPORTED", "pin", 34, 31),
    (10, "EAST ASIA", "Asia stocks tumble on tariff threats",
     "Korea -5.3%, Taiwan -5.1%, Nikkei -2.9%; AI rally fizzles.",
     "Reuters", "CONFIRMED", "chart_down", 127, 37),
    (11, "NORTH AMERICA", "Trump gives Giuliani the Medal of Freedom",
     "Ex-New York mayor honoured at the White House.",
     "Reuters", "OFFICIAL", "medal", -77, 39),
    (12, "SOUTH ASIA", "Sooryavanshi, 15, smashes 204 off 53",
     "Indian teen hits a record double century for India A against UAE.",
     "Press", "REPORTED", "bat", 77, 28),
    (13, "LATIN AMERICA", "Spix's macaw chick hatches in Brazil",
     "Zoo hails the birth as a boost for the species' recovery.",
     "Reuters", "REPORTED", "bird", -52, -10),
]

# (number, region, one-line brief, source code)
BRIEFS = [
    (14, "EUROPE", "Russian strike on Zaporizhzhia kills 2, wounds 22", "Reuters"),
    (15, "EUROPE", "Putin: Ukraine keeps hitting refineries despite Trump's requests", "Reuters"),
    (16, "EUROPE", "Latvia sees a 'tipping point' in the war in 2027", "Reuters"),
    (17, "EUROPE", "Sweden's PM fails again to form a government", "Wire"),
    (18, "EUROPE", "Norway urges Kyiv to show caution over Gulf-style operations", "Reuters"),
    (19, "EUROPE", "NATO vows a shield against space threats after nuclear-satellite reports", "Wire"),
    (20, "MIDDLE EAST", "Houthis push to 60 km from Aden; army says they will not take the city", "Reuters"),
    (21, "MIDDLE EAST", "Houthis: 25 dead in Saudi strikes on southern Yemen", "Wire"),
    (22, "MIDDLE EAST", "Six killed in Israeli strikes across Gaza", "Wire"),
    (23, "MIDDLE EAST", "Gaza health emergency declared over rising meningitis", "Wire"),
    (24, "MIDDLE EAST", "Iraq seeks a bigger oil quota before the 2027 OPEC debate", "Reuters"),
    (25, "EAST ASIA", "China probes Shanghai party boss Chen Jining", "Reuters"),
    (26, "EAST ASIA", "US blacklists an Alibaba unit over alleged Nvidia chip diversion", "Reuters"),
    (27, "NORTH AMERICA", "Trump pardons Thanksgiving turkeys Freedom and Feathers", "Reuters"),
    (28, "NORTH AMERICA", "US consumer confidence hits a near two-year high", "Reuters"),
    (29, "NORTH AMERICA", "CIA and spy chief's office breached; unclassified data hit", "Reuters"),
    (30, "NORTH AMERICA", "Fort Hood gunman seeks a stay of execution", "Reuters"),
    (31, "NORTH AMERICA", "US reports a bird flu death in Washington state", "WHO"),
    (32, "LATIN AMERICA", "Argentina's economic activity falls for a third straight month", "Reuters"),
    (33, "LATIN AMERICA", "Mexico reports 12 active measles cases", "Reuters"),
    (34, "SPORT", "US to host the Copa America again in 2028", "Reuters"),
    (35, "SPORT", "England beat Australia by 8 wickets to level the T20 series", "Press"),
    (36, "SPORT", "Real Madrid beat PSV 5-1; Bellingham's wonder goal", "BBC"),
    (37, "AFRICA", "Fighting traps Ebola teams near a hospital in Ituri, Congo", "WHO"),
    (38, "AFRICA", "Sudan drones killed 1,600+ people this year, UN says", "UN"),
    (39, "AFRICA", "MSF halts work in South Sudan's Yei River after an abduction", "MSF"),
    (40, "AFRICA", "ECOWAS ministers review plans for a 2027 single currency", "PANA"),
    (41, "AFRICA", "Libya conflict risks a new flare-up after the port sinking", "Reuters"),
]

REGIONS = [("EUROPE", 7), ("MIDDLE EAST", 7), ("SOUTH ASIA", 3),
           ("EAST ASIA", 5), ("AFRICA", 5), ("NORTH AMERICA", 8),
           ("LATIN AMERICA", 3), ("SPORT", 3)]

NUMBERS = [
    ("11", "wounded in the Riyadh strike"),
    ("16", "crew evacuated, Gulf ship"),
    ("5.6", "Nepal quake magnitude"),
    ("$54.9bn", "Dell quarterly sales"),
    ("50,018", "Dow close, a record"),
    ("204", "runs, Sooryavanshi, 15"),
]

TIMELINE = [
    ("00:18 UTC", "Shenzhou-24 launches from Jiuquan"),
    ("MORNING", "Asia's chip stocks tumble on tariff threats"),
    ("MORNING", "Zelenskiy confirms the Gulf of Finland strike"),
    ("MIDDAY", "Dow closes above 50,000; Nasdaq slides"),
    ("EVENING", "Dell: sales double to $54.9bn on AI demand"),
    ("EVENING", "Houthi drone wounds 11 at Riyadh's tallest tower"),
]

DATE_CHECK = (
    "DATE CHECK — Every story on this page happened or was first reported on "
    "Wednesday 25 November 2026 (UTC). Left out because they happened on an "
    "earlier day: the US midterm elections (3 Nov); Nvidia's +31.5% surge "
    "(Mon 23 Nov); the Shenzhou-24 crew announcement (Tue 24 Nov — the launch "
    "was today); the Libyan port sinking (Sun 22 Nov — only today's explainer "
    "on its fallout is listed).")

HOW_SURE = (
    "HOW SURE — CONFIRMED: 2+ outlets · OFFICIAL: on the record · REPORTED: "
    "one outlet · CLAIM: one side's account, labelled as such.  Scenes are "
    "drawn illustrations, not photographs. Pictures and map: original, drawn in code.")

# ---------------------------------------------------------------- map data
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66), (-80, 73),
     (-65, 62), (-55, 52), (-60, 47), (-70, 44), (-75, 35), (-80, 26), (-85, 20),
     (-90, 14), (-95, 16), (-100, 20), (-105, 23), (-115, 30), (-125, 40),
     (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    [(-80, 10), (-75, 5), (-60, 5), (-52, 5), (-40, -5), (-35, -10), (-40, -20),
     (-48, -28), (-55, -35), (-65, -40), (-70, -50), (-73, -40), (-75, -25),
     (-78, -15), (-80, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59), (18, 56),
     (21, 55), (24, 59), (28, 60), (30, 62), (30, 70), (25, 71), (18, 69),
     (12, 65), (5, 60), (-5, 58), (-10, 54), (-10, 44)],
    [(-6, 35), (10, 37), (20, 32), (30, 31), (35, 28), (43, 12), (51, 11), (48, 2),
     (40, -10), (35, -18), (32, -28), (26, -34), (19, -35), (15, -27), (12, -18),
     (9, -1), (4, 6), (-8, 5), (-15, 11), (-17, 15), (-16, 20), (-15, 27), (-10, 31)],
    [(30, 70), (40, 68), (55, 68), (70, 72), (90, 75), (110, 76), (130, 72),
     (150, 70), (170, 66), (178, 65), (170, 60), (162, 56), (158, 52), (142, 50),
     (140, 40), (130, 35), (127, 35), (122, 30), (120, 22), (110, 20), (105, 10),
     (100, 8), (98, 12), (95, 16), (92, 20), (88, 22), (80, 15), (76, 10),
     (72, 20), (66, 25), (60, 25), (55, 26), (50, 29), (48, 30), (43, 32),
     (36, 36), (30, 36), (28, 38), (26, 40), (30, 45), (28, 55), (30, 65)],
    [(114, -22), (122, -14), (132, -12), (142, -11), (146, -19), (150, -23),
     (153, -27), (150, -37), (140, -38), (132, -32), (124, -33), (115, -35),
     (113, -26)],
]


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


# ---------------------------------------------------------------- helpers
def wrap(draw, text, fnt, width):
    lines, cur, cur_w = [], [], 0
    space_w = draw.textlength(" ", font=fnt)
    for word in text.split():
        w = draw.textlength(word, font=fnt)
        add = w if not cur else w + space_w
        if cur and cur_w + add > width:
            lines.append(" ".join(cur))
            cur, cur_w = [word], w
        else:
            cur.append(word)
            cur_w += add
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_icon(d, kind, x, y, w, h, col):
    """Flat vector illustration in box (x, y, w, h)."""
    cx, cy = x + w // 2, y + h // 2
    if kind == "ship":
        d.polygon([(x + 4, cy + 2), (x + w - 4, cy + 2), (x + w - 12, cy + 14),
                   (x + 12, cy + 14)], fill=col)
        d.rectangle([cx - 2, cy - 14, cx + 2, cy + 2], fill=col)
        d.polygon([(cx + 2, cy - 14), (cx + 14, cy - 2), (cx + 2, cy - 2)], fill=RED)
        for wx in (x + 2, x + w // 2 - 4, x + w - 14):
            d.arc([wx, cy + 16, wx + 12, cy + 24], 0, 180, fill=col, width=2)
    elif kind == "rocket":
        d.polygon([(cx, cy - 18), (cx + 8, cy - 4), (cx + 6, cy + 10),
                   (cx - 6, cy + 10), (cx - 8, cy - 4)], fill=col)
        d.ellipse([cx - 3, cy - 8, cx + 3, cy - 2], fill=(255, 255, 255))
        d.polygon([(cx - 4, cy + 10), (cx + 4, cy + 10), (cx, cy + 20)], fill=RED)
        for sx, sy in ((x + 4, y + 4), (x + w - 6, y + 10), (x + 8, y + h - 8)):
            d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=col)
    elif kind == "tower":
        d.rectangle([cx - 7, cy - 18, cx + 7, cy + 16], fill=col)
        d.polygon([(cx - 9, cy - 18), (cx, cy - 24), (cx + 9, cy - 18)], fill=RED)
        for wy in range(cy - 12, cy + 14, 6):
            d.rectangle([cx - 4, wy, cx + 4, wy + 3], fill=(255, 255, 255))
        d.ellipse([cx + 12, cy - 20, cx + 18, cy - 14], fill=RED)
    elif kind == "chip":
        d.rectangle([x + 8, y + 6, x + w - 8, y + h - 6], fill=col)
        d.rectangle([x + w // 2 - 6, y + h // 2 - 6, x + w // 2 + 6, y + h // 2 + 6],
                    fill=(255, 255, 255))
        for px in (x + 12, x + w // 2, x + w - 12):
            d.line([(px, y + 2), (px, y + 6)], fill=col, width=2)
            d.line([(px, y + h - 6), (px, y + h - 2)], fill=col, width=2)
    elif kind == "chart_up":
        d.line([(x + 6, y + h - 8), (x + 6, y + 6)], fill=col, width=2)
        d.line([(x + 6, y + h - 8), (x + w - 4, y + h - 8)], fill=col, width=2)
        d.line([(x + 8, y + h - 12), (x + w // 2, y + 14), (x + w - 6, y + 6)],
               fill=RED, width=3)
        d.polygon([(x + w - 6, y + 6), (x + w - 12, y + 4), (x + w - 10, y + 12)],
                  fill=RED)
    elif kind == "chart_down":
        d.line([(x + 6, y + h - 8), (x + 6, y + 6)], fill=col, width=2)
        d.line([(x + 6, y + h - 8), (x + w - 4, y + h - 8)], fill=col, width=2)
        d.line([(x + 8, y + 8), (x + w // 2, y + 18), (x + w - 6, y + h - 12)],
               fill=RED, width=3)
        d.polygon([(x + w - 6, y + h - 12), (x + w - 12, y + h - 14),
                   (x + w - 10, y + h - 6)], fill=RED)
    elif kind == "server":
        for i in range(3):
            yy = y + 4 + i * 12
            d.rectangle([x + 8, yy, x + w - 8, yy + 9], fill=col)
            d.ellipse([x + 11, yy + 3, x + 14, yy + 6], fill=(255, 255, 255))
    elif kind == "crack":
        d.line([(x + 4, y + h - 6), (x + w - 4, y + h - 6)], fill=col, width=2)
        d.line([(x + 8, y + h - 6), (x + 16, y + 8), (x + 26, y + h - 6),
                (x + 34, y + 12), (x + w - 8, y + h - 6)], fill=RED, width=2)
    elif kind == "columns":
        d.rectangle([x + 6, y + 6, x + w - 6, y + 11], fill=col)
        d.rectangle([x + 6, y + h - 10, x + w - 6, y + h - 5], fill=col)
        for bx in (x + 9, x + w // 2 - 3, x + w - 15):
            d.rectangle([bx, y + 12, bx + 6, y + h - 11], fill=col)
    elif kind == "pin":
        d.ellipse([cx - 8, cy - 16, cx + 8, cy], fill=RED)
        d.polygon([(cx - 8, cy - 2), (cx + 8, cy - 2), (cx, cy + 12)], fill=RED)
        d.ellipse([cx - 3, cy - 11, cx + 3, cy - 5], fill=(255, 255, 255))
    elif kind == "medal":
        d.polygon([(cx - 8, cy - 16), (cx - 2, cy - 16), (cx - 4, cy - 4),
                   (cx - 10, cy - 4)], fill=RED)
        d.polygon([(cx + 8, cy - 16), (cx + 2, cy - 16), (cx + 4, cy - 4),
                   (cx + 10, cy - 4)], fill=RED)
        d.ellipse([cx - 11, cy - 6, cx + 11, cy + 16], fill=col)
        d.text((cx - 3, cy - 1), "1", font=F_SRC, fill=(255, 255, 255))
    elif kind == "bat":
        d.line([(x + 8, y + h - 6), (x + w - 10, y + 6)], fill=col, width=5)
        d.ellipse([x + w - 14, y + h - 14, x + w - 4, y + h - 4], fill=RED)
    elif kind == "bird":
        d.ellipse([x + 6, cy - 6, x + w - 10, cy + 12], fill=col)
        d.ellipse([x + w - 18, cy - 14, x + w - 6, cy - 2], fill=col)
        d.polygon([(x + w - 6, cy - 10), (x + w + 1, cy - 7), (x + w - 6, cy - 5)],
                  fill=RED)
        d.ellipse([x + 12, cy - 2, x + w - 16, cy + 8], fill=RED)


# ---------------------------------------------------------------- build
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 20
    cw = W - 2 * mx  # 984

    # 1 masthead + giant date + red lead line
    t = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(t, font=F_MAST)) / 2, 4), t, font=F_MAST, fill=INK)
    dt = "Wednesday 25 November 2026"
    d.text(((W - d.textlength(dt, font=F_DATE)) / 2, 38), dt, font=F_DATE, fill=INK)
    lead = ("UKRAINE CONFIRMS GULF SHIP STRIKE  ·  SHENZHOU-24 CARRIES FIRST "
            "PAKISTANI TO ORBIT  ·  HOUTHIS HIT RIYADH TOWER")
    d.text(((W - d.textlength(lead, font=F_LEAD)) / 2, 86), lead, font=F_LEAD,
           fill=DARKRED)
    d.line([(mx, 108), (W - mx, 108)], fill=RULE, width=2)

    # 2 numbers strip
    y = 116
    d.text((mx, y), "THE DAY IN NUMBERS", font=F_SEC, fill=INK)
    y += 18
    bw = (cw - 5 * 8) // 6
    for i, (fig, lab) in enumerate(NUMBERS):
        x0 = mx + i * (bw + 8)
        d.rectangle([x0, y, x0 + bw, y + 44], fill=PANEL, outline=RULE, width=1)
        d.text((x0 + 8, y + 2), fig, font=F_NUM_F, fill=DARKRED)
        for j, ln in enumerate(wrap(d, lab, F_NUM_L, bw - 12)):
            d.text((x0 + 8, y + 23 + j * 10), ln, font=F_NUM_L, fill=GREY)
    y += 52

    # 3 region bar
    d.rectangle([mx, y, W - mx, y + 20], fill=DARKRED)
    parts = "  ·  ".join("%s %d" % (n, c) for n, c in REGIONS)
    d.text(((W - d.textlength(parts, font=F_REG)) / 2, y + 3), parts,
           font=F_REG, fill=(255, 255, 255))
    y += 26

    # 4 UTC timeline
    d.text((mx, y), "THE DAY IN UTC", font=F_SEC, fill=INK)
    y += 18
    tw = (cw - 5 * 10) // 6
    for i, (when, what) in enumerate(TIMELINE):
        x0 = mx + i * (tw + 10)
        d.rectangle([x0, y, x0 + tw, y + 40], fill=LIGHT, outline=RULE, width=1)
        d.ellipse([x0 + 4, y + 4, x0 + 10, y + 10], fill=RED)
        d.text((x0 + 14, y + 2), when, font=F_TL_T, fill=DARKRED)
        for j, ln in enumerate(wrap(d, what, F_TL, tw - 8)):
            d.text((x0 + 4, y + 15 + j * 11), ln, font=F_TL, fill=INK)
    y += 48

    # 5 three heroes
    d.text((mx, y), "THE THREE BIG STORIES", font=F_SEC, fill=INK)
    y += 18
    hw = (cw - 2 * 10) // 3
    hero_top = y
    for i, (num, region, head, fact, src, sure, icon, lon, lat) in enumerate(HEROES):
        x0 = mx + i * (hw + 10)
        d.rectangle([x0, y, x0 + hw, y + 142], fill=PANEL, outline=RULE, width=1)
        d.rectangle([x0, y, x0 + hw, y + 56], fill=(226, 232, 240))
        draw_icon(d, icon, x0 + 8, y + 4, 56, 48, (70, 90, 120))
        d.text((x0 + 72, y + 6), "%d · %s" % (num, region), font=F_SRC, fill=RED)
        d.text((x0 + 72, y + 22), sure, font=F_SRC, fill=GREY)
        d.text((x0 + 72, y + 38), "Source: " + src, font=F_SRC, fill=GREY)
        lines = wrap(d, head, F_HERO_H, hw - 16)
        for j, ln in enumerate(lines[:2]):
            d.text((x0 + 8, y + 62 + j * 17), ln, font=F_HERO_H, fill=INK)
        fl = wrap(d, fact, F_HERO_F, hw - 16)
        for j, ln in enumerate(fl[:4]):
            d.text((x0 + 8, y + 62 + len(lines[:2]) * 17 + 2 + j * 13), ln,
                   font=F_HERO_F, fill=INK)
    y = hero_top + 142 + 8

    # 6 ten more illustrated stories
    d.text((mx, y), "TEN MORE STORIES", font=F_SEC, fill=INK)
    y += 18
    iw = (cw - 10) // 2
    row_h = 34
    for i, (num, region, head, fact, src, sure, icon, lon, lat) in enumerate(ILLUSTRATED):
        col, row = i % 2, i // 2
        x0 = mx + col * (iw + 10)
        y0 = y + row * row_h
        d.rectangle([x0, y0, x0 + 40, y0 + 30], fill=(226, 232, 240),
                    outline=RULE, width=1)
        draw_icon(d, icon, x0 + 1, y0 + 1, 38, 28, (70, 90, 120))
        d.text((x0 + 46, y0), "%d. %s" % (num, head), font=F_ILL_H, fill=INK)
        fl = wrap(d, fact + "  [%s · %s]" % (src, sure), F_ILL_F, iw - 46)
        for j, ln in enumerate(fl[:2]):
            d.text((x0 + 46, y0 + 14 + j * 12), ln, font=F_ILL_F, fill=GREY)
    y += 5 * row_h + 6

    # 7 briefs list
    d.text((mx, y), "ALSO ON WEDNESDAY 25 NOVEMBER", font=F_SEC, fill=INK)
    y += 18
    bw2 = (cw - 10) // 2
    rows = (len(BRIEFS) + 1) // 2
    for i, (num, region, text, src) in enumerate(BRIEFS):
        col, row = i % 2, i // 2
        x0 = mx + col * (bw2 + 10)
        y0 = y + row * 12
        line = "%d. %s [%s]" % (num, text, src)
        # shrink to fit one line; briefs are written short
        if d.textlength(line, font=F_BRIEF) > bw2:
            while line and d.textlength(line + "…", font=F_BRIEF) > bw2:
                line = line[:-1]
            line += "…"
        d.text((x0, y0), line, font=F_BRIEF, fill=INK)
    y += rows * 12 + 6

    # 8 dotted world map with numbered pins
    d.text((mx, y), "WHERE IT HAPPENED", font=F_SEC, fill=INK)
    y += 18
    map_y0, map_y1 = y, y + 80
    d.rectangle([mx, map_y0, W - mx, map_y1], fill=OCEAN, outline=RULE, width=1)

    def proj(lon, lat):
        x = mx + (lon + 170.0) / 360.0 * cw
        yy = map_y0 + (75.0 - lat) / 130.0 * (map_y1 - map_y0)
        return (x, yy)

    step = 7
    gx = mx + 4
    while gx < W - mx - 2:
        gy = map_y0 + 4
        while gy < map_y1 - 2:
            lon = (gx - mx) / cw * 360.0 - 170.0
            lat = 75.0 - (gy - map_y0) / (map_y1 - map_y0) * 130.0
            if any(point_in_poly(lon, lat, p) for p in CONTINENTS):
                d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=LAND_DOT)
            gy += step
        gx += step
    for num, region, head, fact, src, sure, icon, lon, lat in HEROES + ILLUSTRATED:
        x, yy = proj(lon, lat)
        # nudge colliding pins apart (New York/Washington, Shanghai/Seoul)
        if num == 11:
            x, yy = x + 16, yy - 12
        elif num == 10:
            x, yy = x + 10, yy - 8
        d.ellipse([x - 8, yy - 8, x + 8, yy + 8], fill=RED, outline=(255, 255, 255))
        lbl = str(num)
        d.text((x - d.textlength(lbl, font=F_PIN) / 2, yy - 6), lbl,
               font=F_PIN, fill=(255, 255, 255))
    y = map_y1 + 8

    # 9 + 10 footer: DATE CHECK + HOW SURE
    d.rectangle([mx, y, W - mx, y + 50], fill=LIGHT, outline=RULE, width=1)
    for j, ln in enumerate(wrap(d, DATE_CHECK, F_FOOT, cw - 16)):
        d.text((mx + 8, y + 4 + j * 12), ln, font=F_FOOT, fill=INK)
    y += 56
    for j, ln in enumerate(wrap(d, HOW_SURE, F_FOOT, cw)):
        d.text((mx, y + j * 12), ln, font=F_FOOT, fill=GREY)
    y += len(wrap(d, HOW_SURE, F_FOOT, cw)) * 12 + 2
    print("layout bottom y =", y, "of", H)
    if y > H:
        raise SystemExit("layout overflow")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
