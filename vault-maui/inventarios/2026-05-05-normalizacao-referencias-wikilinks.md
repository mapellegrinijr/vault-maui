---
titulo: "Registro de normalização — referências e wikilinks Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: registro_normalizacao
escopo: projeto_maui
fase: P0.1.19
---

# Registro de normalização — referências e wikilinks Maui

## 1. Decisão

A P0.1.19 corrigiu apenas referências operacionais atuais/futuras com destino inequívoco e preservou registros históricos, diagnósticos e ambíguos.

## 2. Critério de classificação

- Operacional atual/futura: referência em documento vivo, painel operacional ou orientação futura que aponta para caminho obsoleto com destino canônico conhecido.
- Histórica/diagnóstica: referência que registra estado passado, execução, diagnóstico, handoff ou inventário; preservada para rastreabilidade.
- Exemplo/template: referência usada como exemplo de formato ou comportamento; corrigida apenas quando o destino canônico é inequívoco.
- Placeholder: wikilink ou marcador genérico sem destino real conhecido; preservado e registrado.
- Ambígua: referência que pode ser histórica, conceitual ou futura, mas não tem destino seguro; preservada e registrada.

## 3. Referências corrigidas

| Arquivo | Ocorrência anterior | Ocorrência nova | Justificativa |
| --- | --- | --- | --- |
| `vault-maui/panel/status.md` | `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md` | `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md` | O handoff foi reorganizado para `vault-maui/handoffs/` na P0.1.18-pre e o caminho antigo não existe mais. |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | `memoria/`, `memoria/**/*.md`, `memoria/YYYY-MM/*.md` | `memorias/`, `memorias/**/*.md`, `memorias/YYYY-MM/*.md` | P0.1.18 adotou `vault-maui/project-memories/` como diretório canônico de memórias. |
| `vault-maui/00_core/arquitetura-maui-v0-2.md` | `memoria/`, `memoria/YYYY/MM/YYYY-MM-DD-decisao-adocao-piloto-maui.md` | `memorias/`, `memorias/YYYY/MM/YYYY-MM-DD-decisao-adocao-piloto-maui.md` | Documento core atual; referência operacional ao diretório singular estava obsoleta. |
| `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | `memoria/`, `memoria/templates/decisao-template.md`, `memoria/YYYY/MM/...`, `memoria/README.md` | `memorias/`, `memorias/templates/decisao-template.md`, `memorias/YYYY/MM/...`, `memorias/README.md` | Roadmap core atual; exemplos operacionais de memória devem usar o diretório canônico. |
| `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | `memoria/`, `memoria/YYYY/MM/...` | `memorias/`, `memorias/YYYY/MM/...` | Spec funcional core atual; referências operacionais de busca e estrutura de memória foram alinhadas ao diretório canônico. |

## 4. Referências preservadas

| Arquivo | Ocorrência | Motivo da preservação |
| --- | --- | --- |
| `vault-maui/inventarios/2026-05-04-documentacao.md` | referências a `Documentação/` e nomes originais dos 8 arquivos | Histórica/inventário. |
| `vault-maui/inventarios/2026-05-05-diagnostico-estrutural-vault-maui.md` | `vault-maui/memoria/`, `vault-maui/project-memories/`, `Documentação/`, caminhos antigos e placeholders | Diagnóstica; registra o estado encontrado na P0.1.17. |
| `vault-maui/inventarios/2026-05-05-normalizacao-memorias.md` | `vault-maui/memoria/` | Histórica; registra decisão e remoção do diretório vazio na P0.1.18. |
| `vault-maui/exec-reports/` | caminhos antigos, `Documentação/`, `context-packages/current/` e nomes originais | Histórica; exec-reports registram o que foi executado. |
| `vault-maui/handoffs/` | caminhos antigos e decisões anteriores | Histórica; handoffs preservam contexto de transição. |
| `vault-maui/project-memories/` | divergência `memoria/` vs `memorias/` e referências a decisões anteriores | Histórica/diagnóstica; memórias preservam decisões e marcos. |
| `vault-maui/context-packages/archive/` | `memoria/`, wikilinks legados e caminhos antigos | Arquivo histórico; não foi normalizado nesta tarefa. |
| `vault-maui/context-packages/current/2026-05-05-context-brief-p0-1-17-normalizacao-memorias.md` | referências à ambiguidade `memoria/` vs `memorias/` e ao handoff antigo | Context Brief histórico da preparação da P0.1.17. |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | `[[context-packages/current]]`, `[[spec-tecnica-atualizacao-saara-maui-v1]]`, PKAs e specs herdadas em wikilinks | Ambígua; não há destino inequívoco para todos os wikilinks nesta tarefa. |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | `memoria/handoff-*.md` | Ambígua; handoffs têm normalização própria pendente e não foram tratados neste lote. |
| `vault-maui/00_core/arquitetura-maui-v0-2.md` e `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | `context-packages/current/maui-bootstrap.md` | Ambígua/futura; arquivo ainda não existe e não houve destino inequívoco para substituir. |

## 5. Placeholders e pendências

- `[[...]]` permanece em `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` como exemplo de funcionalidade de localização de links.
- `[[...]]` permanece em `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` como exemplo de validação de links internos.
- `[[link]]` e `[[wikilink]]` aparecem em documentos arquivados ou diagnósticos; foram preservados.
- Wikilinks de specs, PKAs, handoff legado e conceitos herdados permanecem pendentes quando não há destino inequívoco no vault atual.
- A normalização de handoffs e `context-packages/current/maui-bootstrap.md` deve ser tratada em lote próprio, se aprovada.

## 6. Impacto

- Context Brief: passa a encontrar memórias pelo diretório canônico já definido em P0.1.18.
- Documentos core: referências operacionais ao diretório de memórias foram alinhadas a `vault-maui/project-memories/`.
- Rastreabilidade histórica: inventários, exec-reports, handoffs, memórias e arquivos arquivados preservam o estado antigo.
- Próximos lotes: permanecem pendentes wikilinks sem destino inequívoco, referências conceituais herdadas e normalização de handoffs/bootstrap.

## 7. Próximo passo recomendado

Prosseguir para Lote 3 — Frontmatter e slugs, somente após revisão humana do resultado da P0.1.19.
