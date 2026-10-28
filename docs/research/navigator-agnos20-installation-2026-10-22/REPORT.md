<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Current execution status — AGNOS 20 installed; parked acceptance passed

AGNOS 20 / slot A is running paired source `26b3416a6b` / `fe59e50338`. Fresh full native build, 840 native tests / 79 skips / 12,063 subtests, Card/pipeline/scheduler checks and 14 parent tests / 6 skips passed. The validation-prefix correction is confined to the harness; 47 helper tests pass.

SSH reconnected after the owner confirmed the normal home screen and ignition on in Park. Display service is active with zero restarts this boot. A fresh six-second observation received 361 uiDebug samples with a 16.67 ms final frame time: the earlier render stall is not present in this check. The prepared Raylib post103 package remains uninstalled; its causal relevance is unproved.

**Powered parked acceptance passed:** 55 seconds, stationary in Park, assistance disengaged, all subscribed topics alive/valid, no vehicle or Panda faults, zero invalid RX / blocked TX, Chestnut supply healthy, big model 20 Hz and zero dropped frames. Both source trees clean and exact pair verified. Navigator geometry, all five options, initial cruise setting, updates paused and Alpha longitudinal off match the backup. Owner 1.20/0.97 is retained in the preserved source.

Learned parameter hashes matched before runtime restoration; all five monitored learned/cache files subsequently changed while runtime operated. This is not proof of bit-for-bit preservation after startup or of a reset. Current snapshots are retained alongside the original backup; no old learned files were forced over live values. IsOffroad changed as expected with ignition on. Calibration reports calibrated.

Original AGNOS 19.9 / slot B and whole previous source remain available for coordinated rollback. Reversible data-directory graphics startup configuration is required and documented in the execution ledger. Parked checks establish runtime operation, not road tracking or high-speed stability. Next evidence is an ordinary supervised drive and review of its logs.

See [execution ledger](EXECUTION.md). The preparation report below is historical.

---

# AGNOS 20 preparation complete — October 22, 2026

The latest paired source is staged and the final read-only device preflight passes. No OS partition writes, boot-slot changes, requested reboot, service stop, launcher replacement or source activation occurred during preparation. OS-write authorization is absent. Live runtime remains on AGNOS19.9/B with db584234/8ccc6cf; candidate26b3416a6/fe59e503 remains inactive.

## Verified

- Fresh private source/settings archive: 843,598,620 bytes, 145 manifest members, 67 parameters; archive and all members verified on the Mac.
- Pristine source checkout: 253 verified LFS assets, independent Git objects, clean exact pair, no inherited prior-OS host build artifacts. The interrupted checkout is retained separately.
- Current owner preferences, learned/calibration parameter hashes, launcher and signed Panda image match backup. The 1.20/0.97 implementation is preserved in the paired source.
- Full read-only device check rehashed all fourteen A/B images, validated current B as19.9, confirmed five unchanged A images match20, checked capacities and verified compressed/decompressed/raw image sizes and hashes through the pinned official decoder. Proposed writes are only inactive A boot/system.
- Forty-six local helper tests pass, including image corruption, URL restrictions, authorization/version guards, failure sequencing and no-bytecode regression. These are not hardware-write or AGNOS20 runtime tests.
- Independent preparation review findings resolved: no inherited native artifacts; explicit post-reboot stop of the hold-only oneshot service; internal Python bytecode suppression and per-command Git optional-lock suppression/safe-directory handling. Reviewed staged helper hashes match local files exactly.
- Current Panda submodule equals candidate a59195163c32a3a375ea6c86715dc08fd0984c1b; opendbc safety tree equals681a5a5cc1f5aa7c77f3f026ab65463fe2c35c52. Panda host transport/firmware expectation source checks show no change.
- Prior private Chestnut configuration archive reopened: one256-byte member matches saved verification hash. Copied alongside the fresh private backup with original name retained, without changing sealed archive. Current device configuration folder is absent; no hardware dump/query was attempted.
- Official Mac recovery wizard loaded and Comma four port instructions verified in BrowserOS neo. Actual USB detection/erase/recovery was not attempted.

## Restart and recovery limits

Owner confirmed the earlier restart was spontaneous. Previous-boot logs/pstore did not retain a cause. Current boot messages record a PMIC controlled-shutdown/reset indication without naming the initiating fault. The device subsequently stayed up for at least one hour, completed resource-limited pristine source preparation and full image verification. This does not prove the restart cause fixed. A repeated restart/power interruption is a stop condition requiring fresh state inspection.

The verified19.9 B images are retained for coordinated source-and-OS rollback. Actual fallback boot and physical factory recovery remain untested. Full fresh AGNOS20 native build, offline isolation probes/tests, offroad acceptance and powered stationary acceptance can only be established after the new OS boots; the maintenance hold remains through those gates.

## Execution decision

[Update and recovery procedure](UPDATE_AND_RECOVERY.md) describes the exact targets, hold across reboot, native gates and rollback. The next step requires explicit authorization to write inactive A boot/system, select A and reboot, plus fresh physical-access/stable-power confirmation. Preparing the files did not perform those actions.

Ruling: a full build generates a new-version Panda firmware artifact. Preserve that as evidence, restore the exact existing signed image after build/offline checks and seal validated host outputs using the standard prebuilt marker only after all checks pass. This preserves firmware; future source changes require deliberate rebuild/revalidation/resealing. It does not skip the required first fresh OS20 build. Application updates stay paused.

Evidence: `preparation-receipt.json`, `final-preflight.json`, `backup-verification.json`, `os-partition-audit.json`, `image-cache.json`, `staged-images.json`. The post-boot isolation harness is prepared/syntax-checked; AGNOS20 execution is still pending.
