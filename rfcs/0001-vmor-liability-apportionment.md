# RFC 0001: Statutory Scope of Work and Liability Apportionment for Fractional Masters of Record (vMoR)

* **Status:** Proposed
* **Author(s):** Daniel Tolczyk (@DanielTolczyk)
* **Related Specifications:** `framework/contractors-and-consulting.md`, `framework/ethics-and-refusal.md`, `pillars/05_liability-insurance.md`
* **Created:** 2026-08-25

---

## 1. Executive Summary

The `v1.2.0` specification establishes the **Fractional Master of Record (vMoR)** framework, permitting small-to-medium businesses (SMBs) to retain licensed Master Practitioners through accredited Trade Contractors for statutory compliance sign-offs, architectural audits, and supervisory oversight. 

However, standard corporate incident attribution often blurs the line between **architectural design liability** and **day-to-day administrative malpractice**. If an SMB client suffers a catastrophic data breach or ransomware event while retaining a vMoR on a fractional basis (e.g., 5–10 hours per month), the legal system risks conflating periodic engineering review with continuous operational management.

This RFC defines the formal legal, procedural, and cryptographic boundaries separating fractional architectural sign-offs from internal corporate culpability, codifying a standard **vMoR Scope-of-Work (SOW) Statutory Rider** and point-in-time attestation mechanisms.

---

## 2. Motivation & Trade Context

In professional engineering (PE) and civil architecture, a structural engineer who stamps a building blueprint is held liable if the foundation collapses due to a demonstrable mathematical or material design defect. They are *not* held liable if the building owner subsequently removes a load-bearing column, disables fire suppression systems, or fails to perform basic facility maintenance.

In cybersecurity, this boundary is historically muddy:
* Corporate executives often assume a fractional consultant or vCISO is a universal scapegoat for all breach events.
* Insurers require clarity on whether a claim falls under the enterprise's cyber liability policy or the contractor's Errors & Omissions (E&O) surety bond.
* Highly skilled Master Practitioners will refuse fractional engagements if periodic advisory reviews expose their personal licenses and business entities to unbounded liability for client operational failures.

---

## 3. Detailed Specification & Proposed Architecture

### 3.1 The "Point-in-Time & Policy Stamp" Standard
A Fractional Master of Record's statutory liability attaches **strictly and exclusively** to:
1. Architectural baselines and technical policies explicitly reviewed, validated, and cryptographically signed with the MoR's Trade Key.
2. Automated CI/CD pipeline gating and policy-as-code admission controllers explicitly certified by the MoR.
3. Verification of internal practitioner logbook telemetry and supervisory ratio compliance within the contracted audit window.

### 3.2 Standardized Statutory Boundary Matrix

| Incident Vector | Primary Liability Attachment | Regulatory & Insurance Disposition |
| :--- | :--- | :--- |
| **Defective Baseline Design:** Breach caused by a fundamental structural flaw in an architecture explicitly stamped by the vMoR as compliant. | **Contractor E&O / vMoR Surety** (Subject to Trade Malpractice Review) | Covered under Trade Contractor E&O; Board investigates whether design conformed to prevailing NIST/trade building codes. |
| **Unapproved Change / Shadow IT:** Breach caused by unapproved infrastructure changes, shadow SaaS deployments, or disabled controls bypass. | **Enterprise Executive Leadership** (Safe Harbor for vMoR) | Enterprise Cyber Liability absorbs loss; vMoR fully shielded via telemetry audit logs. |
| **Ignored Warning / Overridden Baseline:** Breach occurs along a vector where the vMoR previously filed an *Operational Exception Flag* or *Notice of Safety Non-Concurrence*. | **Overriding Corporate Officer(s)** (Personal & Enterprise Liability) | Liability transferred entirely to executive management per `framework/ethics-and-refusal.md`; underwriter may invoke non-compliance deductibles. |
| **Credential Phishing / End-User Social Engineering:** Routine operational credential compromise where IAM baselines (e.g., enforced FIDO2/MFA) were stamped but bypassed by user action. | **Enterprise Operations** (Safe Harbor for vMoR) | Enterprise Cyber Liability; no contractor malpractice attachment unless IAM design was deficient. |

### 3.3 The Mandatory vMoR Statutory Scope Rider (Contract Clause)
All accredited Trade Contractors delivering fractional MoR services must incorporate the following statutory rider into client Master Services Agreements (MSAs):

```text
SECTION [X]: STATUTORY TRADE ACCORD & MASTER OF RECORD SCOPE BOUNDARIES
(a) Scope of Technical Authority: The designated Master of Record (MoR) acts strictly as a statutory 
    architectural and standards-compliance authority. The MoR does not provide continuous real-time 
    operational monitoring, administrative credential management, or direct command over client staff 
    outside the specific audited milestones.
(b) Operational Integrity Warranty: Client warrants that all infrastructure modifications, policy exceptions, 
    and architectural deviations executed outside the MoR's scheduled review intervals shall be documented 
    and submitted for retrospective review.
(c) Liability Shield & Executive Non-Concurrence: Client acknowledges that overriding a formal safety baseline 
    or failing to remediate an Operational Exception Flag logged by the MoR triggers an automatic Notice 
    of Safety Non-Concurrence, transferring statutory liability exclusively to Client's executive officers.
```

---

## 4. Drawbacks, Edge Cases & Risk Analysis

* **The "Negligent Audit" Defense:** A client might argue that a vMoR *should* have caught an active misconfiguration during their monthly 5-hour review.
  * *Mitigation:* The logbook schema must record the exact cryptographic inventory hash of the assets audited during that session. The vMoR is only accountable for evaluating the data state made visible during the formal audit window.
* **Superficial Rubber-Stamping:** Disreputable contractors might offer low-cost, automated vMoR stamps without conducting substantive reviews.
  * *Mitigation:* Enforce the **5-account cap** per Master Practitioner (`framework/supervisory-ratios.md`) and subject randomly sampled fractional attestations to National Board telemetry audits.

---

## 5. Prior Art & Real-World Precedents

* **Professional Engineers (PE) Blueprint Stamping:** National Council of Examiners for Engineering and Surveying (NCEES) model rules on responsible charge and inspection scope.
* **Fractional CFO / Outside Auditor Scope:** AICPA independence standards and Sarbanes-Oxley (SOX) section 302/404 sign-off protections.
* **Maritime Marine Surveyors:** Point-in-time seaworthiness certificates that shield the surveyor if the shipmaster subsequently overloads the vessel or alters ballast tanks.

---

## 6. Implementation & Roadmap

* **Target Release:** `v1.3.0`
* **Impacted Documents:**
  * `framework/contractors-and-consulting.md` (Add Section 4.1: "Statutory Liability Apportionment & Audit Bound Riders").
  * `framework/logbook-schema.md` (Add optional `audit_inventory_manifest_hash` property to `underwriter-attestation.json`).