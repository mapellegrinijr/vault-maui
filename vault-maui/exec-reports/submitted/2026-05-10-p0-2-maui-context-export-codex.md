---
titulo: "Exec-report — Maui Context Export"
versao: "1.0"
status: submitted
data_criacao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: p0_2_scripts_maui
---

# Exec-report — Maui Context Export

## Escopo

Execução do script `maui_context_export.py` no escopo `project`.

## Flags

```json
{
  "dry_run": false,
  "write_report": true,
  "target": "codex",
  "limit_tokens": 1200,
  "scope": "project"
}
```

## Resumo JSON

```json
{
  "script": "maui_context_export.py",
  "ts": "2026-05-10T13:33:40-03:00",
  "ok": true,
  "scope": "project",
  "flags": {
    "dry_run": false,
    "write_report": true,
    "target": "codex",
    "limit_tokens": 1200,
    "scope": "project"
  },
  "critical": [],
  "warnings": [],
  "info": [
    "fontes incluídas: 7"
  ],
  "artifacts": [
    "vault-maui/validations/context-packages/codex-bootstrap-2026-05-10.md",
    "vault-maui/validations/context-packages/codex-bootstrap-2026-05-10.json"
  ]
}
```

## Resultado

- OK: `True`
- Falhas críticas: 0
- Alertas: 0
