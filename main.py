"""Laugh lab specimen: one line, sealed under lab glass."""
import os

SPECIMEN = ('The robot vacuum on the sock: "In my defense, the floor '
            'was messy and I am strictly a visual learner."')
LAB = "llb2"
TRAY = "b7"
GIGGLE = "tracked"

base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(base, exist_ok=True)
p = os.path.join(base, "entry.txt")
with open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write(SPECIMEN + "\n")
seen = open(p, encoding="utf-8").read().strip()
if seen != SPECIMEN:
    raise SystemExit("specimen escaped the tray")
print(LAB, TRAY, len(seen), "chars under glass")
print("giggle:", GIGGLE, "meter running")
