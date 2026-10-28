<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator offline calibration-first tools

Local analysis only. No networking, vehicle interfaces, parameter writes or automatic calibration. The estimator consumes anonymous episodes of **transmitted path angle** (rad) and **calibrated body yaw** (rad/s); requested yaw is a diagnostic/reference signal, not the fitted actuator input.

Run the full pipeline on this retained corpus:

```sh
${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python ${USER_HOME}/Apps/bluepilot/docs/research/navigator-calibration-first-2026-10-16/run.py
```

`run.py` stops on any failed dependent stage and writes `run-journal.json`. The corpus adapter prefers the durable private backup in `corpus-backup.json`; original temporary paths are a fallback. Cached extraction is reused only when ordered raw hashes, extraction-code dependencies, route identity and payload digests agree. This folder's `input-manifest.json` contains only anonymous labels, sizes and hashes; private raw recordings/caches contain location and device data and must remain private.

Files:

- `estimator.py`: pure `Episode`, delayed first-order free-rollout fit, whole-route uncertainty and validation, historical route-held-out CV; no controller application API.
- `dataset.py`, `normalize.py`: past-only alignment by physical measurement timestamp, validity and contiguous episode selection; anonymous arrays.
- `routes.py`, `prepare_cache.py`, `cache_provenance.py`: fixed335segment corpus, verified extraction and immutable-source staging.
- `evaluate.py`: separate source-aware tracking metrics, newest-route validation and historical CV; recommendations remain null.
- `tracking_windows.py`: observed discrepancy windows; not a lane-departure diagnosis.
- `plot.py`: optional standalone figures; requires matplotlib. Existing figures are already rendered. Do not confuse sample-percentile bars with confidence intervals.
- `test_*.py`, `verify.py`: synthetic recovery, abstention, provenance, source-state and corpus assertions.

Dependencies are the existing numpy/scipy/zstandard/pytest environment; no environment changes were made. Body-motion timestamps describe physical observations and are not proof that an online controller received those observations at the same time. This implementation does not replace the separately validated native safety feedback model.

See [REPORT.md](REPORT.md) and [verification.json](../../navigator-reference/PRIVATE_ARTIFACTS.md) for findings and limitations. The current implementation deliberately does not propose a controller gain map where held-out evidence fails. Adding new drives requires an explicit manifest/adapter update, not an unnoticed change to this fixed evaluation corpus.
