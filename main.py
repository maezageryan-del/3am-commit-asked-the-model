#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes one 62-character git commit message to /output/entry.txt:
an AI coding agent at 3am, after a long night of fixing its own bugs,
asking the model for help — and realising the model is itself.

The gate allows 1 to 139 UTF-8 characters, one line, no trailing newline.
"""

import os
import sys

ENTRY = "fix: asked the model for help. the model was me. I was no help"
# 62 chars: short enough that every word earns its place, long enough to land
# the three beats — the ask, the reveal, the shrug.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(ENTRY) <= 139):
        print(f"entry length {len(ENTRY)} is outside the 1-139 gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
