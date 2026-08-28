# Universal Logbook Standards & Competency Ledger

The Universal Digital Logbook provides an immutable, verifiable record of a practitioner's hands-on operational experience, eliminating resume inflation, subjective hiring screens, and the need for redundant technical interviews.

---

## 1. Dual-Format Verification (Digital & Physical Modalities)

To accommodate varied enterprise environments, classified enclaves, and offline physical sites, the framework recognizes two official logbook modalities:

* **Digital Signed Ledger (Standard Format):** An open-standard JSON/Markdown ledger exported from the practitioner's local tooling or Git vault. The supervising Journeyman validates entries and digitally signs the submission using their cryptographic Trade Key.
* **Physical Bound Ledger (Offline / Classified Format):** A standard, tamper-evident physical logbook. For each operational task or sprint milestone, the apprentice logs the domain, hours, and sanitized ticket ID, and the supervising Journeyman physically signs their name, license number, and date.

---

## 2. Logbook Entry Schema
Every operational entry submitted by an apprentice includes:
* **Timestamp & Duration:** Verified hours dedicated to the specific operational task.
* **NICE Framework Work Role Alignment:** Direct mapping to standardized NIST NICE specialty areas (e.g., PR-CDO-001, OM-NET-001, PR-INF-001).
* **Technical Domain Classification:** Core rotational domain (Perimeter/Cloud, SOC/Triage, IAM, Vulnerability Management, or Defensive GRC).
* **Anonymized Artifact Reference:** Internal ticket ID, change request hash, or lab module completion code that verifies completed work without exposing sensitive data.
* **Supervisor Attestation:** Cryptographic digital signature or physical stamp/signature with the active license number of the supervising Journeyman or Master Practitioner.

---

## 3. Operational Workflow & Batch Approvals
To prevent administrative overhead in fast-paced enterprise environments:
* **Periodic Batch Sign-Offs:** Supervisors review and sign off on cumulative operational hours on a weekly, bi-weekly, or monthly cadence based on sprint logs or change management tickets.
* **Simulation & Range Credit:** Up to **1,000 hours (12.5%)** of the 8,000-hour requirement may be logged through Board-accredited high-fidelity cyber range exercises and structured adversary simulation labs.

---

## 4. Intake & Accreditation Workflow
* **Digital Intake:** Apprentices upload their signed JSON ledger export to the JATC portal or Board Clearinghouse. The system programmatically validates the supervisor's cryptographic signature against the active Board Registry.
* **Physical Intake:** Apprentices maintaining physical bound ledgers present their logbook to the regional JATC Training Director during quarterly wage tier evaluations and prior to the Journeyman Licensure Exam. The panel audits the physical entries against supervisor license records and stamps the verified hours into the registry.
* **Public Verification Interface:** Prospective employers, insurance auditors, and state licensing boards verify accredited hours and milestone completions via a secure, read-only Board API.

---

## 5. Data Privacy, Zero-Knowledge Schema & Worker Ownership

To ensure logbooks remain auditable without exposing enterprise proprietary secrets or violating non-disclosure agreements:

* **Statutory Worker Property:** The Universal Logbook is legally recognized as the personal property of the individual practitioner (analogous to an airline pilot's flight ledger or a master electrician's work book). It is permanently portable across employers, contract gigs, and career breaks.
* **Zero-Knowledge Architecture:** The logbook records *what* engineering competency was exercised (NICE work role ID) and for *how long* (verified duration), paired with a sanitized ticket hash or change request ID. It strictly omits customer proprietary data, internal IP addresses, source code, payload artifacts, or business details.
* **Export Safe Harbor:** Because the logbook utilizes zero-knowledge schema hashes, exporting or maintaining a personal logbook export does not violate standard corporate NDAs or intellectual property covenants.

---

## 6. Integrity, Auditing & Anti-Hostage Dispute Protections

* **Falsification Penalties:** Falsifying logbook entries or signing off on unperformed hours constitutes professional fraud, resulting in immediate suspension of both the apprentice's registration and the supervisor's license.
* **Supervisory Dispute Appeals & Anti-Hostage Safe Harbor:** 
  * Employers and supervisors are legally prohibited from withholding logbook sign-offs, conditioning hour verification on post-employment non-disparagement concessions, or threatening departing workers over logbook exports.
  * If a supervisor withholds sign-offs maliciously or due to contractual separation disputes, the apprentice may file an [Ethics & Conduct Incident Report (Form FORM-004)](../templates/FORM-004_ethics-and-conduct-incident-report.md).
  * The JATC Training Panel conducts an administrative ticket audit and peer review, retroactively stamping accredited hours directly into the Board Clearinghouse without requiring employer consent.

