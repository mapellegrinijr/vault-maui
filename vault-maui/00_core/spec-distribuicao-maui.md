---
titulo: "Spec Distribuição — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: distribuicao
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-distribuicao-saara v7.1.1 — adaptado, não copiado"
human_gate: true
ativacao: "proposta — implementação plena depende de P0.3/P0.4"
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
  - "vault-maui/00_core/pka-agent-engineering.md"
  - "vault-maui/00_core/spec-instanciacao-conformidade-maui.md"
  - "vault-maui/00_core/spec-context-engineering-maui.md"
tags:
  - maui
  - spec
  - distribuicao
  - configuracao-base
---

# Spec Distribuição — Maui

> **Spec Subsidiária — MAUI | Camada de Distribuição**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-distribuicao-saara v7.1.1 — adaptada, não copiada.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`. Implementação plena depende de P0.3/P0.4.

---

## 0. Propósito

Definir como o corpus Maui (`vault-maui/`) é distribuído para diferentes backends e ferramentas de execução, mantendo a identidade Maui no corpus versionado e tratando a camada de distribuição como infraestrutura instrumental.

A distribuição entrega o corpus ao modelo ou ferramenta de execução; não é a identidade do Maui. O corpus vive em `vault-maui/`; a distribuição apenas o transporta.

---

## 1. Princípio fundamental

A identidade do Maui é o corpus em `vault-maui/`, não o backend que o executa. Nenhum modelo de distribuição altera, substitui ou define a identidade do Maui. A troca de backend não é troca de identidade.

---

## 2. Modelos de distribuição suportados

### 2.1 Filesystem estático pré-carregado (atual / MVP)

- O executor (Claude Code, script, CI/CD) lê arquivos diretamente de `vault-maui/`
- Sem intermediário de rede; sem sincronização automática
- Adequado para uso local e desenvolvimento
- **Status atual:** modelo em uso durante Configuração-base

### 2.2 MCP Server

- Maui exposto como servidor MCP (Model Context Protocol)
- Ferramentas (`read_corpus`, `retrieve_memory`, `inject_context`) servem conteúdo do vault
- Versionamento e conformidade via `spec-instanciacao-conformidade-maui.md`
- **Status:** planejado para P0.3/P0.4

### 2.3 REST + Actions

- API REST sobre o corpus; chamadas por ferramentas externas via HTTP
- Contrato de entrada/saída definido por Tool Contract
- Autenticação, rate limit e auditoria obrigatórios
- **Status:** planejado para P0.3/P0.4

### 2.4 Webhook / Event-driven

- Eventos externos disparam leitura ou atualização do corpus
- Adequado para integrações com CI/CD, versionamento automático de memórias
- **Status:** planejado para P0.4+

### 2.5 Filesystem sincronizado (distribuído)

- Corpus replicado para múltiplos ambientes via sync (rsync, git submodule, S3 mirror)
- Cada nó mantém cópia local; hash_config verifica conformidade
- **Status:** planejado para P0.4+

---

## 3. Contrato de distribuição (MVS)

Para o modelo filesystem estático atual:

- **Entrada:** caminho base do corpus (`vault-maui/`)
- **Saída:** conteúdo dos arquivos normativos e de memória relevantes
- **Seleção:** guiada por `spec-context-engineering-maui.md` (Camada A/B/C)
- **Conformidade:** verificada por `spec-instanciacao-conformidade-maui.md` quando registry disponível
- **Fallback:** se arquivo não encontrado, declarar ausência; não inventar conteúdo

---

## 4. Sincronização e versionamento

- Corpus Maui é a fonte de verdade; distribuição é downstream
- Atualizações ao corpus devem preceder qualquer atualização da distribuição
- Em caso de divergência entre corpus e cache distribuído: corpus prevalece
- Hash do corpus calculado sobre arquivos normativos de `vault-maui/00_core/`

---

## 5. Segurança e governança

- Nenhum modelo de distribuição autoriza acesso a `vault-maui/` além do escopo definido
- Conteúdo com `confidencialidade: restrita` não deve ser distribuído sem controle explícito
- Logs de distribuição devem ser auditáveis quando backend permitir
- Não distribuir arquivos de rascunho (`status: rascunho`) como normativos ativos

---

## 6. Quality gate — obrigatório

- [ ] Corpus Maui preservado como fonte de verdade; distribuição é instrumento
- [ ] Modelo de distribuição ativo declarado explicitamente
- [ ] Fallback definido para cada modelo
- [ ] Segurança e confidencialidade consideradas
- [ ] Conformidade rastreável quando registry disponível
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 7. Dependências P0.3/P0.4

- P0.3: implementar MCP Server e Tool Contracts para distribuição via protocolo
- P0.3: implementar REST + Actions para integrações externas
- P0.4: distribuição sincronizada e event-driven
- P0.3: registry de conformidade operacional (`spec-instanciacao-conformidade-maui.md`)

---

## Limites desta spec

- Status `proposta`; implementação plena depende de P0.3/P0.4.
- Não cria endpoints, tokens, servidores ou infraestrutura.
- Não executa etapas do roadmap por inferência.
- Não confunde a camada de distribuição com a identidade do Maui.
