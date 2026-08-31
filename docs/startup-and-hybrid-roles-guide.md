---
layout: default
title: Startup Generalists & Hybrid Engineering Guide
permalink: /docs/startup-and-hybrid-roles-guide.html
---

# Startup Generalists & Hybrid Engineering Guide

## Operational Runtime Ledger, Multi-Craft Accords & Fractional Governance

This specification establishes operational standards, runtime hour allocation matrices, and supervisory attestation pathways for cybersecurity practitioners working in hybrid disciplines (such as DevSecOps, Platform Security, and Security Infrastructure Engineering) and early-stage startup environments where practitioners perform generalist duties across multiple technical domains.

---

## 1. The Multi-Craft Reality & Inter-Guild Jurisdiction

In modern cloud organizations, defensive cybersecurity responsibilities frequently intersect with software engineering, site reliability engineering (SRE), and IT systems administration. The Cybersecurity Trade Project approaches these cross-functional responsibilities through the **Digital Infrastructure Trades Council (DITC)** model, codified in the [Guild Formation Charter](../governance/guild-formation-and-charter.md) (Section 11).

### A. Task-Based Competency Accounting vs. Job Titles
The trade standard does not gatekeep or evaluate arbitrary corporate job titles. Instead, runtime accreditation is anchored strictly to verified operational execution mapped to official **NIST NICE SP 800-181 Work Role IDs**:

* **Defensive Engineering Allocation:** Operational hours spent hardening infrastructure, developing security policy-as-code, configuring identity and access management (IAM), conducting threat modeling, triaging alerts, and managing vulnerabilities count directly toward the 8,000-hour Journeyman trade ledger across the 5 Core Domains.
* **Product Feature & Logic Development:** Hours spent strictly on generic application business logic or product feature development can be dual-credited toward Related Technical Instruction (RTI) coursework or cross-credited into sister software engineering guilds through Bilateral Articulation Accords.

### B. DevSecOps & AppSec Domain Allocation Matrix
For practitioners operating in hybrid DevSecOps or Platform Security roles, typical weekly shifts allocate runtime across three core domains:

| Weekly Activity | NIST NICE Work Role | Primary Trade Domain | Credited Ledger Scope |
| :--- | :--- | :--- | :--- |
| **CI/CD Security Automation & SAST/DAST** | `SP-DEV-001` / `SP-SRP-001` | **Domain 3: Software & AppSec** | Pipeline policy enforcement, dependency scanning, container signing. |
| **Cloud IAM & Infrastructure-as-Code Hardening** | `SP-ARC-002` / `PR-CDO-001` | **Domain 1: Defensive Infrastructure** | Terraform/OpenTofu baseline hardening, KMS key rotation, VPC boundary rules. |
| **Vulnerability Triaging & Patch Verification** | `AN-TWA-001` / `OM-NET-001` | **Domain 4: Threat Intelligence** | CVE impact analysis, dependency upgrade validation, patch regression testing. |
| **Threat Modeling & Architectural Review** | `SP-ARC-001` | **Domain 3: Software & AppSec** | STRIDE/DREAD system threat models, boundary data flow validation. |


---

## 2. Startup Generalists & Solo Practitioner Protocols

Early-stage startups and small businesses rarely maintain specialized, segregated cybersecurity teams. Frontline engineers often function as generalists handling IT provisioning, infrastructure security, customer audit questionnaires, and emergency incident response.

### A. Accelerated Multi-Domain Exposure
While enterprise practitioners may be confined to narrow operational silos (such as tier-1 alert queues), startup generalists naturally accumulate balanced runtime across all 5 core domains:

* **Domain 1 (Defensive Infrastructure & Network Hardening - 1,500 hrs):** Firewall configuration, endpoint protection, zero-trust network access (ZTNA), and SSO integrations.
* **Domain 2 (Active Defense, SOC & Incident Triage - 2,000 hrs):** PagerDuty alert response, log aggregation, anomaly investigation, and phishing mitigation.
* **Domain 3 (Secure System Architecture & Software Assurance - 1,500 hrs):** Cloud infrastructure-as-code, container registries, secret management, and code reviews.
* **Domain 4 (Threat Intelligence, Vulnerability & Remediation - 1,500 hrs):** Vulnerability scanner triaging, dependency updates, bug bounty validations, and hardening benchmarks.
* **Domain 5 (Governance, Risk, Compliance & Auditing - 1,500 hrs):** SOC 2 Type II audit evidence collection, ISO 27001 readiness, access reviews, and customer vendor security reviews.

### B. The Fractional Master of Record (vMoR) Retainer Model
Startups with fewer than 50 employees are not required to maintain a full-time Master Practitioner on W-2 payroll. Under [Executive Leadership & The CISO Role](../framework/executive-and-ciso.md) (Section 2) and [Licensed Trade Contractors & Consulting](../framework/contractors-and-consulting.md):

* **Periodic Audit & Baseline Stamping:** Startups retain an accredited **Fractional Master of Record (vMoR)** or Licensed Cybersecurity Trade Contractor for scheduled quarterly architectural reviews, annual baseline sign-offs, and compliance filings.
* **Apprentice Oversight Bridge:** When an apprentice or junior engineer is the sole security practitioner at a startup, their supervisory line-of-sight is maintained through scheduled weekly technical reviews with the retained Fractional Master or regional JATC Training Director.

### C. Third-Party Attestation & Modality B Git Signing
For startup practitioners working without an on-site Journeyman:
1. **Modality B (Cryptographic Git Signatures):** Pull requests containing Terraform configurations, security policies, and automation scripts are signed with GPG or SSH commit keys and archived with immutable pipeline run hashes.
2. **Quarterly JATC Panel Verification:** The regional JATC Training Director reviews the candidate's sanitized commit digests and ticket references, applying the formal trade audit seal to lock verified runtime hours.

---

## 3. Labor Protections & Benefit Portability for High-Turnover Environments

Startups carry inherent macroeconomic volatility, including runway exhaustion, acquisitions, pivots, and workforce reductions. The trade architecture protects startup practitioners through three institutional safeguards:

### A. Taft-Hartley Hour-Bank Health Shield
Under [Dues Structure & Labor Trusts](../governance/dues-and-trust-economics.md), employer contributions ($7.00/hour) fund a multi-employer health trust. Startup employees accumulate excess hours into a personal Hour Bank (up to a 6-month reserve). If a startup dissolves or executes layoffs:
* Family medical, dental, and vision coverage continues seamlessly from the Hour Bank reserve.
* Workers avoid expensive COBRA premiums and retain their doctors while interviewing for their next placement.

### B. Two-Check Defined Benefit Pension Vesting
Retirement contributions travel with the practitioner across all participating employers. A practitioner who works at three different startups over 5 years accumulates a unified 5,000-hour vesting clock, guaranteeing an independent monthly Defined Benefit Pension check upon retirement regardless of whether individual startups survive.

### C. JATC Dispatch Clearinghouse Re-Employment
When a startup downshifter or layoff occurs, licensed Journeymen and registered Apprentices enter the JATC Dispatch Clearinghouse immediately, receiving priority placement with participating enterprise employers, municipal defense programs, or licensed contractor firms with zero recruiter middleman fees.

---

## 4. Summary of Operational Roles

| Environment | Supervisory Ratio | Attestation Modality | Master of Record (MoR) Model |
| :--- | :--- | :--- | :--- |
| **Enterprise SOC / MSSP** | 2:1 (2 Apprentices per Journeyman) | Modality A (WebAuthn / Passkey) or Modality D (Enterprise SSO) | Full-time internal Principal or CISO |
| **Hybrid DevSecOps / Cloud** | 3:1 (3 Apprentices per Journeyman) | Modality B (Git GPG / Commit Hash) | Dual-Hat Executive or Delegated Principal |
| **Startup (Solo / Small Team)** | 1:1 Remote / JATC External Oversight | Modality B (Git Signing) + JATC Quarterly Stamp | Fractional Master of Record (vMoR) |
| **Classified Defense / SCIF** | 2:1 (Direct Physical Oversight) | Modality C (Serialized Bound Book) | Internal Dedicated Facility MoR |