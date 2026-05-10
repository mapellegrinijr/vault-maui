#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from maui_common import (
    VAULT_ROOT,
    add_artifact,
    add_info,
    base_report,
    exit_code,
    mark_critical,
    mark_warning,
    print_markdown,
    rel,
    resolve_path,
    write_report_bundle,
)


REQUIRED_DIRS = [
    "00_core",
    "01_manifest",
    "schemas",
    "exec-reports/submitted",
    "context-packages/current",
    "project/roadmap",
    "project-memories",
    "memorias",
    "status",
    "status-project",
]
REQUIRED_DOCS = [
    "00_core/system-prompt-maui.md",
    "00_core/especificacao-completa-maui.md",
    "00_core/contrato-precedencia-maui.md",
    "00_core/principios-fundacionais-maui.md",
    "00_core/indice-maui.md",
    "00_core/spec-parametrizacao-maui.md",
    "01_manifest/spec-parametrizacao-maui.json",
    "project/roadmap/roadmap-desenvolvimento-maui-v1-0.md",
    "status-project/STATUS-UPDATE-maui.md",
]
REQUIRED_SCHEMAS = [
    "schemas/common-frontmatter.schema.yaml",
    "schemas/exec-report.schema.yaml",
    "schemas/exec-request.schema.yaml",
    "schemas/handoff-sessao.schema.yaml",
    "schemas/review-report.schema.yaml",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Health-check de estrutura do vault Maui")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--target", default=str(VAULT_ROOT), help="Path do vault Maui")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = resolve_path(args.target)
    report = base_report(
        "maui_vault_health.py",
        rel(target),
        {"dry_run": args.dry_run, "write_report": args.write_report, "target": args.target},
    )
    if not target.exists() or not target.is_dir():
        mark_critical(report, f"vault ausente ou inválido: {rel(target)}")
    for item in REQUIRED_DIRS:
        path = target / item
        if not path.is_dir():
            mark_critical(report, f"diretório obrigatório ausente: {rel(path)}")
    for item in REQUIRED_DOCS:
        path = target / item
        if not path.is_file():
            mark_critical(report, f"documento-base ausente: {rel(path)}")
    for item in REQUIRED_SCHEMAS:
        path = target / item
        if not path.is_file():
            mark_critical(report, f"schema P0 ausente: {rel(path)}")

    for runtime_dir in ("memorias", "status"):
        files = [p for p in (target / runtime_dir).rglob("*") if p.is_file()]
        unexpected = [p for p in files if p.name != "README.md"]
        if unexpected:
            mark_warning(report, f"{runtime_dir}/ contém arquivos além de README: {len(unexpected)}")

    add_info(report, f"diretórios verificados: {len(REQUIRED_DIRS)}")
    add_info(report, f"documentos-base verificados: {len(REQUIRED_DOCS)}")
    add_info(report, f"schemas verificados: {len(REQUIRED_SCHEMAS)}")
    for path in write_report_bundle(
        report=report,
        title="Maui Vault Health",
        stem="maui-vault-health",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Vault Health", report)
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)
