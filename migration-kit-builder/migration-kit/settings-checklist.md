# Settings checklist

Things to recreate manually in the Enterprise UI. Anthropic's API doesn't expose these, so they need to be re-set by hand.

## Account
- [ ] Display name and avatar
- [ ] Default response language preference
- [ ] Personal preferences / response style (concise, formal, etc.)

## Connectors
- [ ] Re-authorize any MCP / connector integrations from the source account (Google Drive, GitHub, etc.). Anthropic does not transfer OAuth grants between accounts.

## Custom styles
- [ ] Recreate any custom writing styles you'd defined.

## Skills
- [ ] Re-upload any custom skills you used (e.g. T-Brand designer, skill-creator). Source skill files are not in the export.

## Projects
- [ ] For each project under `projects/`, copy `instructions.md` into the new project's custom instructions and upload `knowledge/`.

## Memory
- [ ] Paste `memory-seed.md` into a fresh Enterprise chat with the instruction: *"Save this as standing memory for future conversations."*
- [ ] (Optional) For projects with rich pre-existing memory, paste the project's `context-digest.md` into the first chat under that project to prime its memory.
