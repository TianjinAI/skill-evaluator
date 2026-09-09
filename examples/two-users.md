# Worked example: one baseline, two fit decisions

**Fictional teaching example.** This is not a review of a real product or evidence of model performance. All package properties and user profiles below are supplied facts of the scenario.

## Source packet

Imagine **LocalDeck 0.4**, a Mac-only desktop application for generating presentation drafts. Its documented requirements are Apple Silicon, an installed local model endpoint, and manual review before export. The supplied implementation excerpt for an export helper is:

```python
def export_all(slides, render, save):
    completed = []
    for slide in slides:
        try:
            completed.append(render(slide))
        except ValueError:
            continue
    save(completed)
    return 0
```

The fictional license permits internal use and redistribution. No application binary, telemetry implementation, model performance results or complete rendering engine is supplied.

## Round 1 — Generic baseline R1-A

**Purpose:** produce presentation drafts within the declared Mac/local-model workflow. The OS restriction is a scope limitation, not evidence of a bug. Potential strengths are a focused workflow and editable intermediate drafts; comparative quality is unproven.

**F-01 — High severity, high confidence in the excerpt's control flow; source-supported.** When any slide raises `ValueError`, the helper skips it, saves only the remaining slides, and returns success. A caller relying on that status can accept an incomplete deck. No execution was performed for this example. Remedy: record per-slide outcomes and fail on incompleteness by default, with any intentional partial export explicitly identified.

**Evidence boundary:** this finding is about the supplied helper. Whether the full application detects missing slides elsewhere is unknown. The statement that processing is local is a scenario documentation claim, not independently verified network behavior.

| Gate | Result and scope |
|---|---|
| Export completeness | Fail for the supplied helper contract |
| Runtime | Documented Mac requirements; actual launch unknown |
| Privacy | Unknown: no end-to-end data-flow evidence |
| Licensing | Scenario terms permit the described use; no real license audited |

**Readiness:** remediation needed before relying on complete exports. A disposable draft experiment is possible, but no production readiness or superior design quality is established.

## Round 2 — User A: supervised internal drafts

Explicit context: Apple Silicon laptop, public input material, local-model setup available, weekly internal drafts, manual slide-by-slide review acceptable. Existing workflow is drafting with a general assistant and assembling slides manually.

**Decision: trial with conditions.** The runtime matches the stated requirements, but has not been launched. F-01 remains a defect. Keep inputs disposable, compare expected/actual slides, and do not treat helper success as completeness. Before real client delivery, require the export remedy. Local-model availability does not establish the application's network behavior.

Pilot: generate a short fixed deck using the current workflow and candidate; compare factual preservation, missing slides, revision effort and total time. A failure fixture should verify that a rejected slide is visible to the operator. This is a plan; no runs or improvement claims exist yet.

## Round 2 — User B: unattended Windows publishing

Explicit context: Windows-only environment, overnight unattended production, no budget for another machine, complete export is mandatory.

**Decision: skip for this use case.** The declared platform is incompatible and F-01 conflicts with unattended completeness. Do not ask the user to switch environments just to justify adoption. Consider a supported alternative with a verified completeness gate.

## What stays unchanged

Baseline R1-A and F-01 remain identical for both users. The personal recommendation changes because workflow and environment differ. User A's tolerance for supervised trials does not resolve F-01; User B's Windows requirement does not make Mac support a generic implementation defect.
