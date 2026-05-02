# Context digest — Big Picture

## Purpose

Translate HT's strategic vision — moving from siloed, legacy-culture
ways of working to an AI-empowered "One Team" future — into engaging
**digital experiences for ~5,500 HT employees**. The Big Picture
watercolor illustration (Croatian + English) is the canonical visual
metaphor; everything else (game, video, OKRs) is a derivative or
companion artefact.

The project's two carrying anchors:
- **HT Big Picture watercolor** (Croatian + English versions) — primary
  visual reference, source of truth for the cultural narrative.
- **HT four leadership principles, always in this order:**
  1. **Trustworthy** — *Gradi Povjerenje*
  2. **Compassionate** — *Podrži Druge*
  3. **Inspiring** — *Oslobodi Potencijal*
  4. **Change-Making** — *Promijeni na Bolje*

## Two flagship artifacts

### 1. The Big Picture interactive guide
A single-page HTML explorer with:
- 20 clickable hotspots on the Big Picture illustration
- Bilingual HRV/EN language toggle (loads the right canonical
  illustration per language)
- Category filters
- Zoom / pan with desktop mouse-drag and pinch on mobile
- Business scenarios + old-world / new-world comparisons
- TeleNeo font family via cdnfonts.com
- Light-mode variant (`big_picture_guide_light.html`)

**Bugs resolved that future iterations should not re-introduce:**
- Mobile hotspot misalignment — fixed with shared `position:relative`
  wrapper around the image; hotspot offsets are anchored to the image
  element, not the viewport.
- Safari / iOS compatibility issues — addressed.

### 2. MOST WANTED! — The Bridge Challenge (training game)
React app, browser-based. A magenta stick figure crosses a 10-plank
bridge from the current to the future state of HT. Players answer
scenario challenges; correct answers (aligned with the four principles)
move forward, wrong answers cost lives.

**Current production-ready spec** drafted for **Google AI Studio
(Gemini 3.1 Pro)**:
- **3D rendering** (Three.js upgrade from current React 2D),
  GTA-V-inspired-but-simplified visual style.
- **Firebase / Firestore** backend (custom database ID, not the
  default — note this when wiring up cloud functions).
- **Google SSO authentication.**
- **Leaderboard, team challenges, achievement system, multiplayer
  bridge race, manager analytics dashboard, progressive difficulty,
  Daily Challenge.**
- 9 feature modules in the spec.
- Embedded "MOST WANTED!" watercolor logo (base64) — start screen
  prominent, watermark during gameplay.

**Scenario design rules (load-bearing):**
- **20 deeply developed scenarios outperform 90 shallow ones.** Quality
  over quantity is the explicit principle.
- **Wrong answers must sound genuinely plausible** — they should
  embody common corporate behaviors (escalating, building consensus,
  following process) that subtly violate the principles, not be
  obviously bad.
- Bilingual scenarios with **named Croatian characters in specific HT
  departments**, rich emotional context, immediate "Why" explanations
  on each answer.
- Total scenario library has been built up to ~104+ across both Gemini
  v1 (4 found low-quality, rewritten) and v2 generations.
- Inspirational bridge intro text uses the Big Picture narrative
  (left-side / right-side framing — "what made us successful on the
  left will not keep us at the top on the right").

## Adjacent artifacts in this project

- **Big Picture strategy video** — 2–3 minute browser-renderable
  animation with English voice narration, summarized narrative, HT
  branding. Built as an HTML animation with overlays; subtitles
  visible in clean mode.
- **B-2 management OKRs** based on the Building Blocks manifest
  (Povjerenje / Podrška / Potencijal / Promjena). Single-Objective
  structure, 4 KRs (one per pillar). Multi-level versions: B, B-1,
  B-2.
- **Big Picture Assistant** — technical blueprint started for an
  internal AI chat application accessible to all HT colleagues
  (including those without ChatGPT Enterprise / Gemini Enterprise
  licences).
- **Cultural-narrative rewrites** (e.g. "culture over strategy") —
  language-tightening exercises around the Building Blocks vocabulary.

## Conventions (firm)

- **Brand magenta `#e20074`** (RGB 226,0,116) is the visual anchor on
  every deliverable.
- **Self-contained single-file delivery** — HTML files with all assets
  base64-embedded. Browser-only, no server, no external dependencies
  beyond the TeleNeo CDN font.
- **Croatian is default**, English toggle is a standard feature on
  every user-facing artefact.
- **TeleNeo font family** (cdnfonts.com) — DT brand requirement, not
  a stylistic choice.
- **Watercolor illustrative style** — the visual identity beyond the
  brand magenta. The "MOST WANTED!" logo is also watercolor.

## Working pattern with Claude (load-bearing)

- **Iterative, specific feedback round-by-round** — not exhaustive
  upfront specification. Build → react to what's wrong → next build.
- **Croatian** is the working language.
- **Sessions are long** with multiple build phases each — be ready to
  carry context.
- **Move to working prototype fast**, refine on direct observation of
  shortcomings.
- **Visual richness matters**. "Sparse graphics" was a recurring
  pain point — address visual depth early on every new artefact.

## Open threads

1. **Production game build in Google AI Studio** is the active work
   item — Three.js 3D, Firebase backend, multiplayer bridge race,
   manager dashboard. Spec is drafted; build is in flight.
2. **Big Picture Assistant** — implementation of the technical
   blueprint (internal AI chat for all HT colleagues regardless of
   licence). Started as concept; needs build phase.
3. **Multi-level OKR rollout** (B / B-1 / B-2) — single combined
   HTML one-pager exists; political adoption is the next step.
4. **Game launch event** — DT board visit slot was referenced as the
   demo target for multiplayer mode.

## Knowledge files attached

- `HRV-Big Picture-narativ-0217 final.docx` — the canonical Croatian
  narrative for the Big Picture.
- `Cre8rel8 HT Training Guide 2522026.pdf` — the training guide whose
  language and principles the game and OKRs draw from.

## What to ask Claude next

When picking this up: paste this digest into the first chat under the
new project. Likely next prompts: (a) continue the production-grade
game build in AI Studio (next Three.js or Firebase prompt), (b) build
out the Big Picture Assistant per the technical blueprint, (c) draft
new scenarios for the game following the quality-over-quantity rules,
or (d) iterate the multi-level OKRs based on directors' feedback.
