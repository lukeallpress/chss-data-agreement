# Technical documentation: the plan and the control inventory
::src Conversation :: Emily and Phil (11/4 call): technical specifics leave the agreement and live in a supplemental document built from Emily's matrix with a specifics column, provided to a district that asks, "a safe amount." Appendix A.7, A.13, and the reference paragraph at the end of the Agreement point here.
::src SchooLinks :: Shape taken from the two-page Data Security and Privacy Plan SchooLinks filed with the Student Data Privacy Consortium (January 2023) and its public security page: plain prose, hosting named, what is encrypted, who can see what, how data moves, deletion at termination, "more detail is in the agreement signed with the district." Part A follows that register; Part B is the on-request detail behind it.
::src Needs CHSS confirmation :: Every platform fact below comes from the platform diagram and the October 26 and November 4 calls and has not been verified against a live tenant. Bracketed entries are CHSS's to fill; "Confirm" in the status column means stated from design, not evidence (Decisions, O4).

> **Two documents in one.** Part A is the district-facing plan, two pages, provided with the agreement package and linkable for the TEC form, and the piece a district privacy officer reads first. It does not replace or revise Stand's website privacy policy. Part B is the control inventory in the matrix format Emily and Phil are working in, with specifics, evidence, status, and owner, provided to a district on request under Appendix A.13. **Draft 0.2, Nov 4, 2026.** Nothing here is a contractual term beyond what Appendix A states.

## Part A. CHSS Data Security and Privacy Plan

*Center for High School Success, a program of Stand for Children Leadership Center, Inc. Last updated [date]. This plan describes how CHSS protects the student data school districts share with it. Protocols and procedures may change as practices improve; CHSS provides the current version with its district agreement package and at a stable link for the forms that ask for one. Stand for Children's website privacy policy (stand.org/privacy-policy) governs the website and is not changed by this plan. More detailed information about how CHSS handles a particular district's data is specified in the data sharing agreement signed with that district.*

### What CHSS receives and why

School districts share student records with CHSS so that 9th Grade Success Teams and CHSS coaches can identify students who are off track in 9th grade and act early. The data is limited to what the on-track work needs: enrollment, courses and marks, credits, attendance, and the elements a district elects for evaluation (Exhibit D-1 of the agreement). CHSS does not ask for Social Security numbers, government identifiers, payment information, or health records. Districts remain the owners of their data and decide who may see it.

### Where the data lives

CHSS's infrastructure is entirely cloud-based, on industry-leading hosting and data-platform providers [such as Microsoft], with the Navigator application delivered on a commercial customer-relationship platform. Where possible, CHSS uses the providers' managed services rather than stand-alone servers, which lowers the attack surface and keeps patching with the provider. All student data is stored and processed in data centers in the United States.

### How data gets to CHSS

Districts never send student data by email. Data moves by a scheduled transfer from the district's student information system or data warehouse to a CHSS SFTP server with key-based authentication, or by a read-only connection from the district's SIS vendor. Files are scanned and validated on receipt, and the district's technical contact receives a validation report after every load. The CHSS Technical and Data Integration Guide describes the files and the process.

### Data security

CHSS maintains an information security program aligned with [CIS Controls v8.1, Implementation Group 1], a framework recognized by the National Data Privacy Agreement, and assesses itself against it annually. Measures include:

- Encryption of student data in transit and at rest, including backups and the SFTP landing zone.
- Multi-factor authentication for all CHSS accounts and for privileged access; role-based access with least privilege as the default.
- Access to student data limited to the people who need it for the service: the district's 9th Grade Success Team sees its own school; the CHSS coach assigned to a school sees that school only; a small set of named CHSS technical staff administer the platform and investigate incidents; CHSS program, research, and leadership staff work only with de-identified data.
- Logging of access to student data and of administrative actions, retained at least ninety days and available to a district for an incident investigation.
- Security updates evaluated, validated, and applied according to severity, system risk, and operational impact, with the platform layer patched by the providers.
- Endpoint protection on CHSS-managed devices; staff devices managed centrally.
- A written incident response plan and a disaster recovery plan, tested [annually].
- Daily backups held separately from the production environment, so data remains available in the event of ransomware; backups are restored only for continuity and recovery, and deletion obligations follow any restored data.
- Security training for every employee at onboarding and annually; background checks for staff with access to student data, coaches included.

### How CHSS ensures privacy

CHSS never sells student or district data and never uses it for advertising, profiling, or the advocacy, political, or fundraising work of any affiliated organization. CHSS does not share student data with program partners, evaluators, or funders unless the district has approved the recipient in writing.

CHSS restricts internal access to and use of district data. Only the CHSS staff who support a district's schools can see its student-level records, and every such access is logged. Student data is not used for development or testing.

When CHSS studies program outcomes, it uses only de-identified data, created by removing identifiers and replacing the student identifier with a random token under a key that is destroyed with the identifiable data. Before any de-identified data is kept or released, CHSS makes and documents the determination FERPA requires that a student cannot be identified from it, taking into account other reasonably available information.

**Artificial intelligence.** The Navigator platform uses approved AI and analytics capabilities to support educational analysis, next-step planning, and intervention recommendations for educators, who make all decisions about students. No student-identifiable data is used by CHSS or any provider to train any AI model, including any large language model. [One sentence naming the category of model provider and the tier used, and stating that the provider does not retain or train on customer data.]

### Incidents

If CHSS validates and confirms that student data has been accessed, acquired, disclosed, or lost without authorization, it notifies the district's privacy contact within seventy-two hours of that confirmation, handles the incident under its incident response plan, supports the district's notice to families, and bears the costs attributable to its own breach.

### Retention and deletion

CHSS keeps a district's student data only for the term of the agreement. On the district's written directive, or within sixty days after the agreement ends, CHSS returns or destroys the district's identifiable student data from every system, including its providers, and certifies the destruction in writing. De-identified data may be retained for program evaluation, with no attempt at re-identification.

### Who to contact

Privacy: [CHSS privacy officer, email]. Security: [CHSS security officer, email]. Vulnerability reports: [email]. Stand for Children website privacy policy: stand.org/privacy-policy. This plan: [stable link].

---

## Part B. Control inventory and technical specifications

*Provided to a district on request under Appendix A.13, under the district's confidentiality obligations. Not for publication; the public piece is Part A.*

| Item | Entry |
|---|---|
| Version and date | [0.2, Nov 2026] |
| Owner | [Phil Toynton, Director of Infrastructure] |
| Relationship to the Agreement | Describes how CHSS implements Appendix A. Not a contractual term beyond what Appendix A states. |
| Review cycle | Annually with the security assessment, and on any change of Subprocessor category or data flow |

**Status key.** Done: in place today, evidence available. In progress: being built, date given. Planned: not started, date given. Confirm: stated from the platform design, not yet verified against the live tenant.

### B.1 Platform overview and data flow

CHSS Navigator is a web application for 9th Grade Success Teams and CHSS coaches, delivered on [Salesforce Experience Cloud]. Behind it, the CHSS data platform [Microsoft Azure and Microsoft Fabric] receives district files, maps them to a common data model, computes on-track indicators, and holds a de-identified warehouse for program analytics [Power BI]. All environments run in United States regions [confirm regions].

1. The district's SIS or data warehouse exports the specified files on a schedule and transfers them by SFTP to the CHSS landing zone, or the SIS vendor delivers them by a read-only connection.
2. Files are virus-scanned and validated on receipt, mapped to the common data model (AI-assisted mapping suggestions reviewed by a CHSS data engineer), checked for quality, and loaded to the data lake and identifiable warehouse with an audit record. A validation report goes to the district's technical contact.
3. Records are matched on the district's student identifier. Probabilistic matching only flags possible duplicates for human review; it never links records automatically.
4. On-track indicators, course-failure flags, attendance measures, and screener results are published to Navigator for the 9th Grade Success Team and the assigned coach.
5. A separate de-identification step produces tokenized datasets (random token, key destroyed with the identifiable data) for the research warehouse, the only data CHSS program, research, and leadership staff use.

### B.2 Control inventory

Rows follow the matrix IDs so the two documents read side by side. "Agreement" is the Appendix A clause the row implements.

### Agreement structure and data scope

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-03 | Services and authorized purposes | A.2, A.4 | Use limited to the Services; no sale, advertising, profiling, advocacy use, or partner sharing without written approval | Agreement text | Done | CHSS |
| G-04 | Data elements and minimum necessary | A.5, Exhibit D-1 | Required and Optional elements listed; no SSNs, government IDs, payment, or health records; IEP/504 and meal status only where elected | Exhibit D-1; integration guide | Done | CHSS |
| G-05 | Data-flow and system inventory | A.6, A.13 | B.1 above and the subprocessor table in B.3; diagram maintained in [location] | This document; architecture diagram | [In progress, date] | Phil |
| G-07 | De-identified and aggregate data | A.10 | Random token not derived from the student ID; key destroyed with identifiable data; documented § 99.31(b)(1) determination before any release; minimum cell size [10] on published aggregates | Tokenization design; review checklist; suppression setting | [In progress] | Emily |

### AI and data use

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-08 | No training on Student Data | A.12 | No CHSS-operated model is trained on identifiable Student Data. The model provider is used through [an enterprise tier: name, tier] with no training on customer data and [zero or n-day] retention; provider terms at [URL, date] | Provider terms excerpt; provider attestation | [Confirm] | Phil |
| G-09 | AI-assisted analysis | A.12 | AI used for: file-mapping suggestions (reviewed by an engineer before use); data-quality anomaly flags; grouping students with similar screener profiles for an intervention cycle; drafting suggestions shown to educators. Educators decide. | Feature list; screenshot | [Confirm] | Emily |
| G-29 | Which data reaches the model provider | A.13 | [Which elements, at which step; whether prompts include names; who at CHSS or the provider can see prompts and outputs; logging of model calls] | Data-flow note | [Confirm] | Phil |

### Security governance and assurance

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-10 | Cybersecurity framework | A.7 | CIS Controls v8.1, Implementation Group 1, as the internal baseline; named on the TEC NDPA Exhibit F. Mapping to the NIST Cybersecurity Framework for New York districts: [one page, date] | Framework mapping; IG1 self-assessment | [In progress, date] | Phil |
| G-33 | Annual assessment | A.13 | Annual self-assessment against CIS v8.1 IG1; summary of findings and corrective actions available to districts on request. First assessment: [date] | Assessment summary | [Planned, date] | Phil |
| G-11 | Third-party audit (where a district requires it) | Exhibit D-5 | Hosting and platform providers' SOC 2 Type 2 reports (Microsoft Azure; Salesforce) provided annually under NDA; CHSS does not hold its own SOC 2. Independent assessment of CHSS's own controls: [not planned / scoped if Columbus requires it] | Provider reports | [Confirm] | Phil |
| G-12 | Penetration testing and vulnerability scanning | Technical documentation only | [Platform providers' testing covers the hosting layer; continuous vulnerability scanning on CHSS components: tool; CHSS custom pages: planned or not] | | [Confirm] | Phil |
| G-26 | Incident response and disaster recovery | A.7, A.8 | Written IR plan covering assessment, containment, evidence preservation, notification, recovery, documentation, review; DR plan with [RTO/RPO]; tested [annually, last test date] | Plan table of contents; test record | [Confirm] | Phil |
| G-27 | Breach notification | A.8 | District privacy contact notified within seventy-two hours of a validated and confirmed incident; notification template; parent-notice support (affected list, draft notice) | Template; runbook | [In progress] | Emily |

### Identity, access, and logging

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-13 | Least privilege and roles | A.7, 5.4 | Navigator roles: school user (own school), district user (own district), CHSS coach (assigned schools only), CHSS technical administrator (named set, minimum necessary). CHSS program, research, and leadership staff: de-identified warehouse only | Role matrix; access roster | [Confirm] | Phil |
| G-14 | Authentication | A.7 | MFA required for all CHSS accounts and privileged access. District users: username/password with MFA [and SSO via Google or Microsoft where the District elects it: confirm availability and date] | Identity configuration | [Confirm; SSO answer owed on Jonah's 6.8 question] | Phil |
| G-15 | Access removal | A.7 | CHSS staff: removed at separation through [HR offboarding checklist], target [same business day]. District users: on the district's roster file or notice under 6.8 | Offboarding checklist | [Confirm] | Phil |
| G-16 | Logging | A.7 | Access and administrative logs on [Salesforce event monitoring / Azure Monitor]; retained [90 days minimum; state actual]; exportable per district for incident investigation | Log retention setting; sample export | [Confirm] | Phil |

### Security operations and data protection

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-17 | Vulnerability and patch management | A.7; Exhibit D-5 for Columbus | Severity-based: critical vulnerabilities evaluated and validated on disclosure, applied within [target] where reasonable and applicable; platform layer patched by providers | Patch policy | [Confirm] | Phil |
| G-18 | Network | Technical documentation only | Production segregated from the public internet by [provider network controls]; VPN-only or IP-restricted administrative access; no direct database exposure | Architecture diagram | [Confirm] | Phil |
| G-19 | Endpoint protection | A.7 | [Product] on all CHSS-managed devices with access to Student Data; coaches' devices managed by [MDM] | Configuration | [Confirm] | Phil |
| G-20 | Secure development | Technical documentation only | Code review and testing before release; secrets in [vault]; no Student Data in non-production environments [or masked]; input sanitization on uploaded files and UI | Release process | [Confirm] | Phil |
| G-21 | Data transfer | A.7, Exhibit D-2 | SFTP with key-based authentication to a per-district landing folder; HTTPS for the SIS vendor connection; email never used | SFTP configuration | [Confirm] | Phil |
| G-22 | Encryption | A.7 | In transit TLS 1.2 or higher; at rest provider-managed encryption [AES-256] on every store including backups and the landing zone; key management by [provider / CHSS] | Configuration | [Confirm] | Phil |

### Retention and deletion

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-23 | Backups | A.10 | Daily backups stored separately from production; retention [n days]; restores only for continuity, recovery, or operations; any restored Student Data subject to the same deletion duty | Backup policy | [Confirm] | Phil |
| G-24 | Return or destruction | A.10 | Within sixty days of a directive or termination, across every store: Navigator, data lake, identifiable warehouse, analytics copies, backups (by expiry), and Subprocessors. Deletion runbook: B.4 | Runbook; certificate template | [In progress, O13] | Emily |
| G-25 | Destruction certification | A.10 | Written certificate signed by [officer], listing systems and the backup expiry date | Template | [Planned] | Emily |

### Workforce

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-30, G-31 | Background checks, confidentiality, training | A.7 | [Background check at hire for all staff with access, coaches included; confidentiality in the employment agreement; privacy and security training before access and annually: course, provider] | HR policy; training records | [Confirm with Demian, O5] | Demian |

### Data rights and subprocessors

| ID | Topic | Agreement | Specifics | Evidence on request | Status | Owner |
|---|---|---|---|---|---|---|
| G-32 | Parent requests | A.11 | District's technical contact requests a student's record; CHSS returns [export format] within [target]; corrections applied on the next feed or by request | Procedure | [Confirm] | Emily |
| G-28 | Flow-down | A.6 | Each Subprocessor under its standard data protection agreement or written terms; see B.3 | Terms links | Done | CHSS |

### B.3 Subprocessors

This is the list Appendix A.6 refers to. It names the providers; the Agreement names only their categories.

| Category | Provider and product | Function | Student Data received | Location | Terms |
|---|---|---|---|---|---|
| Cloud hosting and data platform | Microsoft Azure; Microsoft Fabric | Landing zone, data lake, identifiable warehouse, API management | All elements in Exhibit D-1 | United States [regions] | Microsoft Product Terms and DPA, [URL, date] |
| Customer-relationship platform | Salesforce Experience Cloud; CRM Analytics | Navigator: user platform, student records, intervention workflows, screener results | Student-level records for participating schools | United States | Salesforce DPA, [URL, date] |
| Analytics | Microsoft Power BI | Program analytics and reporting | De-identified and aggregate data only | United States | Covered by Microsoft terms |
| AI model provider | [Provider, product, tier] | Mapping suggestions, data-quality flags, grouping, drafting suggestions | [Elements sent, by step] | United States | [URL, date]; no training on customer data; retention [zero / n days] |

Changes within a category are recorded in the version history of this document.

### B.4 Deletion runbook (outline)

For each store, who runs the step, how it is executed, how completion is evidenced, and how long it takes. [To be completed, O13.]

| Store | Step | Executed by | Evidence | Time |
|---|---|---|---|---|
| Navigator (Salesforce) | Delete district records and related objects; purge recycle bin | [role] | [report] | [days] |
| Data lake and warehouse (Fabric) | Drop district partitions; purge; confirm no copies in notebooks or pipelines | [role] | [report] | [days] |
| Analytics (Power BI) | Remove district datasets; refresh | [role] | [report] | [days] |
| AI provider | Confirm no retained prompts or files | [role] | Provider statement | [days] |
| Backups | Record expiry date; certify when passed | [role] | Backup policy; certificate | [n days] |
| Landing zone (SFTP) | Delete received files and archives | [role] | Listing | [days] |

### B.5 Version history

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | Nov 4, 2026 | First draft from the matrix and platform diagram | |
| 0.2 | Nov 4, 2026 | Part A plan added in the SchooLinks shape; integration guide split out | |
