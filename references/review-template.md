# Review template

Scale detail to the decision. Use two visibly separate rounds; omit Round 2 when it was not requested and context is absent.

## Round 1 — Independent generic review

- Package, canonical source, pinned revision, date, review scope.
- Main purpose, package type, intended audience, features, architecture.
- Underlying thesis, values, assumptions, counterexamples and revisability; architecture and doctrine-to-mechanism mapping.
- Strengths, tradeoffs, plausible alternatives and proposed incremental value.
- Generic category scorecard: score 1–5/NE/NA | confidence | evidence | scope | rationale.
- Findings: severity | confidence/evidence label | trigger | behavior | consequence | evidence location | remedy.
- Distinguish fixable defects, inherent limitations, and author conventions.
- Applicable gates: result, evidence, scope, unresolved question.
- Checks performed and actual results; checks not performed.
- Readiness assessment, supported uses, required remediation, residual unknowns.

## Round 2 — User-specific fit review

- Baseline revision/reference and whether it remains current.
- User profile: explicit needs, known environment, assumptions, critical gaps.
- Requirement → baseline finding/capability → fit consequence → adaptation if any.
- Existing alternatives and incremental value for this user.
- Separate fit scorecard using the six Round 2 categories; include confidence, evidence, scope and rationale.
- Decision: adopt / trial with conditions / adapt before use / skip for this use case.
- Pilot acceptance criteria, actual results if tested, next action, residual uncertainty.

When publishing, separate public baseline from private fit notes. Do not include personal context or copied confidential inputs in a public example.
