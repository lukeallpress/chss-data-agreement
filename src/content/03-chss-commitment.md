# CHSS Commitment to Student Data Privacy and Security
::src Conversation :: Jonah (10/26): the second deliverable is "our commitment to data privacy and security" plus "a system specifications document ... based on the required specifications by the districts that we're trying to contract with," set so CHSS is "compliant no matter what a district asks." James (10/23): a "system improvement plan" of what CHSS must build to meet district agreements.
::src Drafting choice :: Three parts: a short NDPA posture statement for districts that use the national agreement; Appendix A, CHSS's own terms, mapped to the NDPA's structure and set at the Columbus City Schools bar; and a one-page system specification a district CTO can read in five minutes.

This commitment has three parts. Part A states how CHSS will work with the National Data Privacy Agreement. Part B is Appendix A, CHSS's own privacy and security terms, which apply where a district does not use the NDPA and which track its structure. Part C is the system specification a district's technology office reads before signing.

## Part A: NDPA posture statement
::src Lewis County :: A Missouri partner district's technology coordinator wrote on 10/26 that she had asked her consortium (TEC via MOREnet) and the SDPC Resource Registry to obtain an NDPA with CHSS. The NDPA will arrive whether or not CHSS writes its own appendix.
::src SDPC NDPA :: Exhibit E (General Offer of Privacy Terms) lets a provider extend an agreement it has signed with one LEA to any other LEA in the same state that subscribes; the subscribing LEA signs Exhibit E rather than negotiating anew.
::src Luke's experience :: AFUHSD extends other districts' signed NDPAs to itself through Exhibit E routinely; each vendor file holds "the DPA from another district, and then the Exhibit E attachment signed by either me or Lauren."
::src Drafting choice :: Naming the Provider, the Service, and Provider staff up front answers the first three questions a consortium reviewer asks and settles that coaches are inside the agreement.
::src af-dpa :: knowledge/sdpc/exhibit-e-general-offer.md and resource-registry.md (captured 2026-10-26): Exhibit E is "a one-signature piggyback" that extends only privacy terms, within one state, for three years from the provider's signature; a subscribing district "must deliver notice of acceptance." Registry rows are created by districts, not providers ("One row = one district + one resource"), and the originating district uploads "the signed agreement file and a standalone Exhibit E file." So CHSS's job is to sign promptly and hand the first district in each state a clean standalone Exhibit E, not to "list itself."
::src af-dpa :: knowledge/sdpc/ndpa-structure.md: the v1.2 "Provider" definition is "provider of digital educational software or services ... for the digital storage, management, and retrieval of Student Data," a strained fit for a coaching nonprofit; the school-official recital in Article I is the real footing, which is why Section 5.1 of the Agreement states it independently.

The Center for High School Success (CHSS), a program of Stand for Children Leadership Center, Inc., will execute the Student Data Privacy Consortium's National Data Privacy Agreement (NDPA), including any state-specific version and exhibits adopted in the District's state, on request from any partner district or its privacy consortium. With the first executed NDPA in each state, CHSS will sign the General Offer of Privacy Terms (NDPA Exhibit E) and provide the originating district a standalone copy for the SDPC Resource Registry, so that other districts in that state may subscribe to the same terms by accepting Exhibit E and delivering notice of acceptance.

For purposes of the NDPA: the **Provider** is Stand for Children Leadership Center, Inc. (CHSS program); the **Service** is CHSS Navigator and the ninth grade success coaching it supports; **Provider staff** include CHSS coaches, who are bound by the agreement and trained accordingly. CHSS does not operate a student-facing application other than the Belonging and Skills screeners administered through the District's School Team.

Where a district does not use the NDPA, Appendix A (Part B) applies. Where a district uses both, the document the district signed controls.

## Part B: Appendix A, Data Privacy and Security
::src SDPC NDPA :: Section order follows the NDPA's articles (purpose and FERPA designation; data ownership and authorized access; duties of the LEA; duties of the provider; data provisions including security, breach, disposition, and advertising limits; general offer; miscellaneous) so a district privacy officer recognizes the shape immediately.
::src Luke's experience :: AFUHSD's baseline is the Arizona NDPA Standard Version 1.2 with Exhibit G, which carries Arizona contract requirements and the AI questionnaire Luke co-wrote with the privacy leads from Mesa and Deer Valley.

### A.1 Definitions
::src Drafting choice :: Defined terms are the same as in Agreement Sections Five and Six so the two documents never drift.

Terms defined in Sections Five and Six of the Agreement (Student Data, Screening Data, De-identified Data, Aggregate Data, Navigator, School Team, Coach, Cohort) have the same meaning here. **Subprocessor** means a third party that hosts or processes Student Data on CHSS's behalf.

### A.2 Purpose and legal basis
::src FERPA :: 34 C.F.R. § 99.31(a)(1)(i)(B) (school official exception) and § 99.33 (limits on redisclosure).
::src PPRA :: 20 U.S.C. § 1232h applies to the screeners CHSS administers through schools.
::src COPPA :: 15 U.S.C. §§ 6501–6506; Columbus City's DSA requires a COPPA warranty for any data collected directly from students. Navigator is not student-facing, but screener administration may be, so the commitment is stated "to the extent it applies."
::src Columbus City DSA :: "agrees that it shall comply with all applicable Ohio laws ... regarding the collection, use and protection of data as if it were the District." The "as if CHSS were the District" standard is adopted for every state.

CHSS receives Student Data solely to provide the Services described in the Agreement. The District designates CHSS as a school official with a legitimate educational interest under 34 C.F.R. § 99.31(a)(1)(i)(B). CHSS is under the District's direct control with respect to the use and maintenance of education records and is subject to the redisclosure limits of 34 C.F.R. § 99.33. CHSS will comply with FERPA; with the Protection of Pupil Rights Amendment (20 U.S.C. § 1232h) as it applies to screeners; with the Children's Online Privacy Protection Act (15 U.S.C. §§ 6501–6506) to the extent it applies; and with the student privacy laws of the District's state listed in the State Exhibit, as if CHSS were the District.

### A.3 Ownership and control
::src Columbus City DSA :: "All information, data, and other content transmitted by the District ... will remain the sole property of the District. The District will retain exclusive control over student data, including determining who may access data and how it may be used."
::src James's collateral :: "Your student data remains your district's property, and your district decides who can see it."

All Student Data and Screening Data, and all records CHSS creates or receives on the District's behalf, are and remain the property of the District. The District retains exclusive control over its Student Data, including who may access it and for what purposes. CHSS acquires no rights in Student Data other than the limited license to use it to provide the Services.

### A.4 Authorized and prohibited uses
::src SDPC NDPA :: Article IV prohibitions (no sale; no targeted advertising; no profiling beyond the educational purpose) and Article V on advertising limitations.
::src Columbus City DSA :: "Company shall not use educational records for any commercial purpose outside the scope of the agreement, including but not limited to marketing or advertising to students or parents. Company agrees not to sell, share, or disseminate educational records."
::src Conversation :: The 501(c)(4) clause (d) comes from James's 10/23 flag that Stand's dual structure invites questions "even when nothing is wrong."
::src af-dpa :: knowledge/law/coppa.md and arizona.md: COPPA's "operator" definition excludes nonprofits exempt from § 5 of the FTC Act, and A.R.S. § 15-1046 reaches operators of services "designed and marketed for school purposes." A coaching nonprofit may sit outside both, so "the contract is the only enforcement." That is the reason clause (d) and clause (f) are written in rather than left to statute. NDPA v1.2 IV.2 limits use to "the Services outlined in Exhibit A or stated in the Service Agreement"; v2 4.2 closes that gap with "or as instructed by the LEA," which (a) through (f) mirror.
::src af-dpa :: agents/exhibit-h-rider-draft.md, term 6 ("Partner and evaluator visibility"): "Where the approved service shares data with a program partner, evaluator, certifying body or sponsor, Provider will name the recipient and the data shared ... no other third-party visibility is permitted." Marked in the repo as an agent draft not yet adopted by the Director; reused here as clause (f).

CHSS will use Student Data only to provide the Services and as instructed by the District. CHSS will not: (a) sell, rent, or trade Student Data; (b) use Student Data for targeted advertising or marketing to students, parents, or staff; (c) build a profile of a student for any purpose other than the Services; (d) use Student Data in any advocacy, lobbying, political, or fundraising activity of Stand for Children Leadership Center, Inc. or any affiliated entity, including any entity organized under section 501(c)(4); (e) disclose Student Data to any third party other than a Subprocessor listed under A.6, except as required by law and, where lawful, with prior notice to the District; or (f) share Student Data with any program partner, evaluator, funder, certifying body, or sponsor unless the recipient and the data shared are named in Exhibit D-3 of the Agreement and approved by the District in writing.

### A.5 Data minimization
::src SDPC NDPA :: The NDPA's Exhibit B is a checklist of data elements the provider collects; this clause ties CHSS to the equivalent list in Agreement Exhibit D-1.
::src Emily's email :: "Asking for too much could create unnecessary objections and delays."
::src Columbus City DSA :: Service "will not require a student to disclose more information than is reasonably necessary."
::src af-dpa :: agents/exhibit-h-rider-draft.md, term 3 (data minimization): the provider "will not require Social Security numbers, government identification numbers, payment information, health or disability records" unless listed. Adopted here; IEP/504 status stays an optional element the District may elect.

CHSS will collect only the elements listed in Exhibit D-1 of the Agreement and will not require the District to provide more data than is reasonably necessary to deliver the Services. CHSS will not request Social Security numbers, government identification numbers, payment information, or health records, and will receive disability-related status only where the District elects to provide it under Exhibit D-1. Changes to the element list require the District's written agreement.

### A.6 Subprocessors
::src Emily's architecture :: The CHSS Data Platform diagram: Microsoft Azure / Fabric (data lake, SQL warehouse), Azure API Management, Salesforce Experience Cloud as Navigator (with CRM Analytics and Lightning components), Power BI for research and program analytics, and AI-assisted mapping, validation, and intervention recommendations.
::src SDPC NDPA :: Article IV requires the provider to flow down the agreement's obligations to subprocessors and to maintain a list available to the LEA.
::src Luke's experience :: From the Rescue Ready review (2026): the DPA goes with whoever actually hosts the data. Naming the platforms here is what lets a district CTO stop asking.

CHSS uses the following Subprocessors, each bound by written terms at least as protective as this Appendix:

| Subprocessor | Function | Location |
|---|---|---|
| Microsoft (Azure, Fabric) | Cloud hosting, data lake, data warehouse, API management | United States |
| Salesforce (Experience Cloud, CRM Analytics) | Navigator user platform, student records and intervention workflows | United States |
| Microsoft (Power BI) | Analytics and reporting | United States |
| [AI model provider] | File-mapping assistance, data validation, intervention recommendations | United States |

CHSS will give the District at least thirty days' written notice before adding or replacing a Subprocessor that will process Student Data. The District may object in writing, and the Parties will work in good faith to resolve the objection before the change takes effect.

### A.7 Security program
::src Columbus City DSA :: Sections 5 through 8: encrypted storage in monitored data centers; no storage outside the United States; passwords not visible to employees, salted hashes, SSL; patches "within one week of release"; anti-virus; firewall and DMZ; "third party audits of security operations are conducted annually"; access control lists; "the identity of all persons having access to student data is documented and access is logged"; employees bound by FERPA.
::src San Diego CCAP :: "All staff involved in the data sharing process will be required to sign a confidentiality agreement"; passwords changed frequently; data kept in secure facilities.
::src SDPC NDPA :: Article V and Exhibit F (data security requirements) call for a written security program, access controls, encryption, training, and an incident response plan.
::src Conversation :: Luke and Jonah (10/26) on background checks: Phoenix Union required fingerprinting and onboarding of Teach For America mentors who were entirely virtual, which stalled the program for years. Stating a background check as a CHSS commitment removes one reason for a district to add its own.
::src af-dpa :: knowledge/practice/dpa-review-checklist.md: "TLS 1.2+ in transit, AES-256 or equivalent at rest, including backups"; "MFA on vendor support access"; SOC 2 "does not test application code, does not require penetration testing," which is why the pen test is a separate line. NDPA v1.2 IV.3 binds "each employee or agent with access to Student Data" to confidentiality. The repo records no district position on background checks; that line is a drafting choice from the 10/26 discussion.

CHSS maintains a written information security program with administrative, technical, and physical safeguards appropriate to the sensitivity of Student Data, including at minimum:

- **Encryption.** Student Data is encrypted in transit (TLS 1.2 or higher) and at rest (AES-256 or equivalent). File transfers use SFTP or an HTTPS secure upload; email is never used to transfer Student Data.
- **Access control.** Role-based access on the principle of least privilege. Multi-factor authentication for all CHSS staff and administrator accounts. The identity of every person with access to Student Data is documented, reviewed at least quarterly, and removed within one business day of role change or separation.
- **Logging.** Access to student-level records is logged, including user, time, and record; logs are protected from alteration and retained for at least twelve months. On written request, CHSS will provide the District with log data for end-user, administrative, and maintenance activity relating to its Student Data.
- **Passwords and sign-on.** Stored passwords are salted and hashed; passwords are never visible to CHSS staff; single sign-on is supported for District users where the District elects it.
- **Infrastructure.** Production environments are segregated from the public internet by firewall and network controls; critical security patches are applied within seven days of release; anti-malware is current on all endpoints with access to Student Data; backups are encrypted and tested.
- **Secure development.** Changes to Navigator and the data platform go through code review and testing; secrets are managed in a vault, never in code.
- **Personnel.** All CHSS staff with access to Student Data, including Coaches, pass a background check before access is granted, complete privacy and security training at hire and annually, and sign confidentiality obligations.
- **Independent assessment.** CHSS undergoes an independent third-party assessment of its security controls at least annually (SOC 2 Type II or an equivalent independent audit) and an annual penetration test of Navigator and the data platform. Summaries are available to the District under A.13.
- **Incident response.** CHSS maintains and tests an incident response plan covering assessment, containment, evidence preservation, notification, recovery, documentation, and post-incident review.

### A.8 Breach notification
::src Columbus City DSA :: Breach section lists the response steps (assess, communicate, contain, classify severity, protect evidence, notify external agencies, recover, document, assess cost, review, update policies) and gives the District the right to request logs; Ohio R.C. 1347.12 governs notification to affected persons.
::src SDPC NDPA :: Article V requires notice to the LEA of any security breach, cooperation in the investigation, and provider responsibility for its own costs; the national form's notice window is the one most state versions keep.
::src Luke's experience :: 10/19: "if you have a leak, you'll tell us, if we have a leak, we'll tell you ... those things make us feel a lot more comfortable." Districts do not want to learn of a breach from the press.
::src af-dpa :: knowledge/sdpc/ndpa-structure.md, Arizona NDPA v1.2 Article V.4, verbatim: "the Provider shall provide notification to LEA within seventy-two (72) hours of confirmation of the incident, unless notification within this time limit would disrupt investigation of the incident by law enforcement." The repo's reverification notes recommend keeping v1.2's broad, undefined trigger (not v2's "in violation of applicable law" qualifier), saying who notifies families, and lifting the Illinois breach-cost allocation (parent notification, credit monitoring, "legal fees, audit costs, fines").

If CHSS becomes aware of unauthorized access to, or acquisition, disclosure, or loss of, Student Data, whether or not it meets a statutory definition of breach (a "Breach"), CHSS will notify the District's privacy contact without unreasonable delay and in no event later than seventy-two hours after confirming the Breach, unless notification within that time would disrupt a law-enforcement investigation, by telephone and email, with the information then known: the nature of the Breach, a description of the Student Data involved, the students affected, steps taken to contain it, and a point of contact. CHSS will update the District as the investigation proceeds, cooperate fully, and comply with any breach-notification law applicable to the District's data. The District decides whether and how affected students and parents are notified; CHSS will not notify students, parents, or the public without first consulting the District, except where law requires otherwise. CHSS will bear the reasonable costs attributable to its Breach, including parent notification, credit monitoring where offered, forensic investigation, legal fees, and regulatory fines.

### A.9 Data location
::src Columbus City DSA :: "No student data is stored outside the United States without the District's written consent."
::src Conversation :: Jonah (10/26): "Don't store your data in Russia, et cetera."

Student Data is stored and processed only in data centers located in the United States. CHSS will not transfer Student Data outside the United States without the District's prior written consent.

### A.10 Retention, de-identification, and destruction
::src SDPC NDPA :: Article IV "Disposition of Data" and Exhibit D (Directive for Disposition of Data): sixty days from written request; duty does not extend to de-identified data.
::src Columbus City DSA :: Ninety days after termination to destroy or return all educational records.
::src FERPA :: De-identification standard at 34 C.F.R. § 99.31(b)(1); the attribute of "reasonable determination" that identity is not personally identifiable "taking into account other reasonably available information."
::src Emily's architecture :: The platform already separates a "De-identification & Privacy" step (tokenization and pseudonymization for research datasets) from the identifiable warehouse. This clause makes that separation contractual.
::src Drafting choice :: Cell suppression at fewer than ten students is a common state-reporting threshold; it keeps aggregate results publishable without re-identification risk at small schools.
::src Conversation :: James (10/23): keep "Agua Fria High School went from 60% on track to 72%"; delete the student-level data. Luke: "That's a different thing."
::src af-dpa :: knowledge/sdpc/ndpa-structure.md, NDPA v1.2 IV.5: "Provider agrees not to attempt to re-identify De-Identified Student Data ... Provider's use of De-Identified Data shall survive termination of this DPA ... Provider agrees not to transfer de-identified Student Data to any party unless (a) that party agrees in writing not to attempt re-identification, and (b) prior written notice has been given to the LEA who has provided prior written consent." v2 4.5 adds that de-identification must "comply with either NIST de-identification standards or US Department of Education guidance." Both are adopted below.
::src af-dpa :: knowledge/law/ferpa.md: § 99.31(b)(2) allows coded student-level releases only for education research, with a code "not based on" the student's SSN "or other personal information" and the method kept secret; a hash of the student number is a code based on personal information. PTAC: "simple removal of direct identifiers ... DOES NOT constitute adequate de-identification." Hence the random token and the destroyed key.
::src af-dpa :: knowledge/law/deidentification-and-definitions.md: the captures "do not settle" a minimum cell size; PTAC uses "a minimum cell size" and "controlled rounding," and "a vendor's 'aggregate' effectiveness report with n=3 cells is PII." Ten is the drafting choice, matching common state reporting thresholds.

- **During the term.** CHSS retains Student Data only as long as needed to provide the Services.
- **On request.** On the District's written directive at any time, CHSS will return or destroy the Student Data specified within sixty days, on a schedule agreed with the District. The District may use the NDPA's Directive for Disposition of Data (Exhibit D) for this purpose with no further notice required.
- **On termination.** Within sixty days after the Agreement ends, CHSS will destroy or return to the District all Student Data and Screening Data, including copies held by Subprocessors, and will certify destruction in writing signed by an officer. Copies in encrypted backups expire on the documented rotation, not to exceed ninety days, are never restored to production, and are certified as expired when that date passes.
- **De-identified and Aggregate Data.** CHSS may create De-identified Data in accordance with NIST de-identification standards or U.S. Department of Education guidance, by removing direct and indirect identifiers and replacing the student identifier with a random token that is not derived from any student identifier or other personal information, under a key that CHSS destroys with the identifiable data. Aggregate Data is a subset of De-identified Data. CHSS may retain De-identified Data and Aggregate Data after termination to evaluate and improve the program, including following Cohort outcomes over time. CHSS will not attempt to re-identify any student and will not transfer De-identified Data to any third party other than a Subprocessor unless that party agrees in writing not to attempt re-identification and the District has given prior written consent. Aggregate Data will suppress any cell smaller than ten students.
- **Research and publication.** CHSS may publish findings based on De-identified Data and Aggregate Data. No publication will identify a student. CHSS will not identify the District in any publication without the District's prior written consent and will provide the District a copy of any report that includes the District's aggregate results at least fifteen business days before publication. The District may always see its own data.

### A.11 Parent and eligible student rights
::src FERPA :: Parents and eligible students have rights to inspect, review, and seek amendment of education records (34 C.F.R. §§ 99.10–99.22); those rights run against the District, which the provider must support.
::src Columbus City DSA :: The company and District "shall establish reasonable procedures ... by which a parent, legal guardian or eligible student may review personally identifiable information on the pupil's records, correct erroneous information."
::src SDPC NDPA :: Article II: the provider assists the LEA in responding to parent and eligible-student requests within a stated period.

Requests by a parent or eligible student to inspect, review, or correct education records are handled by the District. CHSS will support the District by providing, within ten business days of request, the Student Data it holds about the student, and will correct or delete data as the District directs.

### A.12 Use of artificial intelligence
::src Luke's experience :: The Arizona NDPA Exhibit G AI questionnaire, which Luke co-developed with the privacy leads from Mesa and Deer Valley with input from about a dozen privacy and technology professionals: how the vendor uses AI, what data goes to AI providers, whether user data trains models, and what safeguards and oversight exist. This clause answers those questions before they are asked.
::src Emily's architecture :: AI-assisted mapping, anomaly detection, "risk models and intervention recommendations" are in the platform design; Jonah (10/19) described AI that "can help coach the team leads."
::src af-dpa :: knowledge/practice/ai-dpa-clauses.md (marked in the repo as a drafting suggestion, not a standard): model-provider disclosure "by URL and date, and the country of processing," thirty days' notice before changing a model provider with a termination right; outputs "descriptive of an identifiable student are Student Data"; disclosure of any subprocessor personnel who may view prompts or outputs for abuse monitoring; outputs "require human review before use" and are not "the sole basis for any decision with legal or material effect on a student." The shortest proven binding wording is California NDPA v1.5 Exhibit G cl. 8: "Student Data ... shall not be used for training purposes or to develop synthetic and/or inferred data."
::src af-dpa :: knowledge/sdpc/ai-addendum-and-checklist.md lists the Arizona checklist questions this clause pre-answers: base model and provider (1.1–1.2), opt-out of AI decision-making (1.4), data shared with an AI subprocessor (4.2), whether user data trains the model (4.7), human in the loop (5.6), and query logging (5.7).

CHSS uses automated and machine-learning tools within the data platform to assist with mapping incoming files to a common format, to flag data-quality problems, and to suggest interventions for the School Team's consideration. CHSS commits that: (a) Student Data, De-identified Data, and any outputs derived from them will not be used for training purposes or to develop synthetic or inferred data, by CHSS or by any Subprocessor, except a model used solely to deliver the Services and identified in A.6; (b) each model provider is listed as a Subprocessor with the product tier used, the provider's data-use terms by URL and date, and the country of processing, and is contractually prohibited from retaining or training on Student Data, with CHSS providing the provider's written attestation on request; (c) outputs that describe an identifiable student are Student Data for all purposes of this Appendix; (d) intervention suggestions are recommendations for educators, who make all decisions about students, and are never the sole basis for any decision with a material effect on a student; (e) no Subprocessor personnel view prompts or outputs containing Student Data except as disclosed to the District in writing; (f) the District may request that AI-generated recommendations be disabled for its schools; (g) CHSS will give thirty days' written notice before adding or changing a model provider, and the District may object under A.6; and (h) CHSS will complete the District's AI questionnaire (for example, Arizona NDPA Exhibit G) on request.

### A.13 Audit and assurance
::src Columbus City DSA :: Annual third-party audits of security operations; District may request log data for incident investigation.
::src Conversation :: Jonah (10/26) listed audits among the standard terms to include; James (10/23): "Columbus City requires a security audit every three years or something like that" (the document says annually).
::src Drafting choice :: Evidence-on-request once a year, plus full cooperation after a breach, is the posture most CTOs accept in place of an unlimited audit right; an audit right is still offered where state law or policy demands it.
::src af-dpa :: knowledge/sdpc/article-crosswalk-v1-2-to-v2-1.md: NDPA v1.2 Article V.2 "gives the LEA the right to audit the Provider." knowledge/GAPS.md recommends the Utah audit-evidence menu (self-assessment, questionnaire, "SOC2 or SOC3" report, or on-site review by agreement), adopted below so a district can pick the form of evidence.

On request, not more than once per year unless a Breach has occurred, CHSS will provide the District with any of the following at the District's election: a completed security self-assessment, responses to the District's security questionnaire within thirty days, its most recent independent assessment report (SOC 2 Type II, SOC 3, or equivalent) and penetration test summary under a confidentiality agreement, a description of its security program, and a certificate of insurance. If the District's state law or policy requires an audit right, CHSS will cooperate with an on-site or remote audit at a mutually agreed time, conducted so as not to compromise other districts' data.

### A.14 Insurance
::src Columbus City DSA :: "Your company must carry cyber liability insurance of at least $1,000,000 to cover Crisis Management and Computer System Extortion, Media and Content Liability, and Security and Privacy Liability."
::src San Diego CCAP :: Each party: commercial general liability $1,000,000 per occurrence / $2,000,000 aggregate; professional errors and omissions $1,000,000; other party as additional insured; certificate of insurance on request; self-insurance acceptable.
::src James's MOU draft :: Section Eight currently promises "reasonable liability insurance" and a certificate "including any applicable cybersecurity or data-security coverage" on request; this clause states the limits.
::src af-dpa :: knowledge/practice/dpa-review-checklist.md: "the NDPA has no insurance clause"; district practice research puts "$1M for directory-only, $2M+ for SIS, assessment, special education or health data," and Beaverton requires $2,000,000 per claim and aggregate "with the policy running two years past the contract." $2,000,000 is drafted; Columbus's $1,000,000 floor is satisfied. Stand's finance lead confirms the actual policy before this is sent.

CHSS maintains, and will provide certificates on request for: cyber liability insurance of at least $2,000,000 per claim and in the aggregate, covering security and privacy liability, crisis management, network extortion, and media and content liability, maintained for two years after this Appendix ends; commercial general liability of $1,000,000 per occurrence and $2,000,000 aggregate; and professional errors and omissions liability of $1,000,000 per claim. These requirements may be met through a reasonable self-insurance program.

### A.15 Screening Data
::src Emily's email :: Area 3 of the four the agreement must cover: "the Belonging and Skills screeners we administer, including the collection, storage, analysis, and use of student-level screening data."
::src PPRA :: 20 U.S.C. § 1232h; the District approves instruments and gives notice (Agreement 6.7). This clause covers what CHSS does with the responses.
::src Conversation :: Jonah (10/19): screener results feed the Navigator so the team can see that "fifteen other kids have the same profile" and deliver one intervention to all of them. Student-level screening results therefore have to be visible to the School Team.

Screening Data is collected by CHSS only after the District has approved the instruments and provided any required notice under Section 6.7 of the Agreement. Screening Data is subject to every protection in this Appendix. Student-level screening results are visible to the School Team and, under Option A of Section 5.4, to the Coach; CHSS program and research staff see only De-identified and Aggregate Screening Data.

### A.16 Term, termination, and survival
::src Columbus City DSA :: Term "shall be co-terminus with the contract/agreement and shall terminate when all of the student data ... is destroyed and/or returned."
::src James's MOU draft :: The Agreement's cure period is ten days (Section Two); thirty days is used here for data-specific breaches because remediation of a security finding usually takes longer than ten days.

This Appendix is coterminous with the Agreement and continues until all Student Data has been returned or destroyed under A.10. Sections A.3, A.4, A.8, A.10, and A.11 survive termination. The District may terminate the data provisions of the Agreement on thirty days' written notice if CHSS materially breaches this Appendix and does not cure within that period.

### A.17 Governing law and State Exhibit
::src State law :: Ohio: R.C. 3319.321 (confidentiality of student records), 3319.325–3319.327 (educational records and third-party contractors), and Chapter 1347 including R.C. 1347.12 (breach notification), all named in the Columbus City DSA. California: Education Code § 49073.1 (contract requirements for digital storage and educational software) and the Student Online Personal Information Protection Act, Business and Professions Code § 22584. Arizona: Arizona NDPA Exhibit G, including the AI questionnaire.
::src Lewis County :: Missouri districts will supply the Missouri NDPA state exhibit through their consortium; it is listed as "to be added" rather than drafted here.

This Appendix is governed by the laws of the District's state. The State Exhibit attached for the District's state sets out additional required terms, including: for Ohio, compliance with Ohio Revised Code 3319.321, 3319.325 through 3319.327, and Chapter 1347 (including breach notification under R.C. 1347.12) as if CHSS were the District; for California, the terms required by Education Code § 49073.1 and Business and Professions Code § 22584; for Arizona, Arizona NDPA Exhibit G including the AI questionnaire; and for Missouri, Massachusetts, Utah, and other states, the state NDPA exhibit where one exists.

### A.18 Order of precedence
::src Drafting choice :: Mirrors Section 5.2 of the Agreement so both documents say the same thing about which controls.

If this Appendix conflicts with the Agreement, this Appendix controls as to Student Data. If the District has executed the NDPA with CHSS, the NDPA controls as to any conflict with this Appendix.

## Part C: System specifications (district-facing)
::src Conversation :: Jonah (10/26): "there's going to be a sheet that you design, where it's like, these are the systems we will have, but we're going to present it as, this is our system." Emily: leadership "can very quickly look at it and feel legit that we're behind it," and technical people see "these guys know what they're talking about."
::src Emily's architecture :: Every platform fact below is taken from the CHSS Data Platform diagram; items the diagram claims (RBAC, encryption, audit logging, retention policies) are stated here as commitments and should be confirmed by Emily before this page is shown to a district.
::src Drafting choice :: Written as present-tense statements where CHSS can confirm them and bracketed where a decision or build is still pending.

**Platform.** CHSS Navigator is a web application delivered on Salesforce Experience Cloud, backed by a CHSS data platform on Microsoft Azure and Microsoft Fabric. All environments are hosted in United States regions.

**How data moves.**

1. The District transfers files (CSV, TXT, or Excel) to CHSS by SFTP on a schedule, or uploads them through the CHSS secure portal. Email is never used.
2. Files are virus-scanned and validated on receipt, mapped to a common data model, checked for quality (type, completeness, anomalies), and loaded to the data lake and warehouse with an audit record.
3. Student records are matched by the District's student identifier (and state identifier where provided). Probabilistic matching is used only to flag possible duplicates for human review, never to link records automatically.
4. On-track indicators, course-failure flags, and attendance measures are computed and published to Navigator for the School Team.
5. A separate de-identification step produces tokenized research datasets, which are the only datasets CHSS program and research staff use.

**Who can see what.** Role-based access in Navigator: school users see their school's students; district users see their district; Coaches see aggregate views, or student-level views for their schools where the District has elected Option A; CHSS program and research staff see de-identified and aggregate data only. Every access to a student-level record is logged.

**Security controls.**

- Encryption in transit (TLS 1.2 or higher) and at rest (AES-256).
- Multi-factor authentication for all CHSS accounts; single sign-on available for District users.
- Least-privilege, role-based access; documented access roster reviewed quarterly; access removed within one business day of separation.
- Access and administrative logging retained twelve months and available to the District on request.
- Production segregated from the internet by firewall and network controls; critical patches within seven days; anti-malware on all endpoints; encrypted, tested backups.
- Background checks and annual privacy training for all staff with access, including Coaches.
- Independent security assessment annually (SOC 2 Type II or equivalent) and an annual penetration test; summaries available on request. [First assessment scheduled for completion by: date.]
- Written, tested incident response plan; the District is notified within seventy-two hours of a confirmed breach.

**Subprocessors.** Microsoft (Azure, Fabric, Power BI), Salesforce (Experience Cloud, CRM Analytics), and [AI model provider]. All U.S.-hosted, all under written terms at least as protective as CHSS's agreement with the District. The District receives thirty days' notice of any change.

**Artificial intelligence.** Used for file-mapping assistance, data-quality checks, and intervention suggestions presented to educators. District data is never used to train models available to others. Recommendations can be disabled at the District's request.

**Retention.** Identifiable data is held only for the term of the agreement, destroyed or returned within sixty days of termination or of a written directive, with written certification; backups expire on a documented rotation of no more than ninety days. De-identified and aggregate data may be retained for program evaluation; no re-identification.

**Insurance.** Cyber liability $2,000,000 per claim and aggregate; general liability $1,000,000 per occurrence and $2,000,000 aggregate; professional errors and omissions $1,000,000. Certificates on request.

**Agreements.** CHSS signs the National Data Privacy Agreement (any state version) or provides Appendix A to the same standard, and provides an executed copy and a ninety-day expiration notice.
