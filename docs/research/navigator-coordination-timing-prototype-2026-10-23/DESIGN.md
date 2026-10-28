<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Authorized local timing spike

Exact baseline parent fe08ede1a / child d2e8d040, clean paired checkout. Keep 1.20/0.97, native limits and all driver/epoch/rearm/fault ownership. No Comma access/push/commit/install.

Reproduce the recorded old pose81.521ms at request production +22.847ms to consume =104.368ms. A healthy newer motion publication preceded request creation by0.552ms, but the cached control snapshot did not include it. Logger chronology is not exact IPC receipt, so replay is causal availability evidence, not hardware scheduling proof.

Prototype: a coordination-only nonblocking motion+calibration subscriber drained at publication; per-topic newest publication selection across main/late caches prevents rollback; independent PoseCalibrator builds orientation/angular velocity/pose validity/timestamp together. Preserve real sensor timestamp and existing request time/sequence/ownership. Never reuse orientation with a new timestamp or blindly force validity. Future-to-request source timestamps invalid; unseen late inputs fall back to seen primary inputs; genuinely unseen or invalid selected calibration/motion remain invalid. Primary invalidity and reference withdrawal cannot be cleared. Default-off creates no added subscriber and follows original path exactly. Lateral targets, calibration snapshots, HUD, brake/stop/lead decisions and child safety source unchanged.

Alternatives: main SubMaster late poll changes unrelated model/state inputs and lateral cadence; consumer pose replacement adds cross-frame/authority complexity; longer grace/timeout violates safety boundary. Selected late dedicated poll is an authorized exploratory spike, not an approved deployment.

Validate production publish/schema/real Card+controller path at exact timings; full stale/future/reversal/nonfinite/health/calibration/latch/rearm/disabled parity matrix. Replay new recordings with past-only topic availability (before original producer timestamp, conservative), no invented post-fault engagement. Run retained full longitudinal/native/model/response contracts, full1,015-segment lateral/native corpus, latest33segments and full parent/Ford build checks. Explicitly separate chronology from actual IPC/ARM/road proof.
