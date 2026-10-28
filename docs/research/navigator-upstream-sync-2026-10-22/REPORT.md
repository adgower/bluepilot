<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest master / AGNOS 20 sync — October 22, 2026

**Merged, checked and published. No device activation or OS update.**

- Navigator parent: `26b3416a6b258890b6c065ace24e3411609556d4`
- Official master included: `34d4241e19c983b048a806a17f3234ddd35de445`
- Preserved child: `fe59e503388a7c6593a7cd3117ac977d8894f0c5`
- Branch: `codex/navigator-tracking-release` in both adgower repositories; remote heads verified.

## Changes

Six upstream commits add AGNOS 20 and improve touch/scroll handling. The merge was automatic. The custom Expedition fingerprint remains. All 507 tracked child file hashes and eight protected parent source hashes match the prior pair: owner 1.20/0.97, geometry, all steering corrections, native limits, settings registry and calibration/motion transport are preserved. No new opendbc commit was necessary.

AGNOS 20 moves modem management into the OS, removes the repository modem process, and changes the required boot/system images. The official PR reports a smaller image, faster boot, removal of GCC and other packages, and clang/LLVM 20. These are upstream results, not measurements on this device. [Official release notes](https://github.com/commaai/openpilot/pull/39128).

## Verification

- Configured incremental minimal/full Mac and Panda builds passed.
- Full parent suite: 1,021 passed, 84 skipped, one expected failure, 281 subtests passed.
- Full child suite: 4,353 passed, 1,690 skipped, 24,673 subtests passed. Existing unsanitized Mac debug safety library; no fresh UBSan claim.
- Source/version/manifest contract: two expected failures before merge, all three checks pass afterward and after commit.
- Scoped Ruff, whitespace checks, exact merge parents, paired clean state and remote heads verified. Independent review found no material merge issue.
- Full child replay is carried through unchanged source, not freshly rerun for UI/OS metadata changes. No AGNOS 20 ARM or runtime proof yet.

## Device status and installation boundary

The last verified device remains `db5842348 / 8ccc6cf0` on AGNOS 19.9. No manager restart, source activation, OS flash or firmware update occurred. The new steering candidate `21325dccb / fe59e503` was staged before the user requested latest master. Its full ARM build and 840 native tests passed on 19.9; the scheduler harness then failed because it expected the already-fixed old scheduler to retain its historical bug. The correction was reproduced and tested locally; 25 helper tests pass. The runtime followup was not uploaded or started. That old stage remains held and its activation gate is closed.

A fresh private backup was verified on device and Mac: 843,598,547 bytes, 145 manifest entries, 67 parameters. Backup paths and checksums remain in the installation evidence directory, not published payloads.

A passive boot-slot/partition inventory attempt timed out over SSH; no partition commands executed. Reconnect the Comma to home Wi-Fi before preparing the AGNOS 20 installation. The existing installer’s requirement to preserve the AGNOS 19.9 launcher must be replaced by an exact matching AGNOS 20 source/launcher/manifest contract and reviewed A/B recovery sequence. Do not bypass that check or activate the old stage.

[Final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [publication](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [OS transition assessment](AGNOS20-TRANSITION.md).
