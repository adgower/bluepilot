<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Earlier bounded unwind onset: paired integration

Completed locally October 20, 2026. Branch in both repositories: `codex/navigator-tracking-release`.

- openpilot: `f7b0c47d23de697b73f1247cd5d32021b37e19bc`
- opendbc: `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`

The parent pins the exact child commit; both checkouts are clean. Nothing was pushed or changed on the Comma. Its last documented pair remains f750d756ca/de70d4f945; no live device check was performed.

## Result

The existing all-opt-ins factory now selects `EarlierUnwindOnset`. It credits existing persistence from independently validated, distinct wheel/body histories during withdrawing demand strictly between 60 and 70 mph. Default-off prerequisites and inherited magnitude, rate, budget, release, input validity and native safety limits remain unchanged. No new settings were added. Protected source hashes verify the existing 1.20/0.97 factors, vehicle geometry and previous steering/safety modules are unchanged.

## Verification

- Expected factory regression failed before the port, then passed.
- 72 focused tests pass: 60 onset/guard and 12 factory checks.
- Full configured parent suite: 1,018 passed, 343 subtests, 86 skipped, one expected failure.
- Full child suite: 4,263 passed, 24,673 subtests, 1,690 skipped.
- 714 transition cases / 228,480 frames pass; 128 abort cases pass with zero added neutral tail.
- AST equivalence to the accepted prototype and actual parent-factory equivalence over 86,400 updates pass, including rising-demand, invalid-CAN recovery, boundaries and abort scenarios.
- Scoped Ruff, format and diff checks pass. Independent source integration review found no material issues.
- Configured incremental Mac minimal, development/full and Panda builds pass before and after commits; 12 factory checks pass again at the committed pair.

The accepted 53-recording/819-segment native/controller evidence is carried by the exact class port and factory equivalence, not a fresh integrated full-corpus replay. That replay generated 4,735,309 controller updates per variant with zero additional native rejections. The native-library provenance is retained from the accepted prototype; this integration does not claim a fresh native-hook library build or sanitizer run. Mac builds do not establish ARM/AGNOS boot or vehicle behavior.

Saved 67/69 mph episodes showed encoded onset 0.249/0.101 seconds earlier in the prototype. This proves command timing, not improved physical tracking. Protected below-60 and >=75 mph replay output remains unchanged in the accepted evidence. The 28 mph native-deviation shortfall remains open.

## Next gate

Publication and device installation require a separate request. Preserve the existing whole-install rollback and settings when that stage is authorized. Physical improvement still requires hardware and road evidence.

See [final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [committed-pair builds](../../navigator-reference/PRIVATE_ARTIFACTS.md), [factory equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md) and the [accepted prototype](../navigator-earlier-unwind-onset-prototype-2026-10-20/REPORT.md).
