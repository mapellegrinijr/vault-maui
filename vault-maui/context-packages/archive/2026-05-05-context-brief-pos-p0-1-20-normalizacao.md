---
titulo: "Maui Context Brief — Pós-P0.1.20 Normalização Estrutural"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
tarefa_relacionada: "P0.1.21"
fontes_consultadas:
  - "vault-maui/project-memories/"
  - "vault-maui/handoffs/"
  - "vault-maui/00_core/"
  - "vault-maui/inventarios/"
  - "vault-maui/exec-reports/submitted/"
lacunas_detectadas: true
requer_anexos_usuario: false
---

# Maui Context Brief — Pós-P0.1.20 Normalização Estrutural

## 1. Finalidade

Preparar a continuidade após P0.1.20 e antes do Lote 4 — Context Brief readiness, consolidando o contexto mínimo necessário para o próximo executor.

Este brief deve apoiar a provável P0.1.21, sem reabrir `Documentação/`, sem executar P0.1.11 e sem assumir que a instanciação manual Maui já está pronta.

## 2. Estado atual conhecido

- Estado: Tarefa 2 / saneamento inicial de `Documentação/` está concluída.
- Estado: P0.1.17, P0.1.18, P0.1.19 e P0.1.20 foram concluídas e commitadas.
- Estado: `vault-maui/project-memories/` é o diretório canônico de memórias do Maui.
- Estado: `Documentação/` não possui pendências esperadas dos 8 arquivos originalmente inventariados.
- Estado: P0.1.11 permanece não executada.
- Estado: documentos Maui promovidos ao core permanecem com status `proposta`.
- Evidências: memórias marcadas em `vault-maui/project-memories/`, handoffs recentes, registros de normalização, exec-reports P0.1.16 a P0.1.20 e documentos core promovidos.
- Limites do que foi confirmado: este brief sintetiza fontes locais; não executa reconciliação completa do roadmap, não corrige handoffs, não cria readiness de instanciação manual e não valida conteúdo externo.

## 3. Fontes consultadas

| Fonte | Caminho ou referência | Motivo da consulta | Observação |
| --- | --- | --- | --- |
| Template Context Brief | `vault-maui/context-packages/templates/maui-context-brief.template.md` | Estrutura e regras de preenchimento | Template canônico usado como referência primária. |
| Memória de fechamento Tarefa 2 | `vault-maui/project-memories/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` | Decisões, commits e fechamento dos 8 arquivos de `Documentação/` | Marcada para Context Brief. |
| Memória de decisão estrutural | `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md` | Decisão de tratar P0.1.17 como diagnóstico estrutural amplo | Marcada para Context Brief. |
| Memória P0.1.17 | `vault-maui/project-memories/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md` | Resultado do diagnóstico estrutural | Marcada para Context Brief. |
| Memória plano/estado atual | `vault-maui/project-memories/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md` | Estado consolidado até P0.1.20 | Marcada para Context Brief; reconciliada nesta etapa. |
| Handoff pós-inventário | `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md` | Contexto inicial da Tarefa 2 e estado proposta | Handoff histórico reorganizado para `vault-maui/handoffs/`. |
| Handoff fechamento Tarefa 2 | `vault-maui/handoffs/2026-05-05-handoff-fechamento-tarefa-2-pre-p0-1-17.md` | Continuidade até P0.1.17 e decisão de adiar P0.1.11 | Confirma necessidade de Context Brief antes da normalização. |
| Roadmap core | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | Próximos lotes e status proposta | Contém nota de reconciliação; não foi reescrito. |
| Arquitetura core | `vault-maui/00_core/arquitetura-maui-v0-2.md` | Base arquitetural promovida ao core | Status `proposta`. |
| Spec funcional core | `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | Escopo funcional e pendências de alinhamento | Status `proposta`; possui nota de reconciliação. |
| Spec técnica core | `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | Base técnica Saara→Maui | Promovida ao core na P0.1.12. |
| Regras operacionais | `vault-maui/00_core/regras-operacionais.md` | Instruções Codex para Context Brief sob demanda | Consulta `vault-maui/project-memories/` ou pasta equivalente. |
| Inventário documentação | `vault-maui/inventarios/2026-05-04-documentacao.md` | Fechamento da Tarefa 2 | Mantém rastreabilidade dos 8 arquivos. |
| Diagnóstico estrutural | `vault-maui/inventarios/2026-05-05-diagnostico-estrutural-vault-maui.md` | Divergências e lotes futuros | Base de P0.1.17. |
| Registro Lote 1 | `vault-maui/inventarios/2026-05-05-normalizacao-memorias.md` | Diretório canônico de memórias | Base de P0.1.18. |
| Registro Lote 2 | `vault-maui/inventarios/2026-05-05-normalizacao-referencias-wikilinks.md` | Referências e wikilinks | Base de P0.1.19. |
| Registro Lote 3 | `vault-maui/inventarios/2026-05-05-normalizacao-frontmatter-slugs.md` | Frontmatter e slugs | Base de P0.1.20. |
| Exec-reports recentes | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-*.md` a `2026-05-05-p0-1-20-*.md` | Evidência operacional das execuções | Usados para commits, resultados e ressalvas. |

## 4. Decisões fechadas relevantes

- Decisão: `vault-maui/project-memories/` é o diretório canônico de memórias.
  Fonte: P0.1.18 e registro `2026-05-05-normalizacao-memorias.md`.
  Impacto: Context Briefs futuros devem consultar essa pasta e priorizar memórias com `deve_ser_considerado_em_context_brief: true`.

- Decisão: referências operacionais foram normalizadas de forma conservadora.
  Fonte: P0.1.19.
  Impacto: documentos core usam `memorias/` em referências operacionais; históricos foram preservados.

- Decisão: frontmatter/slugs foram tratados de forma controlada.
  Fonte: P0.1.20.
  Impacto: apenas `vault-maui/panel/status.md` recebeu frontmatter; nenhum slug foi renomeado.

- Decisão: handoffs recentes foram reorganizados para `vault-maui/handoffs/`.
  Fonte: P0.1.18-pre e P0.1.19.
  Impacto: `panel/status.md` passou a apontar para o handoff reorganizado.

- Decisão: P0.1.11 permanece adiada.
  Fonte: handoff de 2026-05-05 e exec-reports recentes.
  Impacto: não instruir Claude Code a criar Context Brief sem aprovação explícita.

## 5. Pendências e bloqueios

- Pendência: Lote 4 — Context Brief readiness.
  Impacto: ainda falta garantir descoberta confiável de memórias, handoffs, exec-reports, insights e atualizações.
  Menor ação necessária: aprovar e executar P0.1.21.

- Pendência: Lote 5 — Instanciação manual Maui.
  Impacto: readiness de instanciação manual ainda não deve ser tratado como concluído.
  Menor ação necessária: executar após readiness documental suficiente.

- Pendência: P0.1.11.
  Impacto: Claude Code ainda não foi instruído a criar Context Brief sob demanda.
  Menor ação necessária: aprovação humana específica.

- Pendência: retomada de P0.1.5.
  Impacto: o plano de adaptação Saara→Maui deve considerar documentos core normalizados, mas ainda depende de normalização suficiente.
  Menor ação necessária: retomar depois de P0.1.21 ou após decisão humana.

- Pendência: placeholders/wikilinks sem destino inequívoco.
  Impacto: não devem ser corrigidos por inferência.
  Menor ação necessária: lote próprio ou decisão de destinos canônicos.

- Pendência: READMEs, índices auxiliares e templates antigos sem frontmatter.
  Impacto: não bloqueia este brief, mas pode afetar automações futuras.
  Menor ação necessária: decidir se entram em lote posterior.

## 6. Handoffs relevantes

| Handoff | Relevância | Status de uso |
| --- | --- | --- |
| `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md` | Registra estado pós-inventário de `Documentação/`, status `proposta` e necessidade de decisão explícita antes de alterar documentos | Usar como contexto histórico; não tratar como estado final atual. |
| `vault-maui/handoffs/2026-05-05-handoff-fechamento-tarefa-2-pre-p0-1-17.md` | Registra fechamento da Tarefa 2, criação do padrão Context Brief e adiamento da P0.1.11 | Usar como transição para normalização estrutural. |

## 7. Memórias relevantes

- Memória: `vault-maui/project-memories/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`
  Aplicação: confirma fechamento da Tarefa 2, documentos promovidos/arquivados, status `proposta` e P0.1.11 não executada.
  Fonte: frontmatter marcado com `deve_ser_considerado_em_context_brief: true`.

- Memória: `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md`
  Aplicação: registra decisão de transformar P0.1.17 em diagnóstico estrutural amplo e organizar correções por lotes.
  Fonte: frontmatter marcado com `deve_ser_considerado_em_context_brief: true`.

- Memória: `vault-maui/project-memories/2026-05-05-marco-diagnostico-estrutural-p0-1-17.md`
  Aplicação: sintetiza divergências estruturais, readiness parcial para Context Brief e proposta de lotes.
  Fonte: frontmatter marcado com `deve_ser_considerado_em_context_brief: true`.

- Memória: `vault-maui/project-memories/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md`
  Aplicação: consolida o ponto alcançado até P0.1.20 e os commits relevantes da normalização.
  Fonte: frontmatter marcado com `deve_ser_considerado_em_context_brief: true`.

## 8. Adendos e insights aplicáveis

- Item: nenhum adendo ou insight específico foi localizado como fonte obrigatória nesta preparação.
- Aplicação: tratar como lacuna leve, sem bloquear P0.1.21.
- Grau de confiança: médio; a ausência foi inferida das fontes obrigatórias consultadas, não de um inventário exaustivo de `adendos/` e `insights/`.

## 9. Atualizações recentes do corpus

- Atualização: P0.1.16 fechou a Tarefa 2 e criou memória de marco.
  Arquivo ou área afetada: inventário de `Documentação/`, `vault-maui/project-memories/`, exec-report P0.1.16.
  Impacto esperado: `Documentação/` não deve ser reaberta para os 8 arquivos inventariados.

- Atualização: P0.1.17 diagnosticou a estrutura do vault Maui.
  Arquivo ou área afetada: inventário diagnóstico e exec-report P0.1.17.
  Impacto esperado: normalização estrutural deve continuar por lotes.

- Atualização: P0.1.18 adotou `vault-maui/project-memories/` como diretório canônico.
  Arquivo ou área afetada: template Context Brief, registro de normalização e exec-report P0.1.18.
  Impacto esperado: briefs futuros devem priorizar memórias marcadas nesse diretório.

- Atualização: P0.1.19 normalizou referências operacionais e wikilinks conservadoramente.
  Arquivo ou área afetada: documentos core e `panel/status.md`.
  Impacto esperado: referências históricas devem continuar preservadas.

- Atualização: P0.1.20 adicionou frontmatter ao painel operacional e registrou pendências de frontmatter/slugs.
  Arquivo ou área afetada: `vault-maui/panel/status.md`, registro e exec-report P0.1.20.
  Impacto esperado: READMEs/templates antigos permanecem pendentes, sem bloquear P0.1.21.

- Atualização: marco de memória pós-P0.1.20 foi reconciliado para nome canônico.
  Arquivo ou área afetada: `vault-maui/project-memories/2026-05-05-marco-plano-normalizacao-estrutural-estado-atual.md`.
  Impacto esperado: futuros Context Briefs devem considerar esse marco.

## 10. Documentos necessários para continuar

| Documento | Necessidade | Obrigatório para continuar? |
| --- | --- | --- |
| `vault-maui/context-packages/templates/maui-context-brief.template.md` | Referência canônica para briefs | Sim |
| `vault-maui/project-memories/*.md` com `deve_ser_considerado_em_context_brief: true` | Memórias priorizadas | Sim |
| `vault-maui/handoffs/2026-05-04-handoff-sessao-claude-pos-inventario.md` | Histórico pós-inventário | Sim |
| `vault-maui/handoffs/2026-05-05-handoff-fechamento-tarefa-2-pre-p0-1-17.md` | Transição para normalização estrutural | Sim |
| Documentos core em `vault-maui/00_core/` | Estado documental base | Sim |
| Registros P0.1.17 a P0.1.20 | Critérios e ressalvas dos lotes | Sim |
| Exec-reports P0.1.16 a P0.1.20 | Evidência operacional | Sim |
| Adendos e insights | Não localizados como fonte obrigatória nesta preparação | Não, salvo se P0.1.21 exigir inventário específico |

## 11. Solicitação ao usuário quando houver lacuna documental

- Lacuna documental: adendos/insights aplicáveis não foram identificados nas fontes obrigatórias desta preparação.
- Impacto na continuidade: baixo para P0.1.21, pois o foco é readiness de Context Brief com memórias, handoffs, exec-reports, inventários e core.
- Menor conjunto solicitado ao usuário: nenhum anexo é necessário neste momento.

## 12. Contexto mínimo para o próximo executor

- Fatos confirmados:
  - `vault-maui/project-memories/` é canônico.
  - As quatro memórias relevantes estão marcadas com `deve_ser_considerado_em_context_brief: true`.
  - P0.1.17 a P0.1.20 foram executadas.
  - P0.1.11 não foi executada.
  - `Documentação/` não deve ser alterada.
  - Status Maui permanece `proposta`.

- Hipóteses ou inferências:
  - P0.1.21 provavelmente deve implementar Lote 4 — Context Brief readiness.
  - Readiness deve validar descoberta de memórias, handoffs, exec-reports, inventários, core, adendos/insights quando existirem e atualizações recentes.

- O que não deve ser assumido:
  - Não assumir que instanciação manual Maui está pronta.
  - Não assumir que placeholders/wikilinks pendentes têm destino canônico.
  - Não assumir que registros históricos devem ser reescritos para refletir caminhos atuais.

- Arquivos que podem ser alterados na próxima tarefa, se aprovada:
  - template de Context Brief;
  - registros/inventários de readiness;
  - exec-report da próxima tarefa;
  - possivelmente scripts ou índices de descoberta, se forem escopo explícito.

- Arquivos que não devem ser alterados sem aprovação explícita:
  - `Documentação/`;
  - documentos core promovidos, salvo leitura ou ajuste expressamente autorizado;
  - handoffs e memórias existentes, salvo reconciliação aprovada;
  - registros históricos.

- Validações mínimas:
  - `git status --short` inicial limpo ou pendências explicitamente classificadas;
  - frontmatter YAML válido em artefatos novos;
  - confirmação de que P0.1.11 não foi executada;
  - confirmação de que `Documentação/` não foi alterada;
  - confirmação de que Context Briefs futuros não copiam corpus inteiro.

## 13. Riscos de continuidade

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Confundir registros históricos com orientação operacional atual | Média | Alto | Classificar fontes como histórica, diagnóstica, operacional ou ambígua antes de editar. |
| Reabrir `Documentação/` sem necessidade | Baixa | Alto | Tratar Tarefa 2 como concluída e consultar documentos promovidos ao core/archive. |
| Executar P0.1.11 sem aprovação | Baixa | Médio | Manter P0.1.11 como pendência explícita. |
| Assumir readiness de instanciação manual como concluída | Média | Alto | Continuar pelos lotes de readiness antes de instanciar. |
| Copiar corpus inteiro em Context Briefs futuros | Média | Médio | Aplicar Context Injection Sob Demanda e sintetizar só fontes materialmente necessárias. |
| Ignorar memórias marcadas para Context Brief | Baixa | Alto | Priorizar `deve_ser_considerado_em_context_brief: true` em `vault-maui/project-memories/`. |

## 14. Próximo passo recomendado

- Próximo passo: executar P0.1.21 — Lote 4 Context Brief readiness.
- Pré-condições: aprovação humana do escopo; working tree limpo; leitura das quatro memórias marcadas e dos registros P0.1.17 a P0.1.20.
- Validações mínimas: confirmar que `vault-maui/project-memories/`, `vault-maui/handoffs/`, `vault-maui/exec-reports/submitted/`, `vault-maui/inventarios/` e `vault-maui/00_core/` são descobertos sem copiar o corpus inteiro.
