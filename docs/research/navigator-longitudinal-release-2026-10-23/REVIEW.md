<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent scoped review

Reviewer read release/helper/controller seam, focused tests, design and both replay harnesses/results. The valid-input correction addresses the reproduced0.2/0.3deadlock. Initial32tests passed, but reviewer foundP2: already creep-compensated self.accel was reused as raw fallback on invalid demand and compensated again, causing progressively stronger braking at low speed.

Reproduced in fallback-red.log. Fixed by retaining processed fallback without creep/rate reprocessing, neutralizing acceleration on disengagement. Added100update low-speed invalid-demand regression. Reviewer independently reran all33tests: passed; P2resolved; no additional concrete finding in follow-up.

No source/device/network edits or builds by reviewer. No physical release, grade-rollback, comfort, fuel or road-readiness certification.
