# Specialty Track Specification: Identity, Credential & Access Management (`SE-ICAM`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-ICAM                                          |
| Discipline: Identity, Credential & Access Management                        |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 1 Discipline Tracking (100% RJPB Baseline)             |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Identity is the foundational security boundary of modern distributed architecture. The Identity, Credential & Access Management specialty (`SE-ICAM`) governs the engineering, protocol federation, credential protection, privileged account isolation, and automated governance lifecycle required to enforce Zero Trust access control across human users, services, and machine workloads.

This specialty covers directory architectures, federation protocols (SAML 2.0, OpenID Connect, OAuth 2.0, SCIM), Privileged Access Management (PAM), passwordless and phishing-resistant multi-factor authentication (FIDO2 / WebAuthn), and Identity Governance and Administration (IGA).

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Enterprise Architect / Identity Architect (`SP-ARC-001`):** Designing enterprise identity fabric, cross-organization trust federation, and single sign-on (SSO) architectures.
* **Primary Work Role 2: Systems Administrator (`PR-INF-001`):** Managing directory service schemas, PAM vaults, just-in-time credentialing systems, and service principal lifecycles.
* **Primary Work Role 3: Network Operations Specialist (`OM-NET-001`):** Implementing conditional access policies, identity-aware proxies, and Zero Trust Network Access (ZTNA) connectors.

### B. Authoritative Identity, Federation & Access Standards
1. **NIST SP 800-63-3 / SP 800-63-4:** Digital Identity Guidelines covering Identity Assurance Levels (IAL), Authenticator Assurance Levels (AAL), and Federation Assurance Levels (FAL).
2. **CISA Zero Trust Maturity Model (Identity Pillar):** Implementing automated credential rotation, dynamic risk-based access policies, and continuous validation.
3. **FIDO Alliance & W3C WebAuthn Standards:** Standardizing public-key cryptography authenticators and phishing-resistant passkey implementations.
4. **OAuth 2.0 & OpenID Connect Core Specifications (RFC 6749, RFC 7519, RFC 7662):** Enforcing secure token grant types, PKCE flows, and JWT validation.
5. **NIST SP 800-207:** Zero Trust Architecture baselines governing the Policy Decision Point (PDP) and Policy Enforcement Point (PEP).


---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-ICAM` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the line-of-sight supervision of an active `SE-ICAM` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-ICAM: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION            |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: Enterprise Federation, SSO & Directory Sync     ──► 500 Hours
  ├─► Domain 2: Privileged Access Management (PAM) & Ephemeral ──► 500 Hours
  ├─► Domain 3: Phishing-Resistant MFA & Passwordless Infra     ──► 500 Hours
  └─► Domain 4: Identity Governance, Lifecycle & Entitlements   ──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: Enterprise Federation, SSO & Directory Synchronization (500 Hours)
* Engineering cross-domain identity federation architectures with SAML 2.0, OpenID Connect, and OAuth 2.0 with strict claim mappings and token signing verification.
* Implementing automated cross-tenant user provisioning and deprovisioning via SCIM (System for Cross-domain Identity Management) connectors.
* Hardening Active Directory, Microsoft Entra ID, Okta, and open-source identity providers against token replay, golden ticket, and pass-the-hash attacks.

### Domain 2: Privileged Access Management (PAM) & Ephemeral Credentials (500 Hours)
* Deploying enterprise PAM vaults for automated credential check-in/check-out, session recording, and live keystroke logging.
* Implementing Just-In-Time (JIT) access workflows, dynamic credential generation, and Zero Standing Privileges (ZSP) across server and cloud estates.
* Managing service account lifecycles, gMSAs, and programmatic API secret rotations without operational downtime.

### Domain 3: Phishing-Resistant MFA & Passwordless Infrastructure (500 Hours)
* Architecting enterprise deployments of FIDO2 hardware security keys, WebAuthn passkeys, and certificate-based authentication (CBA / PIV / CAC).
* Deprecating phishable authentication factors (SMS, voice calls, unencrypted push notifications) across critical enterprise applications.
* Designing risk-based conditional access policies enforcing device health, geolocation sanity, and impossible travel telemetry.

### Domain 4: Identity Governance, Lifecycle & Entitlements (500 Hours)
* Implementing Identity Governance and Administration (IGA) solutions for automated joiner-mover-leaver (JML) provisioning.
* Conducting entitlement recertification campaigns, segregation of duties (SoD) conflict detection, and orphaned account sweeps.
* Integrating identity telemetry into SIEM/SOAR platforms for automated credential suspension upon threat detection.

---

## 3. Master of Record (MoR) Authority for Identity & Access Management

A Master Practitioner holding the `SE-ICAM` Endorsement possesses statutory sign-off authority for:

1. **Enterprise Federation Trust Certification:** Formally stamping and certifying cross-organizational federation bridges, third-party vendor trust relationships, and SSO configurations.
2. **Emergency Break-Glass Credential Access Authorization:** Sole statutory authority to witness, authorize, and audit the usage of emergency break-glass root accounts during major operational crises.
3. **Privilege Architecture Recertification:** Certifying enterprise Zero Standing Privilege (ZSP) baselines and access entitlement reviews for statutory compliance audits.
4. **Notice of Safety Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) if privileged administrative access is granted without MFA, session logging, or least-privilege scoping.

---

## 4. Strict Cross-Crediting & Articulation Boundaries

* **Cross-Crediting from Cloud Security (`SE-CLD`):** Up to **500 hours credit** toward Domain 1 (Federation & Directory Sync) for verified multi-cloud IAM experience.
* **Cross-Crediting from Cryptography & PKI (`SE-PKI`):** Up to **500 hours credit** toward Domain 3 (Certificate-Based Authentication & FIDO2) for verified PKI infrastructure experience.
* **Zero Cross-Crediting from Routine User Helpdesk:** Basic password resets, ticket logging, and active directory user creation tickets provide **0 hours of cross-credit** toward `SE-ICAM`.

---

## 5. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
