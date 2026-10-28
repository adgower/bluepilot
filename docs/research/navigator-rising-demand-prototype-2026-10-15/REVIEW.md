<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Reviewed new local admission code, tests and full replay harness. Found average-window ramp-rate bound could admit a single abrupt request jump. Added a jump-after-active-correction regression (observed RED), bounded every positive adjacent increment by rate×actual interval, and reran tests/replay.

Re-review confirmed the new bound addresses that case and no additional blocking source defect was found. Reviewer inspected source but did not run final tests/replay. Residual synthetic turn-exit steering remains material despite staying below the global peak request. Earlier recorded-input command admission is not proof of improved steering response or reduced intervention.

Opening replay description corrected to six drives/89 segments. Safety rejection and synthetic residual limitations are reported explicitly.
