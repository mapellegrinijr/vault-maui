---
titulo: "Inventário diagnóstico — estrutura do vault Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: inventario_diagnostico
escopo: projeto_maui
fase: P0.1.17
---

# Inventário diagnóstico — estrutura do vault Maui

## 1. Contexto

Este diagnóstico ocorre após o fechamento da Tarefa 2 / saneamento inicial de `Documentação/` e antes de qualquer correção estrutural. O objetivo é identificar divergências no `vault-maui/`, inventariar riscos e propor lotes futuros de correção.

> Este inventário não aplica correções. Nenhum arquivo existente foi movido, apagado, renomeado ou reescrito nesta tarefa.

Observação de estado inicial: `git status --short` não estava limpo antes deste diagnóstico. Havia uma remoção pendente em `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md`, arquivos não rastreados em `vault-maui/handoffs/`, uma memória não rastreada em `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md` e um arquivo `Sem título.canvas` não rastreado na raiz. Estes itens foram apenas observados, não alterados.

## 2. Mapa de diretórios do vault

Diretórios de primeiro e segundo nível sob `vault-maui/`:

| Caminho | Existe? | Arquivos | Subdiretórios | Observações |
| --- | --- | ---: | ---: | --- |
| `vault-maui/` | sim | 2 | 26 | raiz canônica; contém `.DS_Store` |
| `vault-maui/00_core/` | sim | 6 | 0 | contém documentos core promovidos; `README.md` sem frontmatter |
| `vault-maui/01_manifest/` | sim | 1 | 0 | apenas `README.md`; vazio funcionalmente |
| `vault-maui/adendos/` | sim | 1 | 0 | apenas `README.md` |
| `vault-maui/automations/` | sim | 0 | 0 | diretório vazio |
| `vault-maui/context-packages/` | sim | 1 | 5 | contém `.DS_Store`; estrutura ativa de briefs/handoffs |
| `vault-maui/context-packages/archive/` | sim | 6 | 0 | contém handoffs arquivados e documentos históricos |
| `vault-maui/context-packages/current/` | sim | 1 | 0 | contém Context Brief P0.1.17; há remoção pendente de handoff antigo no git status |
| `vault-maui/context-packages/generated/` | sim | 0 | 0 | vazio |
| `vault-maui/context-packages/targets/` | sim | 0 | 0 | vazio |
| `vault-maui/context-packages/templates/` | sim | 1 | 0 | contém template `Maui Context Brief` |
| `vault-maui/evals/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-reports/` | sim | 0 | 4 | contém subpastas de reports |
| `vault-maui/exec-reports/examples/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-reports/reviewed/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-reports/submitted/` | sim | 19 | 0 | reports submetidos; mistura reports antigos sem frontmatter e novos com frontmatter |
| `vault-maui/exec-reports/templates/` | sim | 2 | 0 | templates sem frontmatter |
| `vault-maui/exec-requests/` | sim | 0 | 4 | estrutura criada, sem requests ativos |
| `vault-maui/exec-requests/assigned/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-requests/backlog/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-requests/examples/` | sim | 0 | 0 | vazio |
| `vault-maui/exec-requests/templates/` | sim | 1 | 0 | template sem frontmatter |
| `vault-maui/exports/` | sim | 0 | 0 | vazio |
| `vault-maui/handoffs/` | sim | 2 | 0 | diretório não rastreado no status inicial; possível normalização recente |
| `vault-maui/hooks/` | sim | 0 | 0 | vazio |
| `vault-maui/insights/` | sim | 0 | 0 | vazio |
| `vault-maui/inventarios/` | sim | 1 | 0 | contém inventário de `Documentação/`; este diagnóstico será adicionado |
| `vault-maui/mcp-servers/` | sim | 0 | 0 | vazio |
| `vault-maui/memoria/` | sim | 0 | 0 | vazio; singular; citado nos documentos core |
| `vault-maui/project-memories/` | sim | 2 | 0 | plural; contém memórias marcadas para Context Brief; uma delas não rastreada no status inicial |
| `vault-maui/operator-packs/` | sim | 0 | 7 | subpastas por target, todas vazias |
| `vault-maui/operator-packs/antigravity/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/chatgpt-action/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/chatgpt-handoff/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/claude/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/claude-code/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/codex/` | sim | 0 | 0 | vazio |
| `vault-maui/operator-packs/gemini/` | sim | 0 | 0 | vazio |
| `vault-maui/panel/` | sim | 2 | 2 | painel file-based inicial |
| `vault-maui/panel/decisions/` | sim | 1 | 0 | índice sem frontmatter |
| `vault-maui/panel/reviews/` | sim | 1 | 0 | índice sem frontmatter |
| `vault-maui/plugins/` | sim | 0 | 0 | vazio |
| `vault-maui/procedures/` | sim | 0 | 0 | vazio |
| `vault-maui/reflexes/` | sim | 0 | 0 | vazio |
| `vault-maui/schemas/` | sim | 5 | 1 | schemas P0 já existem |
| `vault-maui/schemas/fixtures/` | sim | 0 | 2 | contém fixtures válidas e inválidas em subpastas |
| `vault-maui/scripts/` | sim | 0 | 0 | vazio |
| `vault-maui/skills/` | sim | 0 | 0 | vazio |
| `vault-maui/subagents/` | sim | 0 | 0 | vazio |
| `vault-maui/validations/` | sim | 0 | 0 | vazio |

Diretórios relevantes ausentes na validação prévia:

- `vault-maui/review-reports/` não existe, embora `review-reports` seja citado como fonte esperada em fluxos de Context Brief.

## 3. Divergências estruturais detectadas

| ID | Divergência | Caminhos envolvidos | Evidência | Severidade | Impacto | Correção sugerida em lote futuro |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 | Singular/plural para memórias | `vault-maui/memoria/`, `vault-maui/project-memories/` | ambos existem; `memoria/` vazio; `memorias/` contém memórias marcadas; core cita `memoria/` | alta | Context Briefs, scripts e validações podem procurar memórias em caminhos diferentes | Lote 1: decidir canônico e compatibilizar ou migrar sem perda |
| D-002 | Handoffs em dois lugares e estado git pendente | `vault-maui/context-packages/current/`, `vault-maui/context-packages/archive/`, `vault-maui/handoffs/` | status inicial mostra delete pendente em `context-packages/current/...` e `vault-maui/handoffs/` não rastreado | média | próximos briefs podem referenciar handoff antigo inexistente no caminho anterior | Lote 4: definir local canônico de handoffs atuais |
| D-003 | Diretório esperado ausente | `vault-maui/review-reports/` | validação prévia retornou ausente | baixa | Context Brief pode listar review-reports como fonte, mas não há área canônica | Lote 4: criar ou documentar ausência |
| D-004 | Operator packs só como diretórios vazios | `vault-maui/operator-packs/*/` | 7 subpastas, 0 arquivos | média | instanciação manual não tem templates operacionais por target | Lote 5: consolidar packs mínimos |
| D-005 | Muitos diretórios vazios de execução | `scripts/`, `procedures/`, `skills/`, `hooks/`, `evals/`, `exports/` | mapa de diretórios mostra 0 arquivos | média | roadmap/spec citam capacidades ainda não materializadas | Lotes 3 e 5: diferenciar placeholder intencional de lacuna de readiness |
| D-006 | Mistura português/inglês e singular/plural | `inventarios/`, `memoria/`, `memorias/`, `exec-reports/`, `context-packages/` | nomes misturam idioma e morfologia | baixa | automações futuras podem exigir convenção explícita | Lote 3: registrar convenção de nomes, sem renomear em massa |
| D-007 | Arquivos de sistema versionáveis no vault | `.DS_Store` em `vault-maui/` e `vault-maui/context-packages/` | mapa de arquivos detectou ambos | baixa | ruído em inventários e hashes futuros | Lote 3: decidir política de exclusão/remoção |

## 4. Diagnóstico de memórias

### `vault-maui/memoria/`

- Existe? sim.
- Arquivos: nenhum.
- Subdiretórios: nenhum.
- Frontmatter dos arquivos: não aplicável.
- Presença de `deve_ser_considerado_em_context_brief: true`: nenhuma, pois não há arquivos.
- Referências no corpus: múltiplas referências em documentos core e arquivos arquivados. Exemplos:
  - `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` cita `memoria/` como parte da estrutura.
  - `vault-maui/00_core/arquitetura-maui-v0-2.md` cita `memoria/` como área de memórias operacionais e episódicas.
  - `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` cita `memoria/README.md`, `memoria/YYYY/MM/...` e scripts de índice.
  - `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` cita `memoria/` para busca, índice e estrutura.

### `vault-maui/project-memories/`

- Existe? sim.
- Arquivos:
  - `vault-maui/project-memories/2026-05-05-marco-fechamento-tarefa-2-documentacao.md`
  - `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md` *(não rastreado no status inicial)*
- Subdiretórios: nenhum.
- Frontmatter dos arquivos: ambos foram lidos como YAML válido.
- Presença de `deve_ser_considerado_em_context_brief: true`: presente nos dois arquivos.
- Referências no corpus:
  - `vault-maui/00_core/regras-operacionais.md` menciona `vault-maui/project-memories/` ou pasta equivalente de memórias.
  - `vault-maui/context-packages/templates/maui-context-brief.template.md` prioriza memórias com `deve_ser_considerado_em_context_brief: true`.
  - `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-fechamento-tarefa-2-documentacao.md` registra que `vault-maui/project-memories/` foi criada e que `vault-maui/memoria/` existia como pasta legada não alterada.

Diagnóstico: `memoria/` parece ser o caminho planejado nos documentos core; `memorias/` é o caminho operacional recente onde as memórias marcadas foram gravadas. Esta é a divergência estrutural de maior prioridade.

## 5. Diagnóstico de documentos core

| Arquivo | Tipo documental | Status | Versão | Frontmatter | Lacuna para instanciação manual |
| --- | --- | --- | --- | --- | --- |
| `vault-maui/00_core/README.md` | não declarado | não declarado | não declarado | ausente | README informativo, não substitui system prompt |
| `vault-maui/00_core/regras-operacionais.md` | `regra_operacional` | `ativo` | `1.0` | válido | contém instrução Codex para Context Brief sob demanda |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | `especificacao_tecnica_atualizacao` | `proposta` | `0.2` | válido | cita `system-prompt.md` e `pka-*.md`, mas estes não existem no core |
| `vault-maui/00_core/arquitetura-maui-v0-2.md` | `especificacao_arquitetural` | `proposta` | `0.2` | válido | arquitetura existe, mas ainda há nota de proposta e referências a estrutura futura |
| `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | `roadmap` | `proposta` | `1.0` | válido | possui nota de reconciliação; fases não foram reconciliadas integralmente |
| `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | `especificacao_funcional` | `proposta` | `0.1` | válido | possui nota de reconciliação; funcionalidades ainda não reconciliadas integralmente |

Lacunas específicas verificadas:

- `vault-maui/00_core/system-prompt.md`: ausente.
- `vault-maui/00_core/pka-*.md`: nenhum arquivo encontrado.
- Regras operacionais: presentes.
- Spec técnica Saara→Maui v2: presente.
- Arquitetura, roadmap e spec funcional: presentes, com status `proposta`.

## 6. Diagnóstico de frontmatter

Foram percorridos arquivos Markdown sob `vault-maui/`.

### YAML inválido

Nenhum frontmatter YAML inválido foi detectado pelo parser nos arquivos Markdown com bloco `---`.

### Arquivos sem frontmatter

Arquivos sem frontmatter detectados:

- `vault-maui/README.md`
- `vault-maui/00_core/README.md`
- `vault-maui/01_manifest/README.md`
- `vault-maui/adendos/README.md`
- `vault-maui/context-packages/archive/2026-05-04-handoff-sessao-maui.md`
- `vault-maui/context-packages/archive/arquitetura-novo-saara-maui-draft.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-draft.md`
- `vault-maui/context-packages/archive/pacote-documental-maui-multi-ia-v1-0.md`
- vários exec-reports antigos de 2026-05-04 em `vault-maui/exec-reports/submitted/`
- `vault-maui/exec-reports/templates/exec-report-template.md`
- `vault-maui/exec-reports/templates/review-report-template.md`
- `vault-maui/exec-requests/templates/exec-request-template.md`
- `vault-maui/panel/README.md`
- `vault-maui/panel/decisions/index.md`
- `vault-maui/panel/reviews/index.md`
- `vault-maui/panel/status.md`

### Campos mínimos ausentes

Nos arquivos com frontmatter válido, não foram detectadas ausências dos campos mínimos diagnósticos: `titulo`, `versao`, `status`, `data_criacao` ou `data_atualizacao`, `idioma`, `tipo`, `escopo`.

### Valores de `status` incomuns

- `current` aparece no Context Brief instanciado para P0.1.17. É plausível para `tipo: context_brief`, mas deve ser validado contra convenção futura.
- `template`, `submitted`, `ativo` e `proposta` aparecem coerentes com usos atuais.

### Valores de `tipo` divergentes ou inconsistentes

Não foi confirmada inconsistência funcional entre tipos atuais, mas há diversidade sem taxonomia consolidada: `regra_operacional`, `especificacao_tecnica_atualizacao`, `especificacao_arquitetural`, `roadmap`, `especificacao_funcional`, `context_brief`, `context_brief_template`, `exec_report`, `handoff_sessao`, `inventario_diagnostico`, `memoria_marco`, `memoria_decisao`.

## 7. Diagnóstico de nomes e slugs

Inconsistências observadas:

- Underscores vs hífens:
  - schemas usam hífens: `exec-report.schema.yaml`, `common-frontmatter.schema.yaml`.
  - arquivos promovidos ao core usam hífens.
  - inventário preserva referências históricas com underscores, como `arquitetura_maui_v_0_2.md`.
- Versões:
  - arquivos core normalizados usam `v0-2`, `v1-0`, `v0-1`.
  - referências históricas ainda aparecem como `v_0_2`, `v_1_0`, `v_0_1`.
  - frontmatter usa versões sem prefixo `v`, como `"0.2"` e `"1.0"`.
- Nomes duplicados para conceito:
  - `spec-tecnica-atualizacao-saara-maui-v2.md` no core e `spec-tecnica-atualizacao-saara-maui-v1.md` no archive.
  - pacotes documentais draft/v1.0 arquivados com nomes normalizados, mas referências históricas mantêm nomes com espaços/underscores.
- Arquivos com espaços:
  - os arquivos originais em `Documentação/` com espaços foram arquivados com slugs sem espaços; referências históricas permanecem no inventário.
- Arquivos sem extensão:
  - o arquivo original `Documentação/Arquitetura novo Saara - Maui` foi arquivado como `.md`; referências históricas permanecem no inventário.
- Acentuação:
  - `Documentação/` permanece como caminho referenciado historicamente; a pasta atual não contém os 8 arquivos originais.

## 8. Diagnóstico de referências e wikilinks

Referências buscadas: `Documentação/`, `vault-maui/memoria`, `vault-maui/memorias`, `memoria/`, `memorias/`, `context-packages/current`, `context-packages/archive`, nomes antigos e novos dos documentos promovidos, `[[...]]`, `[[link]]`, `[[wikilink]]`.

| Arquivo | Trecho curto | Provável status |
| --- | --- | --- |
| `vault-maui/inventarios/2026-05-04-documentacao.md` | múltiplas referências a `Documentação/...` | válido como histórico/inventário |
| `vault-maui/project-memories/2026-05-05-marco-fechamento-tarefa-2-documentacao.md` | menciona `Documentação/` e arquivos promovidos | válido como memória histórica |
| `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-fechamento-tarefa-2-documentacao.md` | registra criação de `vault-maui/project-memories/` e pasta legada `vault-maui/memoria/` | válido como evidência |
| `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md` | `[[context-packages/current]]`, `[[spec-tecnica-atualizacao-saara-maui-v1]]` | precisa revisão; pode apontar para conceito/destino antigo |
| `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | `1. Localizar links [[...]]` | válido como exemplo de funcionalidade, não necessariamente placeholder ativo |
| `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` | `Valida links internos [[...]]` | válido como exemplo funcional |
| `vault-maui/inventarios/2026-05-04-documentacao.md` | `[[...]]`, `[[link]]`, `[[wikilink]]` | placeholder histórico; precisa revisão se migrado para core |
| `vault-maui/context-packages/current/2026-05-05-context-brief-p0-1-17-normalizacao-memorias.md` | `vault-maui/memoria/` e `vault-maui/project-memories/` | válido como diagnóstico/lacuna |
| `vault-maui/handoffs/2026-05-05-handoff-fechamento-tarefa-2-pre-p0-1-17.md` | ambiguidade `vault-maui/memoria/` vs `vault-maui/project-memories/` | válido como handoff, mas arquivo não rastreado no status inicial |
| `vault-maui/00_core/arquitetura-maui-v0-2.md` | `context-packages/current/maui-bootstrap.md` | possivelmente futuro/ausente; precisa revisão |

Não foram alteradas referências nesta tarefa.

## 9. Diagnóstico de Context Brief

- `vault-maui/context-packages/templates/maui-context-brief.template.md` existe.
- O template menciona memórias marcadas com `deve_ser_considerado_em_context_brief: true`.
- O template não aponta explicitamente para `memoria/` nem `memorias/`; ele instrui consultar memórias relevantes.
- `vault-maui/00_core/regras-operacionais.md` aponta para `vault-maui/project-memories/` ou pasta equivalente de memórias.
- `vault-maui/context-packages/current/` existe.
- Há um brief instanciado rastreado: `vault-maui/context-packages/current/2026-05-05-context-brief-p0-1-17-normalizacao-memorias.md`.
- Há remoção pendente de `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md` no status inicial.

Lacunas para Context Brief funcionar como apoio real:

- diretório canônico de memórias não está definido;
- handoffs aparecem em `context-packages/archive/`, `context-packages/current/` e `handoffs/`;
- `review-reports/` não existe;
- não há índice ou script de busca de memórias;
- template depende de disciplina manual para consultar fontes relevantes.

## 10. Diagnóstico de readiness para instanciação manual

Itens verificados:

- `vault-maui/00_core/system-prompt.md`: ausente.
- PKAs em `vault-maui/00_core/pka-*.md`: ausentes.
- Operator packs em `vault-maui/operator-packs/`: diretórios existem, mas não há arquivos de pack/template.
- Template ou instrução Codex: existe instrução em `vault-maui/00_core/regras-operacionais.md`; não há `AGENTS.md` ou operator pack Codex materializado.
- Template ou instrução Claude Code: não encontrado como arquivo materializado; P0.1.11 não foi executada.
- Context package bootstrap/current: existe Context Brief atual; não foi encontrado `maui-bootstrap.md`.
- Regras para instância sem filesystem declarar `unknown`, nunca `current`: aparecem nos documentos core, especialmente roadmap/spec funcional/spec técnica, mas não estão consolidadas em system prompt ou operator pack.
- Registro ou inventário de instâncias: não encontrado como artefato materializado.

Classificação de readiness: **experimental**.

Justificativa: há documentos core importantes e regras operacionais, mas faltam system prompt, PKAs herdadas, operator packs funcionais, bootstrap package, registry de instâncias e normalização estrutural de memórias/handoffs.

## 11. Proposta de lotes futuros de correção

### Lote 1 — Memórias

- Objetivo: normalizar ou compatibilizar `memoria/` vs `memorias/`.
- Pré-requisitos: decisão humana sobre caminho canônico; hash dos arquivos em `memorias/`; status git limpo ou isolamento de mudanças pendentes.
- Arquivos prováveis: `vault-maui/memoria/`, `vault-maui/project-memories/`, template de Context Brief, regras operacionais, inventário/exec-report.
- Risco: médio.
- Critério de aceite: uma fonte canônica definida, memórias marcadas preservadas, Context Briefs conseguem encontrá-las.

### Lote 2 — Referências e wikilinks

- Objetivo: atualizar referências obsoletas e placeholders.
- Pré-requisitos: Lote 1 concluído; lista de referências revisada.
- Arquivos prováveis: documentos core, inventário, context packages, arquivos arquivados apenas se decisão explícita.
- Risco: médio.
- Critério de aceite: placeholders reais classificados; referências históricas preservadas onde fizerem sentido; referências operacionais atualizadas.

### Lote 3 — Frontmatter e slugs

- Objetivo: normalizar campos mínimos, status, tipo, nomes e versões.
- Pré-requisitos: definir taxonomia de `tipo` e status permitidos.
- Arquivos prováveis: README/templates/reports antigos, schemas, inventários.
- Risco: médio.
- Critério de aceite: diagnóstico de frontmatter sem lacunas críticas nos documentos operacionais atuais.

### Lote 4 — Context Brief readiness

- Objetivo: garantir que briefs encontrem memórias, handoffs, exec-reports, insights e atualizações.
- Pré-requisitos: Lote 1 e decisão sobre handoffs atuais.
- Arquivos prováveis: template de Context Brief, regras operacionais, possível índice/README de handoffs/memórias.
- Risco: médio.
- Critério de aceite: brief novo consegue declarar fontes consultadas/ausentes sem ambiguidade de diretórios.

### Lote 5 — Instanciação manual Maui

- Objetivo: criar ou consolidar system prompt, PKAs herdadas, operator packs e context package bootstrap.
- Pré-requisitos: estrutura mínima normalizada e readiness de Context Brief.
- Arquivos prováveis: `00_core/system-prompt.md`, `00_core/pka-*.md`, `operator-packs/*`, `context-packages/current/maui-bootstrap.md`.
- Risco: alto.
- Critério de aceite: uma instanciação manual consegue declarar estado `unknown` quando não houver filesystem/hash e operar com contexto mínimo confiável.

## 12. Recomendação do executor

Recomendo executar primeiro o **Lote 1 — Memórias**, porque a ambiguidade `memoria/` vs `memorias/` afeta Context Brief, memória marcada, scripts futuros e readiness de instanciação. A correção deve ser pequena, com decisão humana explícita sobre o caminho canônico antes de qualquer movimentação.

## 13. F/I/H

### Fatos

- `vault-maui/memoria/` existe e está vazio.
- `vault-maui/project-memories/` existe e contém duas memórias, ambas com `deve_ser_considerado_em_context_brief: true`.
- Uma das memórias em `vault-maui/project-memories/` estava não rastreada no status inicial.
- Documentos core promovidos existem em `vault-maui/00_core/`.
- `system-prompt.md` e `pka-*.md` não existem em `vault-maui/00_core/`.
- `vault-maui/operator-packs/` contém subdiretórios, mas nenhum arquivo de pack/template.
- `vault-maui/review-reports/` não existe.
- P0.1.11 não aparece no `git log --grep='p0.1.11'`.

### Inferências

- `memoria/` parece ser o caminho conceitual original usado pelos documentos core.
- `memorias/` parece ser o caminho operacional recente criado na P0.1.16 para a memória de fechamento.
- A readiness para instanciação manual ainda é experimental, apesar de o core documental estar mais maduro.
- A coexistência de handoffs em múltiplos locais sugere necessidade de política canônica de handoffs.

### Hipóteses

- O usuário provavelmente desejará preservar `memorias/` até que a memória não rastreada seja incorporada ou migrada conscientemente.
- O caminho singular `memoria/` pode ser preferível para alinhar com documentos core, mas isso exige aprovação.
- `review-reports/` pode ser criado em lote futuro ou substituído por `panel/reviews/`, mas não há decisão explícita.

## 14. Próximo passo recomendado

Aprovar o **Lote 1 — Memórias** para decidir o caminho canônico entre `vault-maui/memoria/` e `vault-maui/project-memories/`, preservando as memórias marcadas para Context Brief e registrando a compatibilidade/depreciação do caminho não escolhido.
