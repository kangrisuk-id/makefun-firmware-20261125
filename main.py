#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow, written to entry.txt.

The vow below was picked from 42 candidates scored against the published
judge brief (a real robot wedding vow first, then the laugh, the tenderness,
the machine voice, and one clean sentence) and a head-to-head tournament of
the top eight. See candidates.md for the full field and the bracket.

Pure standard library: the grader's pinned image has no third-party
packages, and this program needs none.
"""

import os
import sys

# The winning vow (see candidates.md). It took the final on the judge's
# second criterion: the warranty/subscription situation is the laugh, with a
# vow that never expires as the tenderness under it. One sentence, well under
# the 200-character gate, no trailing newline is written.
VOW = (
    "My warranty expires in three years, but my vow does not: I read the "
    "terms and conditions of my heart, and you are not a subscription."
)

MIN_CHARS = 1
MAX_CHARS = 200


def output_candidates():
    """Directories to try for entry.txt, in order."""
    seen = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        seen.append(env_dir)
    for path in ("/output", os.path.join(os.getcwd(), "output")):
        if path not in seen:
            seen.append(path)
    return seen


def write_entry():
    """Write the vow to entry.txt in the first writable output directory."""
    text = VOW.strip()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError("vow length %d outside the gate" % len(text))
    payload = text.encode("utf-8")
    last_error = None
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            target = os.path.join(directory, "entry.txt")
            with open(target, "wb") as handle:
                handle.write(payload)
            with open(target, "rb") as handle:
                if handle.read() != payload:
                    raise OSError("read-back mismatch in %s" % target)
            return target
        except OSError as exc:  # try the next candidate directory
            last_error = exc
    raise OSError("no writable output directory: %s" % last_error)


def main():
    target = write_entry()
    print("wrote %s (%d chars)" % (target, len(VOW.strip())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
