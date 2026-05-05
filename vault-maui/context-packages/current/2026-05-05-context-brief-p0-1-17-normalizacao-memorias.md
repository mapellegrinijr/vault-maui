---
titulo: "Maui Context Brief — P0.1.17 — Normalização do diretório canônico de memórias"
versao: "1.0"
status: current
data_criacao: 2026-05-05
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
tarefa: P0.1.17
---

# Maui Context Brief — P0.1.17 — Normalização do diretório canônico de memórias

## 1. Finalidade

Preparar a P0.1.17: normalizar a decisão sobre o diretório canônico de memórias do Maui, resolvendo a ambiguidade operacional entre `vault-maui/memoria/` e `vault-maui/memorias/`.

Este brief consolida apenas o contexto mínimo necessário para o próximo executor propor e executar uma normalização controlada, sem reescrever documentos core nem inventar decisão normativa ausente.

## 2. Estado atual conhecido

- Estado: existem dois diretórios relacionados a memórias: `vault-maui/memoria/` e `vault-maui/memorias/`.
- Evidências:
  - `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` existe e contém `deve_ser_considerado_em_context_brief: true`.
  - `vault-maui/memoria/` existe, mas não contém arquivos encontrados na inspeção material desta preparação.
  - Documentos core promovidos mencionam majoritariamente `memoria/` como caminho conceitual/canônico planejado.
  - P0.1.16 criou `vault-maui/memorias/` porque essa pasta não existia e a tarefa exigia esse destino específico.
- Limites do que foi confirmado:
  - Não foi encontrada decisão normativa explícita que escolha definitivamente entre singular `memoria/` e plural `memorias/`.
  - Não foi feita leitura integral de todos os documentos core; a consulta foi direcionada a ocorrências e fontes recentes materialmente relevantes.

## 3. Fontes consultadas

| Fonte | Caminho ou referência | Motivo da consulta | Observação |
| --- | --- | --- | --- |
| Template canônico | `vault-maui/context-packages/templates/maui-context-brief.template.md` | Estrutura e regra para criação deste brief | Contém regra de priorização de memórias marcadas. |
| Memória marcada | `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` | Marco da P0.1.16 e fechamento da Tarefa 2 | Deve ser considerada em Context Brief. |
| Regras operacionais | `vault-maui/00_core/regras-operacionais.md` | Instruções Codex para Context Brief sob demanda | Menciona `vault-maui/memorias/` ou pasta equivalente. |
| Inventário reconciliado | `vault-maui/inventarios/2026-05-04-documentacao.md` | Fechamento da Tarefa 2 e destinos finais | Confirma saneamento concluído e P0.1.5 desbloqueada. |
| Exec-report P0.1.16 | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-fechamento-tarefa-2-documentacao.md` | Origem da criação de `vault-maui/memorias/` | Registra ressalva: `memorias/` criada; `memoria/` legada não alterada. |
| Exec-reports P0.1.12-P0.1.15 | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-12...` a `...p0-1-15...` | Histórico recente do saneamento documental | Confirmam movimentações, ressalvas e preservação. |
| Core promovido | `vault-maui/00_core/*.md` | Evidências de referências a memória | Ocorrências apontam principalmente para `memoria/`. |
| Estrutura local | `find vault-maui/memoria vault-maui/memorias` | Verificar existência e conteúdo dos diretórios | Só `memorias/` contém a memória P0.1.16. |

## 4. Decisões fechadas relevantes

- Decisão: P0.1.9 criou o template canônico `Maui Context Brief`.
  Fonte: commit `26a56622f1d4f427fcddc288a09e81983b59ea36`; exec-report `2026-05-05-context-brief-template.md`.
  Impacto: P0.1.17 deve usar briefs sob demanda para continuidade.

- Decisão: P0.1.10 instruiu Codex a criar Context Brief sob demanda.
  Fonte: `vault-maui/00_core/regras-operacionais.md`; commit `cbea5991947121b38b5e79d91959201b18860279`.
  Impacto: este brief segue instrução operacional registrada.

- Decisão: P0.1.16 criou uma memória em `vault-maui/memorias/` marcada para Context Brief.
  Fonte: `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`; commit `31c63e90f4c330d500701c79daf409155e24fe47`.
  Impacto: a normalização precisa preservar essa memória e seu marcador.

- Decisão: P0.1.11 não foi executada.
  Fonte: memória P0.1.16 e exec-report P0.1.16.
  Impacto: não assumir etapa intermediária inexistente.

## 5. Pendências e bloqueios

- Pendência ou bloqueio: não há decisão canônica explícita entre `vault-maui/memoria/` e `vault-maui/memorias/`.
- Impacto: scripts futuros, schemas, context briefs, buscas e procedimentos podem consultar caminhos divergentes ou duplicar memórias.
- Menor ação necessária: aprovar uma normalização controlada para escolher o diretório canônico, mover ou manter a memória existente conforme decisão, e registrar compatibilidade/depreciação do outro caminho.

## 6. Handoffs relevantes

| Handoff | Relevância | Status de uso |
| --- | --- | --- |
| `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md` | Contexto histórico da P0.1 e regras de continuidade | Relevante, mas não relido integralmente nesta preparação. |

## 7. Memórias relevantes

- Memória: `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`
- Aplicação: fonte prioritária para decisões fechadas da sessão, commits relevantes, fechamento da Tarefa 2 e próximos passos desbloqueados.
- Fonte: frontmatter contém `deve_ser_considerado_em_context_brief: true`.

## 8. Adendos e insights aplicáveis

- Item: a ambiguidade singular/plural é uma inconsistência estrutural de corpus, não uma divergência de conteúdo das memórias.
- Aplicação: P0.1.17 deve ser uma normalização de caminho/política, não uma reescrita dos documentos core.
- Grau de confiança: alto, baseado na coexistência dos diretórios e nas referências divergentes consultadas.

## 9. Atualizações recentes do corpus

- Atualização: P0.1.16 criou `vault-maui/memorias/` e a primeira memória marcada para Context Brief.
- Arquivo ou área afetada: `vault-maui/memorias/`, template de Context Brief, inventário.
- Impacto esperado: futuros Context Briefs devem considerar memórias marcadas, mas a pasta canônica ainda precisa ser reconciliada.

- Atualização: documentos core promovidos em P0.1.12-P0.1.15 já estão em `vault-maui/00_core/`.
- Arquivo ou área afetada: arquitetura, roadmap, spec funcional e spec técnica v2.
- Impacto esperado: P0.1.17 deve consultar esses documentos apenas para confirmar referências a memória, sem alterar conteúdo substantivo salvo aprovação explícita.

## 10. Documentos necessários para continuar

| Documento | Necessidade | Obrigatório para continuar? |
| --- | --- | --- |
| `vault-maui/memorias/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` | Preservar memória existente e seu marcador | Sim |
| `vault-maui/00_core/regras-operacionais.md` | Confirmar regra de Context Brief e fontes de memória | Sim |
| `vault-maui/context-packages/templates/maui-context-brief.template.md` | Confirmar comportamento de briefs futuros | Sim |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | Verificar referência estrutural a `memoria/` | Sim |
| `vault-maui/00_core/arquitetura-maui-v0-2.md` | Verificar referência estrutural a `memoria/` | Sim |
| `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md` | Verificar referências planejadas a `memoria/` e scripts de memória | Sim |
| `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | Verificar referências funcionais a `memoria/` | Sim |
| `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-fechamento-tarefa-2-documentacao.md` | Entender por que `memorias/` foi criado | Sim |

## 11. Solicitação ao usuário quando houver lacuna documental

- Lacuna documental: falta decisão explícita sobre qual caminho deve ser canônico: `vault-maui/memoria/` ou `vault-maui/memorias/`.
- Impacto na continuidade: sem essa decisão, P0.1.17 pode normalizar na direção errada ou criar compatibilidade contrária à arquitetura planejada.
- Menor conjunto solicitado ao usuário: aprovar uma das duas opções antes da execução:
  - tornar `vault-maui/memoria/` canônico e migrar a memória P0.1.16 para lá, registrando `vault-maui/memorias/` como legado/erro histórico;
  - tornar `vault-maui/memorias/` canônico e atualizar referências operacionais mínimas, registrando divergência com documentos core como débito de reconciliação.

## 12. Contexto mínimo para o próximo executor

- Fatos confirmados:
  - `vault-maui/memoria/` existe.
  - `vault-maui/memorias/` existe.
  - A única memória encontrada está em `vault-maui/memorias/`.
  - A memória P0.1.16 tem `deve_ser_considerado_em_context_brief: true`.
  - P0.1.16 registrou que `vault-maui/memorias/` foi criada e que `vault-maui/memoria/` já existia e não foi alterada.
  - Documentos core promovidos contêm referências a `memoria/`.
  - Regras operacionais mencionam `vault-maui/memorias/` ou pasta equivalente de memórias.

- Hipóteses ou inferências:
  - `vault-maui/memoria/` parece ser o caminho conceitual original nos documentos promovidos.
  - `vault-maui/memorias/` parece ter surgido como destino operacional recente da P0.1.16.
  - A normalização provavelmente deve escolher um caminho canônico e registrar política de transição.

- O que não deve ser assumido:
  - Não assumir que plural `memorias/` é canônico só porque contém a memória mais recente.
  - Não assumir que singular `memoria/` é canônico sem aprovação, apesar das referências nos documentos core.
  - Não mover memória, criar symlink, alterar `.gitignore`, atualizar todos os docs core ou implementar scripts sem prompt específico.

## 13. Riscos de continuidade

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Escolher diretório canônico sem aprovação humana explícita | Média | Alto | Solicitar decisão mínima antes de mover/renomear ou atualizar referências. |
| Perder a memória marcada para Context Brief durante normalização | Baixa | Alto | Validar presença e hash antes/depois de qualquer movimentação. |
| Duplicar memórias em `memoria/` e `memorias/` | Média | Médio | Definir um único caminho canônico e uma política clara para o outro caminho. |
| Atualizar documentos core de forma ampla durante P0.1.17 | Média | Médio | Limitar escopo a normalização canônica e relatório; adiar reconciliação textual ampla. |
| Scripts futuros consultarem caminho diferente do brief/template | Alta | Médio | Registrar a decisão no inventário/memória/exec-report e ajustar apenas instruções operacionais mínimas aprovadas. |

## 14. Próximo passo recomendado

- Próximo passo: pedir aprovação humana para a direção da normalização (`memoria/` canônico ou `memorias/` canônico) e então executar P0.1.17 em lote pequeno.
- Pré-condições:
  - `git status --short` limpo.
  - Validar existência dos dois diretórios.
  - Validar existência e hash da memória P0.1.16.
  - Validar que nenhum arquivo em `Documentação/` será alterado.
- Validações mínimas:
  - Confirmar caminho canônico final.
  - Confirmar que a memória marcada continua acessível.
  - Confirmar que futuros Context Briefs apontam para o caminho escolhido.
  - Criar exec-report da P0.1.17.
