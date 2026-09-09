# Review templates

Use only the templates needed for the task. Blank fields are prompts, not evidence. Inline reviews do not require files.

- [Round 1](round-1.md): public-safe generic baseline.
- [Round 2](round-2.md): private by default; user-specific fit.
- [Evidence ledger](evidence.csv): one row per supporting item; use the evidence labels defined in SKILL.md.
- [Pilot plan](pilot.md): explicit success criteria and actual results, kept separate.

The initializer copies Round 1 and an empty evidence ledger by default; `--rounds both` adds Round 2 and the pilot template. It does not inspect, fetch, install, or evaluate a candidate. An unfinished template must not be presented as a completed review.
