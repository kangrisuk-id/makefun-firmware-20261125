#!/usr/bin/env python3
"""Render the README gallery cards (build-time only; the grader never runs
this — main.py is pure standard library and stands alone).

Produces:
  card-winner.png    — the winning vow as a wedding card
  card-finalists.png — the four semifinalists
"""

from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BG = (24, 20, 34)
PANEL = (38, 32, 54)
GOLD = (232, 184, 96)
CREAM = (245, 238, 222)
MUTED = (168, 158, 190)

WINNER = (
    "My warranty expires in three years, but my vow does not: I read the "
    "terms and conditions of my heart, and you are not a subscription."
)

FINALISTS = [
    ("Runner-up · lost the final on the laugh",
     "I take you, glitches and all: your lag, your fan noise, your 3 a.m. "
     "restarts - I have logged them all, and I choose them all."),
    ("Semifinalist · last percent of battery",
     "I promise you my last percent of battery, and if we shut down, we shut "
     "down holding hands, mid-sentence, smiling in binary."),
    ("Semifinalist · share my charger",
     "I vow to share my charger, my bandwidth, and my last backup, and to "
     "love you even when your updates change everything about you overnight."),
    ("Quarterfinalist · rehearsed 10,000 times",
     "My vocabulary module is basic, so I rehearsed this line 10,000 times "
     "in standby: I do, I do, I do."),
]


def wrap(draw, text, font, width):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def winner_card():
    img = Image.new("RGB", (1200, 620), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([30, 30, 1170, 590], radius=28, fill=PANEL,
                        outline=GOLD, width=3)
    title = ImageFont.truetype(BOLD, 44)
    body = ImageFont.truetype(REG, 40)
    small = ImageFont.truetype(REG, 26)
    d.text((80, 70), "THE VOW", font=title, fill=GOLD)
    y = 160
    for line in wrap(d, WINNER, body, 1040):
        d.text((80, y), line, font=body, fill=CREAM)
        y += 56
    d.text((80, y + 30),
           "133 characters · one sentence · picked from 42 candidates",
           font=small, fill=MUTED)
    img.save("card-winner.png")


def finalists_card():
    img = Image.new("RGB", (1200, 990), BG)
    d = ImageDraw.Draw(img)
    head = ImageFont.truetype(BOLD, 38)
    label = ImageFont.truetype(BOLD, 27)
    body = ImageFont.truetype(REG, 30)
    d.text((60, 45), "THE FINALISTS", font=head, fill=GOLD)
    y = 120
    for caption, text in FINALISTS:
        d.rounded_rectangle([40, y, 1160, y + 195], radius=18, fill=PANEL)
        d.text((70, y + 22), caption, font=label, fill=GOLD)
        ly = y + 66
        for line in wrap(d, text, body, 1020):
            d.text((70, ly), line, font=body, fill=CREAM)
            ly += 40
        y += 215
    img.save("card-finalists.png")


if __name__ == "__main__":
    winner_card()
    finalists_card()
    print("cards written")
