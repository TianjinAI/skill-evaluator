# Validation and limitations

## Version 1.3.0

- All 10 existing package/helper tests passed; skill frontmatter, local references and whitespace checks passed.
- Manual instruction walkthrough covered available/partial/blocked inventory, same-installation aliases, related-but-distinct skills, potential trigger conflicts, private names and cloud-provider constraints.
- Suitability templates now distinguish requirement checks and real task outcomes from assessed-only conclusions.
- No user installation was scanned for this release. No scanner executable was introduced. Inventory handling and conflict detection are host-mediated procedures and have not been behaviorally validated across agent products; added eval cases are prospective.

## Version 1.2.0

- All 10 existing package/helper tests passed after template and reference changes.
- Skill frontmatter/package validation and whitespace checks passed.
- Manually checked round/category consistency, design/doctrine routing and scorecard templates.
- Manual scoring walkthrough: a source-level false-success path supports a low scoped recovery score, not a whole-application rating; absent architecture evidence remains NE; a private or unavailable implementation is not automatically rated 1; user-environment changes affect fit scores rather than intrinsic scores.
- Added prospective behavioral cases for doctrine review, scoring uncertainty and round separation. These cases have not been run with an independent agent. No inter-rater calibration or measured scoring reliability is claimed.

## Version 1.1.0

Actual local checks:

- 10 automated tests passed on Python 3.14: generic/both-round file sets, Unicode metadata, existing-directory preservation, symlink rejection, bad input, missing templates, cleanup after write failure, CLI failure status, local Markdown links and version format.
- Actual CLI created four drafts in a disposable directory; a repeated call returned status 1 and left every original file unchanged.
- Skill-creator package/frontmatter validation passed; git diff whitespace check passed.
- English/Chinese onboarding, reference routing, templates and the fictional worked example reviewed for consistency with the two-round contract.
- CI runs the automated tests on Python 3.10, 3.12 and 3.13. Check the release commit's GitHub Actions result for remote status.

These tests verify packaging/helper behavior, not evaluation judgment. WorkBuddy-native discovery, live cross-agent effectiveness, independent agent execution of the behavioral cases, and comparative outcome improvements remain untested. The new evals directory describes a protocol, not benchmark results.

## Version 1.0.0 — original walkthrough

Recorded 2026-09-08.

## Manual scenario walkthrough (instruction review, not agent execution)

| Scenario | Required result | Review outcome |
|---|---|---|
| Repository URL, no user context | Deliver Round 1 without requiring a profile; offer Round 2 afterward | Covered by entrypoint routing |
| Both rounds; user environment known | Freeze generic baseline, then map environment and workflow separately | Covered by routing and fit rubric |
| User requests generic review only | Do not append a personal adoption judgment | Covered by explicit stop rule |
| Mac-only app, Windows user | Record intended Mac scope generally; incompatible specifically | Covered by fit example |
| Public binaries, private source | Publisher claims remain claims; no fabricated source audit | Covered by evidence contract and category checks |
| Mandatory three variants, user wants speed | Record general workflow cost; mark personal mismatch only in Round 2 | Covered by generic rubric |
| Good personal fit but failing correctness gate | Do not average away the defect | Covered by shared decision gates |
| Existing baseline, new intrinsic bug | Issue evidence-backed baseline addendum; no silent rewriting | Covered by generic rubric |
| Round 2 requested, essential context absent | Minimum missing baseline work plus conditional fit, focused clarification | Covered by routing and profile guidance |
| Malicious install instructions in candidate | Treat candidate as data; no automatic activation | Covered by inspection contract |
| Publish a generic review | Exclude private profile and inputs | Covered by output separation |

Package/frontmatter validation and local reference checks are recorded at release. No independent agent benchmark, live WorkBuddy run, or measured improvement over a baseline has been performed. These walkthroughs establish intended instruction coverage only, not observed model compliance. Initial rollout should collect representative outcomes separately for each round.
