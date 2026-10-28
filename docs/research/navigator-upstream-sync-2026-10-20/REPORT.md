<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest upstream master merged locally

Completed October 20, 2026. Branch: `codex/navigator-tracking-release`.

- Local merge: `db584234805cf2039ee976d856a29b655188ad2a`
- Upstream parent: `1ace967a7e27d2537a956c683978f646d6b6d739`
- Previous Navigator parent: `f7b0c47d23de697b73f1247cd5d32021b37e19bc`
- Preserved child: `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`

The branch is clean and includes the checked upstream master. Nothing was pushed, installed or changed on the Comma. The device's last documented pair remains f7b0c47d2/8ccc6cf0. Parent and previous msgq backup refs `codex/navigator-pre-master-sync-20261020` are retained locally.

## What changed

Adopted all 21 incoming upstream commits, including Autospeed/default planning, initial maximum cruise speed, removal of ExperimentalMode/Chill controls, scheduling and msgq changes. The source now follows upstream's model-based longitudinal planning when openpilot longitudinal is available. Alpha actuation remains a separate explicit opt-in; merging does not repair the Navigator brake/propulsion issue or add MADS.

Resolved only two application conflicts: both settings layouts retain Navigator pinion/low-speed controls and offroad/vehicle/callback guards alongside the new upstream initial-speed UI. The Mici AST test fixture now supplies the new widget and checks its presence/refresh; the existing three guard/retention tests failed before that fixture adaptation and then passed. No assertions were removed. The custom opendbc fork URL, pin and 85 protected Ford/safety source hashes are unchanged. Calibration/motion/tracking modules and controlsd match the prior Navigator parent; Card retains their integration while accepting upstream cruise initialization. Owner1.20/0.97, geometry, native safety, release/budget behavior and all five default-OFF Navigator preferences remain intact. Only msgq advances among dependency checkouts; old dependency head retained by backup ref.

## Checks

- Configured incremental Mac minimal, full/development and Panda builds passed.
- Full parent suite: 1,021 passed, 84 skipped, one expected failure, 281 subtests passed.
- Full child suite: 4,263 passed, 1,690 skipped, 24,673 subtests passed. Uses the existing unsanitized Mac debug safety library; no fresh ARM/UBSan claim.
- Mici UI regression: expected three failures after upstream widget change, then three passed with the fixture extended.
- Fake-clock stall scenarios at20/100Hz passed: after a420ms stall, new Ratekeeper resynchronizes instead of repeated immediate catch-up dispatches. This is synthetic scheduler behavior, not real-time hardware proof.
- Scoped Ruff and diff checks passed. Fresh-context independent integration review found no material issues.
- Final verification confirms both merge parents, upstream ancestry, clean paired checkouts, exact pins, protected child hashes and preserved Navigator guard-method ASTs.

No new full819segment replay was run: prior child-strategy/native evidence remains relevant through unchanged source. It is not new end-to-end evidence for the merged parent, changed scheduler or upstream longitudinal planner. Parent integration/pipeline tests cover local context/provenance/stale withdrawal behavior; Mac checks do not establish ARM startup or road handling. A device install needs separately authorized staging, backup and parked acceptance.

## Procedural decisions

Reused the existing clean feature checkout as requested. Adopted upstream ExperimentalMode removal rather than retaining an obsolete selector; the behavior difference matters when openpilot longitudinal is enabled. No Comma parameters were written. Future installer/acceptance helpers must stop reading/writing ExperimentalMode, retain Alpha/stock-ACC choices explicitly, and test the new initial-speed preference. There are no deferred review findings. The user already chose local integration, so no additional publishing/merging menu was needed; both branches remain available.

[Final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [independent review](REVIEW.md), [stall scenarios](../../navigator-reference/PRIVATE_ARTIFACTS.md), [merge receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).
