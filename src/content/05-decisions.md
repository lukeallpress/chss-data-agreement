# Decisions
::src Conversation :: Jonah (10/26): "we just need to have a little bit more of a calculus"; a small number of people decide. This page is the register: what is still open and who owns it, then the calls already made and why, so each can be defended or reversed on the record.
::src Drafting choice :: Source notes never refer to internal draft numbers; a change is described as a change from "an earlier draft." Version history lives in the header pill only.
::src Drafting choice :: Two lists. **Open decisions** come first: each names an owner, an approver, what evidence settles it, which documents it touches, and whether the package can go to a district before it is settled. **Decisions made** follow, with the reasoning and what would reverse them. Sources on each entry carry the legal basis and the district perspective that shaped it.

Nothing in the drafts goes to a district until every open decision marked **gate** is closed. The rest can travel with a bracket.

## Open decisions

| # | Decision | Owner | Approver | Needed by | Evidence that settles it | Documents | Gate |
|---|---|---|---|---|---|---|---|
| O1 | When data starts flowing, and what the December Navigator pilot runs on | Jonah, Emily | Stand counsel | Before the Leadership Summit (late Nov) | Written statement of the pilot's data source and the Year 1 start date | B §6.10, D-3; A | **Gate** |
| O2 | Liability cap, indemnity, and breach-cost carve-out | Jonah | Stand counsel | Before Columbus review | Counsel's redline of Agreement Section Eight | B conforming edits; C A.8, A.14 | **Gate** |
| O3 | AI model provider, tier, data-use terms, no-training attestation | Emily | Jonah | Before any CTO sees Part C | Provider name, contract excerpt or URL and date, zero-retention arrangement | C A.6, A.12, Part C | **Gate** |
| O4 | Which security controls are true today; dates for the rest | Emily | Jonah | Before any CTO sees Part C | Control-readiness list with evidence per line | C A.7, A.9, A.13, Part C | **Gate** |
| O5 | Background checks and annual privacy training for every person with access, coaches included | Demian, James | Jonah | Before Option A is offered anywhere | HR confirmation of current practice, or a dated plan | C A.7; B §5.4 | **Gate** for Option A |
| O6 | Screener consent classification and question-level review | Tara (program need), Stand counsel (consent) | Jonah | Before any screener runs in a new district | Instrument text; counsel's classification per protected category; district authorization form | B §6.7; C A.15, A.17 | **Gate** for screeners |
| O7 | Insurance limits actually held | Demian (finance), counsel | Jonah | Before draft goes out | Certificate of insurance | C A.14; B conforming edits | Bracket |
| O8 | Contracting entity: Stand for Children Leadership Center, Inc. as the 501(c)(3) signatory | Stand counsel | Jonah | Before draft goes out | Counsel confirmation | B §5.1; C Part A, A.4 | Bracket |
| O9 | Whether a Navigator tenant can run without student names (pseudonymous election) | Emily | Jonah, Tara | Before Columbus review | Platform answer: yes, no, or with which features disabled | B §6.4, D-3 | Bracket |
| O10 | Row-level de-identified retention is actually needed for evaluation, not aggregate only | Tara, Jonah | Stand counsel | Before Columbus review | Description of the longitudinal analyses planned | B §5.5–5.6; C A.10 | Bracket |
| O11 | Integration support through acceptance plus maintenance, and who staffs it | Jonah | Emily | Before draft goes out | Staffing and hours decision | B §6.9; A | Bracket |
| O12 | Standing commitment to sign any state NDPA and Exhibit E | Stand counsel | Jonah | Before the Missouri reply is sent | Counsel's yes | B §5.2; C Part A; D | **Gate** for the Missouri reply |
| O13 | Deletion runbook across Salesforce, Azure/Fabric, Power BI, backups, subprocessors, within 60 days | Emily | Jonah | Before draft goes out | Runbook and a tested dry run | B §5.6; C A.10 | Bracket |
| O14 | Subprocessor list and U.S. region for each tenant | Emily | Jonah | Before draft goes out | Tenant settings or contract excerpts | C A.6, A.9 | Bracket |

### O1. When data starts flowing
::src Conversation :: Jonah (10/26): starting with districts in January "gives us the four or five months of let's get this set up before students start." James (10/23): "when we come to them in April and say, hey, it's time to engineer this SIS integration." Winners announced Dec 15; technical onboarding January and February.
::src James's MOU draft :: Year 0 is readiness ("data access and reporting setup" is listed among Year 0 activities); Year 1 is implementation.
::src Emily's email :: Navigator "target launch at the CHSS Leadership Summit in late November 2026 and pilot schools beginning in December."
::src District lens :: A district counsel reads a December pilot next to a three-month board calendar and concludes the agreement is being asked to cover data already moving. Columbus City said board approval takes about three months.
::src Luke's decision :: Reframed the timeline so the January cohort commits to readiness in Year 0 and live data in August 2027; any spring test load happens only after the agreement is signed. The December pilot is existing partner schools on existing agreements and stays out of the new cohort's agreement entirely.

**Why it is first.** The new cohort is not sharing student data in December. It is committing to be ready by August 2027. If the drafts or the pitch imply otherwise, every district counsel will stop at the calendar. Exhibit D-3 now says: contacts named in January, agreement routed and signed in Year 0, test load after signature, live feed before Year 1 instruction. What has to be decided, before the Summit: the December pilot runs on which schools, under which agreement, with what data. The safe answer is existing partners, existing agreements, de-identified uploads as today.

### O2. Liability and indemnity
::src James's MOU draft :: Section Eight: services "as is"; no liability for indirect or consequential damages; "in no event will the liability of Organization and its affiliates ... exceed applicable liability insurance proceeds." Each party responsible for its own acts; "reasonable liability insurance."
::src af-dpa :: knowledge/practice/dpa-review-checklist.md: "the NDPA has no insurance clause ... No liability cap or indemnity"; district practice is to "carve out data breach, confidentiality and indemnity obligations, or set a breach super-cap."
::src San Diego CCAP :: Mutual indemnification with defined allocation for sole, concurrent, and joint-defense cases; CGL $1M/$2M, E&O $1M, additional insured.
::src District lens :: A board attorney reading Appendix A's breach-cost promise next to Section Eight's cap asks which one wins. Until the two are reconciled, the privacy promises read as capped at the insurance limit and excluding the consequential losses a breach actually causes.

**Recommendation.** Carve breach costs under A.8, confidentiality, and privacy indemnity out of the Section Eight cap, or give them a super-cap of not less than the cyber limit. Add a mutual indemnity for each party's own acts in the data provisions. This is Jonah's call because it is money, and counsel's because it is drafting.

### O3 and O4. AI provider and control readiness
::src Emily's architecture :: AI-assisted mapping, validation, "risk models and intervention recommendations"; Azure/Fabric, Salesforce, Power BI.
::src Luke's experience :: Arizona NDPA Exhibit G AI questionnaire: base model and provider, data shared with AI subprocessors, training on user data, human in the loop, query logging.
::src District lens :: A CTO reads Part C's present-tense controls and asks for evidence of each; a privacy officer will not accept a blank where the model provider's name belongs.

**Recommendation.** Emily returns the subprocessor table filled in, and a line-by-line "true today / true by date" against Part C. Part C is published in present tense only for lines marked true today.

### O5. Personnel claims
::src Conversation :: Luke and Jonah (10/26): Phoenix Union required fingerprinting and onboarding of virtual Teach For America mentors; naming a CHSS background check removes one reason for a district to impose its own.
::src District lens :: If the appendix says every person with access passes a background check and completes annual training, a district will ask for the policy and the roster. Claiming it before HR confirms it is worse than not claiming it.

**Recommendation.** Demian confirms current practice for coaches and technical staff. If not current, the clause becomes "by [date]" and Option A is withheld until then.

### O6. Screeners
::src State law :: Arizona A.R.S. § 15-104 requires prior written parental consent for mental health screening in schools, and § 15-117 exempts § 15-104 screenings from its separate survey regime. The U.S. Department of Education's August 26, 2026 letter treats behavioral health screeners that probe emotional or psychological states as requiring written consent, with PPRA opt-out not a substitute.
::src Emily's email :: The agreement must cover the Belonging and Skills screeners.
::src District lens :: A privacy officer will not approve "notice, opt-out, or consent" without the instruments in hand; Arizona counsel will ask whether the Belonging Screener is a mental health screening under § 15-104.

**Recommendation.** Tara supplies the instruments and the program purpose; Stand counsel classifies each against PPRA's protected areas and § 15-104; the agreement makes collection contingent on the district's written authorization and certification that any required consent is on file.

### O9. Pseudonymous election
::src Luke's experience :: AFUHSD's first ask of Teach For America (2025) was to strip names and keep the linking key; the district's own feeds use deterministic transformations or a mapping table.
::src District lens :: A "fallback without names" that the agreement does not actually contain is a promise a data manager will test and find missing.

**Recommendation.** Emily answers whether a tenant can operate without names and which Navigator features would be off. If yes, Exhibit D-3 gets a pseudonymous election and the agreement says what the district loses. If no, the fallback is removed from the pitch.

### O10. Row-level de-identified retention
::src Conversation :: Tara and Jonah (10/19): follow students "from ninth grade success to CTE enrollment, pathway completion, dual credit, graduation"; James (10/23): keep "went from 60% to 72%," delete student-level data.
::src FERPA :: 34 C.F.R. § 99.31(b)(1) (de-identified release after a reasonable determination that identity is not personally identifiable, accounting for other reasonably available information); Department of Education guidance warns that removing direct identifiers is not enough and that complementary suppression may be needed.
::src District lens :: A privacy officer asks whether cohort-level results need row-level records at all, and if so, what process makes the retained rows not personally identifiable.

**Recommendation.** Keep row-level de-identified retention, because the longitudinal cohort work needs it, and pair it with the reasonable-determination review now in A.10. Tara and Jonah confirm the analyses so the clause can describe them.

### O12. NDPA and Exhibit E
::src Lewis County :: A Missouri partner district has already asked its consortium to obtain the NDPA with CHSS.
::src af-dpa :: Exhibit E is a one-signature general offer, within one state, for three years; the first signed agreement in a state plus a standalone Exhibit E lets other districts subscribe.

**Recommendation.** Counsel confirms Stand will sign any state NDPA as drafted (standard clauses cannot be redlined) and will sign Exhibit E. Until then, the Missouri reply omits the Exhibit E sentence.

## Decisions made

### M1. Option B is "in-session view," not "aggregate only"
::src Luke's decision :: A coach who watches the team lead's student-level screen is receiving identifiable education records. Calling that "aggregate only" was wrong, and it was the one legal error in the earlier draft. Option B now means: no standing login; student-level data seen only in a live session with the team lead; the coach is a school official under the agreement, trained, under confidentiality. Option A means a standing, logged login. Both are honest. James's one-pager, which says "aggregate data only," has to change to match.
::src FERPA :: "Disclosure" under 34 C.F.R. § 99.3 means permitting access to or the release of PII by any means, including oral and visual; the school official exception (§ 99.31(a)(1)(i)(B)) authorizes the access when its conditions are met, whether or not the recipient holds credentials.
::src District lens :: A privacy officer's first objection to an earlier draft: "You say the coach cannot see student-level data, then arrange for the coach to watch the student-level dashboard on a shared screen. That is still disclosure."
::src Conversation :: Jonah (10/26) wanted the less intrusive approach with screen-share and one consistent protocol; James wanted to ask for access and fall back; Luke: the coach already hears names in every kid talk, so the agreement "operationalizes" a threshold already crossed.
::src AFUHSD precedent :: Teach For America (2026): the district accepted the partner coach seeing student data as the only partner viewer, acknowledged as a FERPA school official.

**What would reverse it:** Tara saying coaches cannot do the job without their own login, in which case Option A becomes the default and Option B the fallback. The clause supports either.

### M2. Identifiable data flows; the feed is not de-identified
::src James's MOU draft :: Current Section Six says "de-identified individual student data."
::src Conversation :: 10/19: a direct connection means identifiable data; with a strong agreement "there's more than there used to be" who say yes. Navigator cannot show a school team who needs support without names.
::src Luke's decision :: Identifiable, contained by role (5.4), use (5.5), and retention (5.6). A no-names fallback exists only if Emily confirms the platform can run that way (O9).

### M3. Discipline is optional
::src James's collateral :: Listed discipline among "only the data needed."
::src Conversation :: Tara (10/19): behavior data "we typically don't get"; Luke (10/26): discipline is "the most tightly held" element.
::src Luke's decision :: Not needed for the on-track calculation; the single element most likely to stall a privacy review. Optional, at the district's election. Reversed only if Tara names a Navigator feature that depends on it.

### M4. Sixty-day deletion, backups within ninety, a disposition form
::src SDPC NDPA :: Article IV: disposition within sixty days of written request; Exhibit D, Directive for Disposition of Data; de-identified data exempt.
::src Columbus City DSA :: Destroy or return within ninety days of termination.
::src James's MOU draft :: Current Section Five keeps identifiable data three years after termination.
::src af-dpa :: knowledge/practice/vendor-negotiation.md: backups expire on the documented rotation, never restored to production, with an outside date and certification.
::src Luke's decision :: Sixty days at termination or on directive satisfies NDPA v2, Columbus, and the stricter districts. Districts that do not use the NDPA get Exhibit D-4, a one-page directive modeled on NDPA Exhibit D, so the request is a form and not a negotiation. Emily's runbook (O13) has to make sixty days true.

### M5. De-identified and aggregate retention, with a review step
::src FERPA :: 34 C.F.R. § 99.31(b)(1); § 99.31(b)(2) allows coded student-level data only for education research with a code not based on personal information.
::src SDPC NDPA :: Article IV.5: use of de-identified data survives termination; no re-identification; transfer only under written no-re-identification terms with LEA consent; LEA approval before any publication naming it.
::src District lens :: Replacing an ID and suppressing small cells does not by itself prevent identification through rare combinations or repeated releases.
::src Luke's decision :: Keep row-level de-identified retention (pending O10) under NIST or Department of Education methods, a random token with a destroyed key, a documented reasonable-determination review before retention or release, cells under ten suppressed, and district approval before any district-identifiable publication.

### M6. The NDPA controls, and CHSS will sign it anywhere
::src SDPC NDPA :: The NDPA's own priority clause places the state exhibit and standard clauses above any other writing.
::src af-dpa :: Exhibit E mechanics; registry rows are district-created; the v1.2 "Provider" definition is a strained fit for a coaching nonprofit, so Section 5.1 states the school-official basis on its own.
::src District lens :: "If we sign both, 'the document the district signed controls' does not tell us which document controls."
::src Luke's decision :: Appendix A is the instrument where no NDPA is used; where the state NDPA is signed, it controls over Appendix A and the Agreement as to student data, and 5.2 and A.18 now say so in the same words. CHSS signs Exhibit E with the first district in each state (pending O12).

### M7. Three delivery tiers, described honestly
::src Emily's architecture :: v1 ingests files by SFTP or secure upload; no vendor API.
::src Conversation :: Luke's ranking (10/19): vendor feed, then district SFTP, then rostering tools last. The 10/26 reframe: integration help is part of the offer.
::src District lens :: "You promise no file transfers; SFTP is a file transfer. The agreement permits marking-period uploads and commits to two sessions."
::src Luke's decision :: Tier 1 automated feed is the target, Tier 2 scheduled upload is transitional, Tier 3 vendor connection is listed for districts that can do it. The case-making now says "no manual file handling once your automated feed is running," and support runs until the feed passes acceptance (pending O11).

### M8. Deterministic identifiers; pseudonyms stay inside the agreement
::src James's collateral :: "Records are matched using a consistent unique student identifier."
::src Emily's architecture :: Identity matching lists probabilistic matching.
::src FERPA :: A hash of the student number is a code "based on" personal information, so it does not qualify as a research code under § 99.31(b)(2)(iii). It is still usable as protected Student Data under the school-official arrangement.
::src Luke's decision :: District or state ID in every feed; a district-generated stable pseudonym is allowed and remains Student Data; probabilistic matching only flags duplicates for human review.

### M9. Minimum dataset
::src Emily's email :: "What is the minimum practical dataset we should request initially versus additional data we might pursue later?"
::src AFUHSD precedent :: District data teams strike elements they cannot produce accurately (AFUHSD feeder DSA, 2025).
::src Luke's decision :: Required: ID, name, grade level and enrollment, course enrollments, marks and credits by term, GPA, attendance. Everything else optional.

### M10. Breach notice at seventy-two hours, broad trigger, district controls family notice
::src SDPC NDPA :: Arizona NDPA v1.2 Article V.4: notification "within seventy-two (72) hours of confirmation of the incident, unless notification within this time limit would disrupt investigation."
::src af-dpa :: Keep the broad trigger; say who notifies families; allocate costs (parent notification, credit monitoring, legal fees, fines).
::src Luke's decision :: As drafted in A.8. Cost allocation is subject to O2.

### M11. Audit evidence on a menu
::src Columbus City DSA :: Annual third-party audits of security operations.
::src af-dpa :: NDPA v1.2 gives the LEA an audit right; the Utah evidence menu (self-assessment, questionnaire, SOC 2 or SOC 3, on-site by agreement).
::src Luke's decision :: Annual independent assessment and pen test (dates per O4); districts choose the form of evidence once a year; cooperation with an audit where state law requires.

### M12. District remedies: immediate suspension, subprocessor objection
::src District lens :: "If there is an active security problem, I cannot wait through a thirty-day cure period while access and transfers continue." "If we object to a subprocessor and your team cannot resolve it, the new provider still takes effect."
::src SDPC NDPA :: Article IV requires flow-down to subprocessors and a list available to the LEA; most state exhibits add notice and objection.
::src Luke's decision :: The district may suspend transfers and access immediately when reasonably necessary to protect Student Data, and may disable the affected processing or terminate without penalty if a subprocessor objection is not resolved before the change takes effect. Both are cheap and both are standard in district agreements I have signed.

### M13. Authorized technical personnel
::src District lens :: "You say all CHSS staff see only de-identified data, but somebody must administer Salesforce, troubleshoot imports, and investigate incidents."
::src Luke's decision :: A narrow role, named in 5.4 and A.7: minimum-necessary, time-limited, MFA, logged, under confidentiality, reviewed quarterly. Ordinary program and research staff stay de-identified-only.

### M14. The parental-consent sentence is narrowed
::src FERPA :: Disclosure under the school-official exception needs no consent when its conditions are met; screeners are a separate question under PPRA and state law.
::src District lens :: "That sentence appears to cover the screeners, even though later sections recognize they may require written consent."
::src Luke's decision :: 5.1 now says the District's disclosure for the Services needs no FERPA consent when the school-official conditions are met, and screeners are governed by 6.7.

### M15. Ohio: adopt the protections whether or not the statute applies
::src State law :: Ohio R.C. 3319.325–327 define "technology provider" by reference to school-issued devices or accounts; whether a staff-facing platform and a screener fall inside is a classification question for Ohio counsel.
::src Luke's decision :: A.17 says CHSS contractually adopts the Ohio protections regardless of the statutory definition. Ohio counsel classifies Navigator and the screeners.

### M16. Naming
::src Conversation :: Emily (10/26) proposed "A, B, C" implementation profiles; coach access is "Option A / B."
::src Luke's decision :: Implementation profiles are "Tier 1, 2, 3"; coach access is "Option A / B."
