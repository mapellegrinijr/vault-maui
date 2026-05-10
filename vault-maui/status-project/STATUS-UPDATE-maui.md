# Status Update — Projeto Maui (Project)

- Gerado em: 2026-05-10T03:54:42-03:00
- HEAD: `1d875e367f93645402b9eafdcba5e0f657d5a246` — 2026-05-10 03:44:04 -0300 — `docs(project): alinhar roadmap e core à separação project vs runtime`
- Working tree: limpo na coleta inicial

## 1) TL;DR (5 bullets)

- Configuração-base Maui está concluída por evidência de P0.1.32: `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco e commit `538b441`.
- Estrutura Project vs Runtime foi aplicada e alinhada por `f8b5120`, `9c76d62` e `1d875e3`: projeto usa `project-memories/`, `status-project/` e `project/roadmap/`.
- `vault-maui/memorias/` e `vault-maui/status/` permanecem reservados para runtime e não devem ser usados antes de operação runtime.
- Este pacote manual-first atualiza status, context brief, handoff, roadmap, painel, exec-report e guia manual sem depender de integrações.
- Próxima decisão humana continua sendo escolher P0.2 ou P0.3; nenhuma etapa do roadmap foi executada por inferência.

## 2) Evidência Git

- HEAD completo: `1d875e367f93645402b9eafdcba5e0f657d5a246`
- Data do HEAD: 2026-05-10 03:44:04 -0300
- Mensagem do HEAD: `docs(project): alinhar roadmap e core à separação project vs runtime`
- Status na coleta: `git status --porcelain` sem saída.

Últimos commits:

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
- `a0ee423` `p0.1.22: reconcilia roadmap Maui com estado real`

## 3) Estado confirmado por evidência

- Último lote normativo comprovado: P0.1.32, revisão integrada da configuração-base, com evidência em `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` e commit `538b441`.
- Últimos lotes de governança estrutural: separação Project vs Runtime em `f8b5120`, atualização de context brief/status-project em `9c76d62` e alinhamento de roadmap/core em `1d875e3`.
- Handoff de retomada anterior: `vault-maui/handoffs/2026-05-06-handoff-pos-configuracao-base-maui.md`.
- Context brief anterior relevante: `vault-maui/context-packages/current/2026-05-06-context-brief-pos-configuracao-base-maui.md`.
- Decisões humanas recentes registradas: separar Project vs Runtime; tratar `status-project/` como fonte viva de projeto; manter `memorias/` e `status/` reservados para runtime; gerar pacote manual-first de retomada.
- Pendências/riscos atuais: P0.2, P0.3 e P0.4 seguem não executadas neste pacote; painel é baixo-trust; documentos históricos podem conter menções antigas e devem ser lidos como evidência temporal, não como status corrente.

## 4) Estrutura Project vs Runtime (resumo)

- `vault-maui/project-memories/` = memória de gestação/projeto; pode congelar ao final da implementação.
- `vault-maui/memorias/` = memória operacional de runtime; reservado e não usado antes do Maui operar.
- `vault-maui/status-project/` = status vivo do projeto; usar para retomada e auditoria rápida.
- `vault-maui/status/` = status operacional de runtime; reservado e não usado antes do Maui operar.
- Roadmap atual: `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.
- Painel: `vault-maui/panel/status.md` é apenas indexador baixo-trust; não deve declarar estado por si mesmo.

## 5) Próximo passo recomendado (sem executar)

- Opção A: P0.2 (scripts/validations). Fazer agora se a prioridade for criar validação local e comandos de apoio após a configuração-base. Pré-requisitos: decisão humana explícita, leitura deste status, do context brief current e do roadmap. Risco: transformar documentação em automação antes de revisar limites de escrita.
- Opção B: P0.3 (operator packs). Fazer agora se a prioridade for preparar instruções iniciais de uso por ferramenta. Pré-requisitos: decisão humana explícita, confirmação do escopo manual-first ou mudança deliberada para pacote por ferramenta. Risco: gerar instruções operacionais antes de estabilizar validações P0.2.

## 6) Referências lidas (paths)

- `vault-maui/status-project/STATUS-UPDATE-maui.md` (versão anterior)
- `vault-maui/context-packages/current/2026-05-06-context-brief-pos-configuracao-base-maui.md`
- `vault-maui/handoffs/2026-05-06-handoff-pos-configuracao-base-maui.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-alinha-roadmap-e-core-apos-separacao-project-runtime.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-atualiza-procedure-context-brief-e-status-project.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/panel/status.md`
