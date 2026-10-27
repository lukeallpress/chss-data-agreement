# Notes
::src Drafting choice :: Working page for the CHSS team. First, every claim the drafts make on CHSS's behalf that someone at CHSS has to confirm, grouped by who confirms it. Then the paste-ready email blocks for James, collapsed.
::src Conversation :: Jonah (10/26): "this is our commitment ... this is our technical deliverable." Emily: "I would like to at least review and be involved in what you wrote." The claims below are exactly what that review is for.

The drafts describe CHSS as it needs to be, not necessarily as it is today. Each line below is a statement a district will test. Confirm it, date it, or strike it before the package leaves the building.

## For Emily: the gap analysis
::src Conversation :: Emily (10/27): "I want to see the gap of whether or not we have it today ... check, check, check, or okay, we need to tighten this up." Her example: a district requires 45-day retention and the platform does 30. She asked for the requirements that imply a policy, the measures each policy implies, and the technical items that must be in place, separate from the agreement text.
::src Drafting choice :: The table lists the requirements that recur across the NDPA, the Columbus City agreement, California Education Code § 49073.1, and Appendix A, each with the measure it implies and a blank for CHSS's current state. Fill the last three columns; anything marked "gap" becomes a dated commitment in Part C.

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

## For Emily: technical claims to confirm
::src Emily's architecture :: Every platform fact in Appendix A and Part C is drawn from the CHSS Data Platform diagram and the 10/26 call; none has been verified against a live tenant.
::src District lens :: A CTO will ask for evidence of each present-tense control; a privacy officer will not accept a blank where the model provider belongs.

Answer each as **true today**, **true by [date]**, or **no**:

1. Microsoft Azure / Fabric, Salesforce Experience Cloud and CRM Analytics, and Power BI are the complete subprocessor list for Student Data, and every tenant is in a U.S. region. (A.6, A.9)
2. The AI model provider: name, product tier or API, the data-use terms by URL and date, country of processing, and whether a zero-retention arrangement is enabled. (A.6, A.12)
3. No Student Data, de-identified data, or outputs are used to train or fine-tune any model, by CHSS or any subprocessor, and the provider will attest to that in writing on request. (A.12)
4. Access to student-level records is logged (user, time, record), logs are tamper-protected and kept twelve months, and a per-district export is possible. (A.7)
5. MFA on every CHSS staff and administrator account; SSO (SAML or OIDC) available to district users. (A.7, Part C)
6. Encryption in transit TLS 1.2 or higher and at rest AES-256 across the data lake, warehouse, Salesforce, Power BI, backups, and the SFTP landing zone. (A.7)
7. Critical security patches within seven days; anti-malware on all endpoints with access; firewall and network segregation of production; encrypted, tested backups. (A.7)
8. A documented access roster reviewed quarterly, with deprovisioning within one business day. (A.7)
9. A written, tested incident response plan that can meet seventy-two-hour district notification. (A.8)
10. Independent security assessment (SOC 2 Type II or equivalent) and annual penetration test: current status and the earliest honest completion date. (A.7, A.13, Part C)
11. A deletion runbook that returns or destroys a district's data within sixty days across every store, with backups expiring on a rotation of ninety days or less and never restored to production, and a certificate template. (5.6, A.10)
12. The de-identification step produces a random token not derived from any student identifier, with the key destroyed alongside identifiable data. (A.10)
13. Deterministic matching on district or state ID is the rule; probabilistic matching only flags duplicates for human review. (6.4, Part C)
14. Cell suppression below ten in every aggregate output and dashboard. (A.10)
15. Whether a Navigator tenant can run without student names, and which features would be off. (O9)
16. The December pilot: which schools, under which agreement, with what data. (O1)
17. Integration support: what "support until the feed passes acceptance" costs in staff time, and who staffs it. (6.9, O11)
18. Be ready to demo Navigator to a district's technology or privacy lead and answer the four questions they ask of any AI feature: is the model CHSS's own or a third party's; exactly what goes into the prompt; who at CHSS, the provider, or any maintenance contractor can see inputs and outputs; and what the agent does with the output. (A.12(i); a California district lead asks exactly these and says vendors are often surprised to be asked.)
19. Part C is written in the present tense. Besides the two visible brackets (`[AI model provider]` and the first assessment date), the following are also claims that may need re-tensing or a bracket until confirmed: U.S.-only processing for every tenant, record-level access logging, seven-day patching, the deletion runbook, the personnel practice in A.7, and the insurance limits. Mark each one.

## The NDPA: what CHSS signs, in what order
::src Conversation :: 10/27 call. Jonah: "point us to the shortest distance ... how many of these places we have to apply to." Emily: what is the turnaround for a vendor "application," and does the national consortium give a bigger umbrella than the states? Jonah and Emily agreed to prepare to sign version 1 with Exhibit E.
::src SDPC NDPA :: The Student Data Privacy Consortium (SDPC) is a special interest group of the Access 4 Learning (A4L) Community. Its National Data Privacy Agreement (NDPA) is published in state versions through state alliances; signed agreements and their Exhibit Es are posted in the SDPC Resource Registry. Version 1 state agreements (Arizona, Missouri, Florida, Illinois, Ohio, Oregon, Washington, Tennessee, and others) carry a fixed three-year term, and Exhibit E expires three years from the original signature; version 2 (2024) is in use in some states (Utah's current form is UT-NDPA-V2.1) and remains in effect while the provider holds data. Vendor membership in the A4L Community is annual, priced on gross revenue, and gives Registry access and a "Signatory Badge" for unmodified NDPAs; it is not required to sign.
::src af-dpa :: knowledge/sdpc/registry-and-membership-2026-10-26.md and exhibit-e-general-offer.md: "you do not have to be a member of the Community to sign the NDPA," but "at least one signing party must be a member"; Registry rows are created by districts; the originating district uploads the signed agreement and a standalone Exhibit E; Registry search is members-only since 2022; a subscribing district accepts Exhibit E through the Registry's "Auto Exhibit E Creator" or by signing the PDF and must deliver notice of acceptance; cross-state acceptance is not valid; a vendor-modified originating agreement is not usable for Exhibit E.
::src District lens :: A Missouri partner district's technology coordinator has already routed CHSS through its consortium (TEC via MOREnet). A California district privacy lead (10/27) outsources negotiation to CITE, which hosts the California alliance.

**There is no application.** A provider does not apply to the SDPC or to a state alliance. A district starts it: the district (or its consortium, as Lewis County's did) asks the provider to sign the state's NDPA. The provider signs; the district uploads the signed agreement and, if the provider signed it, a standalone Exhibit E to the Registry. That row is what every other district in the state sees. Turnaround is therefore the district's, not the consortium's: a willing provider can sign the same day it receives the form; the slow part is the district's own routing and, where required, its board.

**The shortest path, in order.**

1. **Counsel reads the standard clauses once.** Start with the national NDPA Standard Version 1 and one state version (Arizona v1.2 is a good specimen, since it carries an AI questionnaire; Missouri's is the one arriving first). The standard clauses cannot be redlined; the only CHSS-specific content is Exhibit A (services), Exhibit B (data elements, which Exhibit D-1 of the Agreement already answers), the subprocessor list, and Exhibit E. Decide now that CHSS will sign unmodified; a vendor-modified agreement cannot carry Exhibit E for other districts.
2. **Sign Missouri first, with Exhibit E, when TEC sends it.** That is already in motion. Ask TEC to upload the standalone Exhibit E alongside the agreement so the row is usable by every other Missouri district.
3. **Then one signature per state as the first district in each state arrives:** Ohio for Columbus, California for San Diego, and so on. Each signature with Exhibit E covers the rest of that state for three years. Expect about ten states for the January cohort plus the existing partners, so about ten signatures, not seventy-five.
4. **Join A4L as a vendor member** (annual, revenue-based dues) so Emily can see the Registry, see which districts have subscribed, and manage Exhibit E acceptances. Not required to sign, but it is how CHSS will know who has piggybacked. Fill in the Registry profile once with the subprocessor list and the data elements.
5. **Prefer version 1 where the state offers it,** for the three-year review cycle Jonah wants; sign version 2 where that is what the state alliance uses (Utah, for example). The Appendix A terms were drafted to sit alongside either.

**What the national consortium does and does not give you.** The national agreement is the template; every state alliance publishes its own version because state law requires it, and the state version is what a district signs. There is no single national signature that covers all states. The umbrella is the Registry and the shared standard clauses, which is why one unmodified signature per state is enough.

**Which versions are in play for the first cohort** (confirm each on the SDPC alliance page before signing): Arizona, AZ-NDPA v1.2 with Exhibit G; California, CA-NDPA (currently v1.x via the California Student Privacy Alliance hosted by CITE) with California's Exhibit G; Ohio, OH-NDPA v1 with Exhibit E; Missouri, MO-NDPA v1 (TEC and MOREnet); Massachusetts, MA-NDPA (The Education Cooperative); Utah, UT-NDPA v2.1.

**Realistic timeline.** Counsel's read of the standard clauses: a week. Missouri signature: the day TEC sends it. Each later state: as fast as the first district routes it, typically two to six weeks including a board where one is required. Registry membership: an online form and an invoice.

:::details Paste-ready email to Jonah and Emily with the NDPA links
> Subject: NDPA packet: what to read, what to sign first
>
> Jonah, Emily,
>
> Here is the shortest path through the Student Data Privacy Consortium, as promised.
>
> There is no application. A district (or its consortium) sends us its state's NDPA; we sign; the district posts it to the SDPC Registry, and every other district in that state can then subscribe to the same terms by accepting our Exhibit E. One unmodified signature per state covers that state for three years. For the first cohort that is roughly ten signatures.
>
> To read now: the national Standard Version 1 and the Arizona version 1.2 (a representative state version, with its AI questionnaire). The standard clauses are not negotiable; the only parts we fill in are the services description, the data elements, the subprocessor list, and Exhibit E. Our own appendix was written to sit alongside either version.
>
> - SDPC home and alliance list: https://privacy.a4l.org/ and https://sdpc.a4l.org/search_alliance.php
> - Arizona NDPA v1.2 with Exhibit E (specimen): https://sdpc.a4l.org/agreements/AZ-NDPA-V1withExhibit%20E.pdf
> - Missouri NDPA v1 (the one arriving first): https://sdpc.a4l.org/agreements/MO_NDPA_V1_no_exhibit.pdf
> - Version 2 usage guide, for states that use it: https://files.a4l.org/privacy/NDPA/NDPAv2_Usage_Guide_and_Development_Process.pdf
> - Vendor membership (optional, gives Registry access and the signatory badge): https://privacy.a4l.org/get-involved/
>
> Order of operations: counsel reads the standard clauses once (a week); we sign Missouri with Exhibit E the day TEC sends it; then Ohio when Columbus is ready and California for San Diego; Emily joins A4L as a vendor member so she can see who subscribes. Decision needed from you: that we will sign unmodified, with Exhibit E, in every state. A modified agreement cannot be extended to other districts.
>
> Luke
:::

## For Jonah: decisions and commitments
::src Conversation :: Jonah (10/26) listed the standard terms to include: deletion on termination, storage location, audits, insurance levels. The items below are the ones that go beyond that list or cost money.

1. **Liability carve-out.** Section Eight caps liability at insurance proceeds and disclaims consequential damages. Appendix A promises breach costs. Decide whether breach costs, confidentiality, and privacy indemnity sit outside the cap or under a super-cap. (O2)
2. **The December pilot and the August 2027 start.** Confirm that the January cohort commits to readiness in Year 0 and live data in Year 1, and that the pilot is existing partners on existing agreements. (O1)
3. **Integration support through acceptance,** not two sessions. It is the honest version of the "support you to do something" offer, and it is a cost line. (O11)
4. **Signing any state NDPA and Exhibit E** as a standing commitment. (O12)
5. **Option B as default** (in-session view) with Option A on district election, or the reverse after Tara weighs in. (M1)
6. **Row-level de-identified retention** for the longitudinal work, with the review process that goes with it. (O10)
7. **One cadence rule for Year 1.** Weekly once live; Tier 2 districts on a dated interim cadence not less than monthly. Confirm CHSS will hold that line, or the Friday-to-Tuesday promise comes out of the case. (O15)

**A note, not a decision: vendor and API fees.** Under Tier 3 a SIS vendor may charge for an API or a scheduled export. The agreement is silent on who pays. The case-making says "$0 due to CHSS," which stays true either way, but a district procurement office will ask. Decide whether CHSS absorbs those fees, the district does, or Tier 3 is offered only where the vendor charges nothing, and we will add one sentence to 6.5.

## For Demian and counsel: people, money, entity
::src District lens :: "If the appendix says every person with access passes a background check and completes annual training, show me the policy and the roster."

1. Every person with access to Student Data, coaches included, passes a background check before access and completes privacy and security training at hire and annually. True today, or by when? (A.7, O5)
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
5. Ask Columbus for a 45-minute slot Nov 2 to 4 with the CTO and their data-agreement reviewer; send the data summary, the file specification outline, the security page, and the screener instruments ahead of it.
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
