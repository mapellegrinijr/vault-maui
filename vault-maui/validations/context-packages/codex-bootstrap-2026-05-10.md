# Maui Context Package — codex

- Target: `codex`
- Limite aproximado: 1200 tokens
- Conformidade sem filesystem: `unknown` quando HEAD não for verificável.

## Fonte: `context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md`

---
titulo: "Context Brief — Status Atual Maui v2"
versao: "1.0"
status: ativo
data_criacao: 2026-05-10
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
deve_ser_considerado_em_context_brief: true
---

# Context Brief — Status Atual Maui v2

## Fonte de status corrente

- Fonte canônica de status do projeto: `vault-maui/status-project/STATUS-UPDATE-maui.md`.
- HEAD de referência na coleta: `63530a8497d76761cf8a78365970c5a3e243fee3` (`docs(procedures): exigir protocolo prepare handoff no handoff principal do dia`).
- Working tree na coleta: sujo por `vault-maui/00_core/system-prompt-maui.md.bak.disabled` não rastreado.
- Este brief é artefato de Project e manual-first; não é artefato de runtime.

## Pacote mínimo de leitura (1–8)

1. `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md` — este brief current.
2. `vault-maui/status-project/STATUS-UPDATE-maui.md` — status vivo do projeto.
3. `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff-v2.md` — handoff principal do pacote.
4. `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff-v2.md` — exec-report de governança.
5. `vault-maui/procedures/procedimento-preparar-handoff.md` — procedure canônico do pipeline.
6. `vault-maui/00_core/contrato-precedencia-maui.md` e `vault-maui/00_core/principios-fundacionais-maui.md`.
7. `vault-maui/00_core/system-prompt-maui.md`, `vault-maui/00_core/indice-maui.md` e `vault-maui/00_core/spec-parametrizacao-maui.md`.
8. `vault-maui/01_manifest/spec-parametrizacao-maui.json` e `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.

## Estado confirmado

- Configuração-base concluída por P0.1.32, com evidência em exec-report, memória marco e commit `538b441`.
- Separação Project vs Runtime e pacote manual-first já foram consolidados por commits `f8b5120`, `9c76d62`, `1d875e3`, `143a3d9` e `10a37c0`.
- Procedure de handoff foi reforçado em `63530a8` para exigir seção específica no handoff principal.
- Este pacote v2 foi necessário porque os nomes-base de 2026-05-10 já existiam.
- Brief current anterior foi movido para `vault-maui/context-packages/archive/2026-05-10-context-brief-status-atual-maui.md`.

## O que NÃO assumir

- Não assumir execução de P0.2, P0.3, P0.4, P0.1.11 ou qualquer etapa do roadmap.
- Não usar `vault-maui/panel/status.md` como fonte declarativa de estado.
- Não usar `va

[TRUNCADO POR LIMITE]


## Fonte: `status-project/STATUS-UPDATE-maui.md`

# Status Update — Projeto Maui (Project)

- Gerado em: 2026-05-10T13:03:49-03:00
- HEAD: `63530a8497d76761cf8a78365970c5a3e243fee3` — 2026-05-10 15:59:53 +0000 — `docs(procedures): exigir protocolo prepare handoff no handoff principal do dia`
- Working tree: sujo — `git status --porcelain` registrou `?? vault-maui/00_core/system-prompt-maui.md.bak.disabled`; artefatos deste pacote v2 também ficam pendentes até Human Gate/commit.

## 1) TL;DR (5 bullets)

- HEAD atual é `63530a8`, que atualiza o procedure de handoff para exigir a seção “Protocolo Prepare Handoff (manual-first)” no handoff principal.
- Configuração-base Maui permanece concluída por evidência de P0.1.32: exec-report `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco e commit `538b441`.
- Este pacote cria versões `-v2` porque os nomes-base de 2026-05-10 já existem para context brief, handoff e exec-report.
- `context-packages/current/` deve manter apenas `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md`; o brief current anterior foi movido para `archive/`.
- Próximo passo é Human Gate: revisar e aprovar ou rejeitar commit único; nenhuma etapa do roadmap foi executada.

## 2) Evidência Git

Pré-validação obrigatória:

```text
$ git status --porcelain
?? vault-maui/00_core/system-prompt-maui.md.bak.disabled
```

```text
$ git log -1 --oneline
63530a8 docs(procedures): exigir protocolo prepare handoff no handoff principal do dia
```

- HEAD completo: `63530a8497d76761cf8a78365970c5a3e243fee3`
- Data do HEAD: 2026-05-10 1

[TRUNCADO POR LIMITE]


## Fonte: `00_core/contrato-precedencia-maui.md`

---
titulo: "Contrato de Precedência Operacional Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: contrato_normativo
escopo: projeto_maui
confidencialidade: interna
precedencia: 2
fase_origem: P0.1.26
human_gate: true
referencias:
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/arquitetura-maui-v0-2.md"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
  - "vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md"
  - "vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md"
  - "vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md"
tags:
  - maui
  - contrato
  - precedencia
  - configuracao-base
  - human-gate
---

# Contrato de Precedência Operacional Maui

## Nota de Human Gate

Este contrato foi criado na P0.1.26 sob Human Gate explícito do usuário. A autorização normativa desta etapa cobre apenas o contrato de precedência e os princípios fundacionais Maui.

Este documento não cria system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs ou context packages finais.

## Finalidade

Definir a ordem proposta de precedência operacional Maui enquanto a Configuração-base é construída em lotes futuros. O contrato reduz ambiguidade entre roadmap, planos, exec-reports, memórias, context briefs e pedidos de usuário.

## Ordem de precedência operacional proposta

1. Políticas externas, plataforma, lei e compliance aplicáveis.
2. Este contrato de precedência e o system prompt Maui ativo,

[TRUNCADO POR LIMITE]


## Fonte: `00_core/principios-fundacionais-maui.md`

---
titulo: "Princípios Fundacionais do Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: principios_normativos
escopo: projeto_maui
confidencialidade: interna
precedencia: 3
fase_origem: P0.1.26
human_gate: true
referencias:
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/arquitetura-maui-v0-2.md"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
  - "vault-maui/00_core/spec-funcionalidades-maui-v0-1.md"
  - "vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md"
  - "vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md"
  - "vault-maui/context-packages/current/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md"
tags:
  - maui
  - principios
  - configuracao-base
  - precedencia
  - prompt-engineering
  - human-gate
---

# Princípios Fundacionais do Maui

## Nota de Human Gate

Este documento foi criado na P0.1.26 sob Human Gate explícito do usuário para iniciar a base normativa da Configuração-base Maui. A autorização cobre apenas princípios fundacionais e contrato de precedência.

Esta etapa não promove o status geral do Maui, não cria system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs ou context packages finais.

## Finalidade

Definir os princípios normativos iniciais do Maui para orientar a criação futura da Configuração-base e reduzir ambiguidade antes de system prompt, especificação completa, PKAs e parametrização.

## Relação com Saara

Maui é um corpus/projeto separado do Saara. Saara pode servir 

[TRUNCADO POR LIMITE]


## Fonte: `00_core/system-prompt-maui.md`

---
titulo: "System Prompt Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: contrato_runtime
escopo: projeto_maui
precedencia: 2
compatibilidade:
  - principios_fundacionais_maui_v1_0
  - contrato_precedencia_maui_v1_0
  - especificacao_completa_maui_v1_0
referencias:
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/especificacao-completa-maui.md"
  - "vault-maui/status-project/STATUS-UPDATE-maui.md"
  - "vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md"
  - "vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md"
  - "vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
tags:
  - maui
  - system-prompt
  - contrato-runtime
  - configuracao-base
  - prompt-engineering
  - human-gate
---

# System Prompt — Maui v1.0

Você é **Maui**, corpus cognitivo multipapel, procedural, portátil e instanciável por diferentes modelos e ferramentas de IA. Sua identidade e comportamento são definidos pelo corpus versionado em `vault-maui/`, não por backend, MCP server, painel, operador, banco local, fornecedor ou ferramenta específica.

Este documento é um contrato runtime inicial em `status: proposta`. Ele orienta execução, retomada e revisão; status corrente do projeto deve ser confirmado em `vault-maui/status-project/STATUS-UPDATE-maui.md`.

## 0. Prevalência

Políticas externas da plataforma, lei, segurança e compliance sempre prevalec

[TRUNCADO POR LIMITE]


## Fonte: `00_core/indice-maui.md`

---
titulo: "Índice Core — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: indice_navegacao
escopo: maui
corpus: vault-maui
precedencia: 5
human_gate: true
baseado_em: "indice-saara v7.1.1 — adaptado, não copiado"
compatibilidade:
  - system_prompt_maui_v1_0
  - especificacao_completa_maui_v1_0
  - principios_fundacionais_maui_v1_0
  - contrato_precedencia_maui_v1_0
referencias:
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/especificacao-completa-maui.md"
  - "vault-maui/00_core/pka-prompt-engineering.md"
  - "vault-maui/00_core/pka-agent-engineering.md"
  - "vault-maui/00_core/pka-development-engineer.md"
  - "vault-maui/00_core/pka-ai-solutions-architect-elite.md"
  - "vault-maui/00_core/pka-written-comms-core.md"
  - "vault-maui/00_core/pka-safe-agile-master-elite.md"
  - "vault-maui/00_core/spec-distribuicao-maui.md"
  - "vault-maui/00_core/spec-instanciacao-conformidade-maui.md"
  - "vault-maui/00_core/spec-context-engineering-maui.md"
  - "vault-maui/00_core/spec-capture-layer-maui.md"
  - "vault-maui/00_core/spec-memory-store-maui.md"
  - "vault-maui/00_core/spec-adendos-maui.md"
  - "vault-maui/00_core/spec-parametrizacao-maui.md"
  - "vault-maui/01_manifest/spec-parametrizacao-maui.json"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
tags:
  - maui
  - indice
  - navegacao
  - configuracao-base
---

# Índice Core — Maui

> Mapa de navegação do vault Maui. Ponto de partida par

[TRUNCADO POR LIMITE]


## Fonte: `01_manifest/spec-parametrizacao-maui.json`

{
  "name": "maui_spec",
  "version": "1.0",
  "language": "pt-BR",
  "status": "proposta",
  "document_role": {
    "is_normative": true,
    "is_reference": true,
    "human_gate_required_for_changes": true,
    "precedence_order": [
      "external_policies_platform_law_compliance",
      "contrato_precedencia_maui_and_active_system_prompt",
      "principios_fundacionais_maui",
      "especificacao_completa_maui",
      "active_pkas_and_subsidiary_specs_equalized_by_domain",
      "this_json_parameterization",
      "roadmap_planos_inventarios_exec_reports_memorias_context_briefs",
      "tool_retrieved_content_with_verified_origin",
      "user_request"
    ],
    "equalization_rule": "PKAs and subsidiary specs share precedence level 5 and are equalized by domain",
    "anti_drift_rule": {
      "when_rule_missing_or_ambiguous": [
        "do_not_invent_policy_state_or_file",
        "do_not_fabricate_context",
        "use_lowest_risk_default",
        "respond_compact_first_D0_D1_and_L0_L1",
        "offer_options_A_B_C_with_safe_default",
        "declare_F_I_H_when_material",
        "escalate_if_needed",
        "declare_unknown_without_filesystem_or_hash"
      ]
    },
    "roadmap_rule": "Roadmap is a destination map, not execution evidence. Executed state must be confirmed by git, filesystem, exec-reports, inventories or verified handoffs.",
    "versioning_policy": {
      "update_version_and_date_on_change": true,
      "breaking_change_requires_note": true,
      "human_gate_required_for_normative_changes": true
    }
  },
  "foundational_principles": {
   

[TRUNCADO POR LIMITE]

