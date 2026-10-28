<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
> Final design supersedes the initial low-actuation proposal below: independent 70–80 mph output overlay over untouched installed state; low observation diagnostic only. See [final validation](../navigator-observer-continuity-validation-2026-10-22/REPORT.md).

# Throwaway observer continuity prototype

Approved scope: local prototype for70–79mph excess turning and23–24mph saturation. No device access, publishing or paired-source edits. Owner1.20/0.97 and native/application limits remain unchanged.

The highway observer collects five distinct, fresh, source-ordered original-target wheel observations while body excess may be below admission margin. Current independent sustained body confirmation, wheel excess beyond the existing0.5degree deadband, predictive closing release, calibration/context/driver guards and the existing15percent/0.01rad caps remain mandatory. Fresh history can credit onset persistence; it does not authorize retaining trim on failed current evidence. Additional admission fades in70–71mph and out79–80mph. The actual selected older `unchanged.stock.upper_reference` is included above75mph.

The low-speed observer checks original intent against the original atomic target even when the feasible command is clipped. It records `headroom_limited` rather than interpreting the changed command as a broken calibration packet. Additional early admission uses fresh independently observed history, requires current wheel/body deficit and predictive catch-up checks, and only acts while intent equals the feasible command. Existing shared0.00025rad*s ramp budget,0.0015rad/5percent cap and250ms episode window remain. Extra admission fades in22–23mph and out24–25mph. It cannot restore authority in fully clipped windows. No spent allowance is replenished by an ordinary observer reset.

Existing release and final rate/range bounds are retained. There is no new persistent error integral or hold through stale/invalid evidence. Protected static speed/default-off tests compare the entire result with the current installed policy. Synthetic transition and abort tests examine residual behavior; recorded replay separately checks native command acceptance.

Acceptance is command-space evidence only. Frozen recorded motion cannot predict physical tracking improvement, oscillation damping or85mph stability. Native replay uses actual RX-derived permission; it must not force controls allowed. This is not installation-ready code or a completed broad-corpus release validation.
