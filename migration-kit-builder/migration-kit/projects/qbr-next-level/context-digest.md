# Context digest — QBR Next Level

## Purpose

Strategic redesign of HT's quarterly business review (QBR) — the
operating-plan steering process across all ~25–32 EMM members. The work
runs in two horizons: (a) **near-term**, fixing what's broken in the
current model before the next QBR cycle; (b) **medium-term**, designing
the OKR-driven 2027 plan as a proof-of-concept for the redesigned
process. The custom instructions cast Claude as a Big-5 strategic
advisor familiar with the **TRAIIN** method (used for inspiration, not
forced).

## What the diagnostic exposed

Two conversations have produced a written diagnosis of the current
operating plan (`OP_2026_Q1_v2`, ~159 initiatives across ~32 EMMs,
~€26.7M Capex + €11M IDC, 5 objectives / 18 KRs):

- **Lopsided objective coverage.** O3 Growth 35%, O1/O4 Customer/
  Transformation 25% each, O5 Reputation 10%, **O2 People 3% (only 4
  initiatives).** Either People is undercounted or massively under-
  resourced for what it's expected to deliver.
- **Granularity is broken.** 78% of initiatives carry no euro at all;
  the top 5 hold >70% of the budget. 28% are micro-initiatives
  (≤1 score), 4% are mega-initiatives spanning 8–10 KRs whose KPIs
  are vague ("concept definition", "complete scope by Q1").
- **Programme layer missing.** Digital Telco appears in 9 initiatives
  across 6 EMMs with no programme owner. Same fragmentation pattern
  for B2Digital, Sprinklr, AIMO, and Pluto & AI.
- **Execution concentration risk.** Ivan Runje owns 21 initiatives
  (13% of the portfolio); only 11 are healthy. 6 of 8 portfolio-wide
  "postponed" status flags are his.
- **Reporting non-compliance.** 24% of initiatives unreported in Q1;
  20 of those 38 blanks are from two EMMs (Tihomir Kapular, Iva
  Cibulić).
- **Funding data unreliable.** 45% of Capex and 64% of IDC fields are
  blank. €2.70M of €2.85M unsecured Capex sits in a single line:
  Ivan Visković's *Network Resilience ph3*.
- **IT-delivery dependency is the biggest hidden risk.** 65 initiatives
  need agile/IT roadmap support; only 39 are confirmed prioritized for
  2026. ~40% of IT-dependent work has no confirmed slot. This is the
  exact gap the Tribe↔IT joint governance with Fred is meant to close.
- **Steering is backward-looking.** Forward-decisions field is 1%
  populated. Q1 KPI achievement only 53% populated even after the
  quarter closed. Multiple abandoned tracking attempts in the file.

## Decisions taken / direction set

- **Move the QBR from "report mode" to "decision mode"** — track what
  was delivered, headline successes/failures, drivers/KPIs, market
  context, decisions/budget/resources requested next quarter.
- **Manage OKRs, not initiatives.** Lock OKRs by Q1 to enable Capex/IPF
  alignment. 2027 OKR design is the PoC for the new model.
- **Add a programme layer above initiatives** with named accountable
  owners. The NatCo Visit deck already implicitly defines ~10
  programmes (Digital Telco, FTTH monetisation, Cyber/Combis, AIMO,
  B2Digital, Pluto & AI, Operating Model 2030, Bill of Rights, etc.) —
  surface them as the missing structure.
- **S/M/L initiative classification + separation of initiatives /
  enablers / BaU.**
- **Workshop scheduled with Vavro in May for 2027 OKRs.** Tiho is
  drafting the new way-of-work.

## Important artifacts

- **HTML diagnostic document** generated in conversation 1 (Fraunces
  serif + IBM Plex Sans, HT-magenta accents, ~3500 words). Structured
  as: portfolio shape → 5 structural problems → 3 problems with the
  steering meeting → 5 proposals → 4-week adoption path. **Highest-
  leverage proposal is #2 — programme layer above initiatives.**
- The **NatCo Visit Croatia – April 2026** deck (62 slides) — the
  external narrative HT is presenting to Bonn. Already structured
  programmatically; the OP needs to mirror it.
- The Q1 review presentation with **yellow-highlighted speaker notes
  on slides 3, 5, 6, 7** — the team's emerging thesis on what to
  change. These notes plus the diagnostic are the basis for the redesign.
- `knowledge/operating_plan_review.html` — the static template the
  project carries.

## Open threads

1. Is the QBR meeting a decision forum or a status update for MB?
   Decision drives meeting design, template, and output artefacts.
2. Are the proposed changes (programme layer, S/M/L, OKR-driven
   reporting) politically agreed yet, or still in proposal stage?
3. NatCo / DT-mandated reporting constraints — what is fixed vs
   negotiable?
4. Network Resilience ph3 €2.7M unsecured Capex needs a Board call.
5. AI & Data Tribe authorship in the next OP iteration: insist that
   any initiative depending on Pluto / AI Agents / Orchestrator carries
   an explicit "AI&D Tribe enabler" tag.

## What to ask Claude next

When picking this up: paste this digest into the first chat in the new
project. Likely next prompts: (a) draft the EMM-facing one-pager from
the diagnostic, (b) propose the cluster of 5–8 programmes the 159
initiatives roll up into, (c) design the Q2 QBR meeting agenda under
the decision-forum model, or (d) draft the 2027 OKR PoC framework with
Vavro.
