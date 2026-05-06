---
titulo: "Spec Instanciação e Conformidade — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: instanciacao_conformidade
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-instanciacao-conformidade-saara v7.1.1 — adaptado, não copiado"
human_gate: true
ativacao: "proposta — registry e CLI dependem de P0.3"
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
  - "vault-maui/00_core/spec-distribuicao-maui.md"
  - "vault-maui/00_core/spec-memory-store-maui.md"
tags:
  - maui
  - spec
  - instanciacao
  - conformidade
  - configuracao-base
---

# Spec Instanciação e Conformidade — Maui

> **Spec Subsidiária — MAUI | Instanciação e Conformidade**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-instanciacao-conformidade-saara v7.1.1 — adaptada, não copiada.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`. Registry e CLI planejados para P0.3.

---

## 0. Propósito

Definir como instâncias do Maui são registradas, rastreadas e verificadas quanto à conformidade com o corpus canônico em `vault-maui/`, detectando drift e permitindo reconciliação.

---

## 1. Conceitos fundamentais

- **Instância Maui:** qualquer execução ativa do corpus Maui em backend específico (Claude Code, ChatGPT, API custom, MCP server etc.)
- **hash_config:** hash SHA-256 calculado sobre o conteúdo dos arquivos normativos canônicos de `vault-maui/00_core/`
- **Tool Instance Registry (TIR):** índice SQLite que rastreia instâncias, seus hashes e estado de conformidade — planejado para P0.3
- **Conformidade:** comparação entre `hash_config` da instância em uso e o hash canônico atual do corpus

---

## 2. Cálculo do hash_config

```
hash_config = SHA-256(concat_sorted_contents(vault-maui/00_core/*.md))
```

- Arquivos ordenados alfabeticamente por caminho
- Conteúdo concatenado sem separador
- Hash recalculado a cada mudança normativa
- Hash registrado no TIR e em memórias de versionamento quando material

---

## 3. Estados de conformidade

| Estado | Significado |
|--------|-------------|
| `current` | hash_config da instância coincide com corpus canônico atual |
| `drift_minor` | diferença em arquivos não normativos (memórias, exec-reports, planos) |
| `drift_major` | diferença em PKA, spec ou normativo de precedência 5 ou superior |
| `incompativel` | diferença em system prompt, princípios fundacionais ou contrato de precedência |
| `unknown` | hash_config ausente ou não verificável; instâncias sem filesystem/hash verificável devem sempre declarar `unknown` |

**Regra anti-alucinação:** nunca declarar `current` sem hash verificável. Em ambientes como ChatGPT/Handoff onde o filesystem não é acessível, declarar `unknown` obrigatoriamente.

---

## 4. Tool Instance Registry (TIR) — planejado para P0.3

Schema mínimo (SQLite):

```sql
CREATE TABLE tool_instances (
  id TEXT PRIMARY KEY,
  backend TEXT NOT NULL,
  hash_config TEXT NOT NULL,
  status TEXT NOT NULL,  -- current | drift_minor | drift_major | incompativel | unknown
  data_registro TEXT NOT NULL,
  data_ultima_verificacao TEXT,
  notas TEXT
);
```

- Não confundir TIR com corpus Maui; TIR é infraestrutura de rastreamento
- TIR ausente em P0.1.30; referenciado como proposta para P0.3

---

## 5. Comandos de reconciliação (planejados para P0.3)

| Comando | Função |
|---------|--------|
| `maui status` | exibe estado de conformidade da instância atual |
| `maui register` | registra nova instância no TIR |
| `maui check` | verifica drift entre instância e corpus canônico |
| `maui diff` | exibe diferença detalhada por arquivo |
| `maui sync-instance` | atualiza instância para corpus canônico atual |
| `maui decommission` | remove instância do registry |

Comandos são propostos; não executar sem implementação P0.3.

---

## 6. Fluxo de verificação de conformidade (MVP atual)

Na ausência do TIR (pré-P0.3), o fluxo manual é:

1. Verificar existência dos arquivos normativos em `vault-maui/00_core/` via filesystem
2. Comparar commit SHA do corpus com o esperado via `git log`
3. Declarar `unknown` se filesystem não acessível
4. Declarar `current` somente com evidência verificável (git SHA, filesystem check)
5. Documentar estado no exec-report quando material

---

## 7. Quality gate — obrigatório

- [ ] Estado de conformidade declarado explicitamente (nunca inferido sem evidência)
- [ ] `unknown` declarado quando filesystem/hash não verificável
- [ ] hash_config calculado sobre arquivos normativos, não memórias
- [ ] TIR ausente declarado até P0.3
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 8. Dependências P0.3

- P0.3: implementar TIR (SQLite) e comandos de reconciliação
- P0.3: automatizar cálculo de hash_config em CI/CD
- P0.3: integrar verificação de conformidade com distribuição MCP/REST

---

## Limites desta spec

- Status `proposta`; TIR e CLI dependem de P0.3.
- Não cria banco de dados, scripts ou endpoints.
- Não executa etapas do roadmap por inferência.
- Não substitui verificação manual (git/filesystem) como evidência de conformidade no MVP atual.
