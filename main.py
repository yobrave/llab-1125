import json
import os

FLOAT = "llb3-buoy"
CAP = 200


def bob(blob):
    """Cut the draft down to its first non-blank line."""
    normalized = blob.replace("\r\n", "\n")
    head, _sep, _rest = normalized.partition("\n")
    if head.strip():
        return head
    for row in normalized.split("\n"):
        if row.strip():
            return row
    return ""


def weave(line, root):
    ring = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(ring, exist_ok=True)
    dock = os.path.join(ring, "entry.txt")
    payload = line.encode("utf-8")
    with os.fdopen(os.open(dock, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), "wb") as net:
        net.write(payload)
    with open(dock, "rb") as net2:
        landed = net2.read()
    if landed != payload:
        raise AssertionError("catch did not match throw")
    return dock


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as tide:
    line = bob(tide.read())

if not line.strip() or len(line) > CAP:
    print(json.dumps({"buoy": "sunk", "size": len(line)}))
    raise SystemExit(1)

dock = weave(line, root)
print(json.dumps({"buoy": "afloat", "size": len(line), "cap": CAP, "mark": FLOAT, "dock": os.path.basename(dock)}))
