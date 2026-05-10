---
titulo: "Exec-report — Maui Memory Index"
versao: "1.0"
status: submitted
data_criacao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: p0_2_scripts_maui
---

# Exec-report — Maui Memory Index

## Escopo

Execução do script `maui_memory_index.py` no escopo `all`.

## Flags

```json
{
  "dry_run": false,
  "write_report": true,
  "scope": "all"
}
```

## Resumo JSON

```json
{
  "script": "maui_memory_index.py",
  "ts": "2026-05-10T13:33:48-03:00",
  "ok": true,
  "scope": "all",
  "flags": {
    "dry_run": false,
    "write_report": true,
    "scope": "all"
  },
  "critical": [],
  "warnings": [
    "memória sem confidencialidade: project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md"
  ],
  "info": [
    "runtime memorias reservado: apenas README",
    "memórias indexadas: 13"
  ],
  "artifacts": [
    "vault-maui/.maui/cache/memory-index.json"
  ]
}
```

## Resultado

- OK: `True`
- Falhas críticas: 0
- Alertas: 1
