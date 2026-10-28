<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local deviation/unwind investigation

Scope: saved logs only; no SSH, ECU queries, CAN output, device changes or paired source edits. Preserve1.20/0.97 and native safety. Reproduce measured28mph shortfall and67mph excess with reproduce.py. Physical response cannot be made to change in a frozen-log replay; distinguish symptom reproduction from testing a vehicle fix.

Ranked hypotheses: (1) calibrated/fixed-pinion disagreement causes28mph clipping; compare actual and perfect calibrated wheel target under unchanged native model. (2) highway admission/persistence/release delays correction; trace each gate before output reason overwrites. (3) slew, repeated speed weighting or quantization suppresses effective correction; trace floating and actual CANPacker quantized outputs. (4) physical steering/PSCM acceleration limit and lag contribute; compare measured body/wheel and demand on rising/steady/falling phases without inferring a hard actuator limit from a source comment.

Use untouched installed factory and original input packets/timestamps; require exact quantized wire agreement for individual mechanism claims. Capture numerical stages/CSV and separate command counterfactuals from physical predictions. Save report and roadmap findings; no implementation or full safety replay claimed under this investigation.
