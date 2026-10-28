<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest master device staging — October 24, 2026

**Latest status:** the update has since been activated. See [activation report](ACTIVATION_REPORT.md); the staging narrative below is retained as historical evidence.

The latest-master candidate is backed up, separately staged and ARM-built. The valid **ignition-ON, exclusive-GPU test passed two starts and 70 finite synthetic inferences**. The original app has been restored and passed fresh offroad acceptance. Alpha remains ON; source, settings, calibration and **1.20/0.97** are preserved. **The new branch remains inactive.** The owner confirmed the restored home screen appears and responds.

## Exact source and recovery

- Active parent: `2aa86b78d323a068d53a40edcbca5e23968b8108`.
- Staged parent: `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` (includes upstream master `9fba666fd485983b5849dfc62550fa1fd37fe338`).
- Active/staged child: `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`.
- Stage: `/data/navigator-validation/<private timestamp identifier>-74eaa6a60`.
- Fresh backup: `/data/navigator-backups/<private timestamp identifier>-pre-master-refresh`; verified private Mac copy: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-master-refresh`.
- Backup verified: 70 parameters, 149 manifest members, 843,631,884 bytes; nested source archives read to EOF.
- Both staged repositories clean; Git object stores self-contained; 253 hydrated LFS assets verified. Exact installed signed firmware image and prebuilt behavior retained.

## Passed checks

- Full isolated ARM build.
- 1,094 ARM/native/Ford/context tests, 79 skips, 12,083 subtests.
- 75 retained contracts, 14 parent smoke tests, calibration engagement regression, actual Controls/Card pipeline and scheduler/default gates.
- Initial actual staged Chestnut ModelState initialization plus three synthetic inferences at each of 1344×760 and 1928×1208. Both returned finite outputs. This did not run the full camera/modeld production loop or establish 20 Hz cadence.
- Dedicated namespace checks: private parameters/cache/logs, active install read-only, network down, no privileges. Vehicle devices masked; model phase exposes only the identified Chestnut USB bridge.
- Independent helper review and 28 local validation-guard tests.
- Final passive current-stack offroad acceptance: 550 Panda samples, no faults or new blocked transmissions; historical blocked counter remained 7.
- Final inactive audit: active source, selected settings, binary calibration, firmware, live service, AGNOS 20.1 and slot `_b` unchanged. Only runtime UptimeOffroad and LastAthenaPingTime hashes changed. Alpha stayed ON throughout.

The initial unit completed all four phases in 1,803.4 seconds. Its `validation-acceptance.json` describes those initial passed gates; **the later activation hold supersedes any readiness inference from that receipt**.

## Supplemental timing check and current blocker

Initial short synthetic runs, under 150% CPU quota and ordinary scheduling, took approximately 56–62 ms (1344) and 75–79 ms (1928) after the first inference. These cannot establish production cadence. A matched longer comparison was added using identical ModelState/helper/parser source, five warmups and 30 measured runs, GC disabled as in modeld.

The first baseline attempt hit the active-tree read-only guard because tinygrad opens disk tensors with a write-capable handle. The guard was retained; three installed model files were copied and verified inside staging instead. That corrected baseline completed 35 finite inferences; measured median 76.68 ms and p95 81.09 ms. Its weights SHA256 is `d4c7a3fcfc95813826ca871a80bea18df833aacb2eb6f5333e25a01e65b1a422`.

The immediately following candidate initialization failed **before inference**, with `bulk IN short read: 0/8 bytes` while setting up GPU memory. One separate candidate-only diagnostic then failed with `PCIe link not up (LTSSM=0x00), custom firmware not ready`. Further model attempts stopped. Cached sysfs still shows the Chestnut bridge at 5000 Mb/s; no relevant host USB disconnect was recorded. This does not prove the GPU/PCIe side is powered or healthy. The candidate warm comparison is incomplete; no performance parity or regression conclusion is supported.

The cause of the link loss is not established: power/link state, repeated device initialization and driver behavior remain possibilities. No steering, Alpha, firmware or OS change was made to conceal or work around it. All before/after preservation audits passed, including both failed supplementary attempts.

## Properly powered retest and restoration

The owner approved the [powered bench procedure](POWERED_BENCH_PLAN.md). Fresh ignition-OFF/noOutput telemetry was verified before pausing the original app. The owner then confirmed ignition ON and stationary Park. The isolated GPU test required the live app to remain stopped, vehicle devices masked, network down and fresh owner powered-Park confirmation; it did not treat the frozen IsOffroad parameter as live ignition proof.

Both candidate starts passed with GC disabled as in modeld: 35 inferences per start, all finite, no USB/PCIe error. The unit completed in 87.70 seconds. Sequential warmed medians were 73.61 and 73.62 ms under a 150% CPU quota and ordinary scheduling. These are harness timings, not production modeld execution times or proof of 20 Hz cadence; do not compare them directly with the earlier current-stack 39.32 ms reading or claim a model-speed improvement.

After explicit owner ignition-OFF confirmation, the same original app was restored. Fresh 55-second offroad acceptance passed: 551 Panda samples, no new blocked transmissions or faults, counter stable at zero. Final audit confirmed clean exact source pairs, Alpha ON, selected settings unchanged, all five calibration hashes identical to the pre-pause snapshot, unchanged firmware/AGNOS/slot and the intentional approved service restart. Runtime parameter changes are listed in the audit.

The previous ignition-off PCIe fault does not establish a new-model regression. It occurred in a test setup that did not assure sustained GPU power. The valid powered test now supplies the missing startup evidence; no driver, firmware or calibration workaround was installed. Keep the old failure evidence as history. Owner home-screen recovery confirmation passed. The previous staging hold is cleared; activation itself is a separate request. Activation, actual production cadence and road behavior remain separate future gates.

Evidence: `evidence/` contains the original complete build/startup run. `evidence-after-perf/` includes preserved failed attempts, baseline model copies manifest, GPU/USB traces, activation-hold.json, all preservation receipts and inactive preparation receipt. `final-audit.json`, `parked-offroad.json` and private backup verification document retained owner state. No activation, live-service restart, OS/firmware update or active vehicle ECU/CAN query occurred.

## Power clarification and cold-cycle follow-up

The owner confirmed Chestnut needs ignition ON for power. USB bridge visibility alone was insufficient evidence of sustained GPU power during earlier tests.

After the cold cycle, the existing `2aa86b78d` installation was observed in Park at zero speed with assistance disengaged and Alpha ON: 160 big-model samples at 20.03 Hz, mean execution 39.32 ms, zero drops, PCIe LTSSM `0x78`, supply 13.195 V and no supply fault. This establishes current-stack recovery under power, not staged-model performance. No staged GPU test was started against the running modeld.

The powered bench plan and helpers are prepared locally. Review identified a process-title matcher defect; four failing tests reproduced it, the matcher was corrected, and all 43 guard tests passed. No app pause, service restart, source change or activation has occurred. The owner subsequently approved the brief interruption; the powered test and restoration are documented above.

## Latest evidence

`evidence-powered-bench/` retains the original successful powered run and per-start receipts. `powered-bench-final-audit.json` and current `parked-offroad.json` verify restoration. `before-powered-bench-parked-offroad.json` preserves the earlier offroad capture. App pause/restore logs and approval receipts document the intentional interruption; no source activation occurred.

## Completed staging outcome

Owner confirmed normal home-screen response after restoration. The prior hold is preserved as history and superseded by a passed powered preactivation status. Candidate `74eaa6a60` remains inactive; the original `2aa86b78d` installation is active. No further app interruption remains pending. Alpha ON, 1.20/0.97, all selected settings and all five pre-pause calibration hashes are preserved. No OS/firmware update or active vehicle ECU query occurred. A fresh activation request, pre-switch snapshot/guards, new-stack powered Park/cadence check and subsequent road evidence remain separate steps.
