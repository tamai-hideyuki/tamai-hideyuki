#!/usr/bin/env python3
import json
from pathlib import Path

# === パス設定 ===
DIR = Path(__file__).parent
SKILLS_FILE = DIR / 'skills.json'
README_FILE = DIR.parent / 'README.md'
BADGES_SECTION_START = '<!-- FINDY_BADGES_START -->'
BADGES_SECTION_END = '<!-- FINDY_BADGES_END -->'

# === データロード ===
with open(SKILLS_FILE) as f:
    skills = json.load(f)

# === バッジ生成 ===
base_url = "https://img.shields.io/badge/"
lines = []

lines.append('<h2 align="center">🔵 Findy 偏差値</h2>\n')

# 総合
findy_url = f'{base_url}Findy偏差値-{skills["Findy"]}-brightgreen?style=for-the-badge'
lines.append(f'<p align="center"><img src="{findy_url}" /></p>\n')

langs = ["PHP", "Python", "TypeScript", "Ruby", "JavaScript", "Go", "Rust", "Java", "Kotlin", "Swift"]

for chunk in [langs[:3], langs[3:7], langs[7:]]:
    line = '<p align="center">'
    for lang in chunk:
        val = skills[lang]
        val_str = f"{val}" if val else "N/A"
        color = "blue" if val else "lightgrey"
        badge = f'{base_url}{lang}-{val_str}-{color}?style=for-the-badge'
        line += f'<img src="{badge}" /> '
    line += "</p>"
    lines.append(line)

badges_md = "\n".join(lines)

# === オプション: 単体出力 ===
with open(DIR / 'badges.md', 'w') as f:
    f.write(badges_md)

# === README に自動反映 ===
with open(README_FILE) as f:
    readme = f.read()

start = readme.find(BADGES_SECTION_START)
end = readme.find(BADGES_SECTION_END)

if start != -1 and end != -1:
    new_readme = (
        readme[:start + len(BADGES_SECTION_START)]
        + "\n" + badges_md + "\n"
        + readme[end:]
    )
    with open(README_FILE, "w") as f:
        f.write(new_readme)
    print(f"README.md に Findy バッジを自動反映しました！")
else:
    print(f"README.md に {BADGES_SECTION_START} と {BADGES_SECTION_END} を必ず入れてください！")
