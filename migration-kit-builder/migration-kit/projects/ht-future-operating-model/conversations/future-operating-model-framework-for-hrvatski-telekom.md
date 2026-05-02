# Future operating model framework for Hrvatski Telekom
- **Conversation ID:** `ce45c427-3192-4216-9169-8cbdc2f254d6`
- **Created:** 2026-03-26T14:34:11.452387+00:00
- **Updated:** 2026-04-01T13:55:34.090517+00:00
- **Messages:** 24

---

## Human  *(2026-03-26T14:34:12.675360+00:00)*

Create a puzzle-style visualization using the attached telco operating map. The goal is to create a simplified framework for creation of the Future Operating Model for Hrvatski Telekom. Use the domains customer, market&sales, product, service, resource and focus on the capability management, business value development, operations readiness & support and fulfillment areas.

## Assistant  *(2026-03-26T14:36:32.384330+00:00)*

The user wants me to create a puzzle-style visualization based on the eTOM framework, focused on specific domains and areas for Hrvatski Telekom's Future Operating Model. Let me plan this out.

Domains to include: Customer, Market & Sales, Product, Service, Resource
Areas to focus on: Capability Management, Business Value Development, Operations Readiness & Support, Fulfillment

Let me read the visualizer readme first to understand the design guidelines.

The user wants a puzzle-style interactive visualization of the eTOM framework for Hrvatski Telekom's Future Operating Model. Let me plan this carefully.

Domains (rows): Customer, Market & Sales, Product, Service, Resource
Areas (columns): Capability Management, Business Value Development, Operations Readiness & Support, Fulfillment

This is a 5x4 grid = 20 cells. Each cell should contain the key process groups from the eTOM framework. I need to make this interactive and "puzzle-style" - meaning interlocking pieces or a jigsaw-like visual.

Let me think about what goes in each cell based on the eTOM framework:

Now I'm mapping out the specific process groups for each domain. The Customer domain covers management capabilities, strategy and relationship development, support operations, and order processing. Market & Sales includes sales development and market research for capability building, marketing campaigns and communications for value creation, readiness support, and the actual selling and lead management processes. The Product domain starts with development and specification capabilities.

I'm thinking about how to visualize this as an interactive puzzle where each piece represents one of these process areas, and users can click through to explore the details and relationships between them.

Building the interactive widget...Robi, this is a great framework exercise. Let me build a puzzle-style interactive visualization mapping the eTOM process areas to HT's future operating model — focusing on the five core domains across your four selected lifecycle phases.

The visualization is rendered. Let me provide a brief explanation of the structure and how to use it.The puzzle maps eTOM v24.5 process areas into a 5×4 grid that reads left-to-right as the operating lifecycle — from strategic capability build-out through to live fulfillment. Each piece is clickable and expands with AI opportunity areas specific to HT's context.

A few structural observations worth noting for the working session:

The **vertical integration** is where the real operating model design happens — a customer order triggers product fulfillment, which decomposes into service activation, which dispatches resource orders. That cascade across the five rows is where zero-touch ambitions either work or break down.

The **capability management column** (leftmost) is where your AI Tribe has the most strategic leverage — it's pre-operational, so you're shaping future capabilities before they hit production. The **fulfillment column** (rightmost) is where AIOps delivers the fastest measurable ROI, especially in the service and resource layers.

The middle two columns — business value development and operations readiness — are the connective tissue that most telcos underinvest in. That's typically where catalog quality, spec accuracy, and support tooling either enable or block the automation ambitions at both ends.

Want me to drill into any specific piece, or would it help to layer on a priority/maturity overlay showing where HT currently stands versus the target state?

## Human  *(2026-03-26T14:36:47.874946+00:00)*

Group the Service and Resource domains into Network domain

## Assistant  *(2026-03-26T14:38:45.739347+00:00)*

Robi wants me to merge the Service and Resource rows into a single "Network" domain. This simplifies the framework from 5 rows to 4 rows. I need to rebuild the puzzle visualization combining the service and resource process areas under one unified "Network" domain.

Good, the visualization is rendered. Let me provide context on the merge decision.Done — Service and Resource are now unified under a single **Network** domain, with each puzzle piece preserving the two-layer internal structure via the dashed divider (service layer above, resource layer below).

This grouping makes practical sense for HT's operating model because the organizational reality is that network teams already operate across both eTOM layers — a NOC engineer doesn't think "I'm doing service performance management now" vs "resource trouble management." The dashed line inside each piece keeps the logical distinction visible for process mapping purposes without inflating the model to five rows.

The 4-domain model also maps more cleanly to HT's actual org structure: Customer-facing teams, Commercial/Sales teams, Product management, and Network/Technology. That's a more intuitive framework for a Board-level conversation than the purist eTOM five-layer split.

Want me to add a maturity or priority overlay, or export this as a standalone HTML deliverable you can use in the working session?

## Human  *(2026-03-26T14:40:39.705265+00:00)*

createa a Standalone HTML I can share, and please use the Telekom branding for styling, with a white background

## Assistant  *(2026-03-26T14:43:13.342930+00:00)*

The user wants a standalone HTML file with Deutsche Telekom branding (magenta theme) and white background. Let me read the relevant skill file for creating HTML files, then build a polished standalone version.

Now let me create a standalone HTML file with Deutsche Telekom branding. The key Telekom brand elements are:

- Magenta (#E20074) as primary color
- White background
- TeleNeo or similar font (I'll use a clean sans-serif since TeleNeo isn't publicly available on CDN)
- Clean, corporate feel
- The "T" logo mark

Let me build this as a polished standalone HTML file.

Let me copy it to outputs and present it.

Done, let me present the file.

Done.Here's your standalone HTML file with Telekom branding — white background, magenta accents on the header/footer borders, DM Sans typography, and the T-logo mark. It's fully self-contained with no external dependencies beyond the Google Font, so it works offline after first load.

The interactive click-to-expand panels work the same way as the inline version. It also includes print styles that auto-expand all detail panels when you print or export to PDF, and it's responsive down to tablet widths.

## Human  *(2026-03-26T14:45:05.498886+00:00)*

can you style the domains in a puzzle-like grid of 2x2, with the lifecycle expanding in a circle-like structure? Also, can you simplify the descriptions in the overview into 1 sentence per domain so it's easy to read and understand, with the details available on click?

## Assistant  *(2026-03-26T14:53:46.268577+00:00)*

The user wants a redesign of the HTML file with:
1. Domains arranged in a 2x2 grid (Customer, Market & Sales, Product, Network)
2. Lifecycle phases expanding in a circle-like structure around each domain
3. Simplified descriptions - 1 sentence per domain in the overview
4. Details available on click

This is a significant visual redesign. Let me think about the layout:

- 2x2 grid of domains: Customer (top-left), Market & Sales (top-right), Product (bottom-left), Network (bottom-right)
- Each domain is a "hub" with 4 lifecycle phases radiating outward in a circular/radial arrangement

- Each hub displays just the domain name and a single sentence summary, with the full lifecycle details hidden until clicked

I'm considering how to structure this interactively. A fully circular layout for each of the four domains might get visually crowded, so I'm thinking of a cleaner approach where each domain card acts as a central hub that expands on click to reveal its four lifecycle phases arranged around it.

Actually, I like the idea of a 2x2 grid where each quadrant represents a domain, with the domain name and description centered and the four lifecycle phases positioned around it in a clockwise circular flow. This creates a more cohesive puzzle-like visual where the phases naturally orbit the domain center—Capability Management at the top-left, Business Value Development at the top-right, Operations Readiness & Support at the bottom-right, and Fulfillment at the bottom-left.

For the interaction pattern, I'm thinking the main view shows a clean 2x2 grid of domain tiles with the name, a brief description, and a subtle visual indicator of the four phases. When a user clicks a domain, it expands to reveal the full circular lifecycle arrangement where each phase becomes clickable for detailed AI opportunities.

Building the visual structure... Building the interactive layout... Building the layout...

Let me design a really polished 2x2 grid where each domain is a circular hub. The lifecycle phases orbit around each domain center in a clockwise pattern. I'll use SVG for the circular arrows and position the phases at cardinal points.

Design direction: Clean, corporate-editorial with Telekom magenta as the accent. White background, generous whitespace, each domain as a self-contained circular system. Think of it like 4 orbital diagrams in a 2x2 grid.

Each domain hub:
- Center: Domain name + 1-sentence description
- N (top): Capability Management

- E (right): Business Value Development
- S (bottom): Operations Readiness & Support
- W (left): Fulfillment

The clockwise flow connects them: Capability Management → Business Value Development → Operations Readiness & Support → Fulfillment → back to start. I'm sizing each domain cell at roughly 550px × 450px and building the layout with SVG circles, orbital paths, and connecting arrows.

For the interaction model, clicking a phase card will display a detail panel below showing the relevant process items and AI opportunity tags. Now I'm working through the geometry of the connecting arrows—I need to draw curved paths between the phase positions that flow clockwise around the center hub, though the bottom-left transition requires some careful positioning to avoid awkward angles. Writing SVG arrow paths...

Actually, I'm reconsidering the whole approach here. Since this needs to work across different screen sizes, I should make each hub a flexible container with the center domain label and position the phase cards around it using absolute positioning, then layer SVG arrows on top for the connections. Let me simplify the sizing—I'll use a responsive container with consistent proportions for the center circle and phase cards, keeping the arrow track at a fixed radius from the center.

For the layout itself, I'm thinking a 3×3 CSS grid where the corners stay empty, the center holds the domain name, and the cardinal directions hold each phase. Then I'll overlay curved SVG arrows between adjacent phases to show the flow. The detail panel will sit below the 2×2 grid and slide in when someone clicks a phase.

I'm going to stick with the Telekom magenta and white palette, using DM Sans throughout. For the circular flow visualization, I could either draw subtle curved arrows in SVG or use a dashed circle with chevrons—I think the SVG arrows will look cleaner and more intentional.

Writing the HTML structure... I'm realizing grid layout might be too constraining for the circular arrangement I want, so I'll switch to absolute positioning instead—that'll give me precise control over placing each phase at the cardinal directions around a centered hub. I'm setting up the container with relative positioning, the center element absolutely centered, and each phase positioned at the north, east, south, and west points, with an SVG overlay for the connecting arrows.

Now I'm planning the overall page structure: a header with the logo and title, a 2x2 grid of domain hubs below it, each with its own circular lifecycle, a detail panel area, and a footer. For the arrows between phases, I'll use SVG with curved bezier paths to create a subtle clockwise flow, and I'll add a staggered entrance animation when the page loads.

Each hub will have the domain name in a colored circle at the center with a description underneath, four phase cards positioned at the cardinal directions, and SVG arrows connecting them. Clicking any phase will display details below. I'm working out the precise positioning now—each hub is roughly 500×420 pixels, with the center at (250, 210) and the phase cards positioned at the cardinal points. The cards themselves will be consistent at 130 pixels wide and about 56 pixels tall.

Writing the component structure... I'm simplifying the approach—instead of manually calculating bezier curves between card edges, I'll draw a dashed circular track around the center point and place small arrow chevrons at intervals to show clockwise flow. The phase cards themselves will be positioned via CSS at the cardinal points on this circle, while an SVG overlay handles the track and directional indicators. Writing SVG arrow paths...

Now I'm thinking through the interaction model—when someone clicks a phase card, I'll highlight it and display a detail panel below the grid showing the process items and AI opportunities for that phase.

I'm finalizing the domain descriptions to be concise yet comprehensive, then I'll write out the complete HTML structure. For the layout, I need to size the 2x2 grid cells to fit within the max-width constraint while keeping the phase cards compact and positioned around each domain.

Writing the HTML structure... Writing positioning styles...

I need to set up the SVG with a fixed viewBox that scales with the container, then map out the phase positions and curved arrow paths that connect them in a clockwise flow around the hub.

Now I'm defining the specific arrow paths with quadratic curves to create smooth quarter-circle arcs between each phase, and I'll add arrow markers to show direction. I'm also planning to give each domain hub a subtle colored background that matches its theme, creating that puzzle-piece effect where the four quadrants fit together visually.

For the responsive layout, I'm thinking through whether to use SVG with viewBox scaling or CSS pseudo-elements for the arrows—I'm leaning toward keeping the arrows as part of a background SVG so everything scales proportionally together.

Actually, I'm overcomplicating this. Let me just use fixed dimensions that work well on desktop since that's the primary viewing context, and I can make it scrollable on smaller screens if needed. I'll set up a grid with two columns, no gap between cells, and position each hub with a fixed height so the phase cards and arrows can be absolutely positioned within them.

Setting up the layout structure... Building the grid layout... Writing SVG coordinate system... I'm scrapping the SVG approach entirely and going with pure CSS instead. I'll create a dashed circular orbit using a positioned div with a border, place the four phase cards around it at cardinal directions, and add small arrow indicators as CSS triangles to show the flow between phases.

Styling the orbit ring... Writing SVG arrow paths... Writing the SVG and animations... Defining the clip-path patterns for the interlocking edges... Finishing the clip-path polygons for the remaining tab configurations, defining the precise coordinates for the inward and outward notches on each edge.

Actually, I'm overcomplicating this with the negative values and complex polygon calculations—browsers might struggle with the rendering. Let me simplify by using a 2x2 grid layout with minimal spacing and rounded corners applied only to the outer edges of each cell, which will give that puzzle-piece aesthetic without the geometric complexity. I'll use distinct background colors for each quadrant to reinforce the four-part operating model concept.

Now I'm ready to write the actual code. For the arrows connecting these pieces, I want them thin and semi-transparent with a dashed style, small arrowheads, and maybe a flowing dash animation to emphasize the lifecycle progression through the model.

Writing the HTML and CSS... Writing the complete HTML structure...

Now I'm thinking through the SVG arrow markers—I need arrowheads on those curved arrows pointing outward from each hub. The cleanest approach is to define the marker once in a hidden SVG at the top of the page, then reference it from each hub's individual SVG elements rather than duplicating it in every hub.

For the flowing animation effect on the arrows, I'm setting up a keyframe animation that shifts the stroke dash offset to create that sense of movement along the path.

Now I'm organizing the content for all the phase-domain combinations into a data structure so the code stays clean and maintainable. I'll hardcode the detail panels directly in the HTML with matching IDs for reliability, then focus on building out the phase cards with their titles and key bullet points for the simplified view. Now I'm mapping out the remaining domains—Sales and Market with their four directional capabilities, Product with its full lifecycle from development through operations, and Network as the foundational service layer supporting everything else.

For the phase labels, I'm considering whether to embed them directly in each card or position them as global axis labels across all four hubs. I think keeping them self-contained within each card works better—that way every phase card shows both the lifecycle phase name and the domain-specific activities it encompasses.

I'm settling on a compact format where the domain title sits prominently at the top with the lifecycle phase as a smaller, muted subtitle below it, giving context without bloating the card size.

Now I'm ready to build the HTML file, and I need to finalize the hub dimensions—each hub around 545px wide with 440px height, phase cards at roughly 125px, and a 150px center circle. I'll also add a close button to the detail panel and style the active phase card with a highlight.

Building the interactive layout... Writing SVG arrow paths... Writing SVG arc paths... Writing SVG code... I'm verifying the arrow coordinates are correct, and they look good—I'll use clockwise small arcs for the SVG paths. Now I need to make sure the CSS positioning of the phase cards aligns with the SVG viewBox coordinates so everything renders in the right proportions.

Calculating card positions...

I'm realizing the scaling issue—when the container width changes, the viewBox units don't map 1:1 to pixels anymore, so the SVG arrows won't align with the HTML cards. The simplest fix is to lock the hub to a fixed 500px × 420px size, which makes the viewBox scale predictable for a presentation context.

But actually, I'm overthinking this. Instead of wrestling with SVG-to-HTML alignment, I'll use a cleaner approach: position the phase cards with CSS and draw a subtle circular orbit ring behind them with small arrow indicators at key angles, skipping the complex arrow-positioning math entirely.

Positioning the chevron arrows...

CSS doesn't support trigonometric functions in calc() reliably, so I'll hardcode the positions instead. For a 140px radius ring, the cardinal offsets work out to roughly 99px, which I can use to place the chevrons at the four diagonal points around the ring. Writing SVG overlay... I need to recalculate the SVG coordinates to account for the card's transform origin—the CSS percentage positions place the card's top-left corner, but I need to find where the card's center actually lands in the SVG viewBox so the arrows connect properly. Now I'm calculating the positions for the remaining cards and realizing the orbit isn't a perfect circle—the north and south cards are 176 pixels from the hub center while the east and west cards are 197 pixels away, so I'll need to draw an ellipse instead.

Let me adjust the card positions to create a more balanced orbit by increasing the vertical padding for the north and south cards while keeping the horizontal padding tighter for east and west. After recalculating with these new percentages, the distances are closer but still not perfectly equal—north and south are 167 pixels out while east and west are 176 pixels out.

Now I'm setting up the SVG arrows to follow an elliptical path with those dimensions, calculating the start and end points for each directional arrow based on angles around the ellipse.

Calculating arrow paths... I'm finishing up the arc calculations for the elliptical paths connecting the phase cards, then I'll add arrowheads with SVG markers. Now I'm moving into the actual implementation—I'll structure the detail panel below the grid and use a JavaScript data object to store all the content for each phase, keeping it clean and organized.

Writing the component code...

For the animations, I want the hub cells to fade in with a stagger effect, the phase cards sliding in from their cardinal directions, and the arrows drawing themselves in smoothly. I'm also adding lifecycle phase labels at each position—capability management to the north, value development to the east, readiness and support to the south, and fulfillment to the west—as small, muted subtitles on each card to give context without cluttering the design.

The phase cards themselves will be clean and compact, showing the phase label in uppercase, a bold domain title, and a few key items listed below. When clicked, a detail panel expands to show the full breakdown with AI tags. I'm keeping the cards as simple rounded rectangles rather than adding puzzle-piece notches, since the puzzle metaphor already comes through from how the four domains fit together conceptually.

Writing the component code... Writing SVG positioning logic...

Now I need to handle the grid layout for the hub cells—I'll use a 2x2 grid with a minimal 2px gap that acts as a subtle border between them, letting the background show through for that puzzle-piece feel. Each cell will contain its domain information.

I'm realizing the SVG arrows need to stay perfectly aligned with the CSS layout regardless of how the hub scales, so I'm verifying that the proportional math works out—since the viewBox aspect ratio matches the container's aspect ratio, percentage-based CSS positions will translate directly to SVG coordinates.

Writing the final implementation... Calculating the arc paths for each transition around the orbit...

Now I'm defining the marker for the arrowheads, but I realize CSS variables won't work in SVG marker fills, so I'll need to use actual color values instead. I'm realizing that since all the SVGs are embedded in the same HTML document, they share the DOM, so I need unique marker IDs across all hubs rather than reusing the same ID. Let me prefix each marker with its hub identifier like "ah-c" for one hub and "ah-m" for another.

Actually, a cleaner approach would be to define a single shared marker in a hidden SVG at the top of the page, then reference it from all the visible hub SVGs using cross-SVG references, which work fine in modern browsers.

Now I'm organizing the full implementation into sections: CSS variables, base styles, header, hub grid, phase cards, detail panel, animations, HTML structure, and JavaScript. Before I start writing though, I need to decide what information shows on the phase cards themselves—the user wants simplicity with details on click, so I'll keep each card minimal with just the lifecycle phase label and the domain-specific title.

Writing the complete code now... Writing the complete implementation... Writing the comprehensive HTML file...

Let me copy it to outputs and present it.

Let me present the file to the user.

Done. Let me provide a brief summary.Here's the redesigned version. The key changes:

**2×2 puzzle grid** — Customer (top-left), Market & Sales (top-right), Product (bottom-left), Network (bottom-right) fit together as four colored quadrants with a tight 3px border creating the puzzle effect.

**Circular lifecycle** — Each domain has four phase cards orbiting the center in a clockwise flow: Capability Management (top) → Value Development (right) → Readiness & Support (bottom) → Fulfillment (left). Animated dashed arcs with arrowheads show the lifecycle direction.

**Simplified overview** — Each domain center shows just the name and one sentence. Phase cards show only the lifecycle stage and a domain-specific title. Clean and scannable at a glance.

**Details on click** — Clicking any phase card opens a detail panel below the grid with two columns: process areas (left) and AI opportunity tags (right). Network phases show the Service/Resource sublayer breakdown. A magenta ring highlights the active selection.

The file is fully standalone with the Telekom branding (magenta accents, T logo, DM Sans typography, white background) and includes entrance animations on load.

## Human  *(2026-03-31T08:38:05.429712+00:00)*

You are a world-class strategist and organizational expert, with deep insights into futurology, philosophy and technology. I want to define a top-down approach for Future target operating model definition for Hrvatski Telekom 2030.+ -> some guidelines are: 2M mobile customers, 1M fixed customers (across fiber, satellite and FWA technologies) and significant new business models beyond the core. We want to be completely digital company, with channel shares on digital 95%, <5% physical stores and 0% other channel sales. We want to have 100% of 1st level support handled by AI, and all company operations with zero-touch processes handled by AI. Our telco products should be fully digital. Ask me additional questions to understand the vision, then lay out a plan for the top-down approach

## Assistant  *(2026-03-31T08:38:37.927581+00:00)*

Robi is asking me to help define a top-down Future Target Operating Model for Hrvatski Telekom 2030+. He's given me some key parameters already. Let me think about what I need to understand better before laying out the plan.

Key parameters already shared:
- 2M mobile customers, 1M fixed customers (fiber, satellite, FWA)
- Significant new business models beyond core
- 100% digital company: 95% digital channels, <5% physical stores, 0% other
- 100% 1st level support = AI
- All operations = zero-touch AI
- Fully digital telco products

What I need to understand better to define a proper top-down TOM:

Before I can map out the full operating model, I need clarity on several critical dimensions: the revenue ambition from new business lines and which models they're prioritizing (B2B2X, IoT, data monetization, edge computing, fintech), the workforce transformation target and current headcount baseline, and their technology strategy around cloud-native architecture and whether they'll leverage DT group platforms or build independently. I also need to understand their B2B versus B2C positioning, their network ownership philosophy (own infrastructure versus wholesale/MVNO), the regulatory and convergence context they're operating in, and how Pluto and their data platform fit into the overall model, plus their partnership strategy.Great brief, Robi. Before I lay out the framework, I need to pressure-test a few dimensions that would fundamentally shape the TOM differently depending on the answer. Let me group these into the areas that matter most.

Good, I've asked the structured questions. Now let me also ask some open-ended questions that are important for the TOM definition.And a few open-ended questions that will shape the organizational and capability layers:

**Workforce & org structure** — What's the current headcount ballpark, and is there a target envelope for 2030? Are you envisioning a continuation of the tribe/squad model, or a more radical restructuring? How much autonomy does HT have from DT group on org design?

**DT group dependency** — For the TOM, how tightly coupled should HT be to DT group platforms (IT, BSS/OSS, procurement)? Is there appetite to diverge where it makes strategic sense, or is group alignment non-negotiable?

**B2B ambition** — The 2M mobile / 1M fixed numbers feel consumer-heavy. What's the B2B/B2C revenue split target? Is there a dedicated enterprise/ICT play, or does B2B run through the same operating model?

**Pluto's role** — Should the data platform be positioned as internal enabler only, or is there a data-as-a-product / data monetization angle that should be architecturally baked into the TOM from day one?

These answers will determine whether the TOM looks more like a "lean digital telco" or a "platform company that happens to own a network" — two very different target states with different capability requirements, cost structures, and talent models.

## Human  *(2026-03-31T08:40:53.359246+00:00)*

Q: Revenue ambition 2030+ — what share of total revenue should come from beyond-core business models (IoT/B2B2X, data monetization, edge, digital services, etc.)?
A: <10% — core telco dominates

Q: Network ownership model — how do you see HT's infrastructure position in 2030?
A: Full owner-operator (build & run everything)

Q: Which of these are genuine 2030 ambitions vs aspirational stretch targets? (select all that are firm commitments) (Select all that apply)
A: 95% digital channel share, 100% AI 1st-level support, Zero-touch operations, Fully digital products (no manual provisioning)

## Assistant  *(2026-03-31T08:41:16.987914+00:00)*

Robi has given me clear answers. Let me synthesize:

1. Revenue: Core telco dominates (<10% beyond-core) — this is a "lean digital telco" not a platform company
2. Network: Full owner-operator — they own and run everything
3. All four targets are firm commitments, not stretch goals

He hasn't answered the open-ended questions yet about workforce, DT group dependency, B2B, and Pluto. Let me ask those as follow-ups before laying out the plan.

Actually, let me re-read his message. He answered the widget questions but not the open-ended ones I asked in prose. I should follow up on those before proceeding, as they're critical for the TOM design.

I'll structure the remaining questions clearly so I can get the answers I need to move forward with the design.Good — that's a very clear signal. You're building a **lean digital telco that owns its infrastructure and runs it with radical automation**, not a platform pivot. All four targets being firm commitments means the TOM needs to be engineered backward from those end states, not iterated toward them incrementally.

I still need the open-ended answers to lock in the organizational and capability layers. Let me sharpen them based on what you've told me:

Waiting for Robi's answers to these questions.And two final open-ended questions that I can't widget-ify:

**Workforce envelope** — What's the current headcount range (rough is fine), and is there a target for 2030? The zero-touch commitment implies significant workforce reshaping — I need to know whether you're designing for 50% of current headcount, 70%, or "same headcount, radically different skills."

**Organizational model** — Do you see the tribe/squad model surviving into 2030, or is the TOM an opportunity to rethink the operating structure entirely? And how much of the org design is HT's call vs DT group mandate?

These are the last inputs I need. Once I have them, I'll lay out the full top-down approach — starting from the 2030 end-state vision and decomposing backward through capability architecture, operating model layers, transition phases, and the governance needed to get there.

## Human  *(2026-03-31T08:41:53.446066+00:00)*

Q: B2B vs B2C revenue split target for 2030 — where does the weight sit?
A: ~55/45 balanced (enterprise is a growth lever)

Q: DT group platform coupling — how much freedom does HT have on IT/BSS/OSS stack choices?
A: Selective autonomy (can diverge with business case)

Q: Pluto's strategic position in the 2030 TOM — what role does the data platform play?
A: Data-as-a-product (internal + external monetization)

## Assistant  *(2026-03-31T08:43:47.058971+00:00)*

Robi has given me comprehensive answers. Let me synthesize everything before laying out the plan:

**Vision summary:**
- Lean digital telco, full infrastructure owner-operator
- 2M mobile, 1M fixed (fiber/satellite/FWA)
- <10% beyond-core revenue (core telco dominates)
- 55/45 B2C/B2B split (enterprise as growth lever)
- All four digital targets are FIRM commitments: 95% digital channels, 100% AI L1 support, zero-touch ops, fully digital products
- Selective autonomy from DT group
- Pluto as data-as-a-product (internal + external monetization)

- He's sidestepped the workforce envelope and org model questions, but he's clearly ready for the plan, so I'll proceed with reasonable assumptions I can flag as gaps.

Now I'm thinking through what a world-class strategic framework should look like—starting with a 2030+ end-state vision, then layering in design principles, capability architecture, operating model structure, transition roadmap, and governance. I could jump straight into building a comprehensive Board-level HTML deliverable, but it makes more sense to walk through the approach conversationally first to get alignment before investing in the full production.

The real strategic challenge here is that HT wants to be capital-intensive on infrastructure but operationally lean through automation—that's the core tension I need to resolve. The operating model has to handle two completely different capability profiles: the infrastructure side is engineering-heavy and long-cycle, while operations and commercial functions need to be AI-native and run with minimal human intervention. And there's something compelling about the Pluto angle—treating data as a product that drives core telco revenue.

Now I'm seeing how Pluto actually functions in this model: it's not a standalone revenue center but rather the connective tissue that strengthens the core business while creating strategic optionality. The 55/45 B2B/B2C split with enterprise as the growth engine means I can't design this as a pure consumer-digital operation. Enterprise customers need different fulfillment—complex, multi-service, SLA-driven—plus relationship-based sales and dedicated support. The "95% digital" aspiration works differently here; for enterprise it means APIs, portals, and self-service dashboards rather than just a mobile app. And the selective autonomy from DT is crucial—I need to map out which parts of the TOM are HT-sovereign and which stay group-aligned, because that distinction directly affects implementation feasibility.

I'm going to structure this as a comprehensive top-down framework starting with the north star, then the strategic design principles that constrain everything downstream, followed by the capability architecture organized around the four domains, and finally the operating model itself.

The operating model has six critical layers—governance, commercial, product, technology, data, and people—that all need to work in concert. Then I'll map out the transition architecture with three clear horizons and milestones, and finish with the governance framework that actually makes decisions stick.

The real insight here is the zero-touch paradox: moving to zero-touch operations doesn't reduce your total talent needs, it just shifts them from operators to engineers. Most telcos cut headcount first and then realize they can't build the automation they need. And that 95% digital channel with a 55/45 B2B split is deceptively complex—it's not just a channel strategy, it's a fundamental reshaping of how the business operates.

Enterprise digital means API-first platforms, self-service configuration for bundled services, and automated SLA negotiation. That's a completely different beast than B2C digital. When you combine full owner-operator responsibility with radical automation, you're essentially building a lights-out factory—the infrastructure still exists and still requires capital, but it runs with minimal human touch. And for data monetization in this model, Pluto becomes the intelligence backbone that makes every business line smarter, not a separate P&L chasing its own revenue.

The tension here is that DT group platforms move at group speed, but HT's automation ambitions need to move faster. I need to design the TOM with explicit decoupling—APIs and abstraction layers that let HT innovate on top of group foundations without fragmenting them.Excellent. The picture is now sharp enough to build on. You haven't answered the workforce and org model questions yet — I'll flag where those answers would change the plan, but I have enough to lay out the full architecture.

Let me also note: you've described something that has a very specific strategic shape. Let me name it before I unpack it.

---

## What you're actually building

You're describing a **lights-out telco** — borrowing the manufacturing metaphor where the factory still exists, is still capital-intensive, and still produces physical output, but runs with minimal human intervention. The assets are heavy; the operations are radically light. This is rare in European telecoms. Most operators either go asset-light (sell the network) or stay operationally heavy (keep the people). You're choosing the harder third path: own everything, automate everything.

That framing matters because it resolves what would otherwise be a contradiction — how can you be a full owner-operator AND have zero-touch operations? The answer is that infrastructure ownership becomes a capital allocation discipline, not an operational one. You build and maintain through engineering and AI, not through headcount.

The second thing worth naming: Pluto as data-as-a-product in a core-dominated revenue model doesn't make Pluto a business unit — it makes it the **nervous system** of the entire operating model. Every zero-touch process, every AI-handled support interaction, every automated provisioning flow depends on data quality, data availability, and data intelligence. The external monetization is a proof point for the platform's maturity, not the primary business case.

Now let me lay out the approach.

---

## Top-down TOM design framework: six layers

The design works backward from the 2030 end-state through six layers, each constraining the one below it. I'll walk through the logic of each, then we can build the detailed deliverable.

### Layer 1 — North star codification

Before anything gets designed, the end-state needs to be locked down in language that's precise enough to make architectural decisions against. Not vision statements — **design constraints**. What you've given me translates to seven hard constraints:

**The magnificent seven** (these are non-negotiable end-state requirements):
1. 3M customer relationships (2M mobile + 1M fixed) across fiber, satellite, and FWA
2. 95% digital channel revenue share (B2C via app/web, B2B via portal/API)
3. 100% AI-handled first-level support (zero human escalation at L1)
4. Zero-touch operations across provisioning, assurance, and billing
5. Fully digital products (no manual provisioning or configuration)
6. Full infrastructure ownership across all access technologies
7. 55/45 B2C/B2B revenue balance with enterprise as the growth vector

Each of these has second-order implications that cascade through the operating model. For instance, constraint #2 (95% digital) applied to constraint #7 (55/45 with enterprise growth) means you need an enterprise digital commerce platform that handles complex multi-service B2B deals through self-service — not just a consumer app. That's a fundamentally different capability than most telcos' "digital transformation."

### Layer 2 — Strategic design principles

These are the guardrails that govern every downstream decision. I'd propose eight, derived from your constraints:

**P1: AI-native, not AI-augmented.** Every process is designed for autonomous execution first. Human involvement is the exception that requires justification, not the default that gets optimized away. This is the difference between "let's add a chatbot" and "let's design support so it doesn't need humans."

**P2: API-first commercial architecture.** Both B2C and B2B channels consume the same product/service APIs. The app, the web portal, the enterprise self-service platform, and the remaining physical stores are all thin clients on top of a common digital commerce layer. This is the only way to reach 95% digital without building four separate channel stacks.

**P3: Data is infrastructure, not a function.** Pluto isn't a team that produces reports — it's the substrate that every operational process runs on. The TOM should treat data pipelines with the same criticality as network links.

**P4: Group-aligned foundations, HT-sovereign intelligence.** Use DT group platforms where they provide commodity capability (billing, core network, procurement). Diverge where HT's automation and AI ambitions require faster iteration — primarily in the AI/ML layer, the digital experience layer, and the data platform. This means explicit architectural decoupling points (APIs, abstraction layers) that let HT innovate without forking group systems.

**P5: Engineering over operations.** The workforce profile shifts from "people who run things" to "people who build things that run themselves." Every operational role should have an engineering counterpart that automates it — and the TOM should measure the ratio.

**P6: Segment-native, not segment-adapted.** B2C and B2B aren't the same operating model with different frontends. They have different fulfillment complexity, different SLA structures, different sales motions. The TOM should have shared foundations (network, data, core IT) but segment-specific commercial and fulfillment layers.

**P7: Product simplicity as a design constraint.** Fully digital products require radically simple product architecture. If a product can't be configured, provisioned, and supported without human intervention, it shouldn't exist in the portfolio. This is the most culturally difficult principle — it means killing legacy products, not just digitizing them.

**P8: Closed-loop everything.** Every operational domain (network, service, product, customer) runs a closed loop: sense → decide → act → learn. The zero-touch commitment requires autonomous feedback loops, not just automation of individual steps.

### Layer 3 — Capability architecture

This maps directly to the four-domain model we already built (Customer, Market & Sales, Product, Network), but now organized around **capability clusters** rather than process areas. Each cluster is a bundle of capabilities that must exist as a coherent unit.

I'd structure this as **12 capability clusters across 3 tiers**:

**Tier 1 — Customer-facing (visible to the market)**
- Digital commerce engine (B2C + B2B channels, product catalog, ordering)
- AI customer operations (L1 support, proactive service, bill management)
- Enterprise solutions delivery (complex B2B fulfillment, managed services, SLA)
- Commercial intelligence (campaigns, personalization, churn, pricing)

**Tier 2 — Product & service (the factory)**
- Digital product factory (product lifecycle, catalog, configuration)
- Service orchestration (activation, assurance, performance, closed-loop)
- Network automation (resource provisioning, fault management, capacity)
- Field operations (the residual physical layer — installs, repairs, satellite)

**Tier 3 — Foundational (the substrate)**
- Data & intelligence platform (Pluto — the nervous system)
- Core IT & BSS/OSS (billing, CRM, inventory — group-aligned where possible)
- Cybersecurity & trust (NIS2, privacy, identity, zero-trust)
- People & organizational capability (engineering talent, AI literacy, culture)

### Layer 4 — Operating model blueprint

This is where the TOM gets concrete. Six operating model dimensions, each designed against the principles above:

**Governance model** — How decisions are made. Dual-speed: strategic decisions (investment, architecture, partnerships) on a quarterly cycle; operational decisions (automation deployment, model updates, incident response) on a continuous/real-time cycle. The Board governs outcomes and constraints; the operating model governs itself within those constraints.

**Commercial model** — How value is captured. B2C runs as a high-volume digital machine (app-first, self-service, AI-driven retention). B2B runs as a solution engine (portal + API + enterprise sales, with AI-assisted configuration and dedicated account management for top accounts only). Shared product catalog, divergent go-to-market.

**Delivery model** — How products reach customers. Fully automated for standard products (order → provision → activate in minutes). Semi-automated for complex B2B (AI-assisted design → automated provisioning → human QA for enterprise SLA). The split between "fully automated" and "semi-automated" defines the residual human workforce in fulfillment.

**Technology model** — How the stack is structured. Three layers: group-aligned foundation (core network, billing, ERP), HT-sovereign intelligence (Pluto, AI/ML, digital experience), and edge/access (fiber, satellite, FWA — owned and operated). The decoupling between group and sovereign layers is the single most important architectural decision.

**Data model** — How intelligence flows. Pluto as the single integration layer. Every operational system writes to Pluto; every AI/automation system reads from Pluto. External data products (anonymized, aggregated) as a revenue stream and a proof point. The data model isn't a department — it's an architectural pattern that every domain must implement.

**People model** — How the organization is shaped. This is where I need your workforce envelope answer. But directionally: radical shift from operations roles to engineering roles. The residual operations workforce is concentrated in field services (physical installs, repairs) and enterprise solution design (complex B2B). Everything else is either automated or handled by engineers who build/maintain automation.

### Layer 5 — Transition architecture

Three horizons, working backward from 2030:

**Horizon 1 (2025–2027): Foundation** — Build the architectural substrate. Pluto maturity to gold-layer coverage across all domains. Core automation of high-volume processes (standard provisioning, L1 support for top 10 contact reasons, basic network fault remediation). Digital channel share to 70%. B2B portal MVP. Product portfolio simplification — retire products that can't be digitized.

**Horizon 2 (2027–2029): Scale** — Automation becomes the default. AI L1 support covers 80%+ of contacts. Zero-touch provisioning for all standard products. Enterprise self-service for mid-market. Digital channel share to 85%. Workforce restructuring — operations roles transition to engineering or exit. Data-as-a-product first external offerings.

**Horizon 3 (2029–2031): Complete** — Hit all seven north star targets. Full AI L1. 95% digital. Zero-touch standard operations. Remaining human roles are engineers, enterprise solution architects, field technicians, and leadership. Pluto is the intelligence backbone for both internal operations and external data products.

### Layer 6 — Governance & steering

The TOM itself needs a governance model for its own implementation. I'd recommend:

- **TOM Board** (quarterly) — Board-level steering on north star KPIs, investment allocation, and organizational transformation decisions
- **Domain councils** (monthly) — One per domain (Customer, Market & Sales, Product, Network) — owns capability maturity, automation progress, and interdependency management
- **Automation office** (continuous) — A cross-functional team (likely sitting in your AI & Data Tribe) that tracks the automation backlog, measures zero-touch coverage, and removes blockers

---

## What comes next

This is the strategic logic. The next step is to turn it into a working deliverable — I'm thinking an interactive HTML document that visualizes all six layers, lets you click through capability clusters, and includes the eTOM mapping we already built as the process-level foundation underneath.

Before I build that, two things:

1. **Your workforce and org model answers** would sharpen Layer 4 (People model) and Layer 5 (transition) significantly. What's the current headcount range, and what organizational model do you envision?

2. **Prioritization input** — Of the 12 capability clusters, which 3–4 do you see as the biggest gaps today? That would let me sequence the transition architecture more precisely.

Want to answer those and then I'll build the full deliverable? Or should I proceed with reasonable assumptions and flag them?

## Human  *(2026-03-31T08:45:24.692210+00:00)*

Workforce envelope - reduce from today's 5,5k employees by at least 25%. Organizational model - minimally we need to restructure the Agile operating model to support real-time production, integration of IT into business, radically simplified and automated (AI-powered) ways of working

## Assistant  *(2026-03-31T08:50:10.636014+00:00)*

Robi has given me the final pieces. Let me synthesize everything and build the comprehensive deliverable. Key inputs:

- Current: 5,500 employees → Target: ~4,125 or less (25%+ reduction)
- Org model: Restructure agile model, integrate IT into business, AI-powered ways of working
- This is a massive transformation - from 5,500 to ~4,100 while simultaneously automating everything

Let me think about what this means for the TOM:

1. The workforce reduction is significant but achievable if zero-touch targets are real
2. IT integration into business means no separate IT department - embedded engineering
3. "Real-time production" means the agile model needs to shift from sprint cycles to continuous delivery

4. AI-powered ways of working means AI isn't just customer-facing - it's embedded into how employees operate daily

Now I'm building an interactive HTML deliverable that visualizes the complete TOM framework across all six layers, incorporating everything Robi's provided. This needs to be Board-quality and impressive as a standalone piece.Now the picture is complete. The 25% reduction from 5,500 to ~4,125 is actually conservative relative to your automation ambition — which tells me the real play is that you're not just cutting, you're **recomposing**. The headcount envelope forces prioritization; the automation targets determine where the cuts fall; and the org restructuring determines what the surviving roles look like.

Let me name the most important implication before I build the deliverable:

**The death of the IT department as a separate entity.** When you say "integration of IT into business," you're describing the end of the model where business units request things and IT builds them. In a zero-touch company, every business domain IS a technology operation. Product managers write product logic that executes autonomously. Network engineers build self-healing systems. Commercial teams configure AI-driven campaigns. The people who remain are all, in some sense, engineers — whether they carry that title or not. This means the TOM doesn't have an "IT domain" — it has embedded engineering capability in every domain, orchestrated by a thin platform layer (which is where your AI & Data Tribe evolves to).

Let me build this into the full deliverable now.

This is a major deliverable. Let me plan the HTML structure carefully. This needs to be Board-quality, visually impressive, and comprehensive. Let me build it section by section:

1. Hero/header with the core vision statement
2. North Star - the 7 design constraints as bold metric cards
3. 8 Strategic Design Principles
4. 12 Capability Clusters in 3 tiers (with the 4-domain mapping)
5. Operating Model Blueprint (6 dimensions)
6. Workforce Transformation (5,500 → ~4,125)
7. Transition Architecture (3 horizons)
8. Governance & Steering

9. 
I'm going with Deutsche Telekom's visual language—magenta accents on a clean white background with DM Sans typography. The design needs to feel editorial and executive-grade, with collapsible sections for deeper exploration and interactive elements throughout.

Let me copy to outputs and present the file.

Now present the file.

Great, the file is ready. Let me give Robi a concise summary of what's in the deliverable and where to go next.Here's the full strategic deliverable. It covers all six layers in a single navigable document with a sticky nav, interactive capability cluster drill-downs, and animated workforce bars.

A few things I'd flag for your attention:

**The workforce chart is the slide that will get the most Board attention.** The -90% on contact center and -85% on traditional IT are the numbers that make the "lights-out telco" tangible. But they only land if the growth bars (AI engineering +200%, data & platform +120%) are presented in the same breath — this is a recomposition narrative, not a cost-cutting story.

**The "IT dissolved into business" principle is the hardest organizational change in the entire plan.** It's easy to say, extremely difficult to execute. The Horizon 1 milestone "begin IT dissolution" needs a concrete mechanism — I'd suggest starting with one domain (probably Product, since it's closest to tech already) as a proof point before doing it across the board.

**The transition architecture assumes Product portfolio simplification happens in Horizon 1.** That's the gating constraint for everything else — you can't have zero-touch provisioning for products that were designed for manual processes. The cultural fight will be around killing profitable legacy products that can't be digitized.

Where would you like to go from here? I can see a few natural next steps: deeper design on any specific layer, the eTOM process mapping underneath the capability clusters (connecting this back to the puzzle we built earlier), or a Board-ready presentation deck distilling this into 12–15 slides.

## Human  *(2026-03-31T08:59:12.311958+00:00)*

Let's go even further into the Horizon - operating model vision for 2040 where the whole company has AI deeply embedded at it's core. We need to define the target skills, organizational model centered around segments (Family, Smart shopper, Digital basic, Young, Modern loyalist, SMB, Enterprise) with self-sustaining teams handling market overview, product market fit, product and proposition design and engineering, supported by central common enterprise functions. Provide a proposal for this vision and align the 2030 operating model transformation to it.

## Assistant  *(2026-03-31T09:04:30.495332+00:00)*

Robi wants me to think really big here - a 2040 vision where AI is deeply embedded, and the organization is restructured around customer segments rather than functional domains. This is a fundamental shift from the 2030 model we built. Let me think through what this means strategically and then build a comprehensive deliverable.

The key insight: moving from domain-organized (Customer, Market & Sales, Product, Network) to segment-organized (Family, Smart Shopper, etc.) is a radical shift. Each segment becomes a self-sustaining P&L with embedded capabilities, supported by shared platforms.

Let me think about what this looks like:

**2040 Vision - "The Segment-Sovereign Telco"**

Each segment team operates as an autonomous unit controlling their entire value chain—from market research and product design through engineering and P&L accountability. This transforms us from a functional matrix into a collection of mini-companies, each optimized for their specific customer base. Supporting this are centralized platforms handling network infrastructure, the evolved data intelligence system, shared AI capabilities, and core functions like finance and security that need to remain unified.

The seven segments span from Family bundles and price-conscious Smart Shoppers through self-service Digital Basic users, Young digital natives, premium Modern Loyalists, SMBs, and Enterprise customers. By 2040, AI becomes a genuine team member rather than a tool—the org chart includes both humans and AI agents as equal participants. Each segment operates lean with 15-30 humans plus AI agents, yet maintains full capability to serve their market. The network becomes a shared utility accessed via APIs, and AI systems generate or configure products based on segment-specific insights, allowing the entire company to run with roughly 2,500-3,000 people.

Now I'm thinking through what skills these segment leads actually need—they'll require a blend of commercial acumen and...

Still building the skills framework...

I'm also mapping how this 2040 vision connects back to the 2030 work: the 2030 phase establishes functional excellence and automation foundations, 2035 pivots from functional to segment-based organization, and 2040 fully realizes the segment-sovereign model. I should create a comprehensive deliverable that visualizes the 2040 vision, defines the segment model, outlines the skills framework, and shows how the entire journey from 2030 through 2040 builds toward this future state.This is the right question at the right time. Let me think out loud about what you're actually describing before I build it, because the organizational shift from 2030 to 2040 is more profound than it might initially appear.

**What you're proposing is the end of the functional telco.** The 2030 model we built is still organized by capability domain — Customer, Market & Sales, Product, Network. That's the inherited telco logic: specialists grouped by what they do. The 2040 model you're describing inverts this entirely — people grouped by **who they serve**. Each segment team owns the full stack from market insight through engineering. The shared infrastructure (network, data, AI platform) becomes a utility that segment teams consume via APIs.

This is philosophically closer to how Amazon structures around customer obsession, or how Spotify's original squad model was supposed to work but rarely did — because most companies don't have the automation foundation to make small teams truly self-sustaining. HT in 2040, with the lights-out infrastructure built by 2030, actually could.

Let me build the complete vision.

Let me copy to outputs and present.

Done, let me present.

Done. Let me provide the strategic commentary.Here's the full 2040 vision document. Let me walk through the most important strategic decisions embedded in it.

**The ~2,800 FTE target is derived, not imposed.** Seven segment teams averaging 15–25 humans each gives you ~140 in segments. Platform teams (AI, data, network, commerce, security) at ~980. Field operations at ~450. Corporate functions at ~280. Enterprise key accounts at ~150. That math lands around 2,800 — roughly half of today's headcount over 15 years.

**The segment team sizes are deliberately asymmetric.** Digital Basic runs with ~6 humans (the automation proof point). Enterprise runs with ~15 humans plus dedicated key account directors. Family and SMB are the largest because they have the most product complexity. This asymmetry is a feature — it means you're allocating human capital to where it creates value, not spreading it evenly.

**The critical sequencing insight** that I'd push hard in any Board conversation: you cannot pivot to segment sovereignty without first achieving functional automation. The 2030 domain model builds the muscles; the 2040 segment model deploys them differently. A segment team of 20 people can only own the full value chain if operations are already autonomous. Skip the 2030 work and you get small teams drowning in manual processes — which is exactly what happens when telcos do "agile transformation" without automation transformation first.

**The AI-as-team-member distinction matters philosophically.** In 2030, AI is a tool that humans direct. By 2040, AI agents are autonomous participants in the segment loop — the Market Scanning Agent doesn't wait to be asked, it produces the weekly intelligence brief independently. The human segment lead reviews and redirects, but doesn't initiate. This is a fundamentally different relationship with technology than anything in the current operating model.

**The skills framework is designed to make this transition survivable.** The four universal skills (AI orchestration, data fluency, systems thinking, commercial acumen) are the filter — anyone who develops all four can move into a segment team or platform team. Anyone who can't is in the 25–50% that exits over 15 years. Starting the upskilling program now, against the 2030 milestones, gives people a decade to adapt.

Want me to merge both documents (2030 TOM + 2040 vision) into a single unified strategic framework, or would you prefer a Board-ready slide deck that tells the story in 15–20 slides?

## Human  *(2026-03-31T13:24:13.643728+00:00)*

Please create a draft set of assumptions first for the 2030 TOM, I will read them and provide you with strategic streams and projects that are already on the horizon

## Assistant  *(2026-03-31T13:25:28.947514+00:00)*

Robi wants a comprehensive set of assumptions that underpin the 2030 TOM. These should be structured, clear, and specific enough that he can validate/challenge each one and then map his existing strategic streams and projects against them. This is a working document, not a presentation — it needs to be scannable and editable.

Let me think about what categories of assumptions matter for a TOM:

1. Market & competitive assumptions
2. Customer & demand assumptions
3. Technology & platform assumptions
4. Regulatory & compliance assumptions
5. DT Group relationship assumptions
6. Financial & investment assumptions
7. Workforce & organizational assumptions
8. AI & automation maturity assumptions
9. Product & portfolio assumptions

10. Network & infrastructure assumptions

Each assumption needs to be specific and testable — if it turns out to be wrong, it should materially change how the TOM is designed. Since this is a working draft he'll annotate and iterate on, I'll create a clean HTML document that's easy to scan and edit rather than burying it in conversation, especially given the volume of assumptions across all these categories.Good call — assumptions first, then we map reality to them. Let me lay these out directly so you can react fast, then I'll build the formal document once we've pressure-tested them.

I'm structuring these as **testable statements** — each one either holds or doesn't, and if it doesn't, it changes the TOM design.

---

## Market & competitive environment

**A1.** The Croatian telecom market remains a three-player oligopoly (HT, A1, Telemach) through 2030, with no significant new entrant or disruptive MVNO gaining >5% share.

**A2.** Market-level mobile subscriber growth is flat to slightly negative — HT's 2M target is achieved through share gain and convergence, not market expansion.

**A3.** Fixed broadband demand continues shifting toward fiber, with satellite and FWA serving as gap-fillers for rural/underserved areas, not mainstream alternatives in urban zones.

**A4.** Price competition intensifies on standalone products but convergent bundles remain defensible — customers who hold 3+ products churn at less than half the rate of single-product customers.

**A5.** B2B/ICT market in Croatia grows at 8–12% CAGR through 2030, driven by cloud adoption, NIS2 compliance requirements, and SMB digitalization — this is the primary growth vector for HT's enterprise push.

**A6.** OTT players (streaming, messaging, fintech) continue to commoditize connectivity but do not enter infrastructure ownership in Croatia by 2030.

## Customer & demand

**A7.** Customer tolerance for digital-only interaction reaches 90%+ in B2C by 2028, driven by generational shift and banking/retail sector normalization of app-first service.

**A8.** B2B mid-market (companies with 10–250 employees) becomes willing to self-serve for standard ICT products by 2027, reducing the need for field sales in this segment.

**A9.** Enterprise customers (top 200 accounts) continue to require human relationship management and custom solution design — full digital self-service is not viable for complex multi-site deals.

**A10.** Croatian-language AI support (voice + text) reaches human-equivalent quality for L1 interactions by 2028, enabled by advances in multilingual LLMs and HT-specific fine-tuning.

**A11.** Customer expectations for resolution speed converge with digital-native benchmarks — meaning <2 minute response and <24h resolution for standard issues becomes the baseline, not a differentiator.

## Technology & platforms

**A12.** DT Group BSS/OSS platforms (billing, CRM, core network) remain the mandated foundation, but HT retains selective autonomy to build sovereign layers on top — particularly for AI, data, and digital experience.

**A13.** Pluto (Data Vault 2.0 on GCP) reaches gold-layer maturity across all 14 data domains by end of 2027, providing the data foundation for all AI and automation use cases.

**A14.** Cloud-native architecture becomes the default for all new applications by 2027 — no new on-premise deployments except for regulatory or latency requirements.

**A15.** API-first architecture is achievable across the core BSS/OSS stack by 2029, enabling the single digital commerce layer that all channels (app, web, portal, stores) consume.

**A16.** The current BSS/OSS stack can be progressively modernized rather than requiring a full rip-and-replace — i.e., HT doesn't need a €100M+ BSS transformation program to achieve the 2030 targets.

**A17.** GenAI/LLM capabilities continue to advance at current trajectory, making autonomous L1 support, content generation, and AI-assisted coding production-grade by 2027–2028.

## AI & automation maturity

**A18.** Zero-touch provisioning for standard mobile and fixed broadband products is achievable by 2027 with current technology trajectory and Pluto as the data backbone.

**A19.** AI-handled L1 support can reach 100% coverage by 2030, but this requires solving for the long tail of low-frequency, high-complexity contact reasons — not just the top 10.

**A20.** Zero-touch operations across billing, assurance, and network management requires closed-loop automation (sense → decide → act → learn), not just rule-based automation of individual steps.

**A21.** AI governance, safety, and regulatory frameworks (EU AI Act) are manageable within HT's operating model and don't fundamentally block deployment of autonomous AI systems in customer-facing roles.

**A22.** The AI & Data Tribe (currently ~25 direct reports + extended network) needs to scale to ~80–100 people by 2028 to deliver on the automation ambition — this is the single biggest hiring challenge.

## Network & infrastructure

**A23.** HT maintains full infrastructure ownership across all access technologies through 2030 — no structural separation, no network sale, no significant infrastructure-sharing beyond existing agreements.

**A24.** Fiber coverage reaches 65–70% of Croatian households by 2030, with satellite and FWA covering the remaining rural/underserved areas to achieve near-universal broadband.

**A25.** 5G coverage reaches 90%+ population by 2028, with 5G SA (standalone) enabling network slicing and edge computing capabilities needed for enterprise propositions.

**A26.** Network CAPEX remains at 15–18% of revenue through 2030, with efficiency gains from automation offsetting the investment in fiber expansion and 5G rollout.

**A27.** Network operations can transition from human-managed NOC to AIOps-driven autonomous operations by 2029, reducing network operations headcount by 40–50%.

## Product & portfolio

**A28.** The current product portfolio can be simplified to <50 active SKUs by 2028 — this requires retiring legacy products that cannot be digitally provisioned, even if they still generate revenue.

**A29.** All new products launched after 2027 are digital-native: configurable, provisionable, and supportable without human intervention as a design requirement.

**A30.** Convergent bundling (mobile + fixed + TV + IoT) remains the primary ARPU growth lever in B2C, and the product architecture supports flexible, AI-configurable bundles.

**A31.** TV/entertainment remains part of the product portfolio through 2030, but increasingly as an aggregation/partnership model rather than own-platform investment.

**A32.** Data-as-a-product (external monetization) generates first revenue by 2028 but remains <2% of total revenue through 2030 — it's a proof point, not a revenue pillar.

## Financial & investment

**A33.** The 2030 TOM delivers net OPEX reduction of 20–25% vs 2025 baseline, primarily through automation of operations, support, and back-office — funding the transformation investment.

**A34.** Total transformation investment (2025–2030) is in the range of €150–250M, covering Pluto scaling, AI development, BSS/OSS modernization, digital channel build, and workforce restructuring.

**A35.** Revenue growth is modest (2–4% CAGR) through 2030, driven by B2B growth and ARPU uplift from convergence — the business case for transformation is primarily cost-led, not revenue-led.

**A36.** The workforce reduction from 5,500 to ~4,125 generates annual savings of €40–60M by 2030, partially offset by higher average cost per FTE (engineering roles command premium vs operations roles).

## Workforce & organization

**A37.** The 25% headcount reduction is achievable through natural attrition (retirement, voluntary turnover) combined with targeted restructuring — without mass layoffs that would trigger regulatory or reputational risk.

**A38.** Croatia's labour market can supply the engineering talent needed (AI/ML, data engineering, full-stack development) through a combination of local hiring, upskilling existing staff, and selective use of DT Group shared services or nearshoring.

**A39.** The agile operating model restructuring (from current model to domain-embedded engineering) can be executed in 2–3 years without catastrophic productivity loss during transition.

**A40.** Croatian labour law and works council requirements are navigable for the restructuring — they'll slow things down but not fundamentally block the organizational changes.

**A41.** DT Group gives HT sufficient organizational autonomy to restructure the operating model, provided it stays within financial guardrails and maintains group platform commitments.

## Regulatory & compliance

**A42.** EU AI Act obligations for high-risk AI systems (which may include autonomous customer support) are manageable with appropriate governance, documentation, and human oversight mechanisms.

**A43.** NIS2 implementation in Croatia imposes operational requirements but also creates B2B market opportunity — HT can position as a trusted security partner for enterprises.

**A44.** GDPR/ePrivacy framework remains stable — no radical new data regulation that would fundamentally undermine the data-as-a-product or AI-powered personalization ambitions.

**A45.** Croatian regulatory environment (HAKOM) remains supportive of infrastructure investment and doesn't impose structural separation or aggressive wholesale obligations that would undermine the owner-operator model.

---

These are the 45 assumptions I'd test. Some are near-certain (A1, A23), some are genuine unknowns that could break the plan (A16, A22, A38). The ones I'd flag as highest-risk are:

**A16** (BSS modernization without rip-and-replace) — if this doesn't hold, the investment envelope in A34 explodes and the timeline shifts by 2–3 years.

**A22** (scaling the AI & Data Tribe to 80–100) — this is the capacity constraint. Everything depends on it.

**A38** (talent supply in Croatia) — engineering talent in a market of 4M people is structurally scarce.

**A19** (100% AI L1 including the long tail) — the top 10 contact reasons are solvable. The 200+ edge cases that make up the remaining 20% are the real test.

Go through these and tell me which ones need adjusting, which are already covered by existing streams, and where you have projects in flight that map to specific assumptions. I'll then align the TOM to reality.

## Human  *(2026-04-01T13:44:46.039189+00:00)*

treba li prvo definirati operativni model ili way of work? Što opisuje operativni model, a što way of work (daj mi primjer)

## Assistant  *(2026-04-01T13:45:33.512861+00:00)*

The user is asking in Croatian whether we should first define the operating model or the way of work, and what each describes with examples. This is a fundamental strategic architecture question. Let me answer clearly and directly.Odlično pitanje — i odgovor na njega mijenja redoslijed svega što radimo. Razmislimo o tome konceptualno.

## Operativni model vs. Way of Work — što je što

**Operativni model** odgovara na pitanje **"ŠTO radimo i TKO to radi"**. To je arhitektura kompanije — struktura, odgovornosti, sposobnosti, tokovi vrijednosti.

**Way of Work** odgovara na pitanje **"KAKO to radimo"**. To je režim izvršenja — procesi, rituali, alati, donošenje odluka, način suradnje ljudi i AI-a.

Evo konkretnog primjera da razlika bude kristalno jasna:

---

**Primjer: Lansiranje novog konvergentnog paketa za Family segment**

**Operativni model definira:**
- Product domain je vlasnik životnog ciklusa proizvoda
- Market & Sales domain definira go-to-market
- Customer domain upravlja iskustvom i podrškom
- Network domain osigurava kapacitet i aktivaciju
- Pluto osigurava podatkovnu podlogu za personalizaciju
- Postoji Product Council koji odobrava lansiranje
- P&L odgovornost je na Product domeni s input KPI-jevima iz ostalih domena

**Way of Work definira:**
- Product tim koristi continuous discovery (ne sprinteve) za validaciju product-market fita
- AI agent generira inicijalnu analizu tržišta i prijedlog bundle konfiguracije — čovjek recenzira i odlučuje
- Odluka o lansiranju ide kroz asinkroni review (ne komitetski sastanak) s 48h SLA za sve domene
- Engineering deploy ide kroz trunk-based development s automated testing — ne release train
- Kampanja se generira AI-em, čovjek odobrava ton i brend, distribucija je automatska
- Retrospektiva je AI-generirana na temelju metrika, ne facilitirani sastanak
- Komunikacija ide kroz structured async (dokumenti > meetings), sa sync touchpointima samo za konflikt resolution

---

## Što dolazi prvo?

Evo mog stava, i on je kontraintuitivan:

**Way of Work dolazi prvo — ali ne cijeli, nego njegovi principi.** Evo zašto:

Operativni model koji dizajniraš ovisi o tome kako pretpostavljaš da ljudi (i AI) rade. Ako pretpostaviš klasični agile s tjednim sprintevima i ceremonijama, dobit ćeš operativni model s puno koordinacijskih slojeva. Ako pretpostaviš continuous delivery s AI-native workflow-ovima, dobit ćeš radikalno drugačiji — tanji, brži operativni model.

Ali ne možeš definirati cijeli Way of Work bez da znaš strukturu. Ne možeš reći "Product tim radi continuous discovery" ako nisi prvo definirao da Product tim postoji i što mu je scope.

Dakle, pravi redoslijed je ovakav:

**1. Way of Work principi** (5–8 principa koji definiraju KAKO želimo raditi u 2030)

**2. Operativni model** (struktura, domene, odgovornosti, tokovi — dizajniran da podržava te principe)

**3. Way of Work detaljni dizajn** (rituali, alati, decision-making procesi, AI-čovjek interakcijski obrasci — dizajnirani za konkretnu strukturu)

To znači da trebamo **prije assumptiona i TOM-a** definirati WoW principe. Daj mi tvoju viziju na ovo:

The user is asking a fundamental question about the relationship between operating model and way of work. I answered in Croatian since they asked in Croatian, and now I'm waiting for their input on the three questions about work rhythm, human-AI relationship, and decision-making model.Tvoji odgovori na ova tri pitanja će odrediti WoW principe, koji onda postaju **ulazni parametri** za operativni model — ne obrnuto. To je ključna razlika od onoga kako većina telco-a radi transformaciju (dizajniraju strukturu pa se nadaju da će se način rada prilagoditi).

## Human  *(2026-04-01T13:50:37.666682+00:00)*

Q: Kakav temeljni radni ritam vidiš za HT 2030?
A: Hybrid (continuous za business, sprint-based za engineering)

Q: Kako vidiš odnos čovjek ↔ AI u svakodnevnom radu 2030?
A: Kontekst-ovisan — ovisi o tipu zadatka i riziku

Q: Koji model donošenja odluka preferiraš?
A: Empowered teams (tim odlučuje u okviru guardrailsa)

## Assistant  *(2026-04-01T13:55:34.077968+00:00)*

The user has made interesting choices - particularly the hybrid model being inverted from what I'd expect (continuous for business, sprint-based for engineering). Let me address this and build out the WoW principles, then create a comprehensive document.

Let me think about what they said:
1. Hybrid - continuous for BUSINESS, sprint-based for ENGINEERING (this is the opposite of what I proposed as an option - I said "continuous za engineering, sprint-based za business" but they flipped it)
2. Context-dependent human-AI relationship
3. Empowered teams with guardrails

This is actually a very thoughtful set of choices. Let me unpack why the inverted hybrid is interesting and build the WoW principles around it.

They deliberately chose the opposite approach, which makes sense in a telco context - business needs to respond continuously to market shifts and competitive moves without waiting for sprint boundaries, while engineering benefits from structured delivery cadences given the complexity of shared platform dependencies and integration requirements.

Now I'm synthesizing their choices into a coherent Ways of Working framework and drafting the document.Zanimljiv odabir — i namjerno si obrnuo hybrid koji sam ponudio. Dao sam ti "continuous za engineering, sprint-based za business", a ti si rekao obrnuto. To je pronicljiv izbor i vrijedi ga raspakirati jer mijenja cijelu filozofiju.

## Zašto "continuous business, sprint-based engineering" ima smisla za HT

Većina tech kompanija radi obrnuto — engineering na continuous delivery, business na ciklusima. Ali za telco koji se transformira, tvoja logika je ispravnija:

**Business mora biti continuous** jer tržišni signali ne čekaju sprint boundary. Kada A1 spusti cijenu, kada Telemach lansira novu ponudu, kada churn metrika skoči — komercijalni odgovor mora biti isti dan, ne za dva tjedna. Kampanje, pricing, ponude, retention akcije — sve to mora teći kontinuirano s AI-om koji reagira u realnom vremenu.

**Engineering treba strukturirane cikluse** jer gradi na shared platformama s ozbiljnim ovisnostima. BSS/OSS integracije, network konfiguracije, Pluto pipeline-ovi — sve to zahtijeva koordinaciju, testiranje, release management. Continuous deployment u izoliranom SaaS startupu je trivijalan. Continuous deployment na telco stacku s 200 integracija je recept za katastrofu. Strukturirani ciklusi (ali kratki — tjedni, ne dvotjedni) daju stabilnost bez sporost.

Sad imam dovoljno za definirati WoW principe. Ovo je temelj na koji stavljamo operativni model.

Let me copy to outputs and present.

Done, now present the file.

Good, the file is created and presented. Let me give a concise summary.Evo WoW principa kao kompletnog dokumenta. Osvrnuo bih se na ono što smatram ključnim u cijelom dokumentu — scenarij na dnu.

**Scenarij s A1 competitive response je najvažniji dio dokumenta.** Ne zato što je najsloženiji, nego zato što je najkonkretniji. Pokazuje da razlika između 53 sata i 6 tjedana za isti odgovor nije u ljudima — isti product owner donosi istu odluku. Razlika je u načinu rada: async vs meeting-driven, AI-initiated vs human-initiated, composable vs monolithic, empowered vs escalation-dependent.

Kad ovaj scenarij prezentiraš leadershipa, pitanje koje treba postaviti nije "slažete li se s principom W1?" — to je apstraktno. Pitanje je: **"Želimo li na A1-ov potez reagirati za 2 dana ili za 6 tjedana?"** Odgovor na to pitanje automatski validira principe.

Sada — prije nego se vratimo na TOM i assumptions, trebam tvoj input na dva mjesta:

1. **Pregledaj 8 principa** — ima li neki koji ti ne sjeda, koji treba zaoštriti ili koji nedostaje? Posebno W5 ("Gradimo, ne naručujemo") jer je to princip koji će izazvati najviše otpora u organizaciji.

2. **Pošalji mi strateške streamove i projekte** koji su već na horizontu — da ih mapiramo na principe i assumptions, i da vidimo gdje postoji alignment, a gdje gap između onoga što se planira i onoga što TOM zahtijeva.
