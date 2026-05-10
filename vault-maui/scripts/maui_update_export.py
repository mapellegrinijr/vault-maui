#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys

from maui_common import (
    VAULT_ROOT,
    add_artifact,
    add_info,
    base_report,
    exit_code,
    mark_critical,
    print_markdown,
    read_text,
    rel,
    resolve_path,
    safe_write_text,
    slugify,
    today,
    write_report_bundle,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Criação de Update Package via Update Request")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--request", required=True, help="Arquivo de Update/Exec Request")
    return parser.parse_args()


def field_value(text: str, field: str) -> str:
    match = re.search(rf"^- {re.escape(field)}:[ \t]*([^\n]*)$", text, re.MULTILINE)
    value = match.group(1).strip() if match else ""
    return value


def build_package(request_path, text: str) -> tuple[str, str, bool]:
    request_id = field_value(text, "ID") or request_path.stem
    title = field_value(text, "Titulo") or "Update Package Maui"
    human_gate = any(token in text.lower() for token in ("00_core", "01_manifest", "normativo", "status: proposta"))
    package = "\n".join(
        [
            f"# Update Package — {title}",
            "",
            f"- Request: `{rel(request_path)}`",
            f"- ID: `{request_id}`",
            f"- Human Gate: `{human_gate}`",
            "",
            "## Escopo",
            "",
            "Gerado a partir do Update Request informado. Revisar manualmente antes de aplicar.",
            "",
            "## Riscos",
            "",
            "- Mudanças normativas exigem Human Gate dedicado.",
            "- Confirmar HEAD antes de aplicar.",
            "",
            "## Rollback",
            "",
            "- Reverter o commit do pacote se a aplicação produzir drift.",
            "",
        ]
    )
    manifest = "\n".join(
        [
            f"id: {request_id}",
            f"title: {title}",
            f"request: {rel(request_path)}",
            f"human_gate: {str(human_gate).lower()}",
            f"generated_at: {today()}",
            "",
        ]
    )
    return package, manifest, human_gate


def main() -> int:
    args = parse_args()
    request_path = resolve_path(args.request)
    report = base_report(
        "maui_update_export.py",
        rel(request_path),
        {"dry_run": args.dry_run, "write_report": args.write_report, "request": args.request},
    )
    if not request_path.exists() or not request_path.is_file():
        mark_critical(report, f"request ausente: {rel(request_path)}")
        print_markdown("Maui Update Export", report)
        return exit_code(report)
    text = read_text(request_path)
    required_sections = ["## Objetivo", "## Escopo permitido", "## Criterios de aceite"]
    for section in required_sections:
        if section not in text:
            mark_critical(report, f"request inválido: seção ausente {section}")
    if report["ok"]:
        package, manifest, human_gate = build_package(request_path, text)
        add_info(report, f"human_gate: {human_gate}")
        if args.write_report and not args.dry_run:
            stem = slugify(field_value(text, "ID") or request_path.stem)
            out_dir = VAULT_ROOT / "validations" / "exports"
            package_path = out_dir / f"update-package-{stem}-{today()}.md"
            manifest_path = out_dir / f"update-package-{stem}-{today()}-manifest.yaml"
            safe_write_text(package_path, package)
            safe_write_text(manifest_path, manifest)
            add_artifact(report, package_path)
            add_artifact(report, manifest_path)
        print(package)
    for path in write_report_bundle(
        report=report,
        title="Maui Update Export",
        stem="maui-update-export",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Update Export", report)
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)
