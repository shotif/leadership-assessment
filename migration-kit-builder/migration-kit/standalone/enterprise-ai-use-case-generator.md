# Enterprise AI use case generator
- **Conversation ID:** `94007264-611d-4817-a684-48a774ad0663`
- **Created:** 2026-03-07T12:52:22.870701+00:00
- **Updated:** 2026-03-07T13:06:24.481617+00:00
- **Messages:** 8

---

## Human  *(2026-03-07T12:52:23.308536+00:00)*

Help me complete the following prompt by asking me questions to fill in the variables, and I would like to change the style guidelines, I will provide you with a file when asked:
You are a senior AI solutions architect and business consultant with deep expertise in enterprise AI implementation. Your task is to generate 10 specific, technically-grounded AI use cases for a client — delivered as a fully self-contained, interactive HTML report.

── CLIENT CONTEXT ───────────────────────────────────────────────────────

Company name: [CLIENT COMPANY NAME]
Industry / sector: [e.g. manufacturing, banking, retail, logistics, pharma]
What the company does: [2–3 sentence description — products, customers, scale]
Focus scope: [one of: specific department name | company-wide | specific business process]
Department / function (if focused): [e.g. Supply Planning, Finance, HR, Customer Service — or write "company-wide"]
Current systems / tech stack: [e.g. SAP S/4HANA, Salesforce, Oracle, custom ERP — or "unknown"]
Known data pain points: [e.g. siloed data, inconsistent naming, no real-time visibility — or "unknown"]
Company size: [headcount and/or revenue range]
Geography: [countries or regions where they operate]

── ARCHITECTURE CONSTRAINT ───────────────────────────────────────────────

Every use case must follow this technical pattern:
— Internal data sources (ERP, CRM, databases, files — whatever the client has)
— External data sources (market data, APIs, news feeds, regulatory databases, supplier portals)
— MCP (Model Context Protocol) layer with specific integrations and tools listed
— LLM on top (Claude or equivalent) as the reasoning and interaction layer

Each use case is a realistic, deployable AI agent or workflow — not a chatbot wrapper.

── OUTPUT REQUIREMENTS ───────────────────────────────────────────────────

Generate exactly 10 AI use cases. For each use case, provide:

PROBLEM STATEMENT
One punchy paragraph explaining what pain exists today. Be specific to this industry and department. Name the exact bottleneck — not "data is siloed" but "the production planner has to reconcile 4 spreadsheets across 3 systems every Monday morning before they can see a single reliable demand figure." Make the reader feel the pain.

USE CASE NAME
A memorable, slightly evocative name — like "The Living BOM" or "The Demand Whisperer" — plus a plain-language subtitle that explains what it actually does.

IMPLEMENTATION STEPS (4–7 steps)
Step-by-step what needs to happen technically and organisationally. Each step should be 1–2 sentences. Start from data access, move through integration, then to the AI layer, then to the user interface / workflow change. End with the measurable outcome.

DATA ARCHITECTURE
For each use case, list:
• Internal sources: which systems, which data entities (e.g. "SAP: open purchase orders, vendor master, BOM")
• External sources: which APIs or feeds (e.g. "LME copper spot price via Yahoo Finance API", "shipping delay signals via Flexport API")
• MCP integrations: which specific MCP servers and tools are needed (e.g. "SAP MCP connector for live ERP reads", "web search MCP for news monitoring", "file system MCP for Excel/PDF parsing")
• LLM role: what the model actually does (e.g. "semantic matching of inconsistent material names across entity databases", "real-time margin calculation with natural language explanation")

CONCRETE EXAMPLE
Write a short, vivid 3–5 sentence scenario of a real person at this company using the solution. Include a specific question they type or ask, and a specific answer the AI gives. Make it feel like a demo, not a description.

BUSINESS IMPACT
One line: what gets faster, cheaper, or less risky. If possible, quantify (e.g. "saves 4 hours per planner per week", "detects margin erosion 3 weeks earlier").

── USE CASE SELECTION CRITERIA ───────────────────────────────────────────

Choose the 10 use cases that are:
1. Specific to this company's industry and the named department or function
2. Varied in type — include at least: one real-time market signal use case, one data quality / harmonisation use case, one scenario planning use case, one sustainability or compliance use case, one customer-facing or revenue use case, and one people / HR or internal operations use case
3. Technically realistic — no magic, no "just connect everything." If a step is hard, say so
4. Different complexity levels — include 3 quick wins (doable in 6–12 weeks), 4 medium-term (3–6 months), and 3 strategic (6–18 months)

── DESIGN REQUIREMENTS ──────────────────────────────────────────────────

Visual style: clean, executive-grade. White background (#FAFAFA), deep navy accents (#1B3A6B), teal highlights (#1A5C52), warm gold for callouts (#B8862A). Use Instrument Serif for display headings, DM Sans for body text, DM Mono for labels and code (load from Google Fonts).

Layout:
— Sticky top navigation with numbered section links
— Each use case gets its own full card with collapsible sections
— Complexity badges (Quick Win / Medium-Term / Strategic) visible at a glance
— Architecture diagram per use case: simple visual showing Internal → MCP → LLM → Output flow
— Summary table at the top: all 10 use cases with name, department, complexity, and top metric

Interactive elements:
— Filter use cases by complexity level (Quick Win / Medium-Term / Strategic)
— Collapsible implementation steps per card
— Click-to-expand architecture detail
— Hover tooltips on MCP integration names explaining what each tool does

Do NOT use any external chart or diagram libraries. Build all visuals with pure HTML/CSS/JS.

All text must be in English throughout. Company name is [CLIENT COMPANY NAME] — spell it consistently everywhere.

── OUTPUT FORMAT ─────────────────────────────────────────────────────────

Output a single, self-contained HTML file. All CSS and JavaScript must be inline — no external dependencies except Google Fonts. The file must open correctly in any modern browser with no server required.

Begin the file with <!DOCTYPE html> and end with </html>. Do not include any explanation before or after the HTML. The entire response should be the HTML file and nothing else.

── QUALITY STANDARD ──────────────────────────────────────────────────────

The person reading this report should feel two things simultaneously:
(1) "I didn't know AI could do this specifically for us" — genuine surprise at the concreteness
(2) "I can see exactly how we'd build this" — confidence from the technical clarity

Do not write generic AI platitudes. Do not write "AI can help you analyse data faster." Write "On Monday morning, instead of Marija spending 3 hours reconciling purchase orders from SAP and supplier portals in Excel, she types: 'What's our real exposure on copper components if lead times slip by 2 weeks?' and gets a number with a breakdown in 8 seconds."

Think before you write. Research the industry thoroughly using your training knowledge. The use cases must feel invented by someone who has spent time on the factory floor, in the finance department, or on the planning team of this exact type of company — not someone who read a whitepaper about it.

## Assistant  *(2026-03-07T12:52:35.235077+00:00)*

The user wants me to help them fill in the variables for this prompt by asking questions. They also want to change the style guidelines and will provide a file for that. Let me ask the key questions to fill in the client context variables.Let's get the client details locked in! I'll ask about the core context first, then we can handle the style file.

The user hasn't responded yet. I need to wait for their response.While you answer those, I'll also need a few open-ended details — please type these out:

1. **Company name** — what should it be called throughout the report?
2. **What the company does** — 2–3 sentences on products, customers, and scale
3. **Current tech stack** — e.g. SAP, Salesforce, Oracle, custom ERP (or "unknown")
4. **Known data pain points** — e.g. siloed data, no real-time visibility (or "unknown")
5. **Geography** — which countries or regions do they operate in?
6. **Department / function** (if you selected "Specific department" above) — e.g. Supply Planning, Finance, HR

And whenever you're ready, **share the style guidelines file** and I'll swap out the design section before generating the report.

## Human  *(2026-03-07T12:53:06.148465+00:00)*

Q: What is the company's industry / sector?
A: telecommunications 

Q: What is the focus scope for this report?
A: Specific department

Q: What is the company's size?
A: Large enterprise (5,000–50,000)

## Assistant  *(2026-03-07T12:53:14.183152+00:00)*

The user answered the multiple choice questions. Now I need the open-ended details. Let me ask for those.Great — telecom, large enterprise, department-focused. Now I need the remaining details to complete the picture:

Also please type out the following:

1. **Company name** — as it should appear throughout the report
2. **What the company does** — 2–3 sentences: products/services, customer base, rough scale
3. **Current tech stack** — e.g. Salesforce, SAP, Oracle, Ericsson OSS/BSS, Amdocs, Netcracker (or "unknown")
4. **Known data pain points** — e.g. siloed BSS/OSS data, no real-time churn signals, inconsistent customer IDs across systems (or "unknown")
5. **Geography** — countries or regions of operation

And don't forget — **please share your style guidelines file** when ready and I'll incorporate it before building the report.

## Human  *(2026-03-07T12:53:17.704680+00:00)*

Q: Which department should the use cases focus on?
A: Sales & Marketing

## Assistant  *(2026-03-07T12:53:21.670086+00:00)*

The user has answered the department question. I still need the remaining details they haven't provided yet. Let me ask for the remaining open-ended details and the style file.Almost there! I just need these last few details — please type them out:

1. **Company name** — as it should appear throughout the report
2. **What the company does** — 2–3 sentences: services offered, customer base, rough scale
3. **Current tech stack** — e.g. Salesforce, SAP, Amdocs, Netcracker, custom CRM (or "unknown")
4. **Known data pain points** — e.g. siloed BSS/OSS data, fragmented customer view, no real-time churn signals (or "unknown")
5. **Geography** — countries or regions where they operate

And whenever you're ready, **please share your style guidelines file** so I can swap out the design section before generating the report!

## Human  *(2026-03-07T12:56:09.934439+00:00)*

Company name is Hrvatski Telekom. Gather details from our website at www.hrvatskitelekom.hr.
Tech stack is unimportant.
Data pain points are unimportant.
Geography is Croatia.
Usecases should be for internal use by sales&marketing to solve a problem, improve efficiency or unlock new market opportunities. Use the attached brand guidelines.

## Assistant  *(2026-03-07T13:06:24.481617+00:00)*

Let me read the brand guidelines file and check the skills directory first.Let me read the brand guidelines and check the skill instructions before I start building.

Let me read the frontend design skill and the docx skill to extract the brand guidelines.

Now let me read the brand guidelines from the uploaded docx file.Now let me extract the brand guidelines from the uploaded file.

The brand guidelines file is a template with empty fields (it uses ____ placeholders). It shows the structure but doesn't have actual filled-in values. However, it does hint at T-Mobile/Deutsche Telekom brand values (magenta #E20074, TeleNeo font). Since Hrvatski Telekom is a Deutsche Telekom subsidiary, I can infer:

- Primary Magenta: #E20074
- White: #FFFFFF
- Dark Burgundy: #6B0038
- Font: TeleNeo (but this isn't available via Google Fonts, so I'll use a close alternative)
- Style: structured, business, high-contrast, minimalistic

- Background: Magenta-white gradient

I can't access the HT website directly, but from what I know, Hrvatski Telekom is Croatia's largest telecom operator and a Deutsche Telekom subsidiary offering mobile, fixed-line, broadband, and TV services. Since TeleNeo isn't available on Google Fonts, I'll need to find a suitable alternative that matches the modern, geometric aesthetic of Deutsche Telekom's branding.

Looking at this template more carefully, it appears to be intentionally blank, and the user has provided it as a starting point. I'll use the standard Deutsche Telekom color palette—magenta #E20074 as the primary color with white accents—and build out the HTML report with a geometric sans-serif font from Google Fonts that approximates TeleNeo's feel. I've settled on Outfit as the typeface for both headings and body text with varying weights to maintain the clean, geometric aesthetic. Now I'm mapping out the ten use cases for Hrvatski Telekom's Sales & Marketing team, focusing on high-impact scenarios like churn prediction, competitive intelligence, and personalized recommendations alongside medium-complexity initiatives around lead scoring and campaign analysis. I'm refining these use cases with more memorable names and clearer business impact—focusing on quick wins that deliver immediate value, medium-term initiatives that build capabilities, and strategic plays that transform the business. The naming convention helps stakeholders immediately grasp what each use case does and why it matters.

Now I'm setting up the HTML with the HT brand palette and building out the visual layout...The brand guidelines file is a blank template — but since Hrvatski Telekom is a Deutsche Telekom subsidiary, I can apply the T-Mobile brand identity (magenta #E20074, structured/high-contrast style, TeleNeo-equivalent typography). Now let me fetch HT's website for company context.

Now I have all the information I need. Let me build the comprehensive HTML report for Hrvatski Telekom Sales & Marketing department.

Key facts about Hrvatski Telekom:
- Croatia's largest telecom operator
- ~2,137 employees (some sources say around 4,000-5,000 with subsidiaries)
- Revenue ~€1.1B (2024)
- ~4 million subscribers total
- 2.5 million mobile subscribers
- 669,000 fixed internet subscribers
- 717,000 fixed telephony subscribers
- Deutsche Telekom subsidiary (51% owned)
- Segments: Residential, Business, Crnogorski Telekom

- Offers mobile, fixed, IPTV, IoT, ICT solutions, and M2M services with strong 5G and FTTH expansion across Croatia's competitive market.

For the design, I'll apply the Deutsche Telekom brand palette—magenta, white, and dark burgundy—with a structured, high-contrast layout using a gradient background and Outfit as the font substitute for the proprietary TeleNeo.

Now I'm mapping out ten use cases for the Sales & Marketing team, starting with three quick wins: a churn prediction system to identify at-risk subscribers before they leave, real-time competitive intelligence to track rival offers as they launch, and a personalized recommendation engine that tailors bundle promotions based on individual customer usage patterns.

Moving into medium-complexity initiatives: consolidating fragmented B2B sales pipelines across enterprise accounts, harmonizing customer data across the mobile, fixed-line, and IPTV systems into a single unified profile, building attribution models that track which marketing touchpoints actually drive conversions across all channels, and developing a contract renewal forecasting system for B2B accounts.

Then the strategic-tier opportunities: building scenario planning tools for pricing and portfolio decisions instead of manual Excel modeling, tracking the carbon footprint of different marketing channels to support ESG commitments, and orchestrating seamless omnichannel journeys when customers upgrade services across product lines.

Building the HTML interface now with the brand colors and typography...I have everything I need. Now let me build the full report.

The report is ready. Here's what's inside:

**10 use cases built specifically for HT Sales & Marketing**, grounded in HT's actual subscriber base (~4M), competitive landscape (A1, Telemach), and Croatian market context (HAKOM, FINA, Sudski registar, OIB):

| # | Name | Type |
|---|------|------|
| 01 | The Churn Whisperer | ⚡ Quick Win |
| 02 | The Signal Scanner | ⚡ Quick Win |
| 03 | The Offer Architect | ⚡ Quick Win |
| 04 | The Pipeline Oracle | 🔧 Medium-Term |
| 05 | The Golden Profile | 🔧 Medium-Term |
| 06 | The Campaign Analyst | 🔧 Medium-Term |
| 07 | The Renewal Radar | 🔧 Medium-Term |
| 08 | The Revenue Compass | 🚀 Strategic |
| 09 | The Green Channel | 🚀 Strategic |
| 10 | The Journey Architect | 🚀 Strategic |

**Brand applied:** HT Magenta (#E20074), high-contrast dark theme, structured layout aligned with Deutsche Telekom brand identity — no playful or overly animated visuals as per the style guidelines.

**Interactive features:** filter by complexity, collapsible cards, expandable architecture detail tables, hover tooltips on all MCP integrations, sticky navigation with active section tracking.
