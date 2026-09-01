# Specialty Track Specification: Cryptographic Infrastructure & PKI (`SE-PKI`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-PKI                                           |
| Discipline: Cryptographic Infrastructure & PKI                              |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 1 Discipline Tracking (100% RJPB Baseline)             |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Cryptographic infrastructure and Public Key Infrastructure (PKI) represent the mathematical bedrock of data confidentiality, message integrity, non-repudiation, and digital identity across all computing systems. The Cryptographic Infrastructure & PKI specialty (`SE-PKI`) governs the engineering, lifecycle management, Hardware Security Module (HSM) deployment, key generation ceremonies, and Post-Quantum Cryptography (PQC) migration required to secure enterprise ecosystems.

This specialty spans enterprise Certificate Authorities (CAs), automated certificate issuance (ACME, SCEP, EST), code signing architectures, TLS termination, symmetric key management, and cryptographic algorithm agility.

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Enterprise Architect / Cryptographic Engineer (`SP-ARC-001`):** Designing multi-tier CA hierarchies, cryptographic trust stores, and enterprise encryption standards.
* **Primary Work Role 2: Software Developer (`SP-DEV-001`):** Implementing cryptographic primitives, safe key derivation functions (KDFs), and memory-safe cryptographic libraries.
* **Primary Work Role 3: Security Control Assessor (`SP-SRP-001`):** Auditing cryptographic implementations for algorithm deprecation (SHA-1, 3DES, RSA-1024), entropy weakness, and compliance with FIPS standards.

### B. Authoritative Cryptographic Standards & Algorithm Baselines
1. **NIST SP 800-57 (Parts 1-3):** Recommendation for Key Management, establishing key states, crypto periods, and key protection mechanisms.
2. **FIPS 140-3:** Security Requirements for Cryptographic Modules (Level 1 through Level 4 hardware security standards).
3. **NIST Post-Quantum Cryptography Standards (FIPS 203, FIPS 204, FIPS 205):** Implementing ML-KEM, ML-DSA, and SLH-DSA algorithms for quantum resistance.
4. **CA/Browser Forum Baseline Requirements:** Standardizing certificate profiles, revocation timelines (OCSP / CRL), and certificate transparency (CT) logging.
5. **RFC 5280, RFC 8555 & RFC 7030:** Internet X.509 Public Key Infrastructure, Automatic Certificate Management Environment (ACME), and Enrollment over Secure Transport (EST).


---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-PKI` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the line-of-sight supervision of an active `SE-PKI` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-PKI: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION             |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: Multi-Tier CA Hierarchy & Root Isolation       ──► 500 Hours
  ├─► Domain 2: HSM Deployment & Formal Key Ceremonies          ──► 500 Hours
  ├─► Domain 3: Automated Certificate Management & MTLS        ──► 500 Hours
  └─► Domain 4: Post-Quantum Cryptography (PQC) & Agility       ──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: Multi-Tier CA Hierarchy & Root Isolation (500 Hours)
* Designing offline Root Certificate Authorities and intermediate issuing CAs with strict Certificate Policy and Certification Practice Statement (CP/CPS) documentation.
* Managing Online Certificate Status Protocol (OCSP) responders, Certificate Revocation Lists (CRLs), and delta CRL publication pipelines.
* Engineering cross-certification agreements, bridge CAs, and internal private CA infrastructures.

### Domain 2: HSM Deployment & Formal Key Ceremonies (500 Hours)
* Deploying and partitioning FIPS 140-3 Level 3 Hardware Security Modules (network and PCIe HSMs).
* Drafting formal Key Ceremony scripts and executing dual-control, M-of-N quorum key generation, backup, and destruction ceremonies.
* Implementing enterprise Key Management Interoperability Protocol (KMIP) servers for database and storage volume encryption.

### Domain 3: Automated Certificate Management & MTLS (500 Hours)
* Deploying automated certificate lifecycle protocols (ACME, SCEP, EST) across web servers, microservices, and network devices to eliminate certificate expiration outages.
* Architecting enterprise-wide mutual TLS (mTLS) with SPIFFE/SPIRE for cryptographically authenticated service mesh communication.
* Engineering code signing pipelines with timestamping authority (TSA) integration and key usage restrictions.

### Domain 4: Post-Quantum Cryptography (PQC) & Cryptographic Agility (500 Hours)
* Conducting comprehensive enterprise cryptographic asset inventories (discovering vulnerable RSA/ECC algorithms across protocols and data stores).
* Engineering hybrid classical/quantum-safe TLS cipher suites and SSH configurations adhering to NIST FIPS 203/204/205 standards.
* Designing algorithm-agile software frameworks capable of rapid cryptographic primitive replacement without re-architecting applications.

---

## 3. Master of Record (MoR) Authority for Cryptography & PKI

A Master Practitioner holding the `SE-PKI` Endorsement possesses statutory sign-off authority for:

1. **Root CA Key Ceremony Master Attestation:** Sole authorized witness and executing engineer legally certifying Root CA key generation, migration, and destruction ceremonies.
2. **Enterprise CP/CPS Approval Stamp:** Formal sign-off on organizational Certificate Policy and Certification Practice Statements for compliance audits and third-party trust federation.
3. **Cryptographic Deprecation Waiver Certification:** Statutory authority to review, approve, or reject temporary operational waivers for deprecated cryptographic ciphers (e.g., SHA-1, TLS 1.0).
4. **Notice of Safety Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) if root private keys are extracted from HSMs, shared across unsegmented environments, or generated without M-of-N quorum protection.

---

## 4. Strict Cross-Crediting & Articulation Boundaries

* **Cross-Crediting from Identity Management (`SE-ICAM`):** Up to **500 hours credit** toward Domain 3 (Automated Certificate Management & MTLS) for verified certificate-based authentication and directory integration.
* **Cross-Crediting from Application Security (`SE-APP`):** Up to **500 hours credit** toward Domain 3 (Code Signing & Software Cryptography) for verified software supply chain provenance and artifact signing experience.
* **Zero Cross-Crediting with Physical Locksmithing or Generic Sysadmin:** Basic web server TLS certificate purchasing does not satisfy specialized PKI engineering hours.

---

## 5. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
