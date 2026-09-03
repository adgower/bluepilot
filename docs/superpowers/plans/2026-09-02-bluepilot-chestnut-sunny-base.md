# BluePilot Chestnut Sunny-Base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a host-verified `codex/chestnut-personal-2` branch with current SunnyPilot Chestnut support as its first-parent platform and BluePilot's complete current behavior layered on top.

**Architecture:** The branch already starts from SunnyPilot `e87dbbab` and contains only the approved design commit. Merge the existing personal branch to forward-port the proven BluePilot overlay, retain Sunny's nested `openpilot/` layout, flatten only `opendbc_repo`, then merge current `bp-dev` for PR #195. Push the result as development-only; installation remains blocked until Sunny publishes the exact matching public model artifact.

**Tech Stack:** Git merge ancestry, Python 3.12/uv, pytest, SCons, Cap'n Proto cereal, Git LFS, Git submodules, comma four/AGNOS 19.7, SunnyPilot `modeld_v2` and model manager.

**Spec:** `docs/superpowers/specs/2026-09-02-bluepilot-chestnut-sunny-base-design.md`

## Global Constraints

- Work only in `/Users/alex/Apps/bluepilot-chestnut-personal-2` on `codex/chestnut-personal-2`; do not modify `feature-sac`, `bp-dev`, `bp-7.0`, or `codex/chestnut-personal`.
- Preserve the first-parent Sunny base `e87dbbaba710bbfe7661d9ff064d46170cac9442`, personal overlay parent `1f4ec37186e6d9f7a3679790b1a75b026e008c26`, and BluePilot parent `501a7c0e911245044196fcc90cb077a69fa0749b`.
- Sunny owns the nested OpenPilot platform, Chestnut runtime, models, AGNOS, firmware, workflows, UI foundations, and non-opendbc submodules.
- BluePilot owns `bluepilot/`, BP UI/portal/branding/build behavior, backend selection, and the flattened Ford-capable `opendbc_repo`.
- Preserve `ChestnutActive`, `ChestnutLoading`, `bigModelReady`, `chestnutState`, `modelV2.big`, separate small/Chestnut model slots, and big-to-small fallback.
- Do not add direct OpenPilot commits, unmerged Sunny PRs, a second GPU detector, or fork-owned LFS objects.
- Do not change Ford lateral, longitudinal, safety, ALP, radar, fingerprinting, dampening, or tuning behavior except PR #195's cruise-button edge handling.
- Hold vehicle angle tuning at high `1.25` and low `1.29`; no steering retune is part of this branch.
- Treat every test, build, or LFS failure as a publication blocker. Host verification is not comma-four or vehicle validation.

---

### Task 1: Preflight and Reproducible Inputs

**Files:**
- Read: `docs/superpowers/specs/2026-09-02-bluepilot-chestnut-sunny-base-design.md`
- Read: `.gitmodules`
- Read: `.lfsconfig`

**Interfaces:**
- Consumes: the three immutable Git commits in Global Constraints.
- Produces: a clean, fully identified worktree and `/tmp` evidence files used by later review gates.

- [ ] **Step 1: Verify branch isolation and exact starting commit**

Run:

```bash
test "$(git branch --show-current)" = "codex/chestnut-personal-2"
test "$(git rev-parse HEAD)" = "5a6cfb0d76acd0a29b7438a178f34e6abcbba336"
test -z "$(git status --porcelain)"
git rev-parse --git-dir --git-common-dir
git rev-parse --show-superproject-working-tree
```

Expected: every `test` exits zero; Git reports a linked worktree, not a submodule.

- [ ] **Step 2: Verify all pinned commits exist without advancing them**

Run:

```bash
git cat-file -e e87dbbaba710bbfe7661d9ff064d46170cac9442^{commit}
git cat-file -e 1f4ec37186e6d9f7a3679790b1a75b026e008c26^{commit}
git cat-file -e 501a7c0e911245044196fcc90cb077a69fa0749b^{commit}
git show -s --format='%H %s' e87dbbaba710bbfe7661d9ff064d46170cac9442 1f4ec37186e6d9f7a3679790b1a75b026e008c26 501a7c0e911245044196fcc90cb077a69fa0749b
```

Expected: the commits identify Sunny model-name sanitization, the original personal Sunny merge, and BluePilot PR #195 respectively.

- [ ] **Step 3: Capture the overlay merge simulation**

Run:

```bash
git merge-tree 51987a62d07c44cc9e14b4d85dcb445edecd17d3 e87dbbaba710bbfe7661d9ff064d46170cac9442 1f4ec37186e6d9f7a3679790b1a75b026e008c26 > /tmp/chestnut-personal-2-overlay.merge-tree
rg -o '^(changed in both|added in both|removed in local|removed in remote|CONFLICT)' /tmp/chestnut-personal-2-overlay.merge-tree | sort | uniq -c
```

Expected: seven `changed in both` entries and one `removed in remote` entry. Any additional overlap requires updating the plan before merging.

- [ ] **Step 4: Record the pinned source tuple**

Run:

```bash
git submodule status > /tmp/chestnut-personal-2-sunny-submodules.txt
shasum -a 256 openpilot/common/hardware/comma/agnos.json openpilot/system/hardware/chestnut/firmware_wrapped.bin > /tmp/chestnut-personal-2-platform-hashes.txt
sed -n '1,8p' openpilot/sunnypilot/models/model_name.py
tr -d '\n' < openpilot/sunnypilot/models/tests/model_hash
tr -d '\n' < openpilot/sunnypilot/models/tests/big_model_hash
```

Expected: AGNOS 19.7; Chestnut firmware version `ed4e39b7`; small model `CD210` ref `5b6436a90cf6902b8aaa71c2b6f3d7164d8ae391`; big model `BMRLNAP Model v4` ref `f877d7a0ccc3cce943c76e285214c020cd65c899`; small hash `c5be11d2fb1115be953c541f30c50f7c71a00bc4a0e128e19aa11b60689317fc`; big hash `2c814f08a2c51323b87839fbf8d2c2a9853a2b5536271b3d67f7b7a2de7f9374`.

### Task 2: Merge the Existing BluePilot Overlay

**Files:**
- Modify: `.github/workflows/build-default-models.yaml`
- Modify: `.gitmodules`
- Modify: `launch_env.sh`
- Modify: `openpilot/cereal/log.capnp`
- Modify: `openpilot/common/params_keys.h`
- Modify: `openpilot/selfdrive/ui/ui_state.py`
- Modify: `openpilot/sunnypilot/modeld_v2/tests/test_compile_modeld.py`
- Modify: `openpilot/system/ui/lib/application.py`
- Replace Git submodule with tracked tree: `opendbc_repo/`

**Interfaces:**
- Consumes: Sunny `e87dbbab` tree and BluePilot overlay merge `1f4ec371`.
- Produces: one ancestry-preserving merge whose tree uses Sunny's source layout and BluePilot's owned layers.

- [ ] **Step 1: Start the real overlay merge without committing**

Run:

```bash
git merge --no-commit --no-ff 1f4ec37186e6d9f7a3679790b1a75b026e008c26
git diff --name-only --diff-filter=U
```

Expected unresolved paths: the seven modified files listed above except `.gitmodules`, plus `opendbc_repo`. Stop if the set differs from the simulation.

- [ ] **Step 2: Resolve Sunny-owned workflow and compile-test files**

Run:

```bash
git checkout --ours .github/workflows/build-default-models.yaml
git checkout --ours openpilot/sunnypilot/modeld_v2/tests/test_compile_modeld.py
git add .github/workflows/build-default-models.yaml openpilot/sunnypilot/modeld_v2/tests/test_compile_modeld.py
```

Expected: current Sunny publication logic and compile assertions remain byte-for-byte equal to `e87dbbab`.

- [ ] **Step 3: Resolve the launcher additively**

Edit `launch_env.sh` with `apply_patch`. Keep Sunny's entire file, including `AGNOS_VERSION="19.7"`, then append the BluePilot `BPConnectBackend` compatibility and host-selection block from:

```bash
git show 1f4ec37186e6d9f7a3679790b1a75b026e008c26:launch_env.sh
```

The finished file must contain exactly one `AGNOS_VERSION` block and one `# BluePilot: connect backend` block. Run:

```bash
bash -n launch_env.sh
test "$(rg -c 'AGNOS_VERSION="19.7"' launch_env.sh)" = "1"
test "$(rg -c '# BluePilot: connect backend' launch_env.sh)" = "1"
git add launch_env.sh
```

Expected: shell syntax succeeds and AGNOS remains 19.7.

- [ ] **Step 4: Resolve cereal and Params interfaces additively**

Edit the three files with `apply_patch`, always starting from the Sunny side:

```bash
git checkout --ours openpilot/cereal/log.capnp openpilot/common/params_keys.h openpilot/selfdrive/ui/ui_state.py
git diff 51987a62d07c44cc9e14b4d85dcb445edecd17d3..1f4ec37186e6d9f7a3679790b1a75b026e008c26 -- openpilot/cereal/log.capnp openpilot/common/params_keys.h openpilot/selfdrive/ui/ui_state.py
```

Apply only the BluePilot additions shown by that diff:

```capnp
controllerStateBP @139 :Custom.ControllerStateBP;
carStateBP @140 :Custom.CarStateBP;
```

Retain all BP parameter definitions with their existing names, types, defaults, and persistence flags. Retain the `is_bluepilot` import and conditional `carStateBP` subscription in `UIState`. Do not renumber any cereal field or remove a Sunny key.

Run:

```bash
rg -n 'controllerStateBP @139|carStateBP @140' openpilot/cereal/log.capnp
rg -n 'ChestnutActive|ChestnutLoading|ModelManager_ActiveBundleChestnut' openpilot/common/params_keys.h
rg -n 'is_bluepilot|carStateBP' openpilot/selfdrive/ui/ui_state.py
git add openpilot/cereal/log.capnp openpilot/common/params_keys.h openpilot/selfdrive/ui/ui_state.py
```

Expected: each canonical Sunny Chestnut key and each BP interface is present exactly once.

- [ ] **Step 5: Resolve the UI application seam**

Run:

```bash
git checkout --ours openpilot/system/ui/lib/application.py
git diff 51987a62d07c44cc9e14b4d85dcb445edecd17d3..1f4ec37186e6d9f7a3679790b1a75b026e008c26 -- openpilot/system/ui/lib/application.py
```

Using `apply_patch`, add the BP invalid-image guard immediately after `rl.load_image(image_path)` while retaining all current Sunny application changes. The guard must unload a zero-sized image and replace it with a transparent `1x1` image before alpha processing. Add only other BP-marked application hunks shown by the diff; do not revert Sunny code.

Run:

```bash
rg -n 'Invalid image dimensions|gen_image_color\(1, 1' openpilot/system/ui/lib/application.py
git add openpilot/system/ui/lib/application.py
```

Expected: the invalid-image guard is present once and the file has no conflict markers.

- [ ] **Step 6: Replace Sunny's opendbc gitlink with BluePilot's flattened tree**

Run:

```bash
git rm -f opendbc_repo
git checkout 1f4ec37186e6d9f7a3679790b1a75b026e008c26 -- opendbc_repo
```

Edit `.gitmodules` with `apply_patch` to remove only the `[submodule "opendbc"]` block. Keep every other Sunny submodule and pin unchanged.

Apply this exact non-functional upstream delta to `opendbc_repo/opendbc/safety/sunnypilot/mads.h` immediately before `mads_set_alternative_experience`:

```c
// cppcheck-suppress misra-c2012-8.7; called from libsafety test harness
```

Run:

```bash
test -z "$(git ls-files -s opendbc_repo | awk '$1 == 160000 {print}')"
test -f opendbc_repo/opendbc/car/ford/carcontroller.py
test "$(rg -c 'misra-c2012-8.7; called from libsafety test harness' opendbc_repo/opendbc/safety/sunnypilot/mads.h)" = "1"
git add .gitmodules opendbc_repo
```

Expected: `opendbc_repo` is a normal tracked directory and the only Sunny `06743dfb..f95f996f` opendbc delta is present.

- [ ] **Step 7: Validate and commit the overlay merge**

Run:

```bash
test -z "$(git diff --name-only --diff-filter=U)"
git diff --cached --check
git ls-files | rg '(~HEAD|~[A-Za-z0-9_-]+$|\.orig$|\.rej$)' && exit 1 || true
test -L openpilot/bluepilot
git status --short
git commit -m "sync: layer BluePilot integration onto Sunny Chestnut base"
```

Expected: no unresolved or temporary paths; the merge commit has two parents, with the pre-merge Sunny/design commit first and `1f4ec371` second.

### Task 3: Merge Current BluePilot bp-dev

**Files:**
- Modify: `opendbc_repo/opendbc/sunnypilot/car/ford/carstate_ext.py`
- Create: `opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_carstate_ext.py`

**Interfaces:**
- Consumes: BluePilot PR #195 at `501a7c0e`.
- Produces: edge-based combo cruise-button handling without repeated sustained-hold events.

- [ ] **Step 1: Simulate and start the bp-dev merge**

Run:

```bash
git merge-tree 5f17cf389b1a48b09185a732564db11bd6477b58 HEAD 501a7c0e911245044196fcc90cb077a69fa0749b > /tmp/chestnut-personal-2-bpdev.merge-tree
git merge --no-commit --no-ff 501a7c0e911245044196fcc90cb077a69fa0749b
git diff --cached --name-only
```

Expected: only `carstate_ext.py` and `test_carstate_ext.py` change. Any other path blocks the merge for review.

- [ ] **Step 2: Prove the new Ford behavior before committing**

Run:

```bash
UV_PROJECT_ENVIRONMENT="$PWD/.venv" uv sync --frozen
PATH="$PWD/.venv/bin:$PATH" pytest -q opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_carstate_ext.py
git diff --cached --check
```

Expected: all sustained-button tests pass and no formatting errors appear.

- [ ] **Step 3: Commit the bp-dev merge**

Run:

```bash
git commit -m "sync: merge current BluePilot bp-dev into Sunny-based Chestnut branch"
git show -s --format='%H%n%P%n%s' HEAD
```

Expected: a two-parent merge commit with `501a7c0e` as the second parent.

### Task 4: Restore Submodules, LFS, and Chestnut Contracts

**Files:**
- Potentially modify: `.gitattributes` only if `git lfs fsck` identifies the raw Bootstrap font at its actual nested path.
- Potentially modify: integration code only after a named existing test fails.

**Interfaces:**
- Consumes: merged Sunny platform and BP overlay.
- Produces: reproducible dependencies and an intact Chestnut/model fallback contract.

- [ ] **Step 1: Initialize only declared submodules**

Run:

```bash
git submodule sync --recursive
git submodule update --init --recursive
git submodule status --recursive
```

Expected pins: `msgq e7396e76`, neural data `03cac2d3`, panda `74a0adce`, rednose `28d4a7f6`, teleoprtc `1aa8fc43`, and tinygrad `e837e367`. No opendbc submodule appears.

- [ ] **Step 2: Validate LFS classification and availability**

Run:

```bash
git lfs fsck
git lfs pull
git lfs fsck
```

Expected: all three commands succeed using `https://gitlab.com/sunnypilot/public/sunnypilot-new-lfs.git/info/lfs`.

If and only if the first `fsck` reports `openpilot/third_party/bootstrap/bootstrap-icons.ttf` as an unexpected Git object, add this exact rule to `.gitattributes` with `apply_patch`, rerun both checks, and commit `build: keep Bootstrap font outside LFS`:

```gitattributes
openpilot/third_party/bootstrap/bootstrap-icons.ttf -filter -diff -merge
```

Any other missing or malformed LFS object blocks the branch.

- [ ] **Step 3: Verify the canonical Chestnut state and model slots**

Run:

```bash
rg -n 'ChestnutActive|ChestnutLoading|bigModelReady|chestnutState|modelV2\.big|ModelManager_ActiveBundleChestnut|ModelManager_ModelsCache_Chestnut' openpilot
rg -n 'UsbGpu|USBGPU|usbgpu' openpilot bluepilot || true
```

Expected: every canonical name is present. Legacy GPU names may occur only in one-way migration compatibility; runtime production code must not publish a second detector or second active-state source.

- [ ] **Step 4: Run model-manager and fallback suites**

Run:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/sunnypilot/models/tests
PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/sunnypilot/modeld_v2/tests
```

Expected: both suites pass, including load-timeout, runtime-exception, non-finite-output, combined-PKL, recovery-power, catalog, slot-selection, download, hash, and tinygrad-reference coverage.

If a test fails because a BP seam was lost, preserve the failing test, make the smallest `apply_patch` integration fix, rerun the single failing test, rerun both suites, and commit `fix: preserve Sunny Chestnut runtime contract`. Do not weaken or skip a test.

### Task 5: Verify BluePilot and Ford Behavior

**Files:**
- Test: `bluepilot/backend/test_backend_import.py`
- Test: `bluepilot/backend/test_modules_only.py`
- Test: `bluepilot/test_web_routes.py`
- Test: `opendbc_repo/opendbc/sunnypilot/car/ford/tests/`
- Test: `opendbc_repo/opendbc/car/ford/tests/test_ford.py`
- Test: `opendbc_repo/opendbc/safety/tests/test_ford.py`

**Interfaces:**
- Consumes: resolved BP UI/backend/Params/cereal seams and flattened Ford tree.
- Produces: evidence that the platform update did not change Ford controls or tuning.

- [ ] **Step 1: Run cereal, Params, manager, and import checks**

Run:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/cereal/messaging/tests openpilot/common/tests/test_params.py openpilot/sunnypilot/system/tests/test_params_migration.py openpilot/system/manager/test/test_manager.py
PATH="$PWD/.venv/bin:$PATH" python -m compileall -q bluepilot openpilot/selfdrive/ui/bp openpilot/sunnypilot
```

Expected: zero failures and no import-compilation errors.

- [ ] **Step 2: Run BluePilot backend and portal smoke tests**

Run:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q bluepilot/backend/test_backend_import.py bluepilot/backend/test_modules_only.py bluepilot/test_web_routes.py
```

Expected: zero failures; any platform-specific skip must state its reason in pytest output.

- [ ] **Step 3: Run focused Ford behavior tests**

Run:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_carstate_ext.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_lateral_angle_ext.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_lane_center_trim.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_vin_fingerprint.py \
  opendbc_repo/opendbc/car/ford/tests/test_ford.py
```

Expected: zero failures across sustained-button, angle, lane positioning, VIN/fingerprint, and stock Ford tests.

- [ ] **Step 4: Run and compare the Ford safety matrix**

Run the same command in the original personal worktree and the new worktree, normalizing only elapsed-time text:

```bash
cd /Users/alex/Apps/bluepilot-chestnut-personal
PATH="$PWD/.venv/bin:$PATH" pytest -q --tb=no -rfE opendbc_repo/opendbc/safety/tests/test_ford.py 2>&1 | sed -E 's/ in [0-9.]+s//' > /tmp/chestnut-personal-ford-safety.txt
cd /Users/alex/Apps/bluepilot-chestnut-personal-2
PATH="$PWD/.venv/bin:$PATH" pytest -q --tb=no -rfE opendbc_repo/opendbc/safety/tests/test_ford.py 2>&1 | sed -E 's/ in [0-9.]+s//' > /tmp/chestnut-personal-2-ford-safety.txt
diff -u /tmp/chestnut-personal-ford-safety.txt /tmp/chestnut-personal-2-ford-safety.txt
```

Expected: identical test outcome matrix. Existing inherited failures are acceptable only when node IDs and failure text match exactly; no new or missing outcome is allowed.

- [ ] **Step 5: Prove the opendbc delta is allowlisted**

Run:

```bash
git diff --name-only 501a7c0e911245044196fcc90cb077a69fa0749b HEAD -- opendbc_repo
git diff 501a7c0e911245044196fcc90cb077a69fa0749b HEAD -- opendbc_repo/opendbc/safety/sunnypilot/mads.h
git diff 501a7c0e911245044196fcc90cb077a69fa0749b HEAD -- opendbc_repo/opendbc/sunnypilot/car/ford opendbc_repo/opendbc/car/ford opendbc_repo/opendbc/safety/ford.h
```

Expected: the only tree difference from current `bp-dev` is the single MISRA suppression comment in `mads.h`; the Ford-specific diff is empty. This proves high `1.25` and low `1.29` behavior was not changed in source.

If an integration test requires a code fix, first preserve its failing output, add or retain the narrow regression test, apply the minimal patch, rerun the focused and safety suites, and commit the fix separately with a descriptive `fix:` message.

### Task 6: Full Build and Provenance

**Files:**
- Modify: `docs/CHESTNUT_PERSONAL_INTEGRATION.md`

**Interfaces:**
- Consumes: the verified merge heads, hashes, submodule pins, and test evidence.
- Produces: a reproducible source/build tuple and a host-buildable branch.

- [ ] **Step 1: Run the full host build**

Run:

```bash
PATH="$PWD/.venv/bin:$PATH" scons -j4
```

Expected: SCons exits zero. Do not substitute a minimal build for this gate.

- [ ] **Step 2: Update provenance using exact observed values**

Edit `docs/CHESTNUT_PERSONAL_INTEGRATION.md` with `apply_patch` to record:

- branch and final local HEAD;
- Sunny `e87dbbab`, incorporated OpenPilot `6249f4d5`, AGNOS 19.7 manifest SHA-256 `ce7eeb20a915a16ec2f4363fdeace6e4cbb2918f3ee929cc7388e4a601657d74`, and firmware `ed4e39b7` / SHA-256 `9520fde0bf43d499c07abd0a09b74e94d8a7cc3d610f577b7a4e218ab8a378e9`;
- small and big model names, refs, and hashes from Task 1;
- all final submodule pins, with flattened opendbc source pin `f95f996f` recorded as provenance rather than a live submodule;
- BluePilot `501a7c0e` and original personal rollback `1f4ec371`;
- exact commands and pass/fail/skip counts from Tasks 4-6;
- the current failed Sunny model-publication run and explicit development-only/no-install status.

Remove the obsolete claim that the old root-level Bootstrap override applies to this nested Sunny layout.

- [ ] **Step 3: Commit provenance**

Run:

```bash
git diff --check
git add docs/CHESTNUT_PERSONAL_INTEGRATION.md
git commit -m "docs: record Sunny-based Chestnut integration provenance"
```

Expected: documentation commit contains no code or generated build artifacts.

### Task 7: Final Review and Development-Branch Publication

**Files:**
- Read all changes since `e87dbbab`.

**Interfaces:**
- Consumes: all passing host gates and provenance evidence.
- Produces: a remote development branch only; no installer recommendation.

- [ ] **Step 1: Run final repository integrity checks**

Run:

```bash
git diff --check e87dbbaba710bbfe7661d9ff064d46170cac9442..HEAD
test -z "$(git status --porcelain)"
git lfs fsck
git submodule status --recursive
test ! -e common
test ! -e cereal
test ! -e selfdrive
test -d openpilot/common
test -d openpilot/cereal
test -d openpilot/selfdrive
git ls-files | rg '(~HEAD|~[A-Za-z0-9_-]+$|\.orig$|\.rej$)' && exit 1 || true
git log --graph --oneline --decorate --max-count=30
```

Expected: clean worktree, valid LFS/submodules, one nested OpenPilot source tree, no conflict artifacts, and visible Sunny/personal/bp-dev merge ancestry.

- [ ] **Step 2: Review the complete first-parent and ownership deltas**

Run:

```bash
git diff --stat e87dbbaba710bbfe7661d9ff064d46170cac9442..HEAD
git diff --name-status e87dbbaba710bbfe7661d9ff064d46170cac9442..HEAD
git log --first-parent --oneline e87dbbaba710bbfe7661d9ff064d46170cac9442..HEAD
```

Expected: changes are limited to the BP overlay, current BP Ford fix, integration seams, provenance, and any separately tested integration fixes.

- [ ] **Step 3: Push only the development branch**

Run:

```bash
git push -u origin codex/chestnut-personal-2
test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/codex/chestnut-personal-2 | cut -f1)"
```

Expected: `origin/codex/chestnut-personal-2` equals local HEAD. Do not push any other branch or tag.

- [ ] **Step 4: Keep the installer gate closed**

Verify the latest Sunny `staging-chestnut` commit and default-model workflow through BrowserOS neo. The installer gate remains closed unless the staged commit records exactly the Sunny source incorporated by this branch and the corresponding tests, `build_big_model`, artifact creation, `upload_defaults`, public download, and hashes all succeed.

Expected at the current snapshot: gate closed because staging records `47db84eb` while this branch incorporates `e87dbbab`, and workflow run `33706185619` failed at `Upload model to HF`.

### Task 8: Deferred Comma-Four Acceptance After the Artifact Gate Opens

**Files:**
- Update verification evidence in `docs/CHESTNUT_PERSONAL_INTEGRATION.md` after each completed device gate.

**Interfaces:**
- Consumes: an exact successful Sunny source/build/model tuple and the published development branch.
- Produces: personal hardware evidence; it does not create an official BluePilot compatibility claim.

- [ ] **Step 1: Verify installer provenance before device use**

Emulate `AGNOSSetup` against `https://installer.comma.ai/adgower/codex%2Fchestnut-personal-2`. Confirm the ARM64 installer embeds `https://github.com/adgower/openpilot.git` and branch `codex/chestnut-personal-2`.

- [ ] **Step 2: Exercise rollback before attaching Chestnut**

Save the current `bp-dev` and original `codex/chestnut-personal` installer URLs, verify SSH/recovery, install v2 without Chestnut while parked on external power, verify Ford/UI/logging/updater/small-model operation, reinstall `bp-dev`, and verify it boots before reinstalling v2.

- [ ] **Step 3: Perform stationary Chestnut acceptance**

Power down, attach the official Chestnut/GPU/power kit, boot stationary, verify firmware, AGNOS, telemetry, model hash, `bigModelReady`, and `ChestnutActive`, then complete a 30-minute thermal/power/process soak. Exercise the supported fallback procedure while stationary; never hot-unplug Chestnut.

- [ ] **Step 4: Perform controlled route comparison**

Drive the same short route first with the small model and then with the big model, holding high `1.25`, low `1.29`, controller mode, vehicle, tires, and all other settings fixed. Roll back immediately for stale model output, unexplained steering behavior, repeated model restarts, thermal/power faults, or failed fallback.
