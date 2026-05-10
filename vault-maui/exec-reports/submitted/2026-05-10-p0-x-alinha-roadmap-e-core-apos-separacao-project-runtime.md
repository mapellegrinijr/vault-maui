---
titulo: "Exec Report — Alinha roadmap e core após separação Project vs Runtime"
status: success
data_execucao: 2026-05-10
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
human_gate: true
---

# Exec Report — Alinha roadmap e core após separação Project vs Runtime

## Objetivo

Atualizar o roadmap Project e documentos importantes do corpus para refletir a estrutura adotada nos commits `f8b5120` e `9c76d62`.

## Evidência de base

- `f8b5120` — separou `project-memories/`, `status-project/`, `memorias/`, `status/` e moveu o roadmap para `project/roadmap/`.
- `9c76d62` — atualizou procedure, skill, template de Context Brief e painel para a nova estrutura.

## Arquivos editados

- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/00_core/indice-maui.md`
- `vault-maui/00_core/regras-operacionais.md`
- `vault-maui/00_core/especificacao-completa-maui.md`
- `vault-maui/00_core/contrato-precedencia-maui.md`
- `vault-maui/00_core/principios-fundacionais-maui.md`
- `vault-maui/00_core/spec-memory-store-maui.md`
- `vault-maui/00_core/spec-capture-layer-maui.md`
- `vault-maui/00_core/spec-context-engineering-maui.md`
- `vault-maui/00_core/system-prompt-maui.md`
- `vault-maui/01_manifest/spec-parametrizacao-maui.json`

## Resumo das mudanças

- Roadmap passou a registrar H0.x como housekeeping concluído de separação Project vs Runtime.
- Roadmap e índice passaram a declarar `status-project/` como status vivo do projeto.
- Índice passou a listar `project/roadmap/`, `status-project/`, `project-memories/`, `status/` e `memorias/` com papéis separados.
- Documentos core passaram a distinguir memória de projeto/gestação (`project-memories/`) de memória operacional runtime (`memorias/`).
- Memory Store e Capture Layer passaram a apontar para `memorias/` como destino runtime, mantendo `project-memories/` como histórico de implementação.
- Manifest JSON atualizado para refletir `canonical_directory: vault-maui/memorias/` e `project_memory_directory: vault-maui/project-memories/`.
- System prompt teve anacronismo de Configuração-base incompleta substituído por referência ao status-project.

## Validação

- Grep para o path antigo do roadmap em `00_core/` retornou zero ocorrências.
- Grep para o path antigo do status update em `status/` retornou zero ocorrências.
- `jq empty vault-maui/01_manifest/spec-parametrizacao-maui.json` executou sem erro.

## Sem execução de roadmap

Nenhuma etapa P0.2, P0.3, P0.4 ou qualquer outra etapa do roadmap foi executada. Esta tarefa foi apenas documental.
