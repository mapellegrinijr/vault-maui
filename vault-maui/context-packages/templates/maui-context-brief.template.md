---
titulo: "Maui Context Brief"
versao: "1.0"
status: template
data_criacao: 2026-05-05
idioma: pt-BR
tipo: context_brief_template
escopo: projeto_maui
---

# Maui Context Brief

## 1. Finalidade

Descrever o objetivo deste context brief e a tarefa, retomada ou continuidade que ele deve viabilizar.

## 2. Estado atual conhecido

Registrar apenas o estado verificável do projeto Maui necessário para continuar a tarefa.

- Estado:
- Evidências:
- Limites do que foi confirmado:

## 3. Fonte de status corrente

Status corrente do projeto:

- Fonte principal: `vault-maui/status-project/STATUS-UPDATE-maui.md`
- Data/hash verificados:
- Observações:

Não usar `vault-maui/panel/status.md` como fonte de estado; o painel é indexador de baixa confiança.

## 4. Pacote mínimo de leitura

Listar o pacote mínimo para retomada, com prioridade 1-8.

| Prioridade | Fonte | Caminho ou referência | Motivo |
| --- | --- | --- | --- |
| 1 | Git/filesystem | `git status --short`; `git log --oneline -20` | Confirmar HEAD e working tree |
| 2 | Context brief atual | `vault-maui/context-packages/current/<context-brief-atual>.md` | Retomada de contexto |
| 3 | Status do projeto | `vault-maui/status-project/STATUS-UPDATE-maui.md` | Estado vivo auditável |
| 4 | Handoff mais recente | `vault-maui/handoffs/<handoff-relevante>.md` | Transição e decisões humanas |
| 5 | Exec-report recente relevante | `vault-maui/exec-reports/submitted/<exec-report-relevante>.md` | Evidência primária de execução |
| 6 | Project memories relevantes | `vault-maui/project-memories/` | Histórico da gestação/projeto |
| 7 | Contrato do corpus | `vault-maui/00_core/` + `vault-maui/01_manifest/` | Normativos e manifest executável |
| 8 | Roadmap Project | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | Mapa de destino; não prova execução |

## 5. Fontes consultadas

Listar os documentos, handoffs, exec-reports, inventários, memórias ou artefatos consultados.

| Fonte | Caminho ou referência | Motivo da consulta | Observação |
| --- | --- | --- | --- |
|  |  |  |  |

## 6. Decisões fechadas relevantes

Registrar somente decisões já fechadas e rastreáveis que afetem a continuidade.

- Decisão:
- Fonte:
- Impacto:

## 7. Pendências e bloqueios

Listar pendências, lacunas documentais, bloqueios técnicos ou decisões ainda abertas.

- Pendência ou bloqueio:
- Impacto:
- Menor ação necessária:

## 8. Handoffs relevantes

Apontar handoffs que devem ser considerados pelo próximo executor.

| Handoff | Relevância | Status de uso |
| --- | --- | --- |
|  |  |  |

## 9. Memórias relevantes

Listar memórias de projeto que sejam materialmente necessárias para a continuidade.

Ao criar um Context Brief, consultar memórias relevantes em `vault-maui/project-memories/` e priorizar memórias com `deve_ser_considerado_em_context_brief: true` quando o escopo, tags ou tarefa relacionada forem compatíveis. Essas memórias não devem ser copiadas integralmente por padrão; devem ser sintetizadas nas seções de decisões, pendências, riscos e próximo passo.

`vault-maui/memorias/` é reservado para memória operacional de runtime e não deve ser usado como fonte de Project antes do Maui operar.

- Memória:
- Aplicação:
- Fonte:

## 10. Adendos e insights aplicáveis

Registrar adendos, insights ou observações aplicáveis à tarefa atual, sem transformar hipótese em decisão.

- Item:
- Aplicação:
- Grau de confiança:

## 11. Atualizações recentes do corpus

Registrar mudanças recentes no corpus documental que possam alterar a leitura da tarefa.

- Atualização:
- Arquivo ou área afetada:
- Impacto esperado:

## 12. Documentos necessários para continuar

Listar o conjunto mínimo de documentos necessário para o próximo executor continuar com segurança.

| Documento | Necessidade | Obrigatório para continuar? |
| --- | --- | --- |
|  |  |  |

## 13. Solicitação ao usuário quando houver lacuna documental

Se faltar documento essencial, declarar a lacuna, explicar o impacto e pedir ao usuário o menor conjunto de documentos ou anexos necessário.

- Lacuna documental:
- Impacto na continuidade:
- Menor conjunto solicitado ao usuário:

## 14. Contexto mínimo para o próximo executor

Sintetizar o contexto mínimo necessário para execução imediata, separando fatos confirmados de hipóteses.

- Fatos confirmados:
- Hipóteses ou inferências:
- O que não deve ser assumido:

## 15. O que não assumir

- Não assumir estado pelo painel; confirmar por Git, status-project, exec-reports e handoffs.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` como fontes de Project antes do runtime Maui operar.
- Não tratar roadmap como evidência de execução.
- Não executar P0.2/P0.3/P0.4 ou qualquer etapa do roadmap durante a geração do brief.
- Não copiar textos longos das fontes; sintetizar o que for material.

## 16. Riscos de continuidade

Registrar riscos de continuação sem contexto suficiente ou com contexto possivelmente obsoleto.

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
|  |  |  |  |

## 17. Próximo passo recomendado

Indicar a próxima ação recomendada, com pré-condições e validações mínimas.

- Próximo passo:
- Pré-condições:
- Validações mínimas:

## Regras obrigatórias de preenchimento

- Se faltar documento essencial, declarar a lacuna, explicar o impacto e pedir ao usuário o menor conjunto de documentos/anexos necessário.
- Não inventar conteúdo, status, versões, hashes ou decisões ausentes.
- Carregar apenas contexto materialmente necessário, respeitando o princípio de Context Injection Sob Demanda.
- O Context Brief é artefato de Project; runtime folders são reservados para operação futura.
