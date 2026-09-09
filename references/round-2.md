# Round 2: User-specific fit review

Question: For this user's actual work and environment, does the candidate improve outcomes enough to justify its costs and constraints?

## Establish the profile

Use information already provided. Record only what affects the decision, distinguish explicit requirements from inferred preferences, and avoid collecting secrets.

| Context | Useful details |
|---|---|
| Task and success | Concrete inputs/outputs, frequency, audience, quality threshold, acceptable error, deadline |
| Workflow | Existing tools, handoffs, review habits, desired autonomy, willingness to explore variants, approval burden |
| Environment | Host agent, OS/architecture, available tools/dependencies, offline needs, network/account restrictions, install permissions |
| Data and authority | Sensitivity, permitted providers, local/cloud boundary, read-only versus real writes, reversibility |
| Resources | Time, cost, model/API budget, maintenance capacity, preferred language |
| Alternatives | Current workflow, plain agent baseline, already-installed capabilities, switching/migration cost |

Ask about a missing requirement only if it could change the recommendation. Continue independent work while waiting when the host supports it. If critical context remains unavailable, provide a conditional fit assessment rather than an unconditional adoption decision. Do not make an entire questionnaire mandatory.

## Map baseline to fit

Link the exact Round 1 revision. For each relevant finding state its consequence for this use case. Keep intrinsic defects distinct from fit concerns. Examples: a Mac-only app may be coherent in Round 1 and unusable for a Windows user in Round 2; a required cloud endpoint may be acceptable generally but disqualifying for an offline workflow.

Check compatibility by actual capabilities rather than model brand. Identify overlap and complementary value with existing tools. Do not recommend installing a second complete workflow solely because its component library is useful.

## Pilot only when warranted

Define a small representative task with fixed inputs and measurable acceptance criteria. Compare the current workflow and candidate; add a plain-agent baseline if it answers a different useful question. Use matched model, tools, time/cost budget, and inputs when feasible; record unavoidable differences. Include relevant edge/failure cases. For variable tasks, repeat enough to avoid a verdict based on one lucky output; do not impose a universal run count.

Measure outcomes that matter: task completeness, factual/data fidelity, false success, unintended side effects, revision effort, recovery, user interventions, elapsed time, and cost. A test plan is not a test result. Do not claim WorkBuddy or another host is validated merely because SKILL.md is present.

End with an adoption decision and explicit conditions. Suggest the smallest useful adaptation; distinguish a configuration change from maintaining a fork. Describe remaining uncertainty and who/what can resolve it. Reuse generic evidence rather than repeating the whole baseline.
