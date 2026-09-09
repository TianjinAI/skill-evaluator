# Validation and limitations

Version 1.0.0, 2026-09-08.

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
