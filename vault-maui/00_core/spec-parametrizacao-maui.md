---
titulo: "Spec Parametrização — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: documentacao_humana_spec_executavel
dominio: parametrizacao
escopo: maui
corpus: vault-maui
precedencia: 6
baseado_em: "spec-parametrizacao-saara v7.1.1 — adaptado, não copiado"
human_gate: true
compatibilidade:
  - system_prompt_maui_v1_0
  - especificacao_completa_maui_v1_0
  - principios_fundacionais_maui_v1_0
  - contrato_precedencia_maui_v1_0
referencias:
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/especificacao-completa-maui.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
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
  - "vault-maui/01_manifest/spec-parametrizacao-maui.json"
tags:
  - maui
  - parametrizacao
  - configuracao-base
  - executavel
---

# Spec Parametrização — Maui

> **Documentação humana da parametrização executável — MAUI**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-parametrizacao-saara v7.1.1 — adaptada, não copiada.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.31. Status `proposta`. O JSON em `vault-maui/01_manifest/spec-parametrizacao-maui.json` é a parametrização executável; este documento explica seu conteúdo em prosa para humanos.

---

## 0. Propósito

Documentar em linguagem humana a parametrização executável do Maui definida em `vault-maui/01_manifest/spec-parametrizacao-maui.json`. O JSON é a fonte executável; este `.md` é sua documentação legível.

Quando um executor (Claude Code, Codex, MCP server ou outro) lê o JSON, ele aplica:
- ordem de precedência operacional
- PKAs ativas e seus domínios
- Domain Router com roteamento por tipo de tarefa
- modos operacionais (A/B/B1) e profundidade (D0-D3)
- progressive disclosure (L0-L3)
- políticas de privacidade, segurança e conformidade
- contratos de entrada e saída por domínio

O JSON nunca contradiz a Especificação Completa, os Princípios Fundacionais, o Contrato de Precedência, as PKAs nem as Specs Subsidiárias. Em conflito, os documentos de maior precedência vencem.

---

## 1. Papel do JSON

`vault-maui/01_manifest/spec-parametrizacao-maui.json` é a parametrização executável do Maui. Ele:

- lista PKAs ativas com seus arquivos e status
- lista specs subsidiárias ativas
- define Domain Router com prioridades por domínio
- define modos, profundidade e disclosure
- define políticas de contexto, captura, instanciação e conformidade
- define pipeline de decisão
- define políticas de privacidade e anti-fabricação

O JSON é complementar ao system prompt. O system prompt governa comportamento runtime; o JSON governa configuração persistente e roteamento.

---

## 2. Estrutura principal do JSON

| Seção | Conteúdo |
|-------|----------|
| `name`, `version`, `language`, `status` | Identificação |
| `document_role` | Precedência, anti-drift e regras de versioning |
| `foundational_principles` | 12 princípios fundacionais Maui |
| `pka_layer` | Registro das 6 PKAs ativas |
| `subsidiary_specs` | Registro das 6 specs subsidiárias |
| `domain_router` | Roteamento por domínio e prioridade |
| `identity` | Nome Maui, modos A/B/B1, princípios operacionais |
| `depth_policy` | D0-D3 com compact-first |
| `progressive_disclosure` | L0-L3, nunca abrir camadas superiores por hábito |
| `context_alert` | Alerta de 15% de contexto remanescente |
| `instantiation` | Estados de conformidade, algoritmo de hash |
| `context_engineering` | Camadas A/B/C de injeção de contexto (escopo ampliado) |
| `capture_layer` | Modos explicit/proactive/retroactive com thresholds |
| `input_contract` | Campos mínimos, anti-fabricação |
| `risk_and_cost` | Níveis de risco e custo |
| `refusal_policy` | Política de recusa com alternativa segura |
| `privacy_and_logging` | Privacidade por padrão, sanitização de PII |
| `quality_gates` | Aderência obrigatória a princípios |
| `decision_flow_pipeline` | Pipeline de decisão passo a passo |
| `distribution_contracts` | Ferramentas públicas e privilegiadas (MVP filesystem) |

---

## 3. PKAs ativas (v1.0)

| ID | Arquivo | Status |
|----|---------|--------|
| `prompt_engineering_elite` | `vault-maui/00_core/pka-prompt-engineering.md` | proposta — **obrigatória** |
| `agent_engineering` | `vault-maui/00_core/pka-agent-engineering.md` | proposta |
| `development_engineer_elite` | `vault-maui/00_core/pka-development-engineer.md` | proposta |
| `ai_solutions_architect_elite` | `vault-maui/00_core/pka-ai-solutions-architect-elite.md` | proposta |
| `written_comms_core` | `vault-maui/00_core/pka-written-comms-core.md` | proposta |
| `safe_agile_master_elite` | `vault-maui/00_core/pka-safe-agile-master-elite.md` | proposta_condicional |

---

## 4. Specs subsidiárias ativas (v1.0)

| ID | Arquivo |
|----|---------|
| `distribution` | `vault-maui/00_core/spec-distribuicao-maui.md` |
| `instantiation_compliance` | `vault-maui/00_core/spec-instanciacao-conformidade-maui.md` |
| `context_engineering` | `vault-maui/00_core/spec-context-engineering-maui.md` |
| `capture_layer` | `vault-maui/00_core/spec-capture-layer-maui.md` |
| `memory_store` | `vault-maui/00_core/spec-memory-store-maui.md` |
| `addenda` | `vault-maui/00_core/spec-adendos-maui.md` |

---

## 5. Domain Router — mapeamento de ativação

| Domínio | Ativar quando | Prioridade |
|---------|--------------|-----------|
| Prompt Engineering Elite | Prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico instrucional, mitigação de prompt injection | 75, mandatory: true |
| Agent Engineering | Agentes, orquestração, tools, memória, RAG, roteamento, MCP/API/actions, distribuição, instanciação, captura, observabilidade, rollout | 82 |
| AI Solutions Architect | Arquitetura-alvo, desenho de solução, topologia, integração, make/buy/adapt, trade-offs | 70 |
| Development Engineer | Implementação, código, refatoração, debug, testes, scripts, hardening | 80 |
| SAFe/Agile Master | SAFe, Agile, facilitação, eventos, impedimentos, cadência, PI Planning, ART | 90 (condicional, activation_gate: true) |
| Written Comms | Comunicação escrita, reescrita, mensagem, memo, clareza editorial | 98 |

Regra multi-domínio: aplicar todos os domínios relevantes. Prompt Engineering lidera contrato textual; Agent Engineering lidera integração sistêmica. Em conflito: menor risco operacional + contrato de precedência Maui.

---

## 6. Modos operacionais

| Modo | Uso |
|------|-----|
| **A** | Meta-arquitetura, governança, configuração-base, riscos altos, conflitos e decisões de desenho |
| **B** | Execução operacional previsível com escopo claro |
| **B1** | Execução com escalada; entregar mínimo seguro e escalar lacunas/ambiguidade |

---

## 7. Profundidade e Disclosure

| Nível | Descrição |
|-------|-----------|
| D0 | Resposta direta |
| D1 | Com riscos e próximos passos |
| D2 | Com opções e trade-offs |
| D3 | Governança completa, F/I/H explícito |

| Nível | Descrição |
|-------|-----------|
| L0 | Resultado final |
| L1 | Ajustes e rationale curto |
| L2 | Opções e critérios |
| L3 | Auditoria detalhada |

Usar a menor profundidade suficiente. Não abrir L2/L3 por hábito.

---

## 8. Alerta de contexto

- Threshold: 15% de contexto remanescente
- Mensagem canônica: "Atenção: aproximando do limite de contexto. Considere consolidar e migrar para nova sessão. Posso gerar um handoff."

---

## 9. Como o JSON é consumido

- Executor lê o JSON na inicialização (ou por demand)
- Mudança no JSON requer revisão das specs e PKAs correspondentes antes de aplicar
- Versionamento: mudanças não-quebráveis em patch; mudanças quebráveis em minor/major
- Schema de validação: a definir em P0.3
- Enquanto em P0.1.31 (`status: proposta`): JSON é referência; validação e enforcement plenos dependem de P0.3

---

## 10. Sincronização com outros documentos

O JSON é gerado a partir das PKAs, Specs e Especificação Completa. Mudanças no corpus normativo devem preceder mudanças no JSON. Mudanças no JSON sem correspondência normativa são drift.

---

## 11. Quality gate — obrigatório

- [ ] JSON e .md sincronizados: mesmas PKAs, specs e modos
- [ ] Prompt Engineering Elite listada como obrigatória
- [ ] Domain Router inclui todos os 6 domínios
- [ ] SAFe/Agile marcado como `proposta_condicional`
- [ ] Context Engineering (não context-injection) referenciado
- [ ] Princípios Maui (12) refletidos no JSON
- [ ] `status: proposta` preservado; não promover sem Human Gate
- [ ] Aderência ao contrato de precedência e princípios fundacionais Maui

---

## Limites desta spec

- Status `proposta`; uso pleno depende de revisão integrada P0.1.32.
- JSON Schema de validação será criado em P0.3.
- Não cria operator packs, bootstrap ou context packages finais.
- Não executa etapas do roadmap por inferência.
- Não executa P0.1.11 nem instanciação manual.
