---
titulo: "Plano — Implementação da Configuração-base Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: plano_implementacao
escopo: projeto_maui
fase: P0.1.25
confidencialidade: interna
---

# Plano — Implementação da Configuração-base Maui

## Finalidade

Definir lotes, dependências, arquivos-alvo, Human Gates, critérios de pronto e riscos para criar a Configuração-base Maui em tarefas futuras, sem criar ainda os artefatos finais.

## Escopo

Este plano cobre a sequência de implementação da Configuração-base Maui: princípios e precedência, especificação completa, system prompt, PKAs, specs subsidiárias, parametrização, índice e revisão integrada. Não executa P0.1.26 nem etapas posteriores.

## Fontes consultadas

- `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-diagnostico-configuracao-base.md`
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/memorias/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md`
- `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-22-reconciliacao-roadmap.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-23-correcao-memoria-defasada.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-diagnostico-configuracao-base.md`
- documentos existentes em `vault-maui/00_core/`
- documentos existentes em `vault-maui/01_manifest/`
- schemas existentes em `vault-maui/schemas/`

## Premissas

- Maui permanece `status: proposta`.
- P0.1.11 segue não executada.
- Instanciação manual Maui segue não pronta.
- `vault-maui/memorias/` é o diretório canônico de memórias.
- Prompt Engineering Elite é PKA/competência obrigatória no Maui.
- Operator packs P0.3 e context packages P0.4 dependem da Configuração-base.
- Criação ou alteração de documento normativo exige Human Gate.

## Limites

- Não criar `system-prompt-maui.md`.
- Não criar `especificacao-completa-maui.md`.
- Não criar/adaptar PKAs.
- Não criar specs subsidiárias.
- Não criar parametrização Maui.
- Não criar índice Maui.
- Não criar operator packs.
- Não criar context packages finais.
- Não copiar integralmente arquivos Saara para Maui.
- Não alterar `Documentação/`.

## Estado de partida pós-P0.1.24

A Configuração-base Maui não existe como pacote completo. Existem documentos core parciais, schemas iniciais, memórias, context briefs e readiness de Context Brief. Estão ausentes system prompt, especificação completa, princípios fundacionais Maui, PKAs Maui, specs subsidiárias, parametrização, índice core, operator packs funcionais e bootstrap final.

## Objetivo da Configuração-base Maui

Estabelecer a base cognitiva, normativa e configuracional que permitirá instanciar Maui com comportamento coerente, precedência explícita, competências PKA materializadas, parâmetros executáveis e referências core navegáveis, antes de gerar operator packs P0.3 e context packages P0.4.

## Artefatos-alvo

| Artefato | Caminho-alvo proposto | Classificação |
| --- | --- | --- |
| Princípios e precedência Maui | `vault-maui/00_core/principios-fundacionais-maui.md` ou decisão de herança/adaptação | adaptado do Saara |
| Contrato de precedência | incluído em princípios ou arquivo core próprio | Maui-native |
| Especificação completa Maui | `vault-maui/00_core/especificacao-completa-maui.md` | Maui-native/adaptado |
| System prompt Maui | `vault-maui/00_core/system-prompt-maui.md` | Maui-native |
| PKA Prompt Engineering Maui | `vault-maui/00_core/pka-prompt-engineering.md` | Maui-native obrigatória |
| PKA Agent Engineering Maui | `vault-maui/00_core/pka-agent-engineering.md` | adaptado do Saara |
| PKA Development Engineer Maui | `vault-maui/00_core/pka-development-engineer.md` | adaptado do Saara |
| PKA AI Solutions Architect Maui | `vault-maui/00_core/pka-ai-solutions-architect-elite.md` | adaptado do Saara |
| PKA Written Comms Maui | `vault-maui/00_core/pka-written-comms-core.md` | adaptado do Saara |
| PKA SAFe/Agile Maui | `vault-maui/00_core/pka-safe-agile-master-elite.md` | herdado temporariamente ou condicional |
| Specs subsidiárias Maui | `vault-maui/00_core/spec-*.md` ou caminho aprovado | adaptado/Maui-native |
| Parametrização Maui | `vault-maui/01_manifest/spec-parametrizacao-maui.md` e/ou `.json` | técnico/executável |
| Índice core Maui | `vault-maui/00_core/indice.md` | Maui-native |
| Changelog Maui | caminho a definir | futuro/fora do escopo P0.1 se não bloqueante |
| Operator packs | `vault-maui/operator-packs/*/` | target-specific; P0.3 |
| Context package bootstrap | `vault-maui/context-packages/current/maui-bootstrap.md` | target/contexto; P0.4 |

## Classificação dos artefatos

| Classe | Artefatos | Regra |
| --- | --- | --- |
| Maui-native | system prompt, índice core, contrato de precedência, Prompt Engineering Elite | Criar com identidade Maui, sem copiar Saara integralmente. |
| Adaptado do Saara | princípios, especificação completa, PKAs herdadas, specs subsidiárias | Adaptar com curadoria e Human Gate. |
| Herdado temporariamente | PKAs condicionais ou princípios ainda não reescritos | Só usar com marcação explícita e prazo de revisão. |
| Target-specific | CLAUDE.md, AGENTS.md, Custom GPT instructions, packs por ferramenta | Só após base aprovada. |
| Futuro/fora do escopo P0.1 | automações completas, MCP, plugins, packs expandidos | Não bloquear P0.1.25. |

## Ordem de implementação por lotes

### P0.1.26 — Definir princípios e contrato de precedência Maui

Escopo:
- decidir herança/adaptação dos princípios Saara;
- definir precedência operacional Maui;
- estabelecer regra de status, Human Gate, `unknown` sem hash e relação corpus/toolkit;
- não criar PKAs ainda, salvo aprovação explícita em tarefa futura.

Arquivos-alvo:
- `vault-maui/00_core/principios-fundacionais-maui.md` ou registro explícito de herança/adaptação;
- possível seção/arquivo de contrato de precedência, se aprovado.

Critérios de pronto:
- precedência operacional definida;
- herança/adaptação Saara decidida;
- limites para ChatGPT/Handoff `unknown` preservados;
- `status: proposta` preservado quando aplicável.

Human Gate: obrigatório.

### P0.1.27 — Criar especificação completa Maui

Escopo:
- consolidar arquitetura, spec funcional, regras operacionais, princípios e fronteiras;
- registrar identidade, governança, limites, papéis e dependências;
- manter status adequado, provavelmente `proposta`, salvo decisão humana explícita.

Arquivo-alvo:
- `vault-maui/00_core/especificacao-completa-maui.md`.

Critérios de pronto:
- cobre identidade, corpus, governança, precedência, PKAs planejadas e limites;
- referencia P0.1.26;
- não duplica integralmente documentos Saara.

Human Gate: obrigatório.

### P0.1.28 — Criar system prompt Maui

Escopo:
- liderado por Prompt Engineering;
- incorporar router de domínios;
- explicitar Prompt Engineering Elite como PKA obrigatória;
- declarar limites para ChatGPT/Handoff `unknown`;
- separar instruções universais de instruções target-specific.

Arquivo-alvo:
- `vault-maui/00_core/system-prompt-maui.md`.

Critérios de pronto:
- usa precedência P0.1.26 e especificação P0.1.27;
- separa Prompt Engineering e Agent Engineering;
- não assume instanciação manual pronta;
- não contém instruções específicas de `CLAUDE.md` ou `AGENTS.md`.

Human Gate: obrigatório.

### P0.1.29 — Criar/adaptar PKAs Maui

Escopo:
- incluir obrigatoriamente Prompt Engineering Elite;
- incluir Agent Engineering, Development Engineer, AI Solutions Architect, Written Comms e demais PKAs aprovadas;
- preservar fronteiras entre PKAs;
- definir PKAs condicionais.

Arquivos-alvo:
- `vault-maui/00_core/pka-prompt-engineering.md`;
- `vault-maui/00_core/pka-agent-engineering.md`;
- `vault-maui/00_core/pka-development-engineer.md`;
- `vault-maui/00_core/pka-ai-solutions-architect-elite.md`;
- `vault-maui/00_core/pka-written-comms-core.md`;
- `vault-maui/00_core/pka-safe-agile-master-elite.md`, se aplicável.

Critérios de pronto:
- Prompt Engineering não é absorvido por Agent Engineering;
- cada PKA declara responsabilidades, limites, inputs, outputs e critérios de sucesso;
- conflitos entre PKAs têm regra de precedência.

Human Gate: obrigatório.

### P0.1.30 — Criar specs subsidiárias Maui

Escopo:
- distribuição;
- instanciação/conformidade;
- context injection/context engineering;
- capture layer;
- memory store;
- adendos.

Arquivos-alvo candidatos:
- `vault-maui/00_core/spec-distribuicao-maui.md`;
- `vault-maui/00_core/spec-instanciacao-conformidade-maui.md`;
- `vault-maui/00_core/spec-context-engineering-maui.md`;
- `vault-maui/00_core/spec-capture-layer-maui.md`;
- `vault-maui/00_core/spec-memory-store-maui.md`;
- `vault-maui/00_core/spec-adendos-maui.md`.

Critérios de pronto:
- specs referenciam princípios, especificação completa, system prompt e PKAs;
- não criam operator packs nem bootstrap;
- definem dependências para P0.3/P0.4.

Human Gate: obrigatório.

### P0.1.31 — Criar parametrização e índice Maui

Escopo:
- parametrização executável;
- índice core;
- lista de PKAs ativas;
- roteamento;
- modos operacionais;
- política de disclosure e Human Gate.

Arquivos-alvo:
- `vault-maui/01_manifest/spec-parametrizacao-maui.md`;
- possível `vault-maui/01_manifest/spec-parametrizacao-maui.json`;
- `vault-maui/00_core/indice.md`.

Critérios de pronto:
- parametrização lista PKAs ativas e modos operacionais;
- índice aponta precedência e artefatos core;
- política `unknown` sem hash preservada;
- nenhuma target instruction final é criada.

Human Gate: obrigatório.

### P0.1.32 — Revisão integrada da Configuração-base Maui

Escopo:
- validar consistência entre arquivos;
- verificar links;
- confirmar que operator packs P0.3 e context packages P0.4 podem ser retomados;
- registrar lacunas remanescentes.

Arquivos-alvo:
- review report;
- exec-report;
- possível memória de marco compacta.

Critérios de pronto:
- todos os artefatos da configuração-base existem ou têm decisão explícita de adiamento;
- referências principais resolvidas;
- Prompt Engineering Elite presente nos pontos obrigatórios;
- P0.3/P0.4 liberados apenas com ressalvas explícitas.

Human Gate: obrigatório para aceitar a configuração-base.

## Dependências entre lotes

```text
P0.1.26 -> P0.1.27 -> P0.1.28 -> P0.1.29 -> P0.1.30 -> P0.1.31 -> P0.1.32
```

Dependências críticas:
- P0.1.27 depende de P0.1.26.
- P0.1.28 depende de P0.1.26 e P0.1.27.
- P0.1.29 depende de P0.1.26 e deve retroalimentar P0.1.28 se houver conflito.
- P0.1.30 depende de P0.1.27, P0.1.28 e P0.1.29.
- P0.1.31 depende de todos os artefatos normativos anteriores.
- P0.1.32 depende de todos os lotes anteriores.

## Human Gates obrigatórios

- Aprovar princípios e contrato de precedência.
- Aprovar especificação completa.
- Aprovar system prompt.
- Aprovar cada PKA ou lote de PKAs.
- Aprovar specs subsidiárias.
- Aprovar parametrização e índice.
- Aprovar revisão integrada antes de iniciar P0.3/P0.4.

## Papel da PKA Prompt Engineering Elite

Prompt Engineering Elite deve participar desde:

- system prompt;
- PKAs;
- parametrização;
- rubricas e evals prompt-level;
- templates de prompt;
- handoff protocol;
- diagnóstico de falha instrucional;
- mitigação textual de prompt injection.

Ela lidera contratos textuais/instrucionais. Não deve ser absorvida por Agent Engineering.

## Fronteira Prompt Engineering vs Agent Engineering

Prompt Engineering lidera prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

Agent Engineering lidera agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout.

Em tarefas híbridas:
- Prompt Engineering decide o contrato textual/instrucional;
- Agent Engineering decide a integração sistêmica e operacional.

## Riscos e mitigações

| Risco | Mitigação |
| --- | --- |
| Criar artefatos finais sem Human Gate | Exigir tarefa própria e aprovação por lote. |
| Copiar Saara integralmente | Adaptar por curadoria, com seção de herança explícita. |
| Prompt Engineering ausente ou absorvido | Criar PKA própria e referenciá-la em system prompt, índice e parametrização. |
| P0.3/P0.4 avançarem cedo | Bloquear operator packs e bootstrap até P0.1.32. |
| Conflitos entre PKAs | Usar contrato de precedência e revisão integrada. |
| ChatGPT/Handoff marcado `current` sem hash | Manter `unknown` sem filesystem/hash verificável. |

## Critérios de pronto da Configuração-base completa

- Princípios e precedência definidos.
- Especificação completa criada.
- System prompt criado.
- PKAs Maui criadas/adaptadas, incluindo Prompt Engineering Elite.
- Specs subsidiárias criadas ou explicitamente adiadas.
- Parametrização e índice core criados.
- Links e referências principais revisados.
- Human Gates registrados.
- P0.3/P0.4 liberados com pré-condições explícitas.
- P0.1.11 e instanciação manual não assumidas por inferência.

## Impacto em P0.3 operator packs

Operator packs só devem ser criados após a Configuração-base aprovada, porque dependem de system prompt, PKAs, parametrização, regras de precedência e limites por target.

## Impacto em P0.4 context packages/bootstrap

Context packages e bootstrap final dependem do índice core, seleção de contexto, system prompt, PKAs e regras `unknown` para targets sem filesystem/hash.

## Proposta de próximas tarefas

1. P0.1.26 — Definir princípios e contrato de precedência Maui.
2. P0.1.27 — Criar especificação completa Maui.
3. P0.1.28 — Criar system prompt Maui.
4. P0.1.29 — Criar/adaptar PKAs Maui.
5. P0.1.30 — Criar specs subsidiárias Maui.
6. P0.1.31 — Criar parametrização e índice Maui.
7. P0.1.32 — Revisão integrada da Configuração-base Maui.

Cada lote futuro deve ter prompt/tarefa próprio.

## F/I/H

### Fatos

- P0.1.24 diagnosticou que a Configuração-base Maui não existe como pacote completo.
- Prompt Engineering Elite é PKA/competência obrigatória decidida.
- `vault-maui/00_core/` não contém system prompt Maui, especificação completa Maui, princípios Maui nem PKAs Maui.
- Operator packs e bootstrap final estão ausentes.

### Inferências

- A ordem princípios → especificação completa → system prompt → PKAs → specs → parametrização/índice reduz retrabalho.
- P0.3 e P0.4 devem aguardar a revisão integrada da Configuração-base.
- Prompt Engineering Elite precisa aparecer antes ou junto do system prompt e das PKAs.

### Hipóteses

- Algumas PKAs Saara podem ser adaptadas com baixo risco se a herança for explicitada.
- Algumas specs subsidiárias podem ser combinadas ou adiadas se a P0.1.30 justificar.
