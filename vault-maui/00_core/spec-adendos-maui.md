---
titulo: "Spec Adendos — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: adendos
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-adendos-saara v7.1.1 — adaptado, não copiado"
human_gate: true
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
  - "vault-maui/00_core/pka-prompt-engineering.md"
  - "vault-maui/00_core/pka-agent-engineering.md"
  - "vault-maui/00_core/pka-ai-solutions-architect-elite.md"
  - "vault-maui/00_core/pka-development-engineer.md"
  - "vault-maui/00_core/pka-written-comms-core.md"
  - "vault-maui/00_core/pka-safe-agile-master-elite.md"
tags:
  - maui
  - spec
  - adendos
  - configuracao-base
---

# Spec Adendos — Maui

> **Spec Subsidiária — MAUI | Adendos de PKA**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-adendos-saara v7.1.1 — adaptada, não copiada.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`.

---

## 0. Propósito

Definir o mecanismo pelo qual PKAs Maui evoluem de forma incremental via adendos, sem modificar o corpo principal da PKA a cada iteração, preservando rastreabilidade, governança e aprovação humana.

Adendos são extensões de PKA produzidas pelo **Insight Pipeline**: observações operacionais, correções pontuais ou ajustes de comportamento que acumulam evidência antes de serem fundidos ao corpo da PKA na próxima revisão.

---

## 1. O que é um adendo

- Extensão incremental de uma PKA específica
- Produzido a partir de observação operacional real (não hipótese)
- Vinculado a uma PKA-alvo por `pka_alvo`
- Aprovado por Human Gate antes de ativação
- Fundido ao corpo da PKA na revisão integrada (quando elegível)

Adendos não substituem o corpo da PKA; coexistem até fusão. Em caso de conflito entre adendo ativo e corpo da PKA, o adendo ativo prevalece se aprovado via Human Gate.

---

## 2. Schema de adendo (frontmatter)

```yaml
---
adendo_id: "[pka-alvo]-adendo-[YYYY-MM-DD]-[slug]"
pka_alvo: "vault-maui/00_core/[pka-nome].md"
titulo: "[título conciso do adendo]"
versao: "1.0"
status: proposto | ativo | merged | rejeitado
data_criacao: "YYYY-MM-DD"
data_ativacao: "YYYY-MM-DD"  # preenchido quando status → ativo
data_merge: "YYYY-MM-DD"      # preenchido quando status → merged
evidencias:
  - "[descrição da observação ou incidente que motivou o adendo]"
aprovado_por: "[identificador do aprovador]"  # obrigatório para status ativo
human_gate: true
---
```

---

## 3. Localização dos adendos

Adendos são armazenados em subdiretórios por PKA, dentro de `vault-maui/00_core/`:

```
vault-maui/00_core/
├── pka-prompt-engineering.md
├── pka-prompt-engineering-adendos/
│   ├── pka-prompt-engineering-adendo-2026-06-01-ajuste-pipeline.md
│   └── pka-prompt-engineering-adendo-2026-07-15-novo-quality-gate.md
├── pka-agent-engineering.md
├── pka-agent-engineering-adendos/
│   └── ...
```

Convenção de nome: `[pka-slug]-adendo-[YYYY-MM-DD]-[slug-descritivo].md`

---

## 4. Ciclo de vida

```
proposto → [Human Gate] → ativo → [elegível após 60+ dias] → [Human Gate] → merged
                                                          → rejeitado
```

### 4.1 proposto
- Adendo criado com evidências
- Aguarda revisão humana
- Não tem efeito no comportamento da PKA

### 4.2 ativo
- Human Gate explícito aprovou
- Adendo entra em vigor como extensão da PKA-alvo
- Comportamento descrito no adendo deve ser seguido

### 4.3 merged
- Após 60+ dias em `ativo` com evidências consistentes
- Human Gate aprova fusão ao corpo da PKA
- Adendo marcado como `merged`; conteúdo integrado ao corpo da PKA na nova versão
- Arquivo do adendo preservado como histórico

### 4.4 rejeitado
- Human Gate rejeitou o adendo em qualquer fase
- Adendo marcado como `rejeitado`; não tem efeito
- Arquivo preservado para auditoria

---

## 5. Limite de adendos pendentes

- Máximo de **2 adendos em status `proposto` ou `ativo` por PKA** simultaneamente
- Se limite atingido: novo adendo só pode ser criado após fusão ou rejeição de um existente
- Exceção: Human Gate pode autorizar terceiro adendo por necessidade operacional documentada

---

## 6. Insight Pipeline (contexto)

O Insight Pipeline é o fluxo pelo qual observações operacionais se tornam adendos:

```
Observação operacional → Formulação de adendo → Validação de evidências
      ↓
Human Gate (aprovação) → Adendo ativo → Acúmulo de evidências
      ↓
Human Gate (merge) → Fusão ao corpo da PKA → Nova versão da PKA
```

Adendos não são produzidos por inferência ou antecipação; exigem evidência operacional real.

---

## 7. Quality gate — obrigatório

- [ ] Frontmatter canônico completo (adendo_id, pka_alvo, evidencias, aprovado_por)
- [ ] Evidências operacionais reais documentadas (não hipóteses)
- [ ] Human Gate respeitado em todas as transições de status
- [ ] Localização correta: subdiretório da PKA-alvo
- [ ] Limite de 2 adendos pendentes por PKA verificado
- [ ] Adendo não contradiz sistema de precedência Maui sem Human Gate explícito
- [ ] Status `ativo` exige aprovado_por preenchido
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` desta spec preservado; não promover sem Human Gate

---

## 8. Elegibilidade para merge

Um adendo é elegível para merge quando:
- status é `ativo` há pelo menos 60 dias; e
- evidências de uso consistente com o adendo foram acumuladas; e
- nenhuma regressão ou conflito foi registrado no período; e
- Human Gate aprova a fusão.

Não fundir adendos por prazo apenas; exigir evidência e aprovação.

---

## Limites desta spec

- Status `proposta`; uso pleno depende de PKAs em status adequado e evidências operacionais.
- Não cria adendos por antecipação; exige observação real.
- Não executa fusão de adendos sem Human Gate.
- Não executa etapas do roadmap por inferência.
