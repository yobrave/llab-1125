"""llab-1125: laugh-lab punchline builder with match-case gate."""

import json
import os

BAR = 200


def pull(folder):
    vial = os.path.join(folder, "entry.txt")
    with open(vial, encoding="utf-8") as dropper:
        drop = dropper.read().strip()
    match len(drop):
        case 0:
            raise SystemExit("empty vial")
        case n if n > BAR:
            raise SystemExit("overflow: %d chars" % n)
        case _:
            return drop


def pour(folder, drop):
    basin = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(basin, exist_ok=True)
    drain = os.path.join(basin, "entry.txt")
    with open(drain, "w", encoding="utf-8", newline="\n") as tap:
        tap.write(drop + "\n")
    return drain


folder = os.path.dirname(os.path.abspath(__file__))
drop = pull(folder)
print(json.dumps({"chomp": drop[:44], "drops": len(drop), "giggle": "certified", "drain": pour(folder, drop)}))
