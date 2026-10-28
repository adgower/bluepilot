<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest pre-install drive

28 retained segments,232,192,109 bytes, every download hash matched the device. Running old0cc74c94f/d64ffcfa. Corrected route start about2026-10-15 <private clock time>:38CDT, duration1624.74s, maximum65.26mph. Initial device wall clock incorrectly reports July28 before time synchronization; use elapsed monotonic times and the final stable clock offset. Absolute early-drive times are inferred, not trustworthy startup timestamps. Raw GPS/device identities remain in the private backup.

- Near elapsed1389.556–1391.257s (about17:11:48–49.43CDT), median14.91mph:1.75s clean meaningful-demand exposure, body curvature~49.2% of request and pinion proxy~70.8%. Driver steering begins near1391.627s (~16.8mph), but a driver-pressed flag alone cannot establish intervention cause. More continuous12.25mph shortfall at1420.355–1422.607s:body~39.9%, pinion~52.1%, lateral-acceleration error~0.099m/s² median.
- Across13–17mph there are5.0s of clean demand, median body46.4%/pinion70.9%. This is descriptive exposure, not a matched-road improvement estimate. Pinion/IMU disagreement means a recovery guard based on pinion can see adequate response before body curvature reaches the same fraction. Investigate model/offset/alignment and latency before adding gain; this installation only addresses the approved wait/catch-up exception.
- Clean40–50mph bends have~117% median body response to request over7.5s;50–70mph~113% over6.45s. Transients/demand mix matter; these aggregates do not establish consistent oversteer or justify a highway tuning change. This pair preserves high-speed outputs.
- Recorded alert text is limited to Reverse and lane-change prompts; no additional fault alert text appears in the extracted selfdrive stream (latest-alerts.json).
- No RX-invalid, persistent steering faults, Panda faults, heartbeat loss, Chestnut supply faults or reported model drops. Nine temporary steering-fault samples all occur stationary in Park (one startup, eight shutdown).
- Moving actual rejected-frame echoes:8 cancel-button0x83 messages across two disengagement edges (elapsed921.675/1524.164s); no active steering rejection. Startup/shutdown have separate inactive0x3d6/metadata/other echoes. Actual recorded-TX native replay reproduces4 cancel rejections (104,909 accepted/104,913 Ford-configured TX,6,433,241 RX with0 invalid). Transport timing accounts for the difference in reproduction; do not label all road TX accepted based on generated-command replay.
- Drive initData logged ExperimentalMode1 and AlphaLongitudinalEnabled0; this is not evidence of experimental longitudinal control running. The current fresh backup instead has ExperimentalMode absent/off and Alpha0; installation preserves that current snapshot. No longitudinal or clock/settings fix was applied.

See latest-analysis.json,actual-rejected-echoes.json,recorded-safety-replay.json and reconstruction.json for inspectable calculations. No new vehicle response to the candidate can be inferred from this pre-install recording.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Purple line marks the first driver-pressed flag in this view; candidate/installed extra terms are both zero in the13–17mph portion; earlier lower-speed pulses differ because the candidate spends its exception budget. The fixed pinion proxy and IMU response differ, so ratio alone is not a reason to increase gain.
