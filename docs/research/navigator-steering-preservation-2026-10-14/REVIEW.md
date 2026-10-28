<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator steering preservation and updater review

No files, refs, configuration, parameters, services, or credentials on the Comma were changed. Read-only SSH commands captured the files on this Mac. No ECU queries were sent.

## Preserved artifacts

- lateral_angle.device.py: exact live working file.
- lateral_angle.installed-base.py: committed version at installed opendbc HEAD.
- navigator-steering.patch: binary-capable Git diff against that HEAD.
- lateral_angle.pending-target.py: version the staged updater is trying to install.
- pending-opendbc-changes.txt and pending-openpilot-changes.txt: already-fetched pending commit summaries.
- manifest.json: SHA256 and byte sizes. All artifact hashes checked successfully. All three Python snapshots parse; this is syntax evidence only, not steering/runtime/road validation.

Installed openpilot HEAD: f35e6e5eb11ca9cddad3ed945d44d8f191679240.
Installed opendbc HEAD and parent gitlink: eb70bef4f56d2e9e91cb5a0a8374890a6acfaf51.
Staged openpilot target: c59724318cd88e9385c905860b6480fe367e99b3, navigator-angle-v1.
Staged target opendbc gitlink: 0bd0763bcf88553f570b1de457ad6c0dc76fca83.
These are observed staged revisions; the current remote tip was not fetched or independently refreshed in this pass.

## Review of the uncommitted change

The live modification adds Expedition-only constants 1.20 (low-speed) and 0.97 (high-speed) to the high-curvature gain arm. It keeps the low-curvature arm unchanged and applies the factors only when carFingerprint is FORD_EXPEDITION_MK4, the forced platform selection on this Navigator.

At v_ego <=13.5 m/s, the high-curvature gain endpoint becomes 1.30*1.20=1.56 rather than 1.30. At v_ego >=26.82 m/s, the Expedition high-curvature gain endpoint becomes 1.425*0.97=1.38225 rather than 1.425. This explains exactly what was preserved; it is not a conclusion that this tuning is safe or optimal.

## Review of the pending update

Target commit 0bd0763b already adds speed-factor code, but with different tuning: 1.15 and 0.98. Its high-curvature endpoints are 1.495 and 1.3965. It also removes the Expedition-only conditional around factor application in lateral_angle.py; non-Expedition callers would need separate review.

Earlier pending commits introduce fixed-model pinion curvature. Ford interface explicitly enables PINION_CURVATURE for the Expedition CAN-FD candidate. lateral_angle.py then estimates curvature from steering angle and fixed VehicleModel geometry instead of yaw rate divided by speed. Ford safety flags and safety/modes/ford.h change too. Thus accepting the current staged branch tip would change both this Navigator's tuning and the curvature feedback/safety path, even if the 1.20/0.97 factors were restored.

27 opendbc files differ, including documentation/replay evidence and tests; the full pinion/safety implementation was not reviewed for deployment or validated on-road in this pass.

## Why a device-only commit is insufficient

lateral_angle.py belongs to the separate opendbc_repo Git repository. Committing only the parent openpilot repository cannot capture its file contents. A correct published change requires a commit in opendbc and a parent openpilot commit pinning that exact opendbc commit.

Installed updated.py fetch_update checks out the remote target branch with force, resets/cleans the staged parent, updates submodules to its gitlinks, then resets those submodules. Consequently a local device-only commit is not a durable preservation policy: the updater still follows the published parent branch/submodule pin. Simply stashing or discarding the diff would remove the immediate obstruction but allow a behavior-changing update.

## Recommended repair design

To preserve current steering behavior, use isolated local checkouts rooted at the installed commits. Commit the preserved 1.20/0.97 change in opendbc without pulling in the pending pinion changes. Publish that commit on a dedicated preservation branch, and publish a corresponding openpilot branch based on installed f35e6e5 with its opendbc gitlink advanced to the preservation commit. Verify both published SHAs and targeted checks before preparing a device transition. This retains the current yaw-rate curvature implementation and explicit tuning while giving the updater a clean, published target.

No branch, commit, push, PR, or device transition was created by this review. Device cleanup and updater-staging reconciliation must be planned around preserving the live checkout; they have not been executed.

Alternative: adopt the pending pinion branch, restore 1.20/0.97 in it, and update the parent gitlink. This preserves the constants but NOT the current steering implementation. It requires separate review and validation and is not recommended as an incidental updater repair.

## Temporary update pause

Avoiding internet alone does not solve the startup issue: historical logs already show the connectivity gate blocking startup. Installed hardwared.py treats DisableUpdates or SnoozeUpdate as exceptions to that gate, but this pass did not inspect the full behavior or supported UI path for those settings. Changing either would be a device configuration change and was not authorized here. Do not use those flags as a proven permanent fix.

A deliberate temporary freeze can be considered while the published preservation branch is prepared, but must be separately scoped and reviewed. No settings were changed. Keep the vehicle parked for any later restart or update validation.
