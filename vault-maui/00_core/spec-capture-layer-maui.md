---
titulo: "Spec Capture Layer — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: capture_layer
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-capture-layer-saara v7.1.1 — adaptado, não copiado"
human_gate: true
materializado_em: "P0.1.30 — spec materializada; implementação operacional depende de P0.3"
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
  - "vault-maui/00_core/spec-memory-store-maui.md"
  - "vault-maui/00_core/spec-context-engineering-maui.md"
tags:
  - maui
  - spec
  - capture-layer
  - configuracao-base
---

# Spec Capture Layer — Maui

> **Spec Subsidiária — MAUI | Capture Layer**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-capture-layer-saara v7.1.1 — adaptada, não copiada.
> **Materialização:** esta spec é materializada em P0.1.30 conforme declarado no system-prompt-maui.md §9 e §12. Implementação operacional plena depende de P0.3.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`. Implementação operacional depende de P0.3.

---

## 0. Propósito

Definir a camada inversa à distribuição: a **Capture Layer** observa conversas, seleciona o que tem valor futuro, compacta e persiste no Memory Store (`vault-maui/memorias/`), garantindo que o corpus Maui cresce com aprendizado real, não com ruído.

---

## 1. Arquitetura da Capture Layer

```
Observer → Selector → Compactor → Memory Store Writer
```

### 1.1 Observer

- Monitora a conversa ativa em busca de sinais de captura
- Sinais explícitos: usuário pede para salvar, lembrar, registrar ou documentar
- Sinais implícitos (proativo): decisão nova, marco atingido, risco identificado, preferência operacional revelada, artefato reutilizável
- Observer não decide; apenas detecta e sinaliza ao Selector

### 1.2 Selector

- Avalia cada sinal do Observer com scoring de relevância
- Threshold de ativação:
  - Captura explícita: 0.5 (limiar baixo; seguir instrução do usuário)
  - Captura proativa: 0.85 (limiar alto; só capturar se claramente valiosa para futuro)
- Critérios de score: novidade, acionabilidade futura, não-redundância com corpus existente, escopo claro

### 1.3 Compactor

- Recebe conteúdo selecionado e compacta para formato canônico de memória Maui
- Usa LLM com prompt fixo de compactação (definido em P0.3)
- Output: markdown estruturado com frontmatter canônico (ver Memory Store spec)
- Remove conversa bruta, preserva: decisão, contexto mínimo, escopo, data
- F/I/H explícito quando conteúdo mistura fato, inferência e hipótese

---

## 2. Modos de operação

| Modo | Trigger | Threshold |
|------|---------|-----------|
| `explicit` | instrução direta do usuário | 0.5 (sempre executar) |
| `proactive` | Observer detecta valor implícito | 0.85 (só se claramente valioso) |
| `retroactive` | revisão de conversa anterior | human gate explícito obrigatório |

**Modo MVS (P0.1.30):** apenas `explicit` está operacional na configuração-base. O modo `proactive` é definido nesta spec mas depende de automação em P0.3. O modo `retroactive` requer decisão humana explícita em qualquer fase.

---

## 3. Governança de captura

- Capture Layer é o **único escritor sanctioned** do Memory Store para memórias originadas em conversa
- Nenhuma outra camada escreve diretamente em `vault-maui/memorias/` sem passar pelo fluxo de captura ou Human Gate explícito
- Exceção: criação manual de memórias por commit human-approved (ex: exec-reports, decisões de P0)
- Sanitização obrigatória antes de persistir: remover dados pessoais desnecessários, credenciais, paths temporários
- Conteúdo capturado deve ter `escopo` e `confidencialidade` declarados no frontmatter

---

## 4. Seleção — critérios de não-captura

Não capturar:
- Conversa bruta sem valor futuro
- Fatos triviais já presentes no corpus
- Estado temporário ou de debugging pontual
- Conteúdo ambíguo sem possibilidade de verificação futura
- Qualquer conteúdo que identifique terceiros sem contexto necessário

---

## 5. Formato de saída da Capture Layer

Memória produzida pela Capture Layer deve respeitar o frontmatter canônico definido em `spec-memory-store-maui.md`. Campos obrigatórios no output do Compactor:

```yaml
---
titulo: "[descrição concisa]"
data: "[YYYY-MM-DD]"
tipo: decisao | marco | preferencia_operacional | risco | artefato | outro
escopo: maui | projeto_x
confidencialidade: interna | restrita
deve_ser_considerado_em_context_brief: true | false
fonte: explicit | proactive
---
```

---

## 6. Quality gate — obrigatório

- [ ] Observer não decide por conta própria; apenas sinaliza
- [ ] Selector aplica threshold correto por modo
- [ ] Compactor remove conversa bruta
- [ ] F/I/H explícito quando material
- [ ] Capture Layer é único escritor sanctioned do Memory Store (conversa)
- [ ] Sanitização aplicada antes de persistir
- [ ] Frontmatter canônico presente em toda memória capturada
- [ ] Modo `retroactive` bloqueado sem Human Gate
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 7. Dependências P0.3

- P0.3: implementar Observer automático integrado ao runtime
- P0.3: implementar Selector com scoring automatizado
- P0.3: implementar Compactor com LLM e prompt fixo de compactação
- P0.3: integrar Capture Layer com Memory Store (gravação via API interna)

---

## Limites desta spec

- Status `proposta`; Compactor LLM e Observer/Selector automáticos dependem de P0.3.
- Modo `explicit` operável manualmente desde o MVP: usuário instrui, Claude Code captura e grava.
- Não cria scripts, serviços ou endpoints.
- Não executa etapas do roadmap por inferência.
