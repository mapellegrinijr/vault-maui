---
titulo: "Context Brief — Status Atual Maui v2"
versao: "1.0"
status: ativo
data_criacao: 2026-05-10
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
deve_ser_considerado_em_context_brief: true
---

# Context Brief — Status Atual Maui v2

## Fonte de status corrente

- Fonte canônica de status do projeto: `vault-maui/status-project/STATUS-UPDATE-maui.md`.
- HEAD de referência na coleta: `63530a8497d76761cf8a78365970c5a3e243fee3` (`docs(procedures): exigir protocolo prepare handoff no handoff principal do dia`).
- Working tree na coleta: sujo por `vault-maui/00_core/system-prompt-maui.md.bak.disabled` não rastreado.
- Este brief é artefato de Project e manual-first; não é artefato de runtime.

## Pacote mínimo de leitura (1–8)

1. `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md` — este brief current.
2. `vault-maui/status-project/STATUS-UPDATE-maui.md` — status vivo do projeto.
3. `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff-v2.md` — handoff principal do pacote.
4. `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff-v2.md` — exec-report de governança.
5. `vault-maui/procedures/procedimento-preparar-handoff.md` — procedure canônico do pipeline.
6. `vault-maui/00_core/contrato-precedencia-maui.md` e `vault-maui/00_core/principios-fundacionais-maui.md`.
7. `vault-maui/00_core/system-prompt-maui.md`, `vault-maui/00_core/indice-maui.md` e `vault-maui/00_core/spec-parametrizacao-maui.md`.
8. `vault-maui/01_manifest/spec-parametrizacao-maui.json` e `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.

## Estado confirmado

- Configuração-base concluída por P0.1.32, com evidência em exec-report, memória marco e commit `538b441`.
- Separação Project vs Runtime e pacote manual-first já foram consolidados por commits `f8b5120`, `9c76d62`, `1d875e3`, `143a3d9` e `10a37c0`.
- Procedure de handoff foi reforçado em `63530a8` para exigir seção específica no handoff principal.
- Este pacote v2 foi necessário porque os nomes-base de 2026-05-10 já existiam.
- Brief current anterior foi movido para `vault-maui/context-packages/archive/2026-05-10-context-brief-status-atual-maui.md`.

## O que NÃO assumir

- Não assumir execução de P0.2, P0.3, P0.4, P0.1.11 ou qualquer etapa do roadmap.
- Não usar `vault-maui/panel/status.md` como fonte declarativa de estado.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` para retomada de Project.
- Não promover `status: proposta` de normativos ou procedures por inferência.
- Não apagar, mover ou commitar `vault-maui/00_core/system-prompt-maui.md.bak.disabled` sem decisão humana explícita.

## Próximo passo recomendado (sem executar)

- Revisar Human Gate do pacote v2.
- Se aprovado, fazer commit único com os artefatos A–E e o move current → archive, excluindo o arquivo `.bak.disabled`.
- Depois do commit, usar como pacote mínimo: Status Update + este Context Brief current + Handoff principal.

## Fatos / Inferências / Hipóteses

- Fato: HEAD de referência é `63530a8`.
- Fato: working tree já estava sujo antes da geração por um arquivo `.bak.disabled` não rastreado.
- Fato: este pacote não alterou `00_core/`, `01_manifest/`, `Documentação/`, `memorias/` ou `status/`.
- Inferência: o sufixo `-v2` evita sobrescrever artefatos do mesmo dia e preserva auditabilidade.
- Hipótese: o `.bak.disabled` é resíduo operacional de outra sessão; falta evidência para qualquer ação automática.
