---
titulo: "Context Brief — Status Atual Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-10
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
deve_ser_considerado_em_context_brief: true
---

# Context Brief — Status Atual Maui

## Fonte de status corrente

- Fonte canônica de status do projeto: `vault-maui/status-project/STATUS-UPDATE-maui.md`.
- HEAD de referência na coleta: `da6cdfab7d7163db8c1fdd87396fc04f704acec4` (`feat(procedures): cria procedimento-preparar-handoff (proposta)`).
- Working tree na coleta: sujo por `vault-maui/00_core/system-prompt-maui.md.bak.disabled` não rastreado.
- Este brief é artefato de Project, não de runtime.

## Pacote mínimo de leitura (1–8)

1. `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md` — este brief.
2. `vault-maui/status-project/STATUS-UPDATE-maui.md` — status vivo do projeto.
3. `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff.md` — handoff desta sessão.
4. `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff.md` — exec-report desta sessão.
5. `vault-maui/00_core/contrato-precedencia-maui.md` e `vault-maui/00_core/principios-fundacionais-maui.md`.
6. `vault-maui/00_core/system-prompt-maui.md` e `vault-maui/00_core/indice-maui.md`.
7. `vault-maui/00_core/spec-parametrizacao-maui.md` e `vault-maui/01_manifest/spec-parametrizacao-maui.json`.
8. `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` — mapa de destino; confirmar execução por evidência.

## Estado confirmado

- Configuração-base concluída por P0.1.32, com evidência em exec-report, memória marco e commit `538b441`.
- Estrutura Project vs Runtime aplicada por `f8b5120`, `9c76d62`, `1d875e3` e consolidada no pacote manual-first `143a3d9`.
- Retomada Cowork e ajuste do system prompt foram commitados em `da00dbf` e `2e10432`.
- Procedure de handoff existe em `vault-maui/procedures/procedimento-preparar-handoff.md`, commit `da6cdfa`, com `status: proposta`.
- `context-packages/current/` deve ficar com este arquivo como brief current; os briefs anteriores foram movidos para `context-packages/archive/` nesta preparação.

## O que NÃO assumir

- Não assumir que P0.2, P0.3 ou P0.4 foram executadas.
- Não usar `vault-maui/panel/status.md` como fonte declarativa de estado.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` para retomada de Project.
- Não promover `status: proposta` de normativos ou procedures por inferência.
- Não apagar ou incorporar o arquivo `.bak.disabled` sem decisão humana explícita.

## Próximo passo recomendado (sem executar)

- Revisar Human Gate do pacote de handoff e decidir se deve haver commit único.
- Se aprovado, commitar apenas os artefatos de handoff/retomada e o arquivamento dos context briefs antigos, preservando o arquivo `.bak.disabled` sem alteração.
- Após isso, decidir explicitamente entre P0.2 e P0.3 se houver intenção de avançar roadmap.

## Fatos / Inferências / Hipóteses

- Fato: HEAD de referência é `da6cdfa`.
- Fato: working tree estava sujo antes da preparação por um arquivo `.bak.disabled` não rastreado.
- Fato: briefs antigos existiam em `context-packages/current/` e foram movidos para `archive/`.
- Inferência: manter apenas um brief em `current/` reduz ambiguidade de retomada.
- Hipótese: o arquivo `.bak.disabled` pode ser sobra operacional de outra sessão; não há evidência suficiente para removê-lo.
