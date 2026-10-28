<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Bounded tracking correction local prototype

User-approved scope: offline implementation and full saved-CAN safety replay only. No Comma access or changes. Existing installed source remains untouched.

1. Write behavioral tests and observe their failure before implementation.
2. Add a report-local strategy subclass of the installed VeryLowSpeedGainPrototype. Preserve its existing feedforward, 1.20/0.97, human override, deviation clip, range, rate and shadow curvature. Duplicate the small update method for this isolated experiment instead of altering the installed branch; future production integration should extract a shared pre-limit hook.
3. Experimental P gain 0.5, error filter time constant 0.30 seconds, extra path-angle cap 0.015 radians and 25% of existing feedforward magnitude. Full speed weight 5–15 mph, smooth fade 15–25 mph, disabled below 5 mph. Reset on any driver press, inactive/human override, unsupported platform/flags, nonfinite inputs and outside speed eligibility. No integrator, no safety limit changes. These are conservative sensitivity settings, not identified vehicle calibration.
4. Confirm default-off baseline equivalence, signed tracking response, caps/filter/reset/fade, unchanged owner factors and inherited bounds. Run Ford/native safety regression tests.
5. Replay all 72 complete locally cached segments across five drives using independent unchanged native Ford safety instances; compare installed baseline and explicitly enabled prototype, retaining recorded permissions. Require no candidate rejects and recorded >=25 and >=45 mph byte parity. Inspect the two latest slow-turn windows. Record coverage and limitations.
6. Review linked upstream/fork pages in BrowserOS neo, deduplicate high-yield ideas into the roadmap with exact provenance. Browser currently blocked by no available browser window; do not invent current PR status.

Replay constrains generated command acceptance, not closed-loop vehicle stability or improved handling. Saved actual steering does not react to hypothetical extra command. No deployment is authorized by this task.
