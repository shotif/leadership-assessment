# Migration kit

Manual rebuild kit for an Enterprise Claude account, generated from a
Claude data export.

**Step-by-step playbook:** [`REBUILD.md`](./REBUILD.md) — copy-paste
prompts and the exact order to do everything in Enterprise.

## Rebuild order

1. **Sign in** to the new Enterprise account.
2. **Recreate each project** under `projects/`:
   - Copy `instructions.md` into the project's custom instructions
     (verbatim).
   - Upload everything in `knowledge/` as project knowledge.
   - Once the project exists in Enterprise, **paste
     `context-digest.md` into the first chat under that project** and
     ask Claude to "save this as standing context for this project."
     This primes the project's project-memory with the synthesis from
     the source account so you don't start from scratch.
3. **Seed account-level memory** by pasting `memory-seed.md` into a
   fresh non-project chat with the instruction *"save this as standing
   memory for our future conversations."*
4. **Recreate connectors / styles / skills** manually using
   `settings-checklist.md` — the API doesn't expose these, so they
   need to be re-set by hand.
5. **Use the standalone transcripts in `standalone/`** as reference if
   you need to look up something specific from a past chat that wasn't
   tied to a project. They're not meant to be replayed into Enterprise.

## What's included

### Projects (5)

| Folder | Convs | Has knowledge | Has instructions |
|---|---:|---:|---|
| `projects/big-picture/` | 12 | yes (2 docs) | — |
| `projects/cico/` | 6 | — | — |
| `projects/ht-future-operating-model/` | 2 | — | — |
| `projects/petaik/` | 2 | — | — |
| `projects/qbr-next-level/` | 2 | yes (1 doc) | yes (TRAIIN advisor) |

Each project folder has `instructions.md`, `knowledge/`,
`context-digest.md`, and `conversations/<slug>.md` for every kept chat.

### Standalone

- `standalone/` — 28 kept non-project conversations (work tasks that
  didn't pattern-match a project, plus a few personal-coding items).

### Cross-cutting

- `memory-seed.md` — work-context memory ready to paste into
  Enterprise. Trimmed to remove personal-life items.
- `settings-checklist.md` — manual reset list (connectors, styles,
  custom skills, etc.).
- `REBUILD.md` — the full playbook with copy-paste prompts.

## Notes

- Conversation transcripts include only `human` / `assistant` text
  turns. Tool use, generated artifacts (HTML / PPTX / DOCX), and
  attached files are not preserved by the export.
- The `coaching` project (private) is excluded by selection.
- A 1.5-step **conversation → project mapping** had to be reconstructed
  in this export — the source format dropped the `project_uuid` field
  on conversations. See `mappings.toml` for the reconstructed
  assignments.
- `selection.toml` records the filter rules used (date floor, min
  message count, keyword excludes). Re-run
  `claude-migration-kit build` with the same selection to reproduce
  this kit.

## Contents at a glance

```
migration-kit/
├── README.md                   ← you are here
├── REBUILD.md                  ← step-by-step playbook with prompts
├── inventory.json              ← machine-readable Phase-1 inventory
├── mappings.toml               ← conversation → project assignments
├── selection.toml              ← filter rules used
├── memory-seed.md              ← paste into a fresh Enterprise chat
├── settings-checklist.md       ← manual UI tasks
├── projects/
│   └── <slug>/
│       ├── instructions.md
│       ├── context-digest.md   ← paste into first chat in the project
│       ├── knowledge/
│       └── conversations/
└── standalone/
    └── <slug>.md               ← non-project transcripts for reference
```
