# Resumo

Implementa o lote P0.2 de scripts bootstrap, validação e contexto do Maui.

## Scripts

- `maui_vault_health.py` — health-check da estrutura do vault.
- `maui_validate_frontmatter.py` — validação de frontmatter Markdown.
- `maui_validate_links.py` — detecção de wikilinks/caminhos quebrados.
- `maui_context_export.py` — geração de context package por target.
- `maui_registry.py` — registry CRUD de instâncias em `.maui/registry/`.
- `maui_update_export.py` — criação de Update Package via request.
- `maui_memory_index.py` — índice reconstruível de memórias.

## Exec-reports

- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-lote-bootstrap-scripts.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-vault-health.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-validate-frontmatter.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-validate-links.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-context-export-codex.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-registry-register.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-update-export.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-2-maui-memory-index-all.md`

## Checklist

- [ ] CI (ruff, flake8, pytest, compileall)
- [ ] 7 exec-reports por script presentes em `exec-reports/submitted/`
- [ ] Scripts não escrevem fora de `validations/`, `.maui/` ou `exec-reports/`
- [ ] `vault-maui/00_core/system-prompt-maui.md.bak.disabled` preservado como untracked local
- [ ] Tag `p0.2-complete` criada após merge

## Observações

- `maui_update_export.py` grava em `vault-maui/validations/exports/` para respeitar o contrato de escrita do lote.
- O arquivo `.bak.disabled` é sujeira local pré-existente e não faz parte deste PR.
