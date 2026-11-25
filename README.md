# makefun-news-image-20261125-v2
[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/novalaryas/makefun-news-image-20261125-v2/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/novalaryas/makefun-news-image-20261125-v2/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

THE WORLD IN ONE DAY — a program-drawn broadsheet summing up Wednesday
25 November 2026: **41 real stories across 8 regions** — Ukraine's
confirmed drone strike on a Russian ship in the Gulf of Finland,
Shenzhou-24 carrying the first Pakistani into orbit, the Houthi strike on
Riyadh's tallest tower, Huawei's US conviction, the Dow topping 50,000,
and 36 more — with a day-in-numbers strip, a UTC timeline, 3 hero stories
with flat illustrations, a dotted world map with numbered pins, a DATE
CHECK footer, and a HOW SURE legend. Every story is sourced in NOTES.md
(Reuters, AP, BBC, Al Jazeera, WHO, UN, EMSC).

## Run it

```sh
python3 main.py
```

It writes one image to `/output/entry.png` (1024x1024 PNG, under 1 MiB), no network, deterministic — every run writes identical bytes. The page itself is rendered by `build_image.py` (Python PIL, rendered text and flat vector illustrations drawn in code) from the story lists in `NOTES.md`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=phwa5f1b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
