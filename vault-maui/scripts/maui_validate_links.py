#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from maui_common import (
    VAULT_ROOT,
    WORKSPACE_ROOT,
    add_artifact,
    add_info,
    base_report,
    exit_code,
    mark_critical,
    mark_warning,
    print_markdown,
    read_text,
    rel,
    resolve_path,
    write_report_bundle,
)


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PATH_RE = re.compile(r"`?(vault-maui/[A-Za-z0-9_./-]+)`?")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detecção de wikilinks e caminhos quebrados")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--scope", default="vault-maui", help="Diretório ou arquivo Markdown")
    return parser.parse_args()


def iter_markdown(scope: Path):
    if scope.is_file() and scope.suffix == ".md":
        yield scope
    elif scope.is_dir():
        yield from sorted(scope.rglob("*.md"))


def build_stem_index() -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for path in VAULT_ROOT.rglob("*.md"):
        index.setdefault(path.stem, []).append(path)
    return index


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def is_normative(path: Path) -> bool:
    return "00_core" in path.parts or "01_manifest" in path.parts


def resolve_target(source: Path, target: str, stems: dict[str, list[Path]]) -> bool:
    target = target.strip().split("#", 1)[0].split("|", 1)[0].strip()
    if not target or is_external(target):
        return True
    if target in stems:
        return True
    candidates = []
    raw = Path(target)
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.extend([source.parent / raw, WORKSPACE_ROOT / raw, VAULT_ROOT / raw])
        if raw.suffix == "":
            candidates.extend([source.parent / f"{target}.md", VAULT_ROOT / f"{target}.md"])
    return any(candidate.exists() for candidate in candidates)


def main() -> int:
    args = parse_args()
    scope = resolve_path(args.scope)
    report = base_report(
        "maui_validate_links.py",
        rel(scope),
        {"dry_run": args.dry_run, "write_report": args.write_report, "scope": args.scope},
    )
    stems = build_stem_index()
    files = list(iter_markdown(scope))
    if not files:
        mark_critical(report, f"nenhum Markdown encontrado em {rel(scope)}")
    broken_count = 0
    for path in files:
        text = read_text(path)
        targets = []
        targets.extend(match.group(1) for match in WIKILINK_RE.finditer(text))
        targets.extend(match.group(1) for match in MD_LINK_RE.finditer(text))
        targets.extend(match.group(1) for match in PATH_RE.finditer(text))
        for target in targets:
            if resolve_target(path, target, stems):
                continue
            broken_count += 1
            message = f"link/caminho quebrado em {rel(path)}: {target}"
            if is_normative(path):
                mark_critical(report, message)
            else:
                mark_warning(report, message)
    add_info(report, f"arquivos Markdown verificados: {len(files)}")
    add_info(report, f"links/caminhos quebrados encontrados: {broken_count}")
    for path in write_report_bundle(
        report=report,
        title="Maui Link Validation",
        stem="maui-validate-links",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Link Validation", report)
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)

