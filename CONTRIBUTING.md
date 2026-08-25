# Contributing to The Cybersecurity Trade Project

Thank you for your interest in contributing to The Cybersecurity Trade Project. This initiative is structured as an open-source, vendor-neutral standard to build an accountable, accessible, and rigorous skilled trade framework for the cybersecurity industry.

---

## 1. Guiding Principles for Contributions
1. **Practicality Over Pedantry:** Proposals must reflect real-world operational workflows, enterprise engineering constraints, and proven skilled trade mechanics (modeled after civil engineering, electrical trades, and healthcare).
2. **Accessible Upward Mobility & Anti-Gatekeeping:** Avoid mechanisms that enforce wealth, academic degree inflation, or arbitrary pedigree barriers. Preserve rigor through verified hands-on operational hours, objective lab exams, and competency milestones.
3. **Vendor Neutrality & Open Standards:** Reference open public frameworks (NIST SP 800-181 NICE, NIST CSF, CIS Controls, ISO/IEC, DOL Registered Apprenticeships) rather than proprietary commercial products or vendor-locked credentials.
4. **Labor-Enterprise Balance:** Proposals should align the protections and safety of frontline engineering labor with the economic incentives and risk reduction requirements of enterprise employers and insurance underwriters.

---

## 2. How to Propose Changes

### Ideation & Open Discussion
* For open-ended questions, brainstorming, or broad philosophical alignment, start a thread in **GitHub Discussions** before opening formal issues.

### Documentation Fixes & Clarifications
* For typos, broken internal links, or phrasing clarifications, open an Issue using the **Documentation & Clarification Fix** template (`[DOCS]`) or submit a direct Pull Request.

### Structural Framework Proposals & Amendments
* For substantial structural changes (e.g., modifying domain rotation hours, altering baseline wage floors, adding new specialty endorsements, or revising board governance structures):
  1. Open a formal issue using either the **Framework Proposal / Amendment** (`[PROPOSAL]`) or **New Specialty Track Proposal** (`[SPECIALTY TRACK]`) template.
  2. State the operational justification, threat/actuarial impact, and how the change maintains alignment with the core 7 pillars.
  3. Once community consensus is established, submit a focused Pull Request referencing the Issue.

---

## 3. Directory & File Architecture

Ensure proposed changes are placed in the appropriate directory:
* `pillars/`: High-level foundational principles and structural design (Pillars I through VII).
* `framework/`: Quantitative and operational standards (wage floors, supervisory ratios, velocity rules, logbook schemas, specialty endorsements, and CISO scopes).
* `governance/`: Legal, board, craft guild, and industry transition mechanics.
* `faq.md` & `glossary.md`: Canonical trade definitions, practitioner FAQs, and enterprise implementation guidance.
* `README.md`: Master architectural overview and project roadmap.

---

## 4. Style & Terminology Standards
* **Voice:** Professional, direct, authoritative, and policy-grounded. Avoid marketing buzzwords, vague abstractions, and hyperbolic claims.
* **Canonical Terminology:** Consistently use established trade definitions:
  * **National Cybersecurity Trade Board** (the statutory licensure and standard-setting authority)
  * **The Cybersecurity Craft Guild** (the workforce representation, labor advocacy, and JATC body)
  * **Master Practitioner** (personal 12,000+ hr credential tier) vs. **Master of Record / MoR** (statutory sign-off role)
  * **Notice of Safety Non-Concurrence** (formal technical refusal filing)
  * **Related Technical Instruction (RTI)** & **Joint Apprenticeship and Training Committee (JATC)**
* **Formatting:** Use standard Markdown. Favor tables for comparative metrics and numbered lists for sequential requirements.

---

## 5. Release Cadence & Versioning Strategy

To maintain stability for enterprise adopters, insurance underwriters, and educational institutions, this project follows Semantic Versioning (`vMAJOR.MINOR.PATCH`) under a release-gated cadence:

* **Direct Commits to `main` (No Tag):** Typo fixes, internal link repairs, markdown formatting, issue templates, and non-breaking documentation tooling.
* **Patch Releases (`v1.0.x`):** Batched policy clarifications, resolving contradictory metrics (such as hours or supervisory ratios), and statutory wording updates.
* **Minor Releases (`v1.x.0`):** Substantive framework milestones, including complete Specialty Endorsement curricula (e.g., AI/ML Assurance, MedTech), model state compact legislation, or actuarial loss-prevention tables.
* **Major Releases (`v2.0.0`):** Structural revisions to the foundational 7 Pillars, changes to the core 8,000-hour rotational model, or fundamental governance overhauls.