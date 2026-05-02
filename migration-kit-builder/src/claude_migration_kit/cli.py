"""Typer CLI for the migration kit builder."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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
