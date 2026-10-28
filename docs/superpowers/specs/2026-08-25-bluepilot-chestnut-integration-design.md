<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# BluePilot Chestnut Integration Design

**Status:** Waiting for SunnyPilot to finish and publish its Chestnut upstream sync

**Audience:** A BluePilot maintainer who understands basic Git use but does not need prior knowledge of openpilot's Chestnut implementation.

**Research basis:** [`docs/research/chestnut-egpu-big-model-compatibility.md`](../../research/chestnut-egpu-big-model-compatibility.md)

## Current decision — 2026-08-28

Continue watching upstream; do not start the BluePilot production branch yet.

The specific wait is for SunnyPilot to make its complete Chestnut contract part of a reproducible release/build baseline. Openpilot already renamed the generic eGPU/`usbgpu` interfaces to Chestnut and hardened stock fallback. SunnyPilot's current `master` still exposes the old names, while [SunnyPilot #1973](https://github.com/sunnypilot/sunnypilot/pull/1973) is the pending 40-file bridge across `modeld_v2`, model-manager keys, migrations, UI, SunnyLink, and model-build workflows.

This does **not** prohibit preparation. Research, conflict mapping, disposable merge spikes, and test-design work may continue. It prohibits merging a Chestnut claim into `bp-dev`/`bp-7.0` or installing an unqualified source build on the comma four.

## Goal

Add production-quality Chestnut eGPU and big-model support to BluePilot on comma four by synchronizing official openpilot and SunnyPilot releases into `bp-dev`, while preserving BluePilot's Ford behavior and retaining a safe small-model fallback.

The first release is complete only when it can be installed through a dedicated BluePilot prebuilt channel, validated offroad and onroad, and rolled back without opening the repository or repairing the device manually.

## Plain-language mental model

- **openpilot** owns the core comma-four, AGNOS, Chestnut firmware, USB/PCIe, tinygrad, stock model runtime, and safety behavior.
- **SunnyPilot** adapts that stack to its alternate model runtime, downloadable model catalogs, model selection, SunnyLink, and prebuilt release workflow.
- **BluePilot** should synchronize those upstream implementations, resolve conflicts with its Ford and UI customizations, and validate the combined system. BluePilot should not independently recreate Chestnut.

This is therefore an upstream merge project, not a copy-and-paste project. Copying individual files can silently omit schema changes, build inputs, firmware payloads, process registration, release metadata, or failure handling.

## Terms used in the implementation guides

- **Upstream:** The project BluePilot receives code from. SunnyPilot is BluePilot's immediate upstream; openpilot is SunnyPilot's upstream.
- **Pinned baseline:** One exact release tag and commit SHA. Branch names such as `master` are not sufficient because they move.
- **Prebuilt:** A device-installable branch whose required native binaries and model artifacts have already been built.
- **Small model:** The normal model that runs on comma four without Chestnut.
- **Big model:** The Chestnut-class model that runs primarily on the external AMD GPU.
- **Fallback:** Automatically continuing with the small model when the big model cannot start or stops working.
- **Release tuple:** The complete tested combination of BluePilot commit, SunnyPilot commit, openpilot base, AGNOS version, tinygrad commit, Chestnut firmware, model catalog/model hash, and GPU.

## Scope decomposition

The work will be delivered as five sequential sub-projects. Each one must produce a reviewable and testable result before the next begins.

1. **Upstream baseline and source synchronization**
2. **Chestnut hardware, firmware, operating-system, and telemetry foundation**
3. **Stock openpilot model runtime and small-model fallback**
4. **SunnyPilot big-model distribution and optional `modeld_v2` support**
5. **BluePilot device validation, prebuilt release, installation, and rollback**

There will be one detailed implementation plan per sub-project. This keeps failures attributable and prevents a single very large merge from being mistaken for a working integration.

### Expected pull-request sequence

1. **PR 1 — upstream baseline only:** synchronize the selected SunnyPilot release into an isolated branch, preserve BluePilot behavior, and prove the small-model build. Do not advertise Chestnut support.
2. **PR 2 — Chestnut platform contract:** bring in AGNOS, firmware, USB/PCIe, cereal, Params, telemetry, alerts, and the complete `usbgpu`-to-`chestnut` migration.
3. **PR 3 — stock model runtime:** enable the official big model with the stock startup/runtime small-model fallback and failure-injection tests.
4. **PR 4 — SunnyPilot model distribution:** add separate small/Chestnut catalogs, downloads, selection persistence, build artifacts, and SunnyLink identity.
5. **PR 5 — optional `modeld_v2`:** enable custom big models only after equivalent fallback is implemented and tested; otherwise keep this path visibly experimental.
6. **PR 6 — BluePilot release channel:** add the minimal BP UI wiring, prebuilt channel, install/rollback documentation, and recorded device-validation evidence.

Each PR depends on the preceding PR and must remain independently reviewable. Ford steering and longitudinal tuning are not part of any Chestnut PR.

## Start gates

### Experimental integration-spike gate

An isolated, non-installable spike may begin when all of the following are true:

1. SunnyPilot merges #1973 or a successor that incorporates openpilot's `ChestnutActive`/`ChestnutLoading`, `chestnut_*` helpers, UI state, model-manager keys, and migration.
2. The merged SunnyPilot commit has a successful `dev-chestnut` or `staging-chestnut` prebuilt generated from that same master commit.
3. No open SunnyPilot regression says that the default Chestnut model cannot load, publish healthy `modelV2`, or return to the stock small model.
4. The exact SunnyPilot commit and its incorporated openpilot commit are recorded before any merge begins.

The spike is source/conflict evidence only. It remains in a disposable worktree, is not merged into `bp-dev` or `bp-7.0`, and is not installed on the comma four.

### Production integration-branch gate

The integration may be researched before the trigger, but the production branch starts only after the following are true:

1. Comma publishes an official Chestnut-capable openpilot release branch or release tag.
2. SunnyPilot publishes a formal release tag containing its Chestnut runtime, Chestnut prebuilt workflow, Chestnut model catalog, model-selection persistence fixes, and legacy-parameter migration.
3. The exact SunnyPilot release commit builds a Chestnut prebuilt successfully in its own CI.
4. The release documents or source identifies the required AGNOS, tinygrad, Chestnut firmware, and default big model.
5. No known open SunnyPilot Chestnut regression blocks startup, fallback, catalog selection, or release publishing.

If SunnyPilot has not tagged a formal release, an experimental spike may pin a staging tag, but that build must remain visibly experimental and must not be merged into `bp-7.0`.

### Current upstream watchlist

- **SunnyPilot #1973:** must merge, or be replaced by an equivalent sync, before BluePilot treats `Chestnut*` names as the SunnyPilot contract.
- **SunnyPilot #1965:** retry-only mitigation for AMD-over-USB lock contention. Its merge is useful but does not satisfy `modeld_v2` fallback.
- **Openpilot #38706:** offroad Chestnut alerts. If it lands after SunnyPilot's selected sync point, include it in the next platform-contract sync rather than hand-copying only its UI strings.
- **Openpilot #38711:** supply-fault logging is already merged and must be present in the selected SunnyPilot/openpilot baseline or explicitly accounted for in PR 2.
- **Formal releases/builds:** a branch name is not enough. Record the exact release tag, source SHA, prebuilt SHA, AGNOS, tinygrad, firmware, and default model.

The stock runner and `modeld_v2` have separate readiness decisions. A production-quality stock-model Chestnut integration can proceed while custom `modeld_v2` remains disabled; lack of `modeld_v2` fallback must not be hidden behind a general “Chestnut supported” label.

## Source-of-truth rules

When two implementations conflict, use this ownership order:

1. Take comma's current implementation for AGNOS, Chestnut detection, firmware, telemetry, core build behavior, and stock `modeld` safety behavior.
2. Take SunnyPilot's current implementation for `modeld_v2`, model catalogs, model downloads, per-catalog selection, SunnyLink, and SunnyPilot prebuilt publication.
3. Add BluePilot code only for necessary Ford/UI integration and release identity.
4. Do not modify Ford steering or longitudinal algorithms merely because the model runtime changed.
5. Mark unavoidable changes to upstream-owned files using BluePilot's documented `# BluePilot:` / `# End BluePilot` convention where the file type supports comments.

## Architecture and boundaries

The dependency flow is one-way:

```text
AGNOS + Chestnut firmware + USB/PCIe qualification
                         ↓
          openpilot/SunnyPilot model runtime
                         ↓
 modelV2 + chestnutState + ChestnutLoading/ChestnutActive
                         ↓
          ordinary controls and BluePilot UI
```

Ford controller code consumes the same model and planner messages regardless of whether the small or big model produced them. It must not query Chestnut USB state, GPU type, firmware version, or model catalog.

BluePilot UI and portal code may display canonical `chestnutState`, `modelV2.big`, `ChestnutLoading`, and `ChestnutActive` state. It must not maintain a second independent determination of whether Chestnut is working.

Legacy SunnyPilot `UsbGpu*`, `usbgpu`, and `ModelManager_*USBGPU` names are migration inputs only. New BluePilot code must use the canonical Chestnut names from the selected upstream release and must preserve SunnyPilot's one-time parameter migration so existing selections are not silently lost.

## Sub-project 1: Upstream baseline and source synchronization

### Purpose

Move `bp-dev` onto a reproducible SunnyPilot/Openpilot baseline before enabling Chestnut.

### Design

1. Record the starting BluePilot `bp-dev` SHA.
2. Record the chosen formal SunnyPilot release tag and SHA.
3. Record the openpilot commit incorporated by that SunnyPilot release.
4. Create an isolated integration worktree and a branch from `bp-dev`.
5. Produce a path and conflict map before resolving any merge conflict.
6. Resolve upstream files in favor of the chosen SunnyPilot release, then reapply the smallest necessary BluePilot customizations.
7. Keep Chestnut disabled while proving the normal small-model build and Ford behavior still work.

### Expected source areas

The exact paths can move between releases. Current SunnyPilot uses an `openpilot/` source root while current BluePilot does not, so the implementation plan must regenerate this map from the selected release instead of assuming today's paths.

Areas include versioning, `launch_env.sh`, cereal schemas/services, Params keys, `system/hardware`, `selfdrive/modeld`, `sunnypilot/modeld_v2`, `sunnypilot/models`, UI state/renderers, release tooling, workflows, submodules, and BluePilot's upstream-file touchpoints.

### Gate

A comma four and supported non-Chestnut BluePilot configurations build and operate using the small model. No Chestnut installation occurs in this sub-project.

## Sub-project 2: Hardware, firmware, AGNOS, and telemetry

### Purpose

Make Chestnut a correctly identified and managed comma-four peripheral before attempting big-model inference.

### Design

Synchronize the chosen upstream versions of:

- AGNOS selection and compatibility requirements;
- supported runtime and ROM USB identifiers;
- exact firmware product-string/hash qualification;
- production and recovery firmware payloads;
- offroad-only firmware flashing and upgrade behavior;
- PCIe-link readiness probing;
- `hardwared` integration and branch/model warnings;
- cereal service/schema entries and Chestnut metrics;
- canonical Params such as `ChestnutLoading` and `ChestnutActive`, plus the selected SunnyPilot release's migration from legacy `UsbGpu*`/`*USBGPU` keys.

Firmware mutation is permitted only while offroad. A firmware error must produce a clear offroad status and must never produce an apparently active big-model state.

### Gate

On comma four, repeated power cycles detect the official ready-to-drive Chestnut hardware, distinguish runtime and recovery states, qualify or update firmware offroad, and report stable telemetry. The device must still boot normally when Chestnut is absent.

## Sub-project 3: Stock model runtime and fallback

### Purpose

Establish the safest known inference path before adding SunnyPilot's selectable model system.

### Design

Synchronize the official stock-model contract as one coherent unit:

- current big-model artifact layout;
- protocol-5 out-of-band/chunked loading;
- QCOM camera warp and AMD policy execution;
- USB/PCIe build probing and tinygrad compiler settings;
- asynchronous big-model load and warmup deadline;
- `modelV2.big`, Chestnut telemetry, and loading/active state;
- non-finite output rejection;
- preloaded small-model fallback after startup or runtime failure.

The first hardware inference build uses the upstream official Chestnut model. It does not yet add a selectable catalog. This isolates hardware/runtime problems from model-manager problems.

### Gate

The official big model starts and publishes healthy output. Forced load failure, forced runtime failure, invalid output, and eGPU loss result in the small-model path without stale big-model messages. Restarting the device without Chestnut also uses the small model normally.

## Sub-project 4: SunnyPilot model distribution and `modeld_v2`

### Purpose

Add SunnyPilot's big-model catalog, downloads, persistence, and optional alternate runtime without weakening the stock fallback contract.

### Design

Synchronize the selected release's:

- separate normal and USB-GPU catalogs;
- default small/big model resolver;
- chunk download, integrity verification, and cache isolation;
- per-catalog model-selection persistence;
- Chestnut connect/disconnect model-state updates;
- SunnyLink model identity;
- big-model build runner and prebuilt publication workflow;
- tinygrad-reference and Git LFS validation.

`modeld_v2` is enabled for the production release only if the selected SunnyPilot release has equivalent startup and runtime fallback to stock `modeld`, or BluePilot adds that behavior with tests and comma-four failure injection. Otherwise stock `modeld` remains the first supported runtime and `modeld_v2` stays experimental.

### Gate

Downloads survive interruption and reboot, hashes are verified, small and big selections remain separate, Chestnut power-state changes select the correct catalog, and failure returns to a known working model.

## Sub-project 5: BluePilot integration, installation, and release

### Purpose

Expose useful status, validate Ford behavior, and deliver a rollback-ready installation channel.

### Design

1. Wire BluePilot displays to canonical upstream runtime state.
2. Keep existing Ford controller settings unchanged for the first comparison.
3. Produce a dedicated BluePilot Chestnut prebuilt branch; do not initially publish it as `bp-7.0`.
4. Verify the branch can be installed and updated using BluePilot's normal comma-four installation mechanism.
5. Publish the exact release tuple and a tested rollback URL/branch.
6. Promote to a BluePilot release branch only after the validation matrix and soak period pass.

### Installation ladder

The comma four installation proceeds in increasing-risk stages:

1. Install the integration prebuilt with Chestnut physically disconnected.
2. Verify boot, UI, Ford detection, small-model operation, logging, update behavior, and rollback.
3. Park and power the device offroad; connect Chestnut and verify firmware/update state.
4. Verify big-model compilation/download/loading while offroad.
5. Verify active/inactive transitions while stationary.
6. Perform a short controlled drive using the small model.
7. Repeat the same route using the big model with identical vehicle settings.
8. Expand road testing only when logs and safety metrics match the release criteria.

At every stage, failure returns to the previous known-good branch or small-model mode. Installation is not attempted from a source branch that lacks a successful prebuilt artifact.

## Ford tuning rule

The initial comparison freezes `FordHighSpeedFactor_ang=1.25` and `FordLowSpeedFactor_ang=1.29`.

The big model may generate a different desired path, but these factors belong to the Ford steering controller. Changing both the model and controller tuning would make results uninterpretable. Retuning is a later, separately designed experiment only if repeated same-route comparisons show a controller-level issue.

## Validation matrix

### Build and static validation

- Clean comma-four release build with real Git LFS model assets.
- SunnyPilot model-manager, model-fetcher, default-model, tinygrad-ref, compiler, and recovery-power tests.
- Cereal generation and service registration.
- BluePilot Ford and UI tests affected by upstream synchronization.
- SunnyPilot process replay with no unexplained model/control changes.
- C3X/MICI build regression check even though Chestnut is comma-four-only.

### Offroad hardware validation

- Boot with Chestnut absent, already powered, late powered, and recovery-mode firmware.
- Repeated 12 V power cycles.
- Firmware match, mismatch, upgrade, and recovery.
- PCIe link delay and link failure.
- Complete, interrupted, corrupted, and cached model downloads.
- Big-model load success and timeout.
- Correct status across connect/disconnect and reboot.

### Stationary runtime validation

- Big and small model startup.
- Forced GPU runtime exception.
- Non-finite output.
- Loss of telemetry.
- No stale model output during fallback.
- Correct process restart behavior.
- Thermal, memory, power, and model-frequency logging.

### Onroad validation

- Small model before big model.
- Angle and curvature modes where supported.
- Same car, route, weather range, tire configuration, and controller parameters.
- Lane keeping, curves, lane changes, lead response, engagement/disengagement, and driver override.
- Review logs before widening the test envelope.

## Promotion criteria

The integration can be promoted only when all of the following are documented:

- A complete release tuple.
- A reproducible successful prebuilt.
- Successful install and rollback on comma four.
- Normal boot and small-model behavior without Chestnut.
- Correct firmware management and big-model behavior with Chestnut.
- Automatic, tested fallback with no stale output.
- No unexplained Ford regression using the frozen initial tune.
- No C3X/MICI build regression.
- A defined soak period completed without a release-blocking issue.

## Non-goals

- Supporting Chestnut on comma 3X/MICI when comma has not declared that hardware combination supported.
- Supporting arbitrary GPUs or power supplies in the first BluePilot release.
- Retuning Ford angle or curvature control during Chestnut bring-up.
- Rewriting upstream Chestnut detection, firmware, model runtime, or model-catalog code as BluePilot-specific implementations.
- Merging an experimental staging spike directly into `bp-7.0`.

## User-visible outcome

For the user, the final workflow should be simple:

1. Select the documented BluePilot Chestnut install channel.
2. Install it on comma four while parked.
3. Confirm normal operation without Chestnut.
4. Connect the documented Chestnut/GPU/power combination while offroad.
5. Allow firmware and model preparation to finish.
6. Confirm the UI reports the big model active.
7. Drive using the existing Ford tune.
8. Use the documented rollback channel if any gate fails.

The engineering work is deliberately more complex so that this final user workflow can be simple and recoverable.
