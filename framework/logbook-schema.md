# Universal Logbook Schema & Telemetry Verification Standard

To prevent subjective rubber-stamping, eliminate administrative friction, and ensure verifiable proof of hands-on competence, the trade utilizes a standardized, machine-auditable **Universal Logbook Schema**.

---

## 1. Dual-Layer Verification Architecture

Unlike traditional physical crafts where work is visually inspected on a job site, virtualized cybersecurity operations require a dual-layer verification mechanism combining **objective digital artifacts** with **supervisory cryptographic attestation**.

* **Layer 1: Objective Engineering Artifacts:** The apprentice logs runtime hours linked to verifiable, immutable, or auditable evidence from enterprise workflows, AI/ML pipelines, or approved simulation lab telemetry.
* **Layer 2: Supervisory Attestation:** The supervising Journeyman (or Master Practitioner) audits the log entries, validates runtime execution against the trade rubric, and signs the batch submission using their cryptographic Trade Key.
* **Layer 3: Clearinghouse & Actuarial Feeds:** Verification proofs sync to the Universal Trade Clearinghouse for licensure tracking and provide zero-knowledge compliance attestations to insurance underwriters.

---

## 2. Canonical JSON Logbook Entry Schema

All trade logbook tooling and enterprise tracking interfaces must conform to the following open-standard data schema:

```json
{
  "$schema": "[https://cybertrade.org/schemas/v1/logbook-entry.json](https://cybertrade.org/schemas/v1/logbook-entry.json)",
  "log_id": "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "version": "1.1.0",
  "practitioner": {
    "trade_id": "CTP-APP-2026-0884",
    "name": "Jane Doe",
    "tier": "Tier 2 Apprentice"
  },
  "supervisor": {
    "trade_id": "CTP-JRN-2024-0192",
    "license_status": "Active",
    "supervision_ratio_compliant": true
  },
  "runtime_execution": {
    "date": "2026-08-25",
    "hours_logged": 4.5,
    "core_domain": "D2_DETECTION_SOC",
    "sub_domain": "CI_CD_PIPELINE_HARDENING",
    "environment_type": "Enterprise_Production"
  },
  "competency_milestone": {
    "code": "D2.3.1",
    "description": "Implemented automated SAST gating and signed container image verification in release pipeline."
  },
  "verification_artifacts": [
    {
      "artifact_type": "git_commit_hash",
      "artifact_reference": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "sanitized_summary": "Enforced Cosign signature validation in production deployment workflow."
    },
    {
      "artifact_type": "change_ticket_id",
      "artifact_reference": "CR-894102-SEC",
      "sanitized_summary": "Approved and merged change ticket for CI/CD supply chain controls."
    }
  ],
  "attestation": {
    "supervisor_signature": "MEUCIQDx4F9G...[Ed25519/ECDSA Signature]...",
    "signed_timestamp": "2026-08-25T17:30:00Z",
    "attestation_statement": "I verify that the above runtime hours reflect authentic, supervised operational execution conforming to trade quality rubrics."
  }
}
```

---

## 3. Approved Telemetry & Artifact Verification Types

To support operational defense across traditional infrastructure, cloud control planes, and emerging AI/ML pipelines without violating non-disclosure agreements (NDAs), the schema supports standardized artifact types:

| Artifact Type | Domain Focus | Enterprise Production Evidence | Simulation / Range Evidence |
| :--- | :--- | :--- | :--- |
| `git_commit_hash` | General / Cloud / GRC | SHA of merged security baseline, policy-as-code, or rule commit. | SHA of lab infrastructure-as-code repository. |
| `pipeline_run_hash` | DevSecOps / AppSec | Immutable execution ID of security scanner or build pipeline. | Automated scoring run ID from range platform. |
| `incident_record_id` | SOC / DFIR | Sanitized ticket ID of triaged or remediated security incident. | Range scenario capture-the-flag (CTF) incident run. |
| `change_ticket_id` | Core Operations / IAM | Enterprise Change Advisory Board (CAB) ticket identifier. | Lab exercise milestone sign-off token. |
| `rule_hash` | Threat Detection | Cryptographic hash of authored SIEM, Sigma, or YARA rule. | Evaluated detection artifact in isolated harness. |
| `model_eval_hash` | AI/ML Security (`SE-AIML`) | Cryptographic hash of adversarial evaluation benchmark run or model card security review. | Evaluated red-team run against model harness. |
| `guardrail_policy_hash` | AI/ML Security (`SE-AIML`) | SHA of committed prompt-defense, input-filtering, or model-inversion safeguard configuration. | Lab verification token for LLM/agent defense. |
| `telemetry_export_token` | Data Pipelines (`SE-AIML`) | Hash of signed data sanitization/lineage manifest for fine-tuning pipelines. | Verified data-scrubbing benchmark output. |

---

## 4. Automated Actuarial Feed & Underwriter Attestation API

To operationalize Pillar V and Pillar VII without exposing proprietary corporate data or creating manual audit overhead, the schema supports an automated, zero-knowledge **Actuarial Attestation Feed**:

```json
{
  "$schema": "[https://cybertrade.org/schemas/v1/underwriter-attestation.json](https://cybertrade.org/schemas/v1/underwriter-attestation.json)",
  "attestation_id": "urn:uuid:3c2b1a0e-9f4a-4c28-98e2-0d12e8b9f1a4",
  "reporting_period": {
    "start_date": "2026-01-01",
    "end_date": "2026-06-30"
  },
  "organization_identifier": "anon_org_sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
  "compliance_summary": {
    "active_master_of_record": true,
    "mor_trade_id_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "supervisory_ratio_compliance_score": 0.984,
    "total_verified_ojt_hours": 12480.0,
    "specialty_endorsements_active": ["SE-ICS", "SE-AIML", "SE-CLD"],
    "unresolved_safety_non_concurrences": 0
  },
  "clearinghouse_signature": {
    "issued_by": "National Cybersecurity Trade Board Clearinghouse",
    "signature": "MEQCIG9X...[Clearinghouse Root Key Signature]...",
    "issued_timestamp": "2026-07-01T00:00:00Z"
  }
}
```

* **Zero-Knowledge Privacy:** Underwriters receive verified cryptographic aggregates (ratio compliance rate, active MoR presence, total supervised hours) without seeing employee identities, raw incident logs, or internal network architecture.
* **Continuous Rate Gating:** Sponsoring enterprises connect their trade registry instance to underwriter APIs to maintain real-time qualification for Tier A premium credits (25% to 35% reductions).

---

## 5. Privacy, NDAs, and Data Sanitization Guardrails

Under no circumstances are proprietary corporate logs, raw payload dumps, customer personally identifiable information (PII), or unredacted enterprise vulnerability findings submitted to the public registry.

1. **Local Telemetry Retention:** Detailed proprietary artifact logs remain inside the sponsoring employer's firewalled systems.
2. **Cryptographic Proofs & One-Way Hashes:** The clearinghouse and public registry store only the one-way cryptographic hash of the artifact and the supervisory digital signature.
3. **Auditing Safe Harbor:** In the event of a Trade Board audit or malpractice review, verification occurs on-premises or via zero-knowledge proofs confirming that the artifact hash corresponds to authenticated enterprise activity.

---

## 6. Encrypted Vault Envelope Schema (`.ctp-vault`)

When exported for secure offline backup or encrypted at rest in local IndexedDB storage, the logbook ledger is formatted as an authenticated cryptographic envelope:

```json
{
  "$schema": "https://cybertrade.org/schemas/v1/encrypted-vault.json",
  "format": "AES-256-GCM",
  "kdf": "PBKDF2-SHA256",
  "iterations": 100000,
  "salt": [142, 23, 89, 211, 45, 12, 99, 184, 201, 78, 155, 33, 67, 120, 8, 245],
  "iv": [12, 44, 91, 180, 205, 16, 73, 220, 15, 88, 34, 112],
  "ciphertext": [201, 45, 118, 92, 14, 88, 230, 17, 85, 3, 166, 240, 77, 19, 102, 54],
  "metadata": {
    "schema_version": "1.1.0",
    "encryption_timestamp": "2026-08-30T12:00:00Z",
    "entry_count": 28,
    "merkle_root_hash": "sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"
  }
}
```

---

## 7. Passive Operational Entropy & Anti-Gaming Telemetry Protocol

To prevent metric manipulation and Goodhart's Law distortion without burdening practitioners with intrusive CAPTCHAs or cognitive fatigue:

* **Zero-Interruption Passive Verification:** Telemetry is verified passively and asynchronously through authentic operational entropy (e.g., FIDO2/WebAuthn hardware key touches during shift sign-in, signed Git commit digests, ticket state transitions, and shell command telemetry). Practitioners are never subjected to interactive "prove you are human" popups or cognitive interruptions during live defense.
* **Hardware-Enforced Cryptographic Pulse:** To eliminate LLM-synthesized bot activity and multi-client "ghost-worker" staffing at MSSPs, operational entropy requires physical FIDO2/WebAuthn hardware token presence (User Presence / UP) and User Verification (UV) contextually bound to specific, non-repeatable operational actions (e.g., privileged container executions, firewall ruleset commits, incident containment authorizations). Software emulators and synthetic API scripts cannot simulate physical capacitive hardware touches.
* **Concurrent Active Session Lockout:** A single Board License ID is cryptographically barred from asserting active physical shift presence across overlapping operational rosters or concurrent customer feeds beyond statutory supervisory limits (`framework/supervisory-ratios.md`).
* **Statistical Entropy Auditing:** Actuarial auditing engines perform out-of-band statistical distribution analysis, comparing logbook submission timing and operational entropy against expected human workflow baselines to detect automated bot generation or artificial metric synthesis.
* **Commercial Fraud Classification:** Synthesizing artificial shift telemetry or gaming reachability metrics to illegitimately capture cyber insurance discounts constitutes **Class-A Malpractice and Insurance Fraud**, resulting in immediate license revocation, PEC employer debarment, and referral to state insurance commissioners.
