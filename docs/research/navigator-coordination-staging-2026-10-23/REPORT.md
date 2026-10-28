<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordination fix: activated; parked acceptance passed — October 23, 2026

> Subsequent road trial failed: calibration-only update clears pose validity and triggers Controls Mismatch during moving engagement. [Failure investigation](../navigator-coordination-engagement-failure-2026-10-23/REPORT.md). This supersedes parked acceptance as a trial-readiness result. No further Alpha trial pending repair.


## Activation update

Owner authorized activation after staging. Exact pair e9ddc7668/d2e8d040 is now installed; ignition-off runtime acceptance passed20seconds/201Panda samples, with no unexpected stopped processes or new blocked transmissions. Coordination preference is1; owner subsequently selected Alpha1 while offroad for powered stationary acceptance. Whole prior installation is retained at `/data/openpilot.pre-coordination-<private timestamp identifier>`. No OS or firmware update. [Activation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Fresh pre-activation private parameters were copied to device and Mac; all67Mac files verified by hash. Three learned values had naturally changed since the original backup during the intervening ignition cycle; the fresh values were preserved across installation, rather than restoring stale ones. Calibration/steering1.20/0.97, existing opt-ins, firmware and launchers were retained. The coordination preference is the only intentional setting change; Alpha was subsequently selected by the owner for passive Park acceptance. [Fresh backup](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The first attempt stopped at immediate readback of an asynchronous preference write and automatically restored the complete old install. Inspection confirmed `put_bool(..., block=False)` is the default; a private temporary Params test proved persistence/readback with `block=True`. The corrected helper passed the retry. Production control source was unchanged. [First attempt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [isolated persistence check](../../navigator-reference/PRIVATE_ARTIFACTS.md).

First powered attempt found Alpha still off (OEM safety parameter10), so the Alpha transport expectation was not met; no coordination fault was recorded. Owner was asked to select Alpha while offroad and cycle ignition. That short mode-mismatch observation is retained separately and is not a passing candidate acceptance. [Mode mismatch](../../navigator-reference/PRIVATE_ARTIFACTS.md).

**Candidate powered stationary acceptance passed.** Final corrected checker completed55.01seconds, all16streams alive/valid, stationary Park and assistance disengaged throughout, Ford Alpha safety parameter11, zero CAN/RX/transport/radar/coordination faults, zero blocked transmissions, no unexpected stopped processes, calibrated model around19.99Hz with zero reported drops. Coordination request/feedback schema was observed live: 1100request samples, all enabled, maximum observed producer age35.13ms; inactive feedback carried no fault. This proves inactive stationary transport, not moving brake release or grade/ride performance. [Candidate acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [final source audit](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The initial complete observation was healthy but a checker-only tuple lookup typo stopped its final assertions; the typo was fixed and the complete passive window repeated successfully. No control source changed. Alpha and coordination are now on by owner selection; existing steering settings and1.20/0.97 remain preserved. Engine/physical ignition state stays under owner control. **Moving road validation remains pending.**

## Completed staging phase (historical state before activation)

The new pair is staged and validated, **not activated**. Both staged repositories are clean, have independent Git object stores and the exact parent→child pin. Current installed software remains `ffebc43497f8015c37be5927800832f2719c7dca` / `0ac9618972dd580281c5e933c7990f186522fbd4`, Alpha0 and coordination preference absent. Owner1.20/0.97 and retained steering/geometry preserved. Powered baseline parked acceptance also passed after owner confirmed stationary Park, assistance disengaged and Alpha off. Staging and its pre-activation checks are complete.

## Exact publication and staging

- openpilot `e9ddc7668eb996f8c0912004facd66aed9206072` — existing adgower/openpilot `codex/navigator-tracking-release`.
- opendbc `d2e8d0404143da0f2685c2ff4932b9b9f702951f` — existing adgower/opendbc branch of the same name.
- Remote heads verified after the fast-forward pushes; incremental bundles verified against the exact installed pair. [Publication](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Staged source: `/data/navigator-validation/<private timestamp identifier>-e9ddc7668/source`.253LFS assets OID-verified;83unchanged steering/safety/geometry source files checked against live and candidate. Intentional controller/schema/CarState changes are verified by exact commits and behavioral tests.
- Git objects made independent using immutable object hardlinks; working files are separate copies. Installed firmware image and prebuilt/launcher behavior retained. No activation helper shipped or source exchange performed. [Preparation](../../navigator-reference/PRIVATE_ARTIFACTS.md); its original filename is a metadata-preparation receipt, not an activation record.

## Fresh rollback material

Private device backup `/data/navigator-backups/<private timestamp identifier>-pre-coordination`; Mac backup `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-coordination`.843,613,037-byte archive checksum verified;147manifest members checked; both nested source archives read through EOF. Source/settings/firmware/launchers and rollback refs retained. [Backup verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## ARM software evidence

Dedicated isolated unit completed successfully in1,679.3seconds: probe, normal device ARM build, native/controller/IPC replay all exit0.979native test cases passed,79skipped,12,083passing subtests;14parent smoke tests passed. Exact constructor selection, real producer/card calls and private schema IPC roundtrip passed; retained stale-provenance release and20/100Hz timing checks passed. New moving-entry, override, reversed-time, integral/fault contracts ran on ARM. [Acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The worker had a read-only active tree, private params/cache/home/shm, blocked vehicle USB/SPI and network, no privileges, resource limits and offroad/memory/disk guards. Minimum available memory remained about1.93GB; minimum free data about9.45GB. No forced hardware controls permission, manual CAN traffic, ECU query, OS update, firmware flashing, active-service stop or reboot.

Retained lateral pipeline fixture needed explicit initialization of the new **disabled** context and keyword-compatible stub. Original local fixture failed; adapted producer/card fixture smoke passed locally with IPC explicitly bypassed/labeled. The actual ARM private IPC test then passed. Assertions/product source were not weakened. [Fixture provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Preservation and parked evidence

After the ARM run and staging finalization, read-only audit verifies15selected settings, five learned-parameter hashes, seven source/firmware/launcher hashes, exact current clean pair and AGNOS20.1/B. Manager PID and live service unchanged through validation; only normal Athena-ping/offroad-uptime bookkeeping hashes changed. [Preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [runner comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Ignition-off acceptance of the still-current installed stack passed55seconds/551Panda samples: required telemetry alive/valid, no Panda/transport faults, no unexpected stopped processes and no new blocked-TX increments. Historical blocked-TX total6remained constant; it is not reported as six new failures. [Offroad parked receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Powered baseline Park acceptance passed55seconds:550Panda samples, all nine subscribed streams alive/valid, no vehicle/transport faults, no unexpected stopped processes, assistance disengaged and zero new blocked-TX increments. Model ran20.000Hz with no reported drops;1,100pose samples were healthy, maximum observed age40.33ms. Alpha remained0 and coordination preference absent. [Powered parked receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). These observations concern the existing installed stack. Candidate hardware/runtime acceptance requires later activation and another powered stationary check; road smoothness, physical brake release, grade/restart behavior and fuel efficiency remain unproven. Current Alpha remains off. No new-code road test is authorized by the staging result alone.
