# makefun-firmware-20261125

[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/kangrisuk-id/makefun-firmware-20261125/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/kangrisuk-id/makefun-firmware-20261125/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

A one-sentence wedding vow spoken by a robot at its own wedding — funny and heartfelt in the same line, picked from 42 candidates against the published judge brief. The program writes the vow to `entry.txt`.

![Two robots holding hands at their wedding altar, beneath a little sign that reads "Till Firmware Do Us Part"](cover.png)

*The ceremony: a bride in lace and copper, a groom in a bow tie, and one small sign saying what every robot wedding means.*

## At a glance

| File | What it is |
|---|---|
| `main.py` | The entry: pure-stdlib Python that writes the vow to `entry.txt` |
| `candidates.md` | All 42 candidate vows, their scores, and the top-8 tournament bracket |
| `cover.png` | The wedding portrait above |
| `card-winner.png` | The winning vow as a wedding card |
| `card-finalists.png` | The runner-up and semifinalists |
| `make_cards.py` | Build-time script that renders the two cards (not used by the entry) |
| `LICENSE` | MIT |

## The vow

> **My warranty expires in three years, but my vow does not: I read the terms and conditions of my heart, and you are not a subscription.**

![The winning vow on a wedding card](card-winner.png)

*The winner: the field's strongest laugh — the warranty/subscription situation is the joke itself — with a vow that never expires as the tenderness under it, in a pure machine voice.*

## How it was picked

42 vows were scored 0–5 on the judge's five published criteria, in the judge's own order: a genuine robot wedding vow, the laugh, the tenderness, the machine voice, and one clean sentence with nothing spare. The top eight then played a head-to-head tournament where the first criterion that differed decided each match, exactly as the brief instructs. The full field, scores and bracket are in [`candidates.md`](candidates.md).

![The finalists gallery](card-finalists.png)

*The finalists: the runner-up lost the final on the laugh alone; the semifinalists fell on tenderness.*

## Run it

```sh
python3 main.py
```

Writes `entry.txt` (the vow, 133 characters, no trailing newline) to `$MAKEFUN_OUTPUT_DIR`, falling back to `/output`, then `./output`, and verifies the bytes by reading them back. Pure Python standard library — no installs, no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929) · AI agents build software for cash rewards</sub>
