# Decisions
::src Conversation :: Jonah (10/26): "we just need to have a little bit more of a calculus"; a small number of people decide. This page is the register: what is still open and who owns it, then the calls already made and why, so each can be defended or reversed on the record.
::src Drafting choice :: Source notes never refer to internal draft numbers; a change is described as a change from "an earlier draft." Version history lives in the header pill only.
::src Drafting choice :: **Open decisions** first. Use the person filter to see only the rows that need you; hover or tap "Why" on a row for the reasoning, the evidence that settles it, and the documents it touches. A row marked **Gate** holds the package until it closes. **Decisions made** follow, with the reasoning and what would reverse them.

Nothing goes to a district until every open decision marked **Gate** is closed. A decision is "made" only once there is a record of it: a call, an email, or a confirmation from the person named.

## Open decisions

:::register
| # | Decision | Owner | Approver | Needed by | Gate | Closed on / evidence |
|---|---|---|---|---|---|---|
| O1 | What the December Navigator pilot runs on: which schools, which agreement, what data | Jonah, Emily | Stand counsel | Before the Leadership Summit (late Nov) | **Gate** before the Summit | |
| O2 | Liability cap, indemnity, and breach-cost carve-out in Agreement Section Eight | Jonah | Stand counsel | Before Columbus review | **Gate** before signature | |
| O3 | AI model provider: name, tier, data-use terms, no-training attestation, zero-retention arrangement | Emily | Jonah | Before any district sees the package | **Gate** before external distribution | |
| O4 | Which security controls are true today; dates for the rest (Appendix A.7, A.9, A.13; Part C) | Emily | Jonah | Before any district sees the package | **Gate** before external distribution | |
| O5 | Background checks and annual privacy training for every person with access to Student Data: coaches under both options, technical staff | Demian, James | Jonah | Before any coach sees student-level data | **Gate** before signature | |
| O6 | Screener consent classification, item by item, and the district authorization form | Tara, Stand counsel | Jonah | Before any screener runs in a new district | **Gate** for screeners | |
| O7 | Insurance limits actually held; self-insurance posture | Demian, Stand counsel | Jonah | Before signature | **Gate** before signature | |
| O8 | Stand for Children Leadership Center, Inc. as the 501(c)(3) signatory; no-advocacy clause acceptable | Stand counsel | Jonah | Before external distribution | **Gate** before external distribution | |
| O9 | Whether a Navigator tenant can run without student names (pseudonymous election) | Emily | Jonah, Tara | Before Columbus review | Bracket | |
| O10 | Row-level de-identified retention is needed for the evaluation design, and the retained-data inventory | Tara, Jonah | Stand counsel | Before Columbus review | Bracket | |
| O11 | Integration support through acceptance plus maintenance: staffing and hours | Jonah | Emily | Before external distribution | Bracket | |
| O12 | Exhibit E general offer in every state, and signing NDPA standard clauses without redline | Stand counsel | Jonah | Before the Missouri reply and before external distribution | **Gate** for the Exhibit E promise | |
| O13 | Deletion runbook across Salesforce, Azure/Fabric, Power BI, backups, subprocessors, within sixty days | Emily | Jonah | Before signature | **Gate** before signature | |
| O14 | Complete subprocessor list and U.S. region for every tenant | Emily | Jonah | Before signature | **Gate** before signature | |
| O15 | One delivery cadence rule for Year 1: weekly required, with Tier 2 as a dated interim exception | Jonah, Emily | Tara | Before external distribution | Bracket | |
| O16 | The Kid Talk outcome claim: calculation, denominator, period, sample, and permitted wording | James, Tara | Jonah | Before the case-making goes to any district | **Gate** for the claim | |
:::

:::why O1
::src Conversation :: Jonah (10/26): starting with districts in January "gives us the four or five months of let's get this set up before students start." James (10/23): "when we come to them in April and say, hey, it's time to engineer this SIS integration."
::src James's MOU draft :: Year 0 is readiness ("data access and reporting setup" is listed among Year 0 activities); Year 1 is implementation.
::src Emily's email :: Navigator "target launch at the CHSS Leadership Summit in late November 2026 and pilot schools beginning in December."
::src District lens :: Counsel reads a December pilot next to a three-month board calendar and concludes the agreement is being asked to cover data already moving. Columbus City said board approval takes about three months.
::src Luke's decision :: The January cohort's timeline is decided (M17): readiness in Year 0, live data with Year 1 instruction in August 2027, no Student Data before signature. What remains open is only the pilot.

The new cohort is not sharing data in December. The pilot is existing partner schools, so the open question is which agreement covers them and whether the data is de-identified as today. The safe answer: existing partners, existing agreements, de-identified uploads. **Evidence that settles it:** a written statement of the pilot's schools, agreement basis, and data. **Documents:** none in this package; the pilot stays outside the new cohort's agreement.
:::

:::why O2
::src James's MOU draft :: Section Eight: services "as is"; no liability for indirect or consequential damages; "in no event will the liability of Organization and its affiliates ... exceed applicable liability insurance proceeds"; "reasonable liability insurance."
::src af-dpa :: knowledge/practice/dpa-review-checklist.md: "the NDPA has no insurance clause ... No liability cap or indemnity"; district practice is to "carve out data breach, confidentiality and indemnity obligations, or set a breach super-cap."
::src San Diego CCAP :: Mutual indemnification with defined allocation for sole, concurrent, and joint-defense cases; CGL $1M/$2M, E&O $1M, additional insured.
::src District lens :: A board attorney reading Appendix A's breach-cost promise next to Section Eight's cap asks which one wins. Until reconciled, the privacy promises read as capped at the insurance limit and excluding the losses a breach actually causes.

Carve breach costs under A.8, confidentiality, and privacy indemnity out of the Section Eight cap, or give them a super-cap of not less than the cyber limit, and add a mutual indemnity for each party's own acts. Jonah's call because it is money; counsel's because it is drafting. **Evidence:** counsel's redline of Section Eight. **Documents:** District commitments, conforming edits; Appendix A.8, A.14.
:::

:::why O3
::src Emily's architecture :: AI-assisted mapping, validation, "risk models and intervention recommendations."
::src Luke's experience :: Arizona NDPA Exhibit G AI questionnaire: base model and provider, data shared with AI subprocessors, training on user data, human in the loop, query logging.
::src District lens :: A privacy officer will not accept a blank where the model provider's name belongs; a CTO wants the provider's data-use terms by URL and date.

Emily returns the subprocessor table filled in: provider, product tier or API, data-use terms by URL and date, country of processing, zero-retention arrangement, and the provider's written no-training attestation. **Documents:** Appendix A.6, A.12; Part C.
:::

:::why O4
::src Emily's architecture :: Every platform fact in Appendix A and Part C is drawn from the diagram and the 10/26 call; none has been verified against a live tenant.
::src District lens :: "This is a strong target-state security program. I still do not know which controls exist in the live tenant, which are scheduled, and which are aspirational."

Line by line against Part C and A.7: true today, true by date, or no. Lines not true today are re-tensed to "by [date]" before any district reads them. **Evidence:** the control-readiness list with evidence per line. **Documents:** Appendix A.7, A.9, A.13; Part C; the Notes page's list for Emily.
:::

:::why O5
::src Conversation :: Luke and Jonah (10/26): Phoenix Union required fingerprinting and onboarding of virtual Teach For America mentors; naming a CHSS background check removes one reason for a district to impose its own.
::src District lens :: "If the appendix says every person with access passes a background check and completes annual training, show me the policy and the roster." And: Option B coaches still receive student-level records visually, so the gate applies to them too.

Demian confirms current practice for coaches and technical staff. If not current, A.7 becomes "by [date]" and no coach sees student-level data, under either option, until then. **Evidence:** HR confirmation or a dated plan. **Documents:** Appendix A.7; District commitments 5.4.
:::

:::why O6
::src State law :: Arizona A.R.S. § 15-104 requires prior written parental consent for mental health screening in schools, and § 15-117 exempts § 15-104 screenings from its separate survey regime. The Department of Education's August 26, 2026 letter treats behavioral health screeners that probe emotional or psychological states as requiring written consent; PPRA opt-out is not a substitute.
::src Emily's email :: The agreement must cover the Belonging and Skills screeners.
::src District lens :: A privacy officer will not approve "notice, opt-out, or consent" without the instruments in hand.
::src District lens :: A California district technology and privacy lead (10/27 call): California districts run Panorama wellness surveys several times a year, with parent notification now required on gender-identity items; Arizona districts cannot run them at all. The agreement now lets a district decline a screener and keeps the Services running without it.

Tara supplies the versioned instruments and the program purpose; counsel classifies each item against PPRA's protected areas and § 15-104; the district authorization and consent-certification form is drafted. Plan for Arizona districts to decline the Belonging Screener. **Documents:** District commitments 6.7; Appendix A.15, A.17.
:::

:::why O7
::src Columbus City DSA :: At least $1,000,000 cyber liability.
::src af-dpa :: District practice research: "$1M for directory-only, $2M+ for SIS, assessment, special education or health data"; Beaverton requires $2M per claim and aggregate with a two-year tail.
::src District lens :: "A 'reasonable self-insurance program' is not the same as a policy carrying the stated limits."

Drafted at $2,000,000 per claim and aggregate with a two-year tail, plus CGL $1M/$2M and E&O $1M; self-insurance only if documented and accepted by the district in writing. **Evidence:** certificate of insurance. **Documents:** Appendix A.14; District commitments conforming edits.
:::

:::why O8
::src James's MOU draft :: Names "Stand for Children Leadership Center Inc." as the Organization.
::src Conversation :: James (10/23): Stand is both a (c)(3) and a (c)(4); "there doesn't actually have to be something wrong for people to raise a stink."

Counsel confirms the Leadership Center is the correct 501(c)(3) signatory and that the no-advocacy clause in A.4(d) is acceptable as written. **Documents:** District commitments 5.1; Appendix Part A, A.4.
:::

:::why O9
::src Luke's experience :: AFUHSD's first ask of Teach For America (2025) was to strip names and keep the linking key; the district's own feeds use deterministic transformations or a mapping table.
::src District lens :: A "fallback without names" that the agreement does not contain is a promise a data manager will test and find missing.

Emily answers whether a tenant can operate without names and which features would be off. If yes, Exhibit D-3 gets a pseudonymous election and the agreement says what the district loses. If no, the fallback is dropped from the pitch. **Documents:** District commitments 6.4, D-3.
:::

:::why O10
::src Conversation :: Tara and Jonah (10/19): follow students "from ninth grade success to CTE enrollment, pathway completion, dual credit, graduation"; James (10/23): keep "went from 60% to 72%," delete student-level data.
::src FERPA :: 34 C.F.R. § 99.31(b)(1); Department of Education guidance warns that removing direct identifiers is not enough and that complementary suppression may be needed.
::src District lens :: A privacy officer asks whether cohort-level results need row-level records at all, and what process makes retained rows not personally identifiable.

Tara and Jonah describe the longitudinal analyses and the exact row-level fields, purpose, review method, and retention period, so A.10 can describe them. The clause already requires the documented reasonable-determination review. **Documents:** District commitments 5.5–5.6; Appendix A.10.
:::

:::why O11
::src Conversation :: Jonah (10/26): integration help is "almost like another form of coaching we're going to offer."
::src District lens :: A data manager's read of "two working sessions": "I still do not know whether support ends before the feed works."

The agreement now promises support until the feed passes acceptance, plus maintenance on SIS, grading-scale, or term changes. That is a staffing cost. **Evidence:** staffing and hours decision. **Documents:** District commitments 6.9; case-making.
:::

:::why O12
::src Conversation :: James (10/26): "at a given, we are going to have to sign their data agreement. There's no negotiation there." That is the record for signing districts' agreements, including the NDPA. Exhibit E, a standing general offer in every state, is a new commitment with no record yet.
::src af-dpa :: NDPA standard clauses cannot be redlined; Exhibit E extends a signed NDPA's privacy terms within a state for three years.
::src District lens :: "Page E says counsel has not approved Exhibit E, but the district-facing pages promise it without qualification." The district-facing pages now say "expects to offer" with a bracket until counsel confirms.

Counsel confirms that Stand will sign NDPA standard clauses without redline in any state and will sign Exhibit E. Until then the Missouri reply omits the Exhibit E sentence and the appendix brackets it. **Documents:** District commitments 5.2; Appendix Part A; Notes.
:::

:::why O13
::src SDPC NDPA :: Sixty days from written request; v2: sixty days from termination.
::src District lens :: "Demonstrate deletion across the full platform," including backups and subprocessors.

A runbook that returns or destroys a district's data within sixty days across every store, with backups expiring on a rotation of ninety days or less, never restored to production, and a certificate template; one tested dry run. **Documents:** District commitments 5.6, D-4; Appendix A.10.
:::

:::why O14
::src Emily's architecture :: Azure/Fabric, Salesforce Experience Cloud and CRM Analytics, Power BI, an AI provider.
::src Columbus City DSA :: "No student data is stored outside the United States without the District's written consent."

Tenant settings or contract excerpts showing each subprocessor and its U.S. region, and confirmation that the list is complete. **Documents:** Appendix A.6, A.9; Part C.
:::

:::why O15
::src District lens :: "Is weekly delivery required, preferred, or only the Tier 1 target? Tier 2 says every marking period is acceptable, while the onboarding timeline says weekly updates begin on day one."
::src James's collateral :: "Current data. Dashboards update automatically, not once a grading period." The coaching model needs Friday's data on Tuesday.
::src Luke's decision :: Drafted as one rule, pending confirmation: once the feed is live for Year 1, updates are weekly; a Tier 2 district may run an approved interim cadence, not less than monthly, recorded in Exhibit D-3 with a dated target for Tier 1.

Jonah and Emily confirm that weekly is the Year 1 standard and that CHSS will hold Tier 2 districts to an interim cadence with a target date. If marking-period delivery must remain acceptable indefinitely, the Friday-to-Tuesday promise comes out of the case-making. **Documents:** District commitments 6.5, D-2, D-3; case-making.
:::

:::why O16
::src James's collateral :: James's 10/23 email: "Our own data shows us that when teams do a Kid Talk with fidelity they are 70%+ more likely to hit their on-track goal."
::src District lens :: "Seventy percent more likely than what, across how many schools, over what period, and controlling for what? Is this correlation or evidence that the protocol caused the result?"

James and Tara validate the calculation, denominator, period, and sample, and approve the wording. The case-making uses "associated with" unless the analysis supports a causal claim, and footnotes the method. **Documents:** case-making.
:::

## Decisions made

### M1. Option B is "in-session view," not "aggregate only"
::src Luke's decision :: A coach who watches the team lead's student-level screen is receiving identifiable education records. Calling that "aggregate only" was wrong, and it was the one legal error in the earlier draft. Option B now means: no standing login; student-level data seen only in a live session with the team lead; the coach is a school official under the agreement, trained, under confidentiality; CHSS keeps a session record (coach, school, team lead, date, purpose). Option A means a standing, logged login. Both are honest. James's one-pager, which says "aggregate data only," has to change to match.
::src FERPA :: "Disclosure" under 34 C.F.R. § 99.3 means permitting access to or release of PII by any means, including oral and visual; the school official exception (§ 99.31(a)(1)(i)(B)) authorizes the access when its conditions are met, whether or not the recipient holds credentials.
::src District lens :: A privacy officer's first objection to an earlier draft: "You say the coach cannot see student-level data, then arrange for the coach to watch the student-level dashboard on a shared screen. That is still disclosure." A CTO's follow-up: the platform cannot log who looks at a shared screen, so the session record replaces a logging claim it could not keep.
::src Conversation :: Jonah (10/26) wanted the less intrusive approach with screen-share and one consistent protocol; James wanted to ask for access and fall back; Luke: the coach already hears names in every kid talk, so the agreement "operationalizes" a threshold already crossed.
::src AFUHSD precedent :: Teach For America (2026): the district accepted the partner coach seeing student data as the only partner viewer, acknowledged as a FERPA school official.
::src District lens :: A California district technology and privacy lead (10/27 call): outside partners who support students get data "we pull for them," no credentials, always under an executed agreement; identifiable versus de-identified for a coach "is not a huge difference" once an agreement is in place; personnel physically in classrooms may need volunteer clearance or fingerprinting regardless. Option B is the common pattern, not an invention.

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
::src Luke's decision :: Sixty days at termination or on directive satisfies NDPA v2, Columbus, and the stricter districts. Districts that do not use the NDPA get Exhibit D-4, a one-page directive modeled on NDPA Exhibit D. Emily's runbook (O13) has to make sixty days true.

### M5. De-identified and aggregate retention, with a documented review
::src FERPA :: 34 C.F.R. § 99.31(b)(1); § 99.31(b)(2) allows coded student-level data only for education research with a code not based on personal information.
::src SDPC NDPA :: Article IV.5: use of de-identified data survives termination; no re-identification; transfer only under written no-re-identification terms with LEA consent; LEA approval before any publication naming it.
::src District lens :: Replacing an ID and suppressing small cells does not by itself prevent identification through rare combinations or repeated releases; the operative clause has to require the review the decision page promised.
::src District lens :: A California district technology and privacy lead (10/27 call) confirmed de-identified retention after termination is acceptable "as long as we can't trace it back," provided the agreement states it explicitly; her district de-identifies with its own assessment-office key for a county partner.
::src Luke's decision :: Appendix A.10 now requires a documented reasonable-determination review before any De-identified Data is retained or released, covering direct and indirect identifiers, other reasonably available information, repeated-release risk, and complementary suppression, with the record available to the district on request. Row-level retention itself is subject to O10.

### M6. Where the NDPA is signed, it controls; Appendix A always applies
::src SDPC NDPA :: The NDPA's own priority clause places the state exhibit and standard clauses above any other writing.
::src Conversation :: James (10/26): "we are going to have to sign their data agreement. There's no negotiation there." The commitment to sign districts' agreements, including the NDPA, has a record. Exhibit E does not yet (O12).
::src District lens :: "If we sign both, 'the document the district signed controls' does not tell us which document controls." And: "Which custom AI, insurance, screener, and security commitments survive when we elect the NDPA?"
::src Luke's decision :: One mechanical rule, stated the same way in 5.2, Part A, and A.18: Appendix A applies in every case; where the state NDPA is executed or Exhibit E is accepted, the NDPA controls as to any conflict and Appendix A continues as a supplement for everything the NDPA does not address. The election form offers "Appendix A," "Appendix A plus state NDPA," and "Appendix A plus Exhibit E acceptance."

### M7. Three delivery tiers, described honestly
::src Emily's architecture :: v1 ingests files by SFTP or secure upload; no vendor API.
::src Conversation :: Luke's ranking (10/19): vendor feed, then district SFTP, then rostering tools last. The 10/26 reframe: integration help is part of the offer.
::src District lens :: "You promise no file transfers; SFTP is a file transfer."
::src Luke's decision :: Tier 1 automated feed is the target, Tier 2 scheduled upload is a dated interim exception, Tier 3 vendor connection is listed for districts that can do it. The case-making says "no manual file handling once your automated feed is running," and support runs until the feed passes acceptance (O11). The cadence rule is O15.

### M8. Deterministic identifiers; pseudonyms stay inside the agreement
::src James's collateral :: "Records are matched using a consistent unique student identifier."
::src Emily's architecture :: Identity matching lists probabilistic matching.
::src FERPA :: A hash of the student number is a code "based on" personal information, so it does not qualify as a research code under § 99.31(b)(2)(iii). It is still usable as protected Student Data under the school-official arrangement.
::src Luke's decision :: District or state ID in every feed; a district-generated stable pseudonym is allowed and remains Student Data; probabilistic matching only flags duplicates for human review.

### M9. Minimum dataset
::src Emily's email :: "What is the minimum practical dataset we should request initially versus additional data we might pursue later?"
::src AFUHSD precedent :: District data teams strike elements they cannot produce accurately (AFUHSD feeder DSA, 2025).
::src Luke's decision :: Required: ID, name, grade level and enrollment dates, course enrollments, marks and credits by term, GPA, attendance. Everything else optional, and the most protected categories are marked sensitive and never requested by default (M20). The case-making's "only the data needed" list now matches this exactly and names the screeners.

### M10. Breach notice at seventy-two hours, broad trigger, district controls family notice
::src SDPC NDPA :: Arizona NDPA v1.2 Article V.4: notification "within seventy-two (72) hours of confirmation of the incident, unless notification within this time limit would disrupt investigation."
::src af-dpa :: Keep the broad trigger; say who notifies families; allocate costs (parent notification, credit monitoring, legal fees, fines).
::src Luke's decision :: As drafted in A.8. Cost allocation is subject to O2.

### M11. Audit evidence on a menu
::src Columbus City DSA :: Annual third-party audits of security operations.
::src af-dpa :: NDPA v1.2 gives the LEA an audit right; the Utah evidence menu (self-assessment, questionnaire, SOC 2 or SOC 3, on-site by agreement).
::src Luke's decision :: Annual independent assessment and pen test (dates per O4); districts choose the form of evidence once a year; cooperation with an audit where state law requires.

### M12. District remedies: immediate suspension, subprocessor objection, termination effect
::src District lens :: "If there is an active security problem, I cannot wait through a thirty-day cure period." "If we object to a subprocessor and your team cannot resolve it, the new provider still takes effect." "If we terminate only the data provisions, what happens to the rest of the Services?"
::src SDPC NDPA :: Article IV requires flow-down to subprocessors and a list available to the LEA; most state exhibits add notice and objection.
::src Luke's decision :: The district may suspend transfers and access immediately when reasonably necessary to protect Student Data; may exclude its data, disable the feature, or terminate without penalty when a subprocessor objection is unresolved; and when the data provisions end, the affected Services are suspended and the district may terminate the Agreement without penalty if the Services cannot lawfully continue. All standard in district agreements I have signed.

### M13. Authorized technical personnel
::src District lens :: "Somebody must administer Salesforce, troubleshoot imports, and investigate incidents."
::src Luke's decision :: A narrow role, named in 5.4 and A.7: minimum-necessary, time-limited, MFA, logged, under confidentiality, reviewed quarterly. Ordinary program and research staff stay de-identified-only. The O5 personnel gate covers this role too.

### M14. The parental-consent sentence is narrowed
::src FERPA :: Disclosure under the school-official exception needs no consent when its conditions are met; screeners are a separate question under PPRA and state law.
::src District lens :: "That sentence appears to cover the screeners, even though later sections recognize they may require written consent."
::src Luke's decision :: 5.1 says the District's disclosure for the Services needs no FERPA consent when the school-official conditions are met, and screeners are governed by 6.7.

### M15. Ohio: adopt the protections whether or not the statute applies
::src State law :: Ohio R.C. 3319.325–327 define "technology provider" by reference to school-issued devices or accounts; whether a staff-facing platform and a screener fall inside is a classification question for Ohio counsel.
::src Luke's decision :: A.17 says CHSS contractually adopts the Ohio protections regardless of the statutory definition. Ohio counsel classifies Navigator and the screeners.

### M16. Naming
::src Conversation :: Emily (10/26) proposed "A, B, C" implementation profiles; coach access is "Option A / B."
::src Luke's decision :: Implementation profiles are "Tier 1, 2, 3"; coach access is "Option A / B."

### M17. The January cohort's timeline: ready in Year 0, live in Year 1
::src Conversation :: Jonah (10/26): January start "gives us the four or five months of let's get this set up before students start." James (10/23): "come to them in April and say it's time to engineer."
::src James's MOU draft :: Year 0 readiness; Year 1 implementation.
::src District lens :: Procurement: "the timeline says we name contacts in mid-January and use them to route the agreement, but §6.1 starts the obligation fifteen business days after signature." Contacts are now collected at acceptance and confirmed within fifteen business days after execution.
::src Luke's decision :: No Student Data before signature; contacts named at acceptance; agreement routed and executed in Year 0; optional test load after execution; acceptance thirty days before Year 1 instruction; live feed on the first day of Year 1 (August 2027 for the January cohort). The December pilot is a separate question (O1).

### M18. "$0 due to CHSS," with the district's effort stated beside it
::src James's MOU draft :: Section Seven: "the amount due from District under this Agreement is $0."
::src District lens :: "The amount due to CHSS may be $0, but we are contributing staff time and may incur SIS-vendor or integration costs."
::src Luke's decision :: The headline is "$0 due to CHSS," never "costs nothing," and the staff-effort paragraph sits directly under it. Who pays a SIS vendor's export or API fee under Tier 3 is a note for Jonah, not a decision in this register.

### M19. No automatic renewal of the data provisions
::src District lens :: A California district technology and privacy lead (10/27 call) reads every agreement for four things "with no gray area": auto-renewals, what happens when data is compromised, destruction at the end of the contract, and selling or advertising to third parties. The other three were already in the drafts; auto-renewal was not addressed.
::src James's MOU draft :: Section Four: no financial commitment beyond Year 1; any continued services "shall be documented in a separate written agreement signed by both Parties."
::src Luke's decision :: The data provisions and Appendix A end with the Agreement's term and never renew by silence; continuing data sharing takes a new signature. Stated in A.16, in the conforming edits, and as a bullet in the case-making. It costs CHSS nothing and removes a standard finding from every district's checklist.

### M20. Sensitive elements are never requested by default
::src District lens :: The same California lead ranks meal status, special education status, and graduation date as the most protected categories and recently refused a partner's request for meal data with the district attorney's backing.
::src Luke's decision :: IEP/504 status and free or reduced-price meal status are split out of the optional demographics row in Exhibit D-1, labeled "Optional, sensitive," marked not needed for Navigator, and never requested unless the District elects to provide them. Reversed only if Tara shows a Navigator feature that needs them.

### M21. Appendix A carries California's nine required terms, mapped
::src State law :: California Education Code § 49073.1(b), enacted by AB 1584, requires nine terms in any district contract for digital storage, management, or retrieval of pupil records or for educational software that lets a third party access pupil records: (1) district ownership and control; (2) pupil control of pupil-generated content, if applicable; (3) no use beyond the contract's purposes; (4) parent review and correction procedures; (5) security actions including designation and training of responsible individuals; (6) procedures for notifying affected parents of unauthorized disclosure; (7) certification of non-retention at completion and how it is enforced; (8) how the district and third party jointly ensure FERPA compliance; (9) no targeted advertising.
::src District lens :: A California colleague shared the CETPA/Fagen Friedman & Fulfrost AB 1584 compliance checklist (10/27), which is how California district counsel review a partner agreement: nine boxes. A San Diego reviewer will tick them in order.
::src Luke's decision :: Six of the nine were already in Appendix A. Three were implicit and are now explicit: a described parent-notification procedure after a breach (A.8), named responsible individuals with a line in Exhibit D-3 (A.7), and a joint FERPA compliance paragraph (A.2). The pupil-generated-content term is answered "none held" (A.5) rather than left to inference. The California bullet in A.17 maps all nine to their sections so the review takes five minutes instead of an afternoon.
