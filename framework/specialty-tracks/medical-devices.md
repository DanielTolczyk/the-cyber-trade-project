# Specialty Track Specification: Medical Device & Clinical Technology Security (`SE-MED`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-MED                                           |
| Discipline: Medical Device & Clinical Technology Security                   |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Wage Adder:  +20% to +25% above Regional Journeyman Prevailing Benchmark    |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Regulatory Frameworks & NIST NICE Mapping

Medical device cybersecurity is governed by life-safety constraints where technical vulnerabilities directly impact patient safety, clinical performance, and diagnostic integrity. This specialty covers the complete medical technology spectrum: **embedded firmware / physical devices (SiMD), Software as a Medical Device (SaMD), companion mobile health apps, and cloud-connected clinical platforms**.

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate core competencies mapped directly to federal work roles:
* **Primary Work Role 1: Software Developer (`SP-DEV-001`):** Secure coding, firmware signing, memory-safe design, and interface isolation across SiMD, SaMD, and mobile health apps.
* **Primary Work Role 2: Security Control Assessor (`SP-SRP-001`):** Component threat modeling, attack surface analysis, vulnerability verification, and non-product R&D tooling qualification.
* **Primary Work Role 3: Cybersecurity Management (`OV-MGT-001`):** Total Product Life Cycle (TPLC) governance, FDA Section 524B compliance packaging, and risk management documentation.

### B. Sector-Specific Consensus Standards & Regulatory Baselines
1. **FDA Statutory Authority (Section 524B):** Compliance with statutory requirements for "cyber devices" under the Federal Food, Drug, and Cosmetic Act (FD&C Act), ensuring devices are designed, developed, and maintained with verified cybersecurity safeguards.
2. **FDA Premarket Cybersecurity Guidance:** Implementing the Total Product Life Cycle (TPLC) security recommendations required for Premarket Submissions (510(k), PMA, De Novo, and eSTAR cybersecurity packages).
3. **Medical Device Risk Management (AAMI TIR57 / ANSI/AAMI/ISO 14971):** Integrating cybersecurity risk analysis directly with medical device safety risk management, evaluating threats through the lens of clinical harm.
4. **Post-Market Management (AAMI TIR97):** Executing post-market surveillance, patch management, and coordinated vulnerability disclosure (CVD) workflows throughout the operational device lifecycle.
5. **Medical Software Processes (IEC 62304 / ISO 13485):** Ensuring secure coding practices, architecture segregation, and quality system integration for software in medical devices (SiMD) and software as a medical device (SaMD).
6. **Global Regulatory Harmonization (IMDRF & EU MDR):** Integrating international medical cybersecurity baselines, including IMDRF N60 principles, EU Medical Device Regulation (EU MDR 2017/745 / MDCG 2019-16), and IEC 81001-5-1 health software lifecycle security to ensure products meet harmonized global premarket clearance requirements.

---

## 2. Medical Device Security Risk Architecture

Practitioners must execute security risk engineering focused on device reliability and patient safety across three distinct architectural profiles:

### A. Safety Risk & Harm Integration
* Security risk assessments must directly map technical vulnerabilities to clinical hazard analyses (ISO 14971).
* Threat events are evaluated based on their potential to impair therapy delivery, corrupt diagnostic sensor data, delay emergency alerts, or breach clinical network isolation.

### B. Product Threat Modeling across Architectural Profiles
* **Profile 1: Embedded Hardware & Firmware (SiMD):** Microcontrollers, on-chip peripherals, physical interfaces, and local wireless links (BLE, Wi-Fi, NFC, proprietary RF).
* **Profile 2: Software as a Medical Device (SaMD) & Clinical AI:** Standalone diagnostic software, clinical decision support (CDS) algorithms, AI/ML imaging pipelines, and web-based diagnostic platforms.
* **Profile 3: Connected Clinical Ecosystems & Mobile Health:** Patient mobile applications (iOS/Android), clinical docking portals, bedside programmer units, and cloud telemetry backbones.
* Threat modeling execution utilizes structured frameworks (AAMI TIR57, STRIDE) mapped directly to design controls.

### C. Non-Product Software & R&D Tooling Assessment
* Evaluating non-product software and automated tooling used in manufacturing, calibration, automated testing, and R&D pipelines to ensure tool qualification and prevent supply chain contamination.

---

## 3. Secure Design & Engineering Controls

Practitioners must design, audit, and verify defensive controls across the device and connected ecosystem:

* **Hardware & Firmware Integrity (SiMD):** Implementing Hardware Root of Trust (HRoT), Secure Boot with cryptographically signed firmware, secure on-chip key storage (TPM / Secure Enclave), and disabling JTAG/UART diagnostic interfaces on production hardware.
* **Software as a Medical Device (SaMD) & Cloud Platform Defense:** Enforcing clinical algorithm integrity, secure API architectures, multi-tenant clinical data isolation, and robust logging telemetry for cloud-connected diagnostic systems.
* **Companion Mobile Health Application Hardening:** Enforcing secure local storage (iOS Keychain / Android Keystore), certificate pinning, biometric authentication for therapy delivery, and anti-tampering / anti-reverse-engineering controls.
* **Interface Isolation & Cryptography:** Enforcing mutual TLS (mTLS) or authenticated cryptographic pairings for inter-device communications, programmer-to-device handshakes, and patient telemetry streams.
* **Software Bill of Materials (SBOM):** Generating, validating, and maintaining machine-readable SBOMs (SPDX or CycloneDX) across all commercial off-the-shelf (COTS), third-party, and open-source software components.
* **Fail-Safe Clinical Defaults:** Ensuring systems enter a fail-safe clinical state upon cybersecurity failure, loss of connectivity, or cryptographic certificate expiration without disrupting life-sustaining therapies.

---

## 4. Post-Market Surveillance & Vulnerability Management

* **Coordinated Vulnerability Disclosure (CVD):** Managing external security researcher reporting channels, coordinated disclosure timelines, and regulatory reporting thresholds.
* **Clinical Vulnerability Scoring:** Utilizing Stakeholder-Specific Vulnerability Categorization (SSVC) and CVSS scoring adapted for patient safety to prioritize vulnerability remediation.
* **Patch Verification & Regression Safety Testing:** Ensuring cybersecurity hotfixes, security updates, and firmware patches undergo complete clinical safety and regression testing prior to field distribution.

---

## 5. Rotational Runtime Ledger (2,000 Post-Licensure Hours)

To achieve the `SE-MED` endorsement, a Licensed Journeyman or Master Practitioner must log a minimum of **2,000 verified operational runtime hours** under the line-of-sight supervision of an active `SE-MED` Master Practitioner across four specialized domains:

| Specialty Domain | Minimum Runtime | Core Focus & Operational Activities |
| :--- | :--- | :--- |
| **Domain 1: Threat Modeling, Safety Risk & Architecture** | 600 hrs | AAMI TIR57 threat modeling, safety harm integration, trust boundary mapping across hardware, app, and cloud interfaces. |
| **Domain 2: System Security Implementation (SiMD, SaMD, Mobile, or Cloud)** | 500 hrs | *Fulfillable via one or more specialized focus areas:*<br>• **Embedded/SiMD:** Secure Boot, firmware signing, memory safety, hardware interface isolation.<br>• **SaMD / Cloud:** Cloud medical platform security, clinical AI model integrity, secure API architectures.<br>• **Mobile / Digital Health:** Mobile patient app hardening, certificate pinning, secure enclave storage. |
| **Domain 3: SBOM Lifecycle, Non-Product Software & Triage** | 500 hrs | SPDX/CycloneDX authoring, automated CVE correlation, SSVC clinical risk triage, regression safety testing. |
| **Domain 4: Premarket Regulatory Packaging & Audits** | 400 hrs | FDA Section 524B readiness packaging, eSTAR cybersecurity documentation compilation, quality system audit defense. |

---

## 6. Statutory Sign-Off Authority

A certified Master Practitioner holding the active `SE-MED` endorsement possesses statutory authority to execute:

1. **Premarket FDA Cybersecurity Readiness Sign-Off:** Formally certifying that a medical device's cybersecurity architecture, threat model, SBOM, and risk management documentation conform to FDA Section 524B statutory requirements for premarket submission.
2. **Clinical Safety Deployment Clearance:** Authorizing firmware updates, connected clinical network integrations, and post-market safety patches for field distribution.

---

## 7. Relationship to Application & Software Product Security (`SE-APP`) & Cross-Crediting

The trade differentiates general commercial software and product security from life-safety medical device engineering:

* **The Core Distinction:** Application & Software Product Security (`SE-APP`) focuses on commercial software, APIs, mobile apps, and product pipelines to mitigate business and operational risk. Medical Device Security (`SE-MED`) enforces strict clinical patient harm integration (ISO 14971 / AAMI TIR57) and statutory federal premarket clearance (FDA Section 524B).
* **Cross-Crediting Bridge from `SE-APP` to `SE-MED`:** Practitioners holding an active `SE-APP` endorsement receive **1,000 hours (50%) credit** toward `SE-MED` for shared technical foundations (threat modeling, secure coding, SBOM lifecycle, and vulnerability triage). They must complete the 1,000-hour clinical bridge in medical device threat modeling, clinical hazard integration, and FDA eSTAR regulatory packaging.
* **Articulation Credit from `SE-MED` to `SE-APP`:** Practitioners holding an active `SE-MED` endorsement receive full articulation credit for `SE-APP`, as medical device engineering encompasses a rigorous superset of software product security controls.


