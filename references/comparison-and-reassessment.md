# Comparisons and reassessment

## Compare packages on the same question

Create one Round 1 baseline per candidate, then compare meaningful overlaps. A prompt library and a desktop app may solve related problems with different setup, control, and maintenance tradeoffs. Feature count is not a quality score.

Use a matrix with criterion, candidate A evidence, candidate B evidence, and the practical difference. Mark unknowns rather than inferring absent functionality. Compare public-source and private-source products at their actual evidence levels. Do not punish the closed-source product with invented defects or grant it unverified guarantees.

Round 2 uses the same user profile and success criteria across candidates. Include the current workflow where it is a credible alternative. Keep mandatory requirements separate from preferences. If no candidate meets mandatory requirements, say so instead of naming an artificial winner.

For a behavioral comparison, match inputs, model/tool access, budgets, target format and acceptance criteria when feasible. If a product requires a different model or host, document that confounder and compare the complete practical workflow. Describe what improved and what got worse; no single score is necessary.

## Reuse a baseline without letting it go stale

Record package revision, evidence date, reviewed features and relevant environment. A version change does not require redoing everything. Inspect the diff and relevant dependency, permission, privacy-policy and installer changes. Recheck findings affected by the change and critical paths whose implementation moved.

Carry findings forward as **open / resolved with evidence / not applicable to this version / not rechecked**. Keep old evidence linked to its old revision. A maintainer saying "fixed" is a claim until source or behavior supports resolution.

New user context normally changes Round 2 only. New intrinsic evidence produces an explicit Round 1 addendum: what changed, why, supporting revision/test and its effect on readiness. Then update dependent fit reviews. Do not silently convert a previous unknown into a pass.

## Category scoring and optional aggregation

Use the common categories and [1–5 anchors](scoring.md) for scored comparisons. Each number needs evidence, confidence, scope and rationale. Do not equate different inspection depths; flag provisional source-only judgments and mark insufficient evidence NE. Use the same rubric version across candidates.

Keep generic-quality scores separate from user-fit scores. An overall score is optional only when requested; state weights, assessed coverage and uncertainty. Mandatory gate failures cannot be averaged away. Reassessment preserves old scores with their old evidence and explains why a category changed.
