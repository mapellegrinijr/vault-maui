---
titulo: "Marco pós-P0.1.25 — Configuração-base Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-25
  - configuracao-base
  - prompt-engineering
  - context-brief
  - handoff
deve_ser_considerado_em_context_brief: true
---

# Marco pós-P0.1.25 — Configuração-base Maui

## Resumo executivo

O Maui está em estado pós-P0.1.25. As tarefas P0.1.16 a P0.1.25 possuem evidência operacional em commits, exec-reports, inventários, plano e memórias. A Configuração-base Maui foi planejada, diagnosticada e teve plano de implementação proposto, mas ainda não existe como pacote materializado.

O próximo passo recomendado é P0.1.26, em tarefa separada, para definir princípios e contrato de precedência Maui. Esta memória não executa P0.1.26, não executa P0.1.11, não cria configuração-base e não assume instanciação manual pronta.

## Estado atual consolidado

- Roadmap core preserva `status: proposta`.
- Roadmap core deve ser tratado como mapa de destino, não como fonte única de status executado.
- `vault-maui/project-memories/` é o diretório canônico de memórias.
- `Documentação/` não possui pendência esperada e não deve ser reaberta sem decisão humana.
- P0.1.11 permanece não executada.
- Instanciação manual Maui permanece fora do escopo e não deve ser assumida como pronta.
- Prompt Engineering Elite foi decidido como PKA/competência obrigatória do Maui, mas ainda não foi materializado como PKA Maui.
- A Configuração-base Maui ainda não existe como pacote completo.
- O plano P0.1.25 propõe lotes P0.1.26 a P0.1.32 para implementação futura controlada.

## Linha do tempo P0.1.16 a P0.1.25

| Etapa | Estado | Evidência principal |
|---|---:|---|
| P0.1.16 | concluída | Commit `31c63e90f4c330d500701c79daf409155e24fe47`; exec-reports e inventários recentes sobre saneamento/documentação |
| P0.1.17 | concluída | Commit `7de2211122aa709e484e232a4ff4af18afd99f32`; diagnóstico estrutural do vault Maui |
| P0.1.18 | concluída | Commit `ccf9efce4cea1261959c83beaf4c62836dce5266`; normalização do diretório canônico de memórias |
| P0.1.19 | concluída | Commit `e554136d14f0bbcaec7e41a9e2096a7e24684e94`; normalização de referências e wikilinks operacionais |
| P0.1.20 | concluída | Commit `86756e18bf90d13b9036963fb7eecaf86603abc6`; `vault-maui/exec-reports/submitted/2026-05-05-p0-1-20-normalizacao-frontmatter-slugs.md` |
| P0.1.20-pre | concluída | Commit `0dc40fb3195f33092d9c9780937555804ac21e6b`; reconciliação de memória e context brief pós-normalização |
| P0.1.21 | concluída | Commit `03dab3d5258f433fd47b667a2a1531ec4a907798`; `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md` |
| P0.1.22 | concluída | Commit `a0ee423087a703b507e9ffce2718b5a567b4a541`; `vault-maui/exec-reports/submitted/2026-05-06-p0-1-22-reconciliacao-roadmap.md` |
| P0.1.23 | concluída | Commit `8804664f5b6298246608d21d27c922998ff6876a`; correção da memória defasada sobre P0.1.20 |
| P0.1.24-pre | concluída | Commit `7e43dbd0289f73208ccc3a3044993e092e0afc59`; planejamento da frente Configuração-base Maui |
| P0.1.24 | concluída | Commit `322b9afbb752d880375c7575bbbd35fc34fe15c8`; `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md` |
| P0.1.25 | concluída | Commit `5cbdceb4c6081cc75de30f8e76938ec35040f880`; `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md` |

## Decisões humanas registradas

- Incluir uma frente própria de Configuração-base Maui antes da continuidade operacional.
- Incluir Prompt Engineering Elite como PKA/competência obrigatória do Maui.
- Preservar a fronteira entre Prompt Engineering e Agent Engineering.
- Usar Saara apenas como referência/de-para curado, sem cópia integral automática.
- Não criar a Configuração-base Maui em P0.1.24-pre, P0.1.24, P0.1.25 ou neste marco pós-P0.1.25.
- Manter o roadmap como `status: proposta` até decisão humana explícita em tarefa separada.

## Estado dos principais diretórios e artefatos

| Área | Estado pós-P0.1.25 |
|---|---|
| `vault-maui/00_core/` | Contém roadmap e documentos core existentes; não contém pacote completo de Configuração-base Maui materializado. |
| `vault-maui/project-memories/` | Diretório canônico de memórias; contém memória de decisão sobre Configuração-base e Prompt Engineering. |
| `vault-maui/inventarios/` | Contém diagnóstico P0.1.24 da Configuração-base Maui. |
| `vault-maui/planos/` | Contém plano P0.1.25 de implementação da Configuração-base Maui. |
| `vault-maui/context-packages/readiness/` | Contém readiness P0.1.21 para Context Brief. |
| `vault-maui/context-packages/current/` | Área apropriada para briefs atuais; este marco pós-P0.1.25 possui brief próprio complementar. |
| `vault-maui/operator-packs/` | Sem operator packs Maui finais criados nesta sequência. |
| `vault-maui/exec-reports/submitted/` | Fonte operacional mais confiável para evidência de execução. |

## Concluído

- Reconciliação de progresso real até P0.1.21.
- Readiness de Context Brief.
- Correção de memória defasada sobre P0.1.20.
- Inclusão da frente Configuração-base Maui no planejamento.
- Diagnóstico dos artefatos de Configuração-base.
- Plano de implementação por lotes para P0.1.26 a P0.1.32.
- Registro de Prompt Engineering Elite como obrigatório no Maui.

## Pendente

- P0.1.11 permanece não executada.
- P0.1.26 ainda não foi executada.
- Princípios Maui e contrato de precedência ainda não foram definidos.
- Especificação completa Maui ainda não foi criada.
- System prompt Maui ainda não foi criado.
- PKAs Maui ainda não foram criadas/adaptadas.
- Specs subsidiárias Maui ainda não foram criadas.
- Parametrização e índice Maui ainda não foram criados.
- Operator packs P0.3 e context packages/bootstrap P0.4 ainda dependem da Configuração-base.
- Instanciação manual Maui ainda não está pronta.

## Riscos e ressalvas

- Usar o roadmap isoladamente pode contaminar retomadas futuras com status planejado tratado como executado.
- Copiar Saara integralmente para Maui pode quebrar a separação entre corpus/projetos.
- Ausência material de Prompt Engineering Elite como PKA Maui pode causar lacuna em prompts, templates, rubricas e mitigação textual de prompt injection.
- Criar operator packs ou bootstrap antes da Configuração-base pode consolidar instruções incompletas.
- ChatGPT/Handoff sem filesystem/hash verificável deve ser tratado como `unknown`, não como `current`.

## Próximos passos recomendados

1. Usar esta memória e o context brief pós-P0.1.25 como entrada de retomada.
2. Executar P0.1.26 apenas em tarefa própria, com Human Gate, para definir princípios e contrato de precedência Maui.
3. Manter P0.1.11 e instanciação manual fora do escopo até decisão explícita.
4. Não criar configuração-base, operator packs ou bootstrap por inferência.

## Limites deste marco

- Não executa P0.1.26.
- Não executa P0.1.11.
- Não executa instanciação manual Maui.
- Não cria Configuração-base Maui.
- Não altera `Documentação/`.
- Não altera `vault-maui/00_core/`.
- Não promove `status: proposta`.
- Não trata este arquivo como configuração-base final.

## F/I/H

### Fatos

- P0.1.21 a P0.1.25 possuem artefatos e commits citados neste marco.
- `vault-maui/project-memories/` é o diretório canônico de memórias.
- O roadmap core permanece `status: proposta`.
- A Configuração-base Maui ainda não existe como pacote completo materializado.

### Inferências

- P0.1.26 deve ser a próxima tarefa operacional porque o plano P0.1.25 a define como primeiro lote de implementação.
- Context briefs futuros devem priorizar exec-reports, inventários, planos e memórias marcadas para Context Brief sobre o roadmap isolado.

### Hipóteses

- Alguns artefatos Saara poderão ser úteis como referência de curadoria, desde que não sejam copiados integralmente para Maui sem decisão humana.
- A materialização da PKA Prompt Engineering Elite reduzirá riscos de lacunas instrucionais em system prompt, templates, rubricas e testes prompt-level.
