# Specialty Track Specification: Cloud Security & Infrastructure (`SE-CLD`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-CLD                                           |
| Discipline: Cloud Security & Infrastructure Architecture                     |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 2 Architectural Complexity (+10% to +15% Wage Adder)   |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Open Standards & NIST NICE Mapping

Modern enterprise compute is predominantly cloud-native, distributed across multi-tenant infrastructure, software-defined networks, and managed orchestration platforms (AWS, Microsoft Azure, Google Cloud Platform, Kubernetes). The Cloud Security & Infrastructure specialty (`SE-CLD`) governs the engineering, automated policy enforcement, identity boundary design, and workload protection mechanisms required to secure cloud environments.

This specialty covers the entire cloud architecture lifecycle: Infrastructure-as-Code (IaC) guardrails, container and Kubernetes cluster security, Cloud Security Posture Management (CSPM), Cloud Workload Protection (CWPP), and Cloud Infrastructure Entitlement Management (CIEM).

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: Enterprise Architect (`SP-ARC-001`):** Designing multi-cloud landing zones, shared responsibility boundaries, and zero trust network perimeters.
* **Primary Work Role 2: Systems Administrator (`PR-INF-001`):** Hardening container runtimes, Kubernetes API servers, microsegmentation policies, and cloud storage buckets.
* **Primary Work Role 3: Network Operations Specialist (`OM-NET-001`):** Engineering virtual private clouds (VPCs), transit gateways, egress proxy architectures, and software-defined boundary isolation.

### B. Authoritative Cloud Security Baselines & Architectures
1. **Cloud Security Alliance Cloud Controls Matrix (CSA CCM v4):** Assessing cloud governance, facility security, identity, and infrastructure resilience.
2. **CIS Cloud Benchmarks (AWS, Azure, GCP, Kubernetes):** Standardizing level-based hardening configurations for cloud control planes and managed services.
3. **NIST SP 800-145 & SP 800-210:** Definitive cloud computing architectural characteristics and access control guidance for cloud services.
4. **FedRAMP Continuous Monitoring Strategy & Rev 5 Baselines:** Enforcing automated compliance telemetry, vulnerability scanning, and configuration baselining.
5. **Open Policy Agent (OPA) / Rego / CloudFormation Guard:** Standardizing policy-as-code guardrails across CI/CD and deployment pipelines.


---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-CLD` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the line-of-sight supervision of an active `SE-CLD` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-CLD: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION             |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: Multi-Cloud Identity, IAM Federation & CIEM    ──► 500 Hours
  ├─► Domain 2: Container, Kubernetes & Microservice Security  ──► 500 Hours
  ├─► Domain 3: Infrastructure-as-Code (IaC) & Policy-as-Code  ──► 500 Hours
  └─► Domain 4: Cloud Workload Protection (CWPP/CSPM) & Egress ──► 500 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: Multi-Cloud Identity, IAM Federation & CIEM (500 Hours)
* Designing least-privilege IAM policies, role-based and attribute-based access controls (RBAC/ABAC), and cross-account trust relationships.
* Deploying Cloud Infrastructure Entitlement Management (CIEM) tools to detect privilege drift, unused permissions, and toxic credential combinations.
* Engineering secure service-to-service authentication via OIDC federation, workload identity pools, and ephemeral token vending machines.

### Domain 2: Container, Kubernetes & Microservice Security (500 Hours)
* Hardening Kubernetes control planes, worker nodes, kubelet configurations, and etcd data stores adhering to CIS Kubernetes Benchmarks.
* Authoring and enforcing Kubernetes Network Policies, Pod Security Standards (PSS), and admission controllers (Kyverno, OPA Gatekeeper).
* Engineering minimal, distroless base container images with cryptographic signature verification (Cosign/Sigstore).

### Domain 3: Infrastructure-as-Code (IaC) & Policy-as-Code (500 Hours)
* Writing secure Terraform, OpenTofu, CloudFormation, and Bicep modules embedded with deterministic security parameters.
* Integrating static IaC scanners (Checkov, tfsec, Trivy) into CI/CD pipelines to block misconfigured storage buckets, unencrypted databases, and open security groups.
* Implementing automated drift detection and self-healing remediation pipelines.

### Domain 4: Cloud Workload Protection (CWPP/CSPM) & Egress (500 Hours)
* Deploying Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platforms (CWPP) across multi-account organizations.
* Engineering centralized cloud egress filtering, TLS inspection proxies, VPC peering architectures, and PrivateLink connections.
* Designing cloud logging pipelines (CloudTrail, VPC Flow Logs, Azure Event Hubs) with immutable storage and tamper-evident write-once-read-many (WORM) controls.

---

## 3. Master of Record (MoR) Authority for Cloud Security

A Master Practitioner holding the `SE-CLD` Endorsement possesses statutory sign-off authority for:

1. **Cloud Landing Zone Architecture Certification:** Formally certifying that enterprise multi-account landing zones, network perimeters, and IAM baselines meet statutory regulatory and insurance requirements.
2. **IaC Policy-as-Code Deployment Approval:** Authorizing the production promotion of automated security guardrails and pre-approved deployment pipelines.
3. **Emergency Cloud Isolation Stamping:** Authorizing emergency network isolation, VPC quarantine routing, and credential revocation during active cloud tenant compromise.
4. **Notice of Safety Non-Concurrence Standing:** Authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) if cloud workloads containing high-impact critical assets are deployed into unprotected public networks without baseline security controls.

---

## 4. Strict Cross-Crediting & Articulation Boundaries

* **Cross-Crediting from Application Security (`SE-APP`):** Practitioners holding an active `SE-APP` endorsement receive up to **500 hours credit** toward Domain 3 (IaC & Policy-as-Code) based on verified automated CI/CD pipeline experience.
* **Cross-Crediting from Identity Management (`SE-ICAM`):** Practitioners holding an active `SE-ICAM` endorsement receive up to **500 hours credit** toward Domain 1 (Cloud IAM Federation).
* **Zero Cross-Crediting from Commercial IT Helpdesk:** General IT infrastructure or basic sysadmin ticketing does not count toward specialized cloud security hours.

---

## 5. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Velocity, Cloud & Safe Harbor](../velocity-and-cloud.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
