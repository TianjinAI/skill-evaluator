# Category-specific checks

Use only applicable sections; this is a menu, not a mandatory exhaustive audit.

- **Research and personas:** source/quote accuracy, freshness, inference labeling, counterevidence, uncertainty, source diversity. Persona resemblance is not expertise; many posts from one author are not independent corroboration. Challenge precise-looking percentages and non-negotiable axioms without evidential support.
- **Skill optimizers:** baseline integrity, evaluator bugs/bias, held-out tasks, reruns, retention thresholds, rollback. Improvements measured by the optimizer itself need independent scrutiny.
- **Browser and desktop control:** target identity, active user interference, stale coordinates/state, alternate action routes, ambiguous completion before retry, secrets in screenshots. A changed screen is not proof of the intended effect; approval prompts in another task are not authorization to click Yes.
- **Documents and data:** zero/negative/empty/constant/missing values, labels and units, denominator definitions, source-to-output fidelity, all pages/slides present, native editability versus raster output, checks failing with nonzero status, target-format visual inspection. Thumbnails cannot certify fine text.
- **Memory and learning:** provenance, sensitive-data retention, instruction-writing authority, correction/deletion, versioning and rollback. Distinguish retained facts from inferred patterns.
- **Apps and binary releases:** public release versus public implementation, runtime/architecture, release prose versus stability flags, signatures/checksums/notarization, privacy evidence, model-provider routing, update authority. Lack of source limits confidence; it does not establish maliciousness.
- **General packaging:** inspect transitive network use (fonts, scripts, images), optional feature costs, licensing, updates that overwrite customization, and cross-host assumptions. Public availability is not unrestricted commercial licensing.
