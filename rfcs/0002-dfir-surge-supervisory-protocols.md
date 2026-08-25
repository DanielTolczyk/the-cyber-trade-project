# RFC 0002: Emergency Surge Capacity and Supervisory Ratio Flexibility in Active DFIR Engagements

* **Status:** Proposed
* **Author(s):** Daniel Tolczyk (@DanielTolczyk)
* **Related Specifications:** `framework/supervisory-ratios.md`, `framework/wage-scales.md`, `pillars/03_rotational-pipeline.md`, `pillars/06_craft-guilds-and-labor-trusts.md`
* **Created:** 2026-08-25

---

## 1. Executive Summary

The `framework/supervisory-ratios.md` specification enforces strict line-of-sight supervisory ratios (**2:1 Apprentice-to-Journeyman**, and **1:1 for Safety-Critical/OT environments**) to ensure quality mentorship and prevent labor exploitation. Furthermore, `framework/wage-scales.md` establishes on-call retainers and **1.5× surge compensation** for emergency incident response.

During major enterprise breaches, critical infrastructure compromises, or active ransomware containment, incident response (DFIR) consultancies and internal security teams experience sudden, non-linear operational spikes. Strict headcount ratios risk becoming an administrative bottleneck if firms cannot rapidly deploy surge staff. Conversely, removing ratios entirely during crises risks critical forensic errors, chain-of-custody destruction, or catastrophic operational missteps by unsupervised apprentices.

This RFC defines the **Emergency Incident Surge Protocol**, establishing strict functional role segregation, rapid-dispatch mechanisms via the Guild Hiring Hall, and time-bounded supervisory variance rules during declared security emergencies.

---

## 2. Motivation & Trade Context

When an enterprise activates an emergency DFIR engagement:
1. **The Velocity Imperative:** Containment, log analysis, and host triage must scale from 2 engineers to 20+ within hours.
2. **The Forensic Chain-of-Custody Constraint:** A single mishandled volatile memory dump or improperly contained domain controller can destroy legal admissibility or alert threat actors, triggering active wiper payloads.
3. **The Mentorship Paradox:** During an active Category 1/2 breach, Journeymen and Masters cannot pause containment actions to deliver pedagogical classroom-style instruction to apprentices.

We must define how emergency DFIR teams scale rapidly while preserving both forensic safety and trade labor integrity.

---

## 3. Detailed Specification & Proposed Architecture

### 3.1 Incident Role Segregation (The Tiered Containment Model)
During a declared security emergency, apprentice practitioners on the Incident Response track (`SE-DFIR`) are restricted to distinct operational tiers:

```
+─────────────────────────────────────────────────────────────+
|               Active Incident Command (Master of Record)    |
+─────────────────────────────────────────────────────────────+
                              │
       ┌──────────────────────┴──────────────────────┐
       ▼                                             ▼
+───────────────────────────+   +─────────────────────────────+
|   Tier 1: Support Ops     |   |   Tier 2: Live Containment  |
|  (Apprentices Allowed)    |   | (Journeyman / Master ONLY)  |
+───────────────────────────+   +─────────────────────────────+
| • Passive SIEM Log Parsing|   | • Memory Acquisition & Vol  |
| • Asset List Scrubbing    |   | • Domain Admin Remediation  |
| • User Verification Calls |   | • Kernel-level EDR Actions  |
| • Timeline Data Formatting|   | • Host Isolation Commands   |
| • IOC Ingestion Scripts   |   | • Threat Actor Negotiation  |
+───────────────────────────+   +─────────────────────────────+
```

* **Apprentice Scope Restriction:** Apprentices are **strictly barred** from executing destructive containment commands, making live forensic acquisitions of primary evidence, or modifying core directory services during an active incident.
* **Support Operational Scope:** Apprentices may execute passive, read-only, and structured data-processing workflows (log enrichment, timeline collation, automated sandbox submissions).

### 3.2 Emergency Supervisory Variance (The 4:1 Support Exception)
When an enterprise formally declares a **Category 1 (Catastrophic Enterprise Compromise)** or **Category 2 (Major Operational Outage)** incident:

1. **Support Ratio Expansion:** For **Tier 1 Support Ops tasks only**, the supervisory ratio expands from **2:1 to a maximum of 4:1** (4 Apprentices per 1 supervising Journeyman).
2. **Time Ceiling:** This ratio variance is valid for a **maximum of 72 consecutive hours** per declared engagement. Beyond 72 hours, the firm must transition back to standard 2:1 ratios or rotate in additional licensed Journeymen.
3. **Mandatory Master of Record Oversight:** Ratio variance is valid *only* if an active Master of Record is designated as the on-duty Incident Commander.

### 3.3 Guild Hiring Hall Rapid-Dispatch Protocol
If an incident response contractor requires immediate surge capacity exceeding its internal Journeyman bench:
* **The Rapid Dispatch Call:** The contractor issues an emergency dispatch request to the **Craft Guild JATC Hiring Hall / Clearinghouse Registry**.
* **Pre-Vetted Roster:** Available Journeymen and Masters registered on the National On-Call Surge Pool are dispatched with standardized 1.5× emergency rate cards, instantly satisfying supervisory ratio requirements without protracted vendor contract negotiations.

---

## 4. Drawbacks, Edge Cases & Risk Analysis

* **Abuse of Emergency Declarations:** Consultancies might declare artificial "emergencies" on routine assessments to permanently run 4:1 ratios and depress billing costs.
  * *Mitigation:* Every invocation of the 72-hour emergency variance must generate a unique `emergency_incident_declaration_id` reported in the quarterly Actuarial Attestation Feed. Insurers will audit firms with abnormal emergency variance frequencies.
* **Burnout & Apprentice Exhaustion:** Apprentices subjected to intense incident rotations could face severe burnout.
  * *Mitigation:* Retain the mandatory on-shift maximums (12 consecutive hours max, followed by 12 mandatory hours of rest). Surge pay differentials apply to all hours worked beyond standard shift baselines.

---

## 5. Prior Art & Real-World Precedents

* **Emergency Medical Services (EMS) / Triage Protocols:** Paramedic and nursing supervisory ratios expand during multi-casualty incidents (MCI) under strict protocolized delegation.
* **Wildland Firefighting Incident Command System (ICS):** Division and crew boss ratios (span-of-control rules: 1 supervisor to 3–7 personnel, optimized at 1:5) under the National Incident Management System (NIMS).
* **Maritime Damage Control:** Emergency watchstanding and damage control party delegation during active sea casualties.

---

## 6. Implementation & Roadmap

* **Target Release:** `v1.3.0`
* **Impacted Documents:**
  * `framework/supervisory-ratios.md` (Add Section 2.1: "Emergency Incident Surge Variance & DFIR Scopes").
  * `framework/wage-scales.md` (Cross-reference emergency declaration triggers for 1.5× surge pay).
  * `pillars/06_craft-guilds-and-labor-trusts.md` (Codify the Rapid-Dispatch Surge Pool in the Guild Hiring Hall).