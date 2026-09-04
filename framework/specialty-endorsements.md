# Specialty Endorsements & Domain Architecture

Cybersecurity is not a monolith. Following the completion of foundational generalist rotations (Years 1-2), practitioners pursue specific technical endorsements that validate deep architectural, operational, and regulatory expertise.

> **Note on Credentials:** Any commercial certifications mentioned under domain tracks are **strictly non-binding illustrative examples** of current industry alignments. The National Cybersecurity Trade Board holds sole statutory authority to evaluate, validate, or design objective, vendor-neutral challenge exams for each endorsement.

---

## 1. The Three-Layer Specialty Architecture

To prevent arbitrary curriculum design and ensure every trade endorsement remains vendor-neutral, federally accredited, and mathematically verifiable, all specialty tracks are structured in a standardized **Three-Layer Hierarchy**:

```
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 1: NIST NICE WORKFORCE TAXONOMY (Workforce Foundation)                |
| Canonical mapping to national NIST SP 800-181 Work Role IDs and standardized|
| Knowledge, Skills, and Tasks (KSTs). Ensures federal workforce recognition. |
+─────────────────────────────────────────────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 2: SECTOR-SPECIFIC CONSENSUS STANDARDS (Technical Baselines)          |
| Authoritative technical frameworks governing the domain:                    |
| • Medical Devices: FDA Section 524B, AAMI TIR57, ANSI/AAMI/ISO 14971        |
| • Product Security: NIST IR 8259, ETSI EN 303 645, EU Cyber Resilience Act  |
| • Industrial Controls: ISA/IEC 62443, NERC CIP, IEC 61511 (SIS)             |
| • Cloud Architecture: CSA CCM v4, CIS Cloud Benchmarks, NIST SP 800-145     |
+─────────────────────────────────────────────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 3: TRADE OPERATIONAL LEDGER & AUTHORITY (Operational Standards)       |
| • 2,000-Hour Post-Licensure Runtime Distribution                            |
| • Line-of-Sight Supervisory Ratios & Headcount Caps                         |
| • Statutory Sign-Off Authority & Regulatory Refusal Standing                |
| • Milestone Wage Percentage Adders (+10% to +25% above RJPB)                |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 2. Endorsement Classification: Discipline Tracking vs. Statutory Adders

To maintain economic equilibrium and provide the Craft Guild Clearinghouse with precise labor telemetry, specialty endorsements are categorized into two operational tiers:

* **Discipline Endorsements (Standard Journeyman Scope - 100% RJPB Base):** Define a practitioner's primary technical specialization (e.g., Application/Product Security, Cloud Infrastructure, Identity). These codes enable the Guild Clearinghouse to track labor supply and demand, match requisitions without recruiter friction, and throttle training pipelines to prevent workforce surpluses or shortages.
* **Statutory & Life-Safety Endorsements (Mandatory Wage Adders: +10% to +25%):** Applied to disciplines involving life-safety critical infrastructure, direct patient safety risks, statutory federal design stamping (FDA 524B / NERC-CIP), or high-liability legal chains of custody.

---

## 3. Master Specialty Endorsements Ledger

| Specialty Discipline | Trade Code | Primary NIST NICE Work Roles | Tier & Wage Classification | Detailed Standard |
| :--- | :--- | :--- | :--- | :--- |
| **Medical Device & Clinical Technology** | `SE-MED` | `SP-DEV-001`, `SP-SRP-001`, `OV-MGT-001` | **Statutory Life-Safety (+20% to +25%)** | [Specification](specialty-tracks/medical-devices.md) |
| **Industrial Control Systems (ICS/SCADA)** | `SE-ICS` | `SP-ARC-002`, `SP-SRP-001`, `OM-NET-001` | **Statutory Life-Safety (+20% to +25%)** | [Specification](specialty-tracks/industrial-control-systems.md) |
| **Digital Forensics & Incident Response** | `SE-DFIR` | `IN-FOR-001`, `PR-CDA-001`, `IN-FOR-002` | **High-Liability (+15% to +20%)** | [Specification](specialty-tracks/digital-forensics-incident-response.md) |
| **Offensive Security & Red Teaming** | `SE-OFF` | `AN-EXP-001`, `SP-DEV-001` | **High-Risk Operational (+15% to +20%)** | [Specification](specialty-tracks/offensive-security.md) |
| **AI / ML Security Assurance** | `SE-AIML` | `SP-DEV-001`, `AN-TWA-001`, `SP-SRP-001` | **Emerging Technology (+15% to +20%)** | [Specification](specialty-tracks/ai-machine-learning.md) |
| **Cloud Security & Infrastructure** | `SE-CLD` | `SP-ARC-001`, `OM-NET-001`, `PR-INF-001` | **Architectural Complexity (+10% to +15%)** | [Specification](specialty-tracks/cloud-security.md) |
| **Application & Software Product Security** | `SE-APP` | `SP-DEV-001`, `SP-SRP-001`, `PR-VAM-001` | **Discipline Endorsement (Standard Base)** | [Specification](specialty-tracks/application-security.md) |
| **Identity, Credential & Access (ICAM)** | `SE-ICAM` | `SP-ARC-001`, `PR-INF-001`, `OM-NET-001` | **Discipline Endorsement (Standard Base)** | [Specification](specialty-tracks/identity-access-management.md) |
| **Cryptographic Infrastructure & PKI** | `SE-PKI` | `SP-ARC-001`, `SP-DEV-001` | **Discipline Endorsement (Standard Base)** | [Specification](specialty-tracks/cryptographic-pki.md) |

---

## 4. Core Generalist Foundation (Mandatory Prerequisite)
Before pursuing post-licensure specialty endorsements, all apprentices must complete 8,000 verified operational hours across the five mandatory core domains (Years 1-4):
1. **Domain 1: Perimeter, Cloud & Network Defense (1,500 Hours):** Packet inspection, stateful firewalling, DNS/routing security, cloud network segmentation, and traffic analysis.
2. **Domain 2: Detection Engineering & Incident Triage / SOC (2,000 Hours):** Incident classification, log correlation, alert triage, SIEM rule development, and baseline threat detection.
3. **Domain 3: Identity, Credential & Access Management / IAM (1,500 Hours):** Directory services, PAM, OAuth/SAML federation, principle of least privilege, and MFA architecture.
4. **Domain 4: Vulnerability & Attack Surface Management (1,500 Hours):** Attack surface mapping, automated vulnerability scanning, patch orchestration, and configuration auditing.
5. **Domain 5: Defensive Governance, Risk & Audit / GRC (1,500 Hours):** Security control auditing (NIST SP 800-53, ISO 27001), vendor risk evaluations, compliance testing, and log audit attestations.

---

## 5. Specialized Trade Branches (Tier 4 Elective & Post-Journeyman)

### Branch A: Digital Forensics & Incident Response (SE-DFIR)
* **Core Focus:** Live incident containment, volatile memory forensics, disk imaging, chain-of-custody evidence preservation, threat actor eradication, malware analysis, statutory breach scoping, and insurer proof-of-loss documentation.
* **Illustrative Examples / Equivalencies:** GCFA, GCFE, GNFA, GCIH (or Board Practical Challenge Exam).
* **Sign-off Authority:** Legal chain of custody digital stamping, formal breach containment attestation for cyber insurers, statutory regulatory breach notification root-cause sign-off.
* **Detailed Standard:** [Specialty Track Specification: SE-DFIR Digital Forensics & Incident Response](specialty-tracks/digital-forensics-incident-response.md).

### Branch B: Offensive Security & Adversary Emulation (SE-OFF)
* **Core Focus:** External and internal penetration testing, red teaming, exploit analysis, social engineering defense testing, and MITRE ATT&CK adversary emulation.
* **Illustrative Examples / Equivalencies:** OSCP, OSEP, GXPN, CREST (or Board Practical Challenge Exam).
* **Sign-off Authority:** Penetration test certification, external attack surface resilience sign-off, Rules of Engagement safety authorization.
* **Detailed Standard:** [Specialty Track Specification: SE-OFF Offensive Security & Adversary Emulation](specialty-tracks/offensive-security.md).

### Branch C: Cloud Security & Infrastructure Architecture (SE-CLD)
* **Core Focus:** Multi-cloud security architecture (AWS/Azure/GCP), container and Kubernetes security, Infrastructure-as-Code (IaC) policy guardrails, CIEM/CSPM, and cloud workload protection.
* **Illustrative Examples / Equivalencies:** CCSP, AWS/Azure Advanced Security Specializations.
* **Sign-off Authority:** Cloud baseline architecture certification, automated deployment policy-guardrail sign-off.
* **Detailed Standard:** [Specialty Track Specification: SE-CLD Cloud Security & Infrastructure](specialty-tracks/cloud-security.md).

### Branch D: Application & Software Product Security (SE-APP)
* **Core Focus:** Secure SDLC integration, component-level threat modeling, SAST/DAST/SCA tooling, API security, Software Bill of Materials (SBOM) lifecycle (CycloneDX/SPDX), non-product R&D tooling qualification, and PSIRT coordinated vulnerability management.
* **Illustrative Examples / Equivalencies:** CASE, CSSLP, specialized product and application security engineering credentials.
* **Sign-off Authority:** Production software and product security release clearance, SBOM compliance verification.
* **Detailed Standard:** [Specialty Track Specification: SE-APP Application & Software Product Security](specialty-tracks/application-security.md).

### Branch E: Medical Device & Clinical Technology Security (SE-MED)
* **Core Focus:** Embedded device firmware (SiMD), Software as a Medical Device (SaMD), companion mobile health apps, FDA Section 524B premarket compliance, AAMI TIR57 / ISO 14971 clinical safety risk integration, and SBOM lifecycle management.
* **Illustrative Examples / Equivalencies:** Biomedical engineering cybersecurity specializations, medical device security credentials (or Board Practical Challenge Exam).
* **Sign-off Authority:** Premarket FDA Section 524B cybersecurity readiness sign-off, clinical safety deployment clearance.
* **Detailed Standard:** [Specialty Track Specification: SE-MED Medical Device Security](specialty-tracks/medical-devices.md).

### Branch F: Industrial Control Systems (SE-ICS / SCADA / OT)
* **Core Focus:** Purdue Model network segmentation (IDMZ Level 3.5), industrial protocols (Modbus, DNP3, CIP, OPC UA, PROFINET), Safety Instrumented Systems (SIS / IEC 61511), physical process protection, ISA/IEC 62443, and NERC-CIP compliance.
* **Illustrative Examples / Equivalencies:** GICSP, GRID, GCIP.
* **Sign-off Authority:** Critical infrastructure plant cyber-safety commissioning stamp, IDMZ conduit certification, outage maintenance safe-harbor clearance.
* **Detailed Standard:** [Specialty Track Specification: SE-ICS Industrial Control Systems & OT Security](specialty-tracks/industrial-control-systems.md).

### Branch G: Identity, Credential & Access Management (SE-ICAM)
* **Core Focus:** Enterprise Zero Trust architectures, cross-domain federation (SAML/OIDC), Privileged Access Management (PAM), secrets management lifecycle, and directory consolidation.
* **Illustrative Examples / Equivalencies:** CIAM, enterprise identity engineering credentials.
* **Sign-off Authority:** Enterprise federation sign-off, emergency root credential rotation attestation.
* **Detailed Standard:** [Specialty Track Specification: SE-ICAM Identity, Credential & Access Management](specialty-tracks/identity-access-management.md).

### Branch H: Cryptographic Infrastructure & PKI (SE-PKI)
* **Core Focus:** Hardware Security Module (HSM) deployment, enterprise PKI lifecycle, root CA isolation, key management ceremonies, and Post-Quantum Cryptography (PQC) migration.
* **Illustrative Examples / Equivalencies:** Board-approved cryptography and PKI engineering credentials.
* **Sign-off Authority:** Root CA key ceremony execution and witness sign-off, enterprise cryptographic standard migration sign-off.
* **Detailed Standard:** [Specialty Track Specification: SE-PKI Cryptographic Infrastructure & PKI](specialty-tracks/cryptographic-pki.md).

### Branch I: AI & Machine Learning Security Assurance (SE-AIML)
* **Core Focus:** Adversarial machine learning threat modeling, prompt injection defense, MLOps pipeline provenance, foundation model weight signing, and NIST AI RMF governance.
* **Illustrative Examples / Equivalencies:** Board-approved AI/ML security credentials.
* **Sign-off Authority:** Enterprise AI model deployment security certification, AI Model Safety Card sign-off.
* **Detailed Standard:** [Specialty Track Specification: SE-AIML AI & Machine Learning Security Assurance](specialty-tracks/ai-machine-learning.md).

---

## 6. Tier 4 Elective Specialty Approval, Substitution & Tracking Workflow

To operationalize the 1,000-hour elective focus option during Apprentice Tier 4 (hours 6,001 to 8,000), the trade enforces a standardized approval and telemetry pipeline:

### 6.1 JATC Elective Petition & Vetting Process
1. **Apprentice Eligibility:** An apprentice in good standing who has accumulated at least 6,000 operational hours across the core domains with zero active disciplinary flags may file a **Tier 4 Specialty Elective Petition** via the Universal Logbook.
2. **MoR Facility & Mentor Attestation:** The sponsoring employer's designated Master of Record must certify that:
   * The host facility maintains active, production-grade infrastructure aligned with the requested specialty track (e.g., live PERA Level 2/3 systems for `SE-ICS`, medical device clinical pipelines for `SE-MED`, or model evaluation registries for `SE-AIML`).
   * The apprentice will be directly supervised by a licensed Journeyman holding the relevant specialty endorsement or possessing verified equivalent competence under the mandatory supervisory ratio table.
3. **JATC Training Director Concurrence:** The regional Joint Apprenticeship and Training Committee reviews the petition against the apprentice's academic progress in Related Technical Instruction (RTI). Upon JATC concurrence, the petition status updates to `APPROVED` on the Clearinghouse ledger.

### 6.2 Logbook Metadata Tagging & Cryptographic Ledger Tracking
* **Specialty Trade Tagging:** Once approved, all runtime hours logged within the specialized rotation must include the canonical `specialty_endorsement_code` (e.g., `"SE-ICS"`) within the logbook entry payload alongside the standard generalist domain code.
* **Domain Substitution Accounting:** The logbook ledger dynamically enforces substitution caps (maximum 500 hours deducted from Domain 2, maximum 250 hours deducted from Domains 1, 3, 4, or 5), ensuring the apprentice preserves the non-negotiable 1,000-hour generalist floor in every core domain.
* **Actuarial & Clearinghouse Telemetry:** The Universal Clearinghouse tallies verified specialty hours separately from generalist totals.

### 6.3 Post-Licensure Articulation & 50% Credit Acceleration
* Upon successfully passing the National Board Practical Challenge Examination, the apprentice earns full Licensed Journeyman standing.
* The 1,000 verified Tier 4 specialty hours immediately apply as an accelerated **50% advance credit** against the 2,000-hour post-licensure requirement for that specific Specialty Endorsement.
* The newly licensed Journeyman requires only 1,000 additional specialized operational hours (or passing the track-specific Board Practical Challenge Exam) to achieve full Specialty Endorsement conferral.

---

## 7. Master Cross-Crediting & Articulation Matrix

To prevent dilution of tradecraft standards, cross-crediting between specialty endorsements is strictly regulated and asymmetrical. Where overlap exists in underlying engineering foundations, the Board permits credit towards the 2,000-hour post-licensure requirement up to strict maximum caps:

| Target Endorsement Track | Eligible Source Track | Max Credit | Justification & Mandatory Remaining Runtime |
| :--- | :--- | :--- | :--- |
| **`SE-MED` (Medical Devices)** | `SE-APP` | 1,000 hrs (50%) | Shared threat modeling and SBOM lifecycle. Must complete 1,000 hrs clinical hazard & FDA 524B packaging. |
| **`SE-APP` (AppSec/Product)** | `SE-MED` | 1,000 hrs (50%) | Medical device software engineering satisfies software product security baselines. |
| **`SE-CLD` (Cloud Infrastructure)** | `SE-APP` or `SE-ICAM` | 500 hrs (25%) | IaC/CI-CD automated pipeline security or cloud identity federation overlap. |
| **`SE-OFF` (Offensive Security)** | `SE-APP` | 500 hrs (25%) | Web/API vulnerability analysis and payload testing overlap. |
| **`SE-AIML` (AI/ML Security)** | `SE-APP` or `SE-OFF` | 500 hrs (25%) | Software supply chain/MLOps security or adversarial prompt injection testing overlap. |
| **`SE-ICAM` (Identity & Access)** | `SE-CLD` or `SE-PKI` | 500 hrs (25%) | Cloud IAM federation or certificate-based authentication overlap. |
| **`SE-PKI` (Cryptography/PKI)** | `SE-ICAM` or `SE-APP` | 500 hrs (25%) | Authentication infrastructure or code signing/cryptographic primitive overlap. |
| **`SE-ICS` (Industrial Control)** | Licensed Electrician / Navy Nuclear | 500 hrs (25%) | Physical process and electrical instrumentation overlap. **0 hrs from commercial IT/AppSec.** |
| **`SE-DFIR` (Digital Forensics)** | Core Generalist Apprenticeship | 0 hrs (0%) | **Evidentiary isolation.** Forensic chain of custody requires 100% domain-specific runtime. |

---

## 8. Endorsement Stacking & Continuing Maintenance
* **Multiple Endorsements:** Practitioners may earn and maintain multiple endorsements across their career by completing required specialized hours or practical exams.
* **Unified Competency Maintenance:** Endorsements do not require separate recurring commercial renewal fees. All endorsements are maintained concurrently through validated professional practice hours and Board-approved continuing technical development.