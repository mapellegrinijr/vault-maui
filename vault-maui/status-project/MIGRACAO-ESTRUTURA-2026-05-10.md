# Migração de Estrutura — 2026-05-10

- Gerado em: 2026-05-10T03:28:25-03:00
- Escopo: separar memória/status de projeto vs runtime e mover roadmap para camada Project.
- HEAD inicial: `d3e5e8ebbe8bb1f08efaf7f84104fcc567b7eb0a`
- Working tree inicial: sujo apenas por `?? vault-maui/status/` antes desta migração.

## Moves

| Origem | Destino |
|---|---|
| `vault-maui` + `memorias/2026-05-05-marco-decisao-normalizacao-estrutural.md` | `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md` |
| `vault-maui` + `memorias/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md` | `vault-maui/project-memories/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md` |
| `vault-maui` + `memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` | `vault-maui/project-memories/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` |
| `vault-maui` + `memorias/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md` | `vault-maui/project-memories/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md` |
| `vault-maui` + `memorias/2026-05-06-decisao-claude-code-gerar-context-brief.md` | `vault-maui/project-memories/2026-05-06-decisao-claude-code-gerar-context-brief.md` |
| `vault-maui` + `memorias/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md` | `vault-maui/project-memories/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md` |
| `vault-maui` + `memorias/2026-05-06-marco-encerramento-sessao-configuracao-base-maui.md` | `vault-maui/project-memories/2026-05-06-marco-encerramento-sessao-configuracao-base-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-handoff-saara-7-1-1-pe-claude-maui.md` | `vault-maui/project-memories/2026-05-06-marco-handoff-saara-7-1-1-pe-claude-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-p0-1-26-principios-precedencia-maui.md` | `vault-maui/project-memories/2026-05-06-marco-p0-1-26-principios-precedencia-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-p0-1-27-especificacao-completa-maui.md` | `vault-maui/project-memories/2026-05-06-marco-p0-1-27-especificacao-completa-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-p0-1-28-system-prompt-maui.md` | `vault-maui/project-memories/2026-05-06-marco-p0-1-28-system-prompt-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` | `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` |
| `vault-maui` + `memorias/2026-05-06-marco-pos-p0-1-25-configuracao-base-maui.md` | `vault-maui/project-memories/2026-05-06-marco-pos-p0-1-25-configuracao-base-maui.md` |
| `vault-maui` + `status/STATUS-UPDATE-maui.md` | `vault-maui/status-project/STATUS-UPDATE-maui.md` |
| `vault-maui` + `status/LISTA-PASTAS-E-ARQUIVOS-maui.md` | `vault-maui/status-project/LISTA-PASTAS-E-ARQUIVOS-maui.md` |
| `vault-maui` + `00_core` / `roadmap-desenvolvimento-maui-v1-0.md` | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` |

## READMEs Criados

| Path | Finalidade |
|---|---|
| `vault-maui` + `memorias/README.md` | reserva `memorias/` para memória operacional de runtime |
| `vault-maui/status/README.md` | reserva `status/` para status operacional de runtime |
| `vault-maui/project-memories/README.md` | documenta memórias de projeto |
| `vault-maui/status-project/README.md` | documenta status vivo do projeto |

## Arquivos Não Encontrados

Nenhum dos arquivos obrigatórios estava ausente. Observação: o relatório de lista de pastas e arquivos que estava em `status/` não estava listado explicitamente na tarefa, mas foi movido para `status-project/` para cumprir a regra de deixar `status/` vazio exceto README.

## Referências

| Path antigo | Ocorrências antes | Ocorrências depois | Path novo |
|---|---:|---:|---|
| antigo `vault-maui` + `memorias/` | 243 | 0 | `vault-maui/project-memories/` |
| antigo `vault-maui` + `status/STATUS-UPDATE-maui.md` | 3 | 0 | `vault-maui/status-project/STATUS-UPDATE-maui.md` |
| antigo `vault-maui` + `00_core` / `roadmap-desenvolvimento-maui-v1-0.md` | 54 | 0 | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` |
| antigo `00_core` / `roadmap-desenvolvimento-maui-v1-0.md` | 54 | 0 | `project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` quando sem prefixo `vault-maui/` |

## Validação

- `find vault-maui/memorias -type f | sort` retorna apenas o README desse diretório.
- `find vault-maui/status -type f | sort` retorna apenas `vault-maui/status/README.md`.
- Greps finais para os paths antigos obrigatórios retornaram zero ocorrências.

## Notas

- P0.2/P0.3/P0.4 não foram executados.
- Status de normativos não foi promovido.
- Arquivos normativos em `00_core/` e `01_manifest/` foram alterados somente por substituição de paths/referências literais quebrados pelos moves.
- Registros históricos, exec-reports, handoffs, inventários e context packages também tiveram paths literais atualizados para evitar links quebrados.
