<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired sustained tracking and unwind integration

Integrated and committed locally on both `codex/navigator-tracking-release` branches:

- openpilot: `0171b897289be53fd62f330935c55825b86c3c3a`
- opendbc: `4167433e5c575f620a9dedf8144a0bc7cba14291`

The parent pins that child commit, and both checkouts are clean. Starting heads were `50baa6fd6acf9d37b7e0768e5736efab2a357ddc` / `0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`.

The child adds the accepted sustained-error/60–70 mph unwind policy and independent installed-history fade from 70 to 75 mph. The original wheel-target controller remains unchanged as the independent reference. The parent selects the new class through the existing prerequisite/default-off factory. No new setting, UI or producer is added.

**1.20/0.97**, geometry, pinion, native safety, legacy controllers, parameter registry, card/motion sources and device settings snapshot remain unchanged. No device connection, push, installation or firmware action occurred.

## Verification

| Check | Result |
|---|---|
| Focused production/factory tests | 134 passed |
| Parent full suite | 1,018 passed; 343 subtests; 86 skipped; 1 expected failure |
| Child full suite | 4,112 passed; 24,673 subtests; 1,690 skipped |
| Configured Mac minimal / development / Panda builds | All pass, including a second pass at committed heads |
| Transition/abort screen | 480 cases / 172,800 frames pass |
| Actual factory versus accepted prototype | 30,240 returned-command updates identical |
| Scoped Ruff / whitespace | Pass |
| Independent integration review | No material findings |

Production class ASTs match the accepted prototype with only exported class naming and explicit `zip(strict=False)` normalization; formatting and imports change outside the class comparison. Protected file hashes and the existing unsanitized native debug library match preservation receipts.

The accepted prototype's 43-route / 740-segment native evidence is carried through exact class and actual-factory equivalence. A fresh integrated 740-segment replay was **not** run in this build task. That prior evidence establishes zero added native rejects, above-75 mph byte parity and protected-range/default-off parity; it is not new physical handling evidence.

The factory regression failed as expected before integration (one failure / 11 passes), then passed in the full suite. Early wrong-working-directory collection attempts are excluded; the correct paired environment was used for successful runs. Initial formatting/lint diagnostics were resolved before final verification without changing class behavior.

These are configured **incremental Mac builds** and full local suites, not clean-room, ARM/AGNOS boot, physical CAN, closed-loop stability or road validation. The pair is locally committed and unpushed; device activation requires its separate backup/build/parked acceptance process.

[Final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build steps](../../navigator-reference/PRIVATE_ARTIFACTS.md), [committed builds](../../navigator-reference/PRIVATE_ARTIFACTS.md), [equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [commits](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Subsequent publication and device activation are tracked in the [installation report](../navigator-sustained-installation-2026-10-19/REPORT.md); the unpushed/no-device statements above describe the completed local build stage.
