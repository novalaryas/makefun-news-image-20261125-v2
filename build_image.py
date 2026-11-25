#!/usr/bin/env python3
"""Build the v2 broadsheet front page for Wednesday 25 November 2026.

Renders THE WORLD as a real rendered-text PNG (1024x1024) with PIL:
masthead + full date, a lead story, a schematic world map with story
locations marked, and 36 further stories grouped by region (37 in all),
every one a real event first reported on 25 November 2026.

Run:  python3 build_image.py   -> writes image.png next to this file.
Deterministic: fixed fonts, fixed layout, no timestamps, no randomness.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "image.png")

W, H = 1024, 1024
PAPER = (253, 253, 248)
INK = (18, 18, 18)
GREY = (90, 90, 90)
RED = (158, 24, 24)
DARKRED = (120, 16, 16)
OCEAN = (214, 228, 238)
LAND = (196, 198, 188)
LAND_LINE = (120, 122, 112)
RULE = (40, 40, 40)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(SERIF_B, 62)
F_DATE = font(SANS_B, 16)
F_TAG = font(SANS_B, 12)
F_LEAD_H = font(SANS_B, 17)
F_LEAD_F = font(SANS, 14)
F_MAP_T = font(SANS_B, 12)
F_MAP_L = font(SANS_B, 10)
F_HEAD = font(SANS_B, 12)
F_FACT = font(SANS, 12)
F_RHEAD = font(SANS_B, 13)
F_FOOT = font(SANS, 11)
F_FOOT_B = font(SANS_B, 11)

# ---------------------------------------------------------------- stories
# (region, headline, fact) -- every story first reported 25 Nov 2026.
STORIES = [
    ("EUROPE", "Russian strike on Zaporizhzhia kills 2, wounds 22",
     "attack hits the south-eastern city, officials say."),
    ("EUROPE", "Putin: Ukraine keeps hitting refineries",
     "Kyiv strikes oil refineries despite Trump's requests to stop."),
    ("EUROPE", "Latvia sees a 'tipping point' in 2027",
     "President Rinkevics says the war may turn as Russia's economy worsens."),
    ("EUROPE", "Sarkozy corruption case sent to trial",
     "ex-president and wife Carla Bruni to trial; first hearing 1 April 2027."),
    ("EUROPE", "Sweden PM fails again to form a government",
     "Andersson's bid collapses as the political impasse deepens."),
    ("EUROPE", "Ukraine sank a Russian ship in Libya",
     "Kyiv confirms a drone attack on a Russian vessel in a Libyan port."),
    ("EUROPE", "NATO vows shield against space threat",
     "alliance chief promises protection after reports of Russian nuclear satellites."),
    ("EUROPE", "Norway urges Kyiv to show caution",
     "Oslo, a strong ally, warns Ukraine over Gulf of Finland-style operations."),
    ("MIDDLE EAST", "Houthis hit Riyadh's tallest tower",
     "drone strike wounds 11, the second attack on the tower within days."),
    ("MIDDLE EAST", "Houthis push to 60 km from Aden",
     "Yemen's army says the rebels will not take the temporary capital."),
    ("MIDDLE EAST", "Houthis: 25 dead in Saudi strikes",
     "group says airstrikes hit coaches and trucks in southern Yemen."),
    ("MIDDLE EAST", "Israeli strike kills Hamas security chief",
     "Naim Abu Nahl killed west of Gaza City, AP reports."),
    ("MIDDLE EAST", "Six killed in Israeli strikes across Gaza",
     "Palestinian emergency services report the toll."),
    ("MIDDLE EAST", "Gaza health emergency over meningitis",
     "ministry declares an emergency as cases rise sharply."),
    ("MIDDLE EAST", "Iraq seeks a bigger oil quota",
     "Baghdad wants a higher output estimate before the 2027 OPEC debate."),
    ("ASIA-PACIFIC", "Shenzhou-24 lifts off with a Pakistani aboard",
     "Zeeshan Ali, 40, is the first Pakistani in orbit, first foreigner on Tiangong."),
    ("ASIA-PACIFIC", "Huawei convicted in US trial",
     "firm guilty over Iran business and trade secrets, acquitted of racketeering."),
    ("ASIA-PACIFIC", "China probes Shanghai party boss",
     "Chen Jining investigated, the fourth Politburo member to fall since 2025."),
    ("ASIA-PACIFIC", "Nepal hit by a 5.6 quake",
     "tremor strikes Koshi province near the China border."),
    ("ASIA-PACIFIC", "Asia stocks tumble on tariff threats",
     "Korea falls 5.3%, Taiwan 5.1%, Nikkei 2.9% as the AI rally fizzles."),
    ("ASIA-PACIFIC", "US blacklists an Alibaba unit",
     "Singapore subsidiary listed over alleged Nvidia chip diversion to China."),
    ("ASIA-PACIFIC", "Sooryavanshi, 15, smashes 204 off 53",
     "Indian teen hits a record double century for India A against UAE."),
    ("AMERICAS", "Trump gives Giuliani the Medal of Freedom",
     "ex-New York mayor honoured at the White House."),
    ("AMERICAS", "Turkeys Freedom and Feathers spared",
     "Trump pardons two birds in the Thanksgiving ceremony."),
    ("AMERICAS", "Dow tops 50,000 as Nasdaq falls",
     "Dow closes at 50,018.70 (+0.85%); Nasdaq drops 1.48%, Nvidia slides 5.9%."),
    ("AMERICAS", "Dell doubles sales on AI demand",
     "revenue $54.9bn, $60.2bn in new AI orders; shares rise 4.1% after hours."),
    ("AMERICAS", "US consumer confidence at near two-year high",
     "November reading beats forecasts after the midterm elections."),
    ("AMERICAS", "CIA and spy chief's office breached",
     "cyberattack hits unclassified systems at the CIA and ODNI, source says."),
    ("AMERICAS", "Fort Hood gunman seeks stay of execution",
     "Hasan, who killed 13 in 2009, asks a court to halt next week's execution."),
    ("AMERICAS", "US reports a bird flu death",
     "three human cases in Washington state, one fatal, WHO says."),
    ("AMERICAS", "US to host Copa America again in 2028",
     "tournament returns to the United States for a second straight edition."),
    ("AFRICA", "Libya conflict risks a new flare-up",
     "Ukraine's sinking of a Russian ship exposes a frozen, crowded war."),
    ("AFRICA", "Fighting traps Ebola teams in Congo",
     "heavy fighting near a hospital in Ituri leaves WHO responders cut off."),
    ("AFRICA", "Sudan drones killed 1,600+ this year",
     "UN rights commission counts the toll of drone strikes."),
    ("AFRICA", "MSF halts work in South Sudan county",
     "charity suspends activities in Yei River after an abduction."),
    ("AFRICA", "ECOWAS plans a 2027 single currency",
     "ministers review preparations for the launch."),
]

LEAD_HEAD = "UKRAINE CONFIRMS IT HIT A RUSSIAN SHIP IN THE GULF OF FINLAND"
LEAD_FACT = ("President Zelenskiy says Kyiv was behind Saturday's drone strike; its 16 crew "
             "were evacuated, the ship was towed to St Petersburg.")

# ---------------------------------------------------------------- map
# Coarse continent outlines as (lon, lat) lists, equirectangular.
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
# (lon, lat, label or None, label dx, label dy, anchor 'l'eft/'r'ight)
DOTS = [
    (30, 50, "KYIV", 7, -11, "r"), (25, 60, None, 0, 0, "r"),
    (47, 25, "RIYADH", 7, -11, "r"),
    (34, 31, "GAZA", -7, -5, "l"), (99, 40, "JIUQUAN", 7, -11, "r"),
    (85, 28, "NEPAL", 7, -11, "r"),
    (121, 25, "TAIPEI", 7, -11, "r"), (-77, 39, "WASHINGTON", 7, 7, "r"),
    (-74, 41, "NEW YORK", 7, -11, "r"), (30, 1, "CONGO", 7, 7, "r"),
    (32, 15, "SUDAN", 7, -11, "r"), (2, 49, None, 0, 0, "r"),
    (18, 59, None, 0, 0, "r"),
    (20, 32, None, 0, 0, "r"), (45, 13, None, 0, 0, "r"),
    (121, 31, None, 0, 0, "r"),
    (-88, 42, None, 0, 0, "r"), (73, 33, None, 0, 0, "r"),
    (127, 37, None, 0, 0, "r"),
]


def wrap_mixed(draw, words, width):
    """Wrap [(text, font)] words into lines of (word, font) lists."""
    lines, cur, cur_w = [], [], 0
    space_w = draw.textlength(" ", font=F_FACT)
    for text, fnt in words:
        w = draw.textlength(text, font=fnt)
        add = w if not cur else w + space_w
        if cur and cur_w + add > width:
            lines.append(cur)
            cur, cur_w = [(text, fnt)], w
        else:
            cur.append((text, fnt))
            cur_w += add
    if cur:
        lines.append(cur)
    return lines


def draw_story(draw, x, y, width, headline, fact):
    """Draw one story; return height used."""
    words = [(w, F_HEAD) for w in headline.split()]
    words += [("—", F_FACT)] + [(w, F_FACT) for w in fact.split()]
    lines = wrap_mixed(draw, words, width - 12)
    lh = 14
    draw.rectangle([x, y + 4, x + 5, y + 9], fill=RED)
    for i, line in enumerate(lines):
        cx = x + 12
        for text, fnt in line:
            draw.text((cx, y + i * lh), text, font=fnt, fill=INK)
            cx += draw.textlength(text + " ", font=fnt)
    return len(lines) * lh + 4


def draw_region_header(draw, x, y, width, name, count):
    draw.rectangle([x, y, x + width, y + 19], fill=DARKRED)
    draw.text((x + 8, y + 3), name, font=F_RHEAD, fill=(255, 255, 255))
    tag = "%d STORIES" % count
    tw = draw.textlength(tag, font=F_RHEAD)
    draw.text((x + width - tw - 8, y + 3), tag, font=F_RHEAD, fill=(255, 220, 220))
    return 19 + 6


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    title = "THE WORLD"
    tw = d.textlength(title, font=F_TITLE)
    d.text(((W - tw) / 2, 6), title, font=F_TITLE, fill=INK)
    date_line = "WEDNESDAY 25 NOVEMBER 2026  •  37 STORIES  •  6 CONTINENTS"
    dw = d.textlength(date_line, font=F_DATE)
    d.text(((W - dw) / 2, 74), date_line, font=F_DATE, fill=DARKRED)
    d.line([(20, 96), (W - 20, 96)], fill=RULE, width=2)
    d.line([(20, 100), (W - 20, 100)], fill=RULE, width=1)

    # ---- lead story
    ly = 108
    d.rectangle([20, ly, 28, ly + 58], fill=RED)
    d.text((38, ly), "LEAD", font=F_TAG, fill=RED)
    d.text((38, ly + 15), LEAD_HEAD, font=F_LEAD_H, fill=INK)
    d.text((38, ly + 38), LEAD_FACT, font=F_LEAD_F, fill=INK)
    d.line([(20, ly + 66), (W - 20, ly + 66)], fill=RULE, width=1)

    # ---- map strip
    my = 182
    d.text((20, my), "WHERE THE NEWS HAPPENED  —  25 NOVEMBER 2026",
           font=F_MAP_T, fill=INK)
    mx0, my0, mx1, my1 = 20, my + 20, W - 20, my + 122
    d.rectangle([mx0, my0, mx1, my1], fill=OCEAN, outline=RULE, width=1)

    def proj(lon, lat):
        x = mx0 + (lon + 170.0) / 360.0 * (mx1 - mx0)
        y = my0 + (75.0 - lat) / 130.0 * (my1 - my0)
        return (x, y)

    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_LINE)
    for lon, lat, label, ldx, ldy, anchor in DOTS:
        x, y = proj(lon, lat)
        d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=RED, outline=(255, 255, 255))
        if label:
            tw = d.textlength(label, font=F_MAP_L)
            if anchor == "l":
                lx = max(mx0 + 2, x + ldx - tw)
            else:
                lx = min(x + ldx, mx1 - tw - 2)
            d.text((lx, y + ldy), label, font=F_MAP_L, fill=DARKRED,
                   stroke_width=2, stroke_fill=(255, 255, 255))

    # ---- stories, two columns, region-grouped flow
    regions = []
    for region, head, fact in STORIES:
        if not regions or regions[-1][0] != region:
            regions.append((region, []))
        regions[-1][1].append((head, fact))

    col_x = [20, 522]
    col_w = 482
    top = my + 132
    bottom = 992
    # measure: build a list of blocks (header height, story heights)
    blocks = []
    for region, items in regions:
        counts = len(items)
        blocks.append(("head", region, counts))
        for head, fact in items:
            words = [(w, F_HEAD) for w in head.split()]
            words += [("—", F_FACT)] + [(w, F_FACT) for w in fact.split()]
            lines = wrap_mixed(d, words, col_w - 12)
            blocks.append(("story", head, fact, len(lines) * 14 + 4))

    col = 0
    y = top
    for b in blocks:
        if b[0] == "head":
            hh = 25
            if y + hh + 20 > bottom:  # keep header with stories: next column
                col += 1
                y = top
            if col > 1:
                raise SystemExit("layout overflow: stories do not fit")
            y += draw_region_header(d, col_x[col], y, col_w, b[1], b[2])
        else:
            hh = b[3]
            if y + hh > bottom:
                col += 1
                y = top
                if col > 1:
                    raise SystemExit("layout overflow: stories do not fit")
            y += draw_story(d, col_x[col], y, col_w, b[1], b[2])
    if col != 1:
        print("warning: only one column used; layout has spare room")

    # ---- footer
    d.line([(20, 1000), (W - 20, 1000)], fill=RULE, width=1)
    foot = ("Every story above was first reported on Wednesday 25 November 2026. "
            "Sources: Reuters, AP, BBC, Al Jazeera — full list in this repo's NOTES.md.")
    d.text((20, 1006), foot, font=F_FOOT, fill=GREY)

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
