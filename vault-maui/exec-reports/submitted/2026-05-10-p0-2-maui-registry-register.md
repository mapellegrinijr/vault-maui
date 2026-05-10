---
titulo: "Exec-report — Maui Registry"
versao: "1.0"
status: submitted
data_criacao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: p0_2_scripts_maui
---

# Exec-report — Maui Registry

## Escopo

Execução do script `maui_registry.py` no escopo `.maui/registry`.

## Flags

```json
{
  "dry_run": false,
  "write_report": true,
  "command": "register",
  "id": "codex-local",
  "target": "codex",
  "status": "unknown",
  "head": "2294c00",
  "notes": "P0.2 smoke registration"
}
```

## Resumo JSON

```json
{
  "script": "maui_registry.py",
  "ts": "2026-05-10T13:33:48-03:00",
  "ok": true,
  "scope": ".maui/registry",
  "flags": {
    "dry_run": false,
    "write_report": true,
    "command": "register",
    "id": "codex-local",
    "target": "codex",
    "status": "unknown",
    "head": "2294c00",
    "notes": "P0.2 smoke registration"
  },
  "critical": [],
  "warnings": [],
  "info": [
    "instância registrada: codex-local"
  ],
  "artifacts": [
    "vault-maui/.maui/registry/instances.json",
    "vault-maui/.maui/registry/instances-snapshot.json"
  ]
}
```

## Resultado

- OK: `True`
- Falhas críticas: 0
- Alertas: 0
