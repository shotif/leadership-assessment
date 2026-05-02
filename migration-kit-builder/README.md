# Claude Migration Kit Builder

Build a manual-rebuild kit from an official Claude data export so an
Enterprise Claude account on a different domain can be reconstructed
quickly and selectively.

This tool only reads the official export file and (later) calls the
official Anthropic API. No browser automation, no claude.ai endpoints.

## Install

```bash
uv sync
```

## Phase 1 — Inventory

```bash
uv run claude-migration-kit inventory path/to/export.dms --out migration-kit
```

Prints a project / conversation summary and writes `inventory.json` into
the output directory. Stop here, review, then proceed to Phase 2.

## Phases 2–3

Not yet implemented.

## Configuration

`ANTHROPIC_API_KEY` (env var) is required for Phase 3 only. Never written
to disk by this tool.
