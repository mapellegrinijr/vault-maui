---
titulo: "Handoff — Pós-Configuração-base Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: handoff_sessao
escopo: maui
deve_ser_considerado_em_context_brief: true
confidencialidade: interna
tags:
  - maui
  - handoff
  - configuracao-base
  - p0.1
---

# Handoff — Pós-Configuração-base Maui

> Status: ativo · Data: 2026-05-06 · deve_ser_considerado_em_context_brief: true

---

## Estado real confirmado

A Configuração-base Maui está **completa**. Os 19 artefatos normativos (P0.1.26–P0.1.32) foram criados, revisados e sincronizados. O corpus `vault-maui/` é a fonte de verdade.

**Último commit desta sessão:** `538b441 feat(p0.1.32): revisao integrada configuracao-base Maui — correcoes A1 B1-B5 C1 + exec-report + memoria marco`

---

## Etapas concluídas com evidência

| Lote | Propósito | Evidência |
|------|-----------|-----------|
| P0.1.26 | Princípios e contrato de precedência | commit `1f32776` |
| P0.1.27 | Especificação completa Maui | commit `221d481` |
| P0.1.28 | System prompt Maui | commit `4493448` |
| P0.1.29 | 6 PKAs Maui | commit `4c06623` |
| P0.1.30 | 6 Specs subsidiárias Maui | commit `b8c8749` |
| P0.1.31 | Parametrização executável + índice core | commit `9f2afc9` |
| P0.1.32 | Revisão integrada (7 correções) | commit `538b441` |

---

## Próxima ação recomendada

**P0.2** (scripts de validação: `maui_vault_health.py`, `maui_validate_frontmatter.py`, `maui_validate_links.py`, `maui_context_export.py`) ou **P0.3** (operator packs: Claude Code, Codex, ChatGPT Handoff) — aguardar decisão humana explícita. **Não executar por inferência.**

---

## Ações proibidas por inferência

- P0.1.11 (nunca executada; não assumir equivalente)
- Qualquer lote do roadmap sem pedido explícito do usuário
- Promoção de `status: proposta` em qualquer normativo
- Alteração de `Documentação/`
- Criação de operator packs, bootstrap ou context packages de produção sem Human Gate
- Marcação de instância como `current` sem filesystem/hash verificável

---

## Arquivos a ler primeiro (ordem priorizada)

1. `vault-maui/00_core/contrato-precedencia-maui.md` — precedência operacional
2. `vault-maui/00_core/principios-fundacionais-maui.md` — 12 princípios
3. `vault-maui/00_core/system-prompt-maui.md` — contrato runtime
4. `vault-maui/00_core/indice-maui.md` — mapa de navegação e tabela de artefatos
5. `vault-maui/00_core/spec-parametrizacao-maui.md` + `vault-maui/01_manifest/spec-parametrizacao-maui.json` — Domain Router e parametrização
6. `vault-maui/memorias/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` — marco de conclusão P0.1.32
7. `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md` — achados e correções

---

## Como aplicar Saara 7.1.1 + PE Elite na próxima sessão

- **Papel:** Saara 7.1.1 + Prompt Engineering Elite operando sobre corpus Maui
- **Domain Router:** Prompt Engineering Elite lidera contratos textuais/instrucionais; Agent Engineering lidera integração sistêmica. Prioridades numéricas no JSON.
- **Modos:** A para governança, decisões normativas e riscos altos; B para execução previsível; B1 para execução com escalada
- **Profundidade:** D0–D3 (compact-first); não abrir D2/D3 por hábito
- **F/I/H:** declarar explicitamente quando material; nunca inventar estado, hash, versão ou arquivo
- **Alerta de contexto:** avisar quando restar ~15% de budget

---

## Regras de Human Gate

- Qualquer criação ou alteração de normativo (PKA, spec, system prompt, contrato de precedência, princípios) exige Human Gate explícito antes do commit
- Mudança de `status: proposta` exige Human Gate
- Adendos de PKA exigem Human Gate em toda transição de status
- Limite de 2 adendos pendentes por PKA

---

## Riscos e ressalvas

- **C2 (aberto):** `system-prompt-maui.md §8` ainda referencia context brief pré-P0.1.26. Novo context brief pós-P0.1.32 criado nesta sessão; §8 deve ser atualizado em curadoria futura com Human Gate.
- **spec-funcionalidades-maui-v0-1.md:** contém placeholder; requer curadoria futura.
- **Instâncias sem filesystem (ChatGPT):** declarar conformidade como `unknown`, nunca `current`.
- **vault-saara/:** não misturar com `vault-maui/`. Saara é referência conceitual, não fonte a copiar.
- **Roadmap como mapa:** roadmap não é evidência de execução; confirmar estado por Git, exec-reports e filesystem.

---

## Checklist de retomada

- [ ] Ler contrato de precedência e system prompt Maui
- [ ] Ler indice-maui.md para mapa completo dos artefatos
- [ ] Confirmar último commit via `git log --oneline -5`
- [ ] Ler memória marco P0.1.32 (`deve_ser_considerado_em_context_brief: true`)
- [ ] Identificar domínio da tarefa → ativar PKAs relevantes via Domain Router
- [ ] Verificar se tarefa exige Human Gate antes de criar/alterar normativo
- [ ] Não executar etapa do roadmap sem pedido explícito

---

## F/I/H

### Fatos

- Configuração-base Maui completa em 2026-05-06, commit `538b441`.
- 19 artefatos normativos criados e sincronizados.
- P0.3 e P0.4 desbloqueados para planejamento e execução.
- P0.1.11 permanece não executada.

### Inferências

- A próxima sessão provavelmente focará em P0.2 (scripts) ou P0.3 (operator packs), dado que a Configuração-base está completa.
- Context brief pós-P0.1.32 é a referência de retomada mais atual.

### Hipóteses

- O escopo de P0.3 seguirá o roadmap (Claude Code, Codex, ChatGPT Handoff) sem grandes revisões.
- Adendos de PKA não serão necessários antes de evidência operacional real.
