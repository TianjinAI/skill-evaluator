# Design, architecture and underlying doctrine

Use this in Round 1 for a standard/deep review, or whenever the user asks about design rationale or philosophy. In a screening review, summarize available evidence and mark uninspected areas. These are substantive assessments of the package, not merely feasibility checks.

## 1. Reconstruct the doctrine fairly

Explain the strongest reasonable version of what the author believes makes the approach work. Distinguish:

- **Goals/values:** what is optimized (speed, rigor, autonomy, persuasion, consistency), and whose interests count.
- **Empirical claims:** statements about what produces outcomes; these need evidence.
- **Heuristics:** useful shortcuts whose validity depends on context.
- **Normative preferences:** style, interaction, editorial or ethical choices; not scientific facts.
- **Hard constraints:** platform, legal, physical or task requirements with a stated basis.

Find the actual instructions supporting this interpretation. Label inferred philosophy as inferred; do not invent an author's motives or biography. A tool need not declare a grand philosophy to have a sound design.

## 2. Challenge assumptions and causal logic

Ask what must be true for the approach to work, where those assumptions apply, and what counterexample would invalidate them. Do the instructions permit withholding judgment, changing course, consulting evidence, and acknowledging tradeoffs? Do they confuse persona resemblance with expertise, engagement with business value, or descriptive convention with effectiveness?

Identify both the useful insight and the overreach. An opinionated approach can be excellent inside a narrow declared scope. Penalize unsupported universality, contradictions and refusal of counterevidence; do not penalize mere disagreement with the reviewer's values.

## 3. Reconstruct the architecture

Trace input → routing/planning → evidence/tools → state/side effects → validation → output/recovery. For prompt-only skills, these are logical stages, not necessarily software modules. Identify boundaries, dependencies, source of truth, persistent memory, extension points, trust boundaries and who can change policy.

Evaluate why the parts are divided this way: cohesion, coupling, replaceability, observability, testability, reuse, portability, update behavior, and failure containment. Prefer the simplest adequate design; more modules or code are not inherently better. Evaluate architectural clarity even when execution cannot be tested, while labeling runtime claims unknown.

## 4. Trace doctrine into mechanisms

Use a small mapping of principle → implementing instruction/component → expected effect → evidence/counterexample. For example:

| Principle | Mechanism to inspect | Question |
|---|---|---|
| Evidence before prose | Source ledger used by the builder/checker | Is unsupported text actually prevented or only discouraged? |
| Every edit is reversible | Transaction boundary and undo history | Does undo cover external effects and partial failures? |
| Autonomous completion | Router and approval boundaries | Can it continue within scope without inventing authorization? |
| Rigorous critique | Independent checks and evaluator inputs | Can the critic detect errors its own generator tends to make? |

A safeguard described in prose is not an enforced boundary. A stated goal that is not mechanized is an implementation gap, but not every editorial preference requires executable enforcement.

## 5. Evaluate alternatives and tradeoffs

Compare one plausible simpler or differently structured approach when it illuminates the design. Ask what is gained and lost, which failure modes were traded away, and where the chosen approach is a good match. Do not prescribe a rewrite merely because another design is possible.

## 6. Deliver a substantive conclusion

Report the underlying thesis, strongest insight, weakest assumption, architecture strengths, material gaps, and justified improvements. Score philosophy and architecture separately using the scoring rubric. A thoughtful philosophy may be poorly implemented; a solid implementation may faithfully enforce a flawed doctrine.

Round 2 then assesses whether those explicit values and tradeoffs fit this user's needs. Preserve the generic findings; personal value alignment is not a substitute for evidence or a reason to reverse an intrinsic assessment.
