#!/usr/bin/env python3
"""make.fun news-image-20261125 v2 entry.

Writes "THE WORLD", a broadsheet front page summing up
Wednesday 25 November 2026: a lead story, a schematic world map with
the day's story locations, and 37 real stories grouped by region.

The page is rendered by build_image.py (PIL) and shipped in this
repository as image.png. This program only copies that file,
byte for byte, to the output path, so it is deterministic and
offline: no network, no randomness, no timestamps, no third-party
imports -- standard library only. Two runs write identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.png")


def run() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SOURCE):
        print("error: image.png missing from repository", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, out_path)
    n = os.path.getsize(out_path)
    if n != os.path.getsize(SOURCE):
        print("error: copied size mismatch", file=sys.stderr)
        return 1
    # The copy is byte-for-byte, so the output hash always matches image.png.
    print("wrote %s (%d bytes, 1024x1024 PNG)" % (out_path, n))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
