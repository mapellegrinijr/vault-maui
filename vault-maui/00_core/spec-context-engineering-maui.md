---
titulo: "Spec Context Engineering — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: context_engineering
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-context-injection-saara v7.1.1 — adaptado, não copiado"
human_gate: true
nota_nomenclatura: >
  'Context Engineering' é o nome intencional para Maui. Cobre escopo mais amplo que
  a injeção Saara: inclui também escrita (captura), seleção (retrieve), compressão e
  isolamento. Não renomear para 'context-injection' sem decisão humana explícita.
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
  - "vault-maui/00_core/spec-capture-layer-maui.md"
  - "vault-maui/00_core/spec-memory-store-maui.md"
tags:
  - maui
  - spec
  - context-engineering
  - configuracao-base
---

# Spec Context Engineering — Maui

> **Spec Subsidiária — MAUI | Context Engineering**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-context-injection-saara v7.1.1 — adaptada, não copiada.
> **Nomenclatura intencional:** "Context Engineering" cobre escopo mais amplo que "context-injection".

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`. Implementação plena das Camadas B e C depende de P0.3/P0.4.

---

## 0. Propósito

Definir como o contexto relevante do corpus Maui é **escrito** (capturado), **selecionado** (recuperado), **comprimido** (compactado), **isolado** (sanitizado) e **injetado** (distribuído ao modelo), garantindo que cada execução receba o contexto mínimo suficiente para retomada segura e previsível.

Context Engineering é mais amplo que injeção de contexto: governa todo o ciclo de vida do contexto — da captura à entrega. Saara chama essa camada de "context-injection"; Maui deliberadamente usa "context-engineering" para explicitar o escopo completo.

---

## 1. Ciclo de vida do contexto

```
Captura (Capture Layer) → Armazenamento (Memory Store)
      ↓
Seleção / Retrieve (este spec)
      ↓
Compressão / Compactação (este spec)
      ↓
Isolamento / Sanitização (este spec)
      ↓
Injeção / Distribuição (spec-distribuicao-maui.md)
      ↓
Execução no modelo
```

---

## 2. Modelo de camadas (A/B/C)

### Camada A — Configuração base (pré-carregada)

- Conteúdo: system prompt, princípios fundacionais, contrato de precedência
- Carregamento: automático, em toda instanciação
- Fonte: `vault-maui/00_core/system-prompt-maui.md`, `principios-fundacionais-maui.md`, `contrato-precedencia-maui.md`
- Custo de contexto: fixo; deve ser minimizado para preservar budget para B e C

### Camada B — Complementos de sessão (primeira chamada / sessão)

- Conteúdo: PKAs relevantes ao domínio da sessão, specs subsidiárias ativas, context brief atual
- Carregamento: na primeira chamada ou ao iniciar sessão com domínio identificado
- Fonte: `vault-maui/00_core/pka-*.md`, `vault-maui/00_core/spec-*-maui.md`, `vault-maui/context-packages/current/`
- Validade de cache: 4 horas; após expiração, recarregar do corpus
- Seleção: guiada pelo domínio da tarefa (ver seção 4)

### Camada C — Contexto conversacional (por turno)

- Conteúdo: memórias relevantes, exec-reports recentes, handoffs, decisões da sessão atual
- Carregamento: por turno, conforme relevância detectada
- Fonte: `vault-maui/memorias/`, `vault-maui/exec-reports/submitted/`, `vault-maui/handoffs/`
- Seleção: via `retrieve` com filtros de escopo, domínio e relevância

---

## 3. Budget de contexto

- `budget_camada_c: a_definir_em_P0.3`
- Alerta de 15%: quando contexto ativo atingir 85% do budget, alertar e priorizar compressão
- Prioridade de preenchimento: Camada A > Camada C (mais relevante) > Camada B complementar

> Budget de tokens para context engineering será calibrado empiricamente em P0.3, quando o retrieve com index SQLite estiver implementado. Valor fixo pré-P0.3 seria suposição sem base operacional.

---

## 4. Contrato de retrieve

### Entrada

```
retrieve(
  dominio: str,          // ex: "prompt-engineering", "agent-engineering"
  escopo: str,           // ex: "maui", "configuracao-base"
  confidencialidade: str, // ex: "interna", "restrita"
  max_tokens: int,       // padrão: 1200 tokens para Camada C
  filtro_data: str       // opcional; ex: "after:2026-05-01"
)
```

### Saída

```
[
  { arquivo: str, trecho: str, tokens: int, relevancia: float }
]
```

- Retornar apenas o que existir no corpus; nunca inventar conteúdo
- Se nenhum item relevante for encontrado, retornar lista vazia com flag `contexto_ausente: true`

---

## 5. Compressão

- Aplicada quando contexto excede budget ou quando Capture Layer solicita compactação
- Regras: preservar decisões, marcos, restrições e riscos; descartar conversa bruta e redundâncias
- Compressor usa LLM com prompt fixo de compactação (definido em P0.3)
- Output: markdown compacto com cabeçalho F/I/H quando material

---

## 6. Isolamento e sanitização

- Remover dados pessoais não necessários antes de persistir ou redistribuir
- Remover credenciais, tokens, paths de sistema não relevantes
- Marcar conteúdo sensível com `confidencialidade: restrita` antes de redistribuir
- Não redistribuir Camada B/C de uma sessão para outra sem sanitização

---

## 7. Quality gate — obrigatório

- [ ] Camadas A/B/C claramente distinguidas
- [ ] Budget de contexto respeitado
- [ ] Retrieve retorna apenas conteúdo verificável do corpus
- [ ] Compressão aplicada antes de exceder budget
- [ ] Sanitização aplicada antes de redistribuir
- [ ] Contexto ausente declarado explicitamente (nunca inventado)
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 8. Dependências P0.3/P0.4

- P0.3: implementar retrieve filtrado com index SQLite (Memory Store)
- P0.3: implementar compressor LLM com prompt fixo
- P0.3: implementar cache de Camada B com TTL configurável
- P0.4: otimizar budget dinâmico por tipo de tarefa

---

## Limites desta spec

- Status `proposta`; Camadas B e C dependem de P0.3/P0.4 para automação plena.
- Camada A é operável manualmente desde o MVP filesystem atual.
- Não cria endpoints, índices ou scripts.
- Não executa etapas do roadmap por inferência.
- Não renomear para "context-injection" sem decisão humana explícita.
