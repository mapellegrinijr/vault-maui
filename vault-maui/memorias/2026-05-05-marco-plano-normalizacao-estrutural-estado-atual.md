---
titulo: "Marco de memória — Plano de normalização estrutural Maui e estado atual"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - normalizacao-estrutural
  - context-brief
  - p0-1
  - memoria
  - handoff
  - roadmap
deve_ser_considerado_em_context_brief: true
---

# Marco de memória — Plano de normalização estrutural Maui e estado atual

## Resumo

Este marco registra o plano de normalização estrutural do vault Maui e o ponto exato alcançado até aqui, para apoiar futuros `Maui Context Briefs`.

A sessão avançou a partir do fechamento da Tarefa 2 / saneamento inicial de `Documentação/`, criou base para `Maui Context Brief`, diagnosticou a estrutura do vault e iniciou a normalização por lotes.

## Estado atual consolidado

### Concluído

- Tarefa 2 / saneamento inicial de `Documentação/` concluída.
- Os 8 arquivos originalmente inventariados em `Documentação/` foram tratados.
- Documentos relevantes foram promovidos para `vault-maui/00_core/`.
- Rascunhos e pacotes históricos foram arquivados em `vault-maui/context-packages/archive/`.
- `Maui Context Brief` foi aprovado como padrão de retomada mínima confiável.
- Codex foi instruído a gerar `Maui Context Brief` sob demanda.
- P0.1.16 registrou fechamento da Tarefa 2 e criou memória de marco.
- P0.1.17 diagnosticou a estrutura do vault Maui.
- P0.1.18-pre reconciliou pendências do working tree antes da normalização.
- P0.1.18 normalizou o diretório canônico de memórias.
- P0.1.19 normalizou referências e wikilinks operacionais.

### Em preparação

- P0.1.20 — Lote 3: normalização de frontmatter e slugs operacionais.

### Ainda pendente

- P0.1.11 — instruir Claude Code a criar Context Brief sob demanda.
- Lote 4 — Context Brief readiness.
- Lote 5 — Instanciação manual Maui.
- Retomada da P0.1.5 — plano de adaptação Saara→Maui, após normalização estrutural suficiente.

## Commits relevantes

| Fase | Commit | Descrição |
|---|---|---|
| P0.1.9 | `26a56622f1d4f427fcddc288a09e81983b59ea36` | criação/aprovação do template `Maui Context Brief` |
| P0.1.10 | `cbea5991947121b38b5e79d91959201b18860279` | instrui Codex a criar Context Brief sob demanda |
| P0.1.12 | `4c63dbff803df726178318e0daa71ab749c60b02` | aplica Lote A da classificação de `Documentação/` |
| P0.1.13 | `f1f50dbc85d082556385dafbd75340cf6edcb8cc` | promove arquitetura Maui v0.2 ao core |
| P0.1.14 | `28cfffe0f6e0bc386737f4db4c6307cf0555c50c` | promove roadmap Maui v1.0 ao core |
| P0.1.15 | `cef5e65fd10faf3d2e1995b351468163a72868e3` | promove spec funcional Maui v0.1 ao core |
| P0.1.16 | `31c63e90f4c330d500701c79daf409155e24fe47` | fecha Tarefa 2 e registra marco de memória |
| P0.1.17 | `7de2211122aa709e484e232a4ff4af18afd99f32` | diagnostica estrutura do vault Maui |
| P0.1.18-pre | `1e12c08e544180cc16f0daa1417984e12c4a65a6` | reconcilia pendências antes da normalização de memórias |
| P0.1.18 | `ccf9efce4cea1261959c83beaf4c62836dce5266` | normaliza diretório canônico de memórias |
| P0.1.19 | `e554136d14f0bbcaec7e41a9e2096a7e24684e94` | normaliza referências e wikilinks operacionais |

## Documentos promovidos ao core

Os seguintes documentos foram promovidos para `vault-maui/00_core/`:

- `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md`
- `vault-maui/00_core/arquitetura-maui-v0-2.md`
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md`

Notas:
- `arquitetura-maui-v0-2.md` teve frontmatter corrigido.
- `roadmap-desenvolvimento-maui-v1-0.md` teve frontmatter corrigido e recebeu nota de reconciliação de status.
- `spec-funcionalidades-maui-v0-1.md` teve frontmatter corrigido e recebeu nota de reconciliação de status e alinhamento.
- O status dos documentos Maui promovidos permanece `proposta`.

## Documentos arquivados

Os seguintes documentos foram movidos para `vault-maui/context-packages/archive/`:

- `vault-maui/context-packages/archive/spec-tecnica-atualizacao-saara-maui-v1.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-v1-0.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-draft.md`
- `vault-maui/context-packages/archive/arquitetura-novo-saara-maui-draft.md`

## Plano de normalização estrutural

A normalização estrutural foi dividida em cinco lotes.

### Lote 1 — Memórias

Status: concluído na P0.1.18.

Decisão:
- `vault-maui/memorias/` é o diretório canônico de memórias do Maui.

Ações:
- template `Maui Context Brief` atualizado para consultar `vault-maui/memorias/`;
- memórias marcadas com `deve_ser_considerado_em_context_brief: true` confirmadas;
- diretório vazio `vault-maui/memoria/` removido localmente;
- registro de normalização criado.

Ressalva:
- remoção de `vault-maui/memoria/` não apareceu no commit porque Git não rastreia diretórios vazios.

### Lote 2 — Referências e wikilinks

Status: concluído na P0.1.19.

Ações:
- referências operacionais corrigidas;
- referências históricas e diagnósticas preservadas;
- documentos core atualizados de `memoria/` para `memorias/`;
- `vault-maui/panel/status.md` atualizado para o novo local do handoff;
- placeholders sem destino inequívoco preservados.

Pendências preservadas:
- `[[...]]` em documentos core como exemplo funcional;
- `[[link]]` e `[[wikilink]]` em documentos históricos/arquivados ou diagnósticos;
- wikilinks herdados sem destino inequívoco;
- `memoria/handoff-*.md` preservado como pendência de normalização de handoffs.

### Lote 3 — Frontmatter e slugs

Status: próximo passo imediato.

Objetivo:
- diagnosticar e corrigir frontmatter de arquivos operacionais atuais;
- preservar históricos, arquivados, inventários, exec-reports, handoffs e memórias, salvo necessidade operacional clara;
- diagnosticar inconsistências de slug;
- renomear apenas slugs com destino inequívoco e baixo risco;
- criar registro de normalização e exec-report.

Prompt para P0.1.20 já foi preparado, mas ainda não executado neste ponto.

### Lote 4 — Context Brief readiness

Status: pendente.

Objetivo:
- garantir que `Maui Context Brief` consiga localizar memórias, handoffs, exec-reports, insights, inventários e atualizações relevantes;
- validar se o template consulta as fontes corretas;
- verificar se memórias marcadas com `deve_ser_considerado_em_context_brief: true` são priorizadas;
- reduzir risco de perda de contexto entre sessões.

### Lote 5 — Instanciação manual Maui

Status: pendente.

Objetivo:
- avaliar e consolidar artefatos necessários para primeira instanciação manual confiável;
- verificar/criar `vault-maui/00_core/system-prompt.md`;
- verificar PKAs herdadas em `vault-maui/00_core/pka-*.md`;
- verificar operator packs;
- verificar context package bootstrap/current;
- garantir regra para instância sem filesystem declarar `unknown`, nunca `current`;
- preparar base para marco futuro de instanciação manual mínima.

## Handoffs e memórias relevantes

Handoffs relevantes:
- `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md`
- `vault-maui/handoffs/2026-05-05-handoff-fechamento-tarefa-2-pre-p0-1-17.md`

Memórias relevantes:
- `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`
- `vault-maui/memorias/2026-05-05-marco-decisao-normalizacao-estrutural.md`
- `vault-maui/memorias/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md`
- este marco de memória

Todas as memórias relevantes para retomada devem conter ou preservar:

`deve_ser_considerado_em_context_brief: true`

## Regras operacionais vigentes

- Após retorno do executor, classificar como:
  - `aceito`
  - `aceito com ressalva`
  - `precisa correção`
- Indicar somente o próximo passo imediato.
- Gerar no máximo um prompt por turno.
- Não executar P0.1.11 sem nova aprovação.
- Não alterar `Documentação/` sem decisão explícita.
- Mudanças normativas exigem Human Gate.
- Instância sem filesystem/hash declara `unknown`, nunca `current`.
- Status atual do Maui permanece `proposta`.
- Context Briefs futuros devem priorizar memórias em `vault-maui/memorias/` marcadas com `deve_ser_considerado_em_context_brief: true`.

## F/I/H

### Fatos

- Tarefa 2 foi concluída.
- P0.1.18 definiu `vault-maui/memorias/` como diretório canônico.
- P0.1.19 corrigiu referências operacionais e preservou histórico.
- P0.1.20 é o próximo lote planejado.
- P0.1.11 não foi executada.
- Instanciação manual ainda está em readiness experimental.

### Inferências

- A normalização estrutural deve continuar antes de retomar profundamente P0.1.5.
- Lote 3 reduzirá riscos para Context Brief e instanciação manual futura.
- Lotes 4 e 5 dependem de uma base documental mais consistente.

### Hipóteses

- Alguns arquivos sem frontmatter podem ser aceitáveis se forem templates, READMEs, históricos ou exemplos.
- Alguns placeholders podem ser intencionais como exemplos funcionais e não devem ser removidos sem análise contextual.
- A criação/adaptação de `system-prompt.md` e PKAs Maui deve ser tratada no Lote 5 ou em etapa imediatamente posterior.

## Instrução para futuros Maui Context Briefs

Ao criar um `Maui Context Brief` para qualquer tarefa relacionada a:

- normalização estrutural;
- P0.1.20;
- Context Brief readiness;
- instanciação manual;
- system prompt;
- PKAs;
- operator packs;
- continuação Saara→Maui;

consultar este marco e refletir:

- o plano de cinco lotes;
- os lotes já concluídos;
- commits relevantes;
- documentos promovidos ao core;
- diretório canônico de memórias;
- pendências preservadas;
- próximo passo imediato.

## Próximo passo recomendado

Executar **P0.1.20 — Lote 3: Frontmatter e slugs**, usando o prompt já preparado, e depois revisar o retorno antes de avançar para o Lote 4.