---
layout: default
title: Contributing & RFCs
---

# Contributing to The Cybersecurity Trade Project

Thank you for your interest in contributing to The Cybersecurity Trade Project. This initiative is structured as an open-source, vendor-neutral standard to build an accountable, accessible, and rigorous skilled trade framework for the cybersecurity industry.

> **Scope & Contribution Pathways:**
> * **Documentation Fixes (`[DOCS]`):** Typo corrections, internal link repairs, and wording clarifications via direct Pull Request.
> * **Framework Amendments (`[PROPOSAL]`):** Curriculum updates, template forms, or metric clarifications via Issue and Pull Request.
> * **Architectural & Governance Changes (`[RFC]`):** Major statutory, legal, or economic policy debates via the formal RFC process in `rfcs/`.
> * **AI Collaboration Standard:** All automated or AI-assisted contributions must adhere strictly to [AGENTS.md](AGENTS.md).

---

## 1. Guiding Principles for Contributions
1. **Practicality Over Pedantry:** Proposals must reflect real-world operational workflows, enterprise engineering constraints, and proven skilled trade mechanics (modeled after civil engineering, electrical trades, and healthcare).
2. **Accessible Upward Mobility & Anti-Gatekeeping:** Avoid mechanisms that enforce wealth, academic degree inflation, or arbitrary pedigree barriers. Preserve rigor through verified hands-on operational hours, objective lab exams, and competency milestones.
3. **Vendor Neutrality & Open Standards:** Reference open public frameworks (NIST SP 800-181 NICE, NIST CSF, CIS Controls, ISO/IEC, DOL Registered Apprenticeships) rather than proprietary commercial products or vendor-locked credentials.
4. **Labor-Enterprise Balance:** Proposals should align the protections and safety of frontline engineering labor with the economic incentives and risk reduction requirements of enterprise employers and insurance underwriters.
5. **NIST-Grade Precision & Clarity:** Specifications must maintain direct, active syntax and regulatory precision without conversational filler, passive nominalization chains, or arbitrary jargon bloat. All specialized statutory terms must be indexed in [GLOSSARY.md](GLOSSARY.md).

---

## 2. How to Propose Changes

### Ideation & Open Discussion
* For open-ended questions, brainstorming, or broad philosophical alignment, start a thread in **GitHub Discussions** before opening formal issues.

### Documentation Fixes & Clarifications
* For typos, broken internal links, or phrasing clarifications, open an Issue using the **Documentation & Clarification Fix** template (`[DOCS]`) or submit a direct Pull Request.

### Structural Framework Proposals & Amendments
* For targeted amendments (e.g., modifying domain rotation hours, altering baseline wage floors, adding new specialty endorsements, or revising board governance structures):
  1. Open a formal issue using either the **Framework Proposal / Amendment** (`[PROPOSAL]`) or **New Specialty Track Proposal** (`[SPECIALTY TRACK]`) template.
  2. State the operational justification, threat/actuarial impact, and how the change maintains alignment with the core 7 pillars.
  3. Once community consensus is established, submit a focused Pull Request referencing the Issue.

---

## 3. The Request for Comments (RFC) Process

Major architectural debates, statutory legal riders, complex economic models, or new operational protocols (such as surge staffing ratios or fractional MoR liability apportionment) are managed through the formal **RFC Process**.

### When is an RFC Required? (The Decision Matrix)

To balance agile development with community peer review, proposed changes follow a clear decision threshold:

* **Direct Pull Request (No RFC Needed):**
  * Fleshing out an existing Specialty Track curriculum (e.g., expanding `SE-ICS` or `SE-AIML` competency rubrics).
  * Adding standardized procedural templates or administrative forms (e.g., `FORM-001`, `FORM-002`, `FORM-003`).
  * Resolving contradictory wording, metric discrepancies, or domain hour mappings across specifications.
  * Routine documentation clarifications, typography hygiene, link repairs, and FAQ additions.

* **Formal RFC Process Required:**
  * **Legal & Liability Apportionment:** Shifting statutory accountability, introducing contractual safe harbor riders, or altering malpractice definitions (e.g., RFC 0001).
  * **Safety Ratio & Headcount Variances:** Establishing temporary exceptions to supervisory headcount ratios or on-shift density rules (e.g., RFC 0002).
  * **Mandatory Prerequisites & Elevation Gates:** Introducing new mandatory instructional quotas or qualification gates for licensure tiers (e.g., RFC 0003).
  * **Core Economic Model Changes:** Altering baseline wage floor percentages, Related Technical Instruction (RTI) compensation rules, or Taft-Hartley trust funding mechanics.
  * **Governance Restructuring:** Modifying Board composition, voting seat allocations, or Guild charter bylaws.

---

### RFC Submission Lifecycle

1. **Fork the Repository:** Create a working branch off `main` (e.g., `rfc/my-feature-name`).
2. **Draft the Document:** Copy `rfcs/0000-template.md` to `rfcs/000X-short-name.md` using the next available 4-digit index.
3. **Submit a Pull Request:** Open a PR titled `RFC: [Title of Proposal]` with the `Status: Proposed` in the header.
4. **Link Discussion:** Create a corresponding thread in [GitHub Discussions](https://github.com/the-cyber-trade-project/framework/discussions) under the **Architecture & RFCs** category linking to your PR.
5. **Review & Adoption:** Once the community and maintainers reach consensus:
   * The RFC status is updated to `Accepted` and merged into the `rfcs/` directory.
   * Implementation Pull Requests are opened against the relevant files in `framework/`, `governance/`, or `pillars/`.

---

## 4. Directory & File Architecture

Ensure proposed changes are placed in the appropriate directory:
* `pillars/`: High-level foundational principles and structural design (Pillars I through VII).
* `framework/`: Quantitative and operational standards (wage floors, supervisory ratios, velocity rules, logbook schemas, specialty endorsements, contractor models, and CISO scopes).
* `governance/`: Legal, board, craft guild, and industry transition mechanics.
* `rfcs/`: Formal Requests for Comments, architectural proposals, and active community debates.
* `faq.md` & `glossary.md`: Canonical trade definitions, practitioner FAQs, and enterprise implementation guidance.
* `AGENTS.md`: Guidelines and quality gates for AI-assisted contributions and agent workflows.
* `README.md`: Master architectural overview and project roadmap.

---

## 5. AI & Automated Contributions (AGENTS.md)

Contributors are welcome to use AI assistants (ChatGPT, Claude, Copilot, Cline, etc.) to help format, research, and draft contributions. However, all AI-assisted work must adhere to the policies established in [AGENTS.md](AGENTS.md):

* **Human Accountability:** You are personally responsible for every word in your PR. If you cannot explain and defend a proposal in your own words, do not submit it.
* **Progressive Disclosure:** Substantive proposals must include a plain-English summary (TL;DR) and an operational practical scenario so human readers can quickly digest the requirements.
* **Zero AI Clichés & Buzzwords:** AI filler phrases, marketing jargon, and sycophantic greetings are strictly prohibited.
* **No Unverified Citations:** Never submit AI-generated statutory, legal, or NIST citations without independently verifying their authenticity.

---

## 6. Style & Terminology Standards
* **Voice:** Professional, direct, authoritative, and policy-grounded. Avoid marketing buzzwords, vague abstractions, and hyperbolic claims.
* **Canonical Terminology:** Consistently use established trade definitions:
  * **National Cybersecurity Trade Board** (the statutory licensure and standard-setting authority)
  * **The Cybersecurity Craft Guild** (the workforce representation, labor advocacy, and JATC body)
  * **Master Practitioner** (personal 12,000+ hr credential tier) vs. **Master of Record / MoR** (statutory sign-off role)
  * **Licensed Cybersecurity Trade Contractor** (commercial entity / LLC / MSSP model)
  * **Fractional Master of Record (vMoR)** (fractional compliance authority for SMBs)
  * **Operational Exception Flag** (frontline internal logging) vs. **Notice of Safety Non-Concurrence** (formal legal refusal filing)
  * **Related Technical Instruction (RTI)** & **Joint Apprenticeship and Training Committee (JATC)**
  * **Actuarial Attestation Feed** (zero-knowledge insurer compliance telemetry API)
* **Formatting:** Use standard Markdown. Favor tables for comparative metrics and numbered lists for sequential requirements.
* **Automated Quality Gate Testing:** Before submitting a Pull Request, run the local specification quality gate to verify link integrity, typography, and RFC schema compliance:
  ```bash
  python3 scripts/validate-specifications.py
  ```
  *(All PRs must pass the automated GitHub Actions Specification Quality Gate before merge).*

---

## 6. Release Cadence & Versioning Strategy

To maintain stability for enterprise adopters, insurance underwriters, and educational institutions, this project follows Semantic Versioning (`vMAJOR.MINOR.PATCH`) under a release-gated cadence:

* **Direct Commits to `main` (No Tag):** Typo fixes, internal link repairs, markdown formatting, issue templates, and non-breaking documentation tooling.
* **Patch Releases (`v1.x.x`):** Batched policy clarifications, resolving contradictory metrics (such as hours or supervisory ratios), and statutory wording updates.
* **Minor Releases (`v1.x.0`):** Substantive framework milestones, including complete Specialty Endorsement curricula (e.g., AI/ML Assurance, MedTech), contractor frameworks, model state compact legislation, or actuarial feed schemas.
* **Major Releases (`v2.0.0`):** Structural revisions to the foundational 7 Pillars, changes to the core 8,000-hour rotational model, or fundamental governance overhauls based on pilot cohort data.