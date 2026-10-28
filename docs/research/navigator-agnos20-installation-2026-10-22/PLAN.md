<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# AGNOS 20 installation preparation

Goal: prepare latest26b3416a6/fe59e503 and officialAGNOS20 images, preserving1.20/.97/settings/calibration and matching OS/source rollback. Device currently19.9, slotB, offroad; no OS partition writes yet.

1. Fresh read-only partition/source/service/settings inventory; verify existing complete backup and refresh changed runtime state before writes.
2. Cache official20 boot/system images, verify compressed/decompressed and raw image hashes; retain19.9 recovery manifest/currentB. Compare every manifest entry to ensure no unrelated shared partition writes.
3. Stage exact source and matching launcher; carry existing steering/native evidence through source identity. New OS20 runtime remains unproved until boot/build/test.
4. Test a reboot-aware state machine with injectable operations: verify readiness/backups/images/inactive target, write onlyinactiveA, verifyimages, commitmatching source/launcher andbootselector,reboot as expected, reconnectOS20, fullARM/runtime/parked gates. Rollback stopsmanager, restoresoldsource andBslot, thenreboots; never startsold19.9launcher on20.
5. Independent review of exact installer and rollback, then final explicit OS-write decision with concrete targets. Noflash/swap/reboot untilthatstep. Afterauthorizedupdate, freshOS20build/native/runtime andoffroad/poweredParkchecks beforedriving.

Existing19.9source-onlyinstaller is not reused acrossreboot. Vehicle interfaces remain inaccessible during offlinevalidation; noECUqueries ormanualCAN. All ownerpreferences andfirmware preserved. Keep frozenpriorstage/evidence; do notdeleteunrelateddata.
