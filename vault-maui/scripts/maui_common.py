#!/usr/bin/env python3
"""Shared helpers for Maui P0.2 CLI scripts."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


VAULT_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = VAULT_ROOT.parent
ALLOWED_WRITE_ROOTS = (
    VAULT_ROOT / "validations",
    VAULT_ROOT / ".maui",
    VAULT_ROOT / "exec-reports",
)


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def today() -> str:
    return dt.date.today().isoformat()


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    return value.strip("-") or "maui"


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    candidates = [WORKSPACE_ROOT / path, VAULT_ROOT / path]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return WORKSPACE_ROOT / path


def rel(path: str | Path) -> str:
    path = Path(path)
    try:
        return path.resolve().relative_to(WORKSPACE_ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def ensure_allowed_write(path: Path) -> None:
    resolved = path.resolve()
    for root in ALLOWED_WRITE_ROOTS:
        try:
            resolved.relative_to(root.resolve())
            return
        except ValueError:
            continue
    raise ValueError(f"refusing to write outside allowed roots: {rel(path)}")


def safe_write_text(path: Path, content: str) -> None:
    ensure_allowed_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip()
    body = text[end + 4:].lstrip("\n")
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(stripped[2:].strip().strip('"'))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        if value == "":
            data[current_key] = []
        else:
            data[current_key] = value.strip('"').strip("'")
    return data, body


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def base_report(script: str, scope: str, flags: dict[str, Any]) -> dict[str, Any]:
    return {
        "script": script,
        "ts": now_iso(),
        "ok": True,
        "scope": scope,
        "flags": flags,
        "critical": [],
        "warnings": [],
        "info": [],
        "artifacts": [],
    }


def mark_critical(report: dict[str, Any], message: str) -> None:
    report["ok"] = False
    report.setdefault("critical", []).append(message)


def mark_warning(report: dict[str, Any], message: str) -> None:
    report.setdefault("warnings", []).append(message)


def add_info(report: dict[str, Any], message: str) -> None:
    report.setdefault("info", []).append(message)


def add_artifact(report: dict[str, Any], path: Path | str) -> None:
    report.setdefault("artifacts", []).append(rel(path))


def render_report_md(title: str, report: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        f"- Script: `{report['script']}`",
        f"- Gerado em: {report['ts']}",
        f"- Escopo: `{report['scope']}`",
        f"- OK: `{report['ok']}`",
        "",
        "## Flags",
        "",
        "```json",
        json.dumps(report.get("flags", {}), ensure_ascii=False, indent=2),
        "```",
    ]
    for key, heading in (
        ("critical", "Falhas críticas"),
        ("warnings", "Alertas"),
        ("info", "Resumo"),
        ("artifacts", "Artefatos"),
    ):
        lines.extend(["", f"## {heading}", ""])
        values = report.get(key, [])
        if values:
            lines.extend(f"- {value}" for value in values)
        else:
            lines.append("- Nenhum.")
    return "\n".join(lines) + "\n"


def write_report_bundle(
    *,
    report: dict[str, Any],
    title: str,
    stem: str,
    write_report: bool,
) -> list[Path]:
    if not write_report:
        return []
    date = today()
    safe_stem = slugify(stem)
    validation_json = VAULT_ROOT / "validations" / f"{safe_stem}-{date}.json"
    validation_md = VAULT_ROOT / "validations" / f"{safe_stem}-{date}.md"
    exec_report = VAULT_ROOT / "exec-reports" / "submitted" / f"{date}-p0-2-{safe_stem}.md"
    md = render_report_md(title, report)
    exec_md = "\n".join(
        [
            "---",
            f'titulo: "Exec-report — {title}"',
            'versao: "1.0"',
            "status: submitted",
            f"data_criacao: {date}",
            "idioma: pt-BR",
            "tipo: exec_report",
            "escopo: p0_2_scripts_maui",
            "---",
            "",
            f"# Exec-report — {title}",
            "",
            "## Escopo",
            "",
            f"Execução do script `{report['script']}` no escopo `{report['scope']}`.",
            "",
            "## Flags",
            "",
            "```json",
            json.dumps(report.get("flags", {}), ensure_ascii=False, indent=2),
            "```",
            "",
            "## Resumo JSON",
            "",
            "```json",
            json.dumps(report, ensure_ascii=False, indent=2),
            "```",
            "",
            "## Resultado",
            "",
            f"- OK: `{report['ok']}`",
            f"- Falhas críticas: {len(report.get('critical', []))}",
            f"- Alertas: {len(report.get('warnings', []))}",
        ]
    )
    safe_write_text(validation_json, json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    safe_write_text(validation_md, md)
    safe_write_text(exec_report, exec_md + "\n")
    return [validation_json, validation_md, exec_report]


def print_markdown(title: str, report: dict[str, Any]) -> None:
    print(render_report_md(title, report), end="")


def exit_code(report: dict[str, Any]) -> int:
    return 0 if report.get("ok") else 1
