# Round 2: User ecosystem suitability and synergy assessment

Question: Does the candidate fit the user's tasks and agent-skill ecosystem, and can it improve their combined outcomes enough to justify its costs and constraints?

The ecosystem includes agents, skills, tools/integrations, workflows and operating constraints. Assess complementarity, useful handoffs, gaps filled and consolidation benefits alongside compatibility and duplication. For each material synergy claim, identify the participating capabilities, input/output handoff, expected benefit, dependencies and observed or still-needed validation. No installed inventory does not prevent task/environment fit assessment; mark ecosystem coverage accordingly.

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

Use [upfront intake](intake-and-completion.md) before delivering findings. Ask about a missing requirement only if it could change the recommendation. Continue independent work while waiting when the host supports it. If critical context remains unavailable, provide a conditional fit assessment rather than an unconditional adoption decision. Do not make an entire questionnaire mandatory.

## Check the actual environment and installed capabilities

Follow [the overlap procedure](installed-skill-overlap.md) for a bounded, read-only inventory. Use the host's existing catalog first, and inspect likely substitutes or conflicts only as needed. Record whether a capability is installed, enabled, callable or execution-verified. Keep inventory scope/omissions visible; lack of access does not mean no duplicates exist.

Check relevant host/OS/tools/dependencies against the candidate contract using available read-only evidence. Do not infer operational compatibility from a product name. Identify the candidate's incremental value, likely trigger conflicts, complementary handoffs and alternatives already available.

## Map baseline to fit

Link the exact Round 1 revision. For each relevant finding state its consequence for this use case. Keep intrinsic defects distinct from fit concerns. Examples: a Mac-only app may be coherent in Round 1 and unusable for a Windows user in Round 2; a required cloud endpoint may be acceptable generally but disqualifying for an offline workflow.

Check compatibility by actual capabilities rather than model brand. Identify overlap and complementary value with existing tools. Do not recommend installing a second complete workflow solely because its component library is useful.

## Test suitability against the user task

Build a small acceptance matrix: requirement → check/input → expected result → actual result → status → evidence. Use passed, failed, not tested, blocked, or not applicable, with a reason. Establish task and environment requirements before judging.

Run a bounded representative task when needed and feasible under existing authorization. Use disposable/sanitized inputs where possible. Do not install or activate a candidate, expose private data or perform real-account writes simply because this is Round 2. If necessary access or runtime is missing, complete available checks and give a conditional conclusion with the exact blocker. Do not replace user-specific testing with more generic source review.

### Matched task trial

Define a small representative task with fixed inputs and measurable acceptance criteria. Compare the current workflow and candidate; add a plain-agent baseline if it answers a different useful question. Use matched model, tools, time/cost budget, and inputs when feasible; record unavoidable differences. Include relevant edge/failure cases. For variable tasks, repeat enough to avoid a verdict based on one lucky output; do not impose a universal run count.

Measure outcomes that matter: task completeness, factual/data fidelity, false success, unintended side effects, revision effort, recovery, user interventions, elapsed time, and cost. A test plan is not a test result. Do not claim WorkBuddy or another host is validated merely because SKILL.md is present.

End with an adoption decision, explicit conditions, overlap recommendation and actual test coverage. When no representative task ran, state "assessed only—suitability not task-validated"; if some tests ran, identify which requirements remain untested. A blocked trial is not a passed test. Suggest the smallest useful adaptation; distinguish a configuration change from maintaining a fork. Describe remaining uncertainty and who/what can resolve it. Reuse generic evidence rather than repeating the whole baseline.


## Fit scorecard

Use the six categories in [scoring](scoring.md) for standard/deep reviews or when requested. Evaluate alignment with the doctrine’s stated values separately from its generic reasoning quality. Link relevant Round 1 findings and score changes to this user’s requirements. Missing context is NE, never a guessed midpoint. Keep mandatory gates visible.
