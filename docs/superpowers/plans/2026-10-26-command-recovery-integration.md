<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Command recovery paired integration implementation plan

> Use superpowers:executing-plans for inline execution; one final fresh-context review.

Goal: port accepted command-recovery prototype into existing local paired release branches without changing the Comma or1.20/0.97.
Architecture: opendbc owns stateful rolling-demand policy and installed integral freeze; openpilot owns native PID mechanics, reset, validity/urgent signals. Replace earlier uninstalled broad low-speed I guard with selected narrow command reduction and local-constraint anti-windup. No schema/safety/lateral/controller-consumer changes.
Tech: Python, pytest, Ruff, SCons, existing Mac native debug safety hooks.

- [x] Record clean parent2ca969e45 /childbcd706d0 and protected file hashes. Reuse existing dedicated paired checkout; preserve dirty root.
- [x] RED public child policy/native parent wrapper tests, including rollback and localconstraint signed recovery.
- [x] Extract RollingRestartControl into child; restore installed pre-broad freeze. Wire parent LongControl and controlsd explicit source_valid/urgent inputs. Keep default call compatibility and disabled behavior.
- [x] GREEN targeted tests, Ruff, diffcheck. Full197-segment integrated replay must exactly match accepted producer and wire streams; private raw hashes retained. No reinterpretation of physical comfort.
- [x] Full minimal/full Mac builds, parent suite, child suite and Panda build. Fresh or hash-bound unchanged native command-stream/safety proof, explicitly label reuse if used.
- [x] Fresh whole-pair review; fix findings, rerun affected checks. Retain highway pulsing unchanged,+4.349s brake exposure and two preexisting timeout caveats.
- [x] Commit child and parent locally with exact gitlink, verify clean pair andprotected hashes. Update roadmap/feature list/evidence. No push/device access.
