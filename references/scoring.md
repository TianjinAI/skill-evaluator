# Anchored category scoring: 1–5

Use a category scorecard by default in standard/deep reviews and whenever requested. Screening can be qualitative unless scores are requested. Score the reviewed revision and scope, not the author's reputation. Scores are **ordinal expert assessments**, not measurements, calibrated probabilities, or security certifications.

## Common scale

| Score | Meaning |
|---|---|
| 1 — Poor | Materially undermines the stated purpose or fails a central requirement in the assessed scope |
| 2 — Weak | Useful elements exist, but substantial gaps or limitations require remediation |
| 3 — Adequate | Coherent and sufficient for the assessed scope, with meaningful limitations |
| 4 — Strong | Well-designed/supported across the relevant cases; remaining weaknesses are limited and explicit |
| 5 — Excellent | Exceptionally convincing for the assessed scope, with clear boundaries and unusually strong supporting evidence |

Use whole numbers only. **NE (not enough evidence)** is not 1 or 3. **NA (not applicable)** requires a reason. A core category cannot be dismissed as NA because it was hard to inspect. Missing tests may justify a low evidence-quality score when the inspected package demonstrably lacks support, while functional correctness stays NE. If access itself is missing, evidence quality may also be NE.

Each scored row includes category, score, confidence, evidence label/IDs, scope and a short rationale including the main limitation. Write the confidence cell as **`level — reason`** (e.g. `low — no tests executed, 3 is provisional`); never leave a bare high/medium/low in the cell, because the reason does not survive the reader's glance.

**Score and confidence are independent axes.** Confidence states how sure you are of the number, not how good the number is. "Low score + high confidence" (a directly checkable defect) and "mid score + low confidence" (a defensible source-based judgment without behavioral validation) are both normal and expected. Print this convention as one line adjacent to every scorecard; a bare confidence column is routinely misread as agreeing with the score, and the misreading is the report's fault, not the reader's. Do not provide a score without a defensible anchor match. Missing evidence remains NE; a band must not be used to disguise a guessed midpoint.

**A low-confidence score is not automatically an estimate.** Separate two cases, because they need different wording: a **point estimate with a wide band** (the rubric anchor is defensible on what was read, but untested behavior could move it) versus a **one-sided bound** (evidence proves the value cannot exceed a ceiling, so the printed number is that ceiling, not a middle). Say which one applies.

Where the band is wide enough to matter, print the reasoned interval beside the number as `3 (2–4)` using the renderer's optional `band` field, and give the interval's basis in the confidence cell. The interval must contain the printed score; give any one-sided ceiling in explicit text rather than disguising it as a point estimate. A reasoned interval is a judgment about which adjacent anchors remain reachable — not a confidence interval, a probability, or measured dispersion; never present it as one. Never encode provisional status in font styling (italics, weight, colour): styling is invisible to plain-text export, screen readers and greyscale printing, and it hides the dimension instead of stating it. Prefer a stated interval or an explicit word over a typographic cue.

Label source-only correctness/reliability judgments provisional; do not assign 4–5 to broad runtime reliability, effectiveness or security on untested promises. Conversely, an observed source defect can justify 1–2 without running it.

Design and doctrine can be evaluated from instructions/source. They do not require production metrics to receive a strong score for conceptual quality, but this must not imply that their empirical claims are verified.

## Round 1 categories and anchors

Use these ten major categories, preserving names/definitions across comparisons. Readiness is a conclusion, not an eleventh score. Scores 2 and 4 fall between the neighboring anchors; explain the specific gap or strength.

| Category | 1: poor | 3: adequate | 5: excellent |
|---|---|---|---|
| Purpose and scope | Contradictory/misleading purpose or unusable boundaries | Clear problem, audience and exclusions | Precise scope with realistic success criteria and well-explained boundaries |
| Philosophy and reasoning | Central doctrine is contradictory, unsupported or immune to counterevidence | Coherent assumptions; useful heuristics and acknowledged limits | Clear values and causal logic, well-bounded assumptions, counterexamples and revisability |
| Design and architecture | Central structure undermines the goal; dependencies/state/validation conflict | Responsibilities and data/action flow are coherent | Simple adequate structure, clear boundaries, strong testability and failure containment with justified tradeoffs |
| Instruction quality | Conflicting/unexecutable rules or systematic scope violation | Actionable routing and coherent guidance | Precise, adaptable instructions with sound uncertainty handling and little unnecessary burden |
| Functional correctness | Core path demonstrably produces wrong/incomplete outcomes | Relevant normal cases supported; bounded limitations | Strong representative and edge-case evidence supports the claimed core outputs |
| Reliability and recovery | False success or unsafe replay/irrecoverable state in plausible failures | Relevant failures visible with usable recovery | Strong evidence across consequential failures, interruption and applicable concurrency/retry paths |
| Authority, security and privacy | Demonstrated material unauthorized action/exposure | Relevant authority and data flows understood with appropriate controls | Strong scoped assurance from independent/behavioral evidence across relevant access and data paths |
| Evidence and validation | Major claims contradicted or presented as proven without support | Traceable support for main claims with honest unknowns | Reproducible, representative, independent evidence and transparent limitations |
| Efficiency and maintainability | Disproportionate cost/complexity or fragile unmaintainable setup | Proportionate dependencies/cost, usable updates and clear terms | Convincingly efficient lifecycle, modular evolution, transparent total cost and maintainable portability |
| Incremental value | Demonstrated detriment or no useful contribution versus a relevant baseline | Specific useful contribution supported for scoped tasks | Strong matched evidence of important gains with tradeoffs disclosed |

Licensing remains a separate gate even though license clarity contributes to maintainability. Do not score a popular or feature-rich package highly on incremental value without explaining the comparison. No baseline evidence often means NE, not an assumed 3.

## Round 2 categories

Use the common scale relative to explicit user requirements. A 1 means a central incompatibility; 3 means workable with stated compromises; 5 means an excellent supported match. No user context means NE rather than an invented scorecard.

| Category | Evaluate |
|---|---|
| Task and output fit | Actual tasks, required formats, quality, frequency and outcome thresholds |
| Workflow and philosophy alignment | Autonomy, interaction style, review habits, values and acceptance of the doctrine's tradeoffs |
| Environment compatibility | Host tools, OS/architecture, dependencies, permissions and integration paths |
| Data and authority fit | Approved providers, retention, sensitivity, write scope and reversibility |
| Cost and operating fit | Budget, time, attention, maintenance capacity and switching burden |
| Value over existing alternatives | Evidence of benefit over the current workflow and installed skills, accounting for substitutes, duplication, complementary value, handoff quality, gaps filled, consolidation benefits and migration cost |

Use [installed-skill overlap](installed-skill-overlap.md) as evidence, with coverage limits. Unavailable inventory is an uncertainty, not proof of uniqueness or a score of 1.

Document known configuration matches separately from actual host execution. A declared Mac requirement and an Apple Silicon user support compatibility-in-principle, not a 5 for a proven end-to-end integration.

## Gates, confidence and aggregation

Show applicable gates beside the scorecards. A mandatory failed gate blocks adoption even if other categories score 5. A numerical category score describes graded quality; a gate enforces a requirement for a particular scope. They must not contradict one another without explanation.

Do not collapse the rounds into one number. Overall scores are optional and only produced when requested. If used, state weights, exclusions, assessed coverage and sensitivity to plausible weight changes. NE/NA must never be converted to zero or silently omitted; disclose omitted weight and decline the aggregate when an unresolved mandatory category would make it misleading. Any weighted average is a decision aid over ordinal judgments, not a scientific measurement. Preserve the unaggregated categories and gate outcomes.

## Example, not a benchmark result

For the fictional exporter in [the worked example](../examples/two-users.md), the supplied source supports **reliability/recovery 1/5, high confidence for the helper's control flow**: it skips a slide error and returns success. Whole-application reliability remains NE because another layer might detect incompleteness. General design quality is NE from that excerpt alone; do not infer an entire architecture from one function. This score is a scoped assessment, not an executed test result.
