# Apprenticeship Standards & Operational On-Ramps

To maintain high technical standards, protect apprentices from unpaid exploitation, and honor practical, non-traditional talent, this standard defines the rules governing on-the-job training (OJT), Related Technical Instruction (RTI), and Prior Learning Assessment (PLA) challenge pathways.

---

## 1. Core 8,000-Hour Rotational Distribution

To graduate as a Licensed Journeyman, an apprentice must log a minimum of **8,000 verified operational runtime hours** under the direct line-of-sight supervision of a Licensed Journeyman or a certified Master Practitioner acting as the Master of Record (MoR).

Hours must be balanced across core operational disciplines:

| Core Rotational Domain | Minimum Required Runtime | Core Focus & Operational Activities |
| :--- | :--- | :--- |
| **Domain 1: Perimeter, Cloud & Network Defense** | 1,500 hrs | Firewall/WAF lifecycle, microsegmentation, control-plane hardening, zero-trust traffic analysis. |
| **Domain 2: Detection Engineering & Incident Triage (SOC)** | 2,000 hrs | 24/7 alert validation, SIEM/EDR rule authoring, containment workflows, log pipeline telemetry. |
| **Domain 3: Identity, Credential & Access Management (IAM)** | 1,500 hrs | PAM governance, directory services, cryptographic key lifecycle, role-based access review. |
| **Domain 4: Vulnerability & Attack Surface Management** | 1,500 hrs | Patch verification, asset discovery, configuration auditing, attack-surface minimization. |
| **Domain 5: Defensive Governance, Risk & Audit (GRC)** | 1,500 hrs | Control implementation testing, audit log verification, policy compliance, vendor risk reviews. |

> **Rotational Flexibility & Specialty Tracks:** Up to 1,000 hours may be allocated as elective focus hours in an approved Specialty Track (such as Industrial Control Systems [ICS/SCADA], Medical Technology [MedTech], Digital Forensics [DFIR], Offensive Security, or AI/ML Assurance) during Apprentice Tier 4. These specialty tracks inherit the environment-specific staffing density rules defined in the trade headcount standards.

---

## 2. Related Technical Instruction (RTI) Requirements

Apprentices must complete a minimum of **144 classroom/lab hours per year** (576 total RTI hours over a standard 4-year term).

* **Zero-Cost Mandate:** All RTI coursework, lab platforms, and testing materials must be provided at zero cost to the apprentice by the sponsoring employer or regional JATC trust.
* **Curriculum Focus:** Instruction must prioritize live-environment labs, packet analysis, script automation, and defensive architecture over rote memorization of multiple-choice banks.
* **Wage Status:** Mandatory RTI conducted outside standard working shifts must be compensated at the apprentice's current hourly base rate.
* **PLA Pro-Rating:** Apprentices entering with advanced standing via Prior Learning Assessment (PLA) will have their total required RTI hours pro-rated relative to their remaining time in the program (e.g., a Tier 3 entry requires a minimum of 288 remaining RTI hours).

---

## 3. Merit-Based Practical Challenge Pathways (Credit-by-Examination)

To prevent artificial gatekeeping, lower barriers for career transitioners, and honor self-taught practitioners, CTF competitors, independent security researchers, and military veterans:

### A. Direct Practical Examination
* Practitioners may test out of prerequisite classroom instruction and lower-tier apprentice hours by passing proctored, hands-on **Practical Challenge Exams**.
* Challenge evaluations consist of live-fire scenario labs (defensive hardening, threat containment, and triage under pressure) evaluated by a panel of Licensed Masters.

### B. Prior Learning Assessment (PLA) Framework
Documented operational experience, open-source security tool development, and verifiable industry benchmarks translate to OJT hour credits according to standardized conversion caps:

| Prior Experience / Benchmark | Eligible Credit Type | Maximum Allowable Bypass |
| :--- | :--- | :--- |
| **Verified Bug Bounty / CVE Disclosures** | Direct OJT Credit (Domain 4) | Up to 1,500 hrs |
| **Accredited Military Cyber MOS / AFSC** | Direct OJT Credit (Domains 1-4) | Up to 4,000 hrs (Tier 3 Entry) |
| **Practical Hands-on Certifications (Lab-Based)** | RTI & OJT Credit (Domains 1-3) | Up to 2,000 hrs (Tier 2 Entry) |
| **Documented Production SysAdmin / NetEng Experience** | Direct OJT Credit (Domains 1 & 3) | Up to 2,000 hrs (Tier 2 Entry) |

> **Mandatory Cap & Residency Rule:** Regardless of prior credentials or exam scores, credit-by-examination and PLA cannot bypass more than **4,000 hours (50%)** of the 8,000-hour core baseline. Every candidate must complete at least 4,000 hours of live, supervised production work to be eligible for the Journeyman Licensure Exam.

---

## 4. Supervisory Ratio Alignment

All operational OJT hours logged under this standard must be conducted in strict compliance with the trade's established mentorship and safety density limits.

For exact 1:1 and 2:1 environment thresholds, solo-shift prohibitions, and Master of Record (MoR) capacity caps, refer directly to the [Supervisory Ratios & Operational Headcount Standards](supervisory-ratios.md).

---

## 5. Standardized Logbook & Portfolio Verification

Apprentices must maintain an immutable, cryptographic or signed physical **Operational Logbook** mapped directly to the technical criteria defined in the [Universal Logbook Standards & Competency Ledger](logbook-standards.md). Logs must strictly record:

1. Hourly distribution across the 5 core rotational domains mapped to standardized **NIST NICE Framework Work Roles**.
2. Verified incidents triaged, systems hardened, and changes audited using anonymized internal artifact references or change request hashes to protect corporate data privacy.
3. Simulation allowances up to **1,000 hours (12.5%)** total, achieved through Board-accredited high-fidelity cyber range exercises and structured adversary simulation labs.
4. Bi-weekly review signatures or periodic batch sign-offs from the supervising Journeyman or Master of Record.
5. Quarterly evaluations submitted to the regional Joint Apprenticeship and Training Committee (JATC) for wage tier advancement.


---

## 6. Apprentice Grievance, Wage Protection & Logbook Dispute Protocol

To ensure trainees are protected from predatory employer practices, wage theft, or supervisory withholding of logbook hours, all participating employers and apprentices are bound by the **Three-Step JATC Dispute Protocol**:

```
+─────────────────────────────────────────────────────────────────────────────+
| THREE-STEP JATC APPRENTICE GRIEVANCE & DISPUTE WORKFLOW                    |
+─────────────────────────────────────────────────────────────────────────────+
  │
  ├─► STEP 1: LOCAL TRAINING DIRECTOR REVIEW (5 Business Days)
  │   • Apprentice files a dispute regarding uncredited hours or withheld wage steps.
  │   • Local JATC Director audits sanitized ticket logs, commits, and timesheets.
  │
  ├─► STEP 2: BIPARTISAN JATC GRIEVANCE HEARING (14 Calendar Days)
  │   • Bipartisan panel (2 employer trustees + 2 Journeyman trustees).
  │   • Apprentice is represented by the elected Apprentice Advocate Delegate.
  │   • Panel reviews operational evidence and issues a binding resolution.
  │
  └─► STEP 3: STATUTORY BOARD DECREE & EMERGENCY REALLOCATION
      • If employer is found non-compliant: hours are credited by Board decree,
        back-wages are recovered via the employer's Trade Surety Bond.
      • The apprentice is immediately re-dispatched to a compliant employer sponsor
        with zero loss of standing or wage step progress.
```



---

## 7. Federal Statutory Compliance Alignment (DOL 29 CFR Part 29 & Part 30)

To guarantee that participating employers, community colleges, and apprentices unlock federal and state registered apprenticeship benefits on Day 1, this standard satisfies all statutory criteria:

| Federal Statutory Requirement (29 CFR Part 29 / 30) | Cybersecurity Trade Project Standard | Statutory Compliance Status |
| :--- | :--- | :--- |
| **Minimum 2,000 OJT Hours / Year (§ 29.5(b)(2))** | 8,000 hours over 4 years across 5 standardized rotational domains. | **100% Compliant** |
| **Minimum 144 Classroom RTI Hours / Year (§ 29.5(b)(4))** | 576 hours total (144 hrs/year) funded zero-cost by JATC training trusts. | **100% Compliant** |
| **Progressive Wage Step Schedule (§ 29.5(b)(5))** | Graduated scale: Tier 1 (50%), Tier 2 (60%), Tier 3 (70%), Tier 4 (80%), Journeyman (100%). | **100% Compliant** |
| **Supervisory Ratios & Worker Safety (§ 29.5(b)(7))** | Enforced 2:1 on-shift operational ratio; solo-shift bans on graveyard/on-call. | **100% Compliant** |
| **Equal Opportunity & Affirmative Action (Part 30)** | Public vocational community college screening and veterans' recruitment partnerships. | **100% Compliant** |
| **Credential Portability & Completion (§ 29.5(b)(15))** | Universal Logbook and issuance of DOL Certificate of Completion of Apprenticeship. | **100% Compliant** |

---

## 8. Exam Failure Remediation & Supervisor Departure Protections

### A. Practical Examination Remediation Protocol
* **Wage Stability:** An apprentice who completes 8,000 operational runtime hours but does not pass the Journeyman Practical Challenge Exam remains at **Tier 4 Apprentice Wages (80% RJPB)** for a structured **6-month remediation period**.
* **Zero-Cost Lab Tutoring:** The regional JATC provides dedicated lab tutoring focusing on the specific domain competencies where the candidate experienced scoring deficiencies.
* **Retake Policy:** Apprentices may attempt the practical examination up to **three (3) times within an 18-month window** before a joint JATC review panel convenes to evaluate career pathway placement.

### B. Supervisor Departure & 14-Day Reassignment Safe Harbor
* **Cryptographic Hour Preservation:** If a supervising Journeyman or Master leaves an enterprise, gets reassigned, or faces license suspension, all previously logged and ticket-hashed hours remain permanently valid and accredited.
* **14-Day Employer Reassignment Window:** The employer has 14 calendar days to assign another active Licensed Journeyman or Master on staff to resume line-of-sight supervision. If no licensed staff is available, the JATC immediately executes emergency reassignment to another participating sponsor with zero loss of training progress.

---

## 9. Pre-Apprentice Candidate Integrity & Intake Debarment

To ensure individuals granted privileged operational access uphold foundational trade ethics from Day 1, pre-apprenticeship participants and practical challenge candidates are bound by the **Candidate Trade Integrity Agreement**:

### A. Candidate Violation Categories & Intake Sanctions
1. **Academic & Lab Dishonesty (Category 1):** Using unauthorized braindumps, sharing live challenge flags, copying code submissions, or bypassing proctor controls results in immediate dismissal from the pre-apprenticeship program, cancellation of exam scores, and a **12-to-24 month suspension** from the National Candidate Clearinghouse.
2. **Discriminatory Harassment & Hate Speech (Category 2):** Engaging in harassment, sexual harassment, deadnaming, or slurs against fellow students, instructors, or lab staff results in immediate dismissal and **permanent debarment** from all JATC apprenticeship indentures.
3. **Range Sabotage & Unauthorized Access (Category 3):** Attacking shared training range infrastructure, tampering with scoring daemons, or credential theft triggers **lifetime trade debarment** and formal referral to civil/criminal legal authorities.

### B. Due Process for Candidates
* Infractions are documented via an [Ethics & Conduct Incident Report (Form FORM-004)](../templates/FORM-004_ethics-and-conduct-incident-report.md) with technical evidence hashes.
* Candidates receive written notice within 5 business days and the right to an evidentiary hearing before a 3-member JATC Candidate Review Panel (1 Vocational Educator, 1 Journeyman Proctor, 1 Apprentice Advocate).

---

## 10. Equal Opportunity & Emergency Harassment Transfers (29 CFR Part 30)

In strict compliance with 29 CFR Part 30 and Title VII:
* **Equal Opportunity Guarantee:** All recruitment, intake screening, classroom RTI, on-the-job rotational assignments, and wage elevations operate strictly without discrimination based on race, color, religion, national origin, sex, sexual orientation, gender identity, disability, age (40+), veteran status, genetic information, pregnancy, or cultural expression.
* **Emergency Apprentice Transfer Protocol:** If an apprentice experiences discrimination, harassment, retaliation, or supervisory abuse at a participating employer, the JATC executes an immediate emergency transfer of the apprentice's indenture to a new compliant sponsor within 14 calendar days, with 100% preservation of accumulated hours, wage tiers, and health hour-bank reserves.

---

## 11. Prohibition of TRAPs, Liquidated Damages & Non-Competes

To prevent the financial indenturing and debt-bondage of early-career practitioners:

### A. Strict Prohibition of Training Repayment Agreement Provisions (TRAPs)
* **Zero Worker Training Debt:** Under JATC multi-employer trust rules, all Related Technical Instruction (RTI), cyber range access, lab licenses, and exam vouchers are funded centrally by participating employer hourly contributions ($1.50/hr).
* **Ban on Exit Debts & Reimbursement Penalties:** Sponsoring employers are legally prohibited from requiring apprentices to execute Training Repayment Agreements (TRAPs), liquidated damages clauses, tuition reimbursement clawbacks, or exit penalties if the apprentice departs during or after the training program.
* **Statutory Nullity:** Any TRAP, promissory note, or repayment contract executed against an apprentice is legally null, void, and unenforceable under trade bylaws, and constitutes an actionable Class D unfair labor practice.

### B. Universal Prohibition of Non-Compete Agreements
* **Labor Mobility Guarantee:** Trade credentials and Journeyman licenses are open-market assets. Sponsoring employers cannot restrict where an apprentice or graduate Journeyman works following graduation.
* **Void Covenants:** Post-employment non-compete agreements, customer solicitation covenants, and geographic practice restrictions applied to registered apprentices or graduating Journeymen are strictly prohibited across all participating employer agreements.

---

## 12. Forensic Trauma, Graphic Material Exposure & Rotational Respite

Defensive cyber operations and digital forensics occasionally expose analysts to high-trauma material during lawful investigations (e.g., child sexual abuse material [CSAM] evidence handling, violent extremism triage, or severe cyber-extortion).

To protect practitioner mental health and eliminate career penalties for occupational trauma exposure:

### A. Rotational Respite for High-Trauma Forensic Investigations
* **Stigma-Free Temporary Reassignment:** Any practitioner or apprentice assigned to forensic investigations involving CSAM evidence, graphic violence, or acute crisis triage holds the unconditional right to request temporary rotational relief away from traumatic materials.
* **Zero Retaliation & Wage Protection:** Exercising a trauma respite request cannot be used as grounds for negative performance reviews, delayed wage-step elevation, or tier demotion. The apprentice is temporarily rotated into non-traumatic domains (e.g., Perimeter Hardening, Identity Governance, Vulnerability Scanning, or Defensive GRC) with 100% preservation of accumulated hours and base pay.

### B. Dedicated Psychological Support Infrastructure
* **Confidential Support Access:** The multi-employer Taft-Hartley Health Trust funds specialized, confidential psychological counseling tailored specifically to forensic digital trauma and high-stress incident containment.
* **Secondary Review Protections:** In CSAM investigations, direct media inspection must be minimized through automated cryptographic hashing (e.g., PhotoDNA matching) and strict operational exposure limits (maximum 2 hours of continuous review).



