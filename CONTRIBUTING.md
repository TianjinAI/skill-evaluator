# Contributing

Useful contributions improve decisions, not just the length of the checklist. Open an issue or pull request with the task, current behavior, proposed improvement and evidence. Use sanitized or synthetic examples; do not include private review notes, access tokens or customer material.

For instruction changes, show which realistic scenario improves and whether another scenario regresses. Preserve the separation between generic package findings and personal fit. Avoid encoding one author's style or one host's capabilities as a universal requirement.

For scripts, add tests of meaningful behavior or invariants and run:

```sh
python3 -m unittest discover -s tests -v
```

Package tests cover filesystem behavior and documentation links; they do not establish model compliance. Use the [evaluation protocol](evals/README.md) for behavioral changes. Record planned versus actual runs honestly.

Update VERSION and CHANGELOG when preparing a release, keep relative links valid, and preserve the MIT license. Do not copy third-party skill text into examples without appropriate rights and attribution. Public documentation should be understandable without private conversation history.
