<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# BluePilot Chestnut Upstream-Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver rollback-ready Chestnut and official big-model support on comma four without regressing BluePilot's normal small-model path or Ford controls.

**Architecture:** SunnyPilot is the immediate upstream and owns the fork-specific model manager, catalog, `modeld_v2`, UI, SunnyLink, and prebuilt adaptations; openpilot remains authoritative for Chestnut hardware, firmware, AGNOS, telemetry, and stock-model fallback. Integrate the selected upstream release as a sequence of reviewable PRs, keeping BluePilot additions at the outer layer and treating stock `modeld` and custom `modeld_v2` as separate production gates.

**Tech Stack:** Git worktrees, Python 3, SCons, pytest, cereal/Cap'n Proto, tinygrad, Git LFS, GitHub Actions, comma four, AGNOS, Chestnut firmware and AMD GPU.

**Spec:** `docs/superpowers/specs/2026-08-25-bluepilot-chestnut-integration-design.md`

## Global Constraints

- Do not execute this production plan until the spec's production integration-branch gate passes.
- Base BluePilot work on the then-current `upstream/bp-dev`, never directly on `bp-7.0`.
- Pin every upstream input by immutable tag and SHA; never use a moving branch as release evidence.
- Use canonical `ChestnutActive`, `ChestnutLoading`, `chestnut_*`, and `ModelManager_*Chestnut` names; legacy `UsbGpu*`/`usbgpu` names are migration inputs only.
- Preserve stock openpilot's preloaded small-model startup and runtime fallback.
- Keep custom `modeld_v2` disabled for production until it has equivalent tested fallback.
- Freeze `FordHighSpeedFactor_ang=1.25` and `FordLowSpeedFactor_ang=1.29` throughout initial A/B validation.
- Do not alter Ford lateral or longitudinal algorithms as part of Chestnut integration.
- Perform firmware writes and model preparation only while offroad.
- Do not install a source branch; install only a successful comma-four prebuilt with a tested rollback target.

---

### Task 1: Freeze the release tuple and create the isolated integration branch

**Files:**
- Create: `docs/chestnut/release-baseline.json`
- Create: `docs/chestnut/upstream-path-map.md`
- Verify: `docs/superpowers/specs/2026-08-25-bluepilot-chestnut-integration-design.md`

**Interfaces:**
- Consumes: the first SunnyPilot formal release satisfying the production gate.
- Produces: an immutable release tuple and `codex/chestnut-upstream-sync` worktree used by every later task.

- [ ] **Step 1: Verify the upstream gates against primary sources**

Run:

```bash
git ls-remote --tags https://github.com/sunnypilot/sunnypilot.git 'v2026.*'
git ls-remote https://github.com/sunnypilot/sunnypilot.git refs/heads/master refs/heads/staging-chestnut refs/heads/dev-chestnut
git ls-remote https://github.com/commaai/openpilot.git refs/heads/master refs/heads/release-chestnut
```

Expected: identify one formal SunnyPilot tag whose source commit and matching Chestnut prebuilt satisfy every start gate in the spec. Stop if there is only a staging branch or if a blocking Chestnut regression remains open.

- [ ] **Step 2: Fetch immutable BluePilot and SunnyPilot refs without changing the existing checkout**

Run:

```bash
git fetch upstream --prune --tags
git fetch https://github.com/sunnypilot/sunnypilot.git refs/tags/$SUNNY_TAG:refs/tags/research/$SUNNY_TAG
```

Expected: `upstream/bp-dev` and `refs/tags/research/$SUNNY_TAG` both resolve locally. Set `SUNNY_TAG` to the formal tag verified in Step 1 before running the second command.

- [ ] **Step 3: Record the release tuple**

Collect the immutable source values first:

```bash
git rev-parse upstream/bp-dev
git rev-parse refs/tags/research/$SUNNY_TAG^{}
git show refs/tags/research/$SUNNY_TAG:system/hardware/tici/agnos.json
git ls-tree refs/tags/research/$SUNNY_TAG tinygrad_repo
git ls-tree -r refs/tags/research/$SUNNY_TAG system/hardware/chestnut
```

Use `apply_patch` to create `docs/chestnut/release-baseline.json` with objects named `bluepilot`, `sunnypilot`, `openpilot`, `agnos`, `tinygrad`, `chestnut`, and `default_big_model`. Record the exact tag, source/prebuilt commits, versions, refs, and SHA-256 digests returned by the pinned source and release artifacts. Validate every commit as 40 lowercase hexadecimal characters and every SHA-256 value as 64 lowercase hexadecimal characters. Stop rather than guessing a missing value.

- [ ] **Step 4: Create the isolated worktree**

Run using the `superpowers:using-git-worktrees` skill:

```bash
git worktree add ../bluepilot-chestnut -b codex/chestnut-upstream-sync upstream/bp-dev
```

Expected: the current `feature-sac` checkout and its untracked research documents remain untouched.

- [ ] **Step 5: Generate the path and conflict map before resolving anything**

Run from the new worktree:

```bash
git merge --no-commit --no-ff refs/tags/research/$SUNNY_TAG
git diff --name-only --diff-filter=U
git status --short
```

Record every conflict under these ownership groups in `docs/chestnut/upstream-path-map.md`: upstream platform, SunnyPilot extension, BluePilot UI/portal, Ford/opendbc, generated assets, submodules/LFS, and release tooling. Abort the exploratory merge after recording the map; the actual resolution begins in Task 2.

- [ ] **Step 6: Commit only the baseline evidence**

```bash
git add docs/chestnut/release-baseline.json docs/chestnut/upstream-path-map.md
git commit -m "docs: pin chestnut integration baseline"
```

---

### Task 2: Synchronize SunnyPilot while keeping the small model authoritative

**Files:**
- Modify: all paths listed in `docs/chestnut/upstream-path-map.md`
- Modify: `launch_env.sh`
- Modify: `common/params_keys.h`
- Modify: `system/manager/process_config.py`
- Test: `cereal/messaging/tests/validate_sp_cereal_upstream.py`

**Interfaces:**
- Consumes: the immutable baseline and conflict ownership map from Task 1.
- Produces: a BluePilot branch structurally synchronized with SunnyPilot that builds and runs the ordinary small model with Chestnut disconnected.

- [ ] **Step 1: Start the real merge from the clean Task 1 commit**

```bash
git merge --no-ff refs/tags/research/$SUNNY_TAG
```

Expected: only the conflicts already categorized in the path map; stop and update the map if new conflict classes appear.

- [ ] **Step 2: Resolve upstream-owned files from the pinned SunnyPilot release**

For platform, cereal, model runtime, SunnyPilot extensions, workflows, submodules, and LFS pointers, take the selected SunnyPilot release as the baseline. Reapply BluePilot changes only where the path map identifies a documented BluePilot responsibility.

- [ ] **Step 3: Preserve BluePilot's outer-layer seams**

Verify:

```bash
rg -n "BluePilot:|End BluePilot" selfdrive system common cereal
rg -n "class .*BP|from .*\.bp\." selfdrive/ui bluepilot
```

Expected: BluePilot UI overrides and additive processes remain explicit; no new Chestnut logic is added to Ford controller files.

- [ ] **Step 4: Prove the small-model source/build path before enabling Chestnut**

Run:

```bash
scons -j$(sysctl -n hw.ncpu) selfdrive/modeld/ cereal/ system/manager/
pytest -q cereal/messaging/tests/test_services.py cereal/messaging/tests/validate_sp_cereal_upstream.py
```

Expected: build and tests pass with no Chestnut hardware requirement.

- [ ] **Step 5: Verify Ford controller scope did not drift**

```bash
git diff --stat upstream/bp-dev -- opendbc_repo/opendbc/car/ford selfdrive/car
git diff upstream/bp-dev -- opendbc_repo/opendbc/car/ford selfdrive/car
```

Expected: every change is attributable to the pinned SunnyPilot/opendbc sync or preservation of existing BluePilot behavior; no tuning change is introduced.

- [ ] **Step 6: Commit the baseline sync as PR 1**

```bash
git add -A
git commit -m "sync: update bluepilot to chestnut-ready sunnypilot baseline"
```

PR 1 must explicitly say that it does not yet claim Chestnut compatibility.

---

### Task 3: Integrate the Chestnut platform contract and legacy migration

**Files:**
- Modify: `common/params_keys.h`
- Modify: `cereal/log.capnp`
- Modify: `cereal/services.py`
- Modify: `system/hardware/hardwared.py`
- Modify: `sunnypilot/system/params_migration.py`
- Test: `cereal/messaging/tests/test_services.py`
- Create or synchronize: `sunnypilot/system/tests/test_params_migration.py`
- Create or synchronize: `system/hardware/chestnut/`

**Interfaces:**
- Consumes: the selected upstream hardware implementation and canonical Chestnut names.
- Produces: `deviceState.chestnutPresent`, `chestnutState`, `ChestnutLoading`, `ChestnutActive`, qualified firmware state, and migrated model-manager selections.

- [ ] **Step 1: Write migration tests before changing Params**

Add tests asserting:

```python
def test_migrates_legacy_chestnut_bundle_once():
  legacy = {"ref": "big-model"}
  params.put("ModelManager_ActiveBundleUSBGPU", legacy)
  run_migration(params)
  assert params.get("ModelManager_ActiveBundleChestnut") == legacy

def test_does_not_overwrite_existing_chestnut_bundle():
  params.put("ModelManager_ActiveBundleUSBGPU", {"ref": "old"})
  params.put("ModelManager_ActiveBundleChestnut", {"ref": "new"})
  run_migration(params)
  assert params.get("ModelManager_ActiveBundleChestnut") == {"ref": "new"}
```

- [ ] **Step 2: Run the migration tests and confirm the pre-port failure**

```bash
pytest -q sunnypilot/system/tests/test_params_migration.py
```

Expected: the new assertions fail because canonical Chestnut keys/migration are not yet fully wired.

- [ ] **Step 3: Synchronize hardware, firmware, schema, service, Params, alerts, and supply-fault logging as one unit**

Bring in the selected release's complete `system/hardware/chestnut/` implementation and corresponding `hardwared`, cereal, service, Param, firmware, and alert changes. Do not create a BluePilot-specific hardware detector.

- [ ] **Step 4: Implement the one-way legacy migration**

Migration behavior must be: canonical value wins; otherwise copy the legacy selection once; never copy canonical state back to a legacy key.

- [ ] **Step 5: Run schema, migration, and hardware tests**

```bash
pytest -q cereal/messaging/tests/test_services.py sunnypilot/system/tests/test_params_migration.py system/hardware/tests
scons -j$(sysctl -n hw.ncpu) cereal/ system/hardware/
```

Expected: generated messaging/service definitions and migration tests pass without physical Chestnut hardware.

- [ ] **Step 6: Commit the platform contract as PR 2**

```bash
git add common/params_keys.h cereal system/hardware sunnypilot/system
git commit -m "feat: integrate chestnut platform contract"
```

---

### Task 4: Enable the official stock big model with automatic fallback

**Files:**
- Modify: `selfdrive/modeld/SConscript`
- Modify: `selfdrive/modeld/modeld.py`
- Modify: `selfdrive/modeld/helpers.py`
- Create: `selfdrive/modeld/tests/test_chestnut_fallback.py`

**Interfaces:**
- Consumes: qualified Chestnut hardware state and official model artifacts.
- Produces: healthy `modelV2`, `modelV2.big`, and one-way big-to-small fallback for startup, runtime exceptions, non-finite output, and device loss.

- [ ] **Step 1: Write failure-injection tests first**

Create tests for four cases: big-model load timeout selects small; runtime exception selects small; non-finite output selects small; Chestnut disappearance selects small. Each test must assert that `ChestnutActive` becomes false and the next published `modelV2.big` is false.

- [ ] **Step 2: Run the tests and verify the unsupported cases fail**

```bash
pytest -q selfdrive/modeld/tests/test_chestnut_fallback.py
```

- [ ] **Step 3: Synchronize the stock upstream runtime without redesigning it**

Keep QCOM camera warp, AMD policy execution, asynchronous big load, preloaded small `ModelState`, runtime swap, invalid-output rejection, and `chestnutState` publication together. Do not port only the USB detection or build flags.

- [ ] **Step 4: Run focused tests and build**

```bash
pytest -q selfdrive/modeld/tests/test_chestnut_fallback.py
scons -j$(sysctl -n hw.ncpu) selfdrive/modeld/
```

- [ ] **Step 5: Commit the stock runtime as PR 3**

```bash
git add selfdrive/modeld
git commit -m "feat: add chestnut stock model fallback"
```

---

### Task 5: Integrate SunnyPilot Chestnut catalogs and artifact publication

**Files:**
- Modify: `sunnypilot/models/default_model.py`
- Modify: `sunnypilot/models/fetcher.py`
- Modify: `sunnypilot/models/helpers.py`
- Modify: `sunnypilot/models/manager.py`
- Modify: `selfdrive/ui/sunnypilot/layouts/settings/models.py`
- Modify: `.github/workflows/build-all-tinygrad-models.yaml`
- Modify: `.github/workflows/build-single-tinygrad-model.yaml`
- Modify: `.github/workflows/sunnypilot-build-model.yaml`
- Modify: `.github/workflows/sunnypilot-build-prebuilt.yaml`
- Test: `sunnypilot/models/tests/test_default_model.py`
- Create or synchronize: `sunnypilot/models/tests/test_manager_download.py`
- Test: `sunnypilot/models/tests/test_tinygrad_ref.py`

**Interfaces:**
- Consumes: canonical Chestnut presence/runtime state and pinned model catalog.
- Produces: independent QCOM/Chestnut catalogs, caches, selections, verified downloads, SunnyLink identity, and reproducible build artifacts.

- [ ] **Step 1: Add failing source-separation tests**

Tests must prove that QCOM and Chestnut return different manifests/cache keys, selecting one never writes the other slot, existing Chestnut selection survives reboot, and a legacy USBGPU selection migrates without overwriting a canonical selection.

- [ ] **Step 2: Run focused tests to establish the failure baseline**

```bash
pytest -q sunnypilot/models/tests/test_default_model.py sunnypilot/models/tests/test_manager_download.py sunnypilot/models/tests/test_tinygrad_ref.py
```

- [ ] **Step 3: Synchronize the selected SunnyPilot model-manager contract**

Use `qcom` and `chestnut` as the only new source identifiers. Preserve independent catalog URLs, cache timestamps, active bundles, chunk integrity, download references, and default-model resolution.

- [ ] **Step 4: Synchronize build and publication workflows**

Require the Chestnut runner label, exact tinygrad ref, real Git LFS objects, model hash verification, and prebuilt publication from the same source SHA recorded in `release-baseline.json`.

- [ ] **Step 5: Run model-manager tests and validate workflow syntax**

```bash
pytest -q sunnypilot/models/tests
python -m compileall -q sunnypilot/models
```

Expected: source separation, persistence, downloads, and tinygrad-ref tests pass.

- [ ] **Step 6: Commit model distribution as PR 4**

```bash
git add sunnypilot/models selfdrive/ui/sunnypilot/layouts/settings/models.py .github/workflows
git commit -m "feat: add chestnut model distribution"
```

---

### Task 6: Gate custom `modeld_v2` behind equivalent fallback

**Files:**
- Modify: `sunnypilot/modeld_v2/modeld.py`
- Modify: `sunnypilot/modeld_v2/compile_modeld.py`
- Create or synchronize: `sunnypilot/modeld_v2/tests/test_chestnut_load.py`
- Create: `sunnypilot/modeld_v2/tests/test_chestnut_fallback.py`

**Interfaces:**
- Consumes: separate QCOM/Chestnut bundles and canonical runtime state.
- Produces: either tested automatic fallback for custom big models or an explicit production-disable gate.

- [ ] **Step 1: Write startup, retry, runtime, and invalid-output tests**

Tests must distinguish retryable AMD lock contention from non-retryable load failure, assert bounded retry timing, instantiate a compatible small bundle before engagement, and assert one-way fallback with no return to the big model until the next drive.

- [ ] **Step 2: Run the tests against the synchronized upstream implementation**

```bash
pytest -q sunnypilot/modeld_v2/tests/test_chestnut_load.py sunnypilot/modeld_v2/tests/test_chestnut_fallback.py
```

Expected: if the selected release still lacks fallback, the fallback tests fail and production `modeld_v2` remains disabled.

- [ ] **Step 3: Implement the smallest runner-compatible fallback only if required**

Load the selected Chestnut bundle and a runner-compatible QCOM small bundle before engagement; on terminal load/runtime/invalid-output failure, set `ChestnutActive` false, switch once to the small state, publish `modelV2.big=false`, and retain failure telemetry until offroad transition.

- [ ] **Step 4: Run focused tests and compile checks**

```bash
pytest -q sunnypilot/modeld_v2/tests
python -m compileall -q sunnypilot/modeld_v2
```

- [ ] **Step 5: Commit PR 5 or document the disable decision**

If all fallback tests pass:

```bash
git add sunnypilot/modeld_v2
git commit -m "feat: add modeld v2 chestnut fallback"
```

If they do not pass, do not weaken the tests; leave custom `modeld_v2` disabled in the release configuration and record that limitation in the release notes.

---

### Task 7: Add minimal BluePilot presentation, prebuilt delivery, and device gates

**Files:**
- Modify: `selfdrive/ui/ui_state.py`
- Modify: `selfdrive/ui/bp/onroad/hud_renderer_bp.py`
- Modify: `selfdrive/ui/bp/mici/onroad/hud_renderer_bp.py`
- Modify: `bluepilot/ui/widgets/sidebar.py`
- Modify: `.github/workflows/prebuilt.yaml`
- Modify: `.github/workflows/release.yaml`
- Create: `docs/chestnut/device-validation.md`
- Create: `docs/chestnut/install-and-rollback.md`

**Interfaces:**
- Consumes: canonical upstream Chestnut state and a successful comma-four prebuilt.
- Produces: one truthful BP status presentation, exact install/rollback instructions, and evidence required to promote the integration.

- [ ] **Step 1: Write UI state tests against the canonical state machine**

Cover disconnected, uncompiled, ready, loading, active, and failed states. The BP layer must consume upstream state and must not probe USB, firmware, GPU, or model files independently.

- [ ] **Step 2: Implement the minimal BP display wiring**

Reuse SunnyPilot/openpilot status semantics. Add BP styling only; do not create new Params or a second status state machine.

- [ ] **Step 3: Build the release prebuilt and record its immutable SHA**

Run the repository's selected comma-four prebuilt workflow from the exact integration commit. Record source SHA, artifact SHA, AGNOS, tinygrad, firmware, model ref/hash, and rollback target in `docs/chestnut/device-validation.md`.

- [ ] **Step 4: Execute the offroad installation ladder**

Install with Chestnut disconnected; verify small-model boot, Ford detection, update and rollback; then connect Chestnut while offroad and verify firmware, PCIe, telemetry, model download, loading, and status transitions.

- [ ] **Step 5: Execute stationary failure injection**

Force load timeout, AMD lock contention, runtime exception, non-finite output, telemetry loss, and physical Chestnut loss. Each terminal failure must select the small model without stale `modelV2.big=true` output.

- [ ] **Step 6: Execute the controlled same-route A/B**

Drive the small model first, then the big model with the same car, route, tire setup, weather envelope, and frozen `1.25`/`1.29` angle factors. Review logs before expanding the test envelope; do not retune during this task.

- [ ] **Step 7: Verify non-Chestnut platforms and rollback**

Build/check C3X and MICI paths, uninstall or switch to the documented known-good BluePilot channel, and confirm the device returns to normal without repository repair.

- [ ] **Step 8: Commit PR 6 and request promotion only with complete evidence**

```bash
git add selfdrive/ui bluepilot/ui .github/workflows docs/chestnut
git commit -m "feat: publish bluepilot chestnut integration channel"
```

Do not target `bp-7.0` until every promotion criterion in the spec is checked and the soak period is complete.
