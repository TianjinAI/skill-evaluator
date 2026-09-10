# HTML delivery

Standard/deep reviews default to a standalone local HTML artifact, with a short verdict and file link in chat. Explicit format requests override this default; a quick screening may remain inline. Do not publish a report to the web unless requested. The public status of this skill does not authorize publishing its outputs.

## Content contract

Use the [review structure](review-template.md) and [completion check](intake-and-completion.md). Include metadata and evidence limits near the verdict, substantive strengths/design/doctrine/findings, separate scorecards, gates, sources and actual checks. Round 2 includes the provenance of user requirements, bounded inventory and acceptance matrix. Use the user's language. Lead with the decision and decisive evidence; put detailed findings beneath it. Avoid a wall of repeated conclusions, unexplained radar charts or invented overall scores.

## Generate

The optional standard-library helper consumes authored JSON; it does not evaluate, verify claims, translate or publish anything. See [the fictional JSON example](../examples/report-input.json) for the structure:

```sh
python3 scripts/render_report.py examples/report-input.json /path/to/new/generic.html
python3 scripts/render_report.py examples/report-input.json /path/to/new/private.html --include-round-2
```

Destination parent must exist; existing files and symlinks are refused. Default export contains only metadata and `round1`. `--include-round-2` adds the separate personal section and a private banner. Metadata and Round 1 still require a manual privacy check; the helper cannot identify private text placed in generic fields. A private label is not encryption or access control.

Required metadata: title, candidate, revision, date, scope; language is optional. Each round has title, verdict, summary and optional sections (paragraphs, bullets, table), scorecard, gates, checks, sources. Tables contain headers and equal-width string rows. Score rows contain category, whole-number 1–5/NE/NA score, confidence, evidence, scope, rationale, plus an optional `band` such as `"2–4"` (ascending whole numbers 1–5, containing the point score) printed beside the point score as `3 (2–4)`; a band is invalid for NE/NA. Sources contain id, label and optional HTTP(S) URL; use exact commit/file/line locators in labels or pinned URLs. Local evidence can be identified in text without embedding private files. Unknown fields are not rendered. The example is a layout fixture, not an evaluation result.

The renderer escapes text, permits only credential-free HTTP(S) source links, embeds CSS, and uses no scripts, external fonts, CDN assets, telemetry or network requests. For a host without Python, generate equivalent self-contained HTML directly using the same content/privacy/escaping rules. If the host cannot create files, deliver the complete text and disclose the artifact limitation.

## Prose rendering contract

Review prose is authored as structured notes and must not be delivered as an undifferentiated text wall. The renderer implements exactly this contract, and nothing more:

- A newline starts a new line. One leading bullet (`·`, `-`, `*`, `•`) followed by whitespace marks a list line; negative numbers and literal punctuation are preserved. Two leading full-width spaces mark a subordinate line.
- `**bold**` becomes a block label; `` `code` `` becomes monospace. A line opening with `**Label**: rest` renders the label as a block heading with the rest beside it.
- Everything else is escaped literal text. There is no heading, image, link or raw-HTML pass-through, so a report cannot smuggle markup through prose fields.

A section must not repeat the round's headline finding in flat narrative. Lead each block with its conclusion, keep the evidence beneath it, and mark an optional `scorecard_note` so the score/confidence convention sits with the table it explains.

**Do not confuse a formatting fix with a structural fix.** If a reviewer says prose is hard to read, adding bold or headings to the same undifferentiated paragraph changes the styling, not the message. Fix the structure: state the takeaway first, split the evidence into scannable lines, and delete sentences that only restate the verdict. Styling applied to a wall of text is still a wall.

## Verify and deliver

Before delivery, check report content against source notes, scorecards and evidence IDs. Open the HTML in an available browser and inspect desktop and narrow layouts, table scrolling, source links, round navigation and print styling when supported. Check no blank sections, clipped verdicts, missing score columns, doubly-prefixed round headings (the heading already prints `Round N`, so a title must not repeat it) or prose that renders as one unbroken block. If browser inspection is unavailable, record that limitation instead of claiming visual QA. Deliver the file itself through the host's attachment/link mechanism, with its actual path; merely printing HTML code is not a delivered artifact. Keep the authored input and evidence ledger with the review if useful.
