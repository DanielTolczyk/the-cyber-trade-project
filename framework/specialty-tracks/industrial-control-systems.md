# Specialty Track Specification: Industrial Control Systems & Operational Technology Security (`SE-ICS`)

```
+─────────────────────────────────────────────────────────────────────────────+
| ENDORSEMENT SPECIFICATION: SE-ICS                                           |
| Discipline: Industrial Control Systems & Operational Technology Security    |
| Target Tier: Post-Journeyman Specialty Endorsement (2,000 OJT Hours)        |
| Classification: Tier 2 Statutory & Life-Safety (+20% to +25% Wage Adder)    |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 1. Scope, Regulatory Baselines & NIST NICE Mapping

Industrial Control Systems (ICS), Supervisory Control and Data Acquisition (SCADA), and Operational Technology (OT) govern physical kinetic processes across critical infrastructure, including power generation and distribution, water treatment, chemical refining, manufacturing, and transportation networks. In these environments, cybersecurity failures directly jeopardize human life, public safety, physical equipment integrity, and environmental stability.

The `SE-ICS` specialty covers security engineering across all levels of the Purdue Enterprise Reference Architecture (PERA / IEC 62264), spanning Level 0 physical sensors and actuators, Level 1 programmable logic controllers (PLCs) and remote terminal units (RTUs), Level 2 distributed control system (DCS) human-machine interfaces (HMIs), Level 3 site manufacturing operations, and the critical Level 3.5 Industrial Demilitarized Zone (IDMZ).

### A. Mandatory NIST NICE Framework Alignment (NIST SP 800-181)
Practitioners in this track demonstrate verified competencies mapped directly to federal work roles:
* **Primary Work Role 1: System Security Architecture (`SP-ARC-002`):** Designing zone and conduit boundaries, air-gap architectures, and demilitarized ingress/egress points adhering to ISA/IEC 62443.
* **Primary Work Role 2: Security Control Assessor / OT Safety Assessor (`SP-SRP-001`):** Conducting factory acceptance testing (FAT), site acceptance testing (SAT), safety integrity level (SIL) cyber reviews, and physical process risk assessments.
* **Primary Work Role 3: Network Operations Specialist (`OM-NET-001`):** Inspecting and securing deterministic fieldbus and industrial Ethernet communications (Modbus, DNP3, CIP, OPC UA, PROFINET, IEC 61850).

### B. Authoritative Industrial & Critical Infrastructure Standards
1. **ISA/IEC 62443 Series:**
   - *Part 2-1 & 2-4:* Security program requirements for IACS asset owners and service providers.
   - *Part 3-2:* Security risk assessment, system partitioning, zones, and conduits.
   - *Part 3-3:* System security requirements and security levels (SL-1 through SL-4).
   - *Part 4-2:* Technical security requirements for IACS components and embedded field devices.
2. **NIST SP 800-82r3:** Guide to Operational Technology (OT) Security, enforcing availability and physical safety prioritization over classical IT confidentiality.
3. **NERC CIP Reliability Standards:** CIP-002 through CIP-014 compliance for Bulk Electric System (BES) cyber assets, electronic security perimeters (ESP), and physical security perimeters (PSP).
4. **Safety Instrumented Systems (SIS) Standards (IEC 61508 / IEC 61511):** Strict cyber isolation of safety shutdown logic and emergency trip systems from process control networks.
5. **CISA Cross-Sector Cybersecurity Performance Goals (CPGs):** Enforcing essential OT baseline practices (mitigating default credentials, single-point OT-IT connections, and unauthenticated industrial protocols).

---

## 2. The 2,000-Hour Specialized OJT Runtime Breakdown

To earn the `SE-ICS` Endorsement, a Licensed Journeyman must complete 2,000 verified post-licensure on-the-job operational hours under the direct line-of-sight supervision of an active `SE-ICS` Master Practitioner across four specialized domains:

```
+─────────────────────────────────────────────────────────────────────────────+
|               SE-ICS: 2,000-HOUR SPECIALTY RUNTIME DISTRIBUTION             |
+─────────────────────────────────────────────────────────────────────────────+
  ├─► Domain 1: Purdue Segmentation, Zone & Conduit Engineering ──► 600 Hours
  ├─► Domain 2: Industrial Protocols & Boundary Hardening       ──► 500 Hours
  ├─► Domain 3: SIS, Physical Process & Fail-Safe Engineering   ──► 500 Hours
  └─► Domain 4: Plant Outage Operations, Commissioning & FAT/SAT ──► 400 Hours
+─────────────────────────────────────────────────────────────────────────────+
```

### Domain 1: Purdue Segmentation, Zone & Conduit Engineering (600 Hours)
* Engineering physical and logical boundaries between Level 4/5 Enterprise IT and Level 0-3 Industrial Control networks via multi-homed Level 3.5 IDMZs.
* Implementing unidirectional security gateways (data diodes) for plant telemetry export to enterprise historians without reverse network routability.
* Conducting detailed asset discovery, hardware inventorying, and firmware baseline auditing across legacy unmanaged OT assets.
* Designing Jump Host architectures, Multi-Factor Authentication (MFA) enforcement points for remote vendor access, and micro-segmentation within Level 2/3 cells.


### Domain 2: Industrial Protocols & Boundary Hardening (500 Hours)
* Inspecting, baselining, and parsing industrial Ethernet and fieldbus protocols (Modbus TCP/RTU, DNP3, EtherNet/IP / CIP, OPC UA, PROFINET, BACnet, IEC 60870-5-104).
* Deploying passive OT network monitoring tools and deep packet inspection (DPI) engines to detect unauthorized write commands, ladder logic downloads, and baseline deviations without active scanning disruption.
* Hardening engineering workstations (EWS), human-machine interfaces (HMIs), and data historians through application allowlisting, USB device locking, and port disabling.

### Domain 3: Safety Instrumented Systems (SIS), Physical Process & Fail-Safe Engineering (500 Hours)
* Enforcing absolute architectural separation between Basic Process Control Systems (BPCS) and Safety Instrumented Systems (SIS / IEC 61511).
* Analyzing physical failure modes, overpressure limits, thermal runaway thresholds, and mechanical interlocks to ensure cyber events cannot override hardware safety valves.
* Auditing PLC/RTU ladder logic, control loops, and configuration files for unauthorized logic tampering or out-of-bounds setpoints.
* Engineering secure out-of-band manual overrides and physical emergency stop mechanisms.

### Domain 4: Plant Outage Operations, Commissioning & FAT/SAT (400 Hours)
* Executing Factory Acceptance Testing (FAT) and Site Acceptance Testing (SAT) cybersecurity verification checklists for new control skids and vendor packages.
* Managing live plant turnaround and maintenance window cyber operations, including firmware flashing, secure backup restoration verification, and configuration drift auditing.
* Authoring site-specific OT Incident Response and Disaster Recovery plans, including manual island-mode plant operation runbooks.

---

## 3. Strict Operational Ratios & On-Shift Safety Controls

Due to severe kinetic and life-safety risks, operational ratios for `SE-ICS` are strictly enforced:

* **Routine Plant Operations & Engineering:** Standard **2:1 on-shift ratio** (maximum 2 apprentices per licensed Journeyman or Master).
* **Live Plant Turnarounds, Outage Windows & Active Generation Maintenance:** Mandatory **1:1 line-of-sight ratio**. An apprentice or candidate may not execute firmware updates, ladder logic modifications, or IDMZ firewall changes without dedicated one-to-one supervision.
* **Safety Instrumented System (SIS) Operations:** Modifications to SIS logic, safety loops, or emergency trip systems require direct execution by an `SE-ICS` Master of Record.

---

## 4. Master of Record (MoR) Authority for Industrial Control Systems

A Master Practitioner holding the `SE-ICS` Endorsement possesses statutory sign-off authority for:

1. **Plant Cyber-Safety Commissioning Stamp:** Formally certifying that new industrial facilities, control skids, or plant expansions conform to ISA/IEC 62443 zone/conduit requirements prior to live process energization.
2. **IDMZ Conduit & Remote Access Certification:** Approving all remote vendor access pathways, unidirectional data flows, and inter-network conduits crossing the Level 3.5 IDMZ boundary.
3. **Outage Maintenance Safe-Harbor Clearance:** Authorizing post-maintenance control system return-to-service following major plant overhauls or emergency cyber restorations.
4. **Statutory Non-Concurrence Standing:** Absolute authority to issue a formal [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md) halting live plant operations if safety shutdown systems are compromised, unsegmented, or bypassed.

---

## 5. Strict Cross-Crediting & Articulation Boundaries

Industrial control cybersecurity requires physical process comprehension and environmental safety tradecraft. The Trade Board enforces strict boundaries:

* **Zero Cross-Crediting from Commercial IT Tracks:** Commercial web application security (`SE-APP`), enterprise cloud administration, and standard IT security provide **0 hours of cross-credit** toward `SE-ICS`.
* **Zero Cross-Crediting with Digital Forensics (`SE-DFIR`):** Forensic evidence handling and incident response do not cross-credit toward plant control systems.
* **Recognized Trade Articulation:** Licensed Industrial Electricians, Instrumentation Technicians, or Navy Nuclear Propulsion Operators entering the trade receive up to **500 hours credit** toward Domain 1/2 upon Board review of certified technical runtime.

---

## 6. Related Specifications & Architecture
* [Specialty Endorsements & Domain Architecture](../specialty-endorsements.md)
* [Supervisory Ratios & On-Shift Capacity](../supervisory-ratios.md)
* [Technical Refusal & Whistleblower Defense](../technical-refusal-and-liability.md)
* [Standards, Regulatory Baselines & Compliance](../standards-and-compliance.md)
* [Notice of Safety Non-Concurrence (Form FORM-001)](../../templates/FORM-001_notice-of-safety-non-concurrence.md)
