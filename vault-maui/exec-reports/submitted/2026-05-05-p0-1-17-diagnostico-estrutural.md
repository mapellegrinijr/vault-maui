---
titulo: "Exec Report — P0.1.17 — Diagnóstico estrutural do vault Maui"
versao: "1.0"
status: submitted
data_criacao: 2026-05-05
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
fase: P0.1.17
---

## Objetivo

Executar diagnóstico estrutural do `vault-maui/`, identificando divergências de estrutura antes de qualquer correção.

## Decisão humana aplicada

O usuário aprovou tratar P0.1.17 como diagnóstico estrutural completo do vault Maui, sem corrigir, mover, renomear, apagar ou reescrever arquivos existentes.

## Escopo analisado

- Diretórios de primeiro e segundo nível sob `vault-maui/`.
- Diretórios `vault-maui/memoria/` e `vault-maui/memorias/`.
- Documentos core em `vault-maui/00_core/`.
- Arquivos Markdown sob `vault-maui/` para diagnóstico de frontmatter.
- Referências e wikilinks selecionados no corpus.
- Context Brief template e Context Brief atual.
- Readiness para instanciação manual.

## Divergências estruturais encontradas

- `vault-maui/memoria/` e `vault-maui/memorias/` coexistem.
- `vault-maui/review-reports/` não existe.
- `vault-maui/operator-packs/` contém subdiretórios por target, mas nenhum arquivo de pack/template.
- Handoffs aparecem entre `context-packages/current`, `context-packages/archive` e `vault-maui/handoffs/`, com mudanças pendentes já existentes antes desta tarefa.
- Muitos diretórios de capacidades futuras estão vazios: `scripts/`, `procedures/`, `skills/`, `hooks/`, `evals/`, `exports/`.

## Diagnóstico específico de `memoria/` vs `memorias/`

- `vault-maui/memoria/` existe e está vazio.
- `vault-maui/memorias/` existe e contém duas memórias com `deve_ser_considerado_em_context_brief: true`.
- Uma memória em `vault-maui/memorias/` já estava não rastreada antes desta tarefa: `2026-05-05-marco-decisao-normalizacao-estrutural.md`.
- Documentos core citam principalmente `memoria/`.
- Regras operacionais e artefatos recentes citam `memorias/` ou pasta equivalente.

## Diagnóstico de frontmatter

- Não foram detectados frontmatters YAML inválidos nos arquivos Markdown com bloco `---`.
- Foram detectados vários arquivos sem frontmatter, incluindo READMEs, templates, reports antigos e alguns arquivos arquivados.
- Nos arquivos com frontmatter válido, os campos mínimos diagnósticos estavam presentes.
- `status: current` aparece no Context Brief instanciado, plausível mas ainda dependente de convenção futura.

## Diagnóstico de referências/wikilinks

- Referências históricas a `Documentação/` permanecem em inventário, memórias e exec-reports, como esperado.
- `[[...]]`, `[[link]]` e `[[wikilink]]` aparecem como placeholders históricos no inventário e como exemplos funcionais em documentos core.
- Referências a nomes antigos com underscores permanecem em contexto histórico.
- Referências a `context-packages/current/maui-bootstrap.md` aparecem em documentos core, mas esse bootstrap não foi encontrado.

## Diagnóstico de Context Brief

- O template canônico existe.
- O template prioriza memórias com `deve_ser_considerado_em_context_brief: true`.
- Existe Context Brief instanciado para P0.1.17.
- Lacunas: diretório canônico de memórias indefinido, handoffs em múltiplos locais, ausência de `review-reports/`, ausência de índice/script de busca de memórias.

## Diagnóstico de readiness para instanciação manual

Classificação: experimental.

Justificativa:

- Core documental existe.
- Regras operacionais existem.
- `system-prompt.md` não existe.
- PKAs herdadas não existem em `00_core/`.
- Operator packs estão vazios.
- Não foi encontrado bootstrap `maui-bootstrap.md`.
- Não há registry materializado de instâncias.

## Lotes futuros propostos

1. Lote 1 — Memórias: normalizar ou compatibilizar `memoria/` vs `memorias/`.
2. Lote 2 — Referências e wikilinks: revisar placeholders e referências obsoletas.
3. Lote 3 — Frontmatter e slugs: normalizar campos mínimos, status, tipo e nomes.
4. Lote 4 — Context Brief readiness: garantir descoberta de memórias, handoffs, exec-reports, insights e atualizações.
5. Lote 5 — Instanciação manual Maui: consolidar system prompt, PKAs, operator packs e context package bootstrap.

## Recomendação do executor

Executar primeiro o Lote 1 — Memórias, com decisão humana explícita sobre o caminho canônico antes de qualquer movimentação.

## Arquivos criados

- `vault-maui/inventarios/2026-05-05-diagnostico-estrutural-vault-maui.md`
- `vault-maui/exec-reports/submitted/2026-05-05-p0-1-17-diagnostico-estrutural.md`

## Validações realizadas

- Registrado `git status --short` inicial, que já continha alterações pendentes não relacionadas.
- Confirmada a existência de `vault-maui/`, `vault-maui/00_core/`, inventário de `Documentação/` e template de Context Brief.
- Confirmada a existência de `vault-maui/memoria/` e `vault-maui/memorias/`.
- Confirmada a existência/ausência dos diretórios estruturais solicitados.
- Confirmado que `Documentação/` não contém os 8 arquivos originalmente inventariados.
- Percorridos arquivos Markdown sob `vault-maui/` para diagnóstico de frontmatter.
- Buscadas referências e wikilinks solicitados.
- Confirmado que `git log --grep='p0.1.11'` não retorna commit.

## Confirmações de não alteração

- Nenhum arquivo existente foi movido, apagado, renomeado ou reescrito nesta tarefa.
- Nenhuma normalização foi aplicada.
- Nenhum arquivo em `vault-maui/memoria/` foi alterado.
- Nenhum arquivo em `vault-maui/memorias/` foi alterado.
- `Documentação/` não foi alterada.
- P0.1.11 não foi executada.

## Resultado

Aceito para revisão.

## Ressalvas

O working tree já estava sujo no início da tarefa, com alterações não relacionadas: remoção pendente em `vault-maui/context-packages/current/`, arquivos não rastreados em `vault-maui/handoffs/`, memória não rastreada em `vault-maui/memorias/` e `Sem título.canvas` na raiz. Esses itens foram diagnosticados quando relevantes, mas não foram alterados nem incluídos no commit desta tarefa.

## Próximo passo recomendado

Aprovar o Lote 1 — Memórias, definindo o caminho canônico entre `vault-maui/memoria/` e `vault-maui/memorias/`.
