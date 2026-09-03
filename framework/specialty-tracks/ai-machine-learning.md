# Specialty Track Specification: AI & Machine Learning Security Assurance (`SE-AIML`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-AIML                                          |
| Discipline: AI & Machine Learning Security Assurance                        |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 2 Emerging Technology (+15% to +20% Wage Adder)         |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Artificial Intelligence (AI) and Machine Learning (ML) systems introduce novel vulnerability classes that diverge fundamentally from classical software engineering. Large Language Models (LLMs), predictive models, and autonomous agentic workflows are vulnerable to non-deterministic failure modes, prompt injection, data poisoning, model extraction, training data reconstruction, and supply-chain tampering.

The `SE-AIML` specialty governs the security engineering, threat modeling, red teaming, training pipeline isolation, and model safety verification required to safely deploy artificial intelligence into enterprise and critical infrastructure environments.

### A. Scope & Applicability Invariant
* **In-Scope Workloads (`SE-AIML` Domain):**
  * Enterprise AI products, custom machine learning models, fine-tuned weights, and Retrieval-Augmented Generation (RAG) vector stores.
  * Autonomous agentic workflows with live production execution boundaries, external API tool-calling, or privileged operational capabilities.
  * Adversarial robustness assessments, red teaming against MITRE ATLAS matrices, and formal Model Safety Card certifications (Form FORM-008).
* **Out-of-Scope Productivity Tools (Classical Engineering Governance):**
  * Developer copilots and coding assistants (e.g., GitHub Copilot, Cursor) are classified as developer productivity tooling. They remain governed by standard peer code review, git branch protections, and CI/CD SAST scanners rather than `SE-AIML` staffing requirements.
  * General enterprise SaaS AI interfaces (e.g., commercial web chat tools) are governed under Domain 5 enterprise acceptable use policy and Data Loss Prevention (DLP) controls.
  * Autonomous CI/CD scanners and static analyzers operate under the Section 3 Velocity Exclusions of the Supervisory Ratios standard.

### B. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Software Developer / ML Engineer (`SP-DEV-001`):** Implementing safe inference pipelines, model sandboxing, memory-safe runtime execution, and input token validation.
* **Primary Work Role 2: Threat Warning Analyst / Adversarial ML Specialist (`AN-TWA-001`):** Threat modeling adversarial machine learning attacks, model evasion techniques, and prompt injection vectors.
* **Primary Work Role 3: Security Control Assessor (`SP-SRP-001`):** Evaluating AI model provenance, model card integrity, privacy preservation, and compliance with AI governance frameworks.

### C. Authoritative AI Governance & Machine Learning Security Baselines
1. **NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0 / NIST AI 100-1):** Governing AI system trustworthiness, validity, safety, security, and resilience.
2. **OWASP Top 10 for Large Language Model Applications (LLM Top 10):** Mitigating prompt injection, insecure output handling, training data poisoning, and model denial of service.
3. **MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems):** Structuring adversarial ML tactics, techniques, and case studies.
4. **ISO/IEC 42001 & ISO/IEC 23894:** Artificial intelligence management system requirements and risk management guidelines.
5. **CISA/NCSC Guidelines for Secure AI System Development:** Covering secure design, secure development, secure deployment, and secure operation of AI systems.


---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-AIML` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the line-of-sight supervision of an active `SE-AIML` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-AIML: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION            |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: AI/ML Threat Modeling & ATLAS Surface Mapping   ──► 500 Hours
  ├─► Domain 2: Adversarial Robustness & Prompt Injection Defense ──► 500 Hours
  ├─► Domain 3: ML Pipeline Security, Model Provenance & Weights ──► 500 Hours
  └─► Domain 4: Model Privacy, Inversion Defense & Guardrails   ──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: AI/ML Threat Modeling & ATLAS Surface Mapping (500 Hours)
* Mapping complete AI architectural flows: training data ingest, feature extraction, embedding databases, foundation model inference, and Retrieval-Augmented Generation (RAG) vector stores.
* Conducting adversarial threat assessments using the MITRE ATLAS matrix to identify evasion, inversion, extraction, and poisoning attack vectors.
* Authoring AI Model Risk Assessments and documentation aligning with NIST AI RMF governance profiles.

### Domain 2: Adversarial Robustness & Prompt Injection Defense (500 Hours)
* Engineering deterministic input validation, semantic firewalls, and dual-LLM verification architectures to defend against direct and indirect prompt injection.
* Conducting automated and manual red teaming against LLMs and multi-modal models to test resistance to jailbreaks, system prompt extraction, and automated agent tool abuse.
* Implementing strict boundary enforcement and least privilege over autonomous AI agent tool calling and API executions.

### Domain 3: ML Pipeline Security, Model Provenance & Weights Integrity (500 Hours)
* Securing MLOps and CI/CD pipelines against training dataset tampering, malicious package dependencies, and backdoor trigger insertions.
* Enforcing cryptographic model signing and provenance verification for foundation model weights and serialized checkpoints (Safetensors, GGUF, ONNX).
* Implementing isolation, memory bounds, and sandboxed runtimes for custom model inference engines.

### Domain 4: Model Privacy, Inversion Defense & Guardrails (500 Hours)
* Deploying differential privacy techniques, membership inference defenses, and training data anonymization pipelines to prevent training data reconstruction.
* Implementing output guardrails to prevent unauthorized disclosure of personally identifiable information (PII), proprietary source code, or toxic content.
* Integrating real-time telemetry and anomaly detection for model drift, concept shift, and adversarial query clustering.

---

## 3. Master of Record (MoR) Authority for AI Security Assurance

A Master Practitioner serving in an active Master of Record (MoR) assignment possesses statutory sign-off authority for enterprise AI deployments. Practitioners who additionally hold the `SE-AIML` Endorsement hold verified domain expertise and qualify for specialized Tier 2 wage adders (+15% to +20%).

Sign-off and refusal authorities include:

1. **Enterprise AI Model Deployment Certification:** Formally certifying that an AI/ML model, RAG pipeline, or autonomous agent workflow meets NIST AI RMF standards prior to production enterprise exposure using [Form FORM-008: Autonomous AI System Deployment & Tool Execution Clearance](../../templates/FORM-008_ai-agent-safety-clearance.md).
2. **AI Model Safety Card Stamping:** Signing off on Model Cards, data provenance records, and algorithmic risk assessments for statutory filings and insurer review.
3. **Agentic Tool Execution Authorization:** Authorizing live production API integration and tool-calling capabilities for autonomous AI agents under bounded least-privilege policies. When an enterprise MoR does not personally hold the `SE-AIML` endorsement, clearance may be executed following verified technical review by an accredited AI security specialist.
4. **Notice of Safety Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) if non-deterministic autonomous AI systems are connected directly to life-safety, financial execution, or critical infrastructure systems without human-in-the-loop safeguards.

---

## 4. Strict Cross-Crediting & Articulation Boundaries

* **Cross-Crediting from Application Security (`SE-APP`):** Up to **500 hours credit** toward Domain 3 (ML Pipeline Security & Provenance) for verified software supply chain and CI/CD pipeline experience.
* **Cross-Crediting from Offensive Security (`SE-OFF`):** Up to **500 hours credit** toward Domain 2 (Prompt Injection & Jailbreak Testing) for verified red team and exploitation experience.
* **Zero Cross-Crediting from Classical Data Science:** Routine exploratory data analysis, business intelligence querying, or generic statistics does not satisfy specialized AI cybersecurity runtime.

---

## 5. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
