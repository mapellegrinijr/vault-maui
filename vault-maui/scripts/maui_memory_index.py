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
    parse_frontmatter,
    print_markdown,
    read_text,
    safe_write_text,
    write_report_bundle,
)


INDEX_PATH = VAULT_ROOT / ".maui" / "cache" / "memory-index.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Índice reconstruível de memórias Maui")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--scope", choices=("project", "runtime", "all"), default="project")
    return parser.parse_args()


def memory_dirs(scope: str):
    if scope in ("project", "all"):
        yield "project", VAULT_ROOT / "project-memories"
    if scope in ("runtime", "all"):
        yield "runtime", VAULT_ROOT / "memorias"


def main() -> int:
    args = parse_args()
    report = base_report(
        "maui_memory_index.py",
        args.scope,
        {"dry_run": args.dry_run, "write_report": args.write_report, "scope": args.scope},
    )
    items = []
    seen = {}
    for kind, directory in memory_dirs(args.scope):
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            data, _ = parse_frontmatter(read_text(path))
            key = (data.get("titulo", path.stem), data.get("data_criacao", "unknown"))
            if key in seen:
                mark_warning(report, f"possível duplicidade: {path.name} e {seen[key]}")
            seen[key] = path.name
            if "confidencialidade" not in data:
                mark_warning(report, f"memória sem confidencialidade: {path.relative_to(VAULT_ROOT)}")
            items.append(
                {
                    "kind": kind,
                    "path": path.relative_to(VAULT_ROOT).as_posix(),
                    "titulo": data.get("titulo", path.stem),
                    "data_criacao": data.get("data_criacao", "unknown"),
                    "tipo": data.get("tipo", "unknown"),
                }
            )
    if args.scope in ("runtime", "all"):
        runtime_files = [p for p in (VAULT_ROOT / "memorias").glob("*.md") if p.name != "README.md"]
        if runtime_files:
            mark_warning(report, f"runtime memorias contém arquivos operacionais: {len(runtime_files)}")
        else:
            add_info(report, "runtime memorias reservado: apenas README")
    index = {"generated_at": report["ts"], "scope": args.scope, "items": items}
    add_info(report, f"memórias indexadas: {len(items)}")
    if args.write_report and not args.dry_run:
        safe_write_text(INDEX_PATH, json.dumps(index, ensure_ascii=False, indent=2) + "\n")
        add_artifact(report, INDEX_PATH)
    for path in write_report_bundle(
        report=report,
        title="Maui Memory Index",
        stem=f"maui-memory-index-{args.scope}",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Memory Index", report)
    print(json.dumps(index, ensure_ascii=False, indent=2))
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)
