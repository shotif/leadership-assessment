# Comprehensive meeting notes and action plan
- **Conversation ID:** `df419f44-5f06-4205-80c0-2af290806944`
- **Created:** 2026-03-16T18:37:45.134628+00:00
- **Updated:** 2026-03-17T12:12:04.519527+00:00
- **Messages:** 16

---

## Human  *(2026-03-16T18:37:45.830536+00:00)*

Please help me create comprehensive meeting notes with action points from the following draft from my colleague, and include any notes and points you can recognize from the attached handwritten notes. Please ask me additional clarification questions, propose a structure and draft comprehensive meeting notes and  action plan:

## Assistant  *(2026-03-16T18:39:13.137509+00:00)*

The user wants me to create comprehensive meeting notes from handwritten notes in the PDF. Let me look at the PDF content first.

The document appears to be handwritten notes but the content wasn't extracted in the document tags - they appear empty. Let me view the file directly.

The PDF is a binary file with compressed image content. I need to use the PDF skill to extract the images from the pages. But wait - the document tags in the context show the PDF pages are empty/blank. The PDF likely contains scanned handwritten notes as images. Let me try to use the pdf skill to extract the content, or I can use the bash tool to convert the pages to images and then use Claude's vision to read them.

Actually, looking at the system prompt, the document content was shown as empty in the `<document>` tags. This suggests the pages might be scanned images (not text-based PDF). I should use the PDF skill to try to extract images, or use bash/python to convert to images.

Let me start by checking what the PDF skill can do.

The PDF contains scanned handwritten notes as images. I need to convert the PDF pages to images and then use Claude's vision to read the handwriting. Let me convert the PDF to images using pdf2image/poppler.

Now I have a good read of all 3 pages. Let me interpret them:

**Page 1: AI Strategy - 16.3.**
- Way of Work
  - Katalozi use cases (Use case catalog)
    - Enableri → AI tribe (Enablers → AI tribe)
    - UC-evi → Poslovanje w/ AI Consultants (Use cases → Business with AI Consultants)
      - → value / effort [diagram showing value vs effort matrix]
- Fail:
  - value commitment → tko? (who?)
  - B-1 nema ideje (B-1 has no ideas)
  - [B-1] — Proof of Value?
- COO ← → CITO ← → CRO/CBO
  - CS → 4 buckets
    - MCP + Voice/Agents + QA + Training + EchoCS (StarTalk)
  - Y1, Y2, Y3, Y4, 2030 [timeline showing cost reduction trajectory with -6%, -51%, -5%]
- NBA - Orchestrator + RM
- Mirđer / NOC / Thorsten Hirsch → CITO / also NETWORK

**Page 2:**

Now I'm mapping out the three main strategic buckets—COO, CRO/CBO with an incremental year-by-year plan, and CTEO—while coordinating with Maša on consultations and pushing the sales angle. I need to include Ogi and Thorsten in the Mirđer discussion, then dive deeper into core network, advertising, and customer support dynamics.

**Page 3: Petra - AI 360**

Looking at the team allocation across MCP initiatives, with Maira driving MovementX at 40%, Karla bootstrapping at 80%, and Luka also involved in the mix.

I'm seeing the CP metrics showing a 120% increase in FTE but a 20 working day reduction, with eight tools or modules needed for R1 delivery by April 15th, pushing to April 20th due to service constraints. There's a parallel workstream timeline I need to map out, and I should clarify some details with Robi before moving forward with the draft. I'm identifying some key acronyms and terms that need clarification—NBA likely refers to Next Best Action with an Orchestrator and Recommendation Model, those percentage targets are probably cost reduction goals, and the product names like EchoCS and StarTalk need confirmation. I have enough context now to propose a document structure while asking Robi for clarification on these specific items.Good — I can read all three pages clearly. Here's what I've decoded before we move to drafting:

**Page 1 (AI Strategy - 16.3.):** Way of Work discussion, use case catalog approach, failure modes (value commitment/B-1 ownership), organizational topology (COO ↔ CITO ↔ CRO/CBO), CS 4-bucket architecture (MCP + Voice/Agents + QA + Training + EchoCS/StarTalk), multi-year efficiency targets (-6%/-51%/-5%), NBA Orchestrator + RM, and a reference to NOC/Thorsten Hirsch as CITO at NETWORK.

**Page 2:** Maša on consultations, Sales push theme, "3 Big Buckets → Big Stones → North Star" framing across COO/CRO-CBO/CTEO, Ogi+Thorsten to be included in Minder(meeting?), Deep Dive 2 covering Core NT / Advertising / Customer Support & Sales B2D.

**Page 3 (Petra - AI 360):** Team allocation — Maira (MovementX, 40%), Karla (Bootstrap, 80%), Luka (MCP, 3%/34%) → 120% FTE headcount question, 20 WD timeline, 8 tools/modules, deadlines: 15.4. (first delivery) and 20.4. (due to Usluge/Services).

A few things I want to clarify before writing the final notes:

I need to wait for the user's response to these questions. But they haven't responded yet - I should present this to the user and wait.

Actually, looking at the interaction - this seems to be a tool call that was presented to the user and now I should present the proposed structure and wait for their answers. Let me present the proposed structure alongside the clarification questions.While you answer those, here's the **proposed structure** for the meeting notes — let me know if you want to adjust it:

---

**AI Strategy Working Session — 16.3.2026**

1. **Meeting Overview** — date, attendees (Robi, Petra, Maša, Ogi, + others), purpose
2. **Way of Work: AI Use Case Operating Model** — catalog approach, AI Tribe enabler role, UC-to-business pairing with AI Consultants, value/effort framing
3. **Organizational Accountability** — COO / CITO / CRO-CBO triangle; failure modes called out (value commitment gap, B-1 ownership); Proof of Value challenge
4. **CS AI Architecture — 4 Buckets** — MCP, Voice/Agents, QA, Training + EchoCS/StarTalk; efficiency targets Y1–2030; NBA Orchestrator + RM
5. **Sales & Marketing AI Theme** — Maša consultations, Sales push, 3 Big Buckets → Big Stones → North Star; incremental YbY plan; Deep Dive 2 scope (Core NT / Advertising / CS&S B2D)
6. **AI 360 Initiative (Petra)** — team allocation (Maira/Karla/Luka), 8 tools/modules for R1, 20 WD timeline, key deadlines (15.4. / 20.4.)
7. **Network / CITO** — NOC, Thorsten Hirsch as CITO, Minder inclusion
8. **Action Items** — owner / deadline table

---

Also — you mentioned "a draft from my colleague" in your message, but I only see the handwritten notes. Did you mean to attach a typed draft as well, or are the handwritten notes the only source?

## Human  *(2026-03-16T18:40:26.667806+00:00)*

Q: What does 'Mirđer' refer to on pages 1-2? (it appears in context with NOC, Thorsten, Ogi)
A: Minder is the specific project name, automating network operations and NOC with agentic AI

Q: The Y1–Y4/2030 graph with -6%, -51%, -5% — what does this represent?
A: illustrative (not real numbers), showcasing the progressive approach in headcount reduction towards the target picture (2030)

Q: What output format do you want for the final meeting notes?
A: let's just continue discussing the structure for now

## Assistant  *(2026-03-16T18:40:51.722041+00:00)*

Good context. Let me now propose a refined structure and ask a few more clarifying questions before drafting.

Key clarifications received:
- Minder = project automating network operations/NOC with agentic AI
- Y1-Y4/2030 graph = illustrative headcount reduction trajectory toward 2030 target
- Output format TBD after structure discussion

Let me think about what I still need to clarify and propose the structure more concretely.

Some things still unclear from the notes:
- Page 1: "fail:" section - "value commitment → kto?" (who?) and "B-1 nema ideje" - these are failure modes being called out

- Page 2 is clarifying some organizational structure: Customer Service breaks into four buckets, and there's a COO role with CS underneath, plus Ogi and Thorsten Hirsch from Deutsche Telekom should be involved in Minder, Maša is handling consultations, Sales needs a push, and there's a framework of three big budgets flowing into big stones that align with the North Star.

Now looking at page 3, I'm seeing release planning details—8 tools or modules needed for Release 1, with phased delivery by April 20th tied to service requirements. There's also what looks like an internal political question about whether Mate is applying pressure. But I should dig into those risk items from page 1 first—the "fail" section seems to be flagging critical ownership gaps, like who's accountable for value commitment and whether the B-1 level even has a clear direction on this. These feel like risks that need explicit owners assigned.Good, this helps a lot. A few more targeted questions before drafting:

Also — while you answer — two things I want to flag on the proposed structure:

On **section 3 (Org Accountability)**, the COO ↔ CITO ↔ CRO/CBO triangle seems to be about who sponsors/owns AI use cases across domains, not just governance. I'd suggest framing it as "AI Ownership Model across Functions" rather than pure governance — does that resonate?

And on **section 6 (AI 360 / Petra)** — the 120% FTE note and "Mate vrši pritisak?" together suggest there's a resourcing tension being discussed. Depending on your answer above, this section may need a dedicated risks/dependencies note.

## Human  *(2026-03-16T18:41:21.377136+00:00)*

Q: Page 1 has a 'fail:' section noting 'value commitment → kto?' and 'B-1 nema ideje'. How should this be treated in the notes?
A: Include as risks/blockers (named)

Q: Page 3: 'Mate vrši pritisak?' (Is Mate applying pressure?) — include in notes?
A: No, keep out of formal notes

Q: NBA on page 1 — what does it stand for in this context?
A: Next Best Action

## Assistant  *(2026-03-16T18:42:04.617684+00:00)*

Good. Now I have enough to draft comprehensive meeting notes. Let me also note that the user mentioned "a draft from my colleague" but only attached handwritten notes. I should ask about this before drafting, or just proceed with what I have and note the gap.

Actually, re-reading the original message: "Please help me create comprehensive meeting notes with action points from the following draft from my colleague, and include any notes and points you can recognize from the attached handwritten notes."

The "draft from my colleague" seems to be referring to something that wasn't actually attached - only the handwritten PDF was uploaded. I should flag this and proceed with what I have.

Let me now synthesize everything I know and draft the meeting notes. Let me do this in the chat rather than as a file for now since the user said "let's just continue discussing the structure for now."

Actually, I've worked through the clarifications already, so I should move forward with drafting the notes in the chat as a proposed version. I have the meeting details—AI Strategy Working Session on 16.3.2026 with attendees including Robi, Petra, Maša, Ogi, Thorsten Hirsch, and others—and I can structure this around the handwritten notes I've reviewed.

Now I'm looking at the rest of the topics covered: the organizational AI ownership model with the COO/CITO/CRO-CBO triangle, how CS maps into four buckets under that structure, and the AI architecture components like MCP, Voice/Agents, and QA that make up those buckets.

For the CS AI architecture specifically, I'm thinking through a multi-year roadmap spanning four years out to 2030, with progressive headcount reductions at different phases and an NBA orchestrator component with a RM layer. There's also the Minder project for network operations automation under Thorsten as CITO, and then the sales and marketing side where Maša handles consultations, with a framework of three big buckets rolling up to a North Star, owned by the COO, CRO-CBO, and CTEO.

Looking at the Deep Dive 2 scope, it covers Core NT, Advertising, and Customer Support & Sales B2D. For AI 360 under Petra, I'm seeing a team of three people across different initiatives—Maira on MovementX at 40%, Karla on Bootstrap at 80%, and Luka on MCP around 34%—which adds up to about 120% FTE, so there's definitely a resourcing crunch. They're building out eight tools or modules for the first release, with two key deadlines: April 15th for the initial delivery and April 20th for the services handoff.Perfect, that's enough to draft. Here's the proposed meeting notes — review and let me know what to adjust before we produce the final document:

---

## AI Strategy Working Session
**Date:** 16 March 2026
**Attendees:** Robi, Petra, Maša, Ogi, Thorsten Hirsch (CITO, Network) + NOC representatives

---

### 1. AI Operating Model — Way of Work

Two distinct tracks from the use case catalog were confirmed:
- **Enableri → AI Tribe**: internal capability and tooling track, owned by AI & Data Tribe
- **UC-evi → Poslovanje + AI Consultant**: business deployment track, pairing use cases with AI Consultants who work directly with business units

Prioritization logic follows a value/effort matrix. The B-1 layer is the expected execution interface between strategy and business units.

**Risks / Blockers (named):**
- *Value commitment ownership gap*: unclear who ultimately commits to value delivery per use case — this must be resolved explicitly
- *B-1 disengagement*: B-1 layer currently lacks ownership or initiative on AI ("nema ideje") — a structural risk to execution velocity
- *Proof of Value*: no established mechanism yet to demonstrate/validate business value from AI deployments; open question requiring resolution

---

### 2. AI Ownership Model Across Functions

Discussed the organizational triangle for AI sponsorship and accountability:
- **COO** — operational AI, CS domain
- **CITO** — technology and network AI
- **CRO / CBO** — commercial and customer AI

Each function anchors a cluster of use cases. Cross-functional coordination mechanism to be defined.

---

### 3. CS AI Architecture — 4 Buckets

Customer Service AI structured into four delivery buckets:
- MCP
- Voice / Agents
- QA
- Training + EchoCS (StarTalk)

**Next Best Action (NBA):** Orchestrator + RM component confirmed as part of the CS AI architecture.

**Multi-year roadmap (illustrative headcount reduction targets):**
- Y1 → progressive automation begins
- Y2/Y3 → acceleration phase
- Y4 / 2030 target → full target picture (illustrative: -6% / -51% / -5% across defined segments)

*Note: figures are illustrative to demonstrate progressive approach, not committed targets.*

---

### 4. Minder — Network Operations AI (Project)

Minder is the initiative to automate network operations and NOC using agentic AI.
- **CITO sponsor:** Thorsten Hirsch
- **Action:** Ogi and Thorsten to be formally included in the Minder project structure

---

### 5. Sales & Marketing AI — Strategic Framing

- **Maša** leading AI consultation track for Sales & Marketing
- **Sales push** confirmed as a priority theme
- Strategic framework: **3 Big Buckets → Big Stones → North Star**, with incremental year-by-year plan and high-value use case focus
- Ownership split: COO / CRO-CBO / CTEO

**Deep Dive 2 scope confirmed:**
- Core NT
- Advertising
- Customer Support & Sales B2D

---

### 6. AI 360 Initiative (Petra)

Team composition and allocation for R1:
- **Maira** (MovementX) — 40%
- **Karla** (Bootstrap) — 80%
- **Luka** (MCP) — ~34%
- *Combined ~120% FTE — resourcing tension flagged, to be resolved*

Scope: 8 tools / modules for R1 delivery
Timeline: 20 working days

**Key deadlines:**
- **15 April** — first delivery (FAZM Delivery)
- **20 April** — final delivery to Usluge (Services)

---

### Action Items

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Define and assign value commitment ownership per use case | Robi | TBD |
| 2 | Develop Proof of Value framework for AI deployments | Robi / AI Tribe | TBD |
| 3 | Activate B-1 layer engagement on AI — propose mechanism | Robi | TBD |
| 4 | Formally include Ogi and Thorsten in Minder project structure | Robi / Ogi | Immediate |
| 5 | Finalize AI 360 R1 resourcing (resolve 120% FTE gap) | Petra | ASAP |
| 6 | Deliver AI 360 R1 — 8 tools/modules | Petra + team | 15 April |
| 7 | AI 360 final delivery to Usluge | Petra | 20 April |
| 8 | Define cross-functional AI coordination mechanism (COO/CITO/CRO-CBO) | Robi | TBD |
| 9 | Deep Dive 2 prep: Core NT / Advertising / CS&S B2D | Maša + relevant leads | TBD |

---

A couple of things I'd like your input on before finalizing:

1. Some deadlines are marked TBD — do you have specific dates for actions 1–3 and 8–9?
2. Should the B-1 risk and value commitment gap be framed more diplomatically (e.g. "open organizational question") or kept direct as written?
3. Any attendees I'm missing, and do you need a distribution list at the top?

## Human  *(2026-03-16T18:43:15.812280+00:00)*

here are the draft notes from my colleague, please use this only as a starting point and then complement from findings from the handwritten notes. Please, disregard any inputs coming from page 3 of the previously uploaded document (this page was from another meeting): AI is a key enabler of the transformation towards a fully digitalized company with approximately 25% fewer employees.

The objective is a structural change of the operating model by 2030, not isolated AI use cases or pilots.

 

 

Acceleration and Commitment
 

We need to significantly accelerate execution in order to be able to commit to concrete, measurable results already by the end of 2026.

Resources should be focused on initiatives with clear and provable value, rather than being spread across ad‑hoc initiatives that are not sufficiently analysed or linked to measurable outcomes.

 

 

Value Ownership
 

B‑1 management is responsible for defining the value of each AI initiative, clearly classified as:

Trim
Revenue
Savings
Decisions on value must be taken at B‑1 level, not at group leader level.

 

 

Operating Model (Business × AI)
 

B‑1 managers currently do not have sufficient clarity on what the business truly needs, which limits focus on the right transformation initiatives.

Group leaders are expected to identify their key pain points and address them to the AI department.

AI consultants act as partners to the business, helping translate business problems into efficient and scalable AI solutions.

 

 

BIG ROCKS Focus – 3 Key Areas (~4000 FTEs)
Three major areas have been identified where large, AI‑driven transformation initiatives must be launched to achieve the 2030 target:

COO –field services, technicians, call center

COR – back‑office operations, AI agentic

CTIO – Technology, network, NOC

 

These areas together represent approximately 4,000 FTEs and the highest potential for structural impact.

For each area, it is required to define:

long‑term target (2030)
annual increments and milestones leading to that target
 

 

Examples of Key AI Initiatives
AI‑driven Contact Center – Voice bots, AI chat and IVR solutions; reference cases show −70% inbound calls (Germany) and −90% (Austria), with a long‑term goal of full CC automation
Hungarian Telekom – VSE segment – Example of best practice where direct sales contact with customers has been fully eliminated through an AI‑driven sales model
Self‑healing Network & AI‑based NOC – Autonomous incident detection and resolution
AI Assistants for Technicians – AI‑based mentoring, faster field execution and AI quality control for fiber installations.
 

 

Governance
The AI Roadmap will be reviewed every two weeks within a dedicated core team.

## Assistant  *(2026-03-16T18:43:45.435011+00:00)*

Now I have both sources. Let me synthesize the colleague's typed draft with the handwritten notes (pages 1 and 2 only, ignoring page 3) into comprehensive meeting notes.

Key additions from handwritten notes to layer in:
- Way of Work: Enableri → AI Tribe / UC-evi → Poslovanje + AI Consultant structure
- Value/effort matrix for prioritization
- Fail/risks: value commitment ownership gap, B-1 disengagement ("nema ideje"), Proof of Value
- NBA Orchestrator + RM (CS architecture)
- 4 CS buckets: MCP + Voice/Agents + QA + Training + EchoCS (StarTalk)

- Multi-year headcount reduction trajectory and the Minder project details (Thorsten Hirsch, NOC, Ogi involvement)
- Maša's role in consultations and sales acceleration
- Deep dive sessions covering Core NT, Advertising, and Customer Support & Sales B2D
- The 3 Big Buckets framework cascading down to Big Stones and North Star metrics with year-over-year incremental targets

The typed draft anchors this with concrete numbers: 25% workforce reduction by 2030, structural reorganization, value ownership split across Trim/Revenue/Savings, and the BIG ROCKS initiative under COO/COR/CTIO leadership managing roughly 4000 FTEs.

Now I'm pulling together the governance cadence and biweekly review structure to finalize the comprehensive meeting notes.Got it. Here's the merged draft — colleague's text as the formal backbone, handwritten notes layered in throughout:

---

## AI Strategy Working Session
**Date:** 16 March 2026
**Attendees:** Robi, Petra, Maša, Ogi, Thorsten Hirsch (CITO, Network)

---

### 1. Strategic Context

AI is a key enabler of HT's transformation towards a fully digitalized company, targeting approximately 25% fewer employees by 2030. The objective is a **structural change of the operating model**, not isolated use cases or pilots. Three major functional areas have been identified as BIG ROCKS, collectively representing ~4,000 FTEs and the highest potential for structural impact:

- **COO** — field services, technicians, call center
- **CRO/CBO** — back-office operations, agentic AI
- **CITO** — technology, network, NOC

For each area, the requirement is to define: (a) long-term 2030 target, and (b) annual increments and milestones leading to that target. The multi-year trajectory is illustrative but directional — progressive automation building toward the 2030 target picture.

---

### 2. Acceleration and Commitment

Execution must significantly accelerate in order to commit to concrete, measurable results by end of 2026. Resources are to be focused on initiatives with clear and provable value — not spread across ad-hoc initiatives lacking measurable outcomes or sufficient analysis.

**Strategic framing discussed:** 3 Big Buckets → Big Stones → North Star, with a high-value, incremental year-by-year plan. The logic: identify the largest structural opportunities per domain, define the long-term North Star, and work backwards into annual milestones.

---

### 3. Value Ownership

B-1 management is responsible for defining the value of each AI initiative, classified as:
- **Trim** (cost reduction)
- **Revenue** (top-line growth)
- **Savings** (efficiency/productivity)

Decisions on value must be taken at B-1 level, not group leader level.

**Risks / Blockers (named):**
- *Value commitment ownership gap:* it remains unclear who ultimately commits to value delivery per use case — must be explicitly resolved
- *B-1 disengagement:* B-1 layer currently lacks initiative and ownership on AI; this is a structural risk to execution velocity that requires direct intervention
- *Proof of Value:* no established mechanism yet to validate business value from AI deployments; open question requiring a concrete framework

---

### 4. AI Operating Model (Business × AI)

**Way of Work — two delivery tracks confirmed:**
- **Enableri → AI Tribe**: internal capability-building and tooling, owned by the AI & Data Tribe
- **UC-evi → Poslovanje + AI Consultants**: business deployment track — use cases paired with AI Consultants who translate business problems into scalable AI solutions

Prioritization follows a **value/effort matrix**. B-1 managers currently lack sufficient clarity on what the business truly needs, which limits focus on the right transformation initiatives. Group leaders are expected to identify key pain points and address them to the AI department. AI Consultants act as partners to the business, not internal service providers.

---

### 5. Key AI Initiatives by Domain

**COO — Customer Service AI (4 Buckets architecture):**
- MCP
- Voice / Agents
- QA
- Training + EchoCS (StarTalk)
- **Next Best Action (NBA):** Orchestrator + RM confirmed as part of CS AI architecture

Reference benchmarks: −70% inbound calls (Germany), −90% (Austria); long-term goal of full contact center automation. Hungarian Telekom VSE segment cited as best practice — direct sales contact with customers fully eliminated through AI-driven sales model.

**CITO — Minder (Network Operations AI):**
Minder is the initiative to automate network operations and NOC using agentic AI. Sponsor: **Thorsten Hirsch (CITO)**. Self-healing network and AI-based NOC are the core scope — autonomous incident detection and resolution. AI Assistants for Technicians (AI-based mentoring, fiber installation QA) also in scope.

**CRO/CBO — Sales & Marketing AI:**
- **Maša** leading AI consultation track for Sales & Marketing
- **Sales push** confirmed as a key theme
- **Deep Dive 2 scope:** Core NT / Advertising / Customer Support & Sales B2D

---

### 6. Governance

The AI Roadmap will be reviewed every two weeks within a dedicated core team. Ogi and Thorsten Hirsch to be formally included in the Minder project structure.

---

### Action Items

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Define and assign value commitment ownership per use case | Robi | TBD |
| 2 | Develop Proof of Value framework for AI deployments | Robi / AI Tribe | TBD |
| 3 | Activate B-1 engagement on AI — define intervention mechanism | Robi | TBD |
| 4 | Formally include Ogi and Thorsten Hirsch in Minder project structure | Robi / Ogi | Immediate |
| 5 | Define long-term 2030 targets + annual milestones per BIG ROCK (COO/CRO/CITO) | Domain leads + Robi | TBD |
| 6 | Define cross-functional AI coordination mechanism across COO/CITO/CRO-CBO | Robi | TBD |
| 7 | Deep Dive 2 prep: Core NT / Advertising / CS&S B2D | Maša + relevant leads | TBD |
| 8 | Schedule next biweekly AI Roadmap review | Robi | Immediate |

---

A few things still worth confirming before this goes to final:

1. **TBD deadlines** on actions 1–3 and 5–7 — do you have dates, or should these land at the next biweekly review?
2. **"COR" in the colleague's draft vs "CRO/CBO" in the notes** — I've used CRO/CBO throughout to match the org structure from the handwritten notes; confirm if COR is a different entity
3. **Distribution** — who receives the final version? Board-level, B-1, or working team only?

## Human  *(2026-03-16T18:52:47.865390+00:00)*

the 3 big buckets are organizational areas: COO (chief operating officer) covering customer support and technicians, CRO/CBO as commercial areas (sales, marketing, backoffice) and CTIO (technology, IT, network, NOC). Big Rocks are used as a metaphor for big opportunities. the value drivers are (non-comprehensive): TRIM (customer satisfaction), Revenue (Growth), Savings (Cost reduction). Northstar was a benchmark which shows functional vs organizational cost and revenue allocation according to a standardized telco operating model, showing gaps in our org vs best in class and average - to be taken as a guiding model, but not necessarily literally as it is prone to strategic decision impact (e.g. not investing in core radio network modernization shows great results in cost efficiency of that area). Value commitment is on B-1 outside of AI & Data Tribe (responsible for enablers), AI Tribe members act as consultants for the rest of the organization by bringing knowledge about what AI can be used for and helping identify areas with potential application. Attendees were: Ogi, Fred, Ana (stand-in for Branimir), Mate, Gigi, Robi. Thorsten Hirsch is mentioned as a group network leadership team member that Ogi will contact about Minder. Please create more concise notes in a simple structure, try to consolidate action items in the action plan. Include also a risk on delivery capacity of the AI Tribe technical team and that a necessity for scaling (increasing number of developers of 4 FTEs) was mentioned in an earlier board meeting - this point is still open for clarification between Ogi, Fred and Robi

## Assistant  *(2026-03-16T18:54:26.168191+00:00)*

Let me now produce clean, concise meeting notes with all the corrections and additions incorporated.

Now I have everything I need to produce the final, concise meeting notes as a .docx document. Let me compile all the information and create it.

Key updates from the last message:
- 3 big areas: COO (customer support, technicians), CRO/CBO (sales, marketing, backoffice), CTIO (technology, IT, network, NOC)
- Big Rocks = metaphor for big opportunities
- TRIM = customer satisfaction (not cost reduction as I had it), Revenue = growth, Savings = cost reduction
- Northstar = benchmark model (functional vs organizational cost/revenue allocation per standardized telco operating model)

- Value commitment sits outside the AI & Data Tribe on B-1, with the tribe functioning as consultants to the effort
- Key attendees are Ogi, Fred, Ana (standing in for Branimir), Mate, Gigi, and Robi; Thorsten Hirsch from group network leadership needs to be contacted by Ogi regarding Minder
- There's a capacity risk with the AI Tribe's delivery—they need to scale up to 4 FTEs of developers, and this gap is being discussed between Ogi, Fred, and Robi

Let me draft the clean notes now in a simple structure without page 3 content, then generate the docx.Good — I have everything needed. Let me produce the final document now.

Clean document, 7 sections + action table. A few things to flag:

The **TRIM definition** — your colleague's draft lists it as a value driver category alongside Revenue and Savings, but you clarified it means customer satisfaction/experience. I've used your definition. Worth aligning with whoever owns the value classification framework so B-1s apply it consistently.

The **AI Tribe scaling risk (item 6)** is left as TBD deadline since it's actively open between you, Ogi and Fred — you may want to anchor it to a specific date before this goes out.

Everything from page 3 (Petra / AI 360) has been excluded as instructed.

## Human  *(2026-03-16T19:00:49.819870+00:00)*

this is too complicated and too much text, needs to be simplified. Don't create a word, generate your draft in chat so we can iterate on it

## Assistant  *(2026-03-16T19:01:06.188861+00:00)*

The user wants a simpler, more concise draft in chat format for iteration.Got it. Here's a leaner version:

---

**AI Strategy — Working Session Notes**
**Date:** 16 March 2026
**Attendees:** Ogi, Fred, Ana (for Branimir), Mate, Gigi, Robi

---

**Context**
HT's AI strategy targets a structural operating model change by 2030 — approximately 25% fewer employees. The focus is transformation at scale, not isolated pilots.

**Big Rocks — 3 Priority Areas (~4,000 FTEs)**
- **COO** — customer support, field technicians
- **CRO/CBO** — sales, marketing, back-office
- **CTIO** — technology, IT, network, NOC

Each area requires a defined 2030 target and annual milestones. The North Star benchmark (best-in-class telco operating model) serves as directional reference, not a literal target.

**Operating Model**
AI Tribe acts as internal consultant — identifying opportunities, translating business problems into AI solutions. Value ownership sits with B-1 managers in each domain, classified as Trim / Revenue / Savings. Group leaders identify pain points; AI Tribe delivers solutions.

**Key Initiative Examples**
- Contact Center AI: voice bots, chat, IVR — benchmarks show up to -90% inbound calls (Austria)
- Minder: agentic AI for network ops and NOC automation (CTIO domain)
- NBA Orchestrator + RM: next best action layer for CS
- Sales AI: Hungarian Telekom VSE as reference — full AI-driven sales, no direct customer contact

**Risks**
- B-1 layer not yet engaged or owning AI value delivery
- No Proof of Value framework in place
- AI Tribe technical capacity (4 developer FTEs) is a bottleneck risk — scaling discussed at prior board meeting, still open

**Actions**

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Assign B-1 value ownership per use case across all three domains | Robi + B-1s | Next biweekly |
| 2 | Ogi to contact Thorsten Hirsch re: Minder | Ogi | Immediate |
| 3 | Define Proof of Value framework | Robi / AI Tribe | Next biweekly |
| 4 | Resolve AI Tribe developer scaling (open from board) | Ogi, Fred, Robi | TBD |
| 5 | Prep Deep Dive 2: Core NT / Advertising / CS&S B2D | Maša + leads | TBD |
| 6 | Schedule biweekly AI Roadmap review | Robi | Immediate |

---

What would you like to cut, expand, or reframe?

## Human  *(2026-03-16T19:05:37.661652+00:00)*

HT has a target of operating model change by 2030 - this is not sole responsibility of the AI strategy, but needs to be strongly supported by AI strategy execution. the 3 priority areas are not called big rocks, big rocks are the use cases with very high potential impact. Group leaders is an example term, b-2 and b-3 management (including group leaders) posess the operational insights about each are/departments operating model which is required to identify AI opportunities, but lack ownership & accountability for value commitment which is with b-1 managers. Proof of value could be extracted from delivered 2025 use cases - this is an action item for Mate. AI Tribe technical capacity is currently at 2,5-3 FTEs, additional 4 are required. Maša is leading the technical services sector which could be highly impacted by AI, so she isn't responsible for Prep Deep Dive2 etc.

## Assistant  *(2026-03-16T19:05:49.129975+00:00)*

Good corrections. Let me incorporate all of these and redraft cleanly.Good corrections throughout. Revised draft:

---

**AI Strategy — Working Session Notes**
**Date:** 16 March 2026
**Attendees:** Ogi, Fred, Ana (for Branimir), Mate, Gigi, Robi

---

**Context**
HT's 2030 target is a structural operating model change — AI strategy execution is a critical enabler of this, but not the sole driver.

**3 Priority Organizational Areas (~4,000 FTEs)**
- **COO** — customer support, field technicians
- **CRO/CBO** — sales, marketing, back-office
- **CTIO** — technology, IT, network, NOC

For each area: define a 2030 target and annual milestones. The North Star benchmark (best-in-class telco operating model) is directional reference, not a literal target — strategic investment decisions will influence the actual trajectory per area.

**Operating Model**
B-2/B-3 management (incl. group leaders) hold the operational insight needed to identify AI opportunities within their areas. B-1 managers own value commitment for each initiative, classified as Trim / Revenue / Savings. The AI Tribe acts as internal consultant — bringing AI knowledge, identifying opportunities, and translating them into solutions.

**Big Rocks** are high-potential use cases to be identified per area. Key reference examples:
- Contact Center AI: voice bots, chat, IVR — benchmarks up to -90% inbound calls (Austria)
- Minder: agentic AI for network ops and NOC automation (CTIO)
- NBA Orchestrator + RM: next best action layer for CS
- Sales AI: Hungarian Telekom VSE — full AI-driven sales model as reference

**Risks**
- B-1 layer not yet engaging or owning AI value delivery
- AI Tribe technical capacity at 2.5–3 FTEs; scaling by +4 FTEs discussed at prior board meeting — still open
- Proof of Value not yet established; extractable from 2025 delivered use cases

**Actions**

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Assign B-1 value ownership per use case across all three areas | Robi + B-1s | Next biweekly |
| 2 | Contact Thorsten Hirsch re: Minder involvement | Ogi | Immediate |
| 3 | Extract Proof of Value from 2025 delivered use cases | Mate | TBD |
| 4 | Resolve AI Tribe developer scaling (+4 FTEs, open from board) | Ogi, Fred, Robi | TBD |
| 5 | Define Deep Dive 2 scope and ownership: Core NT / Advertising / CS&S B2D | Robi | Next biweekly |
| 6 | Schedule biweekly AI Roadmap review | Robi | Immediate |

---

Anything else to adjust?

## Human  *(2026-03-17T12:11:24.607325+00:00)*

turn this into microsoft word from markdown format, without any additional formatting:
**AI Strategy - Internal Efficiency Pillar - Working Session Notes**
**Date:** 16 March 2026
**Attendees:** Ogi, Fred, Ana (for Branimir), Mate, Gigi, Robi
 
---
 
**Context**
HT's 2030 target is a structural operating model change — AI strategy execution is a critical enabler of this, but not the sole driver.
 
**3 Priority Organizational Areas (~4,000 FTEs)**
- **COO** — customer support, field technicians
- **CRO/CBO** — sales, marketing, back-office
- **CTIO** — technology, IT, network, NOC
 
For each area: define a 2030 target and annual milestones. The North Star benchmark (best-in-class telco operating model) is directional reference, not a literal target — strategic investment decisions will influence the actual trajectory per area.
 
**Operating Model**
B-2/B-3 management (incl. group leaders) hold the operational insight needed to identify AI opportunities within their areas. B-1 managers own value commitment for each initiative, classified as Trim / Revenue / Savings. The AI Tribe acts as internal consultant — bringing AI knowledge, identifying opportunities, and translating them into solutions.
 
**Big Rocks** are high-potential use cases to be identified per area. Key reference examples:
- Contact Center AI: voice bots, chat, IVR, training (StarTalk), outbound (EchoCS) — benchmarks (stretch!) up to -90% inbound chats deflected (Austria)
- Example from Group: Minder: agentic AI for network ops and NOC automation (CTIO)
- NBA Orchestrator + Relationship Manager: next best action layer for CS/Sales/CVM/...
- Example for Group: Sales AI: Hungarian Telekom VSE — full AI-driven sales model as reference
- AI Assistants for Technicians - AI-based mentoring, field execution quality control, SMC automation
 
**Risks**
- B-1 layer not yet fully engaging or owning AI value delivery
- AI Tribe technical capacity at 2.5–3 FTEs; scaling by +4 FTEs discussed at prior board meeting — still open
- Proof of Value not yet established; potentially extractable from 2025 delivered use cases (to be explored)
 
**Actions**
 
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Assign B-1 value ownership per use case across all areas for next session discussion | Mate w/ Robi | Next biweekly |
| 2 | Contact Thorsten Hirsch re: Minder involvement | Ogi | ASAP |
| 3 | Extract Proof of Value from 2025 delivered use cases | Mate | TBD |
| 4 | Resolve AI Tribe developer scaling (+4 FTEs, open from board) | Ogi, Fred, Krešo, Robi | TBD |
| 5 | Schedule biweekly AI Roadmap review | Mate (Robi) | ASAP |

## Assistant  *(2026-03-17T12:12:04.497037+00:00)*

The user wants a clean Word document from the provided markdown, minimal formatting.

Clean Word doc, Arial throughout, no extra styling — just bold where your markdown had bold, bullets as bullets, action table at the end.
