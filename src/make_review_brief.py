#!/usr/bin/env python3
"""Generate the adversarial-review brief as one Markdown file.

Reads src/content/*.md and src/VERSION, converts each "::src Label :: text"
provenance line into an indented "Source" note under its heading, and wraps
everything in reviewer instructions. Output: ../../06-adversarial-review-brief.md
(the Deliverables folder) and ./review-brief.md next to this script.
"""
import pathlib, re, datetime

ROOT = pathlib.Path(__file__).parent
SITE = ROOT.parent
OUT_DELIV = SITE.parent / "06-adversarial-review-brief.md"
OUT_LOCAL = SITE / "review-brief.md"
LIVE = "https://lukeallpress.github.io/chss-data-agreement/"

DOCS = [
    ("A", "Case-making (goes up front; audience: superintendent, head of academics, board)", "01-case-making.md"),
    ("B", "District commitments: replacement Sections Five and Six of the Agreement for Services", "02-district-commitments.md"),
    ("C", "CHSS commitment to privacy and security: NDPA posture, Appendix A, system specifications", "03-chss-commitment.md"),
    ("D", "Notes (CHSS-internal working page: paste-ready blocks for current district emails)", "04-notes-for-james.md"),
    ("E", "Decision points and justification (CHSS-internal working page)", "05-decisions.md"),
]

ver, date = [l.strip() for l in (ROOT / "VERSION").read_text().strip().splitlines()[:2]]

HEADER = f"""# Adversarial review brief: CHSS data agreement drafts, v{ver} ({date})

Live page with the same content and per-section source popovers: {LIVE}
Generated {datetime.date.today().isoformat()} from the site source. Everything after the
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

"""


def convert_doc(letter, title, fn):
    text = (ROOT / "content" / fn).read_text()
    out = [f"# Page {letter}. {title}\n"]
    for ln in text.splitlines():
        m = re.match(r"^::src (.+?) :: (.*)$", ln)
        if m:
            out.append(f"    Source [{m.group(1)}]: {m.group(2)}")
            continue
        mh = re.match(r"^(#{1,3})\s+(.*)$", ln)
        if mh:
            # demote one level so the page title is the only H1 for this page
            out.append("#" + mh.group(1) + " " + mh.group(2))
            continue
        out.append(ln)
    return "\n".join(out) + "\n\n---\n\n"


def main():
    body = HEADER + "".join(convert_doc(*d) for d in DOCS)
    body += "*End of brief.*\n"
    OUT_DELIV.write_text(body)
    OUT_LOCAL.write_text(body)
    words = len(body.split())
    print(f"wrote {OUT_DELIV} and {OUT_LOCAL}: {len(body)} chars, ~{words} words")


if __name__ == "__main__":
    main()
