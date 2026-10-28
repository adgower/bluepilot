<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local candidate decision — October 26, 2026

The earlier spike plan required "no weaker encoded braking under strong consumed targets." The original narrow guard did not meet exact baseline identity:27encoded brake-acceleration requests differed by one 0.0039 m/s² increment, with no gas or brake-bit difference at those samples. This remains a measured comparative difference; it is not a demonstrated physical braking-distance effect.

After review of the concrete alternatives and native results, the owner selected: **"Keep narrow guard; document variation."** The question explicitly excluded installation authorization. This acceptance applies only to the original narrow local guard, its exact source hash/base pair and the described replay corpus. It is not a blanket waiver of braking checks, firmware limits, measured clearance or future larger differences.

Retain `ramp_experiment.py` (SHA-256 in SELECTED_CANDIDATE.json). Reject `history_policy.py` and every settle/once variant. Do not copy those variants into paired branches. The repeated 20/40 ms holds add one release-timeout episode in an older route; the one-shot holds avoid that fault but increase weaker encoded samples from 27 to 328/335.

The selected guard passes 41 focused tests, full 162-segment coupled controller replay with no added coordination faults/inactive/pressure-authority violations, and fresh162-segment native replay with zero added safety rejections. Two older reconstructed baseline coordination faults remain unchanged; original native rejections are retained. Plain debug hooks were used, not sanitizer or actual firmware execution.

The selected candidate does not fix the separate downhill cycle, does not force a gear and does not establish lower physical RPM or smoother acceleration. Paired integration/build, ARM validation, parked acceptance and moving evaluation remain separate. Current branches and Comma are unchanged.
