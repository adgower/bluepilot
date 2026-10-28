<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# AGNOS 20 transition assessment

Official master `34d4241e1` requires AGNOS 20. The manifest changes only the boot and system images, both A/B. The raw system image shrinks from 4,718,592,000 to 2,147,483,648 bytes. Other manifest entries are identical. This establishes source layout, not the actual inactive-slot contents or boot status.

The upstream updater targets the inactive slot, marks it unbootable while writing, verifies its partitions and switches the active slot. **The CLI `agnos.py --verify` is not read-only:** success calls `swap` and changes the active slot. It must not be used for passive inventory. Starting the new source on 19.9 also enters its OS updater; `DisableUpdates` does not bypass this launcher requirement.

A future deployment must:

1. Read and record current/target boot slots, partition sizes, current OS and source. The latest inventory attempt timed out; this remains unverified.
2. Retain the verified private source/settings backup, matching old source/launchers, original OS slot and available Mac recovery cables. A source-only rollback cannot be assumed compatible after an OS change.
3. Stage the exact new source and official image hashes. Replace the old installer’s 19.9 launcher-preservation rule with an explicit new version/launcher/manifest contract; keep all steering/calibration/settings preservation checks.
4. Use an OS-transition-aware activation procedure that accounts for the expected reboot. The previous source-only installer’s manager-start wait and rollback behavior must not be reused unchanged across that reboot.
5. Validate the ARM build, native tests, Card/context, compiler dependencies, OS modem service and startup under AGNOS 20; then run offroad and powered stationary Park acceptance. Preserve stock ACC/Alpha off and 1.20/0.97. No manual CAN or ECU requests.

Upstream removed GCC and uses clang/LLVM 20, so availability of the old validation helper’s `cc` command must be checked. Its AGNOS 19.9 ARM result does not prove this new environment. The official checklist includes comma four and Chestnut model-replay evidence, but is not validation on this Navigator.

No OS partitions, boot-slot flags, firmware, installed source or settings were changed during this assessment. No factory reset is part of the described upstream A/B mechanism. Recovery success has not been physically tested here.

[Official AGNOS 20 PR](https://github.com/commaai/openpilot/pull/39128).
