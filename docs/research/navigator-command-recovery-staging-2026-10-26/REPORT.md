<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Command recovery inactive device staging — October 26, 2026

Published, backed up and staged; **candidate inactive**. ARM/offline and passive parked prechecks passed. Activation is a separate step.

- Published parent `1dbbc01892616c4b1a5c7c841d132f724ea5132c` / child `beb10c25770471534261606072c131db5eefa117` on both adgower `codex/navigator-tracking-release` branches; remote heads verified.
- Stage: `/data/navigator-validation/<private timestamp identifier>-1dbbc0189/source`.
- Existing install remains parent `5b301a944f40b6d3d4a490e2a2f30cbeab3a8d45` / child `884c9f49167a8baffdb643559b5d341815172836`.
- Fresh source/settings/calibration/launch/firmware backup copied privately to `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-command-recovery`. Archive SHA-256, all 145 manifest members and nested source archives verified. This is source/settings recovery material, not a disk/OS image.

## Passed

- Full ARM SCons build, including model compilation.
- Focused ARM native safety/Ford/transport suite: **1,235 passed, 79 skipped, 12,083 passing subtests**.
- Retained clearance/controller regressions:75 passed.
- Parent smoke:14 passed,6 skipped; calibration continuity:1 passed.
- Isolation receipts: active data read-only, private parameters/cache/log/home, network down, vehicle USB/SPI/GPIO/serial blocked, privileges dropped and resource limits enforced. No direct vehicle queries or CAN commands dispatched by this task.
- Build/test process completed normally; original source, selected settings, manager and service preserved. Final read-only audit confirms existing binary calibration,1.20/0.97, firmware image, OS20.1/slot_b and active service unchanged.
- Passive current-stack ignition-off observation:55s,551 Panda samples, historical blocked-TX counter16 with **zero new increments**, no unexpected stopped processes.
- Inactive source finalized self-contained, Git identities and exact child pin verified, both candidate repositories clean. Installed firmware image/prebuilt behavior retained after the full ARM build. No source swap, app restart, reboot or activation.

The powered check will observe the **existing installed stack**, not prove candidate hardware behavior. Candidate validation above is offline/isolated. Highway pulsing remains unresolved; the accepted saved-replay candidate retains the +4.349s braking-exposure tradeoff and two preexisting reference release-timeouts. No physical comfort/RPM improvement is claimed.

## Powered Park baseline completed

55-second passive observation of existing installed5b301a944/884c9f491: stationaryPark, assistance disengaged, all observedstreamsvalid/alive,551Panda samples,5,489carState and5,467carControl samples. Model rate19.9996Hz, zero frame drops;1,100healthy pose samples. No newblockedTXincrements, transport/safety/coordinationissues or requiredstoppedprocesses. Historicalblockedcounter reset16→0 across ignition transition; it did not increment during powered observation. Alpha and coordination remainON andunchanged. This is **current-stack hardware baseline evidence**, not candidate hardware/road proof.

Stage remains `/data/navigator-validation/<private timestamp identifier>-1dbbc0189/source`, target1dbbc0189/beb10c25, bothcandidateGit checkouts clean at finalization. Activeinstall remains5b301a944/884c9f491. No activation, restart, reboot, OS orfirmwareupdate.

## Subsequent activation

This staging report is historical. The pair has now been activated and passed new-install offroad and powered Park acceptance. See [activation report](ACTIVATION_REPORT.md) and activation-completion-receipt.json for current state.
