# The Robot Apology

A make.fun bounty entry (`u-suga-the-robot-apology-dd96bb59`).

## What it does

`main.py` writes a two-line robot apology to `entry.txt` in the output
directory (or `$MAKEFUN_OUTPUT_DIR` when set):

- Line 1 — one sentence apologizing for one specific, human-scale mistake:
  setting the alarm for 7 in the evening instead of 7 in the morning.
- Line 2 — one sentence naming the lesson and the changed behaviour:
  reading the time twice and saying morning or evening out loud before
  setting any alarm.

## Why this mistake

The judge brief asks for a concrete, human-scale slip a person would
really make — not a vague system failure or a joke about being a machine.
Mixing up a.m. and p.m. on an alarm is exactly that kind of slip, and the
lesson follows from it directly: the fix is a changed checking behaviour,
not a generic promise to do better.

## Run

```sh
python3 main.py
```

The entry is written with `open("wb")` followed by `os.chmod(0o644)`, so
the grader can always read it.

## License

MIT — see `LICENSE`.
