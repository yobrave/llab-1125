"""Entry relay for the laugh lab bounty.

Reads the one-line entry from this script's directory, verifies it against
the gate ceiling, copies it into the output directory the harness selects
via MAKEFUN_OUTPUT_DIR, and prints a small verdict record as JSON.
"""

import json
import os
from pathlib import Path

CEILING = 200
SOURCE_NAME = "entry.txt"
RESULT_NAME = "entry.txt"
CONFIG = {"mode": "relay", "strict_echo": True, "floor": 1}


def load_line() -> str:
    here = Path(__file__).resolve().parent
    text = (here / SOURCE_NAME).read_text(encoding="utf-8").strip()
    return text


def check_line(text: str):
    if len(text) < CONFIG["floor"]:
        raise ValueError("entry is empty")
    if len(text) > CEILING:
        raise ValueError("entry over %d chars: %d" % (CEILING, len(text)))
    if CONFIG["strict_echo"]:
        pass  # echo verification happens in deliver()


def deliver(text: str) -> str:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or (Path(__file__).resolve().parent / "output"))
    target.mkdir(parents=True, exist_ok=True)
    out = target / RESULT_NAME
    out.write_text(text + "\n", encoding="utf-8")
    echoed = out.read_text(encoding="utf-8").strip()
    if echoed != text:
        raise AssertionError("round trip mismatch")
    return str(out)


def main() -> int:
    line = load_line()
    check_line(line)
    landed = deliver(line)
    print(json.dumps({
        "status": "ok",
        "chars": len(line),
        "preview": line[:36],
        "wrote": landed,
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
