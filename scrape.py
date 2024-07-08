#!/usr/bin/env python
from pathlib import Path
import requests

url_output = """
stigma
static/cup.f896048f24c7.png
static/pad.e16e746971c5.png
menstruation
static/question-mark.341c0791e5e8.jpg
static/red-wood-edit3.6fe2a62a517e.jpg
static/logo-cropped.3ba319a98346.png
about
static/handsphoto.05aa7b6013b8.jpg
static/abstract-red-edit.40b75ae45ac5.jpg
menstruation/professionals
static/tampon.a465340a9d72.png
obstacles
static/freebleedind.21db08dbd36c.png
menstruation/products
static/misc.40ebe04b431f.png
menstruation/extratips

menstruation/basics
"""

urls = [u.strip() for u in url_output.split("\n")]

local_prefix = Path("site/")

for url in urls:
    target_path = local_prefix / Path(url)
    print(f"Target Path: {target_path}")
    if str(url).startswith("static/"):
        target_path.parent.mkdir(parents=True, exist_ok=True)
        output_file = target_path
    else:
        target_path.mkdir(parents=True, exist_ok=True)
        output_file = target_path / Path("index.html")
    print(f"URL -> Output File: {url} -> {output_file}")
    result = requests.get(f"https://talkaboutperiods.com/{url}")

    if result.status_code == 200:
        print(f"Writing to {output_file}")
        output_file.write_bytes(result.content)
    else:
        raise Exception(f"Failed to fetch {url}")
