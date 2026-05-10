---
titulo: "Marco de memória — Fechamento da Tarefa 2 Documentação/"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - documentacao
  - tarefa-2
  - context-brief
  - p0-1
  - marco
deve_ser_considerado_em_context_brief: true
---

# Marco de memória — Fechamento da Tarefa 2 Documentação/

## Resumo

Registrar que a sessão fechou o saneamento inicial dos 8 arquivos inventariados em `Documentação/`, promovendo documentos relevantes ao core, arquivando rascunhos/pacotes e desbloqueando a retomada da P0.1.5.

## Decisões humanas registradas

- P0.1.9 aprovada: criação do template canônico `Maui Context Brief`.
- P0.1.10 executada: Codex instruído a criar Context Brief sob demanda.
- P0.1.11 não executada nesta sessão.
- P0.1.12 aprovada e executada: Lote A aplicado.
- P0.1.13 aprovada e executada: arquitetura Maui v0.2 promovida ao core.
- P0.1.14 aprovada e executada: roadmap Maui v1.0 promovido ao core.
- P0.1.15 aprovada e executada: spec funcional Maui v0.1 promovida ao core.
- P0.1.16 aprovada: registrar fechamento, reconciliar inventário e criar este marco de memória.

## Commits relevantes

- P0.1.9 — `26a56622f1d4f427fcddc288a09e81983b59ea36`
- P0.1.10 — `cbea5991947121b38b5e79d91959201b18860279`
- P0.1.12 — `4c63dbff803df726178318e0daa71ab749c60b02`
- P0.1.13 — `f1f50dbc85d082556385dafbd75340cf6edcb8cc`
- P0.1.14 — `28cfffe0f6e0bc386737f4db4c6307cf0555c50c`
- P0.1.15 — `cef5e65fd10faf3d2e1995b351468163a72868e3`

## Arquivos promovidos ao core

- `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md`
- `vault-maui/00_core/arquitetura-maui-v0-2.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md`

## Arquivos arquivados

- `vault-maui/context-packages/archive/spec-tecnica-atualizacao-saara-maui-v1.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-v1-0.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-draft.md`
- `vault-maui/context-packages/archive/arquitetura-novo-saara-maui-draft.md`

## Ressalvas aceitas

- `Documentação/` estava ignorada por `.gitignore` e fora do controle de versão.
- Por isso, algumas movimentações foram feitas com `mv` em vez de `git mv`.
- A preservação foi validada por hash e/ou comparação textual.
- Roadmap e spec funcional foram promovidos com notas de reconciliação, sem reescrita ampla.
- O status dos documentos promovidos permanece `proposta`.

## Efeito operacional

- A Tarefa 2 / saneamento inicial de `Documentação/` está concluída.
- `Documentação/` não possui pendências esperadas dos 8 arquivos inventariados.
- O próximo fluxo desbloqueado é P0.1.5 — plano de adaptação Saara→Maui.
- Context Briefs futuros devem considerar esta memória quando o escopo envolver retomada da adaptação Saara→Maui, saneamento documental, P0.1 ou documentos promovidos de `Documentação/`.

## Instrução para Context Brief

Ao criar um `Maui Context Brief`, se o escopo envolver continuidade do trabalho Saara→Maui, P0.1, documentação, inventário, core ou retomada após esta sessão, consultar esta memória e refletir:
- decisões fechadas;
- commits relevantes;
- documentos promovidos;
- documentos arquivados;
- pendências desbloqueadas;
- ressalvas aceitas.

## Próximo passo recomendado

Retomar P0.1.5 — plano de adaptação Saara→Maui, usando como base os documentos agora promovidos ao core.
