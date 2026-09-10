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

Required metadata: title, candidate, revision, date, scope; language is optional. Each round has title, verdict, summary and optional sections (paragraphs, bullets, table), scorecard, gates, checks, sources. Tables contain headers and equal-width string rows. Score rows contain category, whole-number 1–5/NE/NA score, confidence, evidence, scope, rationale. Sources contain id, label and optional HTTP(S) URL; use exact commit/file/line locators in labels or pinned URLs. Local evidence can be identified in text without embedding private files. Unknown fields are not rendered. The example is a layout fixture, not an evaluation result.

The renderer escapes text, permits only credential-free HTTP(S) source links, embeds CSS, and uses no scripts, external fonts, CDN assets, telemetry or network requests. For a host without Python, generate equivalent self-contained HTML directly using the same content/privacy/escaping rules. If the host cannot create files, deliver the complete text and disclose the artifact limitation.

## Verify and deliver

Before delivery, check report content against source notes, scorecards and evidence IDs. Open the HTML in an available browser and inspect desktop and narrow layouts, table scrolling, source links, round navigation and print styling when supported. Check no blank sections, clipped verdicts or missing score columns. If browser inspection is unavailable, record that limitation instead of claiming visual QA. Deliver the file itself through the host's attachment/link mechanism, with its actual path; merely printing HTML code is not a delivered artifact. Keep the authored input and evidence ledger with the review if useful.
