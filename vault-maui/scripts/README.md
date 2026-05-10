# Maui P0.2 Scripts

Scripts CLI do lote P0.2 para bootstrap, validação e contexto. Todos expõem `--help`, `--dry-run` e `--write-report`, com saída Markdown em stdout e relatórios JSON/Markdown quando aplicável.

## CLIs

| Script | Função | Flags principais | Escrita com `--write-report` |
| --- | --- | --- | --- |
| `maui_vault_health.py` | Health-check da estrutura mínima do vault | `--target`, `--dry-run`, `--write-report` | `validations/`, `exec-reports/submitted/` |
| `maui_validate_frontmatter.py` | Valida frontmatter Markdown | `--scope`, `--dry-run`, `--write-report` | `validations/`, `exec-reports/submitted/` |
| `maui_validate_links.py` | Detecta wikilinks e caminhos quebrados | `--scope`, `--dry-run`, `--write-report` | `validations/`, `exec-reports/submitted/` |
| `maui_context_export.py` | Gera context package por target | `--target`, `--limit-tokens`, `--scope`, `--dry-run`, `--write-report` | `validations/context-packages/`, `exec-reports/submitted/` |
| `maui_registry.py` | Registra e consulta instâncias Maui | `list`, `register`, `check`, `--dry-run`, `--write-report` | `.maui/registry/`, `validations/`, `exec-reports/submitted/` |
| `maui_update_export.py` | Gera Update Package a partir de request | `--request`, `--dry-run`, `--write-report` | `validations/exports/`, `exec-reports/submitted/` |
| `maui_memory_index.py` | Reconstrói índice de memórias | `--scope project|runtime|all`, `--dry-run`, `--write-report` | `.maui/cache/`, `validations/`, `exec-reports/submitted/` |

## Exemplos

```bash
python vault-maui/scripts/maui_vault_health.py --dry-run
python vault-maui/scripts/maui_validate_frontmatter.py --scope vault-maui/context-packages/current --dry-run
python vault-maui/scripts/maui_validate_links.py --scope vault-maui/00_core --dry-run
python vault-maui/scripts/maui_context_export.py --target codex --limit-tokens 1200 --dry-run
python vault-maui/scripts/maui_registry.py --dry-run list
python vault-maui/scripts/maui_update_export.py --request vault-maui/exec-requests/templates/exec-request-template.md --dry-run
python vault-maui/scripts/maui_memory_index.py --scope project --dry-run
```

## Contrato de escrita

Os scripts P0.2 não devem escrever fora de:

- `vault-maui/validations/`
- `vault-maui/.maui/`
- `vault-maui/exec-reports/`

Use `--dry-run` para inspecionar a execução sem persistir relatórios.
