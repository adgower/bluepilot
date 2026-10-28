<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator IPMA OEM comparison — 2026-10-14

## Result

Uncertain — no factory-equipped comparison IPMA has been independently established from an OEM source in this pass. `RJ6T-14H102-BAH` remains a historical manufacturer-software identifier saved in CarParams, not a verified hardware assembly or service part number. The cache is not a fresh diagnostic observation.

The existing passive report records this string in a saved `22 F1 88` response at diagnostic request address `0x706`. This establishes cache content only. It does not prove installed hardware equivalence, an internal processor, the parking sensor inventory, or Active Park Assist 2.0 support.

## Research access limits

- BrowserOS neo was selected in accordance with the browser skill.
- Automatic approval review rejected an exact-identifier Google search, citing disclosure of a vehicle-specific identifier to an untrusted external destination. That rejected search did not establish any source evidence; it was not retried or bypassed.
- A subsequent generic search for OEM Lincoln 2023 Navigator Active Park Assist documentation failed with `CDP error: No browser window available`.
- After the parent informed the user, generic web research continued against OEM sources. No exact software identifier was disclosed in the fallback searches. OEM equipment and operating documentation was retrieved, but no OEM mapping from this software ID to a factory APA-equipped hardware assembly was established.

## OEM findings

1. Ford's 2023 Navigator L livery equipment sheet for group 200A lists Active Park Assist 2.0 and front, side, and rear parking sensors. This establishes an OEM advertised factory feature set for that configuration, not equipment present on the owner's Reserve and not IPMA hardware applicability. [Ford Pro 2023 Navigator L equipment sheet](https://content.fordpro.com/content/dam/fordpro/us/en-us/pdf/showroom/specialty-vehicles/livery/2023_Lincoln_NavigatorL.pdf), PDF page 1.
2. The 2023 Navigator online owner manual describes activation through a parking aid button followed by the Active Park Assist touchscreen icon, and pausing/resuming through release/hold of the button. Thus the physical button has an operating role in the documented factory system. The manual itself cautions that online content may describe equipment absent from a particular vehicle. It does not establish that adding a button restores a deleted system. [Ford service content, Switching Active Park Assist On and Off](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G2095740&Uid=G2213974&buildtype=web&countryCode=USA&div=l&languageCode=en&moidRef=G2068573&userMarket=USA&vFilteringEnabled=False&variantid=9224).
3. A publicly indexed FordDirect factory window sticker for a different US-market 2023 Navigator 4x4 Reserve explicitly lists `ACTIVE PARK ASSIST 2.0 DELETE` and a $365 credit. A Canadian Navigator L Reserve example lists the same delete description and a $450 credit. This is OEM evidence that the feature was deleted on actual 2023 Reserve builds. Neither sticker identifies why the deletion occurred or which hardware was removed. Neither belongs to the owner's vehicle. [US-market public reference sticker](../navigator-reference/PRIVATE_ARTIFACTS.md), [Canadian public reference sticker](../navigator-reference/PRIVATE_ARTIFACTS.md). These links contain publicly indexed reference-vehicle identifiers, not the owner's VIN. Search-index text was available; direct PDF rendering failed, so sticker layout was not visually verified.

## What remains unresolved

No OEM reference retrieved connects `RJ6T-14H102-BAH` to a particular IPMA hardware assembly, factory-equipped 2023 Navigator, APA software capability, semiconductor population, or approved retrofit. No switch, sensor, harness, or replacement IPMA part number is established. Sensor quantities and lateral sensor positions require applicable OEM service/parts documentation; front/side/rear marketing terminology is insufficient to count individual sensors.

Do not apply Mach-E prep-kit claims, F-150/Expedition deletion codes, other model-year modules, or generic IPMA catalog matches to this Navigator without its own applicability evidence. No independently verified factory APA-equipped donor IPMA identification was found in this pass.

## Required OEM evidence

A useful comparison requires an OEM build record or window sticker confirming a reference vehicle actually has Active Park Assist 2.0, and OEM hardware/software identification tied to that same reference vehicle. A model-year owner manual alone would establish system operation, not equipment present in either vehicle.

The next read-only sources are the 2023 Navigator owner manual and order guide, OEM parts applicability filtered to Active Park Assist equipped vehicles, and Ford/Lincoln service information identifying the responsible modules and parking-space sensors. A build delete option must be verified against this vehicle's factory build record; a missing button alone is insufficient.

No vehicle connection, active ECU query, configuration change, or service interruption was performed for this research pass.
