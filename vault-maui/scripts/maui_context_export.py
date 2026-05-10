#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys

from maui_common import (
    VAULT_ROOT,
    add_artifact,
    add_info,
    base_report,
    exit_code,
    mark_warning,
    print_markdown,
    read_text,
    safe_write_text,
    today,
    write_report_bundle,
)


TARGETS = ("chatgpt-handoff", "claude-code", "codex")
BASE_SOURCES = [
    "status-project/STATUS-UPDATE-maui.md",
    "00_core/contrato-precedencia-maui.md",
    "00_core/principios-fundacionais-maui.md",
    "00_core/system-prompt-maui.md",
    "00_core/indice-maui.md",
    "01_manifest/spec-parametrizacao-maui.json",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Geração de context package por target")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--target", choices=TARGETS, required=True)
    parser.add_argument("--limit-tokens", type=int, default=4000)
    parser.add_argument("--scope", default="project")
    return parser.parse_args()


def truncate(text: str, limit_tokens: int) -> str:
    approx_chars = max(limit_tokens, 1) * 4
    if len(text) <= approx_chars:
        return text
    return text[:approx_chars] + "\n\n[TRUNCADO POR LIMITE]\n"


def build_package(target: str, limit_tokens: int) -> tuple[str, dict]:
    chunks = [
        f"# Maui Context Package — {target}",
        "",
        f"- Target: `{target}`",
        f"- Limite aproximado: {limit_tokens} tokens",
        "- Conformidade sem filesystem: `unknown` quando HEAD não for verificável.",
        "",
    ]
    manifest = {"target": target, "limit_tokens": limit_tokens, "sources": [], "unknown_without_filesystem": True}
    remaining = limit_tokens
    sources = []
    current_briefs = sorted((VAULT_ROOT / "context-packages" / "current").glob("*.md"))
    if current_briefs:
        sources.append(current_briefs[-1].relative_to(VAULT_ROOT).as_posix())
    sources.extend(BASE_SOURCES)
    for source in sources:
        path = VAULT_ROOT / source
        if not path.exists():
            continue
        content = read_text(path)
        budget = max(400, remaining // 2) if remaining > 0 else 400
        chunks.extend([f"## Fonte: `{source}`", "", truncate(content, budget), ""])
        manifest["sources"].append(source)
        remaining -= budget
    return "\n".join(chunks), manifest


def main() -> int:
    args = parse_args()
    report = base_report(
        "maui_context_export.py",
        args.scope,
        {
            "dry_run": args.dry_run,
            "write_report": args.write_report,
            "target": args.target,
            "limit_tokens": args.limit_tokens,
            "scope": args.scope,
        },
    )
    package_md, manifest = build_package(args.target, args.limit_tokens)
    if args.target == "chatgpt-handoff":
        mark_warning(report, "chatgpt-handoff deve declarar conformidade unknown sem filesystem")
    if args.write_report and not args.dry_run:
        out_dir = VAULT_ROOT / "validations" / "context-packages"
        md_path = out_dir / f"{args.target}-bootstrap-{today()}.md"
        json_path = out_dir / f"{args.target}-bootstrap-{today()}.json"
        safe_write_text(md_path, package_md)
        safe_write_text(json_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        add_artifact(report, md_path)
        add_artifact(report, json_path)
    add_info(report, f"fontes incluídas: {len(manifest['sources'])}")
    for path in write_report_bundle(
        report=report,
        title="Maui Context Export",
        stem=f"maui-context-export-{args.target}",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print(package_md)
    print_markdown("Maui Context Export", report)
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)
