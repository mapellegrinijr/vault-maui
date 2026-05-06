---
titulo: "Maui Context Brief — Pós-P0.1.25 Configuração-base"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
uso_previsto: "futuras_instancias_maui_saara"
tarefa_relacionada: "pos-p0.1.25"
fontes_consultadas:
  - "vault-maui/00_core/"
  - "vault-maui/memorias/"
  - "vault-maui/inventarios/"
  - "vault-maui/planos/"
  - "vault-maui/exec-reports/submitted/"
  - "vault-maui/context-packages/readiness/"
lacunas_detectadas: true
requer_anexos_usuario: false
---

# Maui Context Brief — Pós-P0.1.25 Configuração-base

## Finalidade

Este context brief prepara futuras instâncias Maui e/ou Saara para retomar o projeto Maui no estado pós-P0.1.25, preservando a separação entre os corpus e evitando que planejamento seja tratado como execução.

## Estado atual consolidado

- Estado operacional: pós-P0.1.25.
- Próxima tarefa recomendada: P0.1.26, ainda não executada.
- Roadmap core: `status: proposta`.
- P0.1.11: não executada.
- Instanciação manual Maui: não pronta e fora do escopo atual.
- Configuração-base Maui: diagnosticada e planejada, mas não materializada como pacote completo.
- Prompt Engineering Elite: PKA/competência obrigatória decidida para Maui, ainda não materializada como PKA Maui.
- `vault-maui/memorias/`: diretório canônico de memórias.
- `Documentação/`: não deve ser reaberta sem decisão humana.

## Fontes obrigatórias para retomada

- `vault-maui/exec-reports/submitted/`
- `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
- `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
- `vault-maui/memorias/2026-05-06-marco-pos-p0-1-25-configuracao-base-maui.md`
- `vault-maui/memorias/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md`
- `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`, apenas como mapa de destino reconciliável.

## Ordem de precedência operacional

1. Git e filesystem local verificável.
2. Exec-reports em `vault-maui/exec-reports/submitted/`.
3. Inventários e planos em `vault-maui/inventarios/` e `vault-maui/planos/`.
4. Memórias em `vault-maui/memorias/` com `deve_ser_considerado_em_context_brief: true`.
5. Context briefs e readiness em `vault-maui/context-packages/`.
6. Handoffs recentes, quando existirem e forem verificáveis.
7. Roadmap core, como mapa de destino e não como fonte única de status executado.

## Decisões resumidas

- Maui e Saara são projetos/corpus separados.
- Saara pode servir como referência conceitual ou de/para, mas não deve ser copiado integralmente para Maui sem curadoria.
- Prompt Engineering Elite é obrigatório no Maui.
- Prompt Engineering não deve ser absorvido por Agent Engineering.
- A criação da Configuração-base deve ocorrer apenas em lotes futuros aprovados.
- Human Gate é necessário para criação/alteração de documentos normativos.

## Estado da Configuração-base Maui

A Configuração-base Maui não existe como pacote completo. O diagnóstico P0.1.24 identificou lacunas em system prompt, especificação completa, princípios, PKAs, specs subsidiárias, parametrização, índice core, operator packs e bootstrap/context packages finais. O plano P0.1.25 propõe implementação futura por lotes P0.1.26 a P0.1.32.

## Prompt Engineering Elite

Prompt Engineering Elite é obrigatório no Maui e deve aparecer, quando os artefatos forem materializados, em:

- system prompt Maui;
- especificação completa Maui;
- PKAs Maui;
- parametrização Maui;
- índice Maui;
- operator packs;
- rubricas e evals prompt-level;
- templates de prompts executáveis;
- protocolo de handoff.

Responsabilidades: prompts, system prompts, developer prompts, instruction sets, prompt templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

## Fronteira Prompt Engineering vs Agent Engineering

- Prompt Engineering lidera contrato textual/instrucional.
- Agent Engineering lidera agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout.
- Em tarefas híbridas, Prompt Engineering lidera o contrato textual e Agent Engineering lidera a integração sistêmica e operacional.

## O que não assumir

- Não assumir que P0.1.26 foi executada.
- Não assumir que P0.1.11 foi executada.
- Não assumir que instanciação manual Maui está pronta.
- Não assumir que existe system prompt Maui.
- Não assumir que existe especificação completa Maui.
- Não assumir que existem PKAs Maui materializadas.
- Não assumir que operator packs ou bootstrap final existem.
- Não assumir que roadmap sozinho prova execução.
- Não marcar ChatGPT/Handoff como `current` sem filesystem/hash verificável.

## Instruções para futuras instâncias sem filesystem

- Declarar `unknown` para qualquer estado que dependa de filesystem, hash, commit ou arquivo não anexado.
- Solicitar os arquivos mínimos de evidência antes de concluir status operacional.
- Não tratar handoff textual ou histórico de chat como `current` sem verificação.
- Não iniciar P0.1.26, P0.1.11 ou instanciação manual por inferência.
- Não criar configuração-base, operator packs ou bootstrap sem prompt/tarefa próprio e Human Gate quando aplicável.

## Relação com Saara

- Saara é corpus próprio.
- Maui é corpus/projeto separado.
- PKAs Saara podem servir como referência/de-para para Maui.
- Maui requer decisões próprias para princípios, PKAs, parametrização e precedência.
- É proibido copiar Saara integralmente para Maui sem curadoria e decisão explícita.

## Próximos passos recomendados

1. Validar este context brief e a memória marco pós-P0.1.25.
2. Executar P0.1.26 em tarefa separada para definir princípios e contrato de precedência Maui.
3. Manter P0.1.27 a P0.1.32 como plano proposto, não como execução.
4. Preservar Prompt Engineering Elite como obrigatório em todos os lotes da Configuração-base.

## Limites e riscos

- Este context brief não é configuração-base final.
- Este context brief não substitui exec-reports, inventários ou plano P0.1.25.
- Risco principal: instâncias futuras confundirem planejamento com execução.
- Risco adicional: importação acrítica de Saara contaminar a identidade própria do Maui.

## F/I/H

### Fatos

- P0.1.25 criou um plano de implementação da Configuração-base Maui.
- A Configuração-base Maui ainda não foi criada.
- Prompt Engineering Elite foi decidido como obrigatório no Maui.
- O roadmap permanece `status: proposta`.

### Inferências

- P0.1.26 é a próxima tarefa recomendada por ser o primeiro lote do plano P0.1.25.
- Futuras instâncias devem priorizar evidências de filesystem e exec-reports para determinar status real.

### Hipóteses

- A separação explícita Maui/Saara reduzirá risco de cópia indevida de corpus.
- Um context brief atual facilitará retomadas sem criar bootstrap final prematuramente.
