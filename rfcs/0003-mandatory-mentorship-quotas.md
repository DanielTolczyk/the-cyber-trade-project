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
* **Annual Instructional Runtime Quotas (IQR):** Setting annual mentorship benchmarks (10% Journeyman, 15% Master, 20% MoR) for active license maintenance.
* **Mutual Dual-Sign Logbook Protocol:** Eliminating time falsification via cryptographically bound bilateral attestation blocks.
* **Solo Practitioner & Low-Apprentice Environment Waivers:** Providing JATC guest instruction and open-source review alternative pathways.

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

### C. Annual Instructional Runtime Quotas (IQR)
To maintain an active license in good standing, practitioners allocate a baseline percentage of their annual operational runtime to verified apprentice mentorship:

| License Tier | Minimum Annual Mentorship Requirement | Eligible Instructional Modalities |
| :--- | :--- | :--- |
| **Licensed Journeyman** | **10% of annual runtime** (~200 hrs/year) | 1:1 / 2:1 pair triage, script/tool review, live packet analysis, incident post-mortem walkthroughs. |
| **Master Practitioner** | **15% of annual runtime** (~300 hrs/year) | Architecture threat modeling reviews, formal RTI classroom instruction, high-risk operational oversight. |
| **Master of Record (MoR)** | **20% of annual runtime** (~400 hrs/year) | Structured apprentice evaluations, safety non-concurrence drills, rotational domain logbook auditing. |

### D. Mutual Dual-Sign Logbook Protocol
Mentorship hours cannot be logged unilaterally. To prevent ghost-logging and maintain actuarial integrity:
* Both the mentor and apprentice maintain a linked digital logbook entry containing the following mandatory schema fields:
  * `mentorship_record_id`: Unique cryptographic identifier
  * `mentor_license_id`: Licensed Journeyman or Master identifier
  * `apprentice_id`: Registered apprentice identifier
  * `rotational_domain`: Domain 1 through 5 matching the Apprenticeship Standard
  * `instructional_focus`: Narrative breakdown of active pairing, review, or triage
  * `runtime_hours`: Precise duration of instructional contact
  * `timestamp_start` / `timestamp_end`: ISO 8601 operational runtime stamps
  * `mentor_signature` / `apprentice_signature`: Mutual cryptographic attestations
* **Validation Mechanics:** An entry is valid only when cryptographically countersigned by both the mentor and the apprentice.
* **Audit Sampling:** Regional JATC boards sample mentorship logs during quarterly wage tier and triennial license renewals.

### E. Solo Practitioner & Low-Apprentice Environment Waivers
In environments where an employer does not host registered apprentices (e.g., small boutique consulting units, solo contract work):
* **JATC Guest Instruction:** Journeymen and Masters may satisfy their annual quota by teaching accredited RTI lab modules at local community colleges, vocational high schools, or JATC training centers.
* **Public Open-Source Mentorship:** Proctored code reviews, patch guidance, and architecture reviews for apprentices working on accredited open-source defensive security tools count at a 1:1 hourly rate (capped at 50% of annual quota).

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
  1. Should the on-shift instructional wage differential be structured as a flat hourly dollar adder (+$2.50 to +$5.00/hr) or a percentage premium (+5% RJPB)?
  2. How should Taft-Hartley JATC Training Trust funds be allocated to subsidize employer instructional differential costs?
  3. Should annual Instructional Runtime Quotas (10%/15%/20%) be integrated into the triennial CTD renewal hours (120 hrs/3 yrs)?
  4. What specific supervisory telemetry should be fed to cyber insurance underwriters to verify active ratio compliance for preferred premium credits?