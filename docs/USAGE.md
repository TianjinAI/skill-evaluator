# Usage guide

## Start with a request, not a questionnaire

Give the agent a repository URL, local folder, skill text, or release page. It should use the skill in your language. Request a depth if you care; otherwise it chooses a scope proportional to your decision.

| Request | Expected behavior |
|---|---|
| "Quickly screen this skill" | Brief Round 1 with evidence limits; no automatic installation |
| "Review the implementation and likely failure modes" | Standard Round 1 with source tracing and useful bounded checks |
| "Assess this for our weekly reporting workflow" | Generic baseline first, then a separate fit review using supplied context |
| "Round 1 only" | Stop at package readiness; no personal verdict |
| "Use last week's baseline for my new environment" | Check baseline applicability, then update Round 2 |
| "Compare these two; test the critical claims" | Independent baselines plus matched comparison within authorized test scope |

"Deep" authorizes more thorough analysis, not installation, real-account writes, spending, or public disclosure beyond the user's actual permission.

## What to provide for Round 2

You do not need every field. The agent should reuse known context and ask only about decision-changing gaps. A useful short description is:

> I make weekly client PDFs from confidential spreadsheets. I use a Windows laptop and an agent with file access but no browser automation. I want one complete draft with minimal questions. Source data must stay with approved providers. Compare this with my current spreadsheet-to-Word workflow.

No passwords, tokens, customer names or actual confidential records are needed to describe these constraints. The agent should label inferred preferences and avoid claiming compatibility until supported.

## Save an auditable review

For larger reviews, the optional helper creates editable files:

```sh
python3 scripts/init_review.py ./example-review --package "Example Package" --revision "v2.4" --rounds both
```

Python 3.10+; standard library only. Destination must not already exist. Paths are chosen by you; the helper performs no network calls and does not run candidate code. It prints the created directory. Round 2 and pilot notes start labeled as private drafts; this label does not encrypt files or set access controls. Do not commit them to a public repository without reviewing their contents.

Fill the evidence ledger with source locators and actual observations. Reference evidence IDs in findings. Remove the draft label only when the review is complete; keep untested areas explicit. The helper does not grade or verify a review.

## Request a scored design review

> Review the underlying philosophy, assumptions and architecture, then score each major category from 1 to 5. Keep confidence and evidence visible; mark categories NE if you cannot assess them.

Use the [design guide](../references/design-and-doctrine.md) and [score anchors](../references/scoring.md). Scores describe the stated inspection scope, not a guarantee of all behavior.

## Read the conclusion correctly

- **Ready for a bounded pilot** is a generic readiness judgment, not a blanket endorsement.
- **Adapt before use** means an identified change is needed; the review does not perform it unless requested.
- **Unknown** means insufficient evidence, not a hidden failure or a pass.
- **Task-validated** applies to a named task and environment, not every claimed feature.

See the [worked example](../examples/two-users.md) for two different decisions from the same baseline. For updates and comparisons, see [reassessment guidance](../references/comparison-and-reassessment.md).
