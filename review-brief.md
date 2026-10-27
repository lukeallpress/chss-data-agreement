# Adversarial review brief: CHSS data agreement drafts, v0.2 (Oct 27, 2026)

Live page with the same content and per-section source popovers: https://lukeallpress.github.io/chss-data-agreement/
Generated 2026-10-26 from the site source. Everything after the
instructions is the full text of the five pages, with each section's provenance shown as
an indented *Source* note so you can judge the reasoning, not just the words.

## What this is

The Center for High School Success (CHSS), a program of Stand for Children Leadership
Center, Inc. (a 501(c)(3); Stand also has a 501(c)(4) affiliate), coaches high schools on
ninth grade on-track rates. Its National 9th Grade Success Accelerator will bring on roughly
10 to 20 districts (about 50 schools) in January 2027, fully subsidized for an 18-month
Year 0 plus Year 1, with about 75 existing partner districts to migrate afterward. Scale goal:
300 LEAs and 1,000 schools in four years.

Acceptance is conditioned on **SIS integration**: districts send student-level data (IDs,
names, grade level, course enrollments, marks, credits, GPA, attendance) so CHSS can build
ninth grade dashboards in its new **Navigator** platform (Salesforce Experience Cloud on an
Azure/Fabric data platform, with AI-assisted ingestion and intervention suggestions). CHSS
also administers Belonging and Skills screeners to students and wants to keep de-identified,
aggregate results after a partnership ends to evaluate the program over time. Today's
process is de-identified quarterly uploads to Tableau; the new one is identifiable, weekly,
and automated.

Timeline that matters: cohort announced Dec 15, 2026; technical onboarding January through
February; data must flow before students arrive in August 2027. Columbus City Schools needs
about three months for board approval. The Navigator pilot starts in December 2026, before
any new agreement is signed. A Missouri partner district has already asked its consortium to
obtain the SDPC National Data Privacy Agreement (NDPA) with CHSS.

The drafts replace the data sections of CHSS's existing Agreement for Services (whose current
text keeps identifiable data for three years after termination and describes the feed as
"de-identified individual student data," both of which the drafts change).

## Your job

Review these drafts **as a district would**. That is the primary lens. The question is not
"is this well written" but:

1. **Would this district sign?** What would its CTO, privacy officer, counsel, data manager,
   and superintendent each object to, in their own words, and would that objection slow
   signature by weeks or stop it?
2. **Does the district feel supported in getting its data ready to share?** Is it clear what
   to send, how, how often, who does the work, and what help CHSS gives? Would a small rural
   district with one technology coordinator be able to do this? Would a large urban district's
   procurement office be able to route it?

Two secondary lenses, which also matter:

3. **CHSS-internal usability.** Pages D and E are working pages for the CHSS team. Are they
   human-readable and actually useful: can James paste from D into an email today, and can
   Jonah, Emily, and Tara make the decisions in E from what is on the page?
4. **Persuasion.** Page A is the case-making. Is it compelling to a superintendent and a
   board? What would make a skeptical district leader say "we want this" rather than "fine"?

Adopt the personas below one at a time. Each produces its own findings.

## Personas (adopt each, in turn)

- **District CTO / technology director, mid-size suburban district.** Cares about: security
  specifics, subprocessors, where data lives, SSO, logging, how the feed actually runs, who is
  on call when it breaks, what "two working sessions" really covers.
- **Student data privacy officer, large urban district (Columbus City or San Diego scale).**
  Cares about: FERPA basis, state statute (Ohio R.C. 3319.321/3319.325–327/1347; California
  Ed Code 49073.1 and SOPIPA; Arizona 15-1046 and 15-117; Missouri, Massachusetts, Utah),
  NDPA conformance, de-identification standard, retention after termination, research and
  publication, coach access, screeners and PPRA consent, parent rights.
- **District general counsel or board attorney.** Cares about: who the party is, the
  501(c)(4) affiliate, indemnity and liability, insurance limits and evidence, precedence
  between the MOU, Appendix A, and the NDPA, termination and survival, governing law,
  anything that must go to the board and how long that takes.
- **SIS / data manager, small rural district (one technology coordinator, PowerSchool or
  Infinite Campus or Synergy).** Cares about: can I actually produce every Required element
  accurately, what reports, what file format, what cadence, what if I can't automate, how
  much of my time, what happens when the grading scale changes, what the cleanup script is.
- **Superintendent / head of academics.** Cares about: value to schools, risk to the
  district, political exposure, what they are personally committing their staff to, whether
  the case-making is believable, what the board will ask.
- **Ninth grade team lead at a participating school.** Cares about: what they see in
  Navigator, whether the coach can see their students, screener consent conversations with
  parents, whether the data will be current on Tuesday.
- **CHSS staff reader (James, Emily, Tara).** For pages D and E only: is this usable as
  written, what is missing to act on it, what reads as jargon.

## Ground rules

- Cite the section number or heading for every finding (for example, "B §5.6" or "C A.10").
- Distinguish **legal errors** (the draft says something wrong or unenforceable) from
  **district preferences** (a district would push back but the draft is defensible) from
  **clarity problems** (right idea, unclear or missing detail) from **persuasion problems**.
- Do not rewrite the documents. Propose the smallest change that resolves each finding, and
  quote replacement language only when wording is the problem.
- U.S. K12 context. Where a point is state-specific, name the state.
- The drafts carry deliberate open choices (Option A/B coach access, discipline optional,
  $2M cyber, 60-day deletion, Option B default). Attack the reasoning in page E rather than
  re-deriving the choice; say if you would decide differently and why.
- Known gaps you do not need to rediscover: the AI model provider is not yet named; insurance
  limits await Stand's finance lead; the SOC 2 timeline is unknown; the Navigator December
  pilot predates any new agreement; the Missouri, Massachusetts, and Utah state exhibits are
  placeholders; James's existing one-pager already promises Option B to districts.

## What to return

Return Markdown with these sections, in this order:

1. **Would I sign?** One paragraph per persona: yes / yes with changes / no, and the one
   thing that most drives that answer.
2. **Findings**, ranked most severe first, each as:
   - *Where:* page letter and section.
   - *Who raises it:* persona.
   - *The objection, as they would say it:* one or two sentences in their voice.
   - *Type:* legal error / district preference / clarity / persuasion / internal usability.
   - *Effect on signature:* blocks / slows by weeks / friction only / none.
   - *Smallest fix.*
   - *Confidence:* high / medium / low, and why.
3. **Support gaps**: everything a district would still need from CHSS to get its data ready
   that the drafts do not provide or promise.
4. **Case-making**: what is compelling, what is flat, and the three changes that would most
   increase a superintendent's desire to join.
5. **Internal pages**: for D and E, what is unusable or missing for the CHSS reader.
6. **What would make me say yes**: per persona, the shortest list of changes that would move
   "no" or "yes with changes" to "yes."
7. **Three things the drafts get right** that should not be lost in revision.

Aim for precision over volume. A finding that would survive a district's counsel is worth
more than ten that would not.

---

# Page A. Case-making (goes up front; audience: superintendent, head of academics, board)

## A 9th Grade Navigator for Every School
    Source [James's collateral]: Built on James Arndt's "A 9th Grade Navigator (Dashboard) for Every School" (Oct 22, 2026). His headline, framing, and most of the first two sections are kept nearly verbatim.
    Source [Conversation]: Jonah (10/26): case-making goes up front, "we're having to sell ourselves more than some mega vendor," and it may be repeated inside the agreement's "what CHSS will do" section. Emily (10/26): lead with the case before the agreement.

Syncing your Student Information System (SIS) with CHSS Navigator gives your ninth grade team timely, accurate data through clear visualizations and a dashboard that updates automatically. Your team can analyze, discuss, and intervene in minutes, without running reports, downloading files, and entering formulas. Most districts don't have a ninth grade dashboard like this, or the time and budget to build one. CHSS builds and maintains it for you.

### The cost of doing it by hand
    Source [James's collateral]: Verbatim from James's draft, including the three-step routine and the 20-to-30-minute figure.
    Source [Conversation]: James (10/23): "we waste 20 minutes in every coaching session running the Synergy report, exporting, opening, entering a bunch of Excel formulas." Only 20 of 178 partner schools had submitted Q1 data as of 10/23.

Without an integration, almost every coaching session starts the same way:

1. The ninth grade lead runs a report from the SIS.
2. The report is exported to Excel.
3. The lead and coach add formulas to flag which students are failing one or two courses.

That routine eats 20 to 30 minutes of a 60-minute session. Half the hour goes to clerical work instead of kids, and the data is often a full grading period old by the time anyone acts on it.

District staff carry a burden too. Each quarter, CHSS asks a district data specialist to pull a large download and upload it to a secure location. That takes time from your most technical people, and the data is months old by the time it's used. SIS integration makes all of it automatic: no emails, no manual pulls, no file transfers.

### What SIS integration gives your team
    Source [James's collateral]: First five bullets are James's.
    Source [Conversation]: Last two bullets added from the 10/19 and 10/23 calls: Tara and Jonah on longitudinal tracking (on-track through CTE, dual credit, graduation) and on end-of-year data arriving in October today, which makes it "really hard to evaluate our staff, evaluate our impact, plan for the next school year."

Student data flows securely from your SIS into CHSS Navigator, where CHSS builds the ninth grade dashboards your team uses. Teams stop building the data and start using it.

- **Time back for kids.** The 20 to 30 minutes once spent preparing data goes back to talking about students.
- **Current data.** Friday's data for Tuesday's conversation, not last quarter's.
- **Accurate data.** No manual exports or formulas means no copy errors or broken spreadsheets.
- **Faster action.** Teams spot students failing one or two courses and plan support in the same meeting.
- **Visible progress.** Teams can see whether each intervention is working and adjust before the next grading period.
- **A view past ninth grade.** As your cohort moves on, Navigator keeps following it: on-track persistence in 10th grade, CTE course sequences, dual credit, graduation. You see whether the ninth grade work held, and so does your board.
- **End-of-year answers in June, not October.** Automated feeds mean your on-track results are ready when you plan the next year, not after it has started.

### What it gives your district
    Source [Conversation]: The "support you to do something" reframe from the 10/19 call. Jonah: "instead of being seen as 'we're asking you to pretty please do something,' we're actually offering support." Luke: the first question to any district is whether its SIS data lands in a warehouse it owns every night; most who do "are doing the fun stuff."
    Source [Luke's experience]: Setting up SchooLinks and other nightly feeds at AFUHSD: once automated, "I don't think about it at all anymore"; a failure notice arrives if the receiving server is down.
    Source [AFUHSD precedent]: The executed-copy promise comes from the ASU-Helios thread (Mar 2026), where neither the assistant superintendent, the deputy superintendent, finance, nor the data team could find the district's own signed DSA a few years on.

Most districts run reports by hand because nobody has had the time to set up the alternative. The integration work we do together changes that:

- **We set it up with you.** CHSS technical staff meet with your data team, map your SIS exports to the Navigator format, and set up the automated feed. For most districts this is two working sessions.
- **You own your data.** If your district doesn't already keep a nightly copy of its SIS data in a place you control, we'll help you get there. Once you have it, every future partner, dashboard, and analysis gets easier, not just ours.
- **Nothing to remember.** Once the feed runs, no one on your staff runs a report for CHSS again. If a transfer fails, our system notices and we follow up.
- **Clean records.** You get an executed copy of every agreement, indexed, and a reminder before anything expires.

### Built to protect student privacy
    Source [James's collateral]: Opening sentence and "your student data remains your district's property" are James's.
    Source [Drafting choice]: Discipline removed from "only the data needed." James's draft and Emily's architecture both list it; Tara (10/19) said behavior data is rarely received and isn't needed for on-track; Luke (10/26) called discipline "the most tightly held thing." It stays available as an optional element in the agreement.
    Source [Drafting choice]: "Used for one purpose" now carries a second sentence disclosing de-identified evaluation, so the longitudinal work is never a surprise. James's original ("and nothing else") silently excluded it.
    Source [Lewis County]: A Missouri partner district's technology coordinator has already asked its consortium to obtain the NDPA with CHSS, so the NDPA commitment is stated here up front.

SIS integration is governed by a data sharing agreement with your district and designed to meet FERPA and your state's student privacy requirements. CHSS will sign the National Data Privacy Agreement (NDPA), including your state's version, or provide its own appendix written to the same standard. Your student data remains your district's property, and your district decides who can see it.

- **Only the data needed.** CHSS receives student ID, name, grade level, course grades and credits, and attendance.
- **Used for one purpose.** Identifiable student information supports ninth grade success work in your schools and nothing else. CHSS keeps only de-identified and aggregate results to evaluate and improve the program.
- **Deleted when you say so.** When the partnership ends, or whenever you ask, identifiable data is destroyed and we certify it.

### Who sees what
    Source [James's collateral]: Table structure and the school-team row are James's. His draft already states that CHSS coaches and staff see "aggregate data only."
    Source [Conversation]: The coach row is the open A/B question from 10/26. Jonah leaned toward the "less intrusive approach" with screen-share; James wanted to ask for access and fall back. Both options are shown here; the agreement draft carries the clause language for each.
    Source [Luke's experience]: AFUHSD's Teach For America agreement (2025–26) accepted the partner's coach seeing student-level data on the basis that the coach is the only partner viewer and is acknowledged as a FERPA school official. The same district's first ask in 2025 was to strip student names while keeping the linking key the partner needed.

Student names live in Navigator for one reason: so the educators responsible for a student know who needs support and can act. Role-based permissions decide who can see them.

| Who | What they see | Why |
|---|---|---|
| Your school team (individual logins) | Student-level records: names, course performance, attendance | To identify students, build intervention plans, and monitor progress kid by kid |
| CHSS coaches | **Option B (default):** aggregate data only: on-track rate, course failures, attendance by group. In coaching sessions, your team lead shares the screen. **Option A (district may elect):** student-level view for the schools they coach, under the same agreement and training as your staff, with every access logged. | To coach your team and measure impact |
| CHSS program and research staff | De-identified and aggregate data only | To evaluate and improve the program across the network |

Records are matched using a consistent unique student identifier, so Navigator stays accurate as students change classes, schedules, and schools.

---

# Page B. District commitments: replacement Sections Five and Six of the Agreement for Services

## Agreement for Services: Sections Five and Six (replacement draft)
    Source [James's MOU draft]: Replaces Section Five ("Confidential Information") and Section Six ("Data Access and Sharing") of the CHSS Accelerator Agreement for Services draft (Year 0 Readiness + Year 1 Implementation). Section numbering, party names ("CHSS," "Organization," "District"), and defined-term style follow that document.
    Source [Conversation]: James (10/26): the existing data section "needs to be entirely trashed and redone"; what is needed is to "state our expectations as much as anything else." Jonah: the deliverable is "what they're committing to give, what we're committing to take care of, and why this is worth it."
    Source [Drafting choice]: Three things in the current draft conflict with Navigator and will be marked up by any privacy officer: it describes the feed as "de-identified individual student data" while Navigator shows names to school teams; it keeps identifiable data for three years after termination; and it has no FERPA basis, breach, subprocessor, location, or audit terms. This draft fixes all three.

*Drafting note: bracketed fields are completed per district. Conforming edits to Sections Three and Eight are listed at the end.*

### Section Five: Student Data Privacy and Security
    Source [Drafting choice]: Section Five becomes the short, binding statement of the relationship and points to the appendix (or the NDPA) for the detailed terms, so the body of the agreement stays readable for the academic signers.

#### 5.1 Purpose and relationship
    Source [FERPA]: School official exception, 34 C.F.R. § 99.31(a)(1)(i)(B): a contractor or other party to whom the institution has outsourced services may receive education records without consent if it performs a service the institution would otherwise use employees for, is under the institution's direct control as to use and maintenance, and is subject to the redisclosure limits of § 99.33(a).
    Source [Luke's experience]: On the 10/26 call: "there's a legitimate educational reason for you all to be looking at this data," and the coach already hears student names in every kid-talk today; the agreement "operationalizes" a threshold the district has already crossed.
    Source [AFUHSD precedent]: Luke's own test from the 360training review (Jan 2026): a partner is a FERPA school official when it is "an integrated part of learning" that the district facilitates, versus a direct student–vendor relationship like ACT or ASVAB.
    Source [AFUHSD precedent]: The sentence on parental consent is deliberate. AFUHSD's GCU priority-acceptance program (2025) had a board-approved agreement but no scalable consent mechanism and produced about one student in year one. Districts should not go looking for a consent process the school official exception doesn't require.
    Source [af-dpa]: knowledge/law/ferpa.md (captured 2026-10-26): PTAC adds a fourth element, that the party "has been determined to meet the criteria set forth in the school's or district's annual notification of FERPA rights for being a school official" (§ 99.7(a)(3)(iii)); many districts' annual notices name only employees and board contractors. The last sentence below asks the District to close that gap. The studies exception (§ 99.31(a)(6)) is the alternative basis for evaluation work, but it requires destruction when the study ends, which is why evaluation here rests on de-identified data instead.

The District and the Center for High School Success ("CHSS"), a program of Stand for Children Leadership Center, Inc. ("Organization"), a nonprofit organization exempt under section 501(c)(3) of the Internal Revenue Code, share student data under this Agreement so that CHSS can provide ninth grade success coaching, the CHSS Navigator platform, and on-track analytics to the District's participating schools (the "Services").

In providing the Services, CHSS and Organization act as a "school official" with a "legitimate educational interest" under the Family Educational Rights and Privacy Act (FERPA), 34 C.F.R. § 99.31(a)(1)(i)(B). CHSS performs an institutional service for which the District would otherwise use its own employees, is under the District's direct control with respect to the use and maintenance of education records, and will not redisclose student data except as this Agreement permits. The Services do not require parental consent under FERPA. The District will confirm that its annual notification of FERPA rights includes, among the criteria for school officials with a legitimate educational interest, contractors and organizations to which the District has outsourced institutional services.

#### 5.2 Governing privacy terms
    Source [Lewis County]: A partner district in Missouri has already routed CHSS through its consortium (TEC via MOREnet) and the SDPC Resource Registry to obtain the NDPA. Districts in Arizona, Ohio, California, Massachusetts, Utah, and Missouri have state NDPA versions; this clause lets each district choose its instrument without renegotiating.
    Source [SDPC NDPA]: The NDPA is the Student Data Privacy Consortium's national agreement; state alliances publish versions with a state exhibit. AFUHSD signs vendors onto the Arizona Standard Version 1.2.
    Source [Drafting choice]: Order of precedence: whatever the district actually signed controls. Avoids a district's counsel having to reconcile two documents.

All handling of student data under this Agreement is governed by the CHSS Data Privacy and Security Appendix (Appendix A). At the District's election, the Parties will instead, or in addition, execute the Student Data Privacy Consortium's National Data Privacy Agreement (NDPA) in the version adopted in the District's state, in which case the NDPA controls as to any conflict with Appendix A. If Appendix A conflicts with the body of this Agreement, Appendix A controls as to student data.

#### 5.3 Definitions
    Source [FERPA]: De-identified Data tracks 34 C.F.R. § 99.31(b)(1): records may be released without consent after removal of all personally identifiable information, provided the institution has made a reasonable determination that a student's identity is not personally identifiable, taking into account other reasonably available information.
    Source [James's MOU draft]: "Confidential Information" is retained from the current Section Five and narrowed to the defined terms below.
    Source [Conversation]: "Cohort" implements the 10/23 decision with James: start with ninth grade and "grow the dashboard each year after that" so the cohort can be followed into 10th grade, CTE sequences, and graduation.

- **Student Data** means any information from the District's education records that identifies, or could be used to identify, a student, including the elements listed in Exhibit D-1. Student Data is Confidential Information.
- **Screening Data** means responses and scores from the CHSS Belonging Screener and Skills Screener administered to students at participating schools. Screening Data is Student Data.
- **De-identified Data** means Student Data or Screening Data from which all personally identifiable information has been removed in accordance with 34 C.F.R. § 99.31(b)(1), such that a reasonable person in the school community who does not have personal knowledge of the relevant circumstances could not identify the student.
- **Aggregate Data** means statistics computed across groups of students, with any group smaller than ten students suppressed.
- **Navigator** means the CHSS web platform through which the Services are delivered.
- **School Team** means the District employees at a participating school who are responsible for ninth grade students, as designated by the District.
- **Coach** means the CHSS employee assigned to support a participating school.
- **Cohort** means the ninth grade students enrolled at a participating school in a school year in which the Services are provided.

#### 5.4 Who may see student-level data
    Source [James's collateral]: James's "Who sees what" table already commits that "CHSS coaches and staff" see "aggregate data only." Option B is that commitment in contract form.
    Source [Conversation]: 10/26: Jonah asked for both options drafted so Columbus City can react; "is it true that if we didn't ask for that, it would be easier? For some." James: ask for A and let their lawyers say no. Luke: aspirationally ask, be ready with Plan B, because the Phoenix Union experience with Teach For America mentors was six months of fingerprint and onboarding fights.
    Source [AFUHSD precedent]: Luke's review of the renewed TFA template (Feb 2026): "as long as it's just the Coach that's going to see the data then it's covering it, acknowledging them as FERPA proxies." That is Option A's basis: one named role, acknowledged as a school official.
    Source [Drafting choice]: B as default with a one-sentence district opt-in to A keeps one protocol for CHSS while letting friendly districts turn on A without renegotiation. If James's collateral has already been shown to districts, B is the only position consistent with it.

School Team members designated by the District may view student-level records, including names, for their school, to identify students, plan interventions, and monitor progress.

CHSS program, research, and leadership staff, and Organization staff, may view only De-identified Data and Aggregate Data.

**Coaches.** *One of the following applies; the District's election is recorded in Exhibit D-3.*

> **Option A (coach has student-level access).** The Coach assigned to a participating school may view student-level records, including names, for that school only, to support the School Team. Coaches are CHSS employees bound by Appendix A, complete annual FERPA and privacy training, have passed a background check, and are subject to the same access logging as District users. The District may revoke a Coach's access at any time by written notice.

> **Option B (coach has aggregate access; default).** Coaches view Aggregate Data for the schools they support. During coaching sessions, a School Team member logged into Navigator shares the student-level view. Coaches do not hold student-level logins. The District may elect by written notice to grant a Coach student-level access for a school, in which case the conditions in Option A apply.

#### 5.5 Permitted use and restrictions
    Source [James's MOU draft]: Builds on the current Section Five "Permitted Use and Restrictions" (use solely to perform services and evaluation; access limited to those performing work; no third-party disclosure).
    Source [SDPC NDPA]: Mirrors NDPA Article IV prohibitions: no sale, no targeted advertising, no building a profile except to further the educational purpose.
    Source [Conversation]: James (10/23): Stand is both a 501(c)(3) and a 501(c)(4), "so there doesn't actually have to be something wrong for people to raise a stink." The advocacy clause answers the question before a board member asks it.
    Source [Drafting choice]: The evaluation sentence is where the current draft's "Whenever practicable, CHSS will use aggregated or de-identified data" becomes a rule rather than an aspiration: identifiable data for the Services only; de-identified and aggregate data for evaluation.

CHSS and Organization will use Student Data solely to provide the Services to the District. CHSS and Organization will not: (a) sell, rent, or trade Student Data; (b) use Student Data for targeted advertising or marketing to students, parents, or staff; (c) build a profile of a student for any purpose other than the Services; (d) use Student Data in any advocacy, lobbying, political, or fundraising activity of Organization or any affiliated entity, including any entity organized under section 501(c)(4); or (e) disclose Student Data to any third party other than a subprocessor listed in Appendix A, except as required by law.

CHSS may create and retain De-identified Data and Aggregate Data to evaluate and improve the program, including following Cohort outcomes over time. CHSS will not attempt to re-identify any student and will not publish any result that could identify a student or, without the District's written consent, the District.

#### 5.6 Return and destruction
    Source [Columbus City DSA]: "Company shall destroy or return to the District all educational records created, received, or maintained pursuant to the contract/agreement within ninety days" of termination. Term is co-terminus with the contract and ends only when data is destroyed or returned.
    Source [SDPC NDPA]: Article IV "Disposition of Data": dispose of or return data within sixty days of written request on an agreed schedule; the duty does not extend to de-identified data; the LEA may use the Directive for Disposition of Data form (Exhibit D) with no further notice.
    Source [AFUHSD precedent]: Luke rejected "may retain copies in the ordinary course of business" in a 2026 dual-enrollment review and pasted the NDPA disposition clause in its place.
    Source [James's MOU draft]: Replaces the current draft's three-year post-termination retention, which no partner district on the call list will accept.
    Source [Conversation]: James (10/23): CHSS is "perfectly okay to delete the de-identified student data" but wants to keep that "Agua Fria High School went from 60% on track to 72%." Luke: "That's fine. That's a different thing."
    Source [af-dpa]: knowledge/sdpc/article-crosswalk-v1-2-to-v2-1.md: NDPA v1.2 IV.6 is sixty days from a written request and, at termination, "after providing the LEA with reasonable prior notice" with no deadline; v2 4.6 is "within sixty (60) days of termination." Sixty days at termination is used here so the clause satisfies v2, Columbus (ninety), and the stricter districts (Beaverton: sixty days from expiration). knowledge/practice/vendor-negotiation.md: backups "expire on the vendor's documented rotation," with "an outside date" and "certification when the outside date passes."

On the District's written directive at any time, CHSS and Organization will return or destroy the Student Data specified within sixty days, on a schedule agreed with the District. Within sixty days after this Agreement ends, CHSS and Organization will destroy or return to the District all Student Data and Screening Data, including copies held by subprocessors, and will certify destruction in writing; copies in encrypted backups expire on the documented rotation, not to exceed ninety days, are never restored to production, and are certified as expired when that date passes. De-identified Data and Aggregate Data are not subject to this subsection.

#### 5.7 Records of this Agreement
    Source [AFUHSD precedent]: ASU-Helios consortium thread (Mar 2026): the district could not locate its own executed DSA; a partner that supplies an indexed executed copy and a renewal reminder removes a real pain point.
    Source [Luke's experience]: AFUHSD's own agreement inventory lives in the SDPC registry and BoardDocs; most districts have nothing comparable for non-vendor partners.

CHSS will provide the District an executed copy of this Agreement and Appendix A within ten business days of signature, and written notice at least ninety days before this Agreement or Appendix A expires.

### Section Six: Data Access and Sharing
    Source [James's MOU draft]: Keeps the current Section Six's purpose sentence and liaison block; replaces the "de-identified individual student data" framing, the element list, the cadence, and the delivery language.
    Source [Conversation]: Luke (10/26): the district's technical and privacy people must be at the table early, "so that they're not caught with their pants down six months later when they're like, okay, now send the data to Stand."

Successful implementation requires timely access to actionable data that allows School Teams, school leaders, the District, and CHSS to identify students needing support, monitor progress, compare outcomes, and assess the effectiveness of supports.

#### 6.1 District contacts and onboarding
    Source [Conversation]: 10/23 (James and Luke) and 10/26 (all): verbal yeses came from superintendents and heads of academics, not CTOs; James met one CTO so far. The contact designation and the onboarding call are the mechanism that forces the CTO/privacy conversation before data moves.
    Source [James's MOU draft]: The current draft already has a "District Data/IT Liaison" block; this subsection makes naming that person a dated obligation and adds the privacy contact.

Within fifteen business days after signature, the District will designate (a) a technical contact responsible for the data feed, (b) a privacy contact (data privacy officer, technology director, or counsel) responsible for Appendix A, and (c) a program contact for each participating school, and will record them in Exhibit D-3. CHSS will schedule an onboarding call that includes the technical and privacy contacts before any Student Data is transferred.

#### 6.2 Data provided by the District
    Source [James's MOU draft]: The current element list (demographics, course enrollment and master schedule, credits, course performance and GPA, attendance, behavior and discipline "as permitted," summer school, other agreed indicators) is kept, re-sorted into required and optional in Exhibit D-1.
    Source [Conversation]: Tara (10/19): course performance, GPA, credit accrual, attendance; behavior "we typically don't get." James (10/19): the three Synergy reports a school actually runs are GRD 401, GRD 402, and the MST transcript.
    Source [Emily's email]: "Right sizing our data request: what is the minimum practical dataset we should request initially versus additional data we might pursue later?" Required core is kept small; everything else is optional.
    Source [AFUHSD precedent]: In AFUHSD's feeder-district DSA (May 2025) the data team struck an element the district could not produce accurately. Expect district data teams to do the same; a short required list survives that review.

The District will provide the elements marked Required in Exhibit D-1 for each Cohort, and may provide the elements marked Optional at its discretion. The District will provide data as it exists in its student information system; CHSS will report apparent errors to the technical contact and will not alter source data.

#### 6.3 Scope of students and years
    Source [Conversation]: James (10/23): "let's do it in ninth grade, but grow the dashboard each year after that. So when they become 10th graders, we continue importing their data." Luke: "it is an arbitrary difference" technically; the value is in following the cohort.
    Source [Drafting choice]: Written so a district that balks can strike the second sentence and keep a ninth-grade-only feed without touching anything else.

Student Data covers all ninth grade students at participating schools. For each Cohort, the District will continue to provide the Required elements for those students in subsequent school years through graduation or exit, for as long as this Agreement is in effect, so that on-track outcomes can be followed over time.

#### 6.4 Student identifier
    Source [James's collateral]: "Records are matched using a consistent unique student identifier."
    Source [Emily's architecture]: The platform's identity-matching step lists district ID, state ID, and "probabilistic matching." A deterministic ID in every feed makes probabilistic matching unnecessary for linking.
    Source [Luke's experience]: Two de-identification methods used at AFUHSD (10/19 call): a deterministic transformation of the student ID, or a growing mapping table from hashed to random IDs. Either produces a stable pseudonymous identifier a district can send instead of its real ID.
    Source [af-dpa]: agents/operational-context.md: "Pseudonymous or 'anonymized' student-level rows can remain linkable student data, especially when the same student is tracked over time." The last sentence below says so, which keeps a pseudonymous feed inside the agreement's protections rather than outside them.

Each record will include the District's student identifier (and the state student identifier where available) so that records can be matched consistently across feeds and years. A District that prefers not to send its student identifier may instead send a stable pseudonymous identifier that it generates and maintains, provided the same identifier is used in every feed. Records carrying a pseudonymous identifier remain Student Data under this Agreement.

#### 6.5 Delivery method and cadence
    Source [Emily's architecture]: v1 of the CHSS data platform ingests periodic files (Excel, CSV, TXT) by SFTP or secure upload, "quarterly/semester or more frequent." No vendor API in v1.
    Source [Conversation]: Luke's ranking (10/19): SIS vendor feed direct to CHSS first, district SFTP second, Clever/ClassLink last ("this isn't OneRoster data"). Luke (10/23): a menu from "run these five reports and a Python cleanup script" up to a nightly automated export.
    Source [James's MOU draft]: The current draft's "within two weeks after the end of each marking period" is kept as the floor; weekly is the target because the coaching model needs Friday's data on Tuesday.
    Source [James's MOU draft]: The current Section Three already obligates the District to "make grades, attendance, and other agreed-upon key indicators available at least weekly." This subsection is how that happens.

The District will choose one of the delivery tiers in Exhibit D-2. The target for every District is Tier 1 (automated feed) by the end of technical onboarding. Tier 2 (scheduled secure upload) is acceptable for a District that cannot yet automate, with CHSS support to move to Tier 1 when ready. Whatever the tier, the District will provide an initial load at onboarding and updates no later than two weeks after the end of each marking period, the school year, and summer school; weekly updates during the school year are strongly preferred so that coaching conversations use current data.

#### 6.6 Changes affecting the feed
    Source [Luke's experience]: Running district feeds to outside partners: SIS vendor changes, grading-scale changes, and term-structure changes are what break them.
    Source [James's MOU draft]: Extends the current Section Three notice obligation ("data-system changes that may affect implementation") with a lead time.

The District will notify CHSS at least thirty days before a change in student information system, grading scale, or term structure that would affect the feed.

#### 6.7 Screeners
    Source [PPRA]: Protection of Pupil Rights Amendment, 20 U.S.C. § 1232h: surveys funded or administered through a school that touch protected categories (including psychological problems and certain attitudes) require parental notice and, in some cases, opt-out or consent. A belonging screener can reach those categories.
    Source [Emily's email]: Navigator must "explicitly cover the Belonging and Skills screeners we administer, including the collection, storage, analysis, and use of student-level screening data."
    Source [James's MOU draft]: The current Section Three already obligates the District to "administer CHSS or comparable belonging and skills screeners." This subsection makes the District the approver and notice-giver, which is where PPRA puts the responsibility.
    Source [af-dpa]: knowledge/law/ppra-cipa-other-federal.md, quoting the Department of Education's Student Privacy Policy Office letter of Aug 26, 2026: when schools "use behavioral health screeners that probe students' emotional or psychological states, they must ensure that written parental consent is obtained prior to administration," and "the opt-out provisions in PPRA do not apply as a way of securing parental consent." Arizona A.R.S. § 15-117 adds fourteen categories and seven days' advance notice. A belonging screener can reach those categories, so the clause says "consent" and not only "notice."

The District will review and approve the CHSS Belonging Screener and Skills Screener before they are administered; will provide any parent notice, opt-out, or written consent required by District policy, by the Protection of Pupil Rights Amendment (20 U.S.C. § 1232h), or by state law; and will administer the screeners through the School Team. CHSS will provide the full content of each screener to the District for that review and will not add questions without the District's approval. Screening Data is Student Data for all purposes of this Agreement.

#### 6.8 Navigator users
    Source [SDPC NDPA]: Districts remain responsible for their own users' credentials and for prompt notice of role changes; the NDPA places account-management duties on the LEA for its staff.
    Source [Columbus City DSA]: District duties include "take reasonable precautions to secure usernames, passwords, and any other means of gaining access to the service."

The District will designate which School Team members receive Navigator logins and will notify CHSS within five business days when a user's role changes or ends. District users are responsible for safeguarding their credentials.

#### 6.9 CHSS integration support
    Source [Conversation]: Luke (10/26): "Let's send, Luke will have a conversation with your data nerds for two calls, set up a Python system that can clean and refine your data and send it via SFTP." James (10/26): "it's almost like another form of coaching we're going to offer."
    Source [Luke's experience]: Monitoring: a daily failure report is what makes an automated feed trustworthy; the district should never be the one to notice a missed transfer.

CHSS will provide technical assistance to the District's technical contact to establish the data feed, including documentation of the file specification, mapping of the District's exports to it, a cleanup script where needed, and up to two working sessions. CHSS will monitor the feed and notify the technical contact when a transfer fails or expected data is missing.

#### 6.10 Timeline
    Source [Conversation]: 10/23 and 10/26: winners announced by Dec 15; technical onboarding January through February; "four or five months of let's get this set up before students start." James: Columbus City needs about three months for board approval.
    Source [James's MOU draft]: Year 0 is the readiness period; "data access and reporting setup" is already listed among Year 0 activities.

The District will complete technical onboarding, including a successful initial load, by [end of Year 0 month 2], so that the Services are fully operational before [the first day of Year 1 instruction].

**District Data/IT Liaison:** [TO BE COMPLETED] · **Privacy contact:** [TO BE COMPLETED]

### Exhibit D-1: Data elements
    Source [James's MOU draft]: All elements from the current Section Six appear here; the change is the Required/Optional split.
    Source [James's collateral]: James's "only the data needed" list (student ID, name, grade level, course grades, attendance, discipline) with discipline moved to Optional.
    Source [Emily's architecture]: Input categories on the platform diagram: student information, grades, attendance, discipline, other optional (assessments, state tests, program participation).
    Source [Conversation]: Luke (10/19): attendance, discipline, EL, and IEP data "don't belong in rostering tools"; discipline is the element most likely to draw objections.

| Element | Required / Optional | Notes |
|---|---|---|
| District student identifier (state identifier also requested) | Required | Stable across years; see 6.4 |
| Student name (first, last) | Required | Visible to the School Team only; see 5.4 |
| Grade level, school, enrollment status and dates | Required | Entry and exit dates support Cohort tracking |
| Course enrollments by term (course code, title, section) | Required | Teacher of record optional |
| Course marks by grading period and final marks | Required | Include grading scale or pass/fail flag |
| Credits attempted and earned by term | Required | Core of the on-track calculation |
| Cumulative GPA | Required | Weighted and unweighted where both exist |
| Attendance: daily absences and tardies; period absences where available | Required | Chronic absence computed by CHSS |
| Summer school enrollment, completion, credits, and outcomes | Optional | From the current draft |
| Demographics (race/ethnicity, gender, EL, IEP/504, economic status) | Optional | For subgroup reporting at the District's election |
| Discipline (incidents, referrals, outcomes) | Optional | Not required for on-track |
| Assessments, state test scores, program participation | Optional | |
| Date of birth | Optional | Only where identifiers are unavailable for matching |
| Screening Data (Belonging, Skills) | Collected by CHSS under 6.7 | |

### Exhibit D-2: Delivery tiers
    Source [Emily's architecture]: Tier 1 and Tier 2 are the two inputs the v1 platform supports (SFTP; secure file upload).
    Source [Conversation]: Tier 3 reflects Luke's preferred route (10/19): "if you use one of the top five SIS, we have an API route built out with them where you don't even have to think about it." Listed because it is the best privacy posture (no files in the middle) even though v1 does not ingest it.
    Source [Luke's experience]: Tier 2 is the "least prepared district" path from 10/23: "here's the five reports you have to run every week, put them in this spot, and here's a little Python snippet that will clean them up."

| Tier | How it works | Who does what | Cadence |
|---|---|---|---|
| Tier 1: Automated feed (target) | The District's SIS or data warehouse exports the specified files on a schedule and transfers them to CHSS by SFTP. | CHSS provides the specification, credentials, and setup support. The District schedules the job. | Nightly or weekly |
| Tier 2: Scheduled secure upload (floor) | District staff run the specified reports and upload them to the CHSS secure portal, using a CHSS-provided cleanup script where needed. | CHSS provides the report list for the District's SIS and the script. The District uploads on schedule. | Every marking period at minimum; monthly preferred |
| Tier 3: SIS vendor connection (where available) | The SIS vendor provides a read-only API or scheduled export directly to CHSS. | CHSS and the vendor configure it; the District authorizes it. | Nightly |

### Exhibit D-3: District elections and contacts
    Source [Drafting choice]: Collects every per-district choice in one place so the body of the agreement is identical for every district, which is what makes an Exhibit E general offer under the NDPA workable later.

| Item | District election |
|---|---|
| Privacy instrument (5.2) | ☐ Appendix A ☐ State NDPA ☐ Both |
| Coach access (5.4) | ☐ Option A ☐ Option B |
| Delivery tier (6.5) | ☐ Tier 1 ☐ Tier 2 ☐ Tier 3 |
| Cohort tracking beyond ninth grade (6.3) | ☐ Yes ☐ Ninth grade only |
| Optional elements provided (D-1) | [list] |
| Technical contact | [name, title, email, phone] |
| Privacy contact | [name, title, email, phone] |
| Program contact(s) | [name, school] |

### Conforming edits elsewhere in the Agreement
    Source [James's MOU draft]: Section Three, District bullets 8 and 9, and Section Eight's insurance paragraph are the only other places the current draft touches data.
    Source [Columbus City DSA]: Cyber liability of at least $1,000,000 is a stated requirement; Section Eight currently promises only "reasonable liability insurance" and a certificate on request.
    Source [af-dpa]: knowledge/practice/dpa-review-checklist.md: "$1M for directory-only, $2M+ for SIS, assessment, special education or health data"; Beaverton requires $2,000,000 per claim and aggregate "when staff or student information is exchanged." Grades, attendance, and identifiers put CHSS in the $2M tier. Confirm current limits with Stand's finance lead before this number goes out.

- **Section Three, District agrees:** replace "Make grades, attendance, and other agreed-upon key indicators available at least weekly in a user-friendly dashboard or other accessible format" and "Provide CHSS and participating school teams with timely, actionable data ... in accordance with Sections Six and Seven" with a single bullet: "Provide Student Data as described in Section Six and Exhibit D-1, through the delivery tier elected in Exhibit D-3."
- **Section Three, CHSS agrees:** replace "Protect Confidential Information and use student data only as permitted by this Agreement and applicable law" with "Protect Student Data as provided in Section Five and Appendix A, and provide the integration support described in Section 6.9."
- **Section Eight:** add after the certificate-of-insurance sentence: "Organization maintains cyber liability insurance of not less than $2,000,000 per claim, as further described in Appendix A."
- **Section Nine, Notices:** add the privacy contact from Exhibit D-3 as a required notice recipient for matters under Appendix A.

---

# Page C. CHSS commitment to privacy and security: NDPA posture, Appendix A, system specifications

## CHSS Commitment to Student Data Privacy and Security
    Source [Conversation]: Jonah (10/26): the second deliverable is "our commitment to data privacy and security" plus "a system specifications document ... based on the required specifications by the districts that we're trying to contract with," set so CHSS is "compliant no matter what a district asks." James (10/23): a "system improvement plan" of what CHSS must build to meet district agreements.
    Source [Drafting choice]: Three parts: a short NDPA posture statement for districts that use the national agreement; Appendix A, CHSS's own terms, mapped to the NDPA's structure and set at the Columbus City Schools bar; and a one-page system specification a district CTO can read in five minutes.

This commitment has three parts. Part A states how CHSS will work with the National Data Privacy Agreement. Part B is Appendix A, CHSS's own privacy and security terms, which apply where a district does not use the NDPA and which track its structure. Part C is the system specification a district's technology office reads before signing.

### Part A: NDPA posture statement
    Source [Lewis County]: A Missouri partner district's technology coordinator wrote on 10/26 that she had asked her consortium (TEC via MOREnet) and the SDPC Resource Registry to obtain an NDPA with CHSS. The NDPA will arrive whether or not CHSS writes its own appendix.
    Source [SDPC NDPA]: Exhibit E (General Offer of Privacy Terms) lets a provider extend an agreement it has signed with one LEA to any other LEA in the same state that subscribes; the subscribing LEA signs Exhibit E rather than negotiating anew.
    Source [Luke's experience]: AFUHSD extends other districts' signed NDPAs to itself through Exhibit E routinely; each vendor file holds "the DPA from another district, and then the Exhibit E attachment signed by either me or Lauren."
    Source [Drafting choice]: Naming the Provider, the Service, and Provider staff up front answers the first three questions a consortium reviewer asks and settles that coaches are inside the agreement.
    Source [af-dpa]: knowledge/sdpc/exhibit-e-general-offer.md and resource-registry.md (captured 2026-10-26): Exhibit E is "a one-signature piggyback" that extends only privacy terms, within one state, for three years from the provider's signature; a subscribing district "must deliver notice of acceptance." Registry rows are created by districts, not providers ("One row = one district + one resource"), and the originating district uploads "the signed agreement file and a standalone Exhibit E file." So CHSS's job is to sign promptly and hand the first district in each state a clean standalone Exhibit E, not to "list itself."
    Source [af-dpa]: knowledge/sdpc/ndpa-structure.md: the v1.2 "Provider" definition is "provider of digital educational software or services ... for the digital storage, management, and retrieval of Student Data," a strained fit for a coaching nonprofit; the school-official recital in Article I is the real footing, which is why Section 5.1 of the Agreement states it independently.

The Center for High School Success (CHSS), a program of Stand for Children Leadership Center, Inc., will execute the Student Data Privacy Consortium's National Data Privacy Agreement (NDPA), including any state-specific version and exhibits adopted in the District's state, on request from any partner district or its privacy consortium. With the first executed NDPA in each state, CHSS will sign the General Offer of Privacy Terms (NDPA Exhibit E) and provide the originating district a standalone copy for the SDPC Resource Registry, so that other districts in that state may subscribe to the same terms by accepting Exhibit E and delivering notice of acceptance.

For purposes of the NDPA: the **Provider** is Stand for Children Leadership Center, Inc. (CHSS program); the **Service** is CHSS Navigator and the ninth grade success coaching it supports; **Provider staff** include CHSS coaches, who are bound by the agreement and trained accordingly. CHSS does not operate a student-facing application other than the Belonging and Skills screeners administered through the District's School Team.

Where a district does not use the NDPA, Appendix A (Part B) applies. Where a district uses both, the document the district signed controls.

### Part B: Appendix A, Data Privacy and Security
    Source [SDPC NDPA]: Section order follows the NDPA's articles (purpose and FERPA designation; data ownership and authorized access; duties of the LEA; duties of the provider; data provisions including security, breach, disposition, and advertising limits; general offer; miscellaneous) so a district privacy officer recognizes the shape immediately.
    Source [Luke's experience]: AFUHSD's baseline is the Arizona NDPA Standard Version 1.2 with Exhibit G, which carries Arizona contract requirements and the AI questionnaire Luke co-wrote with the privacy leads from Mesa and Deer Valley.

#### A.1 Definitions
    Source [Drafting choice]: Defined terms are the same as in Agreement Sections Five and Six so the two documents never drift.

Terms defined in Sections Five and Six of the Agreement (Student Data, Screening Data, De-identified Data, Aggregate Data, Navigator, School Team, Coach, Cohort) have the same meaning here. **Subprocessor** means a third party that hosts or processes Student Data on CHSS's behalf.

#### A.2 Purpose and legal basis
    Source [FERPA]: 34 C.F.R. § 99.31(a)(1)(i)(B) (school official exception) and § 99.33 (limits on redisclosure).
    Source [PPRA]: 20 U.S.C. § 1232h applies to the screeners CHSS administers through schools.
    Source [COPPA]: 15 U.S.C. §§ 6501–6506; Columbus City's DSA requires a COPPA warranty for any data collected directly from students. Navigator is not student-facing, but screener administration may be, so the commitment is stated "to the extent it applies."
    Source [Columbus City DSA]: "agrees that it shall comply with all applicable Ohio laws ... regarding the collection, use and protection of data as if it were the District." The "as if CHSS were the District" standard is adopted for every state.

CHSS receives Student Data solely to provide the Services described in the Agreement. The District designates CHSS as a school official with a legitimate educational interest under 34 C.F.R. § 99.31(a)(1)(i)(B). CHSS is under the District's direct control with respect to the use and maintenance of education records and is subject to the redisclosure limits of 34 C.F.R. § 99.33. CHSS will comply with FERPA; with the Protection of Pupil Rights Amendment (20 U.S.C. § 1232h) as it applies to screeners; with the Children's Online Privacy Protection Act (15 U.S.C. §§ 6501–6506) to the extent it applies; and with the student privacy laws of the District's state listed in the State Exhibit, as if CHSS were the District.

#### A.3 Ownership and control
    Source [Columbus City DSA]: "All information, data, and other content transmitted by the District ... will remain the sole property of the District. The District will retain exclusive control over student data, including determining who may access data and how it may be used."
    Source [James's collateral]: "Your student data remains your district's property, and your district decides who can see it."

All Student Data and Screening Data, and all records CHSS creates or receives on the District's behalf, are and remain the property of the District. The District retains exclusive control over its Student Data, including who may access it and for what purposes. CHSS acquires no rights in Student Data other than the limited license to use it to provide the Services.

#### A.4 Authorized and prohibited uses
    Source [SDPC NDPA]: Article IV prohibitions (no sale; no targeted advertising; no profiling beyond the educational purpose) and Article V on advertising limitations.
    Source [Columbus City DSA]: "Company shall not use educational records for any commercial purpose outside the scope of the agreement, including but not limited to marketing or advertising to students or parents. Company agrees not to sell, share, or disseminate educational records."
    Source [Conversation]: The 501(c)(4) clause (d) comes from James's 10/23 flag that Stand's dual structure invites questions "even when nothing is wrong."
    Source [af-dpa]: knowledge/law/coppa.md and arizona.md: COPPA's "operator" definition excludes nonprofits exempt from § 5 of the FTC Act, and A.R.S. § 15-1046 reaches operators of services "designed and marketed for school purposes." A coaching nonprofit may sit outside both, so "the contract is the only enforcement." That is the reason clause (d) and clause (f) are written in rather than left to statute. NDPA v1.2 IV.2 limits use to "the Services outlined in Exhibit A or stated in the Service Agreement"; v2 4.2 closes that gap with "or as instructed by the LEA," which (a) through (f) mirror.
    Source [af-dpa]: agents/exhibit-h-rider-draft.md, term 6 ("Partner and evaluator visibility"): "Where the approved service shares data with a program partner, evaluator, certifying body or sponsor, Provider will name the recipient and the data shared ... no other third-party visibility is permitted." Marked in the repo as an agent draft not yet adopted by the Director; reused here as clause (f).

CHSS will use Student Data only to provide the Services and as instructed by the District. CHSS will not: (a) sell, rent, or trade Student Data; (b) use Student Data for targeted advertising or marketing to students, parents, or staff; (c) build a profile of a student for any purpose other than the Services; (d) use Student Data in any advocacy, lobbying, political, or fundraising activity of Stand for Children Leadership Center, Inc. or any affiliated entity, including any entity organized under section 501(c)(4); (e) disclose Student Data to any third party other than a Subprocessor listed under A.6, except as required by law and, where lawful, with prior notice to the District; or (f) share Student Data with any program partner, evaluator, funder, certifying body, or sponsor unless the recipient and the data shared are named in Exhibit D-3 of the Agreement and approved by the District in writing.

#### A.5 Data minimization
    Source [SDPC NDPA]: The NDPA's Exhibit B is a checklist of data elements the provider collects; this clause ties CHSS to the equivalent list in Agreement Exhibit D-1.
    Source [Emily's email]: "Asking for too much could create unnecessary objections and delays."
    Source [Columbus City DSA]: Service "will not require a student to disclose more information than is reasonably necessary."
    Source [af-dpa]: agents/exhibit-h-rider-draft.md, term 3 (data minimization): the provider "will not require Social Security numbers, government identification numbers, payment information, health or disability records" unless listed. Adopted here; IEP/504 status stays an optional element the District may elect.

CHSS will collect only the elements listed in Exhibit D-1 of the Agreement and will not require the District to provide more data than is reasonably necessary to deliver the Services. CHSS will not request Social Security numbers, government identification numbers, payment information, or health records, and will receive disability-related status only where the District elects to provide it under Exhibit D-1. Changes to the element list require the District's written agreement.

#### A.6 Subprocessors
    Source [Emily's architecture]: The CHSS Data Platform diagram: Microsoft Azure / Fabric (data lake, SQL warehouse), Azure API Management, Salesforce Experience Cloud as Navigator (with CRM Analytics and Lightning components), Power BI for research and program analytics, and AI-assisted mapping, validation, and intervention recommendations.
    Source [SDPC NDPA]: Article IV requires the provider to flow down the agreement's obligations to subprocessors and to maintain a list available to the LEA.
    Source [Luke's experience]: From the Rescue Ready review (2026): the DPA goes with whoever actually hosts the data. Naming the platforms here is what lets a district CTO stop asking.

CHSS uses the following Subprocessors, each bound by written terms at least as protective as this Appendix:

| Subprocessor | Function | Location |
|---|---|---|
| Microsoft (Azure, Fabric) | Cloud hosting, data lake, data warehouse, API management | United States |
| Salesforce (Experience Cloud, CRM Analytics) | Navigator user platform, student records and intervention workflows | United States |
| Microsoft (Power BI) | Analytics and reporting | United States |
| [AI model provider] | File-mapping assistance, data validation, intervention recommendations | United States |

CHSS will give the District at least thirty days' written notice before adding or replacing a Subprocessor that will process Student Data. The District may object in writing, and the Parties will work in good faith to resolve the objection before the change takes effect.

#### A.7 Security program
    Source [Columbus City DSA]: Sections 5 through 8: encrypted storage in monitored data centers; no storage outside the United States; passwords not visible to employees, salted hashes, SSL; patches "within one week of release"; anti-virus; firewall and DMZ; "third party audits of security operations are conducted annually"; access control lists; "the identity of all persons having access to student data is documented and access is logged"; employees bound by FERPA.
    Source [San Diego CCAP]: "All staff involved in the data sharing process will be required to sign a confidentiality agreement"; passwords changed frequently; data kept in secure facilities.
    Source [SDPC NDPA]: Article V and Exhibit F (data security requirements) call for a written security program, access controls, encryption, training, and an incident response plan.
    Source [Conversation]: Luke and Jonah (10/26) on background checks: Phoenix Union required fingerprinting and onboarding of Teach For America mentors who were entirely virtual, which stalled the program for years. Stating a background check as a CHSS commitment removes one reason for a district to add its own.
    Source [af-dpa]: knowledge/practice/dpa-review-checklist.md: "TLS 1.2+ in transit, AES-256 or equivalent at rest, including backups"; "MFA on vendor support access"; SOC 2 "does not test application code, does not require penetration testing," which is why the pen test is a separate line. NDPA v1.2 IV.3 binds "each employee or agent with access to Student Data" to confidentiality. The repo records no district position on background checks; that line is a drafting choice from the 10/26 discussion.

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

#### A.8 Breach notification
    Source [Columbus City DSA]: Breach section lists the response steps (assess, communicate, contain, classify severity, protect evidence, notify external agencies, recover, document, assess cost, review, update policies) and gives the District the right to request logs; Ohio R.C. 1347.12 governs notification to affected persons.
    Source [SDPC NDPA]: Article V requires notice to the LEA of any security breach, cooperation in the investigation, and provider responsibility for its own costs; the national form's notice window is the one most state versions keep.
    Source [Luke's experience]: 10/19: "if you have a leak, you'll tell us, if we have a leak, we'll tell you ... those things make us feel a lot more comfortable." Districts do not want to learn of a breach from the press.
    Source [af-dpa]: knowledge/sdpc/ndpa-structure.md, Arizona NDPA v1.2 Article V.4, verbatim: "the Provider shall provide notification to LEA within seventy-two (72) hours of confirmation of the incident, unless notification within this time limit would disrupt investigation of the incident by law enforcement." The repo's reverification notes recommend keeping v1.2's broad, undefined trigger (not v2's "in violation of applicable law" qualifier), saying who notifies families, and lifting the Illinois breach-cost allocation (parent notification, credit monitoring, "legal fees, audit costs, fines").

If CHSS becomes aware of unauthorized access to, or acquisition, disclosure, or loss of, Student Data, whether or not it meets a statutory definition of breach (a "Breach"), CHSS will notify the District's privacy contact without unreasonable delay and in no event later than seventy-two hours after confirming the Breach, unless notification within that time would disrupt a law-enforcement investigation, by telephone and email, with the information then known: the nature of the Breach, a description of the Student Data involved, the students affected, steps taken to contain it, and a point of contact. CHSS will update the District as the investigation proceeds, cooperate fully, and comply with any breach-notification law applicable to the District's data. The District decides whether and how affected students and parents are notified; CHSS will not notify students, parents, or the public without first consulting the District, except where law requires otherwise. CHSS will bear the reasonable costs attributable to its Breach, including parent notification, credit monitoring where offered, forensic investigation, legal fees, and regulatory fines.

#### A.9 Data location
    Source [Columbus City DSA]: "No student data is stored outside the United States without the District's written consent."
    Source [Conversation]: Jonah (10/26): "Don't store your data in Russia, et cetera."

Student Data is stored and processed only in data centers located in the United States. CHSS will not transfer Student Data outside the United States without the District's prior written consent.

#### A.10 Retention, de-identification, and destruction
    Source [SDPC NDPA]: Article IV "Disposition of Data" and Exhibit D (Directive for Disposition of Data): sixty days from written request; duty does not extend to de-identified data.
    Source [Columbus City DSA]: Ninety days after termination to destroy or return all educational records.
    Source [FERPA]: De-identification standard at 34 C.F.R. § 99.31(b)(1); the attribute of "reasonable determination" that identity is not personally identifiable "taking into account other reasonably available information."
    Source [Emily's architecture]: The platform already separates a "De-identification & Privacy" step (tokenization and pseudonymization for research datasets) from the identifiable warehouse. This clause makes that separation contractual.
    Source [Drafting choice]: Cell suppression at fewer than ten students is a common state-reporting threshold; it keeps aggregate results publishable without re-identification risk at small schools.
    Source [Conversation]: James (10/23): keep "Agua Fria High School went from 60% on track to 72%"; delete the student-level data. Luke: "That's a different thing."
    Source [af-dpa]: knowledge/sdpc/ndpa-structure.md, NDPA v1.2 IV.5: "Provider agrees not to attempt to re-identify De-Identified Student Data ... Provider's use of De-Identified Data shall survive termination of this DPA ... Provider agrees not to transfer de-identified Student Data to any party unless (a) that party agrees in writing not to attempt re-identification, and (b) prior written notice has been given to the LEA who has provided prior written consent." v2 4.5 adds that de-identification must "comply with either NIST de-identification standards or US Department of Education guidance." Both are adopted below.
    Source [af-dpa]: knowledge/law/ferpa.md: § 99.31(b)(2) allows coded student-level releases only for education research, with a code "not based on" the student's SSN "or other personal information" and the method kept secret; a hash of the student number is a code based on personal information. PTAC: "simple removal of direct identifiers ... DOES NOT constitute adequate de-identification." Hence the random token and the destroyed key.
    Source [af-dpa]: knowledge/law/deidentification-and-definitions.md: the captures "do not settle" a minimum cell size; PTAC uses "a minimum cell size" and "controlled rounding," and "a vendor's 'aggregate' effectiveness report with n=3 cells is PII." Ten is the drafting choice, matching common state reporting thresholds.

- **During the term.** CHSS retains Student Data only as long as needed to provide the Services.
- **On request.** On the District's written directive at any time, CHSS will return or destroy the Student Data specified within sixty days, on a schedule agreed with the District. The District may use the NDPA's Directive for Disposition of Data (Exhibit D) for this purpose with no further notice required.
- **On termination.** Within sixty days after the Agreement ends, CHSS will destroy or return to the District all Student Data and Screening Data, including copies held by Subprocessors, and will certify destruction in writing signed by an officer. Copies in encrypted backups expire on the documented rotation, not to exceed ninety days, are never restored to production, and are certified as expired when that date passes.
- **De-identified and Aggregate Data.** CHSS may create De-identified Data in accordance with NIST de-identification standards or U.S. Department of Education guidance, by removing direct and indirect identifiers and replacing the student identifier with a random token that is not derived from any student identifier or other personal information, under a key that CHSS destroys with the identifiable data. Aggregate Data is a subset of De-identified Data. CHSS may retain De-identified Data and Aggregate Data after termination to evaluate and improve the program, including following Cohort outcomes over time. CHSS will not attempt to re-identify any student and will not transfer De-identified Data to any third party other than a Subprocessor unless that party agrees in writing not to attempt re-identification and the District has given prior written consent. Aggregate Data will suppress any cell smaller than ten students.
- **Research and publication.** CHSS may publish findings based on De-identified Data and Aggregate Data. No publication will identify a student. CHSS will not identify the District in any publication without the District's prior written consent and will provide the District a copy of any report that includes the District's aggregate results at least fifteen business days before publication. The District may always see its own data.

#### A.11 Parent and eligible student rights
    Source [FERPA]: Parents and eligible students have rights to inspect, review, and seek amendment of education records (34 C.F.R. §§ 99.10–99.22); those rights run against the District, which the provider must support.
    Source [Columbus City DSA]: The company and District "shall establish reasonable procedures ... by which a parent, legal guardian or eligible student may review personally identifiable information on the pupil's records, correct erroneous information."
    Source [SDPC NDPA]: Article II: the provider assists the LEA in responding to parent and eligible-student requests within a stated period.

Requests by a parent or eligible student to inspect, review, or correct education records are handled by the District. CHSS will support the District by providing, within ten business days of request, the Student Data it holds about the student, and will correct or delete data as the District directs.

#### A.12 Use of artificial intelligence
    Source [Luke's experience]: The Arizona NDPA Exhibit G AI questionnaire, which Luke co-developed with the privacy leads from Mesa and Deer Valley with input from about a dozen privacy and technology professionals: how the vendor uses AI, what data goes to AI providers, whether user data trains models, and what safeguards and oversight exist. This clause answers those questions before they are asked.
    Source [Emily's architecture]: AI-assisted mapping, anomaly detection, "risk models and intervention recommendations" are in the platform design; Jonah (10/19) described AI that "can help coach the team leads."
    Source [af-dpa]: knowledge/practice/ai-dpa-clauses.md (marked in the repo as a drafting suggestion, not a standard): model-provider disclosure "by URL and date, and the country of processing," thirty days' notice before changing a model provider with a termination right; outputs "descriptive of an identifiable student are Student Data"; disclosure of any subprocessor personnel who may view prompts or outputs for abuse monitoring; outputs "require human review before use" and are not "the sole basis for any decision with legal or material effect on a student." The shortest proven binding wording is California NDPA v1.5 Exhibit G cl. 8: "Student Data ... shall not be used for training purposes or to develop synthetic and/or inferred data."
    Source [af-dpa]: knowledge/sdpc/ai-addendum-and-checklist.md lists the Arizona checklist questions this clause pre-answers: base model and provider (1.1–1.2), opt-out of AI decision-making (1.4), data shared with an AI subprocessor (4.2), whether user data trains the model (4.7), human in the loop (5.6), and query logging (5.7).

CHSS uses automated and machine-learning tools within the data platform to assist with mapping incoming files to a common format, to flag data-quality problems, and to suggest interventions for the School Team's consideration. CHSS commits that: (a) Student Data, De-identified Data, and any outputs derived from them will not be used for training purposes or to develop synthetic or inferred data, by CHSS or by any Subprocessor, except a model used solely to deliver the Services and identified in A.6; (b) each model provider is listed as a Subprocessor with the product tier used, the provider's data-use terms by URL and date, and the country of processing, and is contractually prohibited from retaining or training on Student Data, with CHSS providing the provider's written attestation on request; (c) outputs that describe an identifiable student are Student Data for all purposes of this Appendix; (d) intervention suggestions are recommendations for educators, who make all decisions about students, and are never the sole basis for any decision with a material effect on a student; (e) no Subprocessor personnel view prompts or outputs containing Student Data except as disclosed to the District in writing; (f) the District may request that AI-generated recommendations be disabled for its schools; (g) CHSS will give thirty days' written notice before adding or changing a model provider, and the District may object under A.6; and (h) CHSS will complete the District's AI questionnaire (for example, Arizona NDPA Exhibit G) on request.

#### A.13 Audit and assurance
    Source [Columbus City DSA]: Annual third-party audits of security operations; District may request log data for incident investigation.
    Source [Conversation]: Jonah (10/26) listed audits among the standard terms to include; James (10/23): "Columbus City requires a security audit every three years or something like that" (the document says annually).
    Source [Drafting choice]: Evidence-on-request once a year, plus full cooperation after a breach, is the posture most CTOs accept in place of an unlimited audit right; an audit right is still offered where state law or policy demands it.
    Source [af-dpa]: knowledge/sdpc/article-crosswalk-v1-2-to-v2-1.md: NDPA v1.2 Article V.2 "gives the LEA the right to audit the Provider." knowledge/GAPS.md recommends the Utah audit-evidence menu (self-assessment, questionnaire, "SOC2 or SOC3" report, or on-site review by agreement), adopted below so a district can pick the form of evidence.

On request, not more than once per year unless a Breach has occurred, CHSS will provide the District with any of the following at the District's election: a completed security self-assessment, responses to the District's security questionnaire within thirty days, its most recent independent assessment report (SOC 2 Type II, SOC 3, or equivalent) and penetration test summary under a confidentiality agreement, a description of its security program, and a certificate of insurance. If the District's state law or policy requires an audit right, CHSS will cooperate with an on-site or remote audit at a mutually agreed time, conducted so as not to compromise other districts' data.

#### A.14 Insurance
    Source [Columbus City DSA]: "Your company must carry cyber liability insurance of at least $1,000,000 to cover Crisis Management and Computer System Extortion, Media and Content Liability, and Security and Privacy Liability."
    Source [San Diego CCAP]: Each party: commercial general liability $1,000,000 per occurrence / $2,000,000 aggregate; professional errors and omissions $1,000,000; other party as additional insured; certificate of insurance on request; self-insurance acceptable.
    Source [James's MOU draft]: Section Eight currently promises "reasonable liability insurance" and a certificate "including any applicable cybersecurity or data-security coverage" on request; this clause states the limits.
    Source [af-dpa]: knowledge/practice/dpa-review-checklist.md: "the NDPA has no insurance clause"; district practice research puts "$1M for directory-only, $2M+ for SIS, assessment, special education or health data," and Beaverton requires $2,000,000 per claim and aggregate "with the policy running two years past the contract." $2,000,000 is drafted; Columbus's $1,000,000 floor is satisfied. Stand's finance lead confirms the actual policy before this is sent.

CHSS maintains, and will provide certificates on request for: cyber liability insurance of at least $2,000,000 per claim and in the aggregate, covering security and privacy liability, crisis management, network extortion, and media and content liability, maintained for two years after this Appendix ends; commercial general liability of $1,000,000 per occurrence and $2,000,000 aggregate; and professional errors and omissions liability of $1,000,000 per claim. These requirements may be met through a reasonable self-insurance program.

#### A.15 Screening Data
    Source [Emily's email]: Area 3 of the four the agreement must cover: "the Belonging and Skills screeners we administer, including the collection, storage, analysis, and use of student-level screening data."
    Source [PPRA]: 20 U.S.C. § 1232h; the District approves instruments and gives notice (Agreement 6.7). This clause covers what CHSS does with the responses.
    Source [Conversation]: Jonah (10/19): screener results feed the Navigator so the team can see that "fifteen other kids have the same profile" and deliver one intervention to all of them. Student-level screening results therefore have to be visible to the School Team.

Screening Data is collected by CHSS only after the District has approved the instruments and provided any required notice under Section 6.7 of the Agreement. Screening Data is subject to every protection in this Appendix. Student-level screening results are visible to the School Team and, under Option A of Section 5.4, to the Coach; CHSS program and research staff see only De-identified and Aggregate Screening Data.

#### A.16 Term, termination, and survival
    Source [Columbus City DSA]: Term "shall be co-terminus with the contract/agreement and shall terminate when all of the student data ... is destroyed and/or returned."
    Source [James's MOU draft]: The Agreement's cure period is ten days (Section Two); thirty days is used here for data-specific breaches because remediation of a security finding usually takes longer than ten days.

This Appendix is coterminous with the Agreement and continues until all Student Data has been returned or destroyed under A.10. Sections A.3, A.4, A.8, A.10, and A.11 survive termination. The District may terminate the data provisions of the Agreement on thirty days' written notice if CHSS materially breaches this Appendix and does not cure within that period.

#### A.17 Governing law and State Exhibit
    Source [State law]: Ohio: R.C. 3319.321 (confidentiality of student records), 3319.325–3319.327 (educational records and third-party contractors), and Chapter 1347 including R.C. 1347.12 (breach notification), all named in the Columbus City DSA. California: Education Code § 49073.1 (contract requirements for digital storage and educational software) and the Student Online Personal Information Protection Act, Business and Professions Code § 22584. Arizona: Arizona NDPA Exhibit G, including the AI questionnaire.
    Source [Lewis County]: Missouri districts will supply the Missouri NDPA state exhibit through their consortium; it is listed as "to be added" rather than drafted here.

This Appendix is governed by the laws of the District's state. The State Exhibit attached for the District's state sets out additional required terms, including: for Ohio, compliance with Ohio Revised Code 3319.321, 3319.325 through 3319.327, and Chapter 1347 (including breach notification under R.C. 1347.12) as if CHSS were the District; for California, the terms required by Education Code § 49073.1 and Business and Professions Code § 22584; for Arizona, Arizona NDPA Exhibit G including the AI questionnaire; and for Missouri, Massachusetts, Utah, and other states, the state NDPA exhibit where one exists.

#### A.18 Order of precedence
    Source [Drafting choice]: Mirrors Section 5.2 of the Agreement so both documents say the same thing about which controls.

If this Appendix conflicts with the Agreement, this Appendix controls as to Student Data. If the District has executed the NDPA with CHSS, the NDPA controls as to any conflict with this Appendix.

### Part C: System specifications (district-facing)
    Source [Conversation]: Jonah (10/26): "there's going to be a sheet that you design, where it's like, these are the systems we will have, but we're going to present it as, this is our system." Emily: leadership "can very quickly look at it and feel legit that we're behind it," and technical people see "these guys know what they're talking about."
    Source [Emily's architecture]: Every platform fact below is taken from the CHSS Data Platform diagram; items the diagram claims (RBAC, encryption, audit logging, retention policies) are stated here as commitments and should be confirmed by Emily before this page is shown to a district.
    Source [Drafting choice]: Written as present-tense statements where CHSS can confirm them and bracketed where a decision or build is still pending.

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

---

# Page D. Notes for James's emails (CHSS-internal working page)

## Notes for James's emails
    Source [Conversation]: James (10/23 and 10/26) is the one writing to districts right now: a Missouri partner district's technology coordinator, the Columbus City CTO for the first review, and San Diego for the second. These are paste-ready paragraphs and asks, in his voice, consistent with the drafts on the other tabs.
    Source [Drafting choice]: Written for a technology coordinator or CTO reader: short, concrete, no legal citations. The agreement drafts carry the citations.

Use what fits. Each block is standalone. Where a block makes a commitment on CHSS's behalf (NDPA, Exhibit E, the de-identified evaluation carve-out), it matches the current drafts; if those change, change the email.

### 1. Reply to the Missouri district's technology coordinator
    Source [Lewis County]: Her 10/26 email: the district has asked its consortium (TEC via MOREnet) and the SDPC Resource Registry to obtain an NDPA with CHSS; "the purpose of this service is to support student success and timely interventions, not to conduct research. If this part is not correct, please let me know."
    Source [FERPA]: She is testing which exception applies. "Interventions" means the school official exception (34 C.F.R. § 99.31(a)(1)(i)(B)); "research" would push her consortium toward the studies exception and a different agreement. The reply confirms her framing and discloses the de-identified evaluation so it is never a surprise.
    Source [af-dpa]: knowledge/sdpc/exhibit-e-general-offer.md: the first signed NDPA in a state plus a standalone Exhibit E lets other districts in that state subscribe. The sentence about "a general offer of terms" assumes CHSS is willing to sign Exhibit E; delete it if not.

> Thank you for getting this started, and for the clear summary. Your description is correct: the Center for High School Success uses information from your SIS to build the ninth grade dashboards your team and our coach use to identify students who need support and to act on it quickly. That is the purpose, and we operate as a school official under FERPA to deliver it.
>
> One clarification so there are no surprises: like most programs, we evaluate whether our work is helping. We do that with de-identified and aggregate results only (for example, your school's on-track rate), never with identifiable student records, and we delete identifiable data when our partnership ends or whenever you ask.
>
> We are glad to work through TEC and the SDPC process. We will sign the Missouri NDPA, and we expect to have a general offer of terms on file so other Missouri districts can use the same agreement. When TEC reaches out, please have them contact Emily Phan, our Executive Technology Officer, who is copied here. Luke Allpress, who is helping us with agreement language and SIS integration, is also copied.
>
> We will send you a short summary of exactly what data we ask for and how it moves before anyone has to review a document.

### 2. The one-paragraph data summary for any district
    Source [James's collateral]: Mirrors the "Only the data needed" and "Who sees what" sections of James's Navigator collateral, with discipline moved to optional and the de-identified evaluation disclosed.
    Source [Emily's architecture]: Delivery is files by SFTP or secure upload in v1; nightly or weekly automated export is the target, scheduled upload is the floor.

> Here is what the integration involves, in plain terms. Your district sends us a file for each ninth grade cohort with student ID, name, grade level, course enrollments, course marks and credits by grading period, GPA, and attendance. Most districts set up an automated weekly export to our secure SFTP; if that is not possible yet, a scheduled upload each grading period works and we will help you automate it later. Your school team sees student-level dashboards with names. Our coaches see aggregate views unless you choose to give them more. Our program and research staff never see identifiable data. Identifiable data is deleted when the partnership ends or whenever you ask; we keep only de-identified and aggregate results to evaluate the program. The full terms are in our data privacy appendix, or we will sign your state's NDPA, whichever you prefer.

### 3. Asks for the Columbus City CTO review
    Source [Columbus City DSA]: Their Student Data Sharing Agreement (revised 3/17/2025) is the strictest document in hand: annual third-party security audit, $1M cyber liability, U.S.-only storage, documented access roster with logs, 90-day destruction, Ohio R.C. 3319.321, 3319.325–327, and Chapter 1347.
    Source [Conversation]: James (10/26): Columbus "has been very diplomatic, easy to talk to"; the plan is to be transparent, "we're trying to find the right language. We know you all have a high bar. Can we review this together?" Luke is available Nov 2 (not 1–2 p.m.), the morning of Nov 3, and Nov 4 (not 1–3 p.m.), Arizona time.

Ask for, in order:

1. Forty-five minutes with the CTO and whoever reviews data agreements for the district (privacy officer or counsel), between Nov 2 and Nov 4, with Luke on the call.
2. Confirmation that the Student Data Sharing Agreement dated 3/17/2025 is the current form, and whether the district would also accept the Ohio NDPA.
3. Their read on two specific points before the call: coach access to student-level data (Option A) versus aggregate only (Option B), and CHSS keeping de-identified results after termination for program evaluation.
4. Whether the district requires anything of CHSS coaches beyond the agreement (background checks, district onboarding, training).
5. Their board timeline from "agreement final" to "approved," so CHSS can work backward from the January start.

### 4. Asks for San Diego
    Source [San Diego CCAP]: The document in hand is the SDCCD–SDUSD College and Career Access Pathways agreement (dual enrollment), not a student data privacy agreement. Its Section V routes data through Cal-PASS Plus. SDUSD will use a different instrument for an outside nonprofit, almost certainly the California NDPA.
    Source [State law]: California Education Code § 49073.1 and the Student Online Personal Information Protection Act set required contract terms for student data. The California NDPA (v1.5) Exhibit G carries them.

Ask for:

1. The student data privacy agreement template SDUSD uses with outside partners that receive student-level data, since the CCAP agreement is the wrong instrument for this.
2. Whether SDUSD prefers the California NDPA or its own form, and who in the district signs it.
3. Whether the district's General Services Agreement and SOW format will be required for the accelerator, so CHSS can structure its "District responsibilities / CHSS responsibilities" sections to match.
4. The same two substantive points as Columbus: coach access and de-identified retention.

### 5. Two sentences for the superintendent-level emails
    Source [Conversation]: James (10/26): verbal yeses came from superintendents and heads of academics; CTOs are hearing about it afterward. This closes that gap in the acceptance email itself.

> Because the accelerator includes SIS integration, we will ask you within the first two weeks to name a technical contact and a data privacy contact, and we will schedule a short onboarding call with both before any data moves. We will sign your state's National Data Privacy Agreement or provide our own privacy appendix written to the same standard, whichever your district prefers.

---

# Page E. Decision points and justification (CHSS-internal working page)

## Decision points and justification
    Source [Conversation]: Jonah (10/26): "we just need to have a little bit more of a calculus"; a small number of people, "you are more informed, plus Tara," decide. This page is that calculus: each choice the drafts embody, what was chosen, why, and what would change it.
    Source [Drafting choice]: Status labels: **Recommended** means the drafts assume it and a reviewer can accept it as is; **Needs confirmation** means a named person has to say yes before it goes to a district; **Open** means the drafts carry both options.

Each item below is a decision the drafts on the other tabs already make. Where a choice is marked "Needs confirmation" or "Open," the drafts are written so the other answer can be dropped in without rewriting anything else.

### 1. Coach access to student-level data
    Source [Conversation]: 10/26: Jonah leaned to the "less intrusive approach" with the team lead screen-sharing; James wanted to ask for access and fall back; Luke: aspirationally ask, be ready with Plan B, citing the PXU–Teach For America fingerprinting fight. Jonah and James to confirm with Tara whether coaches need names.
    Source [James's collateral]: His Navigator one-pager already tells districts that CHSS coaches and staff see "aggregate data only."
    Source [AFUHSD precedent]: AFUHSD accepted a partner coach seeing student data (TFA, 2026) when the coach was the only partner viewer and acknowledged as a FERPA school official; the district's first instinct the year before was to strip names.

**Status: Open.** Drafted as Option B (aggregate only, team lead screen-shares) by default, with a one-sentence district opt-in to Option A (coach has student-level access for their schools, logged, background-checked, trained). Why: B matches the collateral already in circulation, keeps one protocol across the network, and costs little in coaching effectiveness since the team lead is in the room. A is defensible under FERPA and some districts will grant it. What would change it: Tara saying coaches cannot do the job without names, or Columbus and San Diego both saying A is fine.

### 2. Identifiable data at all
    Source [James's MOU draft]: The current Agreement for Services Section Six describes "de-identified individual student data."
    Source [Conversation]: 10/19: Tara noted that today's uploads are de-identified and a direct connection changes that; Luke: "it does change what I like as much," but with a strong agreement in place "there's more than there used to be" who say yes. Navigator cannot show a school team "who needs support" without names.

**Status: Recommended.** The feed is identifiable, because the product requires it for school teams. The draft contains the exposure by role (Section 5.4), use (5.5), and retention (5.6). What would change it: a district that will only send de-identified data, in which case the fallback is a ninth-grade-only, pseudonymous feed and a Navigator without names for that district.

### 3. Discipline records
    Source [James's collateral]: Lists discipline among "only the data needed."
    Source [Emily's architecture]: Discipline is an input category on the platform diagram.
    Source [Conversation]: Tara (10/19): behavior data is "typically" not received; Luke (10/26): discipline is "the most tightly held" element, and in Arizona social-emotional data sharing is restricted.

**Status: Recommended.** Optional, not required. Why: not needed for the on-track calculation, and the single element most likely to stall a privacy review. What would change it: Tara identifying a Navigator feature that depends on it.

### 4. Retention after termination
    Source [Conversation]: James (10/23): delete student-level data, keep "Agua Fria High School went from 60% to 72%." Luke: different things.
    Source [SDPC NDPA]: Article IV: disposition within sixty days of request; de-identified data exempt; use of de-identified data survives termination; no re-identification; transfer only with written no-re-identification terms and LEA consent.
    Source [Columbus City DSA]: Destroy or return within ninety days of termination.
    Source [James's MOU draft]: Current draft keeps identifiable data for three years after termination.

**Status: Recommended.** Identifiable data destroyed within sixty days of termination or directive, with backups expiring within ninety; de-identified and aggregate data retained for evaluation under NDPA-style limits. Why: sixty days satisfies NDPA v2, Columbus, and the stricter districts; the carve-out is the NDPA's own. The three-year clause in the current draft would be struck by every district on the list. What would change it: nothing on the district side; Emily confirms the deletion runbook can meet sixty days across Salesforce, Azure, and Power BI.

### 5. The NDPA, Exhibit E, and CHSS's own appendix
    Source [Lewis County]: A Missouri district has already asked its consortium to obtain the NDPA with CHSS.
    Source [af-dpa]: Exhibit E extends privacy terms within a state for three years from the provider's signature; registry rows are district-created; the originating district uploads the signed agreement and a standalone Exhibit E. The v1.2 "Provider" definition is a strained fit for a coaching nonprofit, so Section 5.1's school-official statement stands on its own.

**Status: Recommended.** CHSS commits to sign any state NDPA on request, signs Exhibit E with the first district in each state, and keeps Appendix A as the instrument for districts that do not use the NDPA. Why: the NDPA will arrive regardless; fighting it costs months, and Exhibit E turns the first signature in each state into a template for the rest. What would change it: Stand's counsel objecting to the NDPA's standard clauses, which cannot be redlined.

### 6. Contracting entity and the 501(c)(4)
    Source [James's MOU draft]: Names "Stand for Children Leadership Center Inc." as the Organization.
    Source [Conversation]: James (10/23): Stand is both a (c)(3) and a (c)(4); "there doesn't actually have to be something wrong for people to raise a stink."
    Source [af-dpa]: A nonprofit may sit outside COPPA's "operator" definition and outside state operator statutes, so "the contract is the only enforcement."

**Status: Needs confirmation (Demian or counsel).** Drafted with Stand for Children Leadership Center, Inc. as the party and an express clause barring any advocacy, lobbying, political, or fundraising use of student data by any affiliate, including any (c)(4). Why: answers the question before a board member asks it. What would change it: confirmation that the Leadership Center is the correct (c)(3) signatory, which the current MOU implies.

### 7. Screeners and parental consent
    Source [Emily's email]: The agreement must "explicitly cover the Belonging and Skills screeners we administer."
    Source [af-dpa]: Department of Education SPPO letter of Aug 26, 2026: behavioral health screeners that probe emotional or psychological states require written parental consent before administration; PPRA opt-out does not substitute. Arizona § 15-117 adds seven days' notice and fourteen categories.
    Source [PPRA]: 20 U.S.C. § 1232h.

**Status: Needs confirmation (Tara).** The District approves screener content and runs notice or consent; CHSS provides the full instrument for review and adds no questions without approval. Why: the belonging screener can reach PPRA's protected areas, and the obligation legally sits with the district. What would change it: Tara confirming the instruments avoid the protected categories, in which case notice alone may suffice.

### 8. Cyber liability at $2M
    Source [Columbus City DSA]: At least $1,000,000.
    Source [af-dpa]: District practice research: "$1M for directory-only, $2M+ for SIS, assessment, special education or health data"; Beaverton requires $2M per claim and aggregate with a two-year tail.
    Source [San Diego CCAP]: CGL $1M/$2M, E&O $1M, additional insured, certificate on request.

**Status: Needs confirmation (Demian).** Drafted at $2M per claim and aggregate with a two-year tail, plus CGL $1M/$2M and E&O $1M. Why: SIS-level data is the $2M tier in district practice, and $2M satisfies Columbus. What would change it: Stand's current policy limit; if it is $1M, the draft says $1M and the gap goes on Emily's list.

### 9. Delivery tiers and the direct SIS connection
    Source [Emily's architecture]: v1 ingests periodic files by SFTP or secure upload; no vendor API.
    Source [Conversation]: Luke's ranking (10/19): SIS vendor feed first, district SFTP second, Clever/ClassLink last. The 10/26 reframe: TA to help districts automate is part of the offer.

**Status: Recommended.** Three tiers: automated feed (target), scheduled upload (floor), vendor connection (where available). Why: matches what the platform ingests today and leaves the best privacy route on the menu. What would change it: Emily adding API ingestion, which would promote Tier 3.

### 10. Student identifiers and matching
    Source [James's collateral]: "Records are matched using a consistent unique student identifier."
    Source [Emily's architecture]: Identity matching lists district ID, state ID, and "probabilistic matching."
    Source [af-dpa]: Pseudonymous rows tracked over time remain student data; a hash of the student number is a code "based on personal information," which FERPA's research-code rule forbids.

**Status: Recommended.** Require the district or state ID in every feed; allow a district-generated stable pseudonym; treat both as Student Data; use probabilistic matching only to flag duplicates for human review. Why: deterministic matching is what privacy officers trust, and it keeps pseudonymous feeds inside the agreement. What would change it: nothing; this is the safe default.

### 11. Minimum dataset
    Source [Emily's email]: "What is the minimum practical dataset we should request initially versus additional data we might pursue later?"
    Source [AFUHSD precedent]: District data teams strike elements they cannot produce accurately (AFUHSD feeder DSA, 2025).

**Status: Recommended.** Required: ID, name, grade level and enrollment, course enrollments, marks and credits by term, GPA, attendance. Optional: summer school, demographics, discipline, assessments, date of birth. Why: the required set is exactly what the on-track calculation and the dashboards need; everything else is a district election. What would change it: Tara or Emily naming a Navigator feature that needs an optional element.

### 12. Breach notification at 72 hours
    Source [af-dpa]: Arizona NDPA v1.2 Article V.4 uses seventy-two hours from confirmation; the repo recommends keeping the broad trigger, saying who notifies families, and allocating costs.

**Status: Recommended.** Seventy-two hours from confirmation, broad trigger, district controls family notification, CHSS bears costs attributable to its breach. Why: it is the NDPA's own number. What would change it: a state exhibit with a shorter window, which would control.

### 13. Navigator pilot timing
    Source [Emily's email]: Navigator launches at the CHSS Leadership Summit in late November 2026; pilot schools begin in December.
    Source [James's MOU draft]: Current agreements with existing partners were written for de-identified uploads.

**Status: Open (Jonah and Emily).** The pilot runs before any new agreement exists. Either it runs on de-identified data under the existing agreements, or pilot districts sign the new Sections Five and Six first. The drafts do not decide this; it has to be decided before the Summit.

### 14. Research and publication
    Source [SDPC NDPA]: Article IV.5: prior written approval before publishing anything that names the LEA explicitly or indirectly.
    Source [San Diego CCAP]: "Any information published in any form will not have the potential to identify individual students."

**Status: Recommended.** De-identified findings may be published; no student identifiable; district not named without consent; district receives any report with its aggregate results fifteen business days ahead; cells under ten suppressed. Why: it is what the longitudinal evaluation needs and what districts already accept in the NDPA. What would change it: a district wanting approval rights over all publication, which the clause can accommodate per district.

### 15. Audit evidence
    Source [Columbus City DSA]: Annual third-party audit of security operations.
    Source [af-dpa]: NDPA v1.2 gives the LEA an audit right; the Utah evidence menu (self-assessment, questionnaire, SOC 2 or SOC 3 report, on-site by agreement) lets districts choose.

**Status: Needs confirmation (Emily).** CHSS commits to an annual independent assessment and penetration test, and offers districts a menu of evidence once a year. Why: it is the Columbus bar and the shape most CTOs accept. What would change it: timing; if the first SOC 2 cannot complete before the 2027–28 school year, the spec page says so with a date rather than claiming it.

### 16. Naming
    Source [Conversation]: Emily (10/26) proposed "A, B, C" implementation profiles; the coach-access variants are also "Option A / Option B."

**Status: Recommended.** Implementation profiles are "Tier 1, 2, 3"; coach access is "Option A / B." Why: two A/B schemes in one agreement will be confused in a board packet.

---

*End of brief.*
