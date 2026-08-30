# Specialty Endorsements & Domain Architecture

Cybersecurity is not a monolith. Following the completion of foundational generalist rotations (Years 1-2), practitioners pursue specific technical endorsements that validate deep architectural, operational, and regulatory expertise.

> **Note on Credentials:** Any commercial certifications mentioned under domain tracks are **strictly non-binding illustrative examples** of current industry alignments. The National Cybersecurity Trade Board holds sole statutory authority to evaluate, validate, or design objective, vendor-neutral challenge exams for each endorsement.

---

## 1. The Three-Layer Specialty Architecture

To prevent arbitrary curriculum design and ensure every trade endorsement remains vendor-neutral, federally accredited, and mathematically verifiable, all specialty tracks are structured in a standardized **Three-Layer Hierarchy**:

```
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 1: NIST NICE WORKFORCE TAXONOMY (The Foundation)                     |
| Canonical mapping to national NIST SP 800-181 Work Role IDs and standardized|
| Knowledge, Skills, and Tasks (KSTs). Ensures federal workforce recognition. |
+─────────────────────────────────────────────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 2: SECTOR-SPECIFIC CONSENSUS STANDARDS (The Building Codes)           |
| Authoritative technical frameworks governing the domain:                    |
| • Medical Devices: FDA Section 524B, AAMI TIR57, ANSI/AAMI/ISO 14971        |
| • Product Security: NIST IR 8259, ETSI EN 303 645, EU Cyber Resilience Act  |
| • Industrial Controls: IEC 62443, NERC CIP                                  |
| • Cloud Architecture: CIS Cloud Benchmarks, Cloud Shared Responsibility     |
+─────────────────────────────────────────────────────────────────────────────+
                                       │
                                       ▼
+─────────────────────────────────────────────────────────────────────────────+
| LAYER 3: TRADE OPERATIONAL LEDGER & AUTHORITY (The Skilled Trade Rules)     |
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
| **Industrial Control Systems (ICS/SCADA)** | `SE-ICS` | `OM-NET-001`, `SP-ARC-001`, `PR-CDO-001` | **Statutory Life-Safety (+20% to +25%)** | *Draft in Progress* |
| **Digital Forensics & Incident Response** | `SE-DFIR` | `IN-FOR-001`, `PR-CIR-001`, `AN-TWA-001` | **High-Liability (+15% to +20%)** | *Draft in Progress* |
| **Offensive Security & Red Teaming** | `SE-OFF` | `AN-EXP-001`, `SP-DEV-001` | **High-Risk Operational (+15% to +20%)** | *Draft in Progress* |
| **AI / ML Security Assurance** | `SE-AIML` | `SP-DEV-001`, `AN-TWA-001`, `SP-SRP-001` | **Emerging Technology (+15% to +20%)** | *Draft in Progress* |
| **Cloud Security & Infrastructure** | `SE-CLD` | `SP-ARC-001`, `OM-NET-001`, `PR-INF-001` | **Architectural Complexity (+10% to +15%)** | *Draft in Progress* |
| **Application & Software Product Security** | `SE-APP` | `SP-DEV-001`, `SP-SRP-001`, `PR-VAM-001` | **Discipline Endorsement (Standard Base)** | *Draft in Progress* |
| **Identity, Credential & Access (ICAM)** | `SE-ICAM` | `SP-ARC-001`, `PR-INF-001`, `OM-NET-001` | **Discipline Endorsement (Standard Base)** | *Draft in Progress* |
| **Cryptographic Infrastructure & PKI** | `SE-PKI` | `SP-ARC-001`, `SP-DEV-001` | **Discipline Endorsement (Standard Base)** | *Draft in Progress* |

---

## 3. Core Generalist Foundation (Mandatory Prerequisite)
Before pursuing specialty endorsements, all apprentices must log validated operational hours across four foundational disciplines (Years 1-2):
1. **Network Defense & Protocols:** Packet inspection, stateful firewalling, DNS/routing security, traffic analysis.
2. **Identity & Access Management (IAM):** Directory services, PAM, OAuth/SAML, principle of least privilege, MFA architecture.
3. **Endpoint & Systems Hardening:** Linux/Windows internals, OS baselines, configuration management, vulnerability patching.
4. **Security Operations & Triage:** Incident classification, log correlation, alert triage, baseline threat detection.

---

## 4. Specialized Trade Branches (Tier 3 through Master)

### Branch A: Digital Forensics & Incident Response (DFIR)
* **Core Focus:** Active breach containment, memory and disk forensics, chain-of-custody evidence preservation, malware reverse engineering, and post-incident reconstruction.
* **Illustrative Examples / Equivalencies:** GCFA, GCFE, GNFA, GCIH (or Board Practical Challenge Exam).
* **Sign-off Authority:** Sworn evidentiary chain of custody, formal breach containment verification for insurance claims, and SEC/regulatory incident attestation.

### Branch B: Cyber Risk Management, Threat Modeling & Governance (GRC)
* **Core Focus:** Architectural threat modeling (STRIDE, PASTA), risk quantification (Open FAIR), security requirements authoring, NIST RMF, and ISO 27001 program governance.
* **Illustrative Examples / Equivalencies:** CRISC, Open FAIR, CISM.
* **Sign-off Authority:** Formal enterprise risk acceptances, statutory compliance readiness filings, and third-party vendor risk certifications.

### Branch C: Offensive Security & Adversary Emulation
* **Core Focus:** Network and application penetration testing, red teaming, exploit analysis, social engineering defense testing, and MITRE ATT&CK adversary emulation.
* **Illustrative Examples / Equivalencies:** OSCP, OSEP, GXPN, CREST.
* **Sign-off Authority:** Penetration test certification, external attack surface resilience sign-off.

### Branch D: Cloud Security & Infrastructure Architecture
* **Core Focus:** Multi-cloud security architecture (AWS/Azure/GCP), container and Kubernetes security, Infrastructure-as-Code (IaC) policy guardrails, CIEM/CSPM, and cloud workload protection.
* **Illustrative Examples / Equivalencies:** CCSP, AWS/Azure Advanced Security Specializations.
* **Sign-off Authority:** Cloud baseline architecture certification, automated deployment policy-guardrail sign-off.

### Branch E: Application & Software Product Security (SE-APP)
* **Core Focus:** Secure SDLC integration, component-level threat modeling, SAST/DAST/SCA tooling, API security, Software Bill of Materials (SBOM) lifecycle (CycloneDX/SPDX), non-product R&D tooling qualification, and PSIRT coordinated vulnerability management.
* **Illustrative Examples / Equivalencies:** CASE, CSSLP, specialized product and application security engineering credentials.
* **Sign-off Authority:** Production software and product security release clearance, SBOM compliance verification.
* **Detailed Standard:** [Specialty Track Specification: SE-APP Application & Software Product Security](specialty-tracks/application-security.md).

### Branch F: Medical Device & Clinical Technology Security (SE-MED)
* **Core Focus:** Embedded device firmware (SiMD), Software as a Medical Device (SaMD), companion mobile health apps, FDA Section 524B premarket compliance, AAMI TIR57 / ISO 14971 clinical safety risk integration, and SBOM lifecycle management.
* **Illustrative Examples / Equivalencies:** Biomedical engineering cybersecurity specializations, medical device security credentials (or Board Practical Challenge Exam).
* **Sign-off Authority:** Premarket FDA Section 524B cybersecurity readiness sign-off, clinical safety deployment clearance.
* **Detailed Standard:** [Specialty Track Specification: SE-MED Medical Device Security](specialty-tracks/medical-devices.md).

### Branch G: Industrial Control Systems (ICS / SCADA / OT)
* **Core Focus:** Purdue Model network segmentation, industrial protocols (Modbus, DNP3, CIP), Safety Instrumented Systems (SIS), IEC 62443, and NERC-CIP compliance.
* **Illustrative Examples / Equivalencies:** GICSP, GRID, GCIP.
* **Sign-off Authority:** Critical infrastructure safety cyber clearance, air-gapped system maintenance sign-off.

### Branch H: Identity, Credential & Access Management (ICAM)
* **Core Focus:** Enterprise Zero Trust architectures, cross-domain federation (SAML/OIDC), Privileged Access Management (PAM), secrets management lifecycle, and directory consolidation.
* **Illustrative Examples / Equivalencies:** CIAM, enterprise identity engineering credentials.
* **Sign-off Authority:** Enterprise federation sign-off, emergency root credential rotation attestation.

### Branch I: Cryptographic Infrastructure & PKI
* **Core Focus:** Hardware Security Module (HSM) deployment, enterprise PKI lifecycle, root CA isolation, key management ceremonies, and Post-Quantum Cryptography (PQC) migration.
* **Illustrative Examples / Equivalencies:** Board-approved cryptography and PKI engineering credentials.
* **Sign-off Authority:** Root CA key ceremony execution and witness sign-off, enterprise cryptographic standard migration sign-off.

---

## 5. Endorsement Stacking & Continuing Maintenance
* **Multiple Endorsements:** Practitioners may earn and maintain multiple endorsements across their career by completing required specialized hours or practical exams.
* **Unified Competency Maintenance:** Endorsements do not require separate recurring commercial renewal fees. All endorsements are maintained concurrently through validated professional practice hours and Board-approved continuing technical development.