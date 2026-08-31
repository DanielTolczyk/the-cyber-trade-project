# Form FORM-005: Targeted OSS Security Fork Exemption & Compensating Control Attestation

**Exemption Identifier:** `OSS-EX-[YYYYMMDD]-[SYSTEM_CODE]`  
**Master of Record (MoR) License ID:** `[LICENSE_ID]`  
**Enterprise / Regulated Entity:** `[ENTITY_NAME]`  
**Filing Date & Timestamp (UTC):** `[ISO_8601_TIMESTAMP]`  
**Exemption Expiration Date (Max 90 Days):** `[YYYY-MM-DD]`  
**Upstream Vulnerability (CVE ID):** `[e.g., CVE-2026-XXXXX / GHSA-XXXX-XXXX]`  

---

## 1. Vulnerable Open-Source Dependency Identification
* **Package Name & Upstream Ecosystem:** `[e.g., org.apache.logging.log4j:log4j-core / npm:express-parser]`
* **Upstream Version Affected:** `[e.g., v2.14.1]`
* **Upstream Maintainer Status:** Unpatched / No Active Response (>72 Hours) / Community Patch Under Review
* **Vulnerable Artifact Digest (SHA-256):** `[UPSTREAM_PACKAGE_SHA256]`

---

## 2. Internal Security Fork & Isolation Parameters
* **Internal Fork Repository / Artifact Digest:** `[INTERNAL_GIT_COMMIT_SHA / PACKAGE_REGISTRY_DIGEST]`
* **Scope of Internal Modifications:**
  * [ ] Vulnerable Code Path Disabled / Stripped
  * [ ] Memory-Safety / Boundary Checks Injected
  * [ ] Custom Mitigation Patch Backported from Upstream Draft PR
* **Automated Regression & Integrity Verification Hash:** `[TEST_SUITE_RUN_HASH]`

---

## 3. Verified Runtime Compensating Controls
Detail the active defense controls neutralizing exploit vectors in production environments:

* **Control 1 (Network / Perimeter):** `[e.g., WAF virtual patch rule blocking specific payload pattern: WAF-RULE-8841]`
* **Control 2 (Workload / Segmentation):** `[e.g., Egress micro-segmentation preventing outbound LDAP/DNS callbacks]`
* **Control 3 (Host / Container):** `[e.g., Seccomp/AppArmor profile restricting execution of unauthorized system calls]`

---

## 4. Master of Record Attestation & Grace Period Execution

By signing below, the designated Master of Record certifies that:
1. The upstream open-source vulnerability has been analyzed and isolated.
2. The internal security fork and active runtime compensating controls effectively neutralize the identified exploit vector without degrading system baseline security.
3. This temporary exemption re-certifies the automated CI/CD deployment pipeline for the specified internal artifact digest for a duration of **90 calendar days**.
4. Sponsoring enterprise insurance safe harbor and preferred warranty discount status remain active during this grace period.

* **Master of Record Signature:** `___________________________`
* **Cryptographic Attestation Hash (SHA-256):** `[GENERATED_HASH]`
