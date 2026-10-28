<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest master refresh — October 24, 2026

Merged upstream `9fba666fd485983b5849dfc62550fa1fd37fe338` into the existing Navigator branch, producing `74eaa6a60d344f141d06da16f4dbe10d3de49c0e`. Published to `adgower/openpilot`, branch `codex/navigator-tracking-release`, and verified the exact remote SHA. Child remains `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`; no child publication was needed.

Upstream adds Flip Flop model, Unix datagram logging and replacement of the old bridge with WebRTC. Both updated upstream submodules match their committed gitlinks. No AGNOS, Panda firmware or custom controller/vehicle geometry change is introduced. All existing steering, coasting, pose fixes and 1.20/0.97 source remain unchanged.

## Validation

- Conflict-free merge and clean final source tree; upstream target is an ancestor.
- Three materialized model artifacts verified by SHA256 and byte count against upstream LFS pointers (`model-verification.json`). Initial Hugging Face cached authentication failed; public access without the cached basic-auth requirement succeeded. GitHub fallback returned missing objects and was not used for artifact proof.
- Minimal/full Mac builds and Panda compilation passed (`build-results.json`).
- Parent: 1,061 passed, 87 skipped, 1 expected failure, 281 subtests passed.
- Child: 4,570 passed, 1,690 skipped, 24,693 subtests passed. Existing Mac native safety debug hooks used; no UBSan claim.
- Independent read-only merge review found no blockers. Custom steering, coordination, pose, geometry, launch and child source unchanged; logging/WebRTC files match upstream. Previous generated bridge binary was retained in this evidence folder because upstream removed its ignore entry.

## Device boundary

Comma was inspected read-only: installed parent remains `2aa86b78d`, Alpha ON, offroad, AGNOS 20.1, about 8.9 GB free. No device writes, restart, activation, OS/firmware update or active ECU query was performed for this refresh.

This is a validated published branch update, not an installed device update. Separate ARM/model startup validation, fresh backup and parked acceptance are still required. New-model road behavior is unproven; unchanged-controller replay does not validate the new requested paths or speed behavior. Existing brake-release timeout cases remain unresolved.
