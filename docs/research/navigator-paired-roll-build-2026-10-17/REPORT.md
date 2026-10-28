<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired Navigator calibration/roll integration and full local build

Integrated and saved on both existing `codex/navigator-tracking-release` branches:

- openpilot `99645f2222ea2ba1fd4124808774bcd6381f8154`
- opendbc `8cbc834fe534a248a3bc6d56ce964106c0f49503`

Parent pins that exact child; both checkouts are clean. These are local commits, not pushed. No Comma access, settings write, installation, reboot or firmware flash occurred. Owner **1.20/0.97**, fixed pinion geometry, vehicle values and native safety source/library are unchanged. New roll mapping remains separately default-off.

## Validation

- **Both Mac builds pass:** full `scons --minimal -j4` and development `scons -j4`. Affected schema/native targets rebuilt; both targets also pass at the final committed heads. These are normal incremental SCons builds, not clean-room builds.
- **Parent suite:**989passed,86skipped,1expectedfailure,343passing subtests.
- **Full child suite:**3880passed,1690skipped,24673passing subtests. Uses the existing unsanitized Mac debug hooks; no UBSan result claimed.
- **Local Panda build passes**, including H7 artifacts; no flashing.
- **Integrated actual producer/card+unique local IPC passes**, including default-off selection, immutable snapshot and controlled-cadence stale-input final release.
- **320transition/abort cases /115200frames pass** against integrated sources; final limits/intent and eventual baseline return verified.
- Scoped repository lint and diff checks pass. Independent review of applied code/test port found no remaining concrete integration finding.

The regression tests now live with their respective paired repositories. The mapping was formatted to repository style and made explicit about the existing `zip(strict=False)` default; module documentation was updated. `staged-equivalence.json` / `integration-verification.json` record normalized control-AST and source binding to the already515-segment replayed candidate. The515-segment replay was **not repeated in this build stage**; prior receipts remain in the preceding package. No new observed tracking-improvement claim.

## Preservation and evidence

`pre-integration.json` records original clean heads/branches and source hashes. `backup/` holds exact changed-source backups plus protected steering/geometry files and the existing historical settings snapshot. It is not a new device inventory.

`verification.json` summarizes checks; `build-results.json`, `post-commit-build-results.json`, suite/build logs, `pipeline-results.json`, `transition-results.json`, `paired-commits.json` and source-equivalence receipts retain evidence. The parent repository links its new `docs/navigator-integration/ROLL_MAPPING_20261017.md` from its integration README.

No AGNOS/Chestnut target runtime, USB/CAN delivery or road evaluation is established by these Mac checks. The existing five bounded rate-limited release-tail frames and physical actuator/ratio identification limits remain documented. Publication, deployment and option activation are separate from this completed local integration/build task.
