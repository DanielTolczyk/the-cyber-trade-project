# RFC 0003: Mandatory Mentorship Quotas and Instructional Runtime Requirements

* **Status:** Draft
* **Author(s):** Daniel Tolczyk (@DanielTolczyk)
* **Related Specifications:** `framework/apprenticeship-standards.md`, `framework/supervisory-ratios.md`, `framework/licensure-and-progression.md`
* **Created:** 2026-08-27

---

## 1. Executive Summary

The traditional corporate technology model creates structural disincentives for senior engineers to train newcomers. Key contributors are evaluated almost exclusively on ticket velocity, feature delivery, and uptime metrics. Mentorship is treated as an uncompensated, informal tax that slows down senior individual contributors, resulting in institutional knowledge hoarding, high burnout, and an entry-level tier left to navigate production systems without meaningful guidance.

In traditional craft trades, holding a Journeyman or Master license carries an enforceable obligation to train the next generation. Technical mastery is not merely the ability to execute complex operations alone; it is the proven ability to transfer operational competency down the line.

This RFC proposes establishing mandatory **Verified Mentorship Runtime Quotas** for all Licensed Journeymen and Master Practitioners. Under this rule, maintaining an active license in good standing and advancing from Journeyman to Master requires logging a verified quota of direct, human-in-the-loop instructional hours with registered apprentices, enforced through cryptographically signed dual-entry logbooks.

---

## 2. Motivation & Trade Context

* **Knowledge Silos and Hero Culture:** High-performing senior engineers often become single points of failure because organizations prioritize short-term ticket resolution over long-term knowledge transfer.
* **Informal & Uncredited Labor:** When senior engineers do take time to mentor, it is rarely tracked or rewarded in compensation or career advancement, causing mentoring to be the first activity dropped during operational surges.
* **The Master Tier Elevation Gap:** Current trade standards require 12,000 operational runtime hours to achieve Master Practitioner standing. However, raw hours alone do not measure pedagogical capability, leadership, or the ability to uphold trade safety standards across a team.
* **Underwriter Risk:** A team with isolated senior "wizards" and untrained juniors has a fragile operational profile. Insurers benefit when defensive tradecraft is systematically distributed across all shifts and tiers.

---

## 3. Detailed Specification & Proposed Architecture

### A. Annual Instructional Runtime Quotas (IQR)
To maintain an active license in good standing, practitioners must allocate a baseline percentage of their annual operational runtime to verified apprentice mentorship:

| License Tier | Minimum Annual Mentorship Requirement | Eligible Instructional Modalities |
| :--- | :--- | :--- |
| **Licensed Journeyman** | **10% of annual runtime** (~200 hrs/year) | 1:1 / 2:1 pair triage, script/tool review, live packet analysis, incident post-mortem walkthroughs. |
| **Master Practitioner** | **15% of annual runtime** (~300 hrs/year) | Architecture threat modeling reviews, formal RTI classroom instruction, high-risk operational oversight. |
| **Master of Record (MoR)** | **20% of annual runtime** (~400 hrs/year) | Structured apprentice evaluations, safety non-concurrence drills, rotational domain logbook auditing. |

### B. Master Advancement Prerequisite (The "Legacy Gate")
To advance from Licensed Journeyman (8,000 hrs) to Master Practitioner (12,000 hrs), the candidate must:
1. Complete a minimum of **800 verified instructional runtime hours** logged during their Journeyman tenure.
2. Have served as the primary or designated co-mentor for at least **one apprentice through a complete rotational tier advancement** (e.g., guiding a Tier 1 to Tier 2, or Tier 3 to Tier 4).

### C. Mutual Dual-Sign Logbook Protocol
To eliminate paper-pencil fraud and unilateral time falsification, mentorship hours are recorded via a dual-attestation entry containing the following mandatory schema fields:
* `mentorship_record_id`: Unique cryptographic identifier
* `mentor_license_id`: Licensed Journeyman or Master identifier
* `apprentice_id`: Registered apprentice identifier
* `rotational_domain`: Domain 1 through 5 matching the Apprenticeship Standard
* `instructional_focus`: Narrative breakdown of active pairing, review, or triage
* `runtime_hours`: Precise duration of instructional contact
* `timestamp_start` / `timestamp_end`: ISO 8601 operational runtime stamps
* `mentor_signature` / `apprentice_signature`: Mutual cryptographic attestations

**Validation Mechanics:**
* **Mutual Lock:** An entry is only valid when cryptographically or physically countersigned by both the mentor and the apprentice.
* **Audit Sampling:** Regional JATC boards sample mentorship logs during quarterly wage tier and triennial license renewals.

### D. Solo Practitioner & Low-Apprentice Environment Waivers
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

* **International Brotherhood of Electrical Workers (IBEW) / UA:** Journeymen are contractually responsible for direct on-the-job training of apprentices; advancement to Master and Foreman status requires demonstrated leadership and apprentice guidance.
* **Medical Residency & Attending Physicians:** Attending physicians cannot maintain clinical faculty standing solely by seeing patients; they must supervise, scrub in with, and evaluate residents during procedures.
* **Aviation (CFI / Pilot in Command):** Airline Transport Pilot (ATP) and Commercial ratings heavily weigh Dual Instruction Given hours; flight instructors maintain specific logs validated by student sign-offs.

---

## 6. Implementation & Roadmap

* **Impacted Specifications:**
  * Update `framework/apprenticeship-standards.md` to incorporate the Mutual Dual-Sign Logbook Protocol.
  * Update `framework/supervisory-ratios.md` Section 4 to include Instructional Quotas.
  * Update `framework/licensure-and-progression.md` to formally add the 800-hour instructional prerequisite to the Master Practitioner tier.
* **Release Target:** Staged for **`release/v1.3.0`** as a core governance enhancement.