from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "vault-maui" / "scripts"


def run_script(name: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_all_scripts_have_help() -> None:
    for script in [
        "maui_vault_health.py",
        "maui_validate_frontmatter.py",
        "maui_validate_links.py",
        "maui_context_export.py",
        "maui_registry.py",
        "maui_update_export.py",
        "maui_memory_index.py",
    ]:
        result = run_script(script, "--help")
        assert result.returncode == 0, result.stderr
        assert "usage:" in result.stdout


def test_vault_health_dry_run() -> None:
    result = run_script("maui_vault_health.py", "--dry-run")
    assert "Maui Vault Health" in result.stdout


def test_validate_frontmatter_with_valid_file(tmp_path: Path) -> None:
    doc = tmp_path / "ok.md"
    doc.write_text(
        "---\n"
        'titulo: "Ok"\n'
        'versao: "1.0"\n'
        "status: ativo\n"
        "data_criacao: 2026-05-10\n"
        "idioma: pt-BR\n"
        "tipo: teste\n"
        "escopo: teste\n"
        "confidencialidade: interna\n"
        "---\n"
        "# Ok\n",
        encoding="utf-8",
    )
    result = run_script("maui_validate_frontmatter.py", "--dry-run", "--scope", str(doc))
    assert result.returncode == 0, result.stdout + result.stderr


def test_validate_links_with_local_file(tmp_path: Path) -> None:
    target = tmp_path / "target.md"
    source = tmp_path / "source.md"
    target.write_text("# Target\n", encoding="utf-8")
    source.write_text("[target](target.md)\n", encoding="utf-8")
    result = run_script("maui_validate_links.py", "--dry-run", "--scope", str(source))
    assert result.returncode == 0, result.stdout + result.stderr


def test_context_export_dry_run() -> None:
    result = run_script("maui_context_export.py", "--dry-run", "--target", "codex", "--limit-tokens", "800")
    assert result.returncode == 0, result.stderr
    assert "Maui Context Package" in result.stdout


def test_registry_list_dry_run() -> None:
    result = run_script("maui_registry.py", "--dry-run", "list")
    assert result.returncode == 0, result.stderr
    assert "Maui Registry" in result.stdout


def test_update_export_dry_run(tmp_path: Path) -> None:
    request = tmp_path / "request.md"
    request.write_text(
        "# Exec Request\n\n"
        "## Identificacao\n\n"
        "- ID: teste\n"
        "- Titulo: Teste\n\n"
        "## Objetivo\n\n"
        "Gerar pacote.\n\n"
        "## Escopo permitido\n\n"
        "Somente teste.\n\n"
        "## Criterios de aceite\n\n"
        "- [ ] Passa\n",
        encoding="utf-8",
    )
    result = run_script("maui_update_export.py", "--dry-run", "--request", str(request))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Update Package" in result.stdout


def test_memory_index_dry_run() -> None:
    result = run_script("maui_memory_index.py", "--dry-run", "--scope", "project")
    assert result.returncode == 0, result.stderr
    assert "Maui Memory Index" in result.stdout

