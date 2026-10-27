# Notes
::src Drafting choice :: Working page for the CHSS team. First, every claim the drafts make on CHSS's behalf that someone at CHSS has to confirm, grouped by who confirms it. Then the paste-ready email blocks for James, collapsed.
::src Conversation :: Jonah (10/26): "this is our commitment ... this is our technical deliverable." Emily: "I would like to at least review and be involved in what you wrote." The claims below are exactly what that review is for.

The drafts describe CHSS as it needs to be, not necessarily as it is today. Each line below is a statement a district will test. Confirm it, date it, or strike it before the package leaves the building.

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

## For Tara: screeners and the evaluation design
::src State law :: Arizona A.R.S. § 15-104 (written parental consent for mental health screening); Department of Education letter of August 26, 2026 on behavioral health screeners.

1. The full text of the Belonging Screener and the Skills Screener, versioned, so counsel can classify each item against PPRA's protected areas and § 15-104. (O6)
2. Whether coaches can do the job with in-session view only, or need a standing login. (M1)
3. Which longitudinal analyses need row-level de-identified records rather than aggregate results. (O10)
4. Whether any Navigator feature depends on discipline data. (M3)
5. Arizona: a belonging screener with items about emotional state or well-being may not be administrable in Arizona at all (Arizona districts cannot run Panorama or ask students how they feel), while California districts run such surveys several times a year. Plan for the Services to run without the Belonging Screener where a district declines it. (6.7)

## For James: collateral and the current emails
::src James's collateral :: The Navigator one-pager says CHSS coaches and staff see "aggregate data only."

1. Change the one-pager's "Who sees what" row to match Option B as now defined: coaches hold no standing login and see student-level data only alongside your team. "Aggregate data only" is no longer accurate.
2. Replace "no emails, no manual pulls, no file transfers" with "no manual file handling once your automated feed is running."
3. **The 70 percent Kid Talk claim** (your 10/23 email: "when teams do a Kid Talk with fidelity they are 70%+ more likely to hit their on-track goal"). Before it appears in anything a board sees: what is the comparison group, how many schools, which years, and how was fidelity measured? Is it a correlation or a controlled result? Until then the case-making says "associated with" and cites "CHSS partner data," and the number carries a footnote with the method. (O16)
4. Hold the Missouri reply until counsel confirms O12; if it goes sooner, drop the Exhibit E sentence.
5. Ask Columbus for a 45-minute slot Nov 2 to 4 with the CTO and their data-agreement reviewer; send the data summary, the file specification outline, the security page, and the screener instruments ahead of it.
6. Ask San Diego which instrument they use with outside partners that receive student-level data, without guessing the answer. Ask specifically whether SDUSD routes partner data agreements through CITE's data privacy services (CITE, California IT in Education, hosts the California Student Privacy Alliance and the California NDPA; many California districts outsource redlining to it), and expect purchasing and business services to review the MOU alongside the CTO. A California district lead's advice for a partner with its own strong appendix: expect to be asked to sign the state agreement too, and say yes.

:::details Paste-ready email blocks for James
### Reply to the Missouri district's technology coordinator
::src Lewis County :: Her 10/26 email asked whether "support student success and timely interventions, not to conduct research" is correct.
::src FERPA :: "Interventions" means the school official exception; "research" would push her consortium toward the studies exception and a different agreement.

> Thank you for getting this started, and for the clear summary. Your description is correct: the Center for High School Success uses information from your SIS to build the ninth grade dashboards your team uses, with our coach alongside, to identify students who need support and to act on it quickly. That is the purpose, and we operate as a school official under FERPA to deliver it.
>
> One clarification so there are no surprises: like most programs, we evaluate whether our work is helping. We do that with de-identified and aggregate results only (for example, your school's on-track rate), never with identifiable student records, and we delete identifiable data when our partnership ends or whenever you ask.
>
> We are glad to work through TEC and the SDPC process. We will sign the Missouri NDPA. [Pending counsel: and we expect to have a general offer of terms on file so other Missouri districts can use the same agreement.] When TEC reaches out, please have them contact Emily Phan, our Executive Technology Officer, who is copied here. Luke Allpress, who is helping us with agreement language and SIS integration, is also copied.
>
> We will send you a short summary of exactly what data we ask for and how it moves before anyone has to review a document.

### The one-paragraph data summary for any district
::src James's collateral :: Mirrors "Only the data needed" and "Who sees what," with discipline optional, the screeners named, and Option B stated accurately.

> Here is what the integration involves, in plain terms. Your district sends us a file for each ninth grade cohort with student ID, name, grade level and enrollment dates, course enrollments, course marks and credits by grading period, GPA, and attendance. The goal is an automated weekly export to our secure SFTP, which we set up with your data team; if that is not possible yet, a scheduled upload on an agreed interim cadence works while we help you automate it. Your school team sees student-level dashboards with names. Our coach has no login of their own and sees student-level data only in sessions with your team lead, unless you choose to give them more. Our program and research staff never see identifiable data. We also administer short belonging and skills screeners through your team, after you have reviewed and approved the questions and certified that any parent notice or consent your policy and state law require is in place. Identifiable data is deleted when the partnership ends or whenever you ask; we keep only de-identified and aggregate results to evaluate the program. The full terms are in our data privacy appendix, and we will also sign your state's NDPA if you prefer.

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
