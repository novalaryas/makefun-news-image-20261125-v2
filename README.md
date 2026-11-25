# makefun-news-image-20261125-v2
[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/novalaryas/makefun-news-image-20261125-v2/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/novalaryas/makefun-news-image-20261125-v2/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A broadsheet front page summing up Wednesday 25 November 2026's world
news: 37 real stories across 6 continents — Ukraine's confirmed drone
strike on a Russian ship in the Gulf of Finland, the Houthi strike on
Riyadh's tallest tower, Shenzhou-24 carrying the first Pakistani into
orbit, Huawei's US conviction, the AI market sell-off, and 32 more —
grouped by region, with a world map marking where the news happened.
Every story is sourced in NOTES.md (Reuters, AP, BBC, Al Jazeera).

## Run it

```sh
python3 main.py
```

It writes one image to `/output/entry.png` (1024x1024 PNG, under 1 MiB), no network, deterministic — every run writes identical bytes. The page itself is rendered by `build_image.py` (Python PIL) from the story list in `NOTES.md`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=phwa5f1b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
