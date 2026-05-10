---
titulo: "Ordem de leitura — Claude Saara PE Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: ordem_leitura_contextual
escopo: projeto_maui
destino_esperado: saara_claude_7_1_1_pe
confidencialidade: interna
---

# Ordem de leitura — Claude Saara PE Maui

## Lista priorizada

| Ordem | Arquivo | Motivo | Extrair | Classe |
| --- | --- | --- | --- | --- |
| 1 | `vault-maui/handoffs/2026-05-06-handoff-saara-7-1-1-pe-claude-maui.md` | Handoff principal desta continuidade | Estado consolidado, limites, próximo passo, regras para Claude | handoff/memória operacional |
| 2 | `vault-maui/context-packages/generated/2026-05-06-claude-saara-7-1-1-pe-maui-continuation.md` | Pacote paste-ready para runtime Claude | Checklist inicial, comportamento, restrições | context package |
| 3 | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-28-system-prompt-maui.md` | Fonte de estado real mais recente | P0.1.28 success, arquivos criados, riscos, próximo passo | evidência operacional |
| 4 | `vault-maui/00_core/system-prompt-maui.md` | Contrato runtime Maui criado em P0.1.28 | Precedência runtime, router planejado, limites | normativo/proposta |
| 5 | `vault-maui/00_core/contrato-precedencia-maui.md` | Define precedência e Human Gate | Ordem de fontes, `unknown`, não execução por inferência | normativo/proposta |
| 6 | `vault-maui/00_core/principios-fundacionais-maui.md` | Princípios inegociáveis Maui | Separação Saara/Maui, PE obrigatório, memória canônica | normativo/proposta |
| 7 | `vault-maui/00_core/especificacao-completa-maui.md` | Referência normativa central | Domínios planejados, lifecycle, dependências P0.1.29-P0.1.32 | normativo/proposta |
| 8 | `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md` | Plano de lotes da configuração-base | Sequência P0.1.26-P0.1.32, critérios e Human Gates | planejamento |
| 9 | `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md` | Diagnóstico de lacunas | Artefatos ausentes/planejados, riscos, de/para Saara | inventário/evidência de diagnóstico |
| 10 | `vault-maui/context-packages/current/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md` | Brief de retomada anterior | Contexto histórico pós-P0.1.25 e cautelas | context brief; pode estar defasado |
| 11 | `vault-maui/project-memories/2026-05-06-marco-p0-1-28-system-prompt-maui.md` | Memória marco mais recente da configuração-base | Decisões runtime e riscos P0.1.28 | memória |
| 12 | Exec-reports P0.1.21-P0.1.27 | Evidência histórica | Linha do tempo, commits, restrições preservadas | evidência operacional |
| 13 | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | Mapa de destino | Sequência macro e proposta de roadmap | roadmap/planejamento |
| 14 | `../Saara/vault-saara/00_core/system-prompt.md` | Modelo runtime Saara 7.1.1 | Formato, precedência, modos, Domain Router | referência Saara |
| 15 | `../Saara/vault-saara/00_core/pka-prompt-engineering.md` | PKA PE vigente | Fronteira PE/Agent, IO, quality gates de prompt | referência Saara |
| 16 | Demais PKAs/specs Saara e `indice.md` | Modelo conceitual | Domínios, specs, parametrização e índice futuros | referência Saara |

## Fontes de estado real

Use como fonte principal de execução:

- Git e filesystem local.
- `vault-maui/exec-reports/submitted/`.
- Arquivos realmente existentes em `vault-maui/00_core/`.
- Inventários e planos quando descrevem diagnóstico/planejamento.
- Memórias marcadas com `deve_ser_considerado_em_context_brief: true`.

## Roadmap e planejamento

Use como planejamento, não como prova isolada:

- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
- Seções de próximos passos em exec-reports.

## Normativos Maui

Normativos atuais em `status: proposta`:

- `vault-maui/00_core/contrato-precedencia-maui.md`
- `vault-maui/00_core/principios-fundacionais-maui.md`
- `vault-maui/00_core/especificacao-completa-maui.md`
- `vault-maui/00_core/system-prompt-maui.md`

Não promover status sem decisão humana.

## Memória e handoff

Use para continuidade, não como prova única:

- `vault-maui/project-memories/2026-05-06-marco-p0-1-28-system-prompt-maui.md`
- `vault-maui/project-memories/2026-05-06-marco-p0-1-27-especificacao-completa-maui.md`
- `vault-maui/project-memories/2026-05-06-marco-p0-1-26-principios-precedencia-maui.md`
- `vault-maui/project-memories/2026-05-06-marco-pos-p0-1-25-configuracao-base-maui.md`
- Este handoff e context package gerado.

## Arquivos que não devem ser usados sozinhos

- Roadmap: não prova execução.
- Context brief pós-P0.1.25: útil, mas defasado após P0.1.26-P0.1.28.
- Memórias: precisam ser reconciliadas com Git/filesystem e exec-reports.
- Handoffs: informam contexto, mas não provam `current` sem hash/filesystem.
- Arquivos Saara: são modelo, não estado Maui.

## Leitura Saara 7.1.1 + PE

Para entender a instância destino:

1. `../Saara/vault-saara/00_core/system-prompt.md` — contrato runtime.
2. `../Saara/vault-saara/00_core/principios-fundacionais.md` — soberania cognitiva, lifecycle, context injection, capture.
3. `../Saara/vault-saara/00_core/especificacao-completa.md` — precedência, PKAs, modos.
4. `../Saara/vault-saara/00_core/pka-prompt-engineering.md` — Prompt Engineering Elite.
5. `../Saara/vault-saara/00_core/pka-agent-engineering.md` — fronteira de integração sistêmica.
6. `../Saara/vault-saara/00_core/spec-parametrizacao.md` e `.json` — modos, disclosure, router.
7. `../Saara/vault-saara/00_core/indice.md` — navegação e precedência.
