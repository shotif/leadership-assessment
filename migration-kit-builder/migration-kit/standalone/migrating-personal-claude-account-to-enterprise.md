# Migrating personal Claude account to enterprise
- **Conversation ID:** `99b89462-3af6-4f55-ab41-ec2eaadb1c18`
- **Created:** 2026-04-29T06:11:02.740394+00:00
- **Updated:** 2026-05-02T06:24:40.476393+00:00
- **Messages:** 6

---

## Human  *(2026-04-29T06:11:03.112515+00:00)*

How do I migrate my settings, memory and working patterns (projects, conversations, ...) from a personal Claude account to a Claude Enterprise account that uses a different e-mail address?

## Assistant  *(2026-04-29T06:11:45.846063+00:00)*

The user is asking about migrating from a personal Claude account to a Claude Enterprise account with a different email, so I should check the product documentation to find the right information.

 I'm looking through the support center to find documentation on migrating between personal and Enterprise accounts.

 I'm reviewing the search results more carefully now. Domain claiming is the official way to migrate accounts, but it only works if the admin can claim a verified domain that matches the email — which doesn't help if the personal account uses a different email like Gmail. The support documentation confirms this limitation applies specifically to organization-tied accounts.

Since there's no self-serve migration path for different email addresses and you can't change an account's email, Robi's only option is manual recreation: exporting conversations as JSON (though they can't be imported into Enterprise), manually rebuilding memory and projects by copying custom instructions and knowledge files, and recreating settings from scratch.

I should structure the answer to be mobile-friendly and lead with why automatic migration won't work here, then walk through what can actually be transferred and in what order.Short answer: there's no automatic transfer between accounts on different email addresses. Anthropic's domain-claim migration only works when the personal account is on the same email domain the Enterprise admin has verified — so a personal account on, say, Gmail can't be merged into an Enterprise tenant on robert.kopal@hrvatskitelekom.hr. You also can't change the email on an existing account. If you have a separate Claude account on a personal email address (like Gmail or Yahoo), that account isn't affected by domain claiming, and it's not possible to change the email address associated with your Claude account at this time.

So it's a manual rebuild. Practical playbook:

**1. Export from the personal account first.** Settings → Privacy → Export data. You get a zip with conversations, projects, and account data as JSON/markdown — useful as an archive and as raw material to feed back in, but Enterprise has no "import" button.

**2. Recreate Projects by hand.** For each project that matters: copy the custom instructions verbatim into a new Enterprise project, re-upload the knowledge files, and either re-add or skip the historical chats. This is the part the migration blog above describes — about an hour for a handful of projects.

**3. Rebuild memory deliberately, don't try to dump it.** On the new account, in an early chat just tell Claude the standing context you want it to keep — role, team structure, current priorities, preferences. That writes into the new account's memory cleanly. Pasting your current memory blob in raw works less well than 5–10 focused "remember that…" statements.

**4. Re-set settings per surface.** User preferences, custom styles, web search/artifacts toggles, connectors (Google Calendar, Drive, Gmail, etc.) all have to be reconnected on the Enterprise side. Connectors especially — they're per-account auth.

**5. Then retire the personal account.** Cancel any paid plan, keep the export zip somewhere safe, and delete it from Settings → Account when you're confident nothing's missing.

One Enterprise-specific thing worth knowing before you commit: data you put into the Enterprise workspace is owned and managed by HT, not you personally — so anything you'd want to keep strictly personal (non-work projects, private notes) is better left on a separate personal account on a non-HT email rather than migrated in.

## Human  *(2026-04-29T06:17:52.006336+00:00)*

Is there a workflow I can build with Claude Code that does this for me, allowing me to choose which projects and conversations I don't want to migrate?

## Assistant  *(2026-04-29T06:18:48.918444+00:00)*

The user wants to know if they can build a Claude Code workflow to migrate projects and conversations between two Claude.ai accounts with different emails. I need to figure out whether Claude.ai has any APIs available that would allow reading from one account and writing to another—specifically for listing conversations, projects, files, and instructions, then recreating them elsewhere.

Looking at what's actually available: Claude.ai is the consumer product and doesn't expose an API for accessing conversations or projects. The Anthropic API only provides model completions, not access to your Claude.ai data. There's an Enterprise Analytics API for usage metrics and a Data Export feature that gives you a zip file of your conversations and projects, but no public API to write that data back into Claude.ai.

So the realistic approach would be exporting the personal account's data as a zip, then either manually recreating projects in the Enterprise account or using browser automation—Claude Code could help parse the exported data, filter what to migrate, reformat it, and generate prompts to seed new projects with.

The core problem is that there's no official API to programmatically create projects, upload knowledge files, or post conversations to Claude.ai. Any fully automated solution would need browser automation against the web UI, which is fragile, likely violates the terms of service, and won't work well with Enterprise SSO authentication. I should verify whether there's actually a Claude.ai API for this and check if any community tools exist.

 I'm realizing there's no public API from Anthropic to access Claude.ai conversations or projects—only the stateless Claude API for model access and the Enterprise Analytics API for read-only metrics. This means I can't directly read or write conversation data through official channels.

The legitimate path for getting data out is Claude's Data Export feature, which packages conversations into a .dms file with project metadata included. But the real problem is on the write side: there's no sanctioned way to programmatically create projects, upload knowledge files, or push conversations back into Claude.ai. The unofficial cookie-based libraries violate the Terms of Service, and even browser automation through Playwright or Puppeteer sits in a gray area since it involves session-based access.

Claude Code could theoretically handle the export-side work—parsing and processing the exported conversation data—but it can't directly automate actions in the Claude.ai web interface in any officially supported way.

So the practical approach would be to split this into two phases. First, I'd use Claude Code to handle the inventory and filtering work: parse the exported .dms file, extract the conversations and project metadata, generate a checklist of what to keep, and filter down the dataset. Then in the second phase, I'd repackage everything for migration—creating setup briefs with custom instructions and knowledge file summaries, organizing the original files into folders, and preparing everything in a format that's ready to be manually recreated on the Enterprise side. t conversations: a digest doc that captures key decisions, deliverables, and unresolved threads — this is much more useful than re-pasting raw transcripts because Claude has fresh context anyway
- Generate a memory seed file — 5-15 standing facts to feed the new account's memory
- Generate a settings/preferences checklist (since these aren't in the export)

**Phase 3: Apply on Enterprise (semi-manual)**
- For each project: manually create the project, paste instructions, upload knowledge files. (Could use Playwright if you accept the gray area; or do it manually — 1-2 minutes per project.)
- Paste the memory seed into a first conversation
- Reconnect connectors

This is a real, useful, ToS-clean workflow. Let me write this up.

I should keep the format light and structured across the phases since this spans multiple screens, and Robi has the technical chops to appreciate concrete architecture details. I'll probably offer to build this for him as a soft offer at the end.Yes, partially — and the "partially" is the important part. Let me explain the constraint, then a workflow that works around it.

**The hard limit:** there's no public Claude.ai API for reading or writing your projects and conversations. The Anthropic API is stateless model access (it knows nothing about your claude.ai data), and the Enterprise Analytics API only returns aggregated usage counts. Anthropic's ToS prohibits session-based access tools, so unofficial cookie-driven libraries are out. That means a fully automated end-to-end migration isn't cleanly buildable. The export side is fine; the write-back side has to be manual or semi-manual.

**What Claude Code can fully automate (export + transform):**

1. You manually trigger the official Data Export on the personal account → you get a `.dms` file (renamed zip) containing `conversations.json` with project metadata embedded and your knowledge files.
2. Claude Code parses the zip and builds an **inventory**: per project, list conversations, last-activity dates, message counts, custom instructions, and attached knowledge files. Output a markdown checklist.
3. You tick what to keep (or pass selection rules — "everything touched in last 6 months", "exclude personal/non-work projects", "drop conversations under 3 turns").
4. Claude Code repackages the kept items into a **migration kit**: one folder per project with `instructions.md`, the original knowledge files, and a generated `context-digest.md` summarizing decisions, deliverables, and open threads from the kept conversations. Plus a `memory-seed.md` with 10–15 standing facts to feed the new account, and a `settings-checklist.md` for things not in the export (custom styles, connectors, preferences).

**What stays manual on the Enterprise side (write-back):** for each project in the kit, create the Enterprise project, paste instructions, upload knowledge files, kick off a first chat that pastes the memory seed. Roughly 1–2 minutes per project. The blog migration write-up earlier estimated ~1 hour for a real portfolio, which matches.

**Why a digest beats raw transcript replay:** pasting old conversations into a new project doesn't actually give Claude useful "memory" — it just bloats context. A 200-word decisions-and-state digest per project is more useful than 50 conversations of scrollback, and Claude Code is very good at producing those digests from the export JSON.

**The gray-area option I'd flag but not recommend:** you could have Claude Code drive Playwright against claude.ai to automate the create-project / upload-files clicks. It's your own data so the ethics are clean, but it crosses the ToS line on automated UI access and SSO/Enterprise auth often blocks headless browsers anyway. Given your role, not worth the exposure.

If you want, I can sketch the actual Claude Code project structure — folder layout, the parser for `conversations.json`, the digest-generation prompts, and the selection CLI — so you have something ready to run as soon as the export download lands.

## Human  *(2026-05-02T06:23:27.507588+00:00)*

i want you to generate a prompt I can give to Claude Code to kickoff this project

## Assistant  *(2026-05-02T06:24:40.476393+00:00)*

I'm thinking through what would make an effective prompt for Claude Code to handle this migration — it needs clear context and specific deliverables, but also technical constraints and the key decisions already made so we don't waste time relitigating them. Since Robi's both technical and executive-minded, the prompt should be concise and let him move quickly without unnecessary detail.

Now I'm drafting the actual prompt structure: it should cover the migration source (the exported data format), spell out exactly what needs to be built (inventory tool, selection mechanism, migration kit), be explicit about what's off-limits (no automated writes back to Enterprise, no UI automation), suggest Python as the natural choice, and define the specific formats for the digest and memory seed outputs along with a settings checklist. I'll format it as a single copyable prompt in markdown since that works well with Claude Code, and keep it scannable even though it'll be substantial — the user can paste it directly without needing an artifact. r for an exec) — users can define rules to include or exclude content by project, date, message count, or keyword, then output a selection.json file marking what gets migrated. For the migration kit itself, I'll organize it as one folder per project containing the custom instructions, knowledge files, and a generated context digest that summarizes key decisions and open threads from the conversations. Standalone chats go in their own folder, and I'll add a memory-seed file pulling out 10–15 standing facts about role and priorities, plus a settings checklist for reauthorizing connectors and recreating preferences. I'm thinking Python with uv, the Anthropic SDK for generating those digests, and Pydantic for the schemas.

The main constraints are that I won't automate against claude.ai directly, won't try to write into an Enterprise account programmatically, and need to treat all exported data as confidential — no external calls except to Anthropic for the digests. The workflow will be: user provides the .dms/zip file, I run the inventory and show a summary, generate a selection template for them to edit, then produce the final migration kit folder ready for manual upload.

Now I'm deciding whether to deliver this as a file artifact or inline. It's going to be a substantial prompt — over 1500 characters — that they'll likely paste directly into Claude Code, so an inline markdown code block makes more sense than a file download. They can copy it easily on mobile that way. I'll write out the actual prompt now, keeping it focused and actionable. knowledge files organized by topic, with summaries
      conversations.json        # filtered to this project only
      assets/                   # any images/files referenced in conversations

## Why this structure
- **README** guides the rebuild without requiring me to re-read the export
- **memory-seed** jumpstarts context so I don't lose institutional knowledge
- **settings-checklist** captures the non-exportable bits (API keys, connector configs, UI preferences)
- **projects/** lets me migrate selectively — I can rebuild high-value projects first, skip low-value ones
- **knowledge/** and **conversations.json** give me the raw material to paste into Enterprise chats

## Tool behavior
1. Parse the `.dms` file (it's a ZIP)
2. Extract `conversations.json` and any knowledge files
3. Ask me which projects to include (by name or tag, if the export has them)
4. For each selected project:
   - Pull all conversations tagged with that project
   - Extract custom instructions (if any)
   - Collect knowledge files scoped to that project
   - Summarize the conversations into a brief "what this project is about" section for the README
5. Generate the folder structure above, with all files pre-populated
6. Output as a downloadable ZIP

## Non-goals
- Do not attempt to "sync" or "merge" — this is one-way migration
- Do not try to recreate the exact UI/UX of claude.ai — focus on content
- Do not parse or modify conversation content (keep it as-is from the export)
- Do not handle authentication or API calls to Anthropic systems

Now I'm looking at the structure of the export file and thinking through how to parse it efficiently — the conversations.json will likely be large, so I should stream or chunk it rather than loading everything into memory at once. I'm outlining the selection rules that'll let me filter the inventory—by project slug, conversation ID, date range, message count threshold, and keyword patterns. Once I refine the `selection.toml` file, I'll re-run with the `--apply-selection` flag to actually filter things down. Then for each kept project, I'll copy over the instructions and knowledge files, convert conversations to clean markdown, and call the API to generate a context digest that summarizes the key decisions and threads.

I'll need to build this as a Python CLI using `uv`, `typer`, and `rich` for the interface, with `pydantic` for validation and the `anthropic` SDK to hit the API. The digest generation will cap at around 600 words per project, and I'll show a progress bar with an upfront cost estimate before running anything. I'm pulling the API key from the environment and will fail loudly if it's missing, and I'm strictly using the official Anthropic API—no browser automation or unofficial endpoints. I'm going back through the spec to tighten it up—the phased approach is already there, which is good. I'll keep claude-opus-4-7 as specified since that's current, but frame the tech stack as suggestions rather than requirements so there's room to adapt. I can drop the specific JSON library call and let the implementation choose. The prompt itself feels solid, so I'll just clean up the presentation and lead with a single framing sentence before the full spec. I'm checking the length and deciding whether the full prompt fits appropriately—it's pushing toward two mobile screens, but since the user specifically asked for a usable prompt, completeness matters more than brevity here.Here you go — paste this into a fresh Claude Code session in an empty directory:

````markdown
# Project: Claude Migration Kit Builder

## Context
I'm migrating from a personal Claude.ai account to a Hrvatski Telekom Enterprise Claude account on a different email domain. Anthropic provides no automated path between accounts on different domains, and there is no public claude.ai API for reading projects/conversations or writing them back. The Enterprise side will be rebuilt manually; this tool's job is to make that rebuild as fast and selective as possible.

## Input
The official Claude data export — a `.dms` file (renamed ZIP) containing `conversations.json` plus any project knowledge files. I'll provide the path when you ask.

## Output: a "migration kit" folder
```
migration-kit/
  README.md                  # step-by-step Enterprise rebuild instructions
  memory-seed.md             # 10–15 standing facts to paste into a fresh Enterprise chat
  settings-checklist.md      # connectors / preferences / styles to recreate manually
  projects/
    <project-slug>/
      instructions.md        # original custom instructions, verbatim
      knowledge/             # original attached files
      context-digest.md      # decisions, current state, open threads
      conversations/         # full markdown transcripts of kept chats (reference)
  standalone/
    <conversation-slug>.md   # non-project chats worth keeping
  inventory.json             # machine-readable record
  selection.toml             # filter rules used (for re-runs)
```

## Phases — implement and validate one at a time

**Phase 1 — Inventory.** Parse the export. For every project: title, full custom instructions, knowledge files, conversations (title, message count, first/last dates, rough token estimate). Same for standalone conversations. Print a summary table; write `inventory.json`. Stop and let me confirm before going further.

**Phase 2 — Selection.** Generate `selection.toml` with sensible defaults. Support: include/exclude project by slug, include/exclude conversation by id, date floor, minimum message count, keyword exclusion list. I edit the file; you re-run with `--apply-selection`.

**Phase 3 — Kit generation.** For each kept project: copy instructions verbatim, copy knowledge files, render kept conversations to clean markdown, then generate `context-digest.md` by calling the Anthropic API (model: `claude-opus-4-7`) with the conversations and a prompt producing: key decisions, current state, open threads, important artifacts referenced — cap ~600 words. After all projects, generate cross-project `memory-seed.md` and `settings-checklist.md`. Estimate API cost before starting and ask me to confirm.

## Tech (suggested — push back if you have a better idea)
- Python, `uv` for dependency management
- `anthropic` SDK, `typer` for CLI, `rich` for output, `pydantic` for schemas
- API key from `ANTHROPIC_API_KEY` env var; fail clearly if missing

## Hard constraints
- No browser automation, session cookies, or unofficial claude.ai endpoints. Only the official export file and the official Anthropic API.
- Treat all exported content as confidential business data. No telemetry, no third-party calls except to api.anthropic.com.
- API key via env var only — never written to config or committed.
- Don't auto-commit anything; leave git decisions to me.

## How to start
1. Set up the project skeleton (`uv init` + dependencies).
2. Sketch the data model from what's known about the export structure (conversations.json with embedded project metadata, knowledge files alongside). Adjust once I provide the actual file.
3. Implement Phase 1 end-to-end, run it on my export, show me the inventory. Do not start Phase 2 until I confirm.

Ask me for the export file path when you're ready.
````

Two things to do before you paste it: run the data export from your personal account so the file is downloaded by the time Claude Code asks for it, and have an `ANTHROPIC_API_KEY` ready (Console → Settings → API Keys) since Phase 3 needs it for the digests. Cost should land in single-digit dollars unless you have hundreds of long conversations.
