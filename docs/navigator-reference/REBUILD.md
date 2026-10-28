# Reconstructing the Navigator source baseline

Snapshot date: October 28, 2026. Read [rebuild-manifest.json](rebuild-manifest.json) first. This is a reproducible source reference, **not an automatic Comma installation, OS update or proof of a fully tuned vehicle**.

## Source pair

- Parent: [adgower/openpilot](https://github.com/adgower/openpilot), `e05e42f43d2907a4f02915a924cfd95a46197e79`.
- Child: [adgower/opendbc](https://github.com/adgower/opendbc), `5097b993965b2b65ea3fcca7e3769cfa9403d49c`, pinned at `opendbc_repo` by the parent.
- Both were reachable from `codex/navigator-tracking-release` when this reference was prepared. Branch names can move; the commit IDs define this snapshot.
- Public reference branch: `adgower/bluepilot`, `docs/navigator-reference`. Its inherited BluePilot code is not the installed Navigator parent.

## Local reconstruction

Choose a new empty local directory. The following commands fetch source only and are not run against a device:

```sh
git clone --no-checkout https://github.com/adgower/openpilot.git navigator-openpilot
git -C navigator-openpilot fetch origin codex/navigator-tracking-release
git -C navigator-openpilot checkout --detach e05e42f43d2907a4f02915a924cfd95a46197e79
git -C navigator-openpilot submodule sync --recursive
git -C navigator-openpilot submodule update --init --recursive
git -C navigator-openpilot rev-parse HEAD
git -C navigator-openpilot/opendbc_repo rev-parse HEAD
```

Use the exact submodule gitlinks, including Panda and model/runtime dependencies. Do not substitute each dependency's current master. Set up the pinned source's documented development environment; its Python requirement is >=3.12.3,<3.13 and its lockfile is part of the source snapshot. Git LFS/model assets and external dependencies must be retrieved through that source's supported setup; they are not embedded in this reference export or guaranteed available forever.

Validate source files with:

```sh
python3 scripts/navigator-reference/verify_reference.py --openpilot-root /path/to/navigator-openpilot
```

A new clone may need environment-specific build work. A source hash check does not establish ARM build success, matching firmware, model startup, runtime health or road performance.

## Settings and calibration

The manifest distinguishes owner source constants from observed nonsecret device settings. Preserve 1.20/0.97 in their original vehicle/scope; do not invent parameter keys for them. The forced Expedition fingerprint is a documented override, not first-party Navigator recognition. Historical mass values require the current mass-normalized schema, not blind restoration of obsolete fields.

Observed settings are a reference, **not an automatic restore list**. A fresh private full parameter backup and a deliberate migration plan are required before changing an existing device. Never copy Wi-Fi credentials, keys, identity or full parameter backups into GitHub.

## Before a future installation

Build and test the reconstructed pair using the exact inputs/revisions appropriate to the candidate. Establish the supported AGNOS/model/Chestnut/Panda requirements and recovery options; the source currently requires AGNOS 20.1. Stage separately, verify the ARM build/model startup and retain rollback material. Activate only through a separately authorized parked procedure and verify the actual installed pair/settings. No install, firmware-update, CAN/ECU-query or reboot script is included here.

Longitudinal pulsing and a high-RPM case remain open in this snapshot. Recent road evidence contains no new 70–85 mph coverage. The manifest therefore records `tuning_complete: false`; rebuilding this source reproduces a development baseline, not a certified final tune.
