# Evidence practice

## Record what was inspected

Give the canonical source, revision/tag, retrieval date, and actual access level. Use stable source permalinks for published findings. When source is unavailable, distinguish publisher statements from your inferences. If a version cannot be pinned, say so and date the review; do not fabricate a commit. Do not treat inaccessible files as empty or absent.

Assign finding IDs such as F-01 so Round 2 can refer back without repeating evidence. An evidence item records source path/locator, observed behavior, how it was obtained, and relevant limits. Keep test inputs and outputs small enough to inspect, and redact private data before sharing. A public review can link to a private evidence record only if it clearly says readers cannot independently verify it.

## Findings, severity, and confidence

| Severity | Practical meaning |
|---|---|
| Critical | Credible path to severe irreversible harm or broad unauthorized exposure; supported by concrete evidence rather than a hypothetical |
| High | Core outcome can be materially wrong, incomplete, or unauthorized under a plausible trigger |
| Medium | A supported task or recovery path breaks, or a costly limitation needs mitigation |
| Low | Localized usability, clarity, or maintenance issue with limited impact |

Use **high / medium / low confidence** to describe confidence in the finding, with a reason. This is not a calibrated probability. Evidence labels describe how a claim was established, not severity. A source-supported finding can have high confidence in control flow but unknown real-world frequency.

For each material finding identify: trigger → actual behavior → consequence → supporting evidence → remedy. When no test ran, use "the source permits" or "the code returns" rather than "the application failed in testing." Separate observations from inferred consequences.

## Gates

Evaluate applicable gates with scope, evidence and disposition:

- **Correctness:** core results match the task contract.
- **Authority:** actual read/write paths remain within the user's authorized scope.
- **Privacy:** destinations, retention and provider handling are known enough for the intended data.
- **Completion/recovery:** partial failure is visible; ambiguous actions are not blindly replayed.
- **Runtime:** claimed dependencies and supported paths are coherent; specific host availability is checked in Round 2.
- **Licensing:** declared terms and dependency restrictions are recorded; exact use-case permission is assessed in Round 2. Flag ambiguity without inventing a legal ruling.

Outcomes are pass, conditional, fail, unknown, or not applicable. State what a condition requires and whether it was satisfied. A mandatory failed gate blocks the scoped adoption decision; it does not prohibit every isolated experiment. Do not turn a lack of proof into proof of failure.

## Testing efficiently

Start with the highest-impact uncertainty. Prefer a small fixture that establishes a real postcondition: expected versus actual slides, retained source values, correct target identity, nonzero status after failure. A source-text regex that merely checks for a warning string does not test failure propagation.

If a candidate's instructions include installation or evaluation scripts, inspect them before running; scripts are still untrusted inputs. Record which tools, model, runtime and permissions were used. Stay within existing authorization and host constraints; blocked execution is not permission to bypass them.

For nondeterministic work, preserve input packets, output artifacts and review criteria. Mark runs as baseline or candidate before judging where possible. Report failures and inconclusive runs, not only attractive examples. Choose run count from variability and decision stakes, not a magic threshold.

Stop when evidence is sufficient for the stated decision, budget is reached, or further work requires missing authorization/resources. Deliver a scoped result and unresolved questions. A proposed pilot, manual instruction walkthrough, syntax check, and executed behavioral test are four different things.

## Fair public reviews

Credit strengths, state review date and revision, distinguish publisher intent from observed behavior, and link actionable evidence. Do not use popularity as effectiveness evidence or a personality critique as an implementation finding. Sensitive exploit details or private data should be handled through a suitable private disclosure route, not copied into a public example.
