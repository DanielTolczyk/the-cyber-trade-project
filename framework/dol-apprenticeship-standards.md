# National Guidelines for Apprenticeship Standards (29 CFR Part 29 & Part 30)

**Program Title:** National Cybersecurity Apprenticeship Program  
**Sponsor:** National Cybersecurity Trade Board (NCTB) & Joint Apprenticeship and Training Committees (JATCs)  
**DOL Occupational Title:** Cybersecurity Trade Practitioner / Journeyman Defender  
**O*NET-SOC Code:** 15-1212.00 (Information Security Analysts) / NIST NICE SP 800-181  
**Program Term:** 8,000 Operational Runtime Hours (Competency & Time-Based Hybrid)  
**Related Technical Instruction (RTI):** 576 Hours (144 Hours per Year Minimum)  

---

## 1. Statutory Registration & Program Standards

These National Guidelines for Apprenticeship Standards (NGAS) are established pursuant to the National Apprenticeship Act of 1937 (29 U.S.C. 50) and Title 29, Code of Federal Regulations, Part 29 (Labor Standards for the Registration of Apprenticeship Programs) and Part 30 (Equal Employment Opportunity in Apprenticeship).

1. **Qualifications for Apprenticeship:**
   * Minimum age of 18 years.
   * High school diploma, GED equivalency, or recognized vocational pre-apprenticeship completion.
   * Successful completion of the [Pillar I Pre-Apprenticeship Benchmark Screening](../pillars/01_pre-apprenticeship.md) (Networking, POSIX/Linux, Scripting, Security Fundamentals) or accredited community college prerequisite.
   * Physical and remote cognitive capability to perform SOC, engineering, and incident response duties.
2. **Probationary Period:** The first 1,000 operational hours (or 6 months) shall be the probationary period. During this period, either the apprentice or the JATC may terminate the apprenticeship agreement without prejudice.
3. **Supervisory Ratio Standard (2:1):** Sponsoring employers shall maintain an on-shift operational supervision ratio of no more than two (2) registered apprentices per one (1) licensed Journeyman or Master Practitioner.

---

## 2. Progressive Wage Step Schedule

Apprentices shall be paid a progressively increasing schedule of wages based on verified operational hours accumulated across the five core domains:

| Apprenticeship Stage | Accumulated Runtime Hours | Related Instruction Completed | Minimum Wage Floor |
| :--- | :--- | :--- | :--- |
| **Tier 1 Apprentice** | **0 - 2,000 Hours** | **Year 1 RTI (144 hrs)** | **50% of Regional Journeyman Prevailing Base (RJPB)** |
| **Tier 2 Apprentice** | **2,001 - 4,000 Hours** | **Year 2 RTI (288 hrs cumulative)** | **60% of Regional Journeyman Prevailing Base (RJPB)** |
| **Tier 3 Apprentice** | **4,001 - 6,000 Hours** | **Year 3 RTI (432 hrs cumulative)** | **70% of Regional Journeyman Prevailing Base (RJPB)** |
| **Tier 4 Apprentice** | **6,001 - 8,000 Hours** | **Year 4 RTI (576 hrs cumulative)** | **80% of Regional Journeyman Prevailing Base (RJPB)** |
| **Licensed Journeyman** | **8,001+ Hours & Exam Pass** | **Full RTI & Board Challenge** | **100% of Regional Journeyman Prevailing Base (RJPB)** |

---

## Appendix A: 8,000-Hour Work Process Schedule

The 8,000 operational hours are distributed across the five mandatory core domains with continuous supervisory attestation recorded via the Universal Digital Logbook:

### Domain 1: Perimeter, Cloud & Network Defense (1,500 Hours)
* Task 1.1: Next-Generation Firewall (NGFW) rule staging, egress filtering, and micro-segmentation. (400 hrs)
* Task 1.2: Cloud Security Posture Management (CSPM), VPC peering, and secure transit gateways. (400 hrs)
* Task 1.3: Software-Defined Perimeter (SDP), Zero Trust Network Access (ZTNA), and VPN gateway maintenance. (350 hrs)
* Task 1.4: Network protocol telemetry inspection, Wireshark packet analysis, and TLS inspection. (350 hrs)

### Domain 2: Detection Engineering, SOC Operations & Incident Triage (2,000 Hours)
* Task 2.1: Tier 1/2 SIEM alert triage, log correlation, and false-positive suppression in 24/7 SOC. (600 hrs)
* Task 2.2: Detection-as-code rule development (Sigma, YARA, Splunk SPL, KQL) mapped to MITRE ATT&CK. (500 hrs)
* Task 2.3: Host artifact forensics, memory capture, EDR triage, and containment isolation. (500 hrs)
* Task 2.4: Phishing email header analysis, sandbox execution, and malware signature staging. (400 hrs)

### Domain 3: Identity, Credential & Access Management / IAM (1,500 Hours)
* Task 3.1: FIDO2 / WebAuthn passwordless deployment, MFA enforcement, and conditional access policies. (400 hrs)
* Task 3.2: Role-Based & Attribute-Based Access Control (RBAC/ABAC) directory audits and least privilege. (400 hrs)
* Task 3.3: Privileged Access Management (PAM) vault management, session recording, and root rotation. (350 hrs)
* Task 3.4: Federation protocol configuration (SAML 2.0, OIDC, OAuth 2.0) and SCIM provisioning. (350 hrs)

### Domain 4: Vulnerability Assessment & Attack Surface Management (1,500 Hours)
* Task 4.1: Automated vulnerability scanning, credentialed infrastructure auditing, and scan tuning. (400 hrs)
* Task 4.2: CVSS v3.1 / v4.0 scoring, EPSS exploit prediction, and patch priority scheduling. (400 hrs)
* Task 4.3: Software Bill of Materials (SBOM) generation (CycloneDX/SPDX) and dependency supply chain audits. (350 hrs)
* Task 4.4: Defensive validation testing, breach and attack simulation (BAS), and configuration verification. (350 hrs)

### Domain 5: Defensive Governance, Risk, Compliance & Audit / GRC (1,500 Hours)
* Task 5.1: Control framework auditing (NIST SP 800-53, ISO/IEC 27001, CIS Critical Security Controls). (400 hrs)
* Task 5.2: Third-party vendor risk assessment, SOC 2 Type II report evaluation, and contract review. (400 hrs)
* Task 5.3: Incident response tabletop exercise facilitation, business continuity, and disaster recovery testing. (350 hrs)
* Task 5.4: Evidentiary documentation, audit log preservation, and Form FORM-001/002 filing management. (350 hrs)

---

## Appendix B: Related Technical Instruction (RTI) Curriculum (576 Hours)

Instruction is delivered across four annual 144-hour modules by public community colleges and accredited [Certified Trade Instructors (CTI)](licensure-and-progression.md#5-certified-trade-instructor-cti-endorsement):

* **Year 1 (Module RTI-101 - 144 hrs):** Advanced TCP/IP, Linux Kernel Internals, Scripting for Security Engineers (Python & Bash), and Cryptographic Fundamentals.
* **Year 2 (Module RTI-201 - 144 hrs):** Defensive Architecture, SIEM/SOAR Engineering, Threat Hunting, and Memory Forensics.
* **Year 3 (Module RTI-301 - 144 hrs):** Enterprise Identity Infrastructure, Cloud Security Architecture (AWS/Azure/GCP), and Application Threat Modeling.
* **Year 4 (Module RTI-401 - 144 hrs):** Critical Infrastructure Defense, Forensic Readiness, Legal & Regulatory Compliance, and Practical Board Challenge Exam Preparation.

---

## Appendix C: Equal Employment Opportunity & Affirmative Action (29 CFR Part 30)

1. **Universal Nondiscrimination:** The recruitment, selection, employment, and training of apprentices shall be conducted without discrimination based on race, color, religion, national origin, sex (including pregnancy and gender identity), sexual orientation, genetic information, disability, or age.
2. **Objective Selection Procedures:** Apprentices are selected exclusively through transparent, rubric-based pre-apprenticeship benchmark testing and structured oral interviews proctored by the regional JATC.
3. **Anti-Harassment & Civil Rights Enforcement:** Sponsoring employers must certify zero tolerance for hostile work environments and provide confidential reporting channels through the JATC Shop Steward under Form FORM-004.

