# Status Update — Projeto Maui (Project)

- Gerado em: 2026-05-10T13:03:49-03:00
- HEAD: `63530a8497d76761cf8a78365970c5a3e243fee3` — 2026-05-10 15:59:53 +0000 — `docs(procedures): exigir protocolo prepare handoff no handoff principal do dia`
- Working tree: sujo — `git status --porcelain` registrou `?? vault-maui/00_core/system-prompt-maui.md.bak.disabled`; artefatos deste pacote v2 também ficam pendentes até Human Gate/commit.

## 1) TL;DR (5 bullets)

- HEAD atual é `63530a8`, que atualiza o procedure de handoff para exigir a seção “Protocolo Prepare Handoff (manual-first)” no handoff principal.
- Configuração-base Maui permanece concluída por evidência de P0.1.32: exec-report `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco e commit `538b441`.
- Este pacote cria versões `-v2` porque os nomes-base de 2026-05-10 já existem para context brief, handoff e exec-report.
- `context-packages/current/` deve manter apenas `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md`; o brief current anterior foi movido para `archive/`.
- Próximo passo é Human Gate: revisar e aprovar ou rejeitar commit único; nenhuma etapa do roadmap foi executada.

## 2) Evidência Git

Pré-validação obrigatória:

```text
$ git status --porcelain
?? vault-maui/00_core/system-prompt-maui.md.bak.disabled
```

```text
$ git log -1 --oneline
63530a8 docs(procedures): exigir protocolo prepare handoff no handoff principal do dia
```

- HEAD completo: `63530a8497d76761cf8a78365970c5a3e243fee3`
- Data do HEAD: 2026-05-10 15:59:53 +0000
- Working tree na coleta: sujo por arquivo não rastreado em `00_core/`; não foi alterado.

Últimos commits relevantes:

- `63530a8` `docs(procedures): exigir protocolo prepare handoff no handoff principal do dia`
- `10a37c0` `docs(project): preparar handoff de sessao`
- `da6cdfa` `feat(procedures): cria procedimento-preparar-handoff (proposta)`
- `2e10432` `fix(core): atualiza referencia context brief no system-prompt (2026-05-06 → 2026-05-10)`
- `da00dbf` `docs(project): retomada Cowork — atualiza HEAD em status/context-brief, commita handoff Saara, registra H0.z`
- `143a3d9` `docs(project): gerar pacote manual-first (status/context/handoff/guia instancias)`
- `1d875e3` `docs(project): alinhar roadmap e core à separação project vs runtime`
- `9c76d62` `docs(project): atualizar context brief + status-project para nova estrutura`
- `f8b5120` `chore(structure): separar project-memories e status-project; mover roadmap para project`
- `538b441` `feat(p0.1.32): revisao integrada configuracao-base Maui — correcoes A1 B1-B5 C1 + exec-report + memoria marco`

## 3) Estado confirmado por evidência

- Último lote normativo comprovado: P0.1.32, com evidência em `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` e commit `538b441`.
- Procedure de handoff existe em `vault-maui/procedures/procedimento-preparar-handoff.md`, com `status: proposta`, e foi reforçado no commit `63530a8`.
- Context brief current deste pacote: `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui-v2.md`.
- Handoff principal deste pacote: `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff-v2.md`.
- Exec-report deste pacote: `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff-v2.md`.
- Pendências/riscos: arquivo `.bak.disabled` não rastreado permanece sem ação; commit depende de Human Gate; P0.2, P0.3, P0.4 e P0.1.11 não foram executadas.

## 4) Estrutura Project vs Runtime (resumo)

- `vault-maui/project-memories/` = memória de gestação/projeto.
- `vault-maui/memorias/` = memória operacional de runtime, reservada.
- `vault-maui/status-project/` = status vivo do projeto.
- `vault-maui/status/` = status operacional de runtime, reservada.
- Roadmap atual: `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.
- Painel: `vault-maui/panel/status.md` é indexador baixo-trust.

## 5) Próximo passo recomendado (sem executar)

- Revisar o Human Gate do pacote v2 e decidir se deve haver commit único com a mensagem padronizada.
- Confirmar decisão sobre o arquivo não rastreado `vault-maui/00_core/system-prompt-maui.md.bak.disabled`; por padrão, ele não deve entrar no commit.
- Não executar P0.2, P0.3, P0.4, P0.1.11 ou qualquer etapa do roadmap por inferência.

## 6) Referências lidas (paths)

- `vault-maui/procedures/procedimento-preparar-handoff.md`
- `vault-maui/status-project/STATUS-UPDATE-maui.md`
- `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`
- `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
