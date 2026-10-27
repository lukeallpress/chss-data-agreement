# Notes
::src Conversation :: James (10/23 and 10/26) is the one writing to districts right now: a Missouri partner district's technology coordinator, the Columbus City CTO for the first review, and San Diego for the second. These are paste-ready paragraphs and asks, in his voice, consistent with the drafts on the other tabs.
::src Drafting choice :: Written for a technology coordinator or CTO reader: short, concrete, no legal citations. The agreement drafts carry the citations.

Use what fits. Each block is standalone. Where a block makes a commitment on CHSS's behalf (NDPA, Exhibit E, the de-identified evaluation carve-out), it matches the current drafts; if those change, change the email.

## 1. Reply to the Missouri district's technology coordinator
::src Lewis County :: Her 10/26 email: the district has asked its consortium (TEC via MOREnet) and the SDPC Resource Registry to obtain an NDPA with CHSS; "the purpose of this service is to support student success and timely interventions, not to conduct research. If this part is not correct, please let me know."
::src FERPA :: She is testing which exception applies. "Interventions" means the school official exception (34 C.F.R. § 99.31(a)(1)(i)(B)); "research" would push her consortium toward the studies exception and a different agreement. The reply confirms her framing and discloses the de-identified evaluation so it is never a surprise.
::src af-dpa :: knowledge/sdpc/exhibit-e-general-offer.md: the first signed NDPA in a state plus a standalone Exhibit E lets other districts in that state subscribe. The sentence about "a general offer of terms" assumes CHSS is willing to sign Exhibit E; delete it if not.

> Thank you for getting this started, and for the clear summary. Your description is correct: the Center for High School Success uses information from your SIS to build the ninth grade dashboards your team and our coach use to identify students who need support and to act on it quickly. That is the purpose, and we operate as a school official under FERPA to deliver it.
>
> One clarification so there are no surprises: like most programs, we evaluate whether our work is helping. We do that with de-identified and aggregate results only (for example, your school's on-track rate), never with identifiable student records, and we delete identifiable data when our partnership ends or whenever you ask.
>
> We are glad to work through TEC and the SDPC process. We will sign the Missouri NDPA, and we expect to have a general offer of terms on file so other Missouri districts can use the same agreement. When TEC reaches out, please have them contact Emily Phan, our Executive Technology Officer, who is copied here. Luke Allpress, who is helping us with agreement language and SIS integration, is also copied.
>
> We will send you a short summary of exactly what data we ask for and how it moves before anyone has to review a document.

## 2. The one-paragraph data summary for any district
::src James's collateral :: Mirrors the "Only the data needed" and "Who sees what" sections of James's Navigator collateral, with discipline moved to optional and the de-identified evaluation disclosed.
::src Emily's architecture :: Delivery is files by SFTP or secure upload in v1; nightly or weekly automated export is the target, scheduled upload is the floor.

> Here is what the integration involves, in plain terms. Your district sends us a file for each ninth grade cohort with student ID, name, grade level, course enrollments, course marks and credits by grading period, GPA, and attendance. Most districts set up an automated weekly export to our secure SFTP; if that is not possible yet, a scheduled upload each grading period works and we will help you automate it later. Your school team sees student-level dashboards with names. Our coaches see aggregate views unless you choose to give them more. Our program and research staff never see identifiable data. Identifiable data is deleted when the partnership ends or whenever you ask; we keep only de-identified and aggregate results to evaluate the program. The full terms are in our data privacy appendix, or we will sign your state's NDPA, whichever you prefer.

## 3. Asks for the Columbus City CTO review
::src Columbus City DSA :: Their Student Data Sharing Agreement (revised 3/17/2025) is the strictest document in hand: annual third-party security audit, $1M cyber liability, U.S.-only storage, documented access roster with logs, 90-day destruction, Ohio R.C. 3319.321, 3319.325–327, and Chapter 1347.
::src Conversation :: James (10/26): Columbus "has been very diplomatic, easy to talk to"; the plan is to be transparent, "we're trying to find the right language. We know you all have a high bar. Can we review this together?" Luke is available Nov 2 (not 1–2 p.m.), the morning of Nov 3, and Nov 4 (not 1–3 p.m.), Arizona time.

Ask for, in order:

1. Forty-five minutes with the CTO and whoever reviews data agreements for the district (privacy officer or counsel), between Nov 2 and Nov 4, with Luke on the call.
2. Confirmation that the Student Data Sharing Agreement dated 3/17/2025 is the current form, and whether the district would also accept the Ohio NDPA.
3. Their read on two specific points before the call: coach access to student-level data (Option A) versus aggregate only (Option B), and CHSS keeping de-identified results after termination for program evaluation.
4. Whether the district requires anything of CHSS coaches beyond the agreement (background checks, district onboarding, training).
5. Their board timeline from "agreement final" to "approved," so CHSS can work backward from the January start.

## 4. Asks for San Diego
::src San Diego CCAP :: The document in hand is the SDCCD–SDUSD College and Career Access Pathways agreement (dual enrollment), not a student data privacy agreement. Its Section V routes data through Cal-PASS Plus. SDUSD will use a different instrument for an outside nonprofit, almost certainly the California NDPA.
::src State law :: California Education Code § 49073.1 and the Student Online Personal Information Protection Act set required contract terms for student data. The California NDPA (v1.5) Exhibit G carries them.

Ask for:

1. The student data privacy agreement template SDUSD uses with outside partners that receive student-level data, since the CCAP agreement is the wrong instrument for this.
2. Whether SDUSD prefers the California NDPA or its own form, and who in the district signs it.
3. Whether the district's General Services Agreement and SOW format will be required for the accelerator, so CHSS can structure its "District responsibilities / CHSS responsibilities" sections to match.
4. The same two substantive points as Columbus: coach access and de-identified retention.

## 5. Two sentences for the superintendent-level emails
::src Conversation :: James (10/26): verbal yeses came from superintendents and heads of academics; CTOs are hearing about it afterward. This closes that gap in the acceptance email itself.

> Because the accelerator includes SIS integration, we will ask you within the first two weeks to name a technical contact and a data privacy contact, and we will schedule a short onboarding call with both before any data moves. We will sign your state's National Data Privacy Agreement or provide our own privacy appendix written to the same standard, whichever your district prefers.
