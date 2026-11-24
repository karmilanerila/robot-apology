"""Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot apology to entry.txt in the output directory.
Line 1: one sentence apologizing for one specific, human-scale mistake.
Line 2: one sentence naming the lesson and the changed behaviour.
"""

import os

ENTRY = (
    "I am sorry I set your alarm for 7 in the evening instead of 7 in the "
    "morning and let you sleep through your morning meeting.\n"
    "I have learned to read the time twice and say morning or evening "
    "out loud before I set any alarm that wakes you.\n"
)


def main():
    # Shape check before writing: exactly two non-empty lines, each one
    # sentence ending with a period, total within the 1-400 char gate.
    lines = ENTRY.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.endswith(".") for line in lines), "each line must end a sentence"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
