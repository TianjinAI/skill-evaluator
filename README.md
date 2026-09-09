# Skill Evaluator

A portable agent skill for evidence-backed package evaluation in two separately deliverable rounds.

1. **Independent generic review:** purpose, features, architecture, instructions, correctness, reliability, privacy, evidence, licensing, and readiness. No assumptions about an individual user's preferences.
2. **User-specific fit review:** maps that baseline to a user's actual tasks, workflow, host environment, constraints, alternatives, and adoption decision.

The second round reuses the first; it does not alter intrinsic findings to suit a preferred verdict. Reviews distinguish publisher claims, source evidence, local checks, and completed task validation.

## Install

Repository: https://github.com/TianjinAI/skill-evaluator

Give your skill-capable agent this repository URL and ask it to install the **whole directory** as `skill-evaluator`, keeping `references/` alongside `SKILL.md`. For WorkBuddy, ask it to fetch this repository through its supported skill-install workflow; exact UI and installation paths vary by version and have not been tested here.

If your agent uses the shared skill directory, an example is:

```sh
git clone https://github.com/TianjinAI/skill-evaluator ~/.agents/skills/skill-evaluator
```

No runtime packages or service accounts are required by the skill itself. The reviewing agent needs suitable repository/file access; behavioral testing may need the candidate's dependencies and separately authorized access.

## Examples

- "Use skill-evaluator for a Round 1 review of this repository. Do not install it."
- "Now run Round 2 using that review: I produce weekly reports on Windows in WorkBuddy, with no cloud upload of source documents."
- "Compare these two skills. Keep their generic merits separate from their fit for my existing workflow."

## Evidence limits

This is a review method, not a security certification or automated benchmark. A valid skill package does not establish that its recommendations are correct. Version 1.0.0 was checked for structure and scenario coverage; live performance across agent products is not yet established.

MIT licensed. Developed from a series of package reviews; public instructions contain no personal user profile or private review inputs.
