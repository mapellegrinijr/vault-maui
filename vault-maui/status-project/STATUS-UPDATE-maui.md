# Status Update — Projeto Maui (Project)

- Gerado em: 2026-05-10T15:20:00-03:00
- HEAD: `143a3d9aae539f783c66668b2d31226106a1a971` — 2026-05-10 03:57:48 -0300 — `docs(project): gerar pacote manual-first (status/context/handoff/guia instancias)`
- Working tree: sujo — arquivo não commitado: `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md`

## 1) TL;DR (5 bullets)

- Configuração-base Maui está concluída por evidência de P0.1.32: `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco e commit `538b441`.
- Reorg Project vs Runtime aplicada por `f8b5120`/`9c76d62`/`1d875e3`; pacote manual-first gerado e commitado em `143a3d9`.
- `vault-maui/memorias/` e `vault-maui/status/` permanecem reservados para runtime (apenas README); não usar em contexto de Project.
- Há um handoff não commitado (`2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md`) gerado por sessão Saara pós-pacote; deve ser commitado com os artefatos desta sessão.
- Próxima decisão humana: escolher P0.2 ou P0.3; nenhuma etapa do roadmap foi executada por inferência neste pacote.

## 2) Evidência Git

- HEAD completo: `143a3d9aae539f783c66668b2d31226106a1a971`
- Data do HEAD: 2026-05-10 03:57:48 -0300
- Mensagem do HEAD: `docs(project): gerar pacote manual-first (status/context/handoff/guia instancias)`
- Working tree na coleta: **sujo** — arquivo não rastreado:
  - `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md`

Últimos commits (20):

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
- `322b9af` `p0.1.24: diagnostica configuracao-base Maui`
- `7e43dbd` `p0.1.24-pre: planeja configuracao-base Maui`
- `8804664` `p0.1.23: corrige memoria defasada pos-roadmap`

## 3) Estado confirmado por evidência

- Último lote normativo comprovado: P0.1.32, revisão integrada da configuração-base, com evidência em `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` e commit `538b441`.
- Últimos lotes de governança estrutural: separação Project vs Runtime (`f8b5120`), atualização de context brief/status-project (`9c76d62`), alinhamento de roadmap/core (`1d875e3`) e geração do pacote manual-first (`143a3d9`).
- Handoffs da sessão 2026-05-10: `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md` (commitado em `143a3d9`) e `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md` (não commitado — pendente).
- Context brief current: `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`.
- Exec-report do pacote: `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md`.
- Decisões humanas recentes: separar Project vs Runtime; `status-project/` como fonte viva; `memorias/` e `status/` reservados; atualização de instâncias é manual-first; geração de pacote manual-first aprovada.
- Pendências/riscos: handoff não commitado; P0.2, P0.3 e P0.4 não executadas; painel é baixo-trust; documentos históricos devem ser lidos como evidência temporal.

## 4) Estrutura Project vs Runtime (resumo)

- `vault-maui/project-memories/` = memória de gestação/projeto; pode congelar ao final da implementação.
- `vault-maui/memorias/` = memória operacional de runtime; reservado — não usar antes do Maui operar.
- `vault-maui/status-project/` = status vivo do projeto; usar para retomada e auditoria rápida.
- `vault-maui/status/` = status operacional de runtime; reservado — não usar antes do Maui operar.
- Roadmap atual: `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.
- Painel: `vault-maui/panel/status.md` é apenas indexador baixo-trust; não deve declarar estado por si mesmo.

## 5) Próximo passo recomendado (sem executar)

- **Pendência imediata**: commitar o handoff pendente `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md` junto com os artefatos desta sessão de retomada.
- **Opção A**: P0.2 (scripts/validations). Pré-requisitos: decisão humana explícita, leitura deste status + context brief current + roadmap. Risco: transformar documentação em automação antes de revisar limites de escrita.
- **Opção B**: P0.3 (operator packs). Pré-requisitos: decisão humana explícita, confirmação do escopo manual-first ou mudança deliberada para pacote por ferramenta. Risco: gerar instruções operacionais antes de estabilizar validações P0.2.

## 6) Referências lidas (paths)

- `vault-maui/status-project/STATUS-UPDATE-maui.md` (versão de 03:54 de 2026-05-10)
- `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`
- `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md`
- `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md` (não commitado)
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-alinha-roadmap-e-core-apos-separacao-project-runtime.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-atualiza-procedure-context-brief-e-status-project.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/panel/status.md`
