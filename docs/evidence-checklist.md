# SOX ITGC — CSW Evidence Checklist

A printable worklist for the evidence owner. For each item: **what** to export, **where** from in CSW, and the **cadence**. Tick as you collect; file exports to immutable storage with an IPE cover record — not screenshots taken during fieldwork week.

> Legend — 🟢 Direct · 🟠 Supporting · ⚪ Evidence Required *(supplied outside CSW)*. CSW evidence is an input to ITGC assurance, not an attestation.

> **Read the boundary first.** Everything below is evidence about the **network-access control** and the **monitoring** around in-scope systems. None of it is evidence about user entitlements, segregation of duties inside the financial application, change authorisation, or the financial records themselves. Those come from IAM, PAM, the application, and ITSM.

> **Cadence is driven by §302.** Quarterly certification means a quarterly pack, with monthly items rolled up into it.

---

## Phase 1 — Coverage (Days 1–10)

- [ ] 🟢 In-scope host list reconciled to **CSW Inventory** against the SOX scoping memo
- [ ] 🟢 Labels applied with the audit boundary first: `sox_scope:in-scope | boundary | out-of-scope`, then `sox_cycle:*`, `financial_app:*`, `fiscal_relevance:*`, `itgc_domain:*`, `app_owner:*`, `env:*`
- [ ] 🟢 CSW scope tree created, including the deliberate `Non-SOX-Adjacent` sibling
- [ ] 🟢 Supporting infrastructure mapped per in-scope application: database, middleware, job scheduler, managed file transfer, identity dependency
- [ ] 🟢 **Cannot-instrument register** recorded (vendor appliances, legacy platforms, network devices)
- [ ] 🟢 Agentless workloads flagged, with a note that **process-level visibility comes from the agent**
- [ ] 🟢 Scoping differences routed to the SOX PMO: hosts missing from the memo, hosts in the memo that no longer exist, and genuine coverage gaps
- [ ] 🟢 Coverage gaps logged in the **deficiency tracker**, not just an IT backlog
- [ ] **Export:** inventory CSV + agent-status view → `evidence/01-coverage/`

## Phase 2 — Baseline (Days 11–45)

- [ ] 🟢 ADM running on the SOX scope across **at least one full month-end close** — ideally a quarter-end
- [ ] 🟢 Batch, interface, and file-transfer flows captured and attributed to a business cycle
- [ ] 🟢 Year-end-only processes identified and documented as known exceptions with named owners
- [ ] 🟢 **Undeclared interfaces** documented and raised to the SOX PMO as scoping questions — a reporting tool pulling straight from the general ledger may widen the boundary
- [ ] 🟢 Application and process owners signed the cluster-to-application mapping
- [ ] 🟠 Vulnerability and reachability snapshot taken for in-scope hosts
- [ ] **Export:** ADM diagram + flow samples with process context → `evidence/02-baseline/`

## Phase 3 — Policy (Days 46–70)

- [ ] 🟢 Default-deny posture defined for `Financial-Reporting-Core`
- [ ] 🟢 `Non-SOX-Adjacent` → `Financial-Reporting-Core` deny authored — the boundary policy
- [ ] 🟢 Production / non-production deny authored
- [ ] 🟢 Admin ports source-locked to approved jump hosts
- [ ] 🟢 ADM-imported allow rules refined with application owners
- [ ] 🟢 **Simulation run across a close window** — not a quiet mid-month fortnight
- [ ] 🟢 Change tickets raised for every false-positive fix; exception register updated
- [ ] 🟢 Enforcement scheduled **outside a close window**, with the rationale documented
- [ ] **Export:** policy export + simulation report, linked to change record IDs → `evidence/03-policy/`

## Phase 4 — Operate (ongoing)

- [ ] 🟢 Enforcement enabled; **negative test recorded in Denied Connections**
- [ ] 🟢 Controlled rollback test performed once and recorded
- [ ] 🟢 Quarterly evidence pack assembled (table below)
- [ ] 🟢 IPE cover record and hash manifest applied to every retained export
- [ ] 🟢 SIEM integration verified with sample events
- [ ] 🟢 ADM re-baselined every 90 days
- [ ] **Export:** enforcement screenshot + quarterly binder → `evidence/04-operate/`

---

## The quarterly pack

| # | Evidence item | CSW source | Cadence | Domain |
|---|---|---|---|---|
| 1 | Enforced segmentation policy export | Defend → Segmentation | Each release + quarterly | 🟢 APD |
| 2 | **Denied Connections for the full period** | Investigate → Flows / Denied | Quarterly | 🟢 APD — operating effectiveness |
| 3 | Boundary proof: out-of-scope → in-scope denies | Flow Search, scope-filtered | Quarterly | 🟢 APD |
| 4 | Production / non-production deny evidence | Flow Search, scope-filtered | Quarterly | 🟢 APD |
| 5 | Admin-path rules + observed admin flows | Defend → Segmentation; Flow Search | Quarterly | 🟢 APD |
| 6 | Inventory reconciled to the scoping memo + exception list | Investigate → Inventory | Quarterly | 🟢 APD |
| 7 | Simulation report and enforcement approval | Policy lifecycle records | Per cutover | 🟢 PC |
| 8 | Policy version history with checksums | Policy export + manifest | Quarterly | 🟢 PC |
| 9 | Policy change audit log — who changed what, when | Administration → Audit Log | Quarterly | 🟢 PC — SoD over the control |
| 10 | Inventory delta, weekly, summarised | Investigate → Inventory | Weekly → quarterly roll-up | 🟠 PC |
| 11 | **Deltas with no matching change ticket** | Inventory diff + ITSM reconciliation | Monthly | 🟠 PC |
| 12 | ADM baseline snapshot spanning a close | Investigate → ADM | 90 days | 🟢 CO + APD |
| 13 | Batch and interface flow evidence | Flow Search on scheduling tiers | Quarterly | 🟢 CO |
| 14 | Alert history | Alerts / SIEM forward | Quarterly | 🟢 CO |
| 15 | Agent coverage and availability report | Manage → Agents | Monthly | 🟢 CO |
| 16 | Incident flow and process timeline | Investigate → Flow / Process Search | Per incident | 🟢 CO |
| 17 | Vulnerability + reachability summary | Investigate → Vulnerability | Monthly | 🟠 risk input |

---

## IPE cover record — apply to every retained export

Once a CSW export is used as audit evidence it becomes **Information Produced by the Entity**, and the auditor must satisfy themselves it is complete and accurate. An undated CSV with no record of who produced it, from which scope, over what period, is weak evidence regardless of how good the underlying control is.

- [ ] **Who** ran it, and under which CSW role
- [ ] **When** it was produced, with timezone
- [ ] **Parameters** — scope, label filter, and the exact time range
- [ ] **Source** — CSW cluster identifier and software version
- [ ] **Integrity** — a hash of the file, recorded separately from the file

```
Produced by   : <operator>
Produced at   : <ISO-8601 with timezone>
CSW cluster   : <cluster-identifier>
CSW version   : <version>
Scope         : SOX-Relevant
Label filter  : sox_scope=in-scope
Period covered: <start> to <end>
Purpose       : SOX ITGC evidence, APD and PC domains
```

Store the hash manifest separately from the exports. See [§11.2 of the Reference Design](../CSW-SOX-Reference-Design.md) for a worked script.

---

## ⚪ Evidence Required — supplied outside CSW

Do not leave these blank in the control narrative. Name the owning control and tool, so a tester sees a boundary rather than a gap.

- [ ] ⚪ User access review and entitlement recertification — IAM / PAM / application
- [ ] ⚪ Authentication and MFA — identity provider
- [ ] ⚪ Privileged access management and session recording — PAM
- [ ] ⚪ Segregation of duties inside the financial application — the application
- [ ] ⚪ Application-layer authorisation — the application
- [ ] ⚪ Change authorisation and approval workflow — ITSM
- [ ] ⚪ Program development and SDLC controls — engineering / PMO
- [ ] ⚪ Backup, recovery, and job-failure handling — IT operations
- [ ] ⚪ Management review controls — finance
- [ ] ⚪ Entity-level COSO controls — SOX PMO

---

## Deficiency candidates to self-report

Surfacing these yourself with a remediation plan is a materially better position than having them found in fieldwork.

- [ ] Agent offline on an in-scope host for part of the period — **a period-evidence gap**, not just an operational issue. Log the outage window, affected hosts, and any compensating evidence
- [ ] In-scope host with no agent and no agentless coverage
- [ ] Undeclared interface into or out of a financially-relevant system
- [ ] Inventory delta with no corresponding change ticket
- [ ] Untagged asset communicating with the financial reporting core
- [ ] Policy modified outside the agreed change process
