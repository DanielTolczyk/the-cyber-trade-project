# Specialty Track Specification: Offensive Security & Adversary Emulation (`SE-OFF`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-OFF                                           |
| Discipline: Offensive Security & Adversary Emulation                        |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 2 High-Risk Operational (+15% to +20% Wage Adder)      |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Offensive Security & Adversary Emulation (`SE-OFF`) governs the authorized, controlled simulation of adversary tactics, techniques, and procedures (TTPs) to evaluate the defensive resilience of systems, networks, applications, and human processes.

Because offensive operations involve live exploitation, tool detonation, and bypass of protective controls on operational or staging infrastructure, practitioners operate under rigorous Rules of Engagement (RoE), legal safe-harbor boundaries, and strict risk-containment protocols to prevent unintended production outages or data loss.

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Exploitation Analyst (`AN-EXP-001`):** Analyzing vulnerabilities, engineering custom proof-of-concept exploits, bypassing defense mechanisms, and testing protocol resilience.
* **Primary Work Role 2: Software Developer / Tool Author (`SP-DEV-001`):** Developing custom red-team implants, payload delivery mechanisms, obfuscation frameworks, and post-exploitation automation.
* **Primary Work Role 3: Cyber Defense Analyst / Purple Teamer (`PR-CDA-001`):** Collaborating with defensive blue teams to correlate offensive telemetry with detection logs, validate SIEM/EDR detection rules, and improve alert coverage.

### B. Authoritative Testing Methodologies & Adversary Emulation Frameworks
1. **Penetration Testing Execution Standard (PTES):** Standardizing pre-engagement interactions, intelligence gathering, threat modeling, vulnerability analysis, exploitation, post-exploitation, and reporting.
2. **MITRE ATT&CK Framework & ATT&CK Evaluations:** Structuring adversary emulation plans directly against documented threat actor campaigns and behavioral techniques.
3. **NIST SP 800-115:** Technical Guide to Information Security Testing and Assessment.
4. **Open Source Security Testing Methodology Manual (OSSTMM v3):** Measuring operational security posture, trust boundaries, and human security interaction.
5. **CISA Red Team Assessment Methodology:** Standardizing multi-disciplinary government and critical infrastructure red team tradecraft.


---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-OFF` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the line-of-sight supervision of an active `SE-OFF` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-OFF: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION             |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: External Surface & Network Penetration Testing  ──► 500 Hours
  ├─► Domain 2: Application, API & Microservice Exploitation    ──► 500 Hours
  ├─► Domain 3: Internal Lateral Movement, AD & EDR Evasion    ──► 500 Hours
  └─► Domain 4: Purple Teaming, Detection Engineering & RoE     ──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: External Surface & Network Penetration Testing (500 Hours)
* Executing non-destructive reconnaissance, asset enumeration, edge vulnerability verification, and perimeter penetration testing.
* Validating perimeter firewall rules, VPN appliances, reverse proxies, and external remote access protocols.
* Authoring reproducible technical finding packages with proof-of-concept evidence, CVSS v4.0 scoring, and clear defensive remediation steps.

### Domain 2: Application, API & Microservice Exploitation (500 Hours)
* Conducting deep manual penetration testing of web applications, REST/GraphQL APIs, and mobile platforms.
* Discovering complex business logic flaws, broken access controls (BOLA/BFLA), server-side request forgery (SSRF), and authentication bypasses.
* Crafting deterministic, non-destructive payloads to prove exploitability without data corruption.

### Domain 3: Internal Lateral Movement, AD & EDR Evasion (500 Hours)
* Emulating advanced adversary tradecraft across Active Directory and hybrid Entra ID environments (Kerberoasting, AS-REP roasting, ACL abuse, Shadow Admin escalation).
* Testing host-based detection capabilities through process injection, syscall manipulation, AMSI/ETW bypass testing, and token manipulation.
* Establishing resilient, encrypted Command & Control (C2) infrastructure with strict egress filtering compliance.

### Domain 4: Purple Teaming, Detection Engineering & RoE Governance (500 Hours)
* Designing and executing collaborative Purple Team exercises with Security Operations Center (SOC) teams.
* Mapping offensive actions in real-time to SIEM/EDR detection timelines to identify detection gaps and blind spots.
* Drafting Rules of Engagement (RoE), defining deconfliction protocols, emergency stop triggers, and establishing strict scope boundaries.

---

## 3. Master of Record (MoR) Authority for Offensive Security

A Master Practitioner holding the `SE-OFF` Endorsement possesses statutory sign-off authority for:

1. **Rules of Engagement (RoE) Safety Authorization:** Legally binding approval of offensive testing scopes, live exploit techniques, deconfliction windows, and emergency kill-switch procedures.
2. **Penetration Test & Red Team Certification Stamp:** Formally stamping offensive assessment reports for regulatory compliance (e.g., PCI DSS Requirement 11, SOC 2 Type II, DORA Article 26 TLPT).
3. **Attack Surface Resilience Clearance:** Certifying to cyber underwriters that high-risk perimeter findings have been remediated and independently re-tested.
4. **Notice of Safety Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) if offensive assessments are executed without authorized RoE boundaries, against out-of-scope third-party infrastructure, or during forbidden operational freezes.

---

## 4. Strict Cross-Crediting & Articulation Boundaries

* **Cross-Crediting from Application Security (`SE-APP`):** Up to **500 hours credit** toward Domain 2 (Application & API Exploitation) for verified manual application security testing.
* **Zero Cross-Crediting with Industrial Controls (`SE-ICS`):** Standard enterprise red-teaming does **not** cross-credit toward OT environments. Live exploitation tools can cause kinetic plant trips.
* **Zero Cross-Crediting with DFIR (`SE-DFIR`):** Forensic investigation and offensive emulation require separate runtime tracks.

---

## 5. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Code of Ethics & Professional Conduct](../code-of-ethics-and-conduct.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
