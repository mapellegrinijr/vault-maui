#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from maui_common import (
    add_artifact,
    add_info,
    base_report,
    exit_code,
    mark_critical,
    mark_warning,
    parse_frontmatter,
    print_markdown,
    read_text,
    rel,
    resolve_path,
    write_report_bundle,
)


REQUIRED_FIELDS = ["titulo", "versao", "status", "data_criacao", "idioma", "tipo", "escopo"]
ALLOWED_STATUS = {"proposta", "ativo", "submitted", "reviewed", "deprecated", "rascunho", "arquivado"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validação de frontmatter Markdown Maui")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--scope", default="vault-maui", help="Diretório ou arquivo Markdown")
    return parser.parse_args()


def iter_markdown(scope):
    if scope.is_file() and scope.suffix == ".md":
        yield scope
    elif scope.is_dir():
        yield from sorted(scope.rglob("*.md"))


def is_normative(path) -> bool:
    parts = set(path.parts)
    return "00_core" in parts or "01_manifest" in parts


def main() -> int:
    args = parse_args()
    scope = resolve_path(args.scope)
    report = base_report(
        "maui_validate_frontmatter.py",
        rel(scope),
        {"dry_run": args.dry_run, "write_report": args.write_report, "scope": args.scope},
    )
    files = list(iter_markdown(scope))
    if not files:
        mark_critical(report, f"nenhum Markdown encontrado em {rel(scope)}")
    for path in files:
        data, _ = parse_frontmatter(read_text(path))
        if not data:
            mark_critical(report, f"sem frontmatter: {rel(path)}")
            continue
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            mark_critical(report, f"campos obrigatórios ausentes em {rel(path)}: {', '.join(missing)}")
        status = str(data.get("status", ""))
        if status and status not in ALLOWED_STATUS:
            mark_critical(report, f"status não permitido em {rel(path)}: {status}")
        if is_normative(path) and "precedencia" not in data:
            mark_warning(report, f"normativo sem precedencia explícita: {rel(path)}")
        if "confidencialidade" not in data:
            mark_warning(report, f"sem confidencialidade explícita: {rel(path)}")
    add_info(report, f"arquivos Markdown verificados: {len(files)}")
    for path in write_report_bundle(
        report=report,
        title="Maui Frontmatter Validation",
        stem="maui-validate-frontmatter",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Frontmatter Validation", report)
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)
