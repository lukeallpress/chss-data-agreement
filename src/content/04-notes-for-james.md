# Notes
::src Drafting choice :: Working page for the CHSS team. First, every claim the drafts make on CHSS's behalf that someone at CHSS has to confirm, grouped by who confirms it. Then the paste-ready email blocks for James, collapsed.
::src Conversation :: Jonah (10/26): "this is our commitment ... this is our technical deliverable." Emily: "I would like to at least review and be involved in what you wrote." The claims below are exactly what that review is for.

The drafts describe CHSS as it needs to be, not necessarily as it is today. Each line below is a statement a district will test. Confirm it, date it, or strike it before the package leaves the building.

## For Emily: the gap analysis
::src Conversation :: Emily (10/27): "I want to see the gap of whether or not we have it today ... check, check, check, or okay, we need to tighten this up." Her example: a district requires 45-day retention and the platform does 30. She asked for the requirements that imply a policy, the measures each policy implies, and the technical items that must be in place, separate from the agreement text.
::src Drafting choice :: The table lists the requirements that recur across the NDPA, the Columbus City agreement, California Education Code § 49073.1, and Appendix A, each with the measure it implies and a blank for CHSS's current state. Fill the last three columns; anything marked "gap" becomes a dated commitment in Attachment 1.

Fill in **Current practice**, **Gap**, and **Action / date**:

| # | Requirement | Where it comes from | Measure it implies | Current practice | Gap | Action / date |
|---|---|---|---|---|---|---|
| G1 | Student Data stored and processed only in U.S. regions | Columbus; NDPA state exhibits; A.9 | Tenant region settings for Azure, Fabric, Salesforce, Power BI, AI provider | | | |
| G2 | Complete, named subprocessor list; 30 days' notice of changes; district remedy on objection | NDPA; A.6 | Subprocessor register; contract flow-down clauses; notice procedure | | | |
| G3 | AI provider named; no training on district data; zero-retention arrangement; human review of suggestions | Arizona Exhibit G; A.12 | Provider contract excerpt; feature design; written attestation | | | |
| G4 | Encryption in transit (TLS 1.2+) and at rest (AES-256) on every store including backups and the SFTP landing zone | NDPA Exhibit F; A.7 | Platform configuration; key management | | | |
| G5 | MFA for all CHSS accounts; SSO for district users | A.7 | Identity configuration; SAML/OIDC support | | | |
| G6 | Every access to student-level records logged; logs tamper-protected, kept 12 months, exportable per district | Columbus §8; A.7 | Salesforce event monitoring or equivalent; log retention; export procedure | | | |
| G7 | Documented access roster, quarterly review, one-business-day deprovisioning | Columbus §8; A.7 | Access review process; offboarding checklist | | | |
| G8 | Critical patches within 7 days; anti-malware; firewall segregation; encrypted, tested backups | Columbus §7; A.7 | Patch management SLA; endpoint protection; backup test records | | | |
| G9 | Annual independent assessment (SOC 2 Type II or equivalent) and annual penetration test | Columbus §7; A.7, A.13 | Audit engagement; pen test engagement; first completion date | | | |
| G10 | Written, tested incident response plan; district notified within 72 hours of confirmation | NDPA v1.2 V.4; Ohio R.C. 1347.12; A.8 | Plan document; tabletop exercise; notification template | | | |
| G11 | Parent-notification procedure after a breach: affected list, draft notice, district sends or directs, costs borne by CHSS | Cal. Ed Code 49073.1(b)(6); A.8 | Runbook section; notice template | | | |
| G12 | Return or destroy Student Data within 60 days of directive or termination, across every store; backups expire within 90 days; officer's certificate | NDPA Art. IV; Columbus; A.10 | Deletion runbook across Salesforce, Azure/Fabric, Power BI, backups, subprocessors; certificate template; dry run | | | |
| G13 | De-identification: random token not derived from the student ID, key destroyed with identifiable data, documented reasonable-determination review, cell suppression under 10 | FERPA § 99.31(b); A.10 | Tokenization step; review checklist; dashboard suppression rule | | | |
| G14 | Background checks and annual privacy training for all staff with access, coaches included | A.7; O5 | HR policy; training records | | | |
| G15 | Named privacy officer and security officer | Cal. Ed Code 49073.1(b)(5); A.7 | Two names on Exhibit D-3 | | | |
| G16 | Cyber liability $2M per claim and aggregate with two-year tail; CGL $1M/$2M; E&O $1M; certificates on request | Columbus §9; A.14 | Policy limits; certificate | | | |
| G17 | No automatic renewal; data term ends with the agreement | District checklists; A.16 | Contract term language | | | |
| G18 | Per-load validation report (rejected files, rejected rows, warnings); failure notice within one business day; acceptance test | 6.9, D-3 | Ingestion validation; monitoring and alerting; acceptance procedure | | | |
| G19 | Screener collection opens only after district authorization and consent certification; instruments versioned | 6.7; A.15 | Feature gate per district; instrument versioning | | | |
| G20 | A Navigator tenant can run without student names (if a district requires it) | O9 | Platform answer: yes, no, or with which features off | | | |
| G21 | Published Data Security and Privacy Plan at a CHSS URL | NY Education Law § 2-d; 8 NYCRR Part 121; TEC NDPA Exhibit K | Plan document covering requirements, safeguards, Parents' Bill of Rights compliance, training, subprocessors, incidents, disposition | | | |
| G22 | Accessibility conformance report for Navigator (WCAG 2.1 AA) | TEC NDPA Schedule 1 | Salesforce platform VPAT plus a report for CHSS's custom pages; remediation plan | | | |
| G23 | A named cybersecurity framework CHSS can claim alignment with; New Hampshire's 23 controls or an annual certification | TEC NDPA Exhibit F; NH Exhibit G; NY Exhibit G (NIST CSF) | Framework mapping; control evidence or certification | | | |
| G24 | Teacher and staff data protected like student data | NH Exhibit G and Exhibit I | Inventory of staff data in Navigator; same controls | | | |
| G25 | Criminal background checks for every employee with direct contact with students | MA, ME, NH, NY, RI, VT Exhibit Gs; A.7 | HR policy; roster of who has student contact | | | |

## For Emily: technical claims to confirm
::src Emily's architecture :: Every platform fact in Appendix A and Attachment 1 is drawn from the CHSS Data Platform diagram and the 10/26 call; none has been verified against a live tenant.
::src District lens :: A CTO will ask for evidence of each present-tense control; a privacy officer will not accept a blank where the model provider belongs.

Answer each as **true today**, **true by [date]**, or **no**:

1. Microsoft Azure / Fabric, Salesforce Experience Cloud and CRM Analytics, and Power BI are the complete subprocessor list for Student Data, and every tenant is in a U.S. region. (A.6, A.9)
2. The AI model provider: name, product tier or API, the data-use terms by URL and date, country of processing, and whether a zero-retention arrangement is enabled. (A.6, A.12)
3. No Student Data, de-identified data, or outputs are used to train or fine-tune any model, by CHSS or any subprocessor, and the provider will attest to that in writing on request. (A.12)
4. Access to student-level records is logged (user, time, record), logs are tamper-protected and kept twelve months, and a per-district export is possible. (A.7)
5. MFA on every CHSS staff and administrator account; SSO (SAML or OIDC) available to district users. (A.7, Attachment 1)
6. Encryption in transit TLS 1.2 or higher and at rest AES-256 across the data lake, warehouse, Salesforce, Power BI, backups, and the SFTP landing zone. (A.7)
7. Critical security patches within seven days; anti-malware on all endpoints with access; firewall and network segregation of production; encrypted, tested backups. (A.7)
8. A documented access roster reviewed quarterly, with deprovisioning within one business day. (A.7)
9. A written, tested incident response plan that can meet seventy-two-hour district notification. (A.8)
10. Independent security assessment (SOC 2 Type II or equivalent) and annual penetration test: current status and the earliest honest completion date. (A.7, A.13, Attachment 1)
11. A deletion runbook that returns or destroys a district's data within sixty days across every store, with backups expiring on a rotation of ninety days or less and never restored to production, and a certificate template. (5.6, A.10)
12. The de-identification step produces a random token not derived from any student identifier, with the key destroyed alongside identifiable data. (A.10)
13. Deterministic matching on district or state ID is the rule; probabilistic matching only flags duplicates for human review. (6.4, Attachment 1)
14. Cell suppression below ten in every aggregate output and dashboard. (A.10)
15. Whether a Navigator tenant can run without student names, and which features would be off. (O9)
16. The December pilot: which schools, under which agreement, with what data. (O1)
17. Integration support: what "support until the feed passes acceptance" costs in staff time, and who staffs it. (6.9, O11)
18. Be ready to demo Navigator to a district's technology or privacy lead and answer the four questions they ask of any AI feature: is the model CHSS's own or a third party's; exactly what goes into the prompt; who at CHSS, the provider, or any maintenance contractor can see inputs and outputs; and what the agent does with the output. (A.12(i); a California district lead asks exactly these and says vendors are often surprised to be asked.)
19. Attachment 1 is written in the present tense. Besides the two visible brackets (`[AI model provider]` and the first assessment date), the following are also claims that may need re-tensing or a bracket until confirmed: U.S.-only processing for every tenant, record-level access logging, seven-day patching, the deletion runbook, the personnel practice in A.7, and the insurance limits. Mark each one.

## The NDPA: one signature, eighteen states
::src Lewis County :: On 10/29 TEC's SDPA coordinator, who represents the Massachusetts, Maine, Colorado, Idaho, Illinois, Iowa, Kentucky, Missouri, Nebraska, New Hampshire, New Jersey, New York, Ohio, Rhode Island, Tennessee, Vermont, Virginia, and Washington alliances of the Student Data Privacy Consortium, sent CHSS the multi-state NDPA as a fillable PDF, with Lewis County C-1 as the originating district. CHSS signs once; TEC has Lewis County countersign; CHSS is posted as "Approved for Use" on the alliance databases; any district in those eighteen states subscribes by completing Exhibit E, which TEC forwards. "You only need to review and sign the DPA once regardless of the number of participating districts."
::src SDPC NDPA :: Read against a published agreement from the same family: MA-ME-NH-NY-RI-VT-NDPA, Standard Version 1.0, executed 2023–24. Version 1.0: three-year term; Exhibit E expires three years from the original signature; Article I.1 makes the provider a school official; Article IV.5 permits de-identified use "to demonstrate the effectiveness of the Services," surviving termination; Article IV.6, disposition within sixty days of request; Article V.2, an annual LEA audit right on ten business days' notice; Article V.3, the provider implements a framework listed in Exhibit F; Article V.4, breach notice within seventy-two hours, and the LEA notifies families.
::src State law :: The state Exhibit Gs in that family add, among other things: in Massachusetts, Maine, New Hampshire, Rhode Island, Vermont, and New York, use is limited to the Exhibit A services ("or stated in the Service Agreement" is deleted) and "all employees of the Provider who will have direct contact with students shall pass criminal background checks"; in New Hampshire, a list of twenty-three security controls or an annual certification under NIST SP 800-171, NIST SP 800-53, FedRAMP, ISO 27001, CIS IG1, SOC 2 Type 2, or PCI DSS, plus protection of teacher data (Exhibit I); in New York, Education Law § 2-d and 8 NYCRR Part 121: a published Data Security and Privacy Plan (Exhibit K), the district's Parents' Bill of Rights (Exhibit J), NIST Cybersecurity Framework alignment, storage in the United States or Canada, ninety-day disposition, provider-paid parent notification for breaches it causes, and an independent audit if the State's Chief Privacy Officer requires one. New York's definition of "Provider" expressly includes a nonprofit "educational partnership organization" receiving student data.
::src Conversation :: 10/27 call: Jonah and Emily agreed to prepare to sign version 1 with Exhibit E. 10/29: James to Luke and Emily, "how this guides our own thinking," and to all, "are we ready to fill this out?"

**What this changes.** One signature with Exhibit E covers eighteen states for three years. Ohio is among them, so Columbus can subscribe rather than negotiate. The states left for separate signatures in the first cohort are California, Arizona, Utah, and any other state not on the list. The NDPA becomes the primary instrument for most districts; Appendix A rides alongside as the supplement, which is what Section 5.2 already says.

**Are we ready to fill it out? Not yet. About two weeks, if four things move this week.** Most of the content exists in these drafts. Two documents do not: the Data Security and Privacy Plan and an accessibility report.

| TEC asks for | Where the answer comes from | Owner | Status |
|---|---|---|---|
| Designated representative (p. 3) | CHSS privacy officer, Appendix A.7 and Exhibit D-3 | Jonah, Demian | Name needed |
| Signature (p. 3) | Authorized signer for the correct legal entity (O8) | Stand counsel | Open |
| Exhibit A, description of services | Draft below; binding scope in six states. Ask TEC what "exclude services" means | Luke drafts, Jonah approves | Draft ready |
| Exhibit B, schedule of student data | Mapped from Exhibit D-1 below; four rows for Emily | Emily | Mostly ready |
| Exhibit D | Leave blank | — | Done |
| Exhibit E, general offer and receiving email | Counsel's yes (O12); a role mailbox for incoming Exhibit Es | Stand counsel, Emily | Open |
| Exhibit F, cybersecurity framework | NIST Cybersecurity Framework recommended; New York requires alignment with it (O20) | Emily | Open |
| Schedule 1, four questions incl. accessibility documentation link | An accessibility conformance report for Navigator (O19) | Emily | **Long pole** |
| Exhibit I, teacher data | Applicable: staff names, work emails, usernames, roles, teacher of record | Emily | Draft below |
| Exhibit K, Data Security and Privacy Plan URL | Drafted on the Privacy plan tab from Appendix A and Attachment 1; needs Emily's confirmation, officer names, and a CHSS URL (O18) | Emily confirms, CHSS hosts | Draft ready |
| Counsel's read | Standard clauses plus all eighteen state Exhibit Gs; not to redline, to know the obligations | Stand counsel | Open |

**Draft Exhibit A.** Written to cover everything CHSS does with student data, because in six of the eighteen states nothing outside Exhibit A is permitted.

> The Center for High School Success (CHSS), a program of Stand for Children Leadership Center, Inc., provides ninth grade success coaching and implementation support to participating high schools. To deliver these services, CHSS receives student data from the LEA's student information system and provides: (1) dashboards that calculate and display ninth grade on-track indicators, course performance, credits, and attendance for the school's ninth grade team, and that continue to follow each ninth grade cohort's progress in later grades; (2) the CHSS Navigator platform, in which school staff and CHSS coaching staff identify students needing support, plan and record interventions, and monitor progress, including software-generated intervention suggestions that educators review before use; (3) administration of the CHSS Belonging and Skills screeners, only with the LEA's approval of the instruments; (4) coaching and professional learning for the ninth grade team; and (5) evaluation of program effectiveness using de-identified and aggregate data. CHSS provides no student-facing accounts other than for screener administration and does not use student data for advertising, marketing, or any activity of an advocacy or political affiliate.

**Exhibit B, mapped from Exhibit D-1.**

- **Check:** student school enrollment; grade level; year of graduation (cohort); student scheduled courses; teacher names (only where teacher of record is provided); student school (daily) and class attendance; student course grades, course data, and grades or performance scores; local ID number; state ID number; student first and last name; student responses to surveys or questionnaires (the screeners).
- **Check, noting "only if the LEA elects to provide":** conduct or behavioral data; gender; ethnicity or race; language information; English language learner information; low-income status; student disability information; specialized education services (IEP or 504).
- **Emily to answer:** IP addresses and cookies (staff users, and students if screeners run in a CHSS tool); metadata on user interaction; provider-assigned student ID (Navigator's internal ID and the de-identification token); student app username and passwords (only if screeners require a student login).
- **Other:** credits attempted and earned; cumulative GPA; enrollment entry and exit dates; summer school enrollment and outcomes; data created in the Service (intervention plans and records, team meeting notes, on-track and risk flags, software-generated suggestions).
- **Leave unchecked:** medical alerts, living situation, transportation, parent or guardian contact, ID, and name, student contact information, student work, online communications, place of birth; date of birth unless a district needs it for matching.

**Exhibit I, teacher data.** Check: teacher app username; local (district) ID where teacher of record is provided; personal email only if staff use a personal address (expect work email instead, listed under Other); application use statistics; IP addresses for staff logins (Emily). Other: work email, role, school assignment.

**How it guides our thinking.** Six points for James and Emily.

1. **Exhibit A is the contract's scope in strict states.** Screeners, intervention suggestions, and cohort follow-up are written into it for that reason.
2. **Version 1.0 settles the version question:** a fixed three-year term, which is the review cycle Jonah wanted.
3. **Background checks become contractual** for any CHSS employee with direct contact with students. Coaches in classrooms or administering screeners likely count (O5).
4. **The audit right is real.** Each subscribing district may audit once a year; New York can require an independent audit at CHSS's expense. Appendix A.13 now says the NDPA's audit clause governs where it is signed.
5. **Deletion and de-identified evaluation already fit.** Sixty days satisfies the standard clause and New York's ninety; the de-identified carve-out is in the standard clause itself.
6. **Three builds follow:** the Data Security and Privacy Plan (O18, now drafted on the Privacy plan tab), an accessibility conformance report (O19), and an Exhibit F framework CHSS can truthfully claim alignment with, with New Hampshire's control list or a certification behind it (O20).

:::details Paste-ready reply for James to TEC
> Thank you for sending this and for the clear instructions. We are reviewing the agreement with our counsel and our technology office and expect to return it completed within two to three weeks. One question on Exhibit A: should we describe the services the agreement covers, list services excluded from coverage, or both?
:::

:::details Paste-ready email to Jonah and Emily: the TEC agreement and what we need
> Subject: TEC's 18-state NDPA: what it means and what we need this week
>
> Jonah, Emily,
>
> TEC sent the multi-state NDPA this morning, with Lewis County as the originating district. It covers eighteen states, including Ohio, New York, Massachusetts, Illinois, and Missouri. We sign once with Exhibit E; any district in those states then subscribes without a new negotiation. Columbus can come in through Ohio.
>
> We are about two weeks from returning it. Most answers are already in our drafts; the full checklist is on the Notes tab of the drafts site. What I need this week:
>
> 1. The signer and legal entity (Stand for Children Leadership Center, Inc.?), and a named privacy officer as designated representative.
> 2. Counsel to read the standard clauses and the eighteen state exhibits. They cannot be redlined; the read is to know what we are agreeing to.
> 3. Emily: the cybersecurity framework we align with (I recommend NIST CSF; New York requires it), the accessibility documentation for Navigator, four Exhibit B items, the teacher-data exhibit, and a privacy@ mailbox for incoming Exhibit Es.
> 4. A go-ahead for me to draft our Data Security and Privacy Plan from the appendix and system specifications, for Emily to confirm and us to post at a CHSS URL. New York requires it, and it is the longest pole.
>
> Two consequences worth knowing now: in six of these states we may use data only for the services we list in Exhibit A, so the description has to be complete (draft on the Notes tab); and six states require background checks for staff with direct student contact, which likely includes coaches.
>
> Luke
:::

:::details Earlier research: SDPC structure, membership, and versions
### How the consortium works
::src SDPC NDPA :: The Student Data Privacy Consortium (SDPC) is a special interest group of the Access 4 Learning (A4L) Community. Its NDPA is published in state and multi-state versions through alliances; signed agreements and their Exhibit Es are posted in the SDPC Resource Registry. Version 1 agreements carry a fixed three-year term; version 2 (2024) is in use in some states (Utah's current form is UT-NDPA-V2.1). Vendor membership in A4L is annual, priced on revenue, and gives Registry access and a Signatory Badge; it is not required to sign.
::src af-dpa :: Registry rows are created by districts; the originating district uploads the signed agreement and a standalone Exhibit E; Registry search is members-only; a subscribing district accepts Exhibit E and must deliver notice of acceptance; cross-state acceptance is not valid; a vendor-modified agreement cannot carry Exhibit E.

**There is no application.** A district or its consortium sends the provider its form; the provider signs; the district posts it. Turnaround is the district's routing, not the consortium's.

**Outside the TEC group**, expect separate signatures as the first district in each state arrives: California (CA-NDPA via the California Student Privacy Alliance hosted by CITE, with its own Exhibit G), Arizona (AZ-NDPA v1.2 with Exhibit G and the AI questionnaire), Utah (UT-NDPA v2.1), and others. Each signature with Exhibit E covers the rest of that state.

**Join A4L as a vendor member** so Emily can see the Registry and track Exhibit E subscriptions. Optional, but it is how CHSS will know who has subscribed.

**Links:** SDPC home https://privacy.a4l.org/ · alliance list https://sdpc.a4l.org/search_alliance.php · Arizona NDPA v1 specimen https://sdpc.a4l.org/agreements/AZ-NDPA-V1withExhibit%20E.pdf · Missouri NDPA v1 https://sdpc.a4l.org/agreements/MO_NDPA_V1_no_exhibit.pdf · version 2 usage guide https://files.a4l.org/privacy/NDPA/NDPAv2_Usage_Guide_and_Development_Process.pdf · vendor membership https://privacy.a4l.org/get-involved/
:::

## For counsel: everything CHSS agrees to by signing
::src Conversation :: Luke to James (10/29): the agreement contains things CHSS commits to, "different specific security protocols," background checks, and more, which "needs to be reviewed by legal and by Emily"; "it's just my job to make sure that those action points are directly in front of the people that need to review them."
::src Drafting choice :: Every obligation CHSS takes on in the Agreement, Appendix A, and the TEC multi-state NDPA, in one list, each with the clause it comes from and whether it is pending. Emily's technical obligations are itemized in the gap table above; this list is the legal view.

Read this with the Agreement tab open. Items marked **pending** have a highlighted placeholder in the Agreement.

| # | CHSS agrees to | Where | Status |
|---|---|---|---|
| L1 | Act as a FERPA school official under each district's direct control; no redisclosure except as permitted | 5.1; A.2; NDPA Art. I.1 | Drafted |
| L2 | Use Student Data only for the listed Services; no sale, rent, advertising, profiling, or use by any advocacy, lobbying, political, or fundraising affiliate; no sharing with partners, evaluators, or funders without district approval | 5.5; A.4; NDPA Exhibit A in six states | Drafted |
| L3 | Sign each state's NDPA unmodified, starting with TEC's 18-state agreement, and offer Exhibit E; the NDPA controls where signed | 5.2; A.18; A.19 | **Pending** (O12) |
| L4 | Comply with each state's student privacy law "as if CHSS were the District": Ohio R.C. 3319.32x and 1347; California Ed. Code 49073.1's nine terms; Arizona Exhibit G and A.R.S. 15-104 and 15-117; New York Education Law 2-d and Part 121; the other TEC state exhibits | A.2; A.17; NDPA Exhibit G | Drafted; counsel reads the 18 exhibits |
| L5 | Notify the district within 72 hours of confirming any unauthorized access; let the district control family notice; pay notification, credit monitoring, forensic, legal, and regulatory costs attributable to CHSS | A.8 | Drafted; cost exposure depends on L13 |
| L6 | Return or destroy identifiable data within 60 days of a directive or of termination; backups expire within 90 days; officer certifies destruction and non-retention | 5.6; A.10; Exhibit D-4 | Drafted; runbook **pending** (O13) |
| L7 | Keep only de-identified and aggregate data after termination, with a documented de-identification review; no re-identification; district consent before any transfer or any publication naming the district | 5.5; A.10; NDPA Art. IV.5 | Drafted; need **pending** (O10) |
| L8 | Carry cyber liability of $2,000,000 per claim and aggregate with a two-year tail, CGL $1M/$2M, and E&O $1M; self-insurance only if the district accepts it | A.14; Section Eight | **Pending** (O7) |
| L9 | Allow each district an annual audit on ten business days' notice; in New York, an independent audit at CHSS's expense if the State Chief Privacy Officer requires one | A.13; NDPA Art. V.2; NY Exhibit G | Drafted |
| L10 | Accept a district's immediate suspension of data transfers; termination for incurable or repeated breach; termination without penalty if the Services cannot lawfully continue; remedies when a subprocessor objection is unresolved | A.6; A.16 | Drafted |
| L11 | No automatic renewal of the data provisions | Section Two; A.16 | Drafted |
| L12 | Background checks and annual privacy training for every person with access; in six TEC states, background checks for every employee with direct contact with students | A.7; NDPA Exhibit G | **Pending** (O5) |
| L13 | Breach costs and confidentiality carved out of Section Eight's liability cap, or a stated super-cap | Section Eight | **Pending** (O2) |
| L14 | Collect screener responses only after district authorization and certified consent | 6.7; A.15 | Instruments **pending** (O6) |
| L15 | No training of any model on district data; AI outputs about a student are Student Data; disclose the model provider and demonstrate the platform on request | A.12 | Provider **pending** (O3) |
| L16 | Support parent and eligible-student requests within ten business days through the district | A.11 | Drafted |
| L17 | Name a Privacy Officer and Security Officer; publish a Data Security and Privacy Plan at a CHSS URL | A.7; NY Exhibit K | **Pending** (O8, O18) |
| L18 | Provide executed copies and a 90-day expiration notice | 5.7 | Drafted |
| L19 | Store and process data only in the United States | A.9 | Regions **pending** (O14) |
| L20 | Governing law and venue of the district's state and county | A.17; NDPA Art. VII.6 | Drafted |

## For Jonah: decisions and commitments
::src Conversation :: Jonah (10/26) listed the standard terms to include: deletion on termination, storage location, audits, insurance levels. The items below are the ones that go beyond that list or cost money.

1. **Liability carve-out.** Section Eight caps liability at insurance proceeds and disclaims consequential damages. Appendix A promises breach costs. Decide whether breach costs, confidentiality, and privacy indemnity sit outside the cap or under a super-cap. (O2)
2. **The December pilot and the August 2027 start.** Confirm that the January cohort commits to readiness in Year 0 and live data in Year 1, and that the pilot is existing partners on existing agreements. (O1)
3. **Integration support through acceptance,** not two sessions. It is the honest version of the "support you to do something" offer, and it is a cost line. (O11)
4. **Signing any state NDPA and Exhibit E** as a standing commitment. (O12)
5. **Coaching-staff access** was decided on 10/27: standing access to the school's students, bound to screening and intervention purposes, no platform-login language. Emily's bullets refining the school-level binding are the only open piece. (M1, O17)
6. **Row-level de-identified retention** for the longitudinal work, with the review process that goes with it. (O10)
7. **One cadence rule for Year 1.** Weekly once live; Tier 2 districts on a dated interim cadence not less than monthly. Confirm CHSS will hold that line, or the Friday-to-Tuesday promise comes out of the case. (O15)

**A note, not a decision: vendor and API fees.** Under Tier 3 a SIS vendor may charge for an API or a scheduled export. The agreement is silent on who pays. The case-making says "$0 due to CHSS," which stays true either way, but a district procurement office will ask. Decide whether CHSS absorbs those fees, the district does, or Tier 3 is offered only where the vendor charges nothing, and we will add one sentence to 6.5.

## For Demian and counsel: people, money, entity
::src District lens :: "If the appendix says every person with access passes a background check and completes annual training, show me the policy and the roster."

1. Every person with access to Student Data, coaches included, passes a background check before access and completes privacy and security training at hire and annually. True today, or by when? (A.7, O5) This is now contractual in six TEC states for any employee with direct contact with students.
2. Cyber liability: current limit, aggregate, and whether a two-year tail is available. Drafted at $2,000,000. CGL $1,000,000 / $2,000,000 and E&O $1,000,000. (A.14, O7)
3. Stand for Children Leadership Center, Inc. is the correct 501(c)(3) signatory, and the no-advocacy clause in A.4(d) is acceptable as written. (O8)
4. Stand will sign the NDPA's standard clauses without redline, in any state. (O12)
5. The Section Eight liability language and the Appendix A promises are reconciled before Columbus sees the package. (O2)
6. Name CHSS's privacy officer and security officer. California law requires the contract to designate responsible individuals, and Exhibit D-3 now has two lines for them. Emily is the obvious security officer; the privacy officer can be Emily, Demian, or counsel, but it has to be a person. (A.7)

## For Tara: screeners and the evaluation design
::src State law :: Arizona A.R.S. § 15-104 (written parental consent for mental health screening); Department of Education letter of August 26, 2026 on behavioral health screeners.

1. The full text of the Belonging Screener and the Skills Screener, versioned, so counsel can classify each item against PPRA's protected areas and § 15-104. (O6)
2. Whether coaches can do the job with in-session view only, or need a standing login. (M1)
3. Which longitudinal analyses need row-level de-identified records rather than aggregate results. (O10)
4. Whether any Navigator feature depends on discipline data. (M3)
5. Arizona: a belonging screener with items about emotional state or well-being may not be administrable in Arizona at all (Arizona districts cannot run Panorama or ask students how they feel), while California districts run such surveys several times a year. Plan for the Services to run without the Belonging Screener where a district declines it. (6.7)

## For James: collateral and the current emails
::src James's collateral :: The Navigator one-pager says CHSS coaches and staff see "aggregate data only."

1. Change the one-pager's "Who sees what" row to match the 10/27 decision: CHSS coaching staff assigned to a school see that school's student-level records, for screening and intervention work with the team only, with every access logged and the district able to limit it. "Aggregate data only" is no longer accurate.
2. Replace "no emails, no manual pulls, no file transfers" with "no manual file handling once your automated feed is running."
3. **The 70 percent Kid Talk claim** (your 10/23 email: "when teams do a Kid Talk with fidelity they are 70%+ more likely to hit their on-track goal"). Before it appears in anything a board sees: what is the comparison group, how many schools, which years, and how was fidelity measured? Is it a correlation or a controlled result? Until then the case-making says "associated with" and cites "CHSS partner data," and the number carries a footnote with the method. (O16)
4. Hold the Missouri reply until counsel confirms O12; if it goes sooner, drop the Exhibit E sentence.
5. Ask Columbus for a 45-minute slot Nov 2 to 4 with the CTO and their data-agreement reviewer; send the data summary, the file specification outline, the security page, and the screener instruments ahead of it. New: Ohio is one of the eighteen states in TEC's multi-state NDPA. Ask whether Columbus will subscribe through Exhibit E once CHSS has signed with Lewis County, in place of or alongside its own Student Data Sharing Agreement.
6. Ask San Diego which instrument they use with outside partners that receive student-level data, without guessing the answer. Ask specifically whether SDUSD routes partner data agreements through CITE's data privacy services (CITE, California IT in Education, hosts the California Student Privacy Alliance and the California NDPA; many California districts outsource redlining to it), and expect purchasing and business services to review the MOU alongside the CTO. A California district lead's advice for a partner with its own strong appendix: expect to be asked to sign the state agreement too, and say yes.

:::details Paste-ready email blocks for James
### Reply to the Missouri district's technology coordinator
::src Lewis County :: Her 10/26 email asked whether "support student success and timely interventions, not to conduct research" is correct.
::src FERPA :: "Interventions" means the school official exception; "research" would push her consortium toward the studies exception and a different agreement.

> Thank you for getting this started, and for the clear summary. Your description is correct: the Center for High School Success uses information from your SIS to build the ninth grade dashboards your team and our coach use to identify students who need support and to act on it quickly. That is the purpose, and we operate as a school official under FERPA to deliver it.
>
> One clarification so there are no surprises: like most programs, we evaluate whether our work is helping. We do that with de-identified and aggregate results only (for example, your school's on-track rate), never with identifiable student records, and we delete identifiable data when our partnership ends or whenever you ask.
>
> We are glad to work through TEC and the SDPC process. We will sign the Missouri NDPA. [Pending counsel: and we expect to have a general offer of terms on file so other Missouri districts can use the same agreement.] When TEC reaches out, please have them contact Emily Phan, our Executive Technology Officer, who is copied here. Luke Allpress, who is helping us with agreement language and SIS integration, is also copied.
>
> We will send you a short summary of exactly what data we ask for and how it moves before anyone has to review a document.

### The one-paragraph data summary for any district
::src James's collateral :: Mirrors "Only the data needed" and "Who sees what," with discipline optional, the screeners named, and Option B stated accurately.

> Here is what the integration involves, in plain terms. Your district sends us a file for each ninth grade cohort with student ID, name, grade level and enrollment dates, course enrollments, course marks and credits by grading period, GPA, and attendance. The goal is an automated weekly export to our secure SFTP, which we set up with your data team; if that is not possible yet, a scheduled upload on an agreed interim cadence works while we help you automate it. Your school team sees student-level dashboards with names. The coach assigned to your school sees that school's students too, only for the screening and intervention work with your team, with every access logged, and you can limit that at any time. Our program and research staff never see identifiable data. We also administer short belonging and skills screeners through your team, after you have reviewed and approved the questions and certified that any parent notice or consent your policy and state law require is in place. Identifiable data is deleted when the partnership ends or whenever you ask; we keep only de-identified and aggregate results to evaluate the program. The full terms are in our data privacy appendix, and we will also sign your state's NDPA if you prefer.

### Asks for the Columbus City CTO review
::src Columbus City DSA :: Their Student Data Sharing Agreement (revised 3/17/2025) is the strictest document in hand.

1. Forty-five minutes with the CTO and whoever reviews data agreements, between Nov 2 and Nov 4, with Luke on the call.
2. Confirmation that the 3/17/2025 agreement is the current form, and whether the district would also accept the Ohio NDPA.
3. Their read, before the call, on coach access (Option A versus B) and on CHSS keeping de-identified results after termination.
4. Anything the district requires of CHSS coaches beyond the agreement (background checks, onboarding, training).
5. The board timeline from "agreement final" to "approved."
6. Send ahead: the data summary, the file specification outline, the security page, and the screener instruments.

### Asks for San Diego
::src San Diego CCAP :: The document in hand is a dual-enrollment agreement, not a student data privacy agreement.

1. Which agreement SDUSD uses with outside partners that receive student-level data.
2. Who signs it, and whether the General Services Agreement and SOW format will be required.
3. The same two substantive points as Columbus.

### Two sentences for the superintendent-level emails

> Because the accelerator includes SIS integration, we will ask you within the first two weeks to name a technical contact and a data privacy contact, and we will schedule a short onboarding call with both before any data moves. We will sign your state's National Data Privacy Agreement or provide our own privacy appendix written to the same standard, whichever your district prefers. Data for your ninth grade cohort begins flowing in August 2027; the months before that are for getting the feed and the agreement in place.
:::
