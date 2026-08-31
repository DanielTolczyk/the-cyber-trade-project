# Universal Logbook Standards & Competency Ledger

The Universal Digital Logbook provides an immutable, verifiable record of a practitioner's hands-on operational experience, eliminating resume inflation, subjective hiring screens, and the need for redundant technical interviews.

---

## 1. Four Recognized Supervisor Attestation Modalities

To accommodate varied enterprise environments, classified enclaves, and offline physical sites, the framework recognizes four official supervisor attestation modalities:

* **Modality A: Asymmetric WebAuthn & FIDO2 Signing (Web PKI & Passkey):** The supervising Journeyman reviews pending shift batches in the PWA or web portal and cryptographically signs using an ECDSA (P-256 or Ed25519) hardware passkey registered to their active trade license ID.
* **Modality B: Git Vault & Cryptographic Commit Signing (GPG / SSH / Sigstore):** For detection engineering, automation, and DevSecOps rotations, the supervisor reviews the apprentice's change pull requests and applies a verified GPG or SSH commit signature to the logbook repository branch.
* **Modality C: Physical Bound Book & Embossed JATC Stamp (Classified SCIF / Air-Gap):** Inside classified defense facilities (SCIF) or air-gapped industrial control zones where digital recording devices are prohibited, the apprentice maintains a serialized, tamper-evident paper ledger. The supervising Journeyman physically stamps and signs each shift with their license number, transcribed into the digital registry during quarterly JATC panel audits.
* **Modality D: Enterprise SSO & Automated Shift Attestation (SAML / OIDC Federation):** In high-volume enterprise SOCs and MSSPs, shift hours are validated programmatically via enterprise identity provider (IdP) assertions tied to ticketing CAB approvals and supervisor badge verification.

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

---

## 7. Client-Side Cryptographic Vault Architecture & At-Rest Encryption

To protect practitioner career data when operating on shared workstations, SCIF terminals, or college labs:

* **WebCrypto AES-256-GCM Encryption:** Local storage vaults are encrypted at rest using authenticated 256-bit AES in Galois/Counter Mode (AES-GCM).
* **PBKDF2 Key Derivation:** Cryptographic encryption keys are derived dynamically in volatile memory from a user-selected 4-digit PIN using PBKDF2 with 100,000 iterations of SHA-256 and a 16-byte random salt. The PIN itself is never stored in browser memory, disk storage, or LocalStorage.
* **Inactivity Auto-Lock & Memory Wiping:** After 15 minutes of inactivity or upon manual lock, the client application encrypts the active ledger into an authenticated ciphertext envelope and wipes all plaintext shift entries from browser RAM.
* **Shared Workstation Recovery Guardrail:** If an unencrypted terminal is reset or local storage cleared, practitioners restore their authenticated ledger using their encrypted backup archive file (`.ctp-vault` or `.json`) without requiring employer intervention.

---

## 8. Dual-Recipient Hybrid Envelope Submission Model

To allow formal JATC training audits without introducing centralized backdoor vulnerabilities:

* **Zero-Backdoor Principle:** The National Board does not maintain master decryption keys for local practitioner vaults.
* **Hybrid Envelope Submissions:** When an apprentice submits an audit batch for statutory wage step elevation:
  1. The shift records are encrypted with an ephemeral 256-bit AES data key.
  2. The data key is encrypted under the apprentice's personal public key (Envelope A) and simultaneously encrypted under the National Board JATC public key (Envelope B).
  3. The combined hybrid package is submitted to the Clearinghouse. The JATC panel decrypts only the specific submitted shift batch using the Board private key in an authenticated hardware security module (HSM).

