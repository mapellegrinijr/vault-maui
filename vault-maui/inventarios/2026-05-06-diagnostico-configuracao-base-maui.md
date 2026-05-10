---
titulo: "Diagnóstico — Configuração-base Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: inventario_diagnostico
escopo: projeto_maui
fase: P0.1.24
confidencialidade: interna
---

# Diagnóstico — Configuração-base Maui

## Finalidade

Diagnosticar o estado atual da Configuração-base Maui, identificando artefatos existentes, planejados, ausentes e candidatos de adaptação Saara → Maui, sem criar ainda a configuração-base.

## Escopo

Este diagnóstico cobre documentos core, manifestos, schemas, operator packs, context packages, memórias e exec-reports relevantes ao planejamento da Configuração-base Maui. Não cria system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice, operator packs, context packages finais ou bootstrap.

## Fontes consultadas

- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-pre-planejamento-configuracao-base.md`
- `vault-maui/project-memories/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md`
- `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-22-reconciliacao-roadmap.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-23-correcao-memoria-defasada.md`
- `vault-maui/00_core/`
- `vault-maui/01_manifest/`
- `vault-maui/schemas/`
- `vault-maui/operator-packs/`
- `vault-maui/context-packages/`
- memórias marcadas com `deve_ser_considerado_em_context_brief: true`
- referências arquivadas em `vault-maui/context-packages/archive/` e inventários existentes, apenas para de/para conceitual.

## Estado atual

A Configuração-base Maui ainda não existe como pacote completo. O repositório contém documentos core de arquitetura, roadmap, spec funcional, spec técnica de atualização e regras operacionais, além de schemas iniciais, context briefs e readiness de Context Brief. Não foram encontrados system prompt Maui, especificação completa Maui, princípios fundacionais Maui, PKAs Maui, specs subsidiárias materializadas, parametrização Maui, índice core Maui, operator packs funcionais ou bootstrap final.

## De/para diagnóstico Saara → Maui

| Origem Saara | Candidato Maui | Estado atual Maui | Classificação | Human Gate |
| --- | --- | --- | --- | --- |
| `system-prompt.md` | `vault-maui/00_core/system-prompt-maui.md` | ausente | normativo/runtime | sim |
| `especificacao-completa.md` | `vault-maui/00_core/especificacao-completa-maui.md` | ausente | normativo | sim |
| `principios-fundacionais.md` | `vault-maui/00_core/principios-fundacionais-maui.md` ou decisão de herança/adaptação | ausente | normativo | sim |
| `pka-agent-engineering.md` | PKA Agent Engineering Maui | ausente | PKA normativa | sim |
| `pka-prompt-engineering.md` | PKA Prompt Engineering Maui obrigatória | ausente; decisão registrada na P0.1.24-pre | PKA normativa | sim |
| `pka-development-engineer.md` | PKA Development Engineer Maui | ausente | PKA normativa | sim |
| `pka-ai-solutions-architect-elite.md` | PKA AI Solutions Architect Maui | ausente | PKA normativa | sim |
| `pka-written-comms-core.md` | PKA Written Comms Maui | ausente | PKA normativa | sim |
| `pka-safe-agile-master-elite.md` | PKA SAFe/Agile Maui, se aplicável | ausente | PKA condicional | sim |
| `spec-distribuicao.md` | spec de distribuição Maui | ausente | spec subsidiária | sim |
| `spec-instanciacao-conformidade.md` | spec de instanciação/conformidade Maui | ausente | spec subsidiária | sim |
| `spec-context-injection.md` | spec de context injection/context engineering Maui | parcialmente coberta por arquitetura/spec funcional; arquivo próprio ausente | spec subsidiária | sim |
| `spec-capture-layer.md` | spec de capture layer Maui | ausente | spec subsidiária | sim |
| `spec-memory-store.md` | spec de memory store Maui | ausente; memórias operacionais existem em `vault-maui/project-memories/` | spec subsidiária | sim |
| `spec-adendos.md` | spec de adendos Maui | ausente | spec subsidiária | sim |
| `spec-parametrizacao.md` / `spec-parametrizacao.json` | parametrização Maui | ausente | técnico/executável | sim |
| `indice.md` | índice Maui | parcialmente coberto por READMEs; índice core com precedência ausente | normativo/operacional | sim |
| changelog Saara | changelog Maui | ausente | governança | sim |
| `CLAUDE.md`, `AGENTS.md`, Custom GPT instructions | operator packs P0.3 | diretórios existem, arquivos ausentes | target/tool | sim |
| bootstrap/context packages | P0.4 `maui-bootstrap.md` e pacotes por target | context briefs/readiness existem; bootstrap final ausente | target/contexto | sim |

## Artefatos existentes

| Artefato | Caminho | Função atual | Tipo |
| --- | --- | --- | --- |
| Arquitetura Maui | `vault-maui/00_core/arquitetura-maui-v0-2.md` | Define arquitetura corpus-first e camadas | normativo/proposta |
| Roadmap Maui | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | Mapa de destino reconciliado; inclui P0.1.24-pre | planejamento/proposta |
| Spec funcional Maui | `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | Visão funcional ampla; ainda com nota de reconciliação própria | normativo/proposta |
| Spec técnica atualização Saara → Maui | `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | Fonte técnica de migração/adaptação | normativo/proposta |
| Regras operacionais | `vault-maui/00_core/regras-operacionais.md` | Regras operacionais e Context Brief sob demanda para Codex | operacional |
| Memórias canônicas | `vault-maui/project-memories/` | Continuidade e decisões; diretório canônico | memória |
| Readiness Context Brief | `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md` | Precedência e limites para Context Brief | operacional |
| Context Brief template | `vault-maui/context-packages/templates/maui-context-brief.template.md` | Template de retomada | operacional/template |
| Schemas P0 iniciais | `vault-maui/schemas/*.schema.yaml` | Frontmatter, exec-report, exec-request, handoff, review-report | técnico |
| Diretórios de operator packs | `vault-maui/operator-packs/*/` | Estrutura alvo vazia por target | target/planejado |

## Artefatos ausentes

| Artefato | Caminho candidato | Impacto |
| --- | --- | --- |
| System prompt Maui | `vault-maui/00_core/system-prompt-maui.md` | Bloqueia instanciação manual confiável. |
| Especificação completa Maui | `vault-maui/00_core/especificacao-completa-maui.md` | Falta consolidação normativa do comportamento Maui. |
| Princípios fundacionais Maui | `vault-maui/00_core/principios-fundacionais-maui.md` | Falta decisão explícita de herança/adaptação Saara. |
| PKAs Maui | `vault-maui/00_core/pka-*.md` | Competências não materializadas no corpus. |
| PKA Prompt Engineering Maui | `vault-maui/00_core/pka-prompt-engineering.md` | Domínio obrigatório decidido, mas ainda não materializado. |
| Specs subsidiárias Maui | `vault-maui/00_core/spec-*.md` ou caminho aprovado | Lacunas em distribuição, instanciação, contexto, capture, memória e adendos. |
| Parametrização Maui | `vault-maui/01_manifest/spec-parametrizacao.*` ou caminho aprovado | Falta contrato executável de parâmetros. |
| Índice core Maui | `vault-maui/00_core/indice.md` ou caminho aprovado | Falta índice de precedência e navegação core. |
| Operator packs funcionais | `vault-maui/operator-packs/*/*` | Diretórios existem, mas sem templates/arquivos. |
| Bootstrap final | `vault-maui/context-packages/current/maui-bootstrap.md` | Ausente; não deve ser criado antes da configuração-base. |
| Changelog Maui | caminho a definir | Falta trilha dedicada de evolução normativa/configuracional. |

## Artefatos planejados mas não materializados

| Artefato planejado | Evidência de planejamento | Estado |
| --- | --- | --- |
| Configuração-base Maui | roadmap P0.1.24-pre e memória de decisão P0.1.24-pre | planejada; diagnóstico em P0.1.24 |
| Prompt Engineering Elite | roadmap P0.1.24-pre e memória de decisão | obrigatório; PKA ausente |
| P0.1.25 plano de implementação | roadmap P0.1.24-pre | futuro, depende de aprovação |
| Operator packs P0.3 | roadmap/spec funcional/spec técnica | dependem da configuração-base |
| Context packages P0.4 | roadmap/spec funcional/spec técnica | dependem da configuração-base |
| Instanciação manual | diagnóstico P0.1.17 e memórias | não pronta |

## Análise da PKA Prompt Engineering Elite

Prompt Engineering Elite deve existir como PKA/competência obrigatória, não absorvida por Agent Engineering.

Deve aparecer em:

- system prompt Maui;
- especificação completa Maui;
- parametrização Maui;
- índice core Maui;
- operator packs;
- rubricas e evals prompt-level;
- templates de prompts executáveis;
- handoff protocol.

Responsabilidades próprias:

- prompts, system prompts e developer prompts;
- instruction sets e templates;
- rubricas e testes prompt-level;
- diagnóstico de falha instrucional;
- mitigação textual de prompt injection.

Fronteira: Agent Engineering lidera agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout. Em tarefas híbridas, Prompt Engineering lidera o contrato textual/instrucional e Agent Engineering lidera a integração sistêmica/operacional.

Risco de ausência: system prompts e templates podem colapsar em Agent Engineering, reduzindo qualidade instrucional, rastreabilidade de rubricas, controle de prompt injection e diagnóstico de falhas prompt-level.

## Dependências

| Dependência | Bloqueia ou influencia |
| --- | --- |
| Decisão de princípios Maui | system prompt, especificação completa, contrato de precedência |
| PKAs Maui | system prompt, operator packs, rubricas, evals e handoffs |
| Parametrização Maui | instanciação, conformidade, drift e geração de packs |
| Índice core Maui | seleção de contexto, precedência e bootstrap |
| Configuração-base | operator packs P0.3 e context packages P0.4 |
| Human Gate | criação/alteração de artefatos normativos e configuração-base |

## Riscos

| Risco | Impacto | Mitigação recomendada |
| --- | --- | --- |
| Criar operator pack antes da configuração-base | Packs inconsistentes ou incompletos | Executar P0.1.25 antes de P0.3/P0.4. |
| Copiar Saara integralmente | Herança indevida ou conflito de identidade | Fazer adaptação curada e registrar decisões. |
| Omitir Prompt Engineering Elite | Falha instrucional sem dono claro | Criar PKA própria e referenciá-la em artefatos core. |
| Promover status prematuramente | Falsa prontidão Maui | Manter `status: proposta` até decisão humana. |
| Usar ChatGPT/Handoff como `current` sem hash | Falsa conformidade | Usar `unknown` sem filesystem/hash verificável. |

## Recomendações para P0.1.25

1. Planejar a sequência de criação da configuração-base sem criar arquivos finais ainda.
2. Definir nomes e caminhos canônicos dos artefatos core da configuração-base.
3. Definir ordem de implementação: princípios/precedência, especificação completa, system prompt, PKAs, specs subsidiárias, parametrização, índice.
4. Incluir PKA Prompt Engineering Maui como obrigatória e separada de Agent Engineering.
5. Definir critérios de Human Gate para cada artefato normativo.
6. Deixar operator packs P0.3 e context packages P0.4 dependentes da configuração-base aprovada.

## Limites do diagnóstico

- Não lê nem copia conteúdo Saara integralmente.
- Não cria ou adapta arquivos de configuração-base.
- Não altera `vault-maui/00_core/`.
- Não altera `Documentação/`.
- Não executa P0.1.11, P0.1.25 ou instanciação manual.

## F/I/H

### Fatos

- P0.1.24-pre registrou Configuração-base Maui no roadmap.
- Prompt Engineering Elite foi decidida como PKA/competência obrigatória.
- `vault-maui/00_core/` não contém `system-prompt-maui.md`, `especificacao-completa-maui.md`, `principios-fundacionais-maui.md` ou `pka-*.md`.
- `vault-maui/operator-packs/` contém diretórios por target, mas não arquivos funcionais.
- `vault-maui/context-packages/current/` contém Context Briefs, mas não `maui-bootstrap.md`.

### Inferências

- A configuração-base deve preceder operator packs P0.3 e context packages P0.4 para evitar packs gerados sobre uma base incompleta.
- A PKA Prompt Engineering Maui deve ser criada antes de system prompts/templates finais ou ao menos como parte do mesmo pacote de configuração-base.
- P0.1.25 deve ser um plano de implementação antes de qualquer criação de arquivos normativos.

### Hipóteses

- Parte dos artefatos Saara pode ser adaptada, mas isso exige curadoria e Human Gate.
- Alguns schemas futuros de context package/operator pack podem ser necessários, pois os schemas atuais ainda são parciais em relação ao roadmap.
