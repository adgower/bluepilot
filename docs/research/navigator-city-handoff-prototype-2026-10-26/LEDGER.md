<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# City handoff prototype — local research only

- Owner requested a local prototype plus continued highway investigation. No paired/runtime/device edits, model training, push or activation. Preserve1.20/0.97 and current narrow low-speed guard.
- Installed recordings use5b301a944/884c9f491; local pair2ca969e45/bcd706d0 includes low-speed antiwindup. Reproduce recorded baseline using the exact old integral function before comparing a prototype to the current local pair.
- Scope includes all14newcitysegments plus162retainedregressionsegments; highway smoothing remains active, not replaced by city work. ExistingOEMcoast evidence is observational with unresolvedRPMquality; no new brake-withholding permission is inferred from it.
- CodeGraph unavailable; exact known source files reused. Existing isolated paired checkout read-only, research artifacts in this new directory and private caches.

- Installed baseline diagnosis:73279producerupdates raw/Iwithin1e-5,17citybrakechangesreproduced,36gas/reasondifferencesafteronecallbackearlyclear. State-publication CANbound doesnotremove mismatch. Hidden receive cutoff notlogged; no timestampfit/seededpressure.
- Hypothesis: target-negative positive-demand antiwindup during fresh release/engineRamp. No newbrake/coast permission, actualbrake/precharge andsignednegativeerrorpreserved. Explicit owner-requested researchspike, notproductiondesignorinstall. RED5failed/35passed, GREEN40passed.
- Primarycomparison uses currentlocal pair with low-speedguard versus candidate, same CANvisibility. Standaloneinstalled-sourceablation separates earlier low-speedguard fromnewpolicy. Existing low-speedguard isretained unchanged.
- Full176segments/512066callbacks:1193->1196switches;441weakerencodedstrong-targetvalues,max0.0312,allwithbrakebit. Rejected; no native/ARM/buildpromotion. Highway20->20. Installedcity17->17withbrake21.538->22.671s.
- Inputaudit rehashed176uniquerawsegments andextractedcaches. Fiveactivemissingatomicupdatesonlyatretainedhighway01prefix; disclosefallback. All441regressionsinothercomplete-active-inputroutes.
- One-state-cycle CANavailabilitysensitivity retains sourcetimestamps;29segments/83201callbacks stillfail44encodedrequests;city7->7/highway22->22. Diagnostic,notassumedactualdelay.
- ReviewerP2 finding accepted: comparisonpreviouslyskippedmissingroutes. RED6failed/41passed, GREEN47; emptycorpusRED1failed/47passed, GREEN48. Manifests nowenforced; fullprimarycomparisonrerunandall10/2/3setschecked.
- Independentfinalreviewclean. No source/devicechange, no modeltraining. Previoushighwayresponse-awarecoastwork remains next engineeringaxis; another integral-onlyhold notsupported.
