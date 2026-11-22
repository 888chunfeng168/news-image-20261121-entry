# news-image-20261121-entry

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/888chunfeng168/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/888chunfeng168/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper front page — "The World in One Day" — summing up Saturday 21 November 2026: the Shenzhen peace pact, the Hague genocide verdict, the AI market sell-off and the strikes on Kryvyi Rih, with short items on Mexico, COP31 and Mercury. The four illustrations are quadrants of an original editorial artwork generated for this entry; compose.py renders every word as crisp text so the page stays legible at any size.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ddg3n73c&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

## About the image

`entry.png` (1024×1024, under 1 MiB) covers the day's most consequential
news, each story verified against reporting from AP, Reuters, the NYT and
the BBC:

- **Shenzhen summit** — Trump, Xi and Putin meet and sign a four-point
  peace declaration, one that says nothing about Ukraine.
- **The Hague** — the World Court finds Myanmar responsible for genocide
  against the Rohingya, a historic first.
- **Markets** — an AI sell-off rattles world markets: the S&P 500 falls
  3.7%, Japan's Nikkei 5.1%.
- **Ukraine** — a Russian missile kills two and wounds 60 in Kryvyi Rih;
  another lands in Poland during NATO drills.

Short items: Mexico captures FBI most-wanted cartel boss "El Chapo Isidro"
in Sinaloa; COP31 in Antalya runs past its deadline over fossil fuels;
BepiColombo reaches Mercury orbit after an eight-year journey.

## Files

- `entry.png` — the submitted image.
- `main.ts` — the competition program; copies `entry.png` to the output
  directory. Running it twice writes identical bytes.
- `compose.py` — builds `entry.png` from `lead-art.png` (`python3 compose.py`).
- `lead-art.png` — the original four-panel illustration made for this entry.
- `.makefun/owner.json` — proves the repository belongs to the entrant.
