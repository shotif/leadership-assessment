# Enterprise rebuild playbook

Step-by-step instructions to recreate everything in the new Hrvatski
Telekom Enterprise Claude account. Follow in order. Each step has the
exact prompt to use.

---

## Phase 0 — Pre-flight (≈ 5 min)

- [ ] You're signed into the **new HT Enterprise Claude account** (not
  the personal Max account).
- [ ] You have this `migration-kit/` folder open locally (or on
  GitHub) so you can copy-paste from it.
- [ ] You can read Croatian — most of the content here is in HRV.

---

## Phase 1 — Account-level memory (≈ 10 min)

The single most important step. Sets the standing context every chat
in the account inherits.

1. Open **a brand-new non-project chat** in Enterprise.
2. Open `memory-seed.md` in this kit.
3. Copy the section between the `---` lines (everything from
   `**Work context**` to the `**Other instructions**` block at the
   end). Paste it into the chat with this opening:

   > ```
   > Save the block below as my standing memory for our future
   > conversations. After you've stored it, confirm in one sentence
   > that you've saved it and list the top three facts you'll
   > remember.
   >
   > <paste memory-seed contents here>
   > ```

4. Verify Claude's confirmation actually mentions: HT, AI & Data Tribe
   Director, Krešo, Keystone AI. If any of those are missing, paste
   again.

> **Stop here if anything went wrong.** Don't move to projects until
> the account-level memory is confirmed.

---

## Phase 2 — Recreate the projects (≈ 15 min × 5 projects)

Five projects to rebuild. **Do them one at a time.** For each:

### 2.A — Create the project shell

In Enterprise → New Project. Use these names verbatim so the slugs
match this kit:

| Name | Slug | Source files |
|---|---|---|
| Big Picture | `big-picture` | `projects/big-picture/` |
| Cico | `cico` | `projects/cico/` |
| HT Future Operating Model | `ht-future-operating-model` | `projects/ht-future-operating-model/` |
| PetAIk | `petaik` | `projects/petaik/` |
| QBR Next Level | `qbr-next-level` | `projects/qbr-next-level/` |

### 2.B — Custom instructions

Open `projects/<slug>/instructions.md`. **Copy the body
(everything below the first `# Custom instructions — …` header)** into
the project's "Custom instructions" field.

If the file says *"No custom instructions set on the original
project"* — leave the Enterprise instructions field blank, or write
your own one-liner that captures the project's purpose.

### 2.C — Knowledge files

Open `projects/<slug>/knowledge/` and **upload every file** as
project knowledge.

- **`big-picture/knowledge/`** — `HRV-Big Picture-narativ-0217 final.docx`,
  `Cre8rel8 HT Training Guide 2522026.pdf`
- **`qbr-next-level/knowledge/`** — `operating_plan_review.html`
- The other three projects have no knowledge files.

### 2.D — Prime the project memory with the digest

Once the project exists in Enterprise, open `projects/<slug>/context-digest.md`
and paste **the whole file** into the **first chat** under that
project, with this opening:

> ```
> This is a context digest from the previous account's project I'm
> rebuilding here. Save it as standing context for this project so
> future conversations inherit it. After saving, confirm in one
> sentence what you've stored and list the project's purpose plus the
> top three open threads.
>
> <paste context-digest.md contents here>
> ```

Verify Claude's confirmation lists the right project name and at least
one specific named entity (a programme, a person, a deliverable). If
not, paste again with "be more specific — the digest mentions X, Y, Z
which you should confirm you've stored."

### 2.E — Per-project notes

Each project has its own quirks worth flagging *in that first chat*
right after the digest is saved:

#### 🟪 Big Picture
> ```
> Working language is Croatian (English toggle on user-facing
> artefacts only). All deliverables ship as self-contained single-file
> HTML with assets base64-embedded. Brand magenta is #e20074;
> typography is TeleNeo via cdnfonts.com. Watercolor illustrative
> style. The HT four leadership principles, always in this order:
> Trustworthy (Gradi Povjerenje), Compassionate (Podrži Druge),
> Inspiring (Oslobodi Potencijal), Change-Making (Promijeni na Bolje).
> ```

#### 🟪 Cico (re-scoped — personal reflection only)
> ```
> Use this project only for personal reflection and coaching-style
> conversations: leadership development, work-life patterns,
> performance review prep, NEXT-program prep. HT work tasks (job ads,
> board decks, panel prep, candidate reviews, OKRs) go to standalone
> chats, not here. This is a deliberate re-scope from the previous
> account.
> ```

#### 🟪 HT Future Operating Model
> ```
> All deliverables are standalone interactive HTML in DT magenta
> (#E20074) on white, DM Sans typography, T-logo mark. TM Forum eTOM
> v24.5 is the structural backbone. Layered framework pattern:
> constraints → principles → capabilities → operations → transitions
> → governance. The 2030 → 2040 sequencing is load-bearing — domain
> model in 2030 is a precondition for segment sovereignty in 2040.
> ```

#### 🟪 PetAIk
> ```
> The single source of truth is the PetAIk Working Document (Word +
> interactive HTML). Don't propose changes to the framing without
> grounding them in that doc. Pilot is HT-own (not via DT group),
> monthly cadence, full day, Q2 2026 start. Internal alignment with
> HR / CRO Marketing-Product / Strategy comes before any Board ask.
> ```

#### 🟪 QBR Next Level
> ```
> You are a Big-5 strategic advisor with 25+ years on operating
> models, fluent in the TRAIIN method (use for inspiration, don't
> force it). Two horizons: near-term fix of the existing QBR cycle,
> and design of the OKR-driven 2027 plan as PoC. Highest-leverage
> proposal from the diagnostic is #2 — programme layer above
> initiatives. 5–8 programmes implicit in the NatCo Visit deck.
> ```

> **Repeat 2.A–2.E for each of the 5 projects.** Don't batch — do one
> end-to-end before starting the next, so any priming issues surface
> immediately.

---

## Phase 3 — Settings, connectors, styles (≈ 20–30 min)

Walk through `settings-checklist.md` top-to-bottom. The big items to
not miss:

- [ ] **Connectors / MCP integrations** (Google Drive, GitHub, etc.) —
  re-authorise from scratch. Anthropic does **not** transfer OAuth
  grants between accounts.
- [ ] **Custom skills** — re-upload any custom skills you used (the
  `t-brand-designer` skill is a notable one). Source skill files are
  not in the export.
- [ ] **Custom writing styles** — recreate manually.

---

## Phase 4 — Verify (≈ 5 min)

In a fresh non-project chat, ask:

> ```
> Quick sanity check on the standing memory you have about me.
> Without searching anything, what do you know about:
> 1. My role and where I work
> 2. The active workstream cluster I'm currently focused on
> 3. The four HT leadership principles
> 4. The conventions for Big Picture / HT FOM deliverables
>
> Be brief — one or two lines per item.
> ```

Then in any project, ask:

> ```
> What's the current state of this project per the context digest you
> stored, and what are the top open threads?
> ```

If both responses match the kit, the rebuild is done.

---

## Phase 5 — Cleanup (≈ 2 min)

- [ ] Delete (or move to encrypted storage) the original `.dms` export
  file from your Downloads folder.
- [ ] Optionally delete the personal Max account's projects/chats once
  you're confident Enterprise has everything.

---

## If something goes wrong mid-rebuild

- **Claude refuses to save memory** — try shorter chunks. The
  account-level seed fits in one paste; the per-project digests can be
  pasted in 2 messages if Claude is paginating.
- **Memory doesn't stick on retry** — start a brand-new chat and try
  again. Sometimes the existing chat session has cached the wrong
  state.
- **Project knowledge upload fails** — Enterprise has per-file size
  limits. The Cre8rel8 PDF is the largest item; if it exceeds the
  limit, split it or upload the most important pages only.
- **You want to redo a digest from scratch** — delete the relevant
  `context-digest.md`, re-run `claude-migration-kit build … --in-chat`
  in the source repo (it's idempotent now and will only rewrite files
  that don't exist), then paste the new digest prompt into Claude.

---

## Re-running the tool against a newer export

If you ever pull a fresh data export and want to update the kit:

```sh
# Adjust paths to taste
EXP=/path/to/new-export.zip

uv run claude-migration-kit inventory   "$EXP" --out migration-kit
uv run claude-migration-kit classify    "$EXP" --in-chat       # writes inchat-classify-prompt.md
# … paste the prompt into a Claude chat, save the JSON to
# migration-kit/inchat-classify-response.json …
uv run claude-migration-kit classify    "$EXP" --import-inchat
uv run claude-migration-kit select      "$EXP"                  # writes selection.toml
# … edit selection.toml …
uv run claude-migration-kit select      "$EXP" --apply-selection
uv run claude-migration-kit build       "$EXP" --in-chat        # writes per-project digest prompts
# … paste each project's inchat-digest-prompt.md into Claude, save the
# resulting digest over the project's context-digest.md …
```

The **build is idempotent** — re-running won't overwrite your existing
`context-digest.md`, `memory-seed.md`, `settings-checklist.md`, or
`README.md`. Delete those files explicitly if you want a clean rewrite.
