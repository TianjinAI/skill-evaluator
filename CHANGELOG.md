# Changelog

## 1.4.3 — Clearer reports and ecosystem assessment

- Retain the published Round 2 ecosystem suitability and synergy assessment across instructions, rubrics, templates and examples.
- Integrate the unreleased 1.4.1–1.4.2 changes below: optional reasoned score bands, explicit confidence explanations, structured prose and scorecard notes.
- Preserve negative numbers and literal punctuation in prose; require score bands to contain their point score. Missing evidence remains NE, never a guessed midpoint.
- Synchronize English/Chinese version information and the embedded Chinese README; exclude macOS metadata from release archives.
- 26 local tests passed. Contributor-reported visual checks are distinguished from independent validation.

## 1.4.2 — Readable prose, not formatted walls

- Render authored prose as structured lines: newline-driven breaks, bullet list lines, subordinate lines, block labels and inline code. Narrow escaping-preserving contract; no heading, link or raw-HTML pass-through, so markup cannot be smuggled through prose fields.
- Add an optional `scorecard_note` so the score/confidence convention sits with the table it explains instead of only in the round summary.
- Reject a round title that repeats its own `Round N` prefix, which rendered as "Round 1 · Round 1 · …".
- Record the distinction between styling and structure: the same undifferentiated paragraph with bold added is still unreadable. Sections must lead with the conclusion and must not restate the round verdict. Applied to the template, HTML delivery contract and completion check.
- Caught by a user reading a delivered report; no scoring anchors or category definitions changed.

## 1.4.1 — Confidence is not the score

- Require every confidence cell to render as `level — reason`; a bare high/medium/low fails the completion check.
- State the score/confidence convention next to each scorecard: confidence is certainty in the number, not the number's magnitude. A reader who saw 2/high and 3/low as contradictions was reading a column the report left ambiguous.
- Add an optional `band` field to the renderer, printed beside the point score as `3 (2–4)`, so a soft number is legible in plain text. Bands are validated (ascending 1–5, numeric scores only) and are documented as a reasoned reachable-anchor interval, not a confidence interval.
- Separate "point estimate with a wide band" from "one-sided bound" in the scoring guidance, and reject font styling (italics, weight, colour) as a provisional marker because it does not survive plain-text export, screen readers or greyscale printing.
- Applied to the scoring rubric, review template, completion check and HTML delivery contract. No scoring anchors or category definitions changed.

## 1.4.0 — Upfront intake, HTML and evidence calibration

- Gather necessary context before findings; deliver selected rounds together without routine mid-review questionnaires.
- Default substantial reviews to offline HTML; add an escaped-text renderer with separate generic/private exports and score validation.
- Tighten primary-source verification, inspection coverage, preference provenance and potential-versus-observed overlap claims.
- Add a completion check for scorecards, acceptance matrices, design/doctrine substance and proportionate verdicts.
- Incorporate lessons from a user-provided WorkBuddy run without publishing its private transcript or inventory. Revised WorkBuddy behavior remains to be retested.

## 1.3.0 — Suitability testing and installed-skill overlap

- Clarified Round 1 as generic screening/assessment and Round 2 as user-specific suitability testing.
- Added scoped, metadata-first read-only inventory and overlap/conflict analysis.
- Added environment/requirement check matrices and assessed-only versus task-validated status.
- Preserved six fit categories; overlap informs value, workflow and compatibility instead of becoming a duplicate penalty.
- Updated templates, privacy guidance, bilingual onboarding and prospective evaluation cases. No machine-wide scanner or automatic skill mutations added.

## 1.2.0 — Design, doctrine and category scores

- Added explicit philosophy/doctrine assessment and architecture/tradeoff review.
- Added anchored whole-number 1–5 scores across ten generic categories and six fit categories.
- Scores carry confidence, evidence, scope and rationale; NE/NA preserve uncertainty.
- Updated entrypoint, rubrics, templates and bilingual onboarding. Mandatory gates remain separate; no default aggregate score.

## 1.1.0 — Public package expansion

- Expanded English README and added a Chinese introduction.
- Added installation/update/removal and usage guides.
- Added explicit review depths, evidence practice, severity/confidence guidance, comparisons and reassessment rules.
- Added reusable Round 1/Round 2 templates, evidence ledger and pilot worksheet.
- Added a fictional example showing two different fit decisions from one unchanged generic baseline.
- Added an optional standard-library review initializer with overwrite protection and tests.
- Added CI, contribution guidance, privacy/security documentation and a behavioral evaluation protocol.
- Kept the original two-round design, automatic discovery and evidence limits. No live cross-agent effectiveness claim is added.

## 1.0.0

Initial two-round skill: generic package assessment plus user-specific fit review, category checks and review template.
