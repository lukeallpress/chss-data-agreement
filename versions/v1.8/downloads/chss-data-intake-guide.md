# Technical and Data Integration Guide
::src Conversation :: Emily and Phil (11/4 call): a data-intake document, separate from the agreement, that tells a district's data engineer "here is the data we need, and what each column means," the kind of documentation Luke has found smoothest to work with as a district. Luke sends samples; Emily's data engineer fits the column definitions to the Fabric data model.
::src SchooLinks :: Modeled on the SchooLinks Technical and Data Integration Guide (public Notion site): one overview, a conventions page, identifiers, SFTP, rostering, then one schema page per file with the same six-line header (purpose, filename, what to include, what to exclude, frequency, partial-data behavior) and the same four-column table. Where CHSS needs something SchooLinks does not, the text says so: daily attendance events rather than a count, an in-year progress-marks file, summer school folded into student courses.
::src James's MOU draft :: Every file and column traces to Exhibits D-1 and D-2 of the Agreement; the Required and Optional split is D-1's. If the two ever disagree, the Agreement controls and this guide is corrected.
::src Needs CHSS confirmation :: Column names and types are a proposal. Bracketed values (hosts, addresses, thresholds, SSO dates) are CHSS's to fill. Section 8.10 waits on Emily's description of the screener flow (Friday 11/6).

> **Who this is for.** The District's technical contact named in Exhibit D-3, and whoever builds exports from the SIS or data warehouse. **Draft 0.2, Nov 4, 2026**, for CHSS to confirm before any district receives it.

## About this guide

This guide is the District's resource for connecting its student information system (SIS) or data warehouse to CHSS. It covers the automated feed in Exhibit D-2 of the Agreement: what files CHSS needs, how they are formatted, how they are sent, and what happens after they arrive.

If you have trouble with any part of the process, extracting, transforming, or uploading your data, contact your CHSS integration contact. We would rather solve it with you than have you guess.

| Item | Entry |
|---|---|
| Data support | [datasupport@chss email] |
| Your integration contact | [name, email, phone], assigned at the onboarding call |
| Privacy questions | [CHSS privacy officer, per Exhibit D-3] |
| Guide version | [0.2, Nov 2026] |

## Contents

1. [Data integration overview](#1-data-integration-overview)
2. [Single sign-on](#2-single-sign-on)
3. [System compatibility and network requirements](#3-system-compatibility-and-network-requirements)
4. [CSV file conventions](#4-csv-file-conventions)
5. [Account identifiers](#5-account-identifiers)
6. [SFTP server and test uploads](#6-sftp-server-and-test-uploads)
7. [Rostering: schools, students, staff](#7-rostering-schools-students-staff)
8. [Student data schemas](#8-student-data-schemas)
9. [Validation, error notifications, and acceptance](#9-validation-error-notifications-and-acceptance)
10. [School year rollover and changing your SIS](#10-school-year-rollover-and-changing-your-sis)
11. [Getting your data back, and deletion](#11-getting-your-data-back-and-deletion)

**Schema pages:** [schools.csv](#7-1-schools-csv) · [students.csv](#7-2-students-csv) · [school_staff.csv](#7-3-school-staff-csv) · [student_courses.csv](#8-1-student-courses-csv-courses-marks-and-credits) · [progress_marks.csv](#8-2-progress-marks-csv-marks-by-grading-period) · [gpa.csv](#8-3-gpa-csv) · [attendance_daily.csv](#8-4-attendance-daily-csv) · [Summer school](#8-5-summer-school) · [state_assessments.csv](#8-6-state-assessments-csv) · [sat_act.csv](#8-7-sat-act-csv-optional) · [discipline.csv](#8-8-discipline-csv-optional-elected) · [program_participation.csv](#8-9-program-participation-csv-optional) · [Screening data](#8-10-screening-data) · [Code tables](#8-11-code-tables-sent-once-in-code-tables)

---

## 1. Data integration overview

The CHSS integration has two phases, in this order:

1. **Rostering.** Schools, students in scope, and the staff who will use Navigator. Three files, or a read-only connection to your SIS vendor where one is available.
2. **Student performance data** for the on-track indicators and the 9th Grade Success Team's work: courses and marks, credits and GPA, attendance, summer school, state assessments, and the optional files the District elects in Exhibit D-3.

Both phases run through the same mechanism: scheduled CSV files placed on the CHSS SFTP server, or a scheduled export from your SIS vendor directly to CHSS (Exhibit D-2). CHSS processes files as they arrive. We ask that scheduled files land between [11 PM and 2 AM] District local time so that the morning's Navigator reflects the previous day.

**Scope.** All 9th grade students at participating schools, and, for each Cohort, the same students in later years until graduation or exit (Agreement Section 6.3). Send the full current roster each time; CHSS handles changes by comparing loads.

**Cadence.** Weekly during the school year, nightly where the District prefers; a final update within two weeks after the end of the school year and after summer school (Section 6.5). Per-file minimums are on each schema page.

**What CHSS never asks for.** Social Security numbers, government identification numbers, payment information, or health records (Appendix A.5). IEP, 504, and meal status only where the District elects them in Exhibit D-3.

## 2. Single sign-on

[Emily and Phil to confirm. The Agreement leaves SSO as an implementation choice (A.7); Jonah's 6.8 question is whether CHSS will offer it and when.]

Navigator supports the following sign-in methods for District staff:

| Method | Status | Notes |
|---|---|---|
| Username and password with multi-factor authentication | [Available] | Default. Usernames are work email addresses from school_staff.csv. |
| Google Workspace sign-in | [Planned, date] | Requires the District to allow sign-in for the CHSS application in the Google Admin console. |
| Microsoft Entra ID sign-in | [Planned, date] | |
| ClassLink or Clever | [Not planned / planned] | |
| SAML (provider-agnostic) | [On request] | |

Students do not have Navigator accounts. Screener administration is described in Section 8.10.

## 3. System compatibility and network requirements

- **Browsers.** Navigator runs in current versions of Chrome, Edge, Safari, and Firefox. No installation.
- **Network.** No inbound connections to the District are required. Outbound SFTP (port 22) to [sftp host] from the server that runs your export job. Allowlist [CHSS SFTP IP addresses] if your firewall restricts outbound traffic.
- **Email.** Validation reports and error notifications come from [noreply address]; allowlist it.
- **Nothing is installed on District systems.** The District's export job runs on District infrastructure under District control.

## 4. CSV file conventions

These conventions cover CHSS's own file formats. If your SIS produces a standard export that does not follow them, tell your integration contact; CHSS can map a vendor-standard export rather than ask you to transform it.

**File format.**

- Send every file as CSV (comma-separated values) with the `.csv` extension, UTF-8 encoded, with a header row.
- Surround every field with double quotes. This is the single most common source of rejected rows (names with commas, course titles with commas).
- Column headers must match the schema exactly: lower case, words separated by underscores (`student_sis_id`), no spaces.
- Dates as `YYYY-MM-DD`. School years as the four-digit ending year (2026-27 is `2027`).
- Leave a column blank rather than omitting it. Headers are always present.
- Be careful saving CSVs from Excel. Excel changes long identifiers to scientific notation and strips leading zeros. Export from the SIS or warehouse directly.

**File naming.** File names are fixed per schema and tell CHSS how to process the file. They are listed on each schema page. Do not add dates or district codes to the file name; CHSS records the receipt time.

**File location.** Files placed in your `/automated` directory are processed within [5 to 10 minutes] of arrival. Files placed in `/test` are validated and reported on but not loaded, for checking an export before scheduling it.

**Full or incremental.** Each schema page says whether a file is *replacing* (the file is the complete, current source of truth; records absent from the new file are archived) or *additive* (the file adds or updates records and never removes them). Rostering files are replacing. Score and event files are additive.

**Code tables.** Four small files sent once and again when they change: grading scale, terms and grading periods, attendance codes, and (if elected) discipline codes. Schemas in Section 8.11.

## 5. Account identifiers

Every student-level file carries exactly one student identifier column, and its header says which identifier it is.

| Entity | Identifier columns (use one) | Recommendation |
|---|---|---|
| Students | `student_sis_id`, `student_number`, `student_state_id` | `student_sis_id` for your SIS's internal key; `student_state_id` where the state issues one. Pick one and use it in every file. |
| Schools | `school_sis_id`, `school_number`, `school_state_id` | The code your SIS uses for the school; `school_state_id` where one exists. |
| Staff | `staff_sis_id`, `staff_id`, `teacher_number` | The SIS key, so teacher of record joins cleanly. |

The identifier the District chooses is set once for the District in CHSS and used for every file. Mixing identifiers across files is the most common cause of mismatched students, so CHSS will reject a file whose identifier column does not match the District's setting rather than guess.

**Pseudonymous identifiers.** A District that prefers not to send its student identifier may send a stable pseudonymous identifier it generates and keeps, in the `student_sis_id` column, provided the same value appears in every file and every load (Agreement Section 6.4). Records carrying a pseudonym are still Student Data under the Agreement. CHSS cannot repair broken keys; a changed identifier reads as a new student.

## 6. SFTP server and test uploads

CHSS creates an SFTP account for each partner District. Credentials go to one designated technical contact, who may share them within the District.

| Item | Entry |
|---|---|
| Host | [sftp.chss.example] |
| Port | 22 |
| Authentication | SSH key. Send your public key to your integration contact; CHSS does not issue passwords by email. |
| Home directory | `/` (appears as root). Subdirectories: `/automated`, `/test`, `/code_tables`, `/archive` (read-only; your last ninety days of received files). |
| Host key | Published at [URL]; rotated [annually] with thirty days' notice (Section 6.6). |

**SIS vendor connection.** For [SIS vendors supported: list], the vendor can deliver a scheduled export directly to CHSS. The District authorizes it in the vendor's console; CHSS and the vendor configure it; the files that arrive are the same schemas as below. Ask before building your own export.

**No upload UI.** CHSS does not offer a manual upload tool for live data (Exhibit D-2 lists the two automated forms only). The `/test` directory is for checking an export before you schedule it.

Email is never used for Student Data, in either direction.

## 7. Rostering: schools, students, staff

### 7.1 schools.csv

| | |
|---|---|
| Purpose | Defines the schools whose students are in scope and the codes every other file uses. |
| Filename | `schools.csv` |
| What to include | Every participating school (Agreement Section Seven). |
| What to exclude | Schools with no participating students. |
| Minimum frequency | Once, then when it changes. |
| Partial data | Replacing. A school absent from a new file is archived; its students stop loading. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `school_sis_id` OR `school_number` OR `school_state_id` | Yes (one) | String (50) | The school identifier the District chose in Section 5. |
| `nces_school_id` | No | String (12) | National identifier; helps CHSS match state assessment files. |
| `name` | Yes | String (100) | Full name of the school. |
| `short_name` | No | String (40) | For dashboards. |
| `low_grade` | No | Integer | Lowest grade offered. |
| `high_grade` | No | Integer | Highest grade offered. |

### 7.2 students.csv

| | |
|---|---|
| Purpose | The roster: who is in scope, where, and the demographics the District provides for subgroup reporting. |
| Filename | `students.csv` |
| What to include | All 9th grade students at participating schools, plus every prior Cohort's students still enrolled (Section 6.3). One row per student. |
| What to exclude | Students in grades not covered. A student enrolled at two schools: one row, the school of record. |
| Minimum frequency | Weekly during the school year; as changes occur is better. |
| Partial data | Replacing. A student absent from a new file is marked exited as of the file date; their history is kept for Cohort tracking. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | The District's chosen identifier. Stable across years. |
| `student_state_id` | No | String (64) | State-issued identifier, where held, if not the primary. |
| `first_name` | Yes | String (100) | Proper case. |
| `last_name` | Yes | String (100) | Proper case. |
| `middle_name` | No | String (100) | |
| `preferred_first_name` | No | String (100) | Shown to the 9th Grade Success Team where provided. |
| `{school identifier}` | Yes | String (50) | Column header is `school_sis_id`, `school_number`, or `school_state_id`, matching schools.csv. |
| `grade_year` | Yes | Integer | 9 through 12. |
| `cohort_year` | Yes | Integer | The school year (ending year) the student first entered 9th grade. Drives Cohort tracking. |
| `enrollment_status` | Yes | String | `active`, `exited`, `transferred`, `graduated`. |
| `entry_date` | Yes | Date | Current enrollment entry date. |
| `exit_date` | No | Date | When exited. |
| `exit_reason` | No | String | District's code; code table optional. |
| `gender` | Yes | String (1) | `M`, `F`, `N` (non-binary, other, or unspecified). |
| `race_ethnicity` | Yes | String | Federal seven categories, or the District's codes with a code table. |
| `el_status` | Yes | String | `el`, `not_el`, `reclassified`. |
| `el_reclassified_date` | No | Date | Where held. |
| `iep_status` | Optional, elected | String | `yes` or `no`. Only where the District elects it in Exhibit D-3. |
| `section_504_status` | Optional, elected | String | `yes` or `no`. Only where elected. |
| `economic_status` | Optional, elected | String | `free`, `reduced`, `none`. Only where elected. |
| `date_of_birth` | Optional | Date | Only where identifiers are unavailable for matching. [If the screeners match on date of birth, this becomes Required; confirm Friday.] |

### 7.3 school_staff.csv

| | |
|---|---|
| Purpose | Creates Navigator accounts for District staff and removes them when access should end (Agreement Section 6.8). Also supplies teacher of record for student_courses.csv. |
| Filename | `school_staff.csv` |
| What to include | Every District staff member who should have Navigator access, and every teacher of record referenced in student_courses.csv (with `navigator_access` = `no` where they do not get a login). |
| What to exclude | Staff with no Navigator role and no course of record. |
| Minimum frequency | As it changes. Removing a departed user depends on this file. |
| Partial data | Replacing. A user absent from a new file loses access at the next load. Manually created CHSS coach accounts are not affected. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `staff_sis_id` OR `staff_id` OR `teacher_number` | Yes (one) | String (64) | The District's chosen staff identifier. |
| `first_name` | Yes | String (100) | |
| `last_name` | Yes | String (100) | |
| `email` | Yes | String (100) | Work email; the Navigator username. |
| `position` | Yes | String (255) | As the District titles it: "Counselor", "Assistant Principal", "9th Grade Seminar Teacher". |
| `role` | Yes | String | `school_leader`, `team_lead`, `team_member`, `district_user`, `teacher_of_record_only`. Roles define what the user can see; see Navigator roles in the technical documentation. |
| `access_type` | Yes | String | `district` (all participating schools) or `school`. |
| `{school identifier}_list` | Yes if `access_type` = `school` | Comma-separated list, quoted | Schools the user may see. |
| `navigator_access` | Yes | String | `yes` or `no`. `no` for teachers of record who do not need a login. |

## 8. Student data schemas

Files marked 🎯 feed the on-track indicators and are Required under Exhibit D-1. Each schema states whether it is replacing or additive.

### 8.1 🎯 student_courses.csv (courses, marks, and credits)

| | |
|---|---|
| Purpose | Every course each student has taken or is taking, with the mark and credit awarded when the course closes. This one file carries course enrollments, final marks, and credits earned (Exhibit D-1 rows 4 to 6). |
| Filename | `student_courses.csv` |
| What to include | All courses for every student in students.csv, for the current school year and all prior high school years (and 8th grade where the District holds it). Include failed and withdrawn courses. Include summer school courses with `academic_term` = `summer`. |
| What to exclude | Elementary courses. Non-credit placeholders (lunch, homeroom) unless the District wants attendance by period for them. |
| Minimum frequency | After each grading period closes; nightly or weekly is better so schedule changes reach the Team. |
| Partial data | Replacing. Send the entire set each time; a course absent from a later file is removed. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `course_id` | Yes | String (64) | The District's course code. Transfer courses may carry an identifier not in the District's catalog. |
| `course_name` | Yes | String (100) | Quoted. |
| `course_subject` | No | String (100) | Department or subject. Used to classify core courses when `core_course` is blank. |
| `core_course` | No | Integer | `1` if the District classifies the course as core (English, math, science, social studies); `0` otherwise. |
| `section_id` | Yes | String (64) | Unique per section per school year. Joins progress_marks.csv and attendance_period.csv. |
| `{school identifier}` | Yes | String (50) | School offering the course. |
| `school_year` | Yes | Integer | Four-digit ending year. |
| `grade_year` | Yes | Integer | Grade the student was in when taking the course. |
| `academic_term` | Yes | String | Term code from the terms code table (`1`, `2`, `summer`, etc.). The term the course started in. |
| `teacher_of_record` | No | String (64) | Staff identifier matching school_staff.csv. |
| `credit_possible` | Yes | Decimal | Credits the course awards on passing. |
| `credit_awarded` | Conditionally | Decimal | Credits earned. Required once the course has closed; blank while in progress. `0` for a failed course. |
| `grade_achieved` | Conditionally | String | Final mark as the SIS stores it (letter or numeric). Required once the course has closed; blank while in progress. |
| `numerical_grade_achieved` | No | Decimal | Numeric equivalent where the mark is a letter. |
| `enrollment_status` | Yes | String | `enrolled`, `completed`, `withdrawn`, `transferred_in`. |
| `enrollment_entry_date` | Yes | Date | |
| `enrollment_exit_date` | No | Date | For schedule changes and withdrawals. |
| `cte_flag` | No | Integer | `1` where the District's catalog flags the course CTE. |
| `dual_credit_flag` | No | Integer | `1` where the catalog flags dual credit or dual enrollment. Many catalogs do not carry this; leave blank and use program_participation.csv for dual-credit completion. |
| `pathway_code` | No | String | Where the catalog carries it. |
| `credit_recovery_flag` | No | Integer | `1` where the enrollment is a credit-recovery course, including mid-year recovery (Exhibit D-1). |

### 8.2 🎯 progress_marks.csv (marks by grading period)

| | |
|---|---|
| Purpose | In-progress marks during the year, so the Team sees a student slipping before the semester closes. The on-track indicator uses these between final marks. |
| Filename | `progress_marks.csv` |
| What to include | One row per student per section per grading period, for the current school year, each time a grading period's marks post. |
| What to exclude | Final marks (they belong in student_courses.csv). |
| Minimum frequency | After each progress report or grading period; weekly where the SIS computes running marks. |
| Partial data | Additive. Each file adds or updates the marks it contains for the grading periods it names; earlier grading periods are kept. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `section_id` | Yes | String (64) | Joins student_courses.csv. |
| `school_year` | Yes | Integer | Ending year. |
| `grading_period` | Yes | String | Code from the terms code table (`q1`, `pr1`, `s1`). |
| `mark` | Yes | String | As the SIS stores it. |
| `mark_type` | Yes | String | `progress`, `quarter`, `semester`. |
| `as_of_date` | Yes | Date | The date the mark was posted or computed. |
| `passing` | No | Integer | `1`/`0` if the SIS stores it; otherwise CHSS derives it from the grading scale. |

### 8.3 🎯 gpa.csv

| | |
|---|---|
| Purpose | Cumulative GPA by term for the on-track calculation and for Cohort analysis. |
| Filename | `gpa.csv` |
| What to include | GPA values for all current students, one row per student per term. |
| What to exclude | Students not in students.csv. |
| Minimum frequency | After each term's marks are released. |
| Partial data | Replacing within a term: each file is the complete source of truth for the terms it names. A student absent from the file for a named term is shown as having no GPA for that term. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `school_year` | Yes | Integer | Ending year. |
| `academic_term` | Yes | String | Term code. |
| `credits_attempted_term` | Yes | Decimal | For the term. |
| `credits_earned_term` | Yes | Decimal | For the term. |
| `credits_earned_cumulative` | Yes | Decimal | As of term end. |
| `gpa_unweighted` | Yes | Decimal | On the District's scale; scale in the grading-scale code table. |
| `gpa_weighted` | No | Decimal | Where the District computes one. |
| `gpa_denominator` | No | Decimal | 4.0, 5.0, 100; overrides the District setting if sent. |

### 8.4 🎯 attendance_daily.csv

| | |
|---|---|
| Purpose | Daily attendance events, from which CHSS computes attendance rate by grading period and chronic absence (ten percent or more of enrolled days). Daily grain lets the Team see a pattern forming; a count cannot. |
| Filename | `attendance_daily.csv` |
| What to include | One row per student per school day with a non-present code (absent or tardy, excused or not). Present days are implied by the calendar in the terms code table. Districts that prefer to send every day, including present, may; CHSS accepts both. |
| What to exclude | Days before the student's `entry_date`. |
| Minimum frequency | Weekly during the school year; nightly preferred. |
| Partial data | Additive by date: each file adds or updates the dates it contains. Send at least the last fourteen days each time so late corrections arrive. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `{school identifier}` | Yes | String (50) | |
| `attendance_date` | Yes | Date | |
| `attendance_code` | Yes | String | District's code, classified in the attendance code table as absent/tardy/present and excused/unexcused. |
| `minutes_absent` | No | Integer | Where held. |

**Alternative: attendance_period.csv.** Districts that take period attendance may send one row per student per date per `section_id` with the same columns plus `period`; CHSS derives daily. **Alternative: attendance_summary.csv.** Where only counts are available, one row per student per grading period with `days_enrolled`, `days_absent_excused`, `days_absent_unexcused`, `tardies`. Counts support the chronic-absence flag but not the weekly trend; use them only where daily grain cannot be exported.

### 8.5 🎯 Summer school

Summer school and credit recovery are sent in student_courses.csv: summer school with `academic_term` = `summer`, credit recovery with `credit_recovery_flag` = `1` in whatever term it ran, and `school_year` = the ending year of the school year the credit applies to, with `credit_awarded` and `grade_achieved` filled in when the course closes. No separate file. Districts whose summer school runs on a separate SIS instance may send a separate `student_courses_summer.csv` with the same schema.

### 8.6 🎯 state_assessments.csv

| | |
|---|---|
| Purpose | State assessment scores, including incoming 8th grade ELA and math, to identify risk before the first grading period (Exhibit D-1). |
| Filename | `state_assessments.csv` |
| What to include | All state assessment scores held for students in students.csv, including grade 8 scores for incoming 9th graders. One row per student per test per administration. |
| What to exclude | District benchmark or interim assessments (not requested). |
| Minimum frequency | When new scores are released; the 8th grade scores for an incoming Cohort before the first day of Year 1 instruction. |
| Partial data | Additive. Scores are added or updated, never removed by omission. One score per student per test per administration date. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `test_name` | Yes | String | State assessment name as the state reports it (for example `AASA`, `ACT Aspire`, `SBAC`, `STAAR`). |
| `subject` | Yes | String | `ela`, `math`, `science`, `other`. |
| `administration_date` | Yes | Date | Or the last day of the testing window. |
| `grade_tested` | Yes | Integer | |
| `scale_score` | Yes | Decimal | |
| `performance_level` | Yes | String | The state's level label or number. |
| `percentile` | No | Decimal | Where the state reports one. |

### 8.7 sat_act.csv (Optional)

| | |
|---|---|
| Purpose | College admissions test scores where the District holds them. Optional under Exhibit D-1; usually delivered by the testing company rather than the SIS. |
| Filename | `sat_act.csv` |
| What to include | PSAT, SAT, PreACT, and ACT scores for current students. |
| Minimum frequency | When scores from new test dates are available. |
| Partial data | Additive. One score per student per test type per test date. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `test_type` | Yes | String | `PSAT`, `SAT`, `PreACT`, `ACT`. |
| `test_date` | Yes | Date | |
| `grade_year` | No | Integer | Grade when tested. |
| `composite` | Yes | Integer | Total or composite score. |
| `reading_writing` | No | Integer | SAT and PSAT. |
| `math` | No | Integer | SAT, PSAT, ACT. |
| `english` | No | Integer | ACT. |
| `reading` | No | Integer | ACT. |
| `science` | No | Integer | ACT. |

### 8.8 discipline.csv (Optional, elected)

| | |
|---|---|
| Purpose | Discipline incidents, only where the District elects them in Exhibit D-3 for an evaluation outcome. Not used for the on-track indicator. |
| Filename | `discipline.csv` |
| What to include | One row per incident for students in students.csv, current school year. |
| What to exclude | Narrative text. Send codes and outcomes only. |
| Minimum frequency | Monthly, or with each weekly feed. |
| Partial data | Additive. Incidents are added or updated by `incident_id`, never removed by omission. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `incident_id` | Yes | String (64) | Unique per incident. |
| `incident_date` | Yes | Date | |
| `incident_type` | Yes | String | District's code; discipline code table. |
| `action_taken` | Yes | String | `referral`, `iss`, `oss`, `expulsion`, `other`. |
| `days_removed` | No | Decimal | |

### 8.9 program_participation.csv (Optional)

| | |
|---|---|
| Purpose | CTE pathway enrollment and completion, industry-recognized credentials, and dual-credit completion, where the District holds them (Exhibit D-1). These usually sit outside the SIS, so this file is separate from student_courses.csv. |
| Filename | `program_participation.csv` |
| What to include | One row per student per program, credential, or dual-credit course. |
| Minimum frequency | Each semester, or when records are updated. |
| Partial data | Additive by `record_id`. |

| Column name | Required | Data type | Description |
|---|---|---|---|
| `student_sis_id` OR `student_number` OR `student_state_id` | Yes (one) | String (64) | |
| `record_id` | Yes | String (64) | Unique per row; stable across loads. |
| `program_type` | Yes | String | `cte_pathway`, `industry_credential`, `dual_credit`. |
| `program_name` | Yes | String (255) | Pathway, credential, or course name. Quoted. |
| `cip_code` | No | String | For CTE pathways. |
| `status` | Yes | String | `enrolled`, `concentrator`, `completer`, `earned`, `attempted`. |
| `status_date` | Yes | Date | |
| `college_credit_hours` | No | Decimal | For dual credit. |

### 8.10 Screening data

The Belonging and Skills screeners are student surveys completed in Navigator, collected by CHSS rather than sent by the District (Exhibit D-1). The District approves the instruments and provides any required notice or consent before collection opens at a school, and District staff (Seminar teachers, Team Leads, or administrators) open each screening window (Agreement Section 6.7). [Emily to confirm what the student enters to be matched to the roster (date of birth, a claim code, or a roster-generated link). If it is date of birth, `date_of_birth` in students.csv becomes Required. This section is completed once that is confirmed.]

### 8.11 Code tables (sent once, in `/code_tables`)

| File | Columns | Notes |
|---|---|---|
| `grading_scale.csv` | `mark`, `numeric_equivalent`, `passing` (1/0), `gpa_points_unweighted`, `gpa_points_weighted` | One row per mark the SIS can store. Pass/fail marks included. |
| `terms.csv` | `{school identifier}`, `school_year`, `term_code`, `term_name`, `start_date`, `end_date`, `grading_period_code`, `grading_period_name`, `grading_period_end_date`, `school_days` | One row per grading period per school. `school_days` lets CHSS compute attendance rate. |
| `attendance_codes.csv` | `attendance_code`, `description`, `category` (`present`, `absent`, `tardy`), `excused` (1/0), `counts_toward_chronic` (1/0) | Every code the SIS uses. |
| `discipline_codes.csv` | `incident_type`, `description`, `severity` | Only where discipline is elected. |

## 9. Validation, error notifications, and acceptance

**On arrival.** Every file is virus-scanned and logged. The technical contact receives an automated receipt within [one hour] of a file landing in `/automated`.

**Validation.** Three checks, in order: structure (expected columns present, types parse, dates valid); keys (every student in a child file exists in students.csv; every `section_id` in progress_marks.csv exists in student_courses.csv; every school code in schools.csv; identifier column matches the District's setting); plausibility (marks on the grading scale; credits not above `credit_possible`; attendance dates inside the calendar).

**Validation report.** Emailed to the technical contact after every load: files accepted or rejected, rows rejected with the row number and reason, and warnings. A rejected file is not loaded. A rejected row is skipped and listed. Reports for the last ninety days are also in `/archive`.

**Error notifications.** If a scheduled file does not arrive within [24 hours] of its expected time, or arrives and is rejected, CHSS notifies the technical contact within one business day and helps diagnose it (Agreement Section 6.9).

**Thresholds for a live load.** No rejected files; rejected rows below [one percent]; warnings reviewed. Thresholds are agreed in writing at the onboarding call (Exhibit D-3).

**Test load and acceptance.**

| Step | What | When |
|---|---|---|
| Onboarding call | Walk this guide; confirm SIS, export tooling, identifier choice, code tables, schedule; exchange SSH key | Within two weeks of acceptance into the program |
| Test load | Current-year files in `/test`; CHSS returns the validation report and a mapping confirmation (which SIS value became which CHSS value) | After the Agreement is executed; no Student Data before then |
| Corrections | Fix exports or code tables; repeat | As needed |
| Acceptance test | A full load of the Required files for all participating schools in `/automated`, within thresholds, with on-track indicators reviewed by the 9th Grade Success Team against what the school knows | At least thirty days before Year 1 instruction |
| Go live | Scheduled feed runs; weekly updates | First day of Year 1 instruction |

CHSS reports apparent errors in source data and never alters it; corrections are made in the SIS and arrive with the next feed (Agreement Section 6.2).

## 10. School year rollover and changing your SIS

**Rollover.** Before the new school year: send a new terms.csv; confirm `cohort_year` is set for incoming 9th graders; expect `section_id` values to change (they are unique per school year, so this is normal); send the 8th grade state assessment scores for the incoming Cohort. Students who graduated or exited stay in students.csv with their `exit_date` and `enrollment_status`, so Cohort tracking continues.

**Changing SIS or export tooling.** Tell your integration contact before the change. The identifier choice in Section 5 usually survives a migration only if the new SIS carries the old key; if not, send a one-time crosswalk file (`old_id`, `new_id`) so CHSS can preserve history. CHSS gives thirty days' notice before changing any schema (Agreement Section 6.6), never mid-year without the District's agreement.

## 11. Getting your data back, and deletion

**Your data, on request.** The District may ask at any time for an export of the Student Data CHSS holds for it, in CSV, within [ten business days]. The 9th Grade Success Team's intervention records and notes created in Navigator are included; they are Student Data under the Agreement (Exhibit D-1).

**Deletion.** On the District's written directive (Exhibit D-4, or the NDPA's directive) or at termination, CHSS returns or destroys the District's Student Data within sixty days and certifies it in writing (Appendix A.10). De-identified data created under A.10 is not affected.

## Questions districts ask

- **We cannot produce one of the Required files.** Tell us which. Most gaps have a workaround (credits from marks and `credit_possible`; attendance from a summary). A Required element the District does not hold at all is noted in Exhibit D-3 and does not block acceptance.
- **Our grading periods differ by school.** terms.csv is per school.
- **We take attendance by period only.** Send attendance_period.csv; CHSS derives daily.
- **Our SIS exports Excel.** Accepted in `/test`. For the live feed, export CSV; nearly every SIS can.
- **A student transfers mid-year.** Send `exit_date` and `exit_reason` in students.csv; the record stays in the Cohort for outcome tracking under Section 6.3.
- **Who at CHSS sees these files?** A small set of named CHSS technical staff, for the load and for support (Appendix A.7). Coaches see Navigator, not files. Program and research staff see de-identified data only.
