---
titulo: "Exec Report — P0.1.20 — Normalização de frontmatter e slugs"
versao: "1.0"
status: submitted
data_criacao: 2026-05-05
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
fase: P0.1.20
---

# Exec Report — P0.1.20 — Normalização de frontmatter e slugs

## Objetivo

Diagnosticar frontmatter e slugs operacionais no vault Maui e corrigir apenas casos atuais, inequívocos e de baixo risco.

## Decisão humana aplicada

Corrigir apenas frontmatter de arquivos operacionais atuais e slugs com destino inequívoco, preservando arquivos históricos, arquivados, diagnósticos, templates antigos, handoffs, memórias, inventários e exec-reports antigos.

## Estado inicial do working tree

O working tree inicial estava limpo.

## Escopo analisado

Foram percorridos arquivos Markdown sob `vault-maui/`, com diagnóstico de frontmatter ausente, incompleto ou inválido e diagnóstico de slugs com espaços, underscores, acentuação, versões inconsistentes, nomes duplicados aparentes e arquivos sem extensão.

## Critério de classificação

- `frontmatter_valido_completo`: preservar.
- `frontmatter_valido_incompleto`: corrigir apenas se operacional atual e inferível.
- `frontmatter_invalido`: corrigir apenas se operacional atual e inferível.
- `frontmatter_ausente`: corrigir apenas se operacional atual e inferível.
- `template_sem_frontmatter_aceitavel`: preservar.
- `historico_ou_arquivado_preservado`: preservar.

Para slugs, só haveria renomeação se o destino fosse inequívoco, operacional atual, baixo risco e sem quebra de referências.

## Frontmatter corrigido

- `vault-maui/panel/status.md`: adicionado frontmatter válido para painel operacional atual.

## Frontmatter preservado ou pendente

- `vault-maui/context-packages/templates/maui-context-brief.template.md`: preservado, pois já tinha frontmatter completo aprovado anteriormente.
- READMEs e índices auxiliares sem frontmatter: preservados como pendência por falta de política específica.
- Exec-reports antigos sem frontmatter: preservados como histórico.
- Templates antigos de exec-report/review-report/exec-request sem frontmatter: preservados para lote próprio, se aprovado.
- Arquivos arquivados sem frontmatter: preservados por regra da tarefa.

## Slugs corrigidos

Nenhum slug foi corrigido nesta tarefa.

## Slugs preservados ou pendentes

Não foram encontrados arquivos Markdown operacionais atuais com espaços, underscores, acentuação, versão `v_0_1`/`v0.1` ou sem extensão. Arquivos históricos e arquivados foram preservados.

## Arquivos alterados/criados

- Alterado: `vault-maui/panel/status.md`
- Criado: `vault-maui/inventarios/2026-05-05-normalizacao-frontmatter-slugs.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-05-p0-1-20-normalizacao-frontmatter-slugs.md`

## Validações realizadas

- `git status --short` inicial confirmou working tree limpo.
- Confirmada a existência dos registros P0.1.17, P0.1.18 e P0.1.19.
- Confirmada a existência dos documentos core atuais.
- Confirmada a existência do template canônico de Context Brief.
- Confirmada a existência de `vault-maui/project-memories/`.
- Validado YAML dos arquivos alterados/criados.
- Confirmado que nenhum slug foi renomeado.

## Confirmações

- `Documentação/` não foi alterada.
- P0.1.11 não foi executada.
- Nenhum arquivo histórico ou arquivado foi renomeado.
- Nenhum exec-report, inventário, handoff ou memória existente foi reescrito fora do registro e exec-report novos desta tarefa.
- Nenhuma pendência não relacionada foi incluída.

## Resultado

Aceito para revisão.

## Ressalvas

- READMEs, índices auxiliares e templates antigos permanecem sem frontmatter até decisão específica.
- Exec-reports antigos sem frontmatter foram preservados para manter rastreabilidade histórica.
- A P0.1.20 não fez renomeações de slugs.

## Próximo passo recomendado

Prosseguir para Lote 4 — Context Brief readiness, somente após revisão humana do resultado da P0.1.20.
