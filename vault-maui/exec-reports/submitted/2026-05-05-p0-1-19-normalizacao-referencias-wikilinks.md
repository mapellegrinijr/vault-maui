---
titulo: "Exec Report — P0.1.19 — Normalização de referências e wikilinks"
versao: "1.0"
status: submitted
data_criacao: 2026-05-05
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
fase: P0.1.19
---

# Exec Report — P0.1.19 — Normalização de referências e wikilinks

## Objetivo

Diagnosticar e corrigir referências operacionais atuais/futuras obsoletas no vault Maui, preservando registros históricos.

## Decisão humana aplicada

Corrigir apenas referências operacionais atuais/futuras com destino inequívoco e preservar referências históricas em inventários, exec-reports, handoffs e memórias.

## Estado inicial do working tree

O working tree inicial estava limpo.

## Escopo analisado

Foram buscadas referências em arquivos Markdown/YAML/JSON/TOML/TXT sob `vault-maui/`, cobrindo caminhos de `Documentação/`, diretórios de memória, `context-packages/current`, `context-packages/archive`, nomes antigos e novos dos documentos promovidos, wikilinks e placeholders.

## Critério de classificação

- Operacional atual/futura: corrigir quando o destino canônico era inequívoco.
- Histórica/diagnóstica: preservar.
- Exemplo/template: corrigir apenas se o destino fosse inequívoco.
- Placeholder: preservar quando não havia destino inequívoco.
- Ambígua: preservar e registrar.

## Referências corrigidas

- `vault-maui/panel/status.md`: handoff atual atualizado de `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md` para `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md`.
- `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md`: referências operacionais a `memoria/` atualizadas para `memorias/`.
- `vault-maui/00_core/arquitetura-maui-v0-2.md`: referências operacionais a `memoria/` atualizadas para `memorias/`.
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`: referências operacionais a `memoria/` atualizadas para `memorias/`.
- `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md`: referências operacionais a `memoria/` atualizadas para `memorias/`.

## Referências preservadas

- Inventários, exec-reports, handoffs, memórias e context briefs históricos que registram caminhos antigos ou a ambiguidade `memoria/` vs `memorias/`.
- Arquivos em `vault-maui/context-packages/archive/`.
- Wikilinks herdados sem destino inequívoco em documentos core.
- Referências a `context-packages/current/maui-bootstrap.md`, por parecerem futuras e ainda sem arquivo de destino.
- Referência `memoria/handoff-*.md`, porque a normalização de handoffs não foi aprovada neste lote.

## Placeholders e pendências

- `[[...]]` preservado em documentos core quando usado como exemplo de funcionalidade.
- `[[link]]` e `[[wikilink]]` preservados em documentos históricos/arquivados ou diagnósticos.
- Wikilinks para PKAs, specs herdadas e handoffs legados permanecem pendentes quando não há destino inequívoco.
- Normalização de handoffs e bootstrap permanece fora do escopo desta tarefa.

## Arquivos alterados/criados

- Alterado: `vault-maui/panel/status.md`
- Alterado: `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md`
- Alterado: `vault-maui/00_core/arquitetura-maui-v0-2.md`
- Alterado: `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`
- Alterado: `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md`
- Criado: `vault-maui/inventarios/2026-05-05-normalizacao-referencias-wikilinks.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-05-p0-1-19-normalizacao-referencias-wikilinks.md`

## Validações realizadas

- `git status --short` inicial confirmou working tree limpo.
- Confirmada a existência dos inventários e template exigidos.
- Confirmada a existência de `vault-maui/memorias/`.
- Confirmada a existência dos documentos promovidos ao core.
- Confirmada a existência dos arquivos arquivados.
- Confirmado que referências corrigidas apontam para diretórios ou arquivos existentes.
- Confirmado que não foram introduzidos wikilinks novos.

## Confirmações

- `Documentação/` não foi alterada.
- P0.1.11 não foi executada.
- Registros históricos não foram alterados apenas por conterem caminhos antigos.
- Nenhuma pendência não relacionada foi incluída.

## Resultado

Aceito para revisão.

## Ressalvas

- Referências históricas e diagnósticas permanecem com caminhos antigos por design.
- Alguns wikilinks herdados continuam pendentes porque não há destino inequívoco no vault atual.
- `memoria/handoff-*.md` não foi convertido, pois handoffs exigem lote próprio de decisão canônica.

## Próximo passo recomendado

Prosseguir para Lote 3 — Frontmatter e slugs, somente após revisão humana do resultado da P0.1.19.
