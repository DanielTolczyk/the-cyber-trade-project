# RFC 0004: Transitional Supervisory Ratios, Progressive Supervision & Employer Variance Procedures

* **Status:** Draft (Open for Community Review)
* **Author(s):** Daniel Tolczyk (@DanielTolczyk)
* **Related Specifications:** `framework/supervisory-ratios.md`, `framework/apprenticeship-standards.md`, `governance/transition-plan.md`, `pillars/03_rotational-pipeline.md`, `governance/craft-guild-charter.md`
* **Created:** 2026-09-05
* **Updated:** 2026-09-05
* **Discussion Thread:** [GitHub Discussion #85](https://github.com/the-cyber-trade-project/framework/discussions/85)

---

## 1. Executive Summary

A central challenge in establishing a registered cybersecurity trade is the initial structural imbalance between entry-level labor supply and qualified journeyworker availability. Modern cybersecurity organizations face an inverted talent pyramid: hundreds of thousands of entry-level candidates seeking employment, contrasted with an acute scarcity of experienced senior practitioners qualified to serve as designated supervisors.

Under Title 29 CFR Part 29 and traditional trade models, strict apprentice-to-journeyworker ratios prevent employers from replacing qualified workers with cheap, unsupervised labor. The current core specification mandates a **2:1 operational shift ratio** (maximum 2 apprentices per 1 licensed Journeyman). While vital for system safety, uninsurable error mitigation, and instructional integrity, applying an unyielding 2:1 ratio on Day 1 across all defensive operational environments threatens to create an intake bottleneck where employers cannot host apprentices because they lack licensed Journeymen on staff.

Conversely, blanket ratio deregulation or arbitrary dilution (e.g., 5:1 or 8:1) risks reviving the failure modes of corporate alert farms: low-wage novice labor performing unguided triage without instructional oversight, leading to operational fatigue, missed detections, and high turnover.

This RFC proposes four concrete mechanisms grounded directly in registered apprenticeship regulations (Title 29 CFR § 29.5(b)(7)), State Apprenticeship Council (SAC) variance precedents, and established joint apprenticeship programs:

1. **A 36-Month Transitional Ramp-Up Schedule:** A temporary ratio adjustment window synchronized with the 36-month Grandfathering Bridge, allowing initial organizational cohorts to scale journeyworker density before full statutory enforcement.
2. **Progressive Supervision Standards (Direct vs. General):** Formally distinguishing between mandatory direct line-of-sight supervision (2:1) for novice apprentices (Tiers 1 and 2) and general supervision (periodic audit and active reachability) for advanced apprentices (Tiers 3 and 4).
3. **The JATC Ratio Variance Petition Protocol (Employer Waivers):** A formal administrative procedure enabling employers with verified labor shortages to petition the Joint Apprenticeship and Training Committee (JATC) for time-limited, conditional ratio variances backed by mandatory cyber range simulation offsets.
4. **Empirical Standards Amendment Criteria:** Explicit statutory requirements based on 29 CFR § 29.3, requiring longitudinal insurer loss data and verified safety telemetry before any permanent modification of baseline trade ratios can be enacted by the National Board.


---

## 2. Motivation & Trade Precedents

### 2.1 The Market Formation Bottleneck
In an established physical trade (such as electrical or plumbing), the journeyworker-to-apprentice ratio functions in a mature labor market where licensed journeyworkers constitute 60% to 75% of the total trade workforce. In digital defense, the licensed labor pool begins at zero. Until experienced practitioners are processed through the Grandfathering Bridge (Tracks A, B, and C), employers attempting to sponsor registered apprentices face severe compliance hurdles if ratio rules do not provide structured transition pathways.

### 2.2 Statutory Precedent: Title 29 CFR § 29.5(b)(7)
Federal registered apprenticeship regulations govern supervisory headcount standards:
> *"A numeric ratio of apprentices to journeyworkers consistent with proper supervision, training, safety, and continuity of employment, and applicable provisions in collective bargaining agreements, except where such ratios are successfully challenged by input from other affected parties."* - 29 CFR § 29.5(b)(7)

In established Department of Labor standards (such as those maintained by the IBEW/NECA Electrical Training Alliance and the United Association of Plumbers and Pipefitters), ratios are strictly maintained, but state councils and local JATCs retain formal administrative mechanisms to grant temporary variances when regional labor shortages prevent workforce training.

### 2.3 Direct vs. General Supervision Precedent
Skilled crafts and regulated technical professions distinguish supervision requirements based on verified apprentice competencies:
* **Direct Supervision (Immediate Proximity / Line-of-Sight):** Applied during foundational training phases where the apprentice cannot execute tasks safely without immediate, continuous oversight.
* **General Supervision (Direction & Verification):** Applied during advanced phases where the apprentice has demonstrated core competencies. The supervisor establishes assignments, remains actively reachable, reviews completed work, and conducts periodic spot inspections, but is not required to observe every keystroke or command invocation.

---

## 3. Proposed Architectural & Regulatory Mechanisms

```
+─────────────────────────────────────────────────────────────────────────────+
|               TRANSITIONAL RATIO & SUPERVISION TAXONOMY                     |
+─────────────────────────────────────────────────────────────────────────────+
                                       │
        ┌──────────────────────────────┴──────────────────────────────┐
        ▼                                                             ▼
┌──────────────────────────────┐              ┌──────────────────────────────┐
│  Tier 1 & Tier 2 Apprentices │              │  Tier 3 & Tier 4 Apprentices │
│   (0 - 4,000 Hours OJT)      │              │  (4,001 - 8,000 Hours OJT)   │
├──────────────────────────────┤              ├──────────────────────────────┤
│ • Mandatory Direct           │              │ • General Supervision        │
│   Supervision (2:1 Ratio)    │              │   Standard Authorized        │
│ • Real-time line-of-sight    │              │ • Asynchronous queue review  │
│ • Zero solo shifts           │              │ • Peer coaching allowance    │
│ • No unattended production   │              │ • Active reachability SLA    │
└──────────────────────────────┘              └──────────────────────────────┘
```

### 3.1 Mechanism 1: The 36-Month Transitional Ramp-Up Schedule
To enable employer onboarding during Phase 1 (Years 0 to 3) while grandfathering applications are audited by the National Board:

1. **Phase 1 (Months 1 to 18): Market Seeding:**
   - Sponsoring employers registered with the JATC may operate with a provisional ratio of **3:1** for mixed cohorts containing at least one Tier 2 or higher apprentice in non-critical commercial environments.
   - Requires appointment of an active Master of Record (MoR) or qualified fractional Master of Record (vMoR).
2. **Phase 2 (Months 19 to 36): Consolidation:**
   - Provisional ratio steps down to standard **2:1** across all standard production shifts.
   - Employers who fail to sponsor completing apprentices to Journeyman standing cannot maintain cohort expansions.
3. **Phase 3 (Month 37 Onward: Full Enforcement):**
   - The transitional schedule sunsets permanently.
   - All participating employers must maintain baseline statutory ratios unless operating under an individual JATC variance.



### 3.2 Mechanism 2: Progressive Supervision Standards (Direct vs. General)
To relieve supervisory strain without lowering quality standards, the framework distinguishes between foundational and advanced operational stages:

* **Direct Operational Supervision (Tiers 1 & 2: 0 to 4,000 Hours):**
  - Standard: Mandatory maximum 2 apprentices per 1 licensed Journeyman.
  - Requirement: Real-time virtual line-of-sight (shared ticketing queue, live communication channels, dual-control production changes).
  - Scope: Routine incident triage, perimeter log analysis, vulnerability scanning, and manual IAM onboarding.
* **General Operational Supervision (Tiers 3 & 4: 4,001 to 8,000 Hours):**
  - Standard: A licensed Journeyman may oversee up to 4 advanced apprentices during routine operations, provided no Tier 1 novices are included in the shift pod.
  - Requirement: Supervising Journeyman must review all ticket closures, audit configuration logs within 4 hours, and maintain the 15-minute Active Reachability SLA.
  - Peer Mentorship Allowance: Advanced Tier 4 apprentices may assist in peer code review, documentation coaching, and lab guidance for Tier 1 trainees. Peer assistance **does not** count toward official supervisory ratios and carries zero logbook sign-off authority.

### 3.3 Mechanism 3: JATC Ratio Variance Petition Protocol (Employer Waivers)
When an employer cannot locate qualified journeyworkers to support apprentice hiring, the employer may submit a formal petition to the regional JATC:

```
+───────────────────+     Exhaustion Proof      +───────────────────+
| Employer Petition | ────────────────────────> |  JATC Evaluation  |
| (Form FORM-003)   |                           |  (Trust Registry) |
+───────────────────+                           +───────────────────+
                                                          │
                                ┌─────────────────────────┴─────────────────────────┐
                                ▼                                                   ▼
                     [ Approved: Max 12 Mo ]                             [ Denied: Unmet Need ]
                     • Ratio relief up to 3:1                            • Dispatched from Book 2
                     • Mandatory range offsets                           • Employer retains 2:1
                     • Underwriter disclosure
```

1. **Evidentiary Threshold:**
   - The employer must submit verified telemetry proving that a labor requisition was filed on the Guild Hiring Hall (Out-of-Work Register Book 1 and Book 2) for at least **30 calendar days** without fulfillment.
   - The employer must demonstrate an active JATC training trust contribution record in good standing.
2. **Variance Terms & Conditions:**
   - **Maximum Duration:** Variances are granted for a maximum term of **twelve (12) months** and are non-renewable without submitting new hiring hall telemetry.
   - **Maximum Capacity:** Variances cannot exceed a **3:1 ratio** for human-in-the-loop operational shifts.
   - **Simulation Compensation Offset:** The sponsoring employer must provide an additional **250 hours of accredited Cyber Range simulation** per apprentice covered under the variance to compensate for reduced individual journeyworker contact hours.
3. **Actuarial Transparency & Underwriter Reporting:**
   - Approved ratio variances are registered in the Clearinghouse Attestation Registry (`ratio_variance_active: true`).
   - Cyber liability carriers receive cryptographic notice via the Actuarial Telemetry Gateway, ensuring coverage pricing reflects approved workforce training structures rather than unverified ratio defaults.

### 3.4 Mechanism 4: Empirical Standards Amendment Criteria (Permanent Adjustments)
Individual employers or commercial trade associations cannot unilaterally rewrite baseline statutory ratios. A permanent revision of the standard 2:1 ratio requires a formal **Standards Amendment** evaluated under the following empirical benchmarks:

1. **Actuarial Loss-Ratio Parity:** Sponsoring carriers must demonstrate through five (5) consecutive years of aggregated claim data that organizations operating with advanced supervisory tooling or automated telemetry achieve incident frequencies equal to or lower than organizations operating under baseline 2:1 human ratios.
2. **Apprentice Completion & Licensing Rates:** The JATC must verify that apprentice cohorts trained under the proposed ratio standard achieve a minimum 80% first-time pass rate on the Board Practical Challenge Examination.
3. **Tripartite Board Ratification:** Under Article IV of the National Cybersecurity Trade Board Bylaws, any permanent modification to supervisory headcount ratios requires a supermajority vote (8 of 11 voting trustees), including unanimous approval from Constituency 1 (Workforce Trustees).



---

## 4. Invariants, Boundary Exclusions & Malpractice Protections

To prevent erosion of frontline safety and avoid worker exploitation:

1. **Absolute Critical Infrastructure & Safety-Critical Ban:**
   - Ratio relief, transitional expansions, and JATC variances are strictly prohibited in **Safety-Critical / IoMT / Medical Systems** and **Industrial Control / OT / SCADA networks**.
   - Mandatory **1:1 line-of-sight oversight** remains permanent and immutable for all live operational technology and clinical medical environments.
2. **Absolute Prohibition of Solo Apprentice Shifts:**
   - Under no circumstances may an apprentice be scheduled as the sole defensive operator on graveyard, weekend, or on-call emergency rotations.
   - Every active shift requires at least one designated on-duty licensed Journeyman or Master Practitioner.
3. **Right of Technical Refusal Preservation (Pillar V):**
   - If an employer compels an apprentice or Journeyman to work outside approved ratios or without an active JATC variance, the practitioner retains statutory protection to file a formal Notice of Safety Non-Concurrence (`FORM-001`).
   - Filing transfers all regulatory and operational liability exclusively to overriding executive officers and grants the practitioner unconditional safe harbor against disciplinary retaliation.

---

## 5. Comparative Trade Precedents Crosswalk

| Trade / Profession | Governing Standard | Baseline Ratio | Variance Mechanism | Advanced Autonomy Standard |
| :--- | :--- | :--- | :--- | :--- |
| **Electrical (IBEW/NECA)** | 29 CFR § 29.5(b)(7) | 1:1 to 2:1 depending on job classification | Local JATC / State Apprenticeship Council emergency variance upon certified out-of-work list exhaustion | 4th and 5th-year apprentices permitted general task execution under job foreman oversight |
| **Plumbing & Pipefitting (UA)** | 29 CFR § 29.5(b)(7) | 1:1 first apprentice, 1:2 or 1:3 for shop aggregate | Local Joint Apprenticeship Committee written variance for large industrial project agreements | Senior apprentices perform independent fitting and layout work; inspection required prior to line pressurization |
| **Medical Residency (ACGME)** | ACGME Common Program Requirements Section VI | 1:1 to 1:4 attending-to-resident ratio | Institutional Graduate Medical Education Committee (GMEC) program adjustments | PGY-2 and PGY-3 residents exercise progressive authority with attending physician available via telecommunication |
| **Aviation Maintenance (FAA)** | 14 CFR Part 65 Subpart D | Direct physical supervision for uncertificated mechanics | No ratio variances; strict logbook sign-off accountability | Practical experience verification required before Airframe & Powerplant (A&P) practical exam eligibility |
| **Cybersecurity Trade (Proposed RFC)** | 29 CFR § 29.5(b)(7) & NCTB Standards | **2:1** standard operational shift ratio | 12-month JATC Variance Petition (`FORM-003`) backed by hiring hall telemetry and simulation offset | Direct supervision (Tiers 1-2); General supervision and peer coaching allowance (Tiers 3-4) |

---

## 6. Implementation Plan & Affected Specifications

Upon community review and NCTB acceptance of RFC 0004:

1. **`framework/supervisory-ratios.md`:**
   - Incorporate progressive supervision definitions (Direct vs. General).
   - Add formalization of the 12-Month JATC Ratio Variance Petition Protocol.
2. **`framework/apprenticeship-standards.md`:**
   - Update on-shift tracking metrics to support general supervision logging for Tier 3 and Tier 4 operational hours.
3. **`governance/transition-plan.md`:**
   - Codify the 36-Month Transitional Ramp-Up Schedule into Phase 1 of the national transition roadmap.
4. **`templates/`:**
   - Author `FORM-003-ratio-variance-petition.md` for employer submissions to regional JATC training committees.
5. **Tooling Synchronization:**
   - Update `telemetry` scoring engines and `clearinghouse` registries to ingest and validate `ratio_variance_active` flags.

