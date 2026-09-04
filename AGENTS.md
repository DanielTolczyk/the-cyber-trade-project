---
layout: default
title: AI Collaboration & Standards Drafting Policy
---

# AI Collaboration & Standards Drafting Policy (AGENTS.md)

The Cybersecurity Trade Project uses automated tools, large language models (LLMs), and automated continuous integration suites to assist in drafting, schema synchronization, and specification validation.

This document establishes the canonical standards for AI-assisted contributions, ensuring all specifications maintain the technical precision, statutory rigor, and structural clarity expected of an authoritative public standard.

---

## 1. Audience & Regulatory Scope

All specifications, governance charters, and curricula are drafted for four primary institutional stakeholders:
1. **Labor Regulators & Standards Bodies:** U.S. Department of Labor (OA/SAA), state apprenticeship councils, and international vocational bodies reviewing statutory compliance (29 CFR Part 29, Taft-Hartley Section 302(c), ERISA).
2. **Cyber Insurance Underwriters & Actuaries:** Actuarial consortia and syndicates evaluating risk stratification, labor-backed warranty credits, and loss prevention telemetry.
3. **Enterprise Leadership & Counsel:** CISOs, CIOs, and General Counsels evaluating liability transfer instruments, contractor capacity limits, and operational workforce structures.
4. **Master Engineers, Journeymen & Apprentices:** Frontline practitioners executing defensive rotations, supervising shifts, and maintaining trade logbooks.

---

## 2. Specification Architecture (NIST / RFC Standard)

Substantive framework specifications, pillar expansions, and specialty track curricula must adhere to formal standards-body structure:

* **1. Purpose, Scope & Applicability (Informative Overview):**
  An authoritative introductory framing defining the operational objective, affected roles, and regulatory baseline before introducing technical requirements.
* **2. Normative Requirements & Quantifiable Thresholds (Normative Core):**
  Unambiguous, active-voice statutory and operational requirements, including exact hour distributions, mandatory supervisory ratios, wage step percentages, and schema definitions.
* **3. Implementation Guidance & Procedural Workflows (Informative Reference):**
  Concrete calculation models (e.g., localized MSA wage indexing formulas), procedural workflows (e.g., FORM-001 Notice of Safety Non-Concurrence filing sequences), and administrative guidelines.

---

## 3. The NIST-Grade Precision Standard

Contributions must reflect the drafting rigor of a NIST Special Publication or Department of Labor standard:

* **Active Voice & Syntactic Economy:**
  Write in direct, active subject-verb construction. Prohibit passive nominalization chains (e.g., write "Supervisors verify logbook hours" rather than "The operational execution of verification mechanisms is performed by supervisory personnel").
* **Zero Dilution of Technical & Statutory Precision:**
  Never dumb down technical standards, statutory citations, or actuarial models. Retain established legal and technical terminology (*ERISA*, *Taft-Hartley 302(c)*, *NIST SP 800-181 work role IDs*, *RJPB*, *Master of Record*).
* **Glossary Integration Mandate:**
  Specialized statutory, labor, or insurance terms must be formally indexed in [GLOSSARY.md](GLOSSARY.md) to enable interactive hover discovery for newcomers without diluting normative text.
* **Zero AI Slop & Sycophancy:**
  Prohibit conversational filler, marketing hyperbole, rhetorical questions, and corporate clichés. State requirements directly, authoritatively, and neutrally.
* **The Real-World Precedent Mapping Mandate (Zero Synthetic Neologisms):**
  We adapt proven, real-world trade mechanisms; we do not invent speculative governance jargon, corporate consulting abstractions, or pseudo-academic neologisms. Every labor, training, referral, and governance mechanism must map 1:1 to an established statutory or trade precedent:
  * *Statutory Apprenticeship Baselines:* Title 29 CFR Parts 29 and 30 (U.S. Department of Labor Registered Apprenticeship Programs). Standard terminology: *Pre-Apprentice*, *Registered Apprentice*, *Specialty Candidate*, *Licensed Journeyman*, *Master Practitioner*, *Master of Record*. Prohibit corporate or synthetic neologisms (never "practitioner tiers", "standing profiles", or "competency personas").
  * *Multi-Employer Trust Administration:* Taft-Hartley / LMRA Section 302(c) and ERISA multi-employer trusts. Standard terminology: *Joint Apprenticeship and Training Committee (JATC)*, *Related Technical Instruction (RTI)*, *Modular Continuing Education*, *Hour-Bank Trust*. Prohibit consulting frameworks (never "Horizons", "skill streams", or "upskilling journeys").
  * *Hiring Hall & Referral Dispatch:* Standard trade dispatch rules (IBEW/NECA, UA). Standard terminology: *Out-of-Work Register*, *First-In, First-Out (FIFO) Seniority*, *Dispatch Book 1 (Resident Local)*, *Book 2 (Traveler)*, *Bilateral Referral Slip*, *Supervised Specialty Dispatch*. Prohibit synthetic routing jargon (never invented pseudo-academic credentials or bilateral mesh abstractions).
  * *Labor Economics & Telemetry:* Department of Labor and Bureau of Labor Statistics (BLS) standards. Standard terminology: *Structural Deficit*, *Transient Demand Spike (Normalized)*, *Balanced Supply*, *Persistent Labor Shortage Index (PLSI)*. Prohibit consulting hype terms (never synthetic fad narratives, speculative dampening models, or corporate speed buzzwords).


---

## 4. Permitted vs. Prohibited AI Workflows

### Permitted AI Functions
* **Automated Formatting & Structural Linting:** Markdown formatting, table alignment, and schema validation.
* **Standards Cross-Referencing:** Mapping proposed competencies to NIST SP 800-181 NICE task codes, OWASP SAMM, or IEC 62443 baselines.
* **Test Fixture Generation:** Authoring unit and integration test fixtures for sister tools (`estimator`, `logbook`, `clearinghouse`).
* **Drafting from Human Engineering Directives:** Structuring technical outlines into formal specification templates.

### Strictly Prohibited AI Functions (The Cut-Off Line)
* **Unreviewed Bulk Generation:** Submitting synthetic text that has not been line-by-line verified by a qualified human practitioner.
* **Hallucinated Standards or Citations:** Introducing fabricated NIST IDs, imaginary legal precedents, or false statutory references.
* **Autonomous PR Execution:** Opening, approving, or merging pull requests without explicit human initiation and oversight.
* **Front-Running Active RFC Consensus:** Unilaterally resolving open architectural debates on `main` while community RFCs remain active.

---

## 5. Automated Specification Quality Gate

All AI-assisted contributions must pass the local and CI specification quality gate before PR submission:

```bash
python3 scripts/validate-specifications.py
```

The gate automatically enforces:
* Zero typography defects (0 em-dashes, 0 en-dashes, 0 emojis, 0 prohibited phrases).
* 100% relative link integrity across all internal specifications.
* Strict immutability of the 7 Core Pillars.
* RFC schema compliance and active RFC branch protection.
* Front-end security SAST invariants.
