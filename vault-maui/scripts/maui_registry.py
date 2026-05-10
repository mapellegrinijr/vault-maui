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
    mark_critical,
    mark_warning,
    print_markdown,
    read_text,
    safe_write_text,
    write_report_bundle,
)


REGISTRY_PATH = VAULT_ROOT / ".maui" / "registry" / "instances.json"
SNAPSHOT_PATH = VAULT_ROOT / ".maui" / "registry" / "instances-snapshot.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Registry CRUD de instâncias Maui")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="Lista instâncias registradas")
    register = sub.add_parser("register", help="Registra ou atualiza instância")
    register.add_argument("--id", required=True)
    register.add_argument("--target", required=True)
    register.add_argument("--status", default="unknown")
    register.add_argument("--head", default="unknown")
    register.add_argument("--notes", default="")
    check = sub.add_parser("check", help="Checa uma instância")
    check.add_argument("--id")
    return parser.parse_args()


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"instances": []}
    return json.loads(read_text(REGISTRY_PATH))


def save_registry(data: dict) -> None:
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    safe_write_text(REGISTRY_PATH, payload)
    safe_write_text(SNAPSHOT_PATH, payload)


def main() -> int:
    args = parse_args()
    flags = vars(args).copy()
    report = base_report("maui_registry.py", ".maui/registry", flags)
    data = load_registry()
    instances = data.setdefault("instances", [])

    if args.command == "register":
        current = next((item for item in instances if item.get("id") == args.id), None)
        record = {
            "id": args.id,
            "target": args.target,
            "status": args.status,
            "head": args.head,
            "notes": args.notes,
        }
        if current:
            current.update(record)
            add_info(report, f"instância atualizada: {args.id}")
        else:
            instances.append(record)
            add_info(report, f"instância registrada: {args.id}")
        if not args.dry_run:
            save_registry(data)
            add_artifact(report, REGISTRY_PATH)
            add_artifact(report, SNAPSHOT_PATH)
    elif args.command == "check":
        if args.id:
            found = next((item for item in instances if item.get("id") == args.id), None)
            if found:
                add_info(report, f"instância encontrada: {args.id} ({found.get('status')})")
            else:
                mark_critical(report, f"instância não encontrada: {args.id}")
        else:
            unknown = [item for item in instances if item.get("status") == "unknown"]
            if unknown:
                mark_warning(report, f"instâncias unknown: {len(unknown)}")
            add_info(report, f"instâncias registradas: {len(instances)}")
    else:
        add_info(report, f"instâncias registradas: {len(instances)}")

    if args.write_report and not args.dry_run and args.command != "register":
        safe_write_text(SNAPSHOT_PATH, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        add_artifact(report, SNAPSHOT_PATH)
    for path in write_report_bundle(
        report=report,
        title="Maui Registry",
        stem=f"maui-registry-{args.command}",
        write_report=args.write_report and not args.dry_run,
    ):
        add_artifact(report, path)
    print_markdown("Maui Registry", report)
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return exit_code(report)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro crítico: {exc}", file=sys.stderr)
        raise SystemExit(1)

