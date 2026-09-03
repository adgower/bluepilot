# BluePilot Chestnut Sunny-Base Rebuild Design

## Goal

Build a new personal BluePilot branch whose first-parent platform is current SunnyPilot with Chestnut support, then layer the existing BluePilot integration and latest BluePilot Ford fixes on top. The original `codex/chestnut-personal` branch remains unchanged as the rollback baseline.

## Pinned Starting State

- Branch: `codex/chestnut-personal-2`
- Repository: `adgower/bluepilot`
- Initial first parent: SunnyPilot `master@e87dbbaba710bbfe7661d9ff064d46170cac9442`
- Existing BluePilot overlay source: `codex/chestnut-personal@1f4ec37186e6d9f7a3679790b1a75b026e008c26`
- Current BluePilot source: `bp-dev@501a7c0e911245044196fcc90cb077a69fa0749b`
- Sunny incorporated OpenPilot: `6249f4d5`
- OpenPilot comparison head: `master@06d76bdb24b9f5f3e69120782e8e3eb54a2f4f7e`

These pins are immutable inputs to this rebuild. A later upstream refresh is a separate reviewed merge.

## History and Integration Architecture

The branch starts directly from SunnyPilot so current Sunny platform, source-root layout, Chestnut runtime, model manager, AGNOS, firmware, and submodule versions form the primary history. Merge the existing personal branch with `--no-ff` as the second parent; Git then forward-ports the already-reviewed BluePilot overlay from its Sunny parent instead of recreating BluePilot by copying files. Merge current `bp-dev` afterward so its two post-baseline Ford commits are incorporated through normal ancestry.

The expected order is:

1. SunnyPilot `e87dbbab` as branch root.
2. Merge `1f4ec371` to apply and preserve the BluePilot overlay history.
3. Resolve the eight known overlap areas under the ownership rules below.
4. Merge BluePilot `501a7c0e` to add PR #195.
5. Add provenance documentation and only minimal integration fixes demonstrated by failing tests.

Do not squash, rebase, or synthesize a file-copy commit. Both upstream histories must remain inspectable.

## Ownership and Conflict Rules

SunnyPilot wins for the nested `openpilot/` platform tree, cereal and Params foundations, Chestnut detection/state, `modeld_v2`, model catalogs and downloads, AGNOS, firmware, workflows, UI foundations, and every non-opendbc submodule.

BluePilot wins for `bluepilot/`, the `openpilot/bluepilot` integration link, BP UI subclasses and wiring, portal/backend behavior, branding, build presentation, connection-backend selection, and Ford behavior. Preserve the flattened `opendbc_repo` because it contains BluePilot's Ford controller; do not replace it with Sunny's submodule.

Resolve the known overlaps as follows:

- Keep Sunny's current default-model workflow and model publication logic.
- Combine Sunny's current launcher with BluePilot backend selection and verbose-build fallback.
- Preserve current Sunny cereal schemas while retaining the exact `ControllerStateBP` and `CarStateBP` field names, ordinals, services, and publishers.
- Preserve all current Sunny parameter keys and migrations, then add the BP keys without renaming or changing defaults.
- Retain Sunny UI state and application changes while adding BP subscriptions, invalid-image protection, and BP UI scheduling behavior.
- Use Sunny's current `modeld_v2` compile test unless a BP-specific assertion is still semantically required.
- Keep the flattened BP opendbc tree, compare Sunny's old and new opendbc pins, and apply only the reviewed upstream delta. At the pinned target that delta is the non-functional MISRA test-harness suppression comment in `opendbc/safety/sunnypilot/mads.h`; any functional Ford or safety delta stops the merge for review.

Remove every temporary conflict-suffix path and ensure there is exactly one active OpenPilot source tree.

## Runtime and Safety Contract

Retain Sunny's canonical Chestnut contract: `ChestnutActive`, `ChestnutLoading`, `bigModelReady`, `chestnutState`, `modelV2.big`, and separate small/Chestnut model selections, downloads, caches, and hashes. Preserve small-model fallback after big-model load timeout, runtime exception, or non-finite output; after fallback, remain on the small model until restart.

BluePilot and Ford controls consume normal planner/model messages and must not implement GPU detection. No direct OpenPilot cherry-picks and no unmerged Sunny PRs are allowed.

Ford lateral, longitudinal, safety limits, ALP, radar behavior, fingerprinting, dampening, and vehicle tuning must remain behaviorally identical except for BluePilot PR #195's sustained cruise-button edge handling. Angle mode remains frozen at high `1.25` and low `1.29` for vehicle testing.

## Publication and Device Gate

The branch is development-only while Sunny's model publication is incomplete. The current Sunny workflow compiled and uploaded its temporary big-model artifact, but `upload_defaults` failed at `Upload model to HF`; therefore no comma-four installation is authorized from this branch yet.

Pushing the branch is allowed only after host verification succeeds. Advertising or using its installer URL additionally requires a coherent Sunny source/staging/model tuple: the staged commit must record the pinned-or-newer Sunny source, all source tests and Chestnut compilation jobs must pass, and public model upload plus integrity verification must succeed.

The existing installer for `codex/chestnut-personal@1f4ec371` and current BluePilot `bp-dev` remain rollback references. Nothing updates `bp-dev`, `bp-7.0`, or the original personal branch.

## Verification

Before pushing, require a clean tracked worktree; `git diff --check`; valid submodules and Git LFS objects; no duplicate source trees or conflict artifacts; cereal/service and Params migration tests; complete Sunny model-manager and `modeld_v2` fallback suites; process configuration, BluePilot UI/backend/portal smoke tests; Python import compilation; focused Ford controller, sustained-button, radar, ALP, fingerprinting, angle, dampening, and safety-differential tests; and the full host SCons build with the project environment on `PATH`.

Compare the final Ford/opendbc tree against `bp-dev@501a7c0e`. Every difference must be either a mechanical Sunny platform adaptation or the reviewed non-functional opendbc pin delta. Confirm explicitly that no tuning values or steering behavior changed.

Once the upstream artifact gate clears, emulate `AGNOSSetup` against the encoded installer URL, verify that the ARM64 installer selects `adgower/openpilot.git` and `codex/chestnut-personal-2`, then follow the existing stationary soak, fallback, rollback, and controlled-route procedure. Host checks never count as comma-four or vehicle validation.
