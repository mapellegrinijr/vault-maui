---
titulo: "Readiness de Context Brief Maui — P0.1.21"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: context_brief_readiness
escopo: projeto_maui
fase: P0.1.21
confidencialidade: interna
---

# Readiness de Context Brief Maui — P0.1.21

## Finalidade

Definir como preparar retomadas confiáveis por `Maui Context Brief` no estado pós-P0.1.20-pre, usando evidências verificáveis do filesystem e sem assumir instanciação manual Maui pronta.

## Escopo

Este readiness cobre seleção e precedência de fontes para Context Briefs Maui, limites por target e critérios mínimos de prontidão documental. Não executa P0.1.11, não cria bootstrap final, não cria operator pack, não instancia Maui manualmente e não altera documentos normativos em `vault-maui/00_core/`.

## Fontes obrigatórias

| Fonte | Caminho | Uso obrigatório |
| --- | --- | --- |
| Exec-reports submetidos | `vault-maui/exec-reports/submitted/` | Evidência primária de execução, resultados, validações, ressalvas e próximos passos. |
| Inventários e registros | `vault-maui/inventarios/` | Evidência de diagnóstico, normalização aplicada, pendências preservadas e divergências estruturais. |
| Memórias canônicas | `vault-maui/project-memories/` | Memórias de continuidade; priorizar arquivos com `deve_ser_considerado_em_context_brief: true`. |
| Handoffs recentes | `vault-maui/handoffs/` | Transições entre sessões, decisões humanas e contexto operacional recente. |
| Template de Context Brief | `vault-maui/context-packages/templates/maui-context-brief.template.md` | Estrutura canônica de preenchimento. |
| Git local | `git status`, `git log`, `git show` | Confirmação de working tree, commits, hashes e ausência ou presença de etapas executadas. |

## Fontes opcionais

| Fonte | Caminho | Quando consultar |
| --- | --- | --- |
| Context briefs atuais | `vault-maui/context-packages/current/` | Quando houver brief recente relacionado à tarefa ou retomada. |
| Context packages arquivados | `vault-maui/context-packages/archive/` | Quando a tarefa envolver histórico, origem documental ou documentos arquivados. |
| Painel file-based | `vault-maui/panel/` | Quando for necessário conferir estado operacional resumido ou links de navegação. |
| Adendos | `vault-maui/adendos/` | Quando a tarefa mencionar decisão normativa, exceção ou extensão de comportamento. |
| Insights | `vault-maui/insights/` | Quando houver insights aplicáveis ao escopo. |
| Review reports | `vault-maui/review-reports/` ou `vault-maui/exec-reports/reviewed/` | Consultar se existirem; ausência deve ser registrada como lacuna, não inventada. |

## Fontes defasadas ou com ressalva

| Fonte | Ressalva | Regra de uso |
| --- | --- | --- |
| Roadmap core | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` permanece `status: proposta` e registra reconciliação apenas até P0.1.13. | Usar como mapa de destino e critérios, nunca como fonte única de status executado. |
| Memória de plano pós-normalização | `vault-maui/project-memories/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md` ainda descreve P0.1.20 como próximo passo em algumas seções. | Reconciliar com exec-report P0.1.20 e P0.1.20-pre antes de declarar estado atual. |
| Handoffs antigos | Handoffs podem refletir estado anterior ao fechamento da Tarefa 2 ou à normalização de memórias. | Usar como histórico; conferir contra exec-reports e inventários mais recentes. |
| Registros históricos e arquivados | Podem conter caminhos antigos, placeholders e wikilinks sem destino inequívoco. | Preservar como histórico e não normalizar por inferência em Context Brief. |

## Regras de seleção de contexto

1. Começar por `git status --short` e pelos exec-reports mais recentes relacionados à tarefa.
2. Confirmar no Git commits associados às fases citadas quando o brief declarar execução concluída.
3. Ler inventários e registros de normalização antes de sintetizar pendências.
4. Ler todas as memórias relevantes em `vault-maui/project-memories/` marcadas com `deve_ser_considerado_em_context_brief: true` quando escopo, tags ou fase forem compatíveis.
5. Ler handoffs recentes para decisões humanas e transições, mas reconciliar seu conteúdo com fontes posteriores.
6. Usar o roadmap core apenas para intenção, ordem macro, critérios e lacunas planejadas.
7. Separar fato, inferência e hipótese sempre que o status depender de reconciliação.
8. Declarar fontes ausentes ou não consultadas quando forem materialmente relevantes.
9. Não copiar memórias ou handoffs integralmente por padrão; sintetizar apenas o contexto necessário.
10. Não alterar `Documentação/`, `vault-maui/00_core/` ou registros históricos durante criação de Context Brief sem autorização explícita.

## Ordem de precedência operacional

1. Estado do Git local e arquivos existentes no filesystem.
2. Exec-reports recentes e seus commits.
3. Inventários e registros de normalização.
4. Memórias canônicas marcadas para Context Brief.
5. Handoffs recentes.
6. Context briefs atuais.
7. Documentos core, incluindo roadmap, como contratos, mapa de destino ou referência estrutural.
8. Arquivos arquivados, históricos, adendos e insights quando aplicáveis.

## Limites por target

### Codex ou executor com filesystem

- Pode declarar caminhos, hashes e commits somente após verificar no filesystem ou Git.
- Deve registrar working tree limpo, sujo ou desconhecido.
- Deve tratar documentos core `status: proposta` como proposta salvo evidência direta em contrário.

### Claude Code ou executor equivalente com filesystem

- Pode seguir a mesma regra de evidência local quando houver acesso ao repositório.
- P0.1.11 continua não executada; não assumir que Claude Code foi instruído a criar Context Brief sob demanda.

### ChatGPT/Handoff sem filesystem

- Não pode marcar instância ou handoff como `current` sem hash verificável.
- Deve usar `unknown` quando não houver filesystem, hash ou commit verificável.
- Deve declarar que opera por contexto fornecido e pode estar defasado.
- Deve pedir o menor conjunto de arquivos/anexos quando faltar fonte obrigatória.

## Checklist de readiness

- [x] Diretório canônico de memórias definido como `vault-maui/project-memories/`.
- [x] Template canônico de Context Brief existe.
- [x] Exec-reports P0.1.16 a P0.1.20 existem.
- [x] Inventários e registros de normalização existem.
- [x] Handoffs recentes existem em `vault-maui/handoffs/`.
- [x] Roadmap identificado como mapa de destino, não fonte única de status.
- [x] Limite `unknown` para ChatGPT/Handoff sem filesystem declarado.
- [x] P0.1.11 preservada como não executada.
- [x] Instanciação manual mantida fora do escopo.
- [ ] Review reports não têm área canônica materializada em `vault-maui/review-reports/`.
- [ ] Adendos e insights não têm itens aplicáveis identificados para P0.1.21.
- [ ] Roadmap core ainda não foi reconciliado documentalmente com P0.1.16 a P0.1.20.

## Critérios de pronto

Um `Maui Context Brief` está pronto para retomada quando:

- lista fontes consultadas e ausentes;
- usa exec-reports, inventários, memórias canônicas e handoffs antes do roadmap para status executado;
- declara roadmap como fonte estrutural/proposta;
- separa fatos, inferências e hipóteses;
- preserva `Documentação/` fora do escopo sem nova decisão humana;
- preserva P0.1.11 como não executada;
- não assume instanciação manual pronta;
- usa `unknown` para qualquer target sem filesystem/hash verificável.

## Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Roadmap defasado ser tratado como status executado | Conclusões incorretas sobre fases concluídas | Aplicar ordem de precedência e exigir exec-report/inventário/Git para conclusão. |
| Memória parcialmente defasada sobre P0.1.20 | Próximo passo antigo ser repetido | Conferir sempre P0.1.20 e P0.1.20-pre antes de declarar estado atual. |
| Handoff antigo ser usado como estado final | Reabrir pendências já fechadas | Tratar handoffs como transição e reconciliar com artefatos mais recentes. |
| ChatGPT/Handoff sem filesystem ser marcado `current` | Falsa conformidade | Usar `unknown` sem hash verificável. |
| Falta de review-reports canônico | Lacuna em revisões futuras | Registrar ausência no brief e consultar `exec-reports/reviewed/` se aplicável. |

## F/I/H

### Fatos

- `vault-maui/project-memories/` é o diretório canônico de memórias.
- P0.1.16 a P0.1.20 têm exec-reports e commits associados.
- P0.1.20-pre criou Context Brief para continuidade e recomendou P0.1.21.
- P0.1.11 não foi executada.
- Maui permanece `status: proposta` nos documentos core promovidos.
- Instanciação manual foi diagnosticada como experimental e segue fora do escopo desta tarefa.

### Inferências

- Context Briefs futuros devem considerar exec-reports e inventários mais recentes antes de handoffs e roadmap.
- A ausência de `vault-maui/review-reports/` não bloqueia P0.1.21, mas deve ser declarada quando a fonte for esperada.
- Um inventário separado para P0.1.21 não acrescenta valor real se este readiness já registrar classificação, regras e riscos.

### Hipóteses

- Adendos e insights podem se tornar obrigatórios em tarefas futuras se houver conteúdo material nesses diretórios.
- A reconciliação normativa do roadmap pode ser necessária antes de retomar fases macro do roadmap ou P0.1.5.

## Próxima ação recomendada

Revisar e aceitar este readiness. Depois, quando houver decisão humana, retomar a próxima etapa imediata sem executar P0.1.11 nem instanciação manual por inferência.
