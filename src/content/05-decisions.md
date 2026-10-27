# Decision points and justification
::src Conversation :: Jonah (10/26): "we just need to have a little bit more of a calculus"; a small number of people, "you are more informed, plus Tara," decide. This page is that calculus: each choice the drafts embody, what was chosen, why, and what would change it.
::src Drafting choice :: Status labels: **Recommended** means the drafts assume it and a reviewer can accept it as is; **Needs confirmation** means a named person has to say yes before it goes to a district; **Open** means the drafts carry both options.

Each item below is a decision the drafts on the other tabs already make. Where a choice is marked "Needs confirmation" or "Open," the drafts are written so the other answer can be dropped in without rewriting anything else.

## 1. Coach access to student-level data
::src Conversation :: 10/26: Jonah leaned to the "less intrusive approach" with the team lead screen-sharing; James wanted to ask for access and fall back; Luke: aspirationally ask, be ready with Plan B, citing the PXU–Teach For America fingerprinting fight. Jonah and James to confirm with Tara whether coaches need names.
::src James's collateral :: His Navigator one-pager already tells districts that CHSS coaches and staff see "aggregate data only."
::src AFUHSD precedent :: AFUHSD accepted a partner coach seeing student data (TFA, 2026) when the coach was the only partner viewer and acknowledged as a FERPA school official; the district's first instinct the year before was to strip names.

**Status: Open.** Drafted as Option B (aggregate only, team lead screen-shares) by default, with a one-sentence district opt-in to Option A (coach has student-level access for their schools, logged, background-checked, trained). Why: B matches the collateral already in circulation, keeps one protocol across the network, and costs little in coaching effectiveness since the team lead is in the room. A is defensible under FERPA and some districts will grant it. What would change it: Tara saying coaches cannot do the job without names, or Columbus and San Diego both saying A is fine.

## 2. Identifiable data at all
::src James's MOU draft :: The current Agreement for Services Section Six describes "de-identified individual student data."
::src Conversation :: 10/19: Tara noted that today's uploads are de-identified and a direct connection changes that; Luke: "it does change what I like as much," but with a strong agreement in place "there's more than there used to be" who say yes. Navigator cannot show a school team "who needs support" without names.

**Status: Recommended.** The feed is identifiable, because the product requires it for school teams. The draft contains the exposure by role (Section 5.4), use (5.5), and retention (5.6). What would change it: a district that will only send de-identified data, in which case the fallback is a ninth-grade-only, pseudonymous feed and a Navigator without names for that district.

## 3. Discipline records
::src James's collateral :: Lists discipline among "only the data needed."
::src Emily's architecture :: Discipline is an input category on the platform diagram.
::src Conversation :: Tara (10/19): behavior data is "typically" not received; Luke (10/26): discipline is "the most tightly held" element, and in Arizona social-emotional data sharing is restricted.

**Status: Recommended.** Optional, not required. Why: not needed for the on-track calculation, and the single element most likely to stall a privacy review. What would change it: Tara identifying a Navigator feature that depends on it.

## 4. Retention after termination
::src Conversation :: James (10/23): delete student-level data, keep "Agua Fria High School went from 60% to 72%." Luke: different things.
::src SDPC NDPA :: Article IV: disposition within sixty days of request; de-identified data exempt; use of de-identified data survives termination; no re-identification; transfer only with written no-re-identification terms and LEA consent.
::src Columbus City DSA :: Destroy or return within ninety days of termination.
::src James's MOU draft :: Current draft keeps identifiable data for three years after termination.

**Status: Recommended.** Identifiable data destroyed within sixty days of termination or directive, with backups expiring within ninety; de-identified and aggregate data retained for evaluation under NDPA-style limits. Why: sixty days satisfies NDPA v2, Columbus, and the stricter districts; the carve-out is the NDPA's own. The three-year clause in the current draft would be struck by every district on the list. What would change it: nothing on the district side; Emily confirms the deletion runbook can meet sixty days across Salesforce, Azure, and Power BI.

## 5. The NDPA, Exhibit E, and CHSS's own appendix
::src Lewis County :: A Missouri district has already asked its consortium to obtain the NDPA with CHSS.
::src af-dpa :: Exhibit E extends privacy terms within a state for three years from the provider's signature; registry rows are district-created; the originating district uploads the signed agreement and a standalone Exhibit E. The v1.2 "Provider" definition is a strained fit for a coaching nonprofit, so Section 5.1's school-official statement stands on its own.

**Status: Recommended.** CHSS commits to sign any state NDPA on request, signs Exhibit E with the first district in each state, and keeps Appendix A as the instrument for districts that do not use the NDPA. Why: the NDPA will arrive regardless; fighting it costs months, and Exhibit E turns the first signature in each state into a template for the rest. What would change it: Stand's counsel objecting to the NDPA's standard clauses, which cannot be redlined.

## 6. Contracting entity and the 501(c)(4)
::src James's MOU draft :: Names "Stand for Children Leadership Center Inc." as the Organization.
::src Conversation :: James (10/23): Stand is both a (c)(3) and a (c)(4); "there doesn't actually have to be something wrong for people to raise a stink."
::src af-dpa :: A nonprofit may sit outside COPPA's "operator" definition and outside state operator statutes, so "the contract is the only enforcement."

**Status: Needs confirmation (Demian or counsel).** Drafted with Stand for Children Leadership Center, Inc. as the party and an express clause barring any advocacy, lobbying, political, or fundraising use of student data by any affiliate, including any (c)(4). Why: answers the question before a board member asks it. What would change it: confirmation that the Leadership Center is the correct (c)(3) signatory, which the current MOU implies.

## 7. Screeners and parental consent
::src Emily's email :: The agreement must "explicitly cover the Belonging and Skills screeners we administer."
::src af-dpa :: Department of Education SPPO letter of Aug 26, 2026: behavioral health screeners that probe emotional or psychological states require written parental consent before administration; PPRA opt-out does not substitute. Arizona § 15-117 adds seven days' notice and fourteen categories.
::src PPRA :: 20 U.S.C. § 1232h.

**Status: Needs confirmation (Tara).** The District approves screener content and runs notice or consent; CHSS provides the full instrument for review and adds no questions without approval. Why: the belonging screener can reach PPRA's protected areas, and the obligation legally sits with the district. What would change it: Tara confirming the instruments avoid the protected categories, in which case notice alone may suffice.

## 8. Cyber liability at $2M
::src Columbus City DSA :: At least $1,000,000.
::src af-dpa :: District practice research: "$1M for directory-only, $2M+ for SIS, assessment, special education or health data"; Beaverton requires $2M per claim and aggregate with a two-year tail.
::src San Diego CCAP :: CGL $1M/$2M, E&O $1M, additional insured, certificate on request.

**Status: Needs confirmation (Demian).** Drafted at $2M per claim and aggregate with a two-year tail, plus CGL $1M/$2M and E&O $1M. Why: SIS-level data is the $2M tier in district practice, and $2M satisfies Columbus. What would change it: Stand's current policy limit; if it is $1M, the draft says $1M and the gap goes on Emily's list.

## 9. Delivery tiers and the direct SIS connection
::src Emily's architecture :: v1 ingests periodic files by SFTP or secure upload; no vendor API.
::src Conversation :: Luke's ranking (10/19): SIS vendor feed first, district SFTP second, Clever/ClassLink last. The 10/26 reframe: TA to help districts automate is part of the offer.

**Status: Recommended.** Three tiers: automated feed (target), scheduled upload (floor), vendor connection (where available). Why: matches what the platform ingests today and leaves the best privacy route on the menu. What would change it: Emily adding API ingestion, which would promote Tier 3.

## 10. Student identifiers and matching
::src James's collateral :: "Records are matched using a consistent unique student identifier."
::src Emily's architecture :: Identity matching lists district ID, state ID, and "probabilistic matching."
::src af-dpa :: Pseudonymous rows tracked over time remain student data; a hash of the student number is a code "based on personal information," which FERPA's research-code rule forbids.

**Status: Recommended.** Require the district or state ID in every feed; allow a district-generated stable pseudonym; treat both as Student Data; use probabilistic matching only to flag duplicates for human review. Why: deterministic matching is what privacy officers trust, and it keeps pseudonymous feeds inside the agreement. What would change it: nothing; this is the safe default.

## 11. Minimum dataset
::src Emily's email :: "What is the minimum practical dataset we should request initially versus additional data we might pursue later?"
::src AFUHSD precedent :: District data teams strike elements they cannot produce accurately (AFUHSD feeder DSA, 2025).

**Status: Recommended.** Required: ID, name, grade level and enrollment, course enrollments, marks and credits by term, GPA, attendance. Optional: summer school, demographics, discipline, assessments, date of birth. Why: the required set is exactly what the on-track calculation and the dashboards need; everything else is a district election. What would change it: Tara or Emily naming a Navigator feature that needs an optional element.

## 12. Breach notification at 72 hours
::src af-dpa :: Arizona NDPA v1.2 Article V.4 uses seventy-two hours from confirmation; the repo recommends keeping the broad trigger, saying who notifies families, and allocating costs.

**Status: Recommended.** Seventy-two hours from confirmation, broad trigger, district controls family notification, CHSS bears costs attributable to its breach. Why: it is the NDPA's own number. What would change it: a state exhibit with a shorter window, which would control.

## 13. Navigator pilot timing
::src Emily's email :: Navigator launches at the CHSS Leadership Summit in late November 2026; pilot schools begin in December.
::src James's MOU draft :: Current agreements with existing partners were written for de-identified uploads.

**Status: Open (Jonah and Emily).** The pilot runs before any new agreement exists. Either it runs on de-identified data under the existing agreements, or pilot districts sign the new Sections Five and Six first. The drafts do not decide this; it has to be decided before the Summit.

## 14. Research and publication
::src SDPC NDPA :: Article IV.5: prior written approval before publishing anything that names the LEA explicitly or indirectly.
::src San Diego CCAP :: "Any information published in any form will not have the potential to identify individual students."

**Status: Recommended.** De-identified findings may be published; no student identifiable; district not named without consent; district receives any report with its aggregate results fifteen business days ahead; cells under ten suppressed. Why: it is what the longitudinal evaluation needs and what districts already accept in the NDPA. What would change it: a district wanting approval rights over all publication, which the clause can accommodate per district.

## 15. Audit evidence
::src Columbus City DSA :: Annual third-party audit of security operations.
::src af-dpa :: NDPA v1.2 gives the LEA an audit right; the Utah evidence menu (self-assessment, questionnaire, SOC 2 or SOC 3 report, on-site by agreement) lets districts choose.

**Status: Needs confirmation (Emily).** CHSS commits to an annual independent assessment and penetration test, and offers districts a menu of evidence once a year. Why: it is the Columbus bar and the shape most CTOs accept. What would change it: timing; if the first SOC 2 cannot complete before the 2027–28 school year, the spec page says so with a date rather than claiming it.

## 16. Naming
::src Conversation :: Emily (10/26) proposed "A, B, C" implementation profiles; the coach-access variants are also "Option A / Option B."

**Status: Recommended.** Implementation profiles are "Tier 1, 2, 3"; coach access is "Option A / B." Why: two A/B schemes in one agreement will be confused in a board packet.
