---
titulo: "Exec-report — P0.2 lote scripts bootstrap, validação e contexto"
versao: "1.0"
status: submitted
data_criacao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: p0_2_scripts_maui
---

# Exec-report — P0.2 lote scripts bootstrap, validação e contexto

## Escopo

Implementação do lote P0.2 em branch `feature/p0.2-bootstrap-scripts`, criando sete CLIs Python em `vault-maui/scripts/` e seus artefatos de exemplo, smoke reports, registry/cache e testes mínimos.

## HEAD base

- Base informada: `2294c00`.
- Branch criada: `feature/p0.2-bootstrap-scripts`.
- Working tree inicial: sujo apenas por `vault-maui/00_core/system-prompt-maui.md.bak.disabled`, preservado fora do lote.

## Scripts criados

- `vault-maui/scripts/maui_vault_health.py`
- `vault-maui/scripts/maui_validate_frontmatter.py`
- `vault-maui/scripts/maui_validate_links.py`
- `vault-maui/scripts/maui_context_export.py`
- `vault-maui/scripts/maui_registry.py`
- `vault-maui/scripts/maui_update_export.py`
- `vault-maui/scripts/maui_memory_index.py`
- `vault-maui/scripts/maui_common.py`

## Artefatos de validação gerados

- `vault-maui/validations/examples/`
- `vault-maui/validations/tests/test_p0_2_scripts.py`
- `vault-maui/validations/context-packages/codex-bootstrap-2026-05-10.md`
- `vault-maui/validations/context-packages/codex-bootstrap-2026-05-10.json`
- `vault-maui/validations/exports/update-package-exec-request-template-2026-05-10.md`
- `vault-maui/validations/exports/update-package-exec-request-template-2026-05-10-manifest.yaml`
- Relatórios Markdown/JSON em `vault-maui/validations/`.

## Artefatos `.maui/`

- `vault-maui/.maui/registry/instances.json`
- `vault-maui/.maui/registry/instances-snapshot.json`
- `vault-maui/.maui/cache/memory-index.json`

## Exec-reports por script

- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-vault-health.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-validate-frontmatter.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-validate-links.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-context-export-codex.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-registry-register.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-update-export.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-memory-index-all.md`

## Validações executadas

- `PYTHONPYCACHEPREFIX=/private/tmp/maui-pycache python3 -m py_compile ...` — passou.
- `python3 vault-maui/scripts/maui_vault_health.py --dry-run` — passou.
- `python3 vault-maui/scripts/maui_validate_frontmatter.py --dry-run --scope vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md` — passou com alerta de confidencialidade ausente no brief.
- `python3 vault-maui/scripts/maui_validate_links.py --dry-run --scope vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md` — passou.
- `python3 vault-maui/scripts/maui_context_export.py --dry-run --target codex --limit-tokens 800` — passou.
- `python3 vault-maui/scripts/maui_registry.py --dry-run list` — passou.
- `python3 vault-maui/scripts/maui_update_export.py --dry-run --request vault-maui/exec-requests/templates/exec-request-template.md` — passou.
- `python3 vault-maui/scripts/maui_memory_index.py --dry-run --scope project` — passou.

## Limitações de ambiente

- `python3 -m pytest vault-maui/validations/tests` não pôde rodar porque `pytest` não está instalado no ambiente.
- `ruff` não está instalado.
- `flake8` não está instalado.

## Decisões de implementação

- `maui_update_export.py` grava pacotes em `vault-maui/validations/exports/` para respeitar o limite operacional de que scripts não escrevam fora de `validations/`, `.maui/` ou `exec-reports/`.
- `maui_context_export.py` grava packages gerados em `vault-maui/validations/context-packages/` pelo mesmo motivo.
- O arquivo pré-existente `vault-maui/00_core/system-prompt-maui.md.bak.disabled` não foi alterado nem incluído.

## Confirmação de limite

- Sem promoção de status de normativos/procedures.
- Sem alteração em `Documentação/`.
- Sem alteração em `vault-maui/00_core/` ou `vault-maui/01_manifest/`.
- Sem alteração em runtime reservado `vault-maui/memorias/` e `vault-maui/status/`.

