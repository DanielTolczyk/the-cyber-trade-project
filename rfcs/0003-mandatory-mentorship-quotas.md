# RFC 0003: Mandatory Mentorship Quotas, Instructional Wage Differentials & Supervisor Liability Allocation

* **Status:** Draft (Open for Community Review)
* **Author(s):** Daniel Tolczyk (@DanielTolczyk)
* **Related Specifications:** `framework/wage-scales.md`, `framework/licensure-and-progression.md`, `framework/supervisory-ratios.md`, `framework/apprenticeship-standards.md`, `governance/guild-formation-and-charter.md`
* **Created:** 2026-08-27
* **Updated:** 2026-09-01
* **Discussion Thread:** [GitHub Discussion #11](https://github.com/DanielTolczyk/the-cyber-trade-project/discussions/11)

---

## 1. Executive Summary

The traditional corporate technology model creates structural disincentives for senior engineers to train newcomers. Key contributors are evaluated almost exclusively on ticket velocity, feature delivery, and uptime metrics. Mentorship is treated as an uncompensated, informal tax that slows down senior individual contributors, resulting in institutional knowledge hoarding, high burnout, and an entry-level tier left to navigate production systems without meaningful guidance.

In physical skilled craft trades (such as electrical and pipefitting), holding a Journeyman or Master license carries both an enforceable obligation and a financial incentive to train the next generation:
1. Senior practitioners receive an **Instructional Wage Differential** (+$/hr or +% premium) while actively supervising apprentices on production shifts.
2. The differential is justified because the supervising Journeyman's license bears technical accountability for the work executed under their oversight.
3. Attaining Master Practitioner standing requires verified proof of having successfully mentored and advanced apprentices.

This RFC proposes establishing a comprehensive Tripartite Mentorship & Instructional Standard:
* **On-Shift Instructional Wage Differentials:** Establishing a mandatory +$2.50 to +$5.00/hr (or +5% RJPB) supervisory differential for active line-of-sight apprentice supervision.
* **Supervisory Liability & Safe Harbor Boundaries:** Codifying vicarious technical responsibility and clear negligence thresholds.
* **Certified Trade Instructor (CTI) Endorsement:** Creating a recognized vocational teaching credential and career transition safety valve.
* **Mandatory Verified Mentorship Runtime Quotas:** Requiring verified instructional hours for Master Practitioner elevation.

---

## 2. Motivation & Trade Precedent

* **The "Velocity Tax" Penalty:** Explaining packet captures, conducting line-by-line code reviews, and supervising live containment commands consumes 25% to 40% of a senior engineer's attention. Without a dedicated wage differential, senior staff view assigned apprentices as a performance review penalty.
* **Supervisory Liability Justification:** When an apprentice executes production firewall changes or cloud IAM provisioning, the supervising Journeyman's license is on the line. Compensating supervisors reflects this heightened responsibility.
* **The Master Tier Definition:** In certified crafts, a "Master" is not merely an isolated high-performing technician; a Master is a recognized teacher capable of passing on tradecraft and safety standards to the next generation.
* **Career Transition Safety Valve:** During macroeconomic contractions or between contract engagements, credentialed instructors provide the JATC training network with experienced frontline faculty while maintaining personal income.

---

## 3. Detailed Specification & Proposed Architecture

### A. On-Shift Instructional Wage Differential
To eliminate the economic disincentive to train, a Licensed Journeyman designated as the on-duty supervisor for one or two registered apprentices (2:1 ratio) receives an **Instructional Differential**:

* **Differential Scale:** **+$2.50 to +$5.00/hr** (or a flat **+5% above prevailing Journeyman RJPB**) applied for all hours with active apprentice oversight.
* **Funding Models under Debate:**
  * *Option A (Direct Employer Payroll):* Funded by the sponsoring employer as part of standard shift operational costs.
  * *Option B (JATC Training Trust Subsidy):* Partially subsidized through the multi-employer Taft-Hartley JATC Training Trust fund.

### B. Supervisory Liability & Safe Harbor Allocation
Compensated supervision carries legal and regulatory accountability:
* **The Supervision Safe Harbor:** If an apprentice commits an operational mistake during guided instruction where the supervisor maintained active line-of-sight oversight, the event is protected under standard trade safe harbor as a training error.
* **Supervisory Negligence Boundary:** Leaving an apprentice to perform solo production changes on a classified, high-consequence, or Tier-I network without active oversight constitutes **Class-B Supervisory Negligence**, subjecting the supervisor's license to Board review.

### C. Certified Trade Instructor (CTI) Credential
A standardized JATC pedagogical endorsement for Journeymen and Masters:
* **Curriculum Modules:** Adult vocational pedagogy (36 hrs), hands-on cyber range simulation management (36 hrs), rubric-based evaluation integrity (36 hrs), and anti-harassment/training ethics (36 hrs).
* **Operational Privileges:** Qualifies practitioners to serve as paid classroom RTI faculty at public community college JATC labs, providing stable employment during career transitions or industry downturns.

### D. Master Elevation Prerequisite (The Legacy Gate)
To advance from Licensed Journeyman (8,000 hrs) to Master Practitioner (12,000 hrs):
* **Quota:** Candidate must log a minimum of **500 to 800 verified instructional runtime hours** supervising registered apprentices under Modality A or B.
* **Verification:** Logged via the Mutual Dual-Sign Logbook Protocol, requiring cryptographic countersignatures from supervised apprentices.

---

## 4. Drawbacks, Edge Cases & Risk Analysis

* **Tokenism & Ghost Mentoring:** Supervising engineers might sit in the same room with apprentices while working in total isolation, claiming passive hours as active instruction. 
  * *Mitigation:* The standard strictly defines eligible modalities (pairing, active walkthroughs, live triage) and empowers apprentices to review and approve specific task descriptions in the dual-sign logbook.
* **Operational Velocity Friction:** High-tempo incident response teams during major crises cannot always pause to explain concepts.
  * *Mitigation:* Active Incident Surges carry temporary emergency exemptions; instructional hours are averaged over a rolling 12-month calendar year rather than weekly mandates.
* **Administrative Overhead:** Logging hourly instructional breakdowns could add friction to daily operations.
  * *Mitigation:* Integrated logbook tracking natively within standard ticketing/time-tracking workflows (e.g., tagging a peer-review or pair-programming ticket as `+mentorship`).

---

## 5. Prior Art & Real-World Precedents

* **International Brotherhood of Electrical Workers (IBEW) / UA:** Journeymen are contractually responsible for direct on-the-job training of apprentices and receive Foreman/Lead premiums when supervising crews.
* **Medical Residency & Attending Physicians:** Attending physicians cannot maintain clinical faculty standing solely by seeing patients; they must supervise, scrub in with, and evaluate residents during procedures.
* **Aviation (CFI / Pilot in Command):** Airline Transport Pilot (ATP) and Commercial ratings heavily weigh Dual Instruction Given hours; flight instructors maintain specific logs validated by student sign-offs.

---

## 6. Implementation & Feedback Areas

* **Questions for Community Review:**
  1. Should the instructional wage differential be structured as a flat hourly dollar adder (+$2.50 to +$5.00/hr) or a percentage rate (+5% RJPB)?
  2. Is 500 hours or 800 hours the optimal instructional threshold for Master Practitioner elevation?
  3. Should CTI credential holders receive preferred dispatch ranking for JATC academic training roles?