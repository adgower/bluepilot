# Personal Chestnut integration

## Status and scope

`codex/chestnut-personal` is a personal experimental BluePilot branch for a
comma four with the official Chestnut/GPU/power kit. It integrates SunnyPilot's
small- and big-model system, including the merged big-to-small fallback, while
preserving BluePilot's current Ford behavior.

This branch is not an official `bp-7.0` Chestnut release or compatibility
claim. It must pass the stationary and controlled-driving gates below before it
is considered usable on this vehicle.

## Reproducible source tuple

| Component | Pinned value |
| --- | --- |
| BluePilot base | `bp-dev@5f17cf389b1a48b09185a732564db11bd6477b58` |
| SunnyPilot source | `master@51987a62d07c44cc9e14b4d85dcb445edecd17d3` |
| Matching Sunny staging build | `staging-chestnut@6831cf5e79fe790c2559ad2ae590614038131ad1` |
| Sunny big-to-small fallback | PR #1974, merge `98ed8111f6bb5136aa1c7f0cf3078f3ac3a43210` |
| Sunny OpenPilot sync | merge `1dd5a7c91d9a82b18cdb117f8372568362814d06` |
| Incorporated OpenPilot commit | `4a13639cfd122ccb9113a4d6ce225dcbd8e61914` (`reduce chestnut states`, #38705) |
| AGNOS | `19.6`, manifest `openpilot/common/hardware/comma/agnos.json` |
| Chestnut firmware | `ed4e39b7` |
| Small/QCOM default | `CD210`, ref `5b6436a90cf6902b8aaa71c2b6f3d7164d8ae391` |
| Chestnut default | `Lebowski`, ref `fa0c6876d3cf070e91e25e5353ceadc68a5b3285` |
| Small model source | `driving_models_v21.json` |
| Chestnut model source | `driving_models_chestnut_v22.json` |
| Default small-model hash | `49133798d9cd9cacf47085c7ef8122bfee88cd9c6192a8314c81bfb1b37f5809` |
| opendbc upstream | `06743dfb39cff0f0cd5ddae244afef42891f4b93` plus the audited BluePilot Ford overlay |
| msgq | `e7396e76dadbb49e374d4b664ff6bbb43a39bcb0` |
| panda | `ea5a83a956d61c7540c1a13a8d76f08c24675d1b` |
| rednose | `28d4a7f69e80e1c3e0d24ca0733d7daeaeade3d0` |
| teleoprtc | `1aa8fc433bef1519a95c0700c96258c3be6dfb34` |
| tinygrad | `66ee3cfb4f3a3908a6a20ddfbec7774ba7c09b4e` |

The staging build is provenance evidence that the pinned Sunny source was
built by Sunny's Chestnut pipeline. This BluePilot branch is installed as an
on-device source build; it does not reuse Sunny's prebuilt artifact.

## Integration contract

- Sunny owns Chestnut detection, firmware qualification, hardware state,
  AGNOS, model catalogs, model downloads, and model runtimes.
- BluePilot consumes the canonical `ChestnutActive`, `ChestnutLoading`,
  `bigModelReady`, `chestnutState`, and `modelV2.big` state. It does not add a
  second hardware detector.
- The small and Chestnut model slots remain separate:
  `ModelManager_ActiveBundle` and `ModelManager_ActiveBundleChestnut`, with
  separate catalogs and caches.
- The legacy `ModelManager_ActiveBundleUSBGPU` key exists only as a one-way
  migration source for an older selection.
- `modeld_v2` warms the Chestnut model asynchronously while preparing the small
  fallback. A load timeout, runtime exception, or non-finite output clears
  `ChestnutActive`, marks subsequent output as non-big, and stays on the small
  model until the process or device restarts.
- Ford controls continue to consume ordinary model and planner messages. They
  do not branch on Chestnut state.

## BluePilot preservation boundary

The merge retains the current BluePilot portal, branding, BP UI subclasses,
ALP, angle-mode dampening, radar recovery, VIN/fingerprinting behavior, Sentry
diagnostics, and Ford controller/safety extensions. The Ford angle tune is
frozen for initial testing:

- high factor: `1.25`
- low factor: `1.29`

No steering, longitudinal, safety-limit, or vehicle-tuning change is part of
the Chestnut integration.

## Deliberately excluded follow-ups

- SunnyPilot #1965, AMD-over-USB lock retries, is not included because it was
  not merged into the pinned Sunny baseline.
- OpenPilot #38711, #38727, and #38706 are not cherry-picked directly.
- No later OpenPilot changes, BluePilot-specific detector, or parallel fallback
  implementation are included.

These changes should arrive through a future reviewed SunnyPilot sync rather
than bypassing the fork's upstream layer.

## Local verification evidence

The following checks were run on the merged source tree before publication:

- Git LFS checkout and `git lfs fsck`: complete and clean for all pinned model
  and UI artifacts.
- Full host `ZMQ=1` SCons build: passed, including cereal, model, panda firmware,
  replay, and UI build targets.
- Cereal service validation: 83 passed.
- Params migration and model-manager default tests: 54 passed, 1 skipped.
- Complete Sunny model-manager and `modeld_v2` test directories: 153 passed,
  1 skipped, including load-timeout, runtime-exception, and non-finite-output
  fallback coverage.
- BluePilot Ford controller, ALP, fingerprint, angle, and dampening tests plus
  the upstream Ford car test: 52 passed, 16 subtests passed.
- Manager/process registry, BluePilot UI/sound/theme, and portal smoke tests:
  44 passed, 1 skipped, with 2 existing warnings caused by test functions
  returning values.
- Migrated BluePilot and Ford Python trees: `compileall` passed.

These are host-source verification results. No comma-four/C3X/MICI hardware
build, device installation, stationary soak, rollback exercise, or road test
has been performed by this merge.

## Known Ford safety baseline exception

Sunny's current Ford safety test matrix exposes an existing BluePilot reset
bypass-latch test debt. The full merged matrix reports 22,759 failures, 474
passes, 285 skips, and 1,756 passing subtests. This is not treated as a green
safety suite.

To separate merge regression from inherited behavior, the exact Ford safety
test file from pinned BluePilot `bp-dev@5f17cf389` was run twice: once against
the exact pinned BluePilot safety implementation and once against the merged
safety implementation. Both runs produced the identical result: 22,556
failures, 487 passes, 279 skips, and 1,930 passing subtests. The merged branch
therefore preserves the pinned BluePilot behavior for that exact matrix, but
does not resolve or waive the underlying test debt. Changing the safety latch
was outside this Chestnut-only merge and is intentionally deferred for a
separate review.

Device installation remains gated on explicitly accepting this known baseline
exception and completing the offroad, rollback, and controlled-driving checks
below.

## Installation and rollback gate

1. Confirm SSH/device recovery and save the current `bp-dev` installer path.
2. Power down and disconnect Chestnut.
3. Install `codex/chestnut-personal` and let it build while parked on external
   power. Accept only the pinned upstream AGNOS path while offroad.
4. Confirm the displayed branch/commit, Ford detection, UI, logger, updater,
   and small-model operation.
5. Reinstall `bp-dev` and confirm it boots, then reinstall this branch. This
   exercises rollback before Chestnut is introduced.
6. Power down, attach the official Chestnut/GPU/power setup, and boot parked.
7. Confirm firmware, telemetry, model integrity, `bigModelReady`, and
   `ChestnutActive` before a 30-minute stationary soak.
8. Test upstream-supported big-to-small failure handling while stationary.
   Never hot-unplug the hardware while driving.
9. Reboot without Chestnut and confirm normal small-model startup.

Driving starts with the small model on a short route. Repeat the same route with
the Sunny big model without changing the vehicle, tires, controller mode, tune,
or other BluePilot settings. Roll back immediately for stale model output,
unexplained steering behavior, repeated model restarts, hardware faults,
thermal or power instability, or failure to return cleanly to the small model.

## Evidence still required on the physical kit

Repository tests and local builds do not prove comma-four, AGNOS, USB, thermal,
power, or on-road behavior. Final acceptance requires a normal no-Chestnut
drive, reliable offroad Chestnut activation, verified fallback, an exercised
`bp-dev` rollback, and no unexplained Ford behavior change with the frozen tune.
