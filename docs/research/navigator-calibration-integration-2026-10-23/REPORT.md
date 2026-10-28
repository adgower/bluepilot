<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration repair paired integration — October 23, 2026

Local parent commit `fe08ede1af29a9c37b0c8b3550ce66cbd9392348` on `codex/navigator-tracking-release` retains exact opendbc gitlink `d2e8d0404143da0f2685c2ff4932b9b9f702951f`. Child source is unchanged; both paired source trees are clean.

Calibration-only updates now rebuild calibrated pose and validity atomically from retained motion, keeping its original timestamp. Freshness, sensor health, nonfinite input, reversed-time and latched-fault checks remain in force. Disabled behavior is unchanged. Regression cases include the real card transport and owner disable/rearm sequence.

The three committed source/test SHA256 values and four protected Ford source hashes match the prior validated repair exactly (`source-verification.json`). Owner steering 1.20/0.97, geometry and native safety are unchanged. The full 1,015-segment safety replay is retained by exact source provenance; it added zero rejections, with historical shared rejects documented in the [repair report](../navigator-calibration-update-fix-2026-10-23/REPORT.md). This commit adds integration documentation without changing the replayed implementation.

Fresh precommit focused tests: 26 passed. Ruff and whitespace checks pass. Full build and suite results are recorded in `build-results.json` and phase logs.

No push, device connection, installation, settings change, OS/firmware operation or CAN transmission was performed. Mac builds and offline replays do not establish ARM, powered parked or road readiness. The Comma still has the previous installation; keep Alpha off pending separately authorized staging and acceptance checks.

## Fresh integration checks

All five phases completed successfully: minimal Mac build, full Mac build, full parent suite, full opendbc suite, standalone Panda build. Parent: **1,029 passed, 87 skipped, 1 expected failure, 281 passing subtests**. Child: **4,485 passed, 1,690 skipped, 24,693 passing subtests**. The child uses the existing unsanitized Mac debug safety library; this is not a UBSan or ARM result. All MISRA mutation subchecks passed in this run. No separate type checker was available or claimed.

Final paired source trees remain clean after all checks. See `build-results.json`, `parent-tests.xml`, `child-tests.xml` and phase logs for commands and results.
