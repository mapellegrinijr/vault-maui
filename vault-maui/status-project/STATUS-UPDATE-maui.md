# Status Update — Projeto Maui (Project)

- Gerado em: 2026-05-10T12:50:00-03:00
- HEAD: `da6cdfab7d7163db8c1fdd87396fc04f704acec4` — 2026-05-10 15:46:39 +0000 — `feat(procedures): cria procedimento-preparar-handoff (proposta)`
- Working tree: sujo — coleta inicial registrou `vault-maui/00_core/system-prompt-maui.md.bak.disabled` não rastreado; esta preparação de handoff também deixa artefatos documentais pendentes até Human Gate/commit.

## 1) TL;DR (5 bullets)

- HEAD atual é `da6cdfa`, com o procedure `vault-maui/procedures/procedimento-preparar-handoff.md` criado em `status: proposta`.
- Configuração-base Maui segue concluída por evidência de P0.1.32: exec-report `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco e commit `538b441`.
- Pacote manual-first anterior foi commitado em `143a3d9`; retomada Cowork e ajuste do system prompt foram commitados em `da00dbf` e `2e10432`.
- `context-packages/current/` foi saneado nesta preparação para manter apenas o context brief current; briefs antigos foram movidos para `context-packages/archive/`.
- Próximo passo é Human Gate: revisar os artefatos deste handoff e decidir se deve haver commit único; P0.2/P0.3/P0.4 não foram executadas.

## 2) Evidência Git

- HEAD completo: `da6cdfab7d7163db8c1fdd87396fc04f704acec4`
- Data do HEAD: 2026-05-10 15:46:39 +0000
- Mensagem do HEAD: `feat(procedures): cria procedimento-preparar-handoff (proposta)`
- Working tree na coleta inicial: sujo por arquivo não rastreado:
  - `vault-maui/00_core/system-prompt-maui.md.bak.disabled`

Últimos commits:

- `da6cdfa` `feat(procedures): cria procedimento-preparar-handoff (proposta)`
- `2e10432` `fix(core): atualiza referencia context brief no system-prompt (2026-05-06 → 2026-05-10)`
- `da00dbf` `docs(project): retomada Cowork — atualiza HEAD em status/context-brief, commita handoff Saara, registra H0.z`
- `143a3d9` `docs(project): gerar pacote manual-first (status/context/handoff/guia instancias)`
- `1d875e3` `docs(project): alinhar roadmap e core à separação project vs runtime`
- `9c76d62` `docs(project): atualizar context brief + status-project para nova estrutura`
- `f8b5120` `chore(structure): separar project-memories e status-project; mover roadmap para project`
- `d3e5e8e` `context: consolida handoff pos-configuracao-base Maui`
- `538b441` `feat(p0.1.32): revisao integrada configuracao-base Maui — correcoes A1 B1-B5 C1 + exec-report + memoria marco`
- `9f2afc9` `feat(p0.1.31): cria parametrizacao executavel e indice core Maui (proposta)`
- `b8c8749` `feat(p0.1.30): cria specs subsidiárias Maui (proposta)`
- `4c06623` `feat(p0.1.29): cria PKAs Maui — PE Elite obrigatória + 5 PKAs adaptadas`
- `8d60c8e` `fix: normaliza status de regras-operacionais.md para proposta`
- `6170d82` `docs: ensina Claude Code a gerar Context Brief Maui`
- `baf02e6` `handoff: prepara continuidade Saara 7.1.1 PE Claude Maui`
- `4493448` `p0.1.28: cria system prompt Maui`
- `221d481` `p0.1.27: cria especificacao completa Maui`
- `1f32776` `p0.1.26: define principios e precedencia Maui`
- `10978c1` `p0.1.25-post: consolida memoria e context brief`
- `5cbdceb` `p0.1.25: planeja implementacao da configuracao-base Maui`

## 3) Estado confirmado por evidência

- Último lote normativo comprovado: P0.1.32, com evidência em `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` e commit `538b441`.
- Últimos lotes de governança: separação Project vs Runtime (`f8b5120`, `9c76d62`, `1d875e3`), pacote manual-first (`143a3d9`), retomada Cowork (`da00dbf`), ajuste de referência no system prompt (`2e10432`) e criação do procedure de handoff (`da6cdfa`).
- Context brief current: `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`.
- Handoff desta sessão: `vault-maui/handoffs/2026-05-10-handoff-sessao-prepare-handoff.md`.
- Exec-report desta sessão: `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-handoff-prepare-handoff.md`.
- Pendências/riscos: arquivo `.bak.disabled` não rastreado; commit deste pacote ainda depende de Human Gate; P0.2, P0.3 e P0.4 permanecem sem execução nesta sessão.

## 4) Estrutura Project vs Runtime (resumo)

- `vault-maui/project-memories/` = memória de gestação/projeto.
- `vault-maui/memorias/` = memória operacional de runtime, reservada.
- `vault-maui/status-project/` = status vivo do projeto.
- `vault-maui/status/` = status operacional de runtime, reservado.
- Roadmap atual: `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.
- Painel: `vault-maui/panel/status.md` é indexador baixo-trust.

## 5) Próximo passo recomendado (sem executar)

- Revisar o Human Gate deste pacote de handoff e decidir se os artefatos devem ser commitados.
- Depois do commit, escolher explicitamente entre P0.2 e P0.3 se o objetivo for avançar roadmap.
- Não executar P0.2, P0.3, P0.4 ou qualquer lote por inferência.

## 6) Referências lidas (paths)

- `vault-maui/procedures/procedimento-preparar-handoff.md`
- `vault-maui/status-project/STATUS-UPDATE-maui.md`
- `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`
- `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md`
- `vault-maui/handoffs/2026-05-10-handoff-sessao-retomada-cowork.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
