<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent installer review

Reviewed the master-sync helper sources against PLAN.md and the previous earlier-unwind installation helpers. Read-only review; no device contact, helper execution, source changes, or activation. Exact configured candidate: parent `db584234805cf2039ee976d856a29b655188ad2a`, previous parent `f7b0c47d23de697b73f1247cd5d32021b37e19bc`, unchanged child `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`.

## Finding

- **P2 — Require executed parent smoke tests.** `check_validation.py:13-14` rejects JUnit failures/errors and requires both test module names, but accepts skipped test cases. Consequently a zero-execution cruise/Mici suite can satisfy the fresh parent-runtime acceptance gate. Before acceptance, require non-skipped passing cases from both modules (and make unexpected skips explicit). This is a gate weakness, not evidence that any current run skipped these tests; no current device JUnit was reviewed.

## Reviewed behavior

The retired ExperimentalMode key is archived raw and excluded from candidate preference equality; candidate application code never accesses it through the new Params registry. AlphaLongitudinalEnabled remains preserved and explicitly required off. An absent InitialCruiseSpeedKph permits only absence or the new 40 default; an existing value must remain exact. Rollback restores the two migration keys as raw bytes after restoring the complete old source tree.

Both exchange and guarded-rename recovery paths preserve the old complete installation and handle failure before/after the stage symlink. Preparation removes alternate-object dependencies, checks connectivity, preserves installed firmware and launchers, and requires clean exact refs. Activation repeats cleanliness, source, offroad, preference, calibration and parameter-drift checks around stopping the manager. Unexpected parameter changes fail closed instead of being silently accepted. I found no additional missing runtime-key allowance established by the supplied helper evidence.

Isolation uses a separate writable stage, read-only active data/persist, private Params/cache/log/home, blocked vehicle device nodes, a fresh network namespace, dropped capabilities and no-new-privileges assertions. Fresh validation covers the ARM build, native suites, actual Car constructor and message pipeline, scheduler stalls and parent/default-key tests. Carried child matrices are explicitly identified as carried, bound to old parent/unchanged child and receipt hashes, and paired with 85 protected child source hashes. This does not establish road behavior.

The changed msgq bundle is fetched through its HEAD ref and checked out at the parent-pinned submodule commit. Powered acceptance uses the current target parent/child literals and preserves the initial-speed owner value/default contract. PLAN.md still says readiness confirmation is pending; the coordinator reports it is now confirmed, so that sentence is stale documentation rather than an activation gate.

No other concrete blocking installer issue was found in this scoped review. Fresh device validation, backup receipts and actual offroad/powered acceptance remain execution requirements; this review does not substitute for them.
