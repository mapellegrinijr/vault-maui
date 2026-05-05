---
titulo: "Handoff de sessão Maui — fechamento Tarefa 2 e preparação P0.1.17"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: saara_chatgpt
destino_esperado: saara_qualquer
fase_atual: P0.1.16-concluida
proxima_acao: >
  Criar um Maui Context Brief para preparar P0.1.17 — normalização do
  diretório canônico de memórias. O brief deve consultar o marco de memória
  da P0.1.16, exec-reports recentes, inventário reconciliado, regras
  operacionais e documentos core promovidos. Deve registrar explicitamente a
  ambiguidade entre vault-maui/memoria/ e vault-maui/memorias/ como risco/lacuna
  antes de qualquer movimentação.
deve_ser_considerado_em_context_brief: true
---

# Handoff de sessão Maui — fechamento Tarefa 2 e preparação P0.1.17

## 1. Resumo executivo

Esta sessão continuou as atividades de atualização do Saara para o Maui a partir do handoff pós-inventário de `Documentação/`.

O bloqueio principal era a **Tarefa 2 — decisão arquivo a arquivo sobre os 8 documentos inventariados em `Documentação/`**. A sessão concluiu essa frente: os documentos foram classificados, registrados, movidos/promovidos/arquivados por lotes, e o fechamento foi registrado no inventário e em marco de memória.

Também foi criado e incorporado o padrão operacional **Maui Context Brief**, incluindo instrução para o Codex gerar briefs sob demanda e regra para priorizar memórias marcadas com `deve_ser_considerado_em_context_brief: true`.

Ao final, surgiu uma nova pendência estrutural: existem `vault-maui/memoria/` e `vault-maui/memorias/`. Antes de normalizar, recomenda-se criar um Context Brief específico para P0.1.17.

## 2. Estado atual

- Tarefa 2 / saneamento inicial de `Documentação/`: concluída.
- P0.1.16: concluída e commitada.
- `Documentação/`: não possui mais os 8 arquivos originalmente inventariados.
- Documentos relevantes foram promovidos para `vault-maui/00_core/`.
- Rascunhos e pacotes históricos foram arquivados em `vault-maui/context-packages/archive/`.
- Codex foi instruído a gerar `Maui Context Brief` sob demanda.
- Claude Code ainda não foi atualizado para Context Brief sob demanda; P0.1.11 permanece não executada por decisão do usuário.
- Nova pendência: ambiguidade entre `vault-maui/memoria/` e `vault-maui/memorias/`.

## 3. Decisões humanas registradas nesta sessão

### 3.1 P0.1.9 — Maui Context Brief

O usuário aprovou a criação do padrão **Maui Context Brief**, com objetivo de recuperar o contexto mínimo necessário para continuidade de tarefas no Maui.

Função aprovada:
- consultar corpus, memórias, adendos, handoffs, insights, exec-reports, review-reports, inventários e atualizações relevantes;
- registrar fontes consultadas e ausentes;
- pedir ao usuário documentos/anexos quando houver lacuna essencial;
- não inventar status, versões, hashes, decisões ou conteúdo ausente;
- permitir continuidade degradada apenas com confiança explicitamente marcada.

Commit detectado posteriormente:
- `26a56622f1d4f427fcddc288a09e81983b59ea36`

### 3.2 P0.1.10 — Codex Context Brief sob demanda

Executado e aceito com ressalva.

Arquivo alterado:
- `vault-maui/00_core/regras-operacionais.md`

Exec-report:
- `vault-maui/exec-reports/submitted/2026-05-05-p0-1-10-codex-context-brief.md`

Commit:
- `cbea5991947121b38b5e79d91959201b18860279`

Ressalva aceita:
- Não havia arquivo específico versionado em `vault-maui/operator-packs/codex/`; a instrução foi registrada no documento operacional canônico dos executores.

### 3.3 P0.1.11 — Claude Code Context Brief sob demanda

Não executada por decisão do usuário.

Foi criado um prompt para executar P0.1.11, mas a execução foi explicitamente adiada.

Status:
- pendente;
- não há commit `p0.1.11`, confirmado durante P0.1.16.

### 3.4 P0.1.12 — Aplicar Lote A de Documentação/

Executado e aceito com ressalva.

Ações:
- moveu a spec técnica v2 para `vault-maui/00_core/`;
- arquivou a spec técnica v1;
- arquivou os dois pacotes documentais;
- arquivou o rascunho inicial sem extensão.

Commit:
- `4c63dbff803df726178318e0daa71ab749c60b02`

Ressalva aceita:
- `git mv` não pôde ser usado porque `Documentação/` estava ignorada por `.gitignore` e fora do controle de versão; foi usado `mv`, com preservação validada por hash.

### 3.5 P0.1.13 — Arquitetura Maui v0.2

Executado e aceito com ressalva.

Ação:
- corrigiu apenas o frontmatter inválido de `Documentação/arquitetura_maui_v_0_2.md`;
- moveu para `vault-maui/00_core/arquitetura-maui-v0-2.md`;
- preservou o corpo do documento.

Commit:
- `f1f50dbc85d082556385dafbd75340cf6edcb8cc`

Frontmatter aplicado:

```yaml
---
titulo: "Arquitetura Alvo — Maui"
versao: "0.2"
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: especificacao_arquitetural
escopo: projeto_maui
---