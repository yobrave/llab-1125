"""llb6: sock court stenographer. The whole hearing runs inside one context."""
import contextlib
import json
import os
import sys
from pathlib import Path

LEASE = 200
record = {"court": "llb6-sock-r11251422", "accepted": False}


@contextlib.contextmanager
def hearing():
    yield record


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    body = raw.strip()
    record["chars"] = len(body)
    with hearing():
        if body and not body.isspace() and len(body) <= LEASE:
            pen = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
            pen.mkdir(parents=True, exist_ok=True)
            (pen / "entry.txt").write_bytes(body.encode("utf-8"))
            record["accepted"] = True
    print("VERDICT", json.dumps(record))
    return 0 if record["accepted"] else 1


if __name__ == "__main__":
    sys.exit(main())
