<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# AGNOS 20.1 installation — October 23, 2026

**Current execution:** AGNOS **20.1/B** is booted and the published pair is activated: parent `24e981d6dd44ef11325f08846fbbba2d3ee53842`, child `01f32a6f66743f63ac02f1357141e5f7359b2825`. Fresh full ARM build passed, followed by 911 native/controller tests, 79 skips and 12,063 subtests; parent smoke checks passed 14 tests with six allowed base-class skips. Pipeline, stall and default-key checks passed. Runtime restoration rechecked exact clean pair, preferences and learned hashes; original firmware and launcher preserved. Owner **1.20/0.97** unchanged.

Passive ignition-off acceptance passed: 200 Panda samples, noOutput mode, assistance disabled, no faults, no invalid RX, blocked TX stable at zero, and no unexpected stopped processes. Initial UI-frame check received no messages with the screen asleep (backlight zero). Owner subsequently confirmed the normal home screen appears and responds. Powered display telemetry passed: 483 frames, 60.215 fps, median frame time 16.604 ms.

**Powered stationary acceptance passed** over 55.05 seconds in Park with assistance disabled: all 12 topics alive/valid, no alerts or vehicle faults, 551 healthy Panda samples with blocked TX and invalid RX both zero, no supply fault, and all expected processes running. Large model: 1,103 samples, 20.036 Hz, zero reported frame drops, mean execution 39.534 ms. Exact paired heads remained clean; owner Navigator preferences, stock longitudinal, Alpha off and initial cruise 40 kph confirmed. Calibration valid. This completes installation and parked acceptance; road behavior and 85 mph stability remain unproven. [Powered result](../../navigator-reference/PRIVATE_ARTIFACTS.md), [display result](../../navigator-reference/PRIVATE_ARTIFACTS.md).

All seven target B partitions were fully verified; all seven saved actual A hashes remain unchanged. Original source is retained at `/data/navigator-previous-agnos201-<private timestamp identifier>`; private backup is verified on Mac. Actual fallback boot is untested. [Device receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [offline status](../../navigator-reference/PRIVATE_ARTIFACTS.md), [ignition-off acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The following preparation record is historical and superseded by this execution status and [execution log](EXECUTION.md).

# AGNOS 20.1 preparation — October 23,2026

**Preparation passed. No OS writes, boot-slot change, reboot, service change or source activation.**

The updated paired branch is built/tested and published: parent `24e981d6dd44ef11325f08846fbbba2d3ee53842`, child `01f32a6f66743f63ac02f1357141e5f7359b2825`. Exact remote heads verified. Required OS20.1; current Comma remains20/A with source 26b3416/fe59e503. Owner 1.20/0.97, geometry and all five Navigator options retained. Updates paused, stock longitudinal/Alpha off.

## Ready evidence

- Fresh private843,597,916byte backup:67 parameters, archiveSHA256 and143 members verified on Mac. Whole current install remains live; rollback source/launcher/firmware preserved. Private copy under `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-observer-highway`.
- New separate source `/data/navigator-validation/<private timestamp identifier>-24e981d6d/source`:253 LFS assets verified; self-contained Git objects; clean exact pair; existing firmware preserved. No prior-OS native artifacts or prebuilt bypass. Fresh20.1build remains required.
- Official pinned boot/system images verified locally and on-device through compressed hash/size, decompressed stream hash, complete raw-image hash/size. Image files only staged; no partition write.
- Read-only14partition audit: inactive Bcommon partitions match20.1; **only boot_b/system_b need writes**. CurrentAboot/common full-check partitions match20manifest. Active20/A is retained untouched.
- Final preflight verifies exact live/candidate source, clean repositories, unchanged selected preferences, all five learned/cache hashes equal backup, unchanged launcher and signed firmware. Both authorization flags false.
- Full Mac checks for latest merge passed:1,021 parent tests/87skips/1expected failure/281subtests;4,424 child tests/1690skips/24673subtests; minimal/full/Panda builds pass.91protected steering/safety/context files unchanged. Independent merge/preparation reviews no material findings.

## Recovery and evidence limits

Active A system's raw hash differs from the original factory image; its exact difference is not diagnosed. Its staging marker is zero, consistent with pinned official agnos.swap clearing that marker before boot. The running root is mounted read-only; neither this nor the marker establishes factory raw identity. We retain actual hashes and the currently running20/A installation; an actual fallback boot is not tested. No write to A is proposed. The original20compressed image cache remains available.

The20-only graphics wrapper under/datais conditional on VERSION20 and remains unchanged; it will not force those graphics aliases on 20.1. New20.1display/runtime must be checked after boot. Mac recovery cables/screen access were owner-confirmed; factory recovery is not exercised.

The prior38172286f/01f32a6f candidate completed ARM build and911 native/controller tests/79skips/12063subtests plus14parent smoke tests/6base-class skips on20. It never activated. Its activation/preparation entry points have been retained under `.superseded` names to prevent stale activation. These results do not validate the new source or 20.1runtime.

## Proposed next action requiring explicit20.1 approval

Write only mismatching boot/system in inactive B, verify every target before slot selection, selectB and reboot under a maintenance hold. Keep active 20/A and original source for coordinated rollback. On20.1, perform fresh full native build, offline controller/native/pipeline checks with vehicle interfaces blocked; preserve firmware and owner settings; activate the exact published pair only after gates. Then ignition-off and powered stationary acceptance before any drive. A failed powered check is a stop/recovery condition.

No20.1OS-write or reboot authorization is inferred from the earlier20authorization. No OS-write/update runner has been executed or uploaded in this preparation.

[Final preflight](../../navigator-reference/PRIVATE_ARTIFACTS.md), [A/B audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verified images](../../navigator-reference/PRIVATE_ARTIFACTS.md), [staged images](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [master merge](../navigator-master-agnos201-integration-2026-10-23/REPORT.md).
