<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local integration review

Scope: one production module plus recorded regression fixtures and 11 regression/guard tests. Parent change is an exact opendbc pin and integration note.

- Keep ReleaseBarrier validation and the original observed-clear condition unchanged.
- BrakeReleaseProgress only decides fault waiting; no method returns propulsion permission.
- Progress requires received post-start samples, a substantial overall decline and continuing recent decline. Duplicate messages cannot manufacture progress; stale/gapped samples, reversal, plateau and low noise fail the extension.
- Timeout threshold remains bounded at two seconds; a stalled release faults at the original one-second threshold. Existing observed-clear qualification precedes timeout evaluation as before.
- Resetting or changing the release start clears the progress history. Existing owner override and RestartClearance behavior remain intact.
- No gains, lateral mapping, CAN payload construction, native safety source or device parameters changed.
- The prototype and integrated source differ only in whitespace and explicit zip(strict=False). Recomputed controller output and wire bytes match exactly across all three saved replay routes. Prior native-hook results therefore apply to these identical wire streams; no claim of hardware/road proof.
- Separate pose fault and highway comfort work remain unresolved and are not hidden by this availability fix.
