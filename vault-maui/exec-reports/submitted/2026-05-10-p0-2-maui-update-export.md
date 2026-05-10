---
titulo: "Exec-report — Maui Update Export"
versao: "1.0"
status: submitted
data_criacao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: p0_2_scripts_maui
---

# Exec-report — Maui Update Export

## Escopo

Execução do script `maui_update_export.py` no escopo `vault-maui/exec-requests/templates/exec-request-template.md`.

## Flags

```json
{
  "dry_run": false,
  "write_report": true,
  "request": "vault-maui/exec-requests/templates/exec-request-template.md"
}
```

## Resumo JSON

```json
{
  "script": "maui_update_export.py",
  "ts": "2026-05-10T13:34:07-03:00",
  "ok": true,
  "scope": "vault-maui/exec-requests/templates/exec-request-template.md",
  "flags": {
    "dry_run": false,
    "write_report": true,
    "request": "vault-maui/exec-requests/templates/exec-request-template.md"
  },
  "critical": [],
  "warnings": [],
  "info": [
    "human_gate: False"
  ],
  "artifacts": [
    "vault-maui/validations/exports/update-package-exec-request-template-2026-05-10.md",
    "vault-maui/validations/exports/update-package-exec-request-template-2026-05-10-manifest.yaml"
  ]
}
```

## Resultado

- OK: `True`
- Falhas críticas: 0
- Alertas: 0
