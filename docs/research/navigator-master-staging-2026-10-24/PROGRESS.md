<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Current handoff

Current source is still parent `2aa86b78d` / child `3a5fe9fe`. Candidate parent `74eaa6a60` / same child is separately staged, clean and inactive. Full ARM build, 1,094 native tests, 12,083 subtests, 75 contracts, 14 parent tests and calibration/startup checks passed. Initial three synthetic inferences at each camera resolution were finite. Backup is verified privately on the device and Mac.

## Current hardware evidence

Owner cold-cycled the setup. New boot ID: `<private identifier>`. The current installed model is healthy with ignition ON: 20.03 Hz, 39.32 ms mean, zero drops, PCIe `0x78`, supply 13.195 V. Park, zero speed, assistance disengaged, Alpha ON. Retained in `cold-active-passive.json`.

Owner clarified Chestnut requires ignition ON. Earlier ignition-off PCIe failures are not evidence of a new-model regression. Do not run the old offroad GPU helpers against the currently running modeld.

## Pending approval and procedure

`POWERED_BENCH_PLAN.md` and helpers are LOCAL ONLY, not uploaded or run. Explicit owner approval for a brief app interruption and ignition OFF is pending in the async question. After approval:

1. Upload reviewed powered-bench helpers. Run `pause_for_powered_bench.py STAGE --owner-approved-pause` only after fresh actual ignition-OFF/noOutput telemetry. It preserves source/settings and stops the app.
2. Ask owner to turn ignition ON and remain in Park. After that confirmation, run `authorize_powered_bench.py STAGE --owner-confirmed-powered-park`, then local `start_powered_bench.py`. Test two candidate starts with 35 synthetic inferences each. Fresh owner powered-Park confirmation replaces stale IsOffroad as physical-state evidence; app must remain stopped, vehicle devices are masked, and only Chestnut USB is exposed.
3. Ask owner to turn ignition OFF. Run `restore_after_powered_bench.py STAGE --owner-confirmed-ignition-off`; restore the SAME original app, then run passive offroad acceptance. Alpha stays ON throughout. No activation or firmware/OS update is authorized by the bench approval.

Review's process-title matcher defect was reproduced with four failing tests and fixed; 43 guard tests passed. Prior failure evidence and activation hold are retained. Do not clear the hold or claim staged readiness until the valid powered test passes. Preserve new attempt receipts and report the intentional service pause/restart separately from source preservation.


APP PAUSE EXECUTED after explicit owner 'Ignition off proceed'. Uploaded reviewed helpers and pause_for_powered_bench completed with fresh real ignition OFF/noOutput samples, source/settings/Alpha unchanged. Current app intentionally STOPPED; awaiting owner's ignition ON/Park reply to async question. Do not activate. Next: authorize_powered_bench with explicit owner powered-Park confirmation, start_powered_bench local wrapper, inspect unit/results; then owner OFF and restore original service. If owner cancels, confirm actual ignition OFF before restore. App remains unavailable until restored; avoid leaving that state unreported.


POWERED BENCH PASSED: owner approved pause, confirmed OFF -> pause verified; then owner ON/Park -> authorization recorded and isolated unit completed in87.70s. Two candidate starts,35syntheticinferences each,allfinite,noUSB/PCIefault. Warm median73.61ms each underCPU150% sequentialharness; no production20Hz claim. Current app STILL STOPPED; awaiting owner OFF confirmation in async question to restore SAME oldapp via restore_after_powered_bench.py. Newbranchnotactivated. Downloading evidence-powered-bench. After restore run passiveoffroadcheck and freshaudit allowing intentionalservicePIDchange; updatehold/report/roadmap to poweredgatespassed withproductionParkcheckseparate.


RESTORATION DONE after owner OFF. restore_after_powered_bench passed; 55s fresh offroad check passed (551 Panda samples, blocked counter0 stable). powered-bench-final-audit passed: active2aa86b78d/staged74eaa6a60/child3a5fe9fe, exact clean pairs, AlphaON/1.20/.97/selectedsettings preserved, all five calibration hashes equal prePause, firmware/OSslot unchanged. Original app active; service restart intentional approved. Awaiting owner response to 'normal home screen appears/responds' async question. After that confirmation clear/update activation-hold.json (preserve prior version), archive root NOT_READY_FOR_ACTIVATION.md, record powered preactivation pass with productionPark/20Hz/road still pending. Newbranch NOT activated. Update REPORT/roadmap status and final answer.


COMPLETE: owner confirmed restored home screen appears/responds. Powered startup gate passed2starts/70finite; old2aa app restored/active, new74 staged/inactive, child3a5, AlphaON/1.20/.97/settings/fivecalibrationhashes preserved. Clearing oldactivationhold with history preserved and recording superseding passed status. Next independent task is explicitowneractivation request + freshsnapshot/normalguards, followedbyactualnewstackpoweredPark/20Hzcheck. No apppause remains pending.


ACTIVATION IN PROGRESS: user explicitly requested staged latestmaster activation. Fresh64param device/Mac snapshot verified; currentlearnedstate retained. ReviewexactModelReceiptfinding fixed with6REDcounterexamples ->43GREENguardtests. Uploadedhelpershashverified. Atomicwholeinstall activation completed, parent74eaa/child3a5 active; old2aa retainedwhole at/data/openpilot.pre-master-refresh-<private timestamp identifier>. AlphaON1.20/.97/settings/calibrationpreserved. Offroad199samplesPASS/no newblockedTX. Owner confirmednewhomeUIresponds andignONPark; runningpowered-parked-check.py (55s). Logactivation-powered-parked-check.log. After result, downloadJSON+samples, inspectallassertions; ifinitialELMtransientpreservefirstcaptureandrerunsettledonly. Then final_activation_audit.py usingactivation-config dynamic, addfullLFSverificationifneeded, recordfreshcurrentmodel20Hz/drop/coordination/Pandaproof. UpdateACTIVATIONREPORT/roadmap+finalstatus. No roadproof.


COMPLETE: latestmaster74eaa/child3a5 active. Offroad199samplesPASS; ownerUIconfirmed/respondsandIGNonPark. Powered55sPASS:1101bigmodel,20.002Hz38.77ms0drops,550PandaFord11all0fault/rxinvalid/txblocked/controlsdisallowed.1101coordinationposevalid,nofault,producermax25.93ms. FinalauditPASS exactcleanactive/wholeoldrollback,all253LFS assets,signedFW/launchers,selectedsettingsAlphaON1.20/.97,AGNOS20.1B/serviceactive. Fresh64paramsdevice/privateMacbackupretained; oldwhole2aa install/data/openpilot.pre-master-refresh-<private timestamp identifier>. Runtimelearners4changedafterIGNon,nomanualresets. No OSFWupdate,ECUqueriesorengagementtests. Roadtracking/Alpha4releasetimeoutsremainunproven/unresolved. FinalreportACTIVATION_REPORT.md.
