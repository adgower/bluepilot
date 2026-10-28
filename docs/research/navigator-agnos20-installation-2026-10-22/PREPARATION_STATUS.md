<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Preparation status — completed; OS execution pending

No OS partition write, boot-slot change, source activation or requested reboot has occurred. Installed source remains db584234 / 8ccc6cf on AGNOS 19.9, slot B.

Fresh private backup and cached official AGNOS 20 boot/system images were verified. All seven current slot-B images match the recovery manifest. The proposed inactive-slot update changes boot/system only.

Historical interruption (subsequently resolved by pristine replacement): The device restarted during inactive source preparation, with no completion receipt. Previous-boot journal and pstore supplied no cause. Owner confirmed no physical reboot or unplug. At the follow-up check, uptime exceeded 41 minutes. Current-boot logs report PMIC PS_HOLD / MSM-controlled shutdown and companion GP1 reset reasons, which do not identify the initiating cause. No retained previous-boot journal or pstore crash record exists. Current memory has about 2.8 GB available and /data has 8.9 GB free; these current readings cannot rule out a transient pre-reboot problem. No staging or flashing process remains running. Stable operation and recovery readiness must be established before OS writes.

Independent review found that the first staged checkout inherited ignored AGNOS 19.9 native artifacts. The local staging helper now omits that copy. This change does not sanitize the existing remote checkout. Preserve that partial checkout for inspection and create a pristine source stage without old native outputs before acceptance. A successful incremental build of the contaminated checkout would not prove an AGNOS 20 rebuild.

Remaining gates: resolve restart, finish pristine source preparation, review installation and rollback implementation, obtain explicit OS-write authorization, then validate a fresh native build and runtime on AGNOS 20. Owner 1.20/0.97 and settings remain preserved. Current state does not establish readiness to flash or road readiness.

## Follow-up preparation

The pristine replacement completed under CPU/memory limits without a reboot. Source-prepared and fresh-native-state receipts exist; parent/child trees are clean and self-contained. The inherited-native-artifact finding is resolved; the earlier interrupted tree remains preserved for inspection. Fresh owner preferences/calibration and launcher match backup. The live installation remains AGNOS19.9/B on db584234/8ccc6cf.

The prior private 256-byte Chestnut configuration archive was reopened and its member hash matched the saved three-read verification receipt. It is absent from the current device folder, so recovery must retain that private archive and original member name. No firmware query or flash occurred. The official live factory recovery wizard loads; physical WebUSB detection and recovery are untested.

Independent readiness review identified post-reboot oneshot-service state and bytecode/Git metadata risks. The runbook now verifies the hold and explicitly stops the hold-only service after reboot. The runner suppresses bytecode internally and Git optional locks per command, with per-command safe.directory for root inspection. A regression test failed before bytecode suppression and passes after it. The local suite has 46 passing tests. Post-boot isolation helpers are adapted for exact source/stage paths and syntax-checked; their actual AGNOS20 execution remains a post-boot gate.

Ruling: full host build regenerates a new-version Panda image. Preserve it as evidence, restore the unchanged current signed Panda image, and seal host outputs with the standard prebuilt marker only after the fresh OS20 build and offline checks pass. This preserves firmware but means later source edits require deliberate rebuild/revalidation before resealing; the application update pause remains enabled.

## Final gate

Final default-mode device preflight passed with zero exit status. All reviewed staged helper hashes match local files. No OS-write authorization exists; live service remains active and original OS/source/settings are preserved. See REPORT.md for current status; earlier incomplete-state notes above are historical.
