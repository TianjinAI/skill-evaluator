# Validation and limitations

## Version 1.4.3

- Independently inspected WorkBuddy's local handoff, archive and patch against the published ecosystem revision. The patch preserves the entrypoint and ecosystem rubric; the example's reverted Round 2 title was restored during review.
- The supplied archive contained AppleDouble `._*` metadata files and failed the Markdown-link test when extracted. Applied the reviewed source patch instead and excluded metadata from the release archives.
- Corrected prose rendering that removed negative signs (for example `-74` became `74`), rejected bands excluding their point score, and clarified that missing evidence remains NE rather than a placeholder score. Updated version declarations and synchronized the embedded Chinese introduction.
- All 26 local tests passed, including new regression checks for signed numbers/literal punctuation, band containment and non-text prose. Skill frontmatter validation and whitespace checks passed. Release archives are generated from tracked Git content and checked after extraction.
- WorkBuddy reported desktop/mobile visual checks for its earlier renderer in the handoff; this review did not independently reproduce those checks. No new visual or print verification is claimed for the corrected renderer. The local-file browser restriction recorded under 1.4.0 remains a limitation of this review.

## Versions 1.4.1–1.4.2

Recorded together: both changes came from the same review cycle, from defects a user reported while reading a delivered report, and neither was released independently. The `band` field and the score/confidence wording are 1.4.1; the prose rendering and round-heading fixes are 1.4.2.

- Two defects were reported by a user reading a delivered report, and both were fixed in the package rather than only in that report:
  - The renderer escaped authored emphasis and collapsed every newline, so structured review notes were delivered as one unformatted paragraph. Fixed by adding a narrow inline contract (`**bold**`, `` `code` ``, everything else escaped) and line-based prose rendering. No heading, link or raw-HTML pass-through was added; a regression test asserts that `<script>` and `<img>` in prose stay escaped text.
  - A round title that repeated its own `Round N` prefix rendered as "Round 1 · Round 1 · …". The renderer now rejects that input instead of silently double-prefixing.
- Added an optional `band` field (`"2–4"`), printed beside the point score as `3 (2–4)`, validated as ascending whole numbers 1–5 and rejected for NE/NA. Documented as a reasoned reachable-anchor interval, explicitly not a confidence interval or probability.
- Added an optional `scorecard_note` so the score/confidence convention sits with the table it explains.
- All 23 automated tests passed locally (up from 17): the six additions cover score bands and their rejection cases, prose lines and inline markers, prose markup pass-through, round-heading validation and scorecard-note placement.
- WorkBuddy’s handoff reports visual QA at 1280 px and 390 px in Chrome, covering summary blocks, the scorecard and narrow-layout table scrolling. This is contributor-reported evidence, not independently reproduced here; print styling remains visually unverified.
- The prose fixes are a rendering change plus a documentation rule, not a change to scoring anchors or category definitions. Whether the revised structure actually improves comprehension for other readers has not been measured; that remains a judgment, not a result.

## Version 1.4.0

- Reviewed one user-supplied WorkBuddy output and its visible tool trace from the earlier evaluator. Observations informed intake timing, evidence calibration, coverage reporting and overlap reasoning. The private transcript/inventory are not bundled.
- All 17 automated package/renderer tests passed locally: initializer behavior and relative links plus text escaping, unsafe source URL rejection, score/provenance validation, Unicode/tables, generic/private export separation, overwrite/symlink protection and invalid-input handling.
- Both generic and combined HTML files were generated using the CLI. The skill frontmatter validator and whitespace check passed.
- Browser visual QA was attempted but blocked by the browser URL security policy for local files. Desktop/mobile/print rendering remains visually unverified; print and responsive styles are included, not claimed tested.
- Manually walked the upfront intake and completion rules against the observed trace. No independent agent benchmark or revised WorkBuddy rerun has been performed; regression scenarios remain prospective.

Earlier sections below are historical records; 1.4.0 supersedes the former offer-Round-2-afterward routing.

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
