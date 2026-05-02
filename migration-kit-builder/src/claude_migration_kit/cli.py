"""Typer CLI for the migration kit builder."""

from __future__ import annotations

import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import anthropic
import tomli_w
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .classifier import (
    BATCH_SIZE,
    INPUT_PRICE_PER_M,
    MODEL,
    OUTPUT_PRICE_PER_M,
    STANDALONE_SLUG,
    Mapping,
    UsageTotals,
    build_catalog,
    build_payload,
    chunked,
    classify_batch,
    estimate_full_run,
    render_system_prompt,
)
from .inventory import build_inventory
from .models import ConversationSummary, Inventory
from .parser import ParseError, parse_export

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    help="Build a manual-rebuild kit from a Claude data export.",
)
console = Console()


def _render_inventory(inv: Inventory) -> None:
    totals = inv.totals
    console.print(
        Panel.fit(
            f"[bold]Export:[/bold] {inv.export_path}\n"
            f"[bold]Projects:[/bold] {totals['projects']}    "
            f"[bold]Conversations:[/bold] {totals['conversations']} "
            f"(standalone: {totals['standalone_conversations']})\n"
            f"[bold]Messages:[/bold] {totals['messages']:,}    "
            f"[bold]Est. tokens:[/bold] {totals['estimated_tokens']:,}",
            title="Inventory summary",
        )
    )

    if inv.projects:
        t = Table(title="Projects", show_lines=False)
        t.add_column("Slug", style="cyan", no_wrap=True)
        t.add_column("Name")
        t.add_column("Instr", justify="right")
        t.add_column("Knwl", justify="right")
        t.add_column("Convs", justify="right")
        t.add_column("Msgs", justify="right")
        t.add_column("Est. tokens", justify="right")
        for p in inv.projects:
            msgs = sum(c.message_count for c in p.conversations)
            tokens = sum(c.estimated_tokens for c in p.conversations)
            t.add_row(
                p.slug,
                p.name,
                "yes" if p.has_instructions else "—",
                str(len(p.knowledge_files)),
                str(len(p.conversations)),
                f"{msgs:,}",
                f"{tokens:,}",
            )
        console.print(t)

    if inv.standalone_conversations:
        t = Table(title=f"Standalone conversations ({len(inv.standalone_conversations)})")
        t.add_column("Last", style="dim", no_wrap=True)
        t.add_column("Msgs", justify="right")
        t.add_column("Est. tokens", justify="right")
        t.add_column("Title")
        for c in inv.standalone_conversations[:25]:
            last = c.last_message_at.date().isoformat() if c.last_message_at else "—"
            t.add_row(
                last,
                str(c.message_count),
                f"{c.estimated_tokens:,}",
                c.title[:80],
            )
        if len(inv.standalone_conversations) > 25:
            t.caption = f"showing 25 of {len(inv.standalone_conversations)}"
        console.print(t)


@app.command("inventory")
def inventory_cmd(
    export: Annotated[
        Path,
        typer.Argument(
            exists=True,
            readable=True,
            help="Path to the Claude export (.dms / .zip / unpacked folder).",
        ),
    ],
    out_dir: Annotated[
        Path,
        typer.Option("--out", "-o", help="Output directory for the migration kit."),
    ] = Path("migration-kit"),
) -> None:
    """Phase 1: parse the export, print a summary, write inventory.json."""
    try:
        parsed = parse_export(export)
    except ParseError as exc:
        console.print(f"[red]Parse error:[/red] {exc}")
        raise typer.Exit(2)

    inv = build_inventory(parsed)
    _render_inventory(inv)

    out_dir.mkdir(parents=True, exist_ok=True)
    inv_path = out_dir / "inventory.json"
    inv_path.write_text(inv.model_dump_json(indent=2), encoding="utf-8")
    console.print(f"\n[green]Wrote[/green] {inv_path}")
    console.print(
        "[dim]Review the summary, then confirm before moving to Phase 2 "
        "(selection).[/dim]"
    )


def _write_mappings_toml(
    out_path: Path,
    mappings: list[Mapping],
    usage: UsageTotals,
    threshold: float,
) -> None:
    """Write mappings.toml, lowest-confidence first so review work is at the top."""
    sorted_mappings = sorted(mappings, key=lambda m: (m.confidence, m.title))
    doc: dict[str, object] = {
        "meta": {
            "model": MODEL,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "threshold": threshold,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_creation_input_tokens": usage.cache_creation_input_tokens,
            "cache_read_input_tokens": usage.cache_read_input_tokens,
            "estimated_cost_usd": round(usage.cost_usd(), 4),
        }
    }
    convs: dict[str, dict[str, object]] = {}
    for m in sorted_mappings:
        convs[m.conversation_id] = {
            "title": m.title,
            "project_slug": m.project_slug,
            "confidence": round(m.confidence, 3),
            "reason": m.reason,
            "needs_review": m.confidence < threshold,
        }
    doc["conversations"] = convs
    out_path.write_bytes(tomli_w.dumps(doc).encode("utf-8"))


def _render_classify_summary(
    mappings: list[Mapping], threshold: float, usage: UsageTotals
) -> None:
    counts = Counter(m.project_slug for m in mappings)
    review_counts = Counter(
        m.project_slug for m in mappings if m.confidence < threshold
    )
    t = Table(title="Conversations per project")
    t.add_column("Slug", style="cyan", no_wrap=True)
    t.add_column("Kept", justify="right")
    t.add_column("Needs review", justify="right", style="yellow")
    for slug in sorted(counts):
        t.add_row(slug, str(counts[slug]), str(review_counts.get(slug, 0)))
    console.print(t)

    weakest = sorted(mappings, key=lambda m: m.confidence)[:10]
    t = Table(title=f"Lowest-confidence assignments (top {len(weakest)})")
    t.add_column("Conf", justify="right")
    t.add_column("Slug", style="cyan", no_wrap=True)
    t.add_column("Title")
    t.add_column("Reason", style="dim")
    for m in weakest:
        t.add_row(
            f"{m.confidence:.2f}",
            m.project_slug,
            m.title[:60],
            m.reason[:80],
        )
    console.print(t)

    console.print(
        Panel.fit(
            f"[bold]Tokens[/bold]  in: {usage.input_tokens:,}  "
            f"out: {usage.output_tokens:,}  "
            f"cache write: {usage.cache_creation_input_tokens:,}  "
            f"cache read: {usage.cache_read_input_tokens:,}\n"
            f"[bold]Actual cost:[/bold] ${usage.cost_usd():.4f}",
            title="Run accounting",
        )
    )


@app.command("classify")
def classify_cmd(
    export: Annotated[
        Path,
        typer.Argument(
            exists=True,
            readable=True,
            help="Path to the Claude export (.dms / .zip / unpacked folder).",
        ),
    ],
    out_dir: Annotated[
        Path,
        typer.Option("--out", "-o", help="Output directory for the migration kit."),
    ] = Path("migration-kit"),
    apply: Annotated[
        bool,
        typer.Option("--apply", help="Run the full classification and write mappings.toml."),
    ] = False,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            help="Classify 3 sample conversations and print estimated full-run cost. (Default.)",
        ),
    ] = False,
    threshold: Annotated[
        float,
        typer.Option(
            "--threshold",
            help="Confidence below which a mapping is flagged needs_review.",
        ),
    ] = 0.6,
) -> None:
    """Phase 1.5: classify conversations against projects (or 'standalone')."""
    if apply == dry_run:
        # If both true or both false, default to dry-run (safer).
        dry_run, apply = True, False

    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print(
            "[red]ANTHROPIC_API_KEY is not set.[/red] "
            "Export it before running this command."
        )
        raise typer.Exit(2)

    try:
        parsed = parse_export(export)
    except ParseError as exc:
        console.print(f"[red]Parse error:[/red] {exc}")
        raise typer.Exit(2)

    inv = build_inventory(parsed)
    if not inv.projects:
        console.print(
            "[yellow]No projects found in the export — nothing to classify against.[/yellow]"
        )
        raise typer.Exit(1)

    slugs_by_uuid = {p.uuid: p.slug for p in inv.projects}
    catalog = build_catalog(parsed.projects, slugs_by_uuid)
    system_prompt = render_system_prompt(catalog)
    valid_slugs = {entry.slug for entry in catalog} | {STANDALONE_SLUG}

    convs = parsed.conversations
    payloads = [build_payload(c) for c in convs]
    client = anthropic.Anthropic()

    if dry_run:
        console.print(
            Panel.fit(
                f"[bold]Catalog:[/bold] {len(catalog)} projects + standalone\n"
                f"[bold]Conversations:[/bold] {len(convs)}\n"
                f"[bold]Batches:[/bold] {(len(convs) + BATCH_SIZE - 1) // BATCH_SIZE}"
                f" of {BATCH_SIZE}\n"
                f"[bold]Model:[/bold] {MODEL}",
                title="Dry-run plan",
            )
        )
        try:
            est_in, est_out, est_cost = estimate_full_run(
                client, system_prompt, payloads
            )
        except anthropic.APIStatusError as exc:
            console.print(f"[red]Token-count call failed:[/red] {exc}")
            raise typer.Exit(2)

        console.print(
            f"[bold]Estimated full-run tokens:[/bold] in {est_in:,} / out {est_out:,}"
        )
        console.print(
            f"[bold]Estimated full-run cost:[/bold] ${est_cost:.4f}  "
            f"(input ${est_in/1_000_000*INPUT_PRICE_PER_M:.4f} + "
            f"output ${est_out/1_000_000*OUTPUT_PRICE_PER_M:.4f})"
        )

        sample = payloads[:3]
        if not sample:
            console.print("[yellow]No conversations to classify.[/yellow]")
            raise typer.Exit(0)

        console.print("\n[bold]Classifying 3 sample conversations…[/bold]")
        try:
            sample_mappings, sample_usage = classify_batch(
                client, system_prompt, sample, valid_slugs
            )
        except anthropic.APIStatusError as exc:
            console.print(f"[red]API error:[/red] {exc}")
            raise typer.Exit(2)

        usage = UsageTotals()
        usage.add(sample_usage)
        t = Table(title="Sample classifications")
        t.add_column("Conf", justify="right")
        t.add_column("Slug", style="cyan", no_wrap=True)
        t.add_column("Title")
        t.add_column("Reason", style="dim")
        for m in sample_mappings:
            t.add_row(
                f"{m.confidence:.2f}",
                m.project_slug,
                m.title[:60],
                m.reason[:80],
            )
        console.print(t)
        console.print(
            f"[dim]Sample call cost: ${usage.cost_usd():.4f} "
            f"(in {usage.input_tokens:,} / out {usage.output_tokens:,} tokens).[/dim]"
        )
        console.print(
            "\n[green]Dry-run complete.[/green] Re-run with [bold]--apply[/bold] "
            "to classify all conversations and write mappings.toml."
        )
        return

    # --apply: full run
    console.print(
        f"[bold]Classifying {len(convs)} conversations "
        f"in {(len(convs) + BATCH_SIZE - 1) // BATCH_SIZE} batches…[/bold]"
    )
    usage = UsageTotals()
    all_mappings: list[Mapping] = []
    for i, batch in enumerate(chunked(payloads, BATCH_SIZE), 1):
        try:
            mappings, batch_usage = classify_batch(
                client, system_prompt, batch, valid_slugs
            )
        except anthropic.APIStatusError as exc:
            console.print(f"[red]Batch {i} failed:[/red] {exc}")
            raise typer.Exit(2)
        usage.add(batch_usage)
        all_mappings.extend(mappings)
        console.print(
            f"  batch {i}: {len(mappings)} classified  "
            f"(running cost ${usage.cost_usd():.4f})"
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    mappings_path = out_dir / "mappings.toml"
    _write_mappings_toml(mappings_path, all_mappings, usage, threshold)
    console.print(f"\n[green]Wrote[/green] {mappings_path}")

    _render_classify_summary(all_mappings, threshold, usage)
    console.print(
        "[dim]Edit mappings.toml by hand for anything that looks wrong, "
        "then proceed to Phase 2 (selection).[/dim]"
    )


def _resolve_inventory(out_dir: Path, export: Path) -> Inventory:
    """Load inventory.json from out_dir, rebuilding from export if missing."""
    inv_path = out_dir / "inventory.json"
    if inv_path.exists():
        return Inventory.model_validate_json(inv_path.read_text(encoding="utf-8"))
    parsed = parse_export(export)
    return build_inventory(parsed)


def _render_selection_preview(
    result: "SelectionResult",
    views_by_id: dict[str, "ConversationView"],
) -> None:
    by_project_kept: dict[str, list[ConversationSummary]] = {}
    by_project_dropped: dict[str, int] = {}
    for c in result.kept:
        slug = views_by_id[c.uuid].project_slug
        by_project_kept.setdefault(slug, []).append(c)
    for c, _ in result.dropped:
        slug = views_by_id[c.uuid].project_slug
        by_project_dropped[slug] = by_project_dropped.get(slug, 0) + 1

    t = Table(title="Selection result by project")
    t.add_column("Slug", style="cyan", no_wrap=True)
    t.add_column("Kept", justify="right")
    t.add_column("Dropped", justify="right", style="dim")
    t.add_column("Kept tokens", justify="right")
    all_slugs = sorted(set(by_project_kept) | set(by_project_dropped))
    total_kept_tokens = 0
    for slug in all_slugs:
        kept = by_project_kept.get(slug, [])
        tokens = sum(c.estimated_tokens for c in kept)
        total_kept_tokens += tokens
        t.add_row(slug, str(len(kept)), str(by_project_dropped.get(slug, 0)), f"{tokens:,}")
    console.print(t)

    drop_reasons: dict[str, int] = {}
    for _, reason in result.dropped:
        drop_reasons[reason] = drop_reasons.get(reason, 0) + 1
    if drop_reasons:
        t = Table(title="Drop reasons")
        t.add_column("Reason")
        t.add_column("Count", justify="right")
        for reason, n in sorted(drop_reasons.items(), key=lambda kv: -kv[1]):
            t.add_row(reason, str(n))
        console.print(t)

    console.print(
        Panel.fit(
            f"[bold]Kept:[/bold] {len(result.kept)}    "
            f"[bold]Dropped:[/bold] {len(result.dropped)}    "
            f"[bold]Kept est. tokens:[/bold] {total_kept_tokens:,}",
            title="Totals",
        )
    )


@app.command("select")
def select_cmd(
    export: Annotated[
        Path,
        typer.Argument(
            exists=True,
            readable=True,
            help="Path to the Claude export — used to rebuild inventory if missing.",
        ),
    ],
    out_dir: Annotated[
        Path,
        typer.Option("--out", "-o", help="Output directory (must contain mappings.toml)."),
    ] = Path("migration-kit"),
    apply_selection: Annotated[
        bool,
        typer.Option(
            "--apply-selection",
            help="Apply the rules in selection.toml and print a preview. "
            "Default behavior writes a fresh selection.toml with defaults.",
        ),
    ] = False,
) -> None:
    """Phase 2: write/apply selection.toml to filter what enters the kit."""
    from .selection import (
        ConversationView,
        Selection,
        SelectionResult,
        apply,
        build_views,
        render_default,
    )

    mappings_path = out_dir / "mappings.toml"
    if not mappings_path.exists():
        console.print(
            f"[red]Missing[/red] {mappings_path}. "
            "Run [bold]classify --apply[/bold] first."
        )
        raise typer.Exit(2)

    try:
        inv = _resolve_inventory(out_dir, export)
    except ParseError as exc:
        console.print(f"[red]Parse error:[/red] {exc}")
        raise typer.Exit(2)

    import tomllib

    mappings_doc = tomllib.loads(mappings_path.read_text(encoding="utf-8"))
    views = build_views(inv, mappings_doc)
    views_by_id = {v.summary.uuid: v for v in views}

    selection_path = out_dir / "selection.toml"

    if not apply_selection:
        slugs = sorted({p.slug for p in inv.projects} | {"standalone"})
        out_dir.mkdir(parents=True, exist_ok=True)
        if selection_path.exists():
            console.print(
                f"[yellow]Refusing to overwrite[/yellow] {selection_path}. "
                "Delete it first if you want fresh defaults."
            )
            raise typer.Exit(1)
        selection_path.write_text(render_default(slugs), encoding="utf-8")
        console.print(f"[green]Wrote[/green] {selection_path}")
        console.print(
            "[dim]Edit it, then re-run with [bold]--apply-selection[/bold] "
            "to preview the kept set.[/dim]"
        )
        return

    if not selection_path.exists():
        console.print(
            f"[red]Missing[/red] {selection_path}. "
            "Run [bold]select[/bold] (without --apply-selection) first to generate defaults."
        )
        raise typer.Exit(2)

    sel = Selection.from_toml(selection_path)
    result = apply(views, sel)
    _render_selection_preview(result, views_by_id)
    console.print(
        f"[dim]Edit {selection_path} and re-run --apply-selection to iterate. "
        "Phase 3 (build) will use the same selection.toml.[/dim]"
    )


@app.command("build")
def build_cmd(
    export: Annotated[
        Path,
        typer.Argument(
            exists=True,
            readable=True,
            help="Path to the Claude export.",
        ),
    ],
    out_dir: Annotated[
        Path,
        typer.Option("--out", "-o", help="Output directory for the migration kit."),
    ] = Path("migration-kit"),
) -> None:
    """Phase 3: materialize the kit on disk.

    Writes the directory structure, copies instructions/knowledge, renders
    conversations, and creates skeleton files for context-digest /
    memory-seed / settings-checklist. Does NOT call the API. The synthesis
    step (LLM-driven) is left for a follow-up.
    """
    from . import build as build_mod
    from .selection import Selection, apply, build_views
    import tomllib

    mappings_path = out_dir / "mappings.toml"
    selection_path = out_dir / "selection.toml"
    if not mappings_path.exists() or not selection_path.exists():
        console.print(
            f"[red]Missing[/red] {mappings_path} or {selection_path}. "
            "Run [bold]classify --apply[/bold] and [bold]select[/bold] first."
        )
        raise typer.Exit(2)

    try:
        parsed = parse_export(export)
    except ParseError as exc:
        console.print(f"[red]Parse error:[/red] {exc}")
        raise typer.Exit(2)

    inv = build_inventory(parsed)
    mappings_doc = tomllib.loads(mappings_path.read_text(encoding="utf-8"))
    sel = Selection.from_toml(selection_path)
    views = build_views(inv, mappings_doc)
    result = apply(views, sel)
    kept_ids = {c.uuid for c in result.kept}

    # Index: uuid -> Conversation, slug -> Project
    convs_by_id = {c.uuid: c for c in parsed.conversations}
    parsed_projects_by_uuid = {p.uuid: p for p in parsed.projects}
    projects_by_slug = {
        ps.slug: parsed_projects_by_uuid[ps.uuid]
        for ps in inv.projects
        if ps.uuid in parsed_projects_by_uuid
    }
    project_summaries_by_slug = {p.slug: p for p in inv.projects}

    # Conversation slug -> project slug from mappings
    slug_for_conv: dict[str, str] = {}
    for cid, info in mappings_doc.get("conversations", {}).items():
        if isinstance(info, dict):
            slug_for_conv[cid] = info.get("project_slug", "standalone")

    # Build per-project kept conversation lists
    by_project: dict[str, list] = {}
    standalone: list = []
    for cid in kept_ids:
        conv = convs_by_id.get(cid)
        if conv is None:
            continue
        slug = slug_for_conv.get(cid, "standalone")
        if slug == "standalone" or slug not in projects_by_slug:
            standalone.append(conv)
        else:
            by_project.setdefault(slug, []).append(conv)

    # Knowledge files from the loose archive set, re-keyed by project slug.
    from .parser import attach_knowledge_to_projects

    archive_kn = attach_knowledge_to_projects(
        parsed.projects, parsed.loose_knowledge_files
    )
    slug_by_uuid = {ps.uuid: ps.slug for ps in inv.projects}
    knowledge_by_slug: dict[str, list[tuple[str, bytes]]] = {}
    for uuid, files in archive_kn.items():
        slug = slug_by_uuid.get(uuid)
        if not slug or not files:
            continue
        knowledge_by_slug[slug] = [
            (member, parsed.loose_knowledge_files[member])
            for member, _size in files
            if member in parsed.loose_knowledge_files
        ]

    # Per-project memory from memories.json (keyed by uuid)
    project_memories_by_slug: dict[str, str] = {}
    if isinstance(parsed.memories, list) and parsed.memories:
        first = parsed.memories[0]
        if isinstance(first, dict):
            pm = first.get("project_memories") or {}
            if isinstance(pm, dict):
                for uuid, text in pm.items():
                    for ps in inv.projects:
                        if ps.uuid == uuid and isinstance(text, str):
                            project_memories_by_slug[ps.slug] = text

    out_dir.mkdir(parents=True, exist_ok=True)
    project_dirs: list[tuple[str, Path, int]] = []
    for slug, convs in sorted(by_project.items()):
        proj = projects_by_slug.get(slug)
        if proj is None:
            continue
        proj_dir = build_mod.write_project(
            out_dir=out_dir,
            project=proj,
            project_slug=slug,
            kept_conversations=sorted(
                convs,
                key=lambda c: c.updated_at or c.created_at or datetime.min.replace(tzinfo=timezone.utc),
                reverse=True,
            ),
            knowledge_files_from_archive=knowledge_by_slug.get(slug),
            project_memory=project_memories_by_slug.get(slug),
        )
        project_dirs.append((slug, proj_dir, len(convs)))
        console.print(
            f"  wrote projects/{slug}/  ({len(convs)} convs, "
            f"{len(proj.docs)} docs)"
        )

    used_standalone: set[str] = set()
    for conv in sorted(
        standalone,
        key=lambda c: c.updated_at or c.created_at or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    ):
        build_mod.write_standalone(out_dir, conv, used_standalone)
    console.print(f"  wrote standalone/  ({len(standalone)} convs)")

    # Memory seed — start from the verbatim conversations_memory if present,
    # otherwise leave a placeholder.
    memory_text: str | None = None
    if isinstance(parsed.memories, list) and parsed.memories:
        first = parsed.memories[0]
        if isinstance(first, dict):
            cm = first.get("conversations_memory")
            if isinstance(cm, str) and cm.strip():
                memory_text = cm.strip()

    if memory_text:
        memory_md = (
            "# Memory seed\n\n"
            "Paste the section below into a fresh Enterprise chat with the "
            "instruction: *\"Save this as standing memory for our future "
            "conversations.\"* Trim or rewrite anything you don't want carried "
            "over.\n\n"
            "---\n\n"
            f"{memory_text}\n"
        )
    else:
        memory_md = (
            "# Memory seed\n\n"
            "_(memories.json was empty or absent — synthesize 10–15 standing "
            "facts manually from the project digests.)_\n"
        )
    (out_dir / "memory-seed.md").write_text(memory_md, encoding="utf-8")
    console.print("  wrote memory-seed.md")

    (out_dir / "settings-checklist.md").write_text(
        build_mod.render_settings_checklist(parsed.memories), encoding="utf-8"
    )
    console.print("  wrote settings-checklist.md")

    (out_dir / "README.md").write_text(
        build_mod.render_readme(out_dir, project_dirs, len(standalone), bool(memory_text)),
        encoding="utf-8",
    )
    console.print("  wrote README.md")

    console.print(
        f"\n[green]Mechanical build complete.[/green] {len(by_project)} projects, "
        f"{sum(n for _, _, n in project_dirs)} project conversations, "
        f"{len(standalone)} standalone."
    )
    console.print(
        "[dim]Per-project context-digest.md is a placeholder — fill it via "
        "API call or in-chat synthesis.[/dim]"
    )


def main() -> None:
    app()


if __name__ == "__main__":
    main()
