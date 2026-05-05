---
titulo: "Exec Report — P0.1.18 — Normalização de memórias"
versao: "1.0"
status: submitted
data_criacao: 2026-05-05
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
fase: P0.1.18
---

# Exec Report — P0.1.18 — Normalização de memórias

## Objetivo

Executar o Lote 1 da normalização estrutural do vault Maui, adotando `vault-maui/memorias/` como diretório canônico de memórias.

## Decisão humana aplicada

O usuário aprovou explicitamente `vault-maui/memorias/` como diretório canônico, porque este diretório já contém as memórias recentes usadas para continuidade e Context Brief.

## Estado inicial do working tree

O working tree inicial estava limpo após a execução da P0.1.18-pre no commit `1e12c08e544180cc16f0daa1417984e12c4a65a6`.

## Diretório canônico escolhido

`vault-maui/memorias/`.

## Estado de `vault-maui/memoria/`

`vault-maui/memoria/` existia no início da tarefa e estava vazio. O diretório vazio foi removido localmente; como Git não rastreia diretórios vazios, essa remoção não gera alteração rastreável.

## Estado de `vault-maui/memorias/`

`vault-maui/memorias/` existe e contém memórias marcadas com `deve_ser_considerado_em_context_brief: true`:

- `vault-maui/memorias/2026-05-05-marco-decisao-normalizacao-estrutural.md`
- `vault-maui/memorias/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md`
- `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`

Nenhum arquivo de memória foi apagado, movido ou reescrito.

## Referências encontradas e classificação

- Operacional futura atualizada: template `vault-maui/context-packages/templates/maui-context-brief.template.md`.
- Operacional já compatível: `vault-maui/00_core/regras-operacionais.md`, que já menciona `vault-maui/memorias/` ou pasta equivalente de memórias.
- Histórica ou diagnóstica preservada: inventário P0.1.17, exec-reports P0.1.16/P0.1.17, context brief P0.1.17, handoffs e memórias que registram a ambiguidade `memoria/` vs `memorias/`.
- Conceitual ou fora do escopo mínimo preservada: documentos core promovidos e arquivos arquivados que citam `memoria/` como estrutura planejada ou histórica.

## Referências atualizadas

O template canônico de Context Brief foi atualizado para orientar consulta explícita a `vault-maui/memorias/` e priorização de memórias com `deve_ser_considerado_em_context_brief: true`.

## Referências históricas preservadas

Registros históricos, diagnósticos e handoffs antigos foram preservados sem edição para manter rastreabilidade das decisões e do diagnóstico da divergência.

## Template Context Brief atualizado ou confirmado

Atualizado em `vault-maui/context-packages/templates/maui-context-brief.template.md`.

## Registro de normalização criado

Criado `vault-maui/inventarios/2026-05-05-normalizacao-memorias.md`.

## Arquivos alterados/criados

- Alterado: `vault-maui/context-packages/templates/maui-context-brief.template.md`
- Criado: `vault-maui/inventarios/2026-05-05-normalizacao-memorias.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-05-p0-1-18-normalizacao-memorias.md`

## Validações realizadas

- `git status --short` inicial confirmou working tree limpo.
- Confirmada a existência de `vault-maui/memorias/`.
- Confirmada a existência do template canônico de Context Brief.
- Confirmada a existência do inventário diagnóstico P0.1.17.
- Confirmada a existência das memórias esperadas em `vault-maui/memorias/`.
- Confirmado que `vault-maui/memoria/` existia e estava vazio antes da remoção local.
- Confirmado que memórias em `vault-maui/memorias/` têm `deve_ser_considerado_em_context_brief: true`.
- Confirmado que o template aponta para `vault-maui/memorias/`.

## Confirmações

- Nenhum arquivo de memória foi apagado.
- `Documentação/` não foi alterada.
- P0.1.11 não foi executada.
- Nenhuma normalização adicional de documentos core, arquivos arquivados ou registros históricos foi aplicada.

## Resultado

Aceito para revisão.

## Ressalvas

- A remoção do diretório vazio `vault-maui/memoria/` não aparece no commit porque diretórios vazios não são rastreados pelo Git.
- Referências históricas e conceituais a `memoria/` foram preservadas e devem ser tratadas, se necessário, no Lote 2 — Referências e wikilinks ou em lote dedicado de reconciliação documental.

## Próximo passo recomendado

Prosseguir para Lote 2 — Referências e wikilinks, somente após revisão humana do resultado da P0.1.18.
