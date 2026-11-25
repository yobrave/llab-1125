"""Laugh lab mixer: pours the one-liner, spins it, decants into the output flask."""
STAMP = "onebug-11251142-llb3"
import json
import os
import shutil
from pathlib import Path

LAB = Path(__file__).resolve().parent
FLASK_MAX = 200
SAMPLE = ("My smart fridge started its own grocery list, "
          "which is how I learned my appliance has quietly decided I have given up.")


def spin(text):
    drop = text.strip()
    return {"poured": bool(drop) and len(drop) <= FLASK_MAX, "stamp": STAMP, "drops": len(drop)}


def decant():
    vial = LAB / "entry.txt"
    reading = spin(vial.read_text(encoding="utf-8"))
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and reading["poured"]:
        Path(bay).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(vial, Path(bay) / "entry.txt")
    print(json.dumps(reading))


if __name__ == "__main__":
    decant()
