# Specialty Track Specification: Application & Software Product Security (`SE-APP`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-APP                                           |
| Discipline: Application & Software Product Security                         |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 1 Discipline Tracking (100% RJPB Baseline)             |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Modern software engineering requires dedicated security tradecraft embedded throughout the software development lifecycle (SDLC). The Application & Software Product Security specialty (`SE-APP`) covers the engineering practices, automated CI/CD security controls, architectural threat modeling, software supply-chain defenses, and vulnerability disclosure protocols required to secure commercial software products, APIs, cloud-native microservices, mobile applications, and enterprise web platforms.

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Software Developer (`SP-DEV-001`):** Secure code authoring, defensive architectural patterns, input validation, cryptographic primitives, and memory-safe design.
* **Primary Work Role 2: Security Control Assessor (`SP-SRP-001`):** Component threat modeling, architectural risk reviews, SAST/DAST rule tuning, and pipeline security verification.
* **Primary Work Role 3: Vulnerability Assessment Analyst (`PR-VAM-001`):** Software vulnerability triage, root-cause flaw reproduction, dependency vulnerability validation, and exploit impact analysis.

### B. Open Technical Baselines & Engineering Standards
1. **OWASP Software Assurance Maturity Model (SAMM v2.0):** Evaluating organizational software security governance, design, implementation, verification, and operations.
2. **OWASP Application Security Verification Standard (ASVS v4.0):** Standardizing functional security controls and level-based technical requirements (Level 1, 2, and 3).
3. **NIST Secure Software Development Framework (SSDF / SP 800-218):** Implementing federal security requirements across organizational preparation, software protection, well-secured software production, and vulnerability response.
4. **Supply-chain Levels for Software Artifacts (SLSA v1.0):** Enforcing cryptographic build provenance, tamper-resistant CI/CD pipelines, and source-to-binary verification.
5. **Software Bill of Materials (SBOM) Standards (CycloneDX / SPDX):** Authoring, signing, and managing machine-readable dependency inventories adhering to CISA minimum elements.
6. **OWASP API Security Top 10 & Web Top 10:** Designing and hardening REST, GraphQL, and gRPC endpoints against broken object-level authorization (BOLA) and logic flaws.



---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-APP` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours distributed across four core domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-APP: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION             |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: Secure Architecture & Threat Modeling       ──► 500 Hours
  ├─► Domain 2: Automated CI/CD Tooling & Pipeline Security ──► 500 Hours
  ├─► Domain 3: Software Supply Chain & SBOM Lifecycle      ──► 500 Hours
  └─► Domain 4: Vulnerability Remediation, Bug Bounty & PSIRT──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: Secure Architecture, Design Review & Component Threat Modeling (500 Hours)
* Executing component-level threat modeling using STRIDE, PASTA, or attack trees on production features, APIs, and microservices before code development.
* Reviewing system architecture diagrams, data flow diagrams (DFDs), and trust boundaries.
* Designing authentication and authorization architectures (OAuth 2.0, OpenID Connect, SAML, RBAC/ABAC policy-as-code).
* Establishing cryptographic engineering standards for data at rest and data in transit (TLS 1.3, envelope encryption, key rotation policies).

### Domain 2: Static, Dynamic & Interactive Security Testing in Automated CI/CD (500 Hours)
* Integrating and tuning Static Application Security Testing (SAST) engines within pull request workflows to minimize false positives.
* Configuring Dynamic Application Security Testing (DAST) and Interactive Application Security Testing (IAST) across staging and ephemeral test environments.
* Implementing automated security policy guardrails and gating criteria in CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, Tekton).
* Authoring custom Semgrep, CodeQL, or regex-based defensive linting rules for proprietary codebases.

### Domain 3: Software Supply Chain Security, Dependency Auditing & SBOM Lifecycle (500 Hours)
* Implementing automated Software Composition Analysis (SCA) to detect known CVEs in third-party and open-source libraries.
* Generating, validating, and cryptographically signing Software Bills of Materials (SBOMs) using CycloneDX and SPDX standards.
* Implementing build artifact provenance verification and attestation under SLSA Framework Level 2 and Level 3 standards.
* Auditing container base images, multi-stage Dockerfiles, and Infrastructure-as-Code (Terraform, Helm, Kubernetes manifests) for misconfigurations and secret leakage.

### Domain 4: Product Vulnerability Remediation, Bug Bounty Triage & Coordinated Disclosure / PSIRT (500 Hours)
* Managing Product Security Incident Response Team (PSIRT) intake, triage, and CVSS v3.1 / v4.0 severity scoring.
* Reproducing complex software vulnerabilities (e.g., SSRF, race conditions, IDOR, deserialization flaws) in sandboxed test environments.
* Collaborating directly with software developers to engineer root-cause code fixes rather than superficial WAF bypass filters.
* Managing external bug bounty programs, coordinated vulnerability disclosure (CVD) timelines, and CVE allocation workflows.


---

## 3. Related Technical Instruction (RTI) Curriculum (288 Hours)

Candidates complete four 72-hour structured classroom and range lab modules:

* **Module APP-101: Threat Modeling & Secure Architecture Design (72 Hours):** STRIDE/PASTA methodologies, data flow diagrams, trust boundaries, OAuth/OIDC protocols, cryptographic engineering, and secure API design.
* **Module APP-102: Automated Pipeline Security & Static Analysis (72 Hours):** SAST/DAST/IAST integration, authoring custom Semgrep and CodeQL rules, CI/CD policy-as-code guardrails, and developer tooling ergonomics.
* **Module APP-103: Software Supply Chain Defense & SBOM Lifecycle (72 Hours):** SLSA framework, reproducible builds, CycloneDX/SPDX generation, container hardening, and dependency vulnerability verification.
* **Module APP-104: Root-Cause Remediation, Bug Bounty & PSIRT Operations (72 Hours):** Flaw reproduction, secure coding patterns in modern languages (Rust, Go, Python, TypeScript), CVSS scoring, and CVD coordination.

---

## 4. Master of Record (MoR) Authority for Application Security

A Master Practitioner holding the `SE-APP` Endorsement possesses statutory sign-off authority for:

1. **Automated CI/CD Pipeline Certifications:** Certifying automated security guardrails and security policy-as-code rules to exempt developer deployments from manual headcount ratios.
2. **SBOM & Supply Chain Attestation:** Digitally signing production SBOMs and SLSA provenance attestations for regulatory filings and third-party risk disclosures.
3. **Product Release Security Stamps:** Inspecting and approving software security verification packages under OWASP ASVS Level 2 or Level 3 baselines.
4. **Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) when software containing critical unmitigated CVEs or structural architectural flaws is ordered into production.

---

## 5. Cross-Crediting & Articulation with Other Endorsements

* **Cross-Crediting to Medical Device Security (`SE-MED`):** Practitioners holding an active `SE-APP` endorsement receive **1,000 hours (50%) credit** toward `SE-MED` for shared technical foundations (threat modeling, secure coding, SBOM lifecycle, and vulnerability triage). They must complete the 1,000-hour clinical bridge in medical device threat modeling, clinical hazard integration, and FDA eSTAR regulatory packaging.
* **Articulation from `SE-MED` to `SE-APP`:** Practitioners holding an active `SE-MED` endorsement receive full articulation credit for `SE-APP`, as medical device engineering encompasses a rigorous superset of software product security controls.

---

## 6. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Medical Device & Clinical Technology Track (`SE-MED`)](medical-devices.md)
* [Velocity, Cloud & Safe Harbor](../velocity-and-cloud.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Licensure Standards & Progression](../licensure-and-progression.md)

