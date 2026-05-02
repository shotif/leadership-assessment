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
from .models import Inventory
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


@app.command("select")
def select_cmd() -> None:
    """Phase 2: write selection.toml from the inventory. (Not implemented yet.)"""
    console.print("[yellow]Phase 2 not implemented yet.[/yellow]")
    raise typer.Exit(1)


@app.command("build")
def build_cmd() -> None:
    """Phase 3: render the migration kit. (Not implemented yet.)"""
    console.print("[yellow]Phase 3 not implemented yet.[/yellow]")
    raise typer.Exit(1)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
