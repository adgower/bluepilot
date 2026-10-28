<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Bounded precharge device update — 2026-10-26

Owner authorized update/enable and confirmed ignition off, stable power/Wi-Fi and screen/recovery availability. Alpha remains ON. Fresh private source/settings archive was created and verified on the Mac. Candidate parent `5b301a944f40b6d3d4a490e2a2f30cbeab3a8d45` and child `884c9f49167a8baffdb643559b5d341815172836` were transferred by local Git bundles; no publication or OS/firmware update.

Full isolated ARM build passed. Native suite:1,131 passed,79 skipped,12,083 passing subtests. Retained tests:75passed. Parent smoke14passed; pose continuity, card startup, real local IPC and stall checks passed. Vehicle devices and network were inaccessible to the validation process; live source/settings/manager/service preservation checks passed.

The initial retained harness reported8failures because it compared the six appended metadata fields to old-peer defaults. A separate84-case diagnostic proved every legacy field and CAN command identical. Corrected comparisons assert truthful metadata separately and exact CAN equality. Production code unchanged. The native suite pass is retained with source/receipt hashes; corrected affected tests and startup gates were freshly rerun. A resume guard caught hydrated LFS index metadata; all253assets were reverified and index content kept identical. One resume invocation continued after that failed guard and was stopped; active app stayed unchanged. Failed attempt evidence retained where available, with the complete sequence in tool history.

Only weak-brake entry uses bounded precharge. Early coasting remains disabled; measured release clearance is unchanged. Existing1.20/0.97and steering preferences retained. The local137-segment replay shows1,879precharge-only callbacks/189entries with no added native rejects; physical comfort or highway pulsing improvement is unproved. The two existing reconstructed older-route release-timeout faults remain.

Candidate finalized/activation status follows the receipts. Powered stationary and road acceptance are separate.

## Activated; powered acceptance pending

Whole-install guarded swap succeeded. Exact paired commits active,201passive no-output samples, zero blocked TX observed, no unexpected stopped processes. Alpha1 and all selected settings/learned hashes preserved. Whole original install retained at rollback_tree in activation-config.json. Powered Park check requested; no moving-road proof yet.

## Powered stationary acceptance complete

Owner confirmed home screen responds and ignition ON in Park, assistance disengaged.55.0066s passive check passed:1,100fresh-target requests and1,101feedback samples use protocol1; all pose inputs valid, maximum observed request age20.79ms. Model20.0003Hz with0%frame drop;550Panda samples, Ford safety11, controlsAllowedfalse,0invalid RX and0blocked TX, no faults/heartbeat/SPI errors. Source pair clean and exact. Alpha/coordinationON; all prior steering settings,1.20/0.97, firmware, launchers, OS20.1and slot_b verified. No active precharge occurs in Park. Physical brake response, comfort and moving engagement still require road comparison. Final audit records normal learned-parameter runtime changes separately; no manual parameter writes.
