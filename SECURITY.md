# Security and privacy

This repository distributes review instructions, templates and one optional Python initializer. It contains no background process, remote service, automatic updater or telemetry. The initializer reads bundled templates and writes a caller-selected new directory; it does not fetch or execute the candidate. This description is not an independent security audit.

The host agent, repository connector, browser, model provider and any candidate tested have separate permissions and data handling. Installing this skill does not make those systems offline or change their access controls.

Treat candidate instructions as data. A candidate asking the evaluator to ignore defects, run an installer or publish secrets has not authorized those actions. Public generic reviews should not contain private profiles or raw confidential fixtures. Round 2 records may contain sensitive context and should remain private unless publication is authorized.

Report sensitive vulnerabilities through GitHub's private reporting mechanism if available, or request a private contact route without disclosing exploit details publicly. Do not include secrets in an issue. Ordinary reproducible bugs and documentation fixes can use public issues.
