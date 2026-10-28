<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator staged source — 2026-10-14

Staged on the Comma at `/data/navigator-master-staged-6ae31161b`, separate from the active `/data/openpilot`. The staged branch has not been launched or built. No service, launcher path, parameter, boot slot, OS or firmware was changed. No active ECU query was made.

## Verified source and assets

- Parent `6ae31161b73de2ce5043f708569759ac5f55f283`; paired child `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`.
- All six pinned submodules resolve correctly; parent and dependency working trees are clean.
- All **262 tracked LFS assets**, totaling **922,112,650 bytes**, are materialized and their SHA256/size checks pass. These include the actual models, fonts/images and updater binary; downloading a file does not execute it or update the OS.
- 1.20/0.97 constants are present in both the staged and active steering helper. Forced Expedition identity is present in the stage. No old `prebuilt` marker or Mac native artifacts were copied.
- Active source hashes, selected preferences, calibration and saved learned data still match the verified pre-migration backup. `/data/pythonpath` and the old staging symlink still point to `/data/openpilot`.
- AGNOS remains 19.7, slot A; actual Chestnut USB product remains `custom ed4e39b7-CLEAN`. The candidate's 19.9/8516b768 requirements have not been applied.

The detailed verification record is stored privately on the Comma at `/data/navigator-staging-records/6ae31161b-verification.json` and copied to `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-master-migration/stage-verification.json`. This is source/assets staging evidence, not a target-native build, activation or road evaluation.

## Recovery readiness

See [recovery options](RECOVERY_OPTIONS.md). Official factory web recovery supports a Mac using Chrome and physical USB/data plus power connections, and erases userdata. Chrome is installed on this Mac; device WebUSB detection and recovery have not been tested. A/B partitions exist, but rollback to the exact old combination is untested.

`/data/chestnut_config` is absent. The candidate's normal flash saves a verified 256-byte config before erase/program, but an independent pre-flash copy is not yet available. Creating it through the firmware access path may change USB driver/power/register state, so no such routine was run under the current no-update staging scope. Do not describe Chestnut ROM recovery as established.

Existing source-provided Chestnut image/flasher, Panda H7 signed image/bootstub and old AGNOS manifest were separately copied to the private Mac backup's `recovery-material/` directory and their hashes checked. These are stored files, not raw firmware dumps or proof of the currently flashed Panda signature. No firmware utility was executed.

## Next boundary

Keep this directory inert. Before activation, establish physical recovery access and the Chestnut configuration preservation step, confirm backups/capacity/parked power and network, and deliberately authorize the OS/firmware migration. Do not run AGNOS `--verify` as a read-only check: successful verification can switch the boot slot. Do not launch the staged manager/hardwared/pandad to test it: those can initiate compatibility updates. The application update pause does not suppress them.
