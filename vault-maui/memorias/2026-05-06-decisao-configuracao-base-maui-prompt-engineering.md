---
titulo: "Memória de decisão — Configuração-base Maui e Prompt Engineering Elite"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_decisao
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - configuracao-base
  - prompt-engineering
  - pka
  - roadmap
  - p0-1-24
deve_ser_considerado_em_context_brief: true
---

# Memória de decisão — Configuração-base Maui e Prompt Engineering Elite

## Decisão

Registrar no roadmap uma frente explícita de Configuração-base Maui antes da P0.1.24.

Essa frente existe para planejar o diagnóstico e a implementação futura da base cognitiva/configuracional do Maui. A P0.1.24 deve ser diagnóstico da configuração-base; a P0.1.25 deve ser plano de implementação, se aprovada.

## Prompt Engineering Elite

Prompt Engineering Elite deve ser incluída como PKA/competência obrigatória no Maui.

Responsabilidades:

- prompts;
- system prompts;
- developer prompts;
- instruction sets;
- templates;
- rubricas;
- testes prompt-level;
- diagnóstico de falha instrucional;
- mitigação textual de prompt injection.

## Fronteira com Agent Engineering

Agent Engineering continua responsável por agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout.

Em tarefas híbridas prompt + agente:

- Prompt Engineering lidera contrato textual/instrucional;
- Agent Engineering lidera integração sistêmica e operacional.

## Limite desta etapa

Esta decisão não cria a configuração-base Maui.

Não foram criados:

- `system-prompt-maui.md`;
- `especificacao-completa-maui.md`;
- PKAs Maui;
- specs subsidiárias Maui;
- parametrização Maui;
- operator packs;
- context packages;
- bootstrap final.

## Próximo passo

Executar P0.1.24 como diagnóstico da Configuração-base Maui, sem assumir instanciação manual pronta e sem executar P0.1.11.
