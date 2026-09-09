# Round 1: Independent generic review

Question: Does the package credibly deliver its stated purpose, and what are its intrinsic strengths, defects, limitations, and unresolved claims?

| Dimension | Inspect |
|---|---|
| Purpose and boundaries | Intended audience, triggers, promised outputs, explicit exclusions; skill versus library versus application |
| Incremental capability | What is added beyond an ordinary capable agent with comparable tools? Without matched evidence, describe the proposed advantage as unproven. |
| Features and architecture | Inputs, tools, executable entrypoints, data destinations, state, dependencies, outputs, transitive resources |
| Instruction quality | Coherence, routing precision, scope control, uncertainty, unsupported axioms, forced judgment, author preferences presented as universal truths |
| Functional correctness | Trace a normal task and consequential failure; compare claims with real postconditions and output completeness |
| Reliability and recovery | Partial success, retries after uncertain outcomes, stale state, concurrency, rollback, interruption, persistent changes |
| Authority and privacy | Read/write power, credential handling, outbound content, telemetry defaults, optional versus mandatory channels, enforcement outside the model |
| Evidence quality | Reproducible fixtures, actual results, source provenance, held-out cases, limitations; separate package checks from behavioral tests |
| Operations and maintenance | Runtime portability, install/update behavior, model/API cost, latency, attention demanded, maintenance burden, license and distribution rights |
| Readiness and boundaries | Applicable gates, necessary remedies, unresolved evidence, audiences/tasks supported by the inspected evidence |

Procedure:
1. Identify the canonical package and pin the inspected revision. If a link concatenates multiple repositories, split only when unambiguous.
2. Inspect the smallest sufficient set of documentation, entrypoints, implementations, and tests. Trace optional capabilities separately when authority or cost changes.
3. Compare advertised behavior with code. Check success signaling, fallback paths, and how the package handles inadequate evidence.
4. Run safe, bounded checks where they can change the conclusion. Capture actual input/result. Do not turn a static review into a security audit claim.
5. Produce findings and a readiness assessment. Distinguish required fixes from optional improvements. State what the review could not establish.

Generic review can describe an onerous workflow (e.g. three mandatory variants) and its general cost. Whether that workflow conflicts with THIS user's preference belongs only in Round 2. Avoid defaulting to the reviewer's current OS, model, available tools, budget, or language as a universal requirement.

If new evidence in Round 2 reveals an intrinsic bug, issue a versioned addendum to Round 1 with its evidence. Do not quietly rewrite the earlier baseline to support a preferred outcome.
