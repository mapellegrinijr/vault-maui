---
titulo: "Procedimento — Gerar Maui Context Brief"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: procedimento_operacional
escopo: projeto_maui
confidencialidade: interna
mantenedor: claude-code
---

# Procedimento — Gerar Maui Context Brief

## Finalidade

Descrever passo a passo como gerar um `Maui Context Brief` confiável: seleção de fontes, ordem de leitura, regras de declaração de lacunas, separação de F/I/H e critérios de qualidade. Este procedimento é a referência canônica para Claude Code, Codex e qualquer executor que precise preparar retomada segura de tarefas no projeto Maui.

## Quando usar

- Antes de iniciar ou retomar qualquer tarefa no projeto Maui que exija contexto de estado atual.
- Quando solicitado explicitamente pelo usuário ("gere o context brief", "prepare o contexto para retomada").
- Antes de handoffs entre sessões, agentes ou operadores.
- Quando um executor recém-iniciado precisa se orientar sobre o estado real do projeto.

## Quando não usar

- Para inventariar o corpus completo (não é dump integral do vault).
- Como substituto de exec-reports ou de inventários de diagnóstico.
- Para registrar decisões ainda abertas como se fossem fechadas.
- Para executar ou avançar etapas do roadmap.
- Para reabrir `Documentação/` ou alterar `vault-maui/00_core/`.
- Quando o objetivo é apenas registrar uma memória ou criar um exec-report.

## Pré-condições

Antes de iniciar a geração do brief, verificar:

1. `git status --short` confirma working tree limpo ou lista arquivos em estado conhecido.
2. O gerador tem acesso ao filesystem de `vault-maui/` ou recebe os arquivos mínimos via anexo.
3. A tarefa ou escopo-alvo do brief está definido (ex.: pós-P0.1.28, retomada de P0.1.29, handoff Saara).
4. Nenhuma etapa do roadmap será executada durante a geração do brief.

## Fontes obrigatórias

Ler sempre antes de compor o brief:

| Fonte | Caminho | Prioridade |
| --- | --- | --- |
| Git local | `git status`, `git log --oneline -20`, `git show <hash>` | 1 — máxima |
| Exec-reports submetidos | `vault-maui/exec-reports/submitted/` | 2 |
| Inventários | `vault-maui/inventarios/` | 3 |
| Memórias canônicas com flag | `vault-maui/project-memories/` onde `deve_ser_considerado_em_context_brief: true` | 4 |
| Handoffs recentes | `vault-maui/handoffs/` | 5 |
| Context briefs atuais | `vault-maui/context-packages/current/` | 6 |
| Template canônico | `vault-maui/context-packages/templates/maui-context-brief.template.md` | — (estrutura) |

## Fontes opcionais

Consultar quando aplicável ao escopo:

| Fonte | Caminho | Quando consultar |
| --- | --- | --- |
| Readiness de context brief | `vault-maui/context-packages/readiness/` | Quando houver readiness relacionado à tarefa |
| Planos | `vault-maui/planos/` | Quando a tarefa for continuidade de plano anterior |
| Adendos | `vault-maui/adendos/` | Quando houver decisão normativa ou exceção citada |
| Insights | `vault-maui/insights/` | Quando houver insights com aplicação ao escopo |
| Painel | `vault-maui/panel/` | Para conferir links de navegação ou estado operacional resumido |
| Context packages arquivados | `vault-maui/context-packages/archive/` | Quando a tarefa envolver histórico documental |

## Fontes defasadas ou com ressalva

| Fonte | Ressalva | Regra de uso |
| --- | --- | --- |
| Roadmap core | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` permanece `status: proposta`. Reconciliação documentada somente até P0.1.13. | Usar apenas como mapa de destino, ordem macro e critérios. Nunca como fonte única de status executado. |
| Handoffs antigos | Podem refletir estado anterior a fases já fechadas. | Usar como histórico. Sempre reconciliar com exec-reports e inventários mais recentes. |
| Memórias sem `deve_ser_considerado_em_context_brief: true` | Podem conter contexto parcial ou desatualizado. | Usar com cautela; confirmar relevância antes de incluir no brief. |
| Históricos e arquivos arquivados | Podem conter caminhos antigos, placeholders e wikilinks obsoletos. | Preservar como histórico. Não normalizar por inferência no brief. |

## Ordem de leitura recomendada

1. `git status --short` e `git log --oneline -20` — confirmar estado do filesystem.
2. Exec-reports mais recentes em `vault-maui/exec-reports/submitted/` — evidência primária de execução.
3. Inventários em `vault-maui/inventarios/` — diagnósticos, pendências e divergências.
4. Memórias em `vault-maui/project-memories/` com `deve_ser_considerado_em_context_brief: true` — sínteses de continuidade.
5. Handoffs em `vault-maui/handoffs/` — transições e decisões humanas recentes.
6. Context briefs em `vault-maui/context-packages/current/` — briefs anteriores relacionados ao escopo.
7. Roadmap e planos — apenas como referência estrutural e mapa de destino.

## Regra de precedência operacional

Em caso de conflito entre fontes:

1. Git local e filesystem verificável.
2. Exec-reports recentes com commit associado.
3. Inventários e registros de normalização.
4. Memórias canônicas marcadas para Context Brief.
5. Handoffs recentes verificáveis.
6. Context briefs atuais.
7. Documentos core (`vault-maui/00_core/`), incluindo roadmap, como contratos e mapa de destino.
8. Arquivos arquivados, históricos, adendos e insights quando aplicáveis.

A fonte de maior precedência vence; declarar quando houver conflito explícito.

## Passo a passo para gerar o brief

### Passo 1 — Confirmar pré-condições

```
git status --short
git log --oneline -20
```

Registrar estado do working tree. Se sujo, documentar quais arquivos estão alterados e por quê.

### Passo 2 — Definir escopo do brief

Confirmar com o usuário ou com o contexto da tarefa:
- Qual é a tarefa ou retomada que o brief deve viabilizar?
- Qual é o executor-alvo (Claude Code, Codex, ChatGPT, Saara)?
- Há restrição de tempo ou de tamanho de contexto?

### Passo 3 — Ler fontes obrigatórias na ordem de precedência

Ler cada fonte e anotar internamente:
- O que está confirmado como fato verificável.
- O que é inferência razoável mas não confirmada por filesystem/hash.
- O que é hipótese ou estimativa ainda não validada.

Não copiar fontes integralmente. Sintetizar apenas o que é materialmente necessário para a tarefa.

### Passo 4 — Identificar lacunas

Para cada fonte obrigatória não consultada, registrar:
- Por quê não foi consultada (não existe, acesso indisponível, fora do escopo).
- Se a ausência bloqueia a geração do brief ou apenas gera ressalva.

### Passo 5 — Preencher o template canônico

Usar `vault-maui/context-packages/templates/maui-context-brief.template.md` como estrutura base. Preencher apenas as seções materialmente relevantes para o escopo. Seções sem conteúdo podem ser omitidas com nota `— não aplicável`.

### Passo 6 — Aplicar regra F/I/H

Em cada seção que declare status operacional ou decisões:
- **F (fato):** verificável por filesystem, commit, exec-report ou documento canônico.
- **I (inferência):** dedução razoável a partir de fatos, mas sem hash/filesystem direto.
- **H (hipótese):** suposição plausível não confirmada.

Nunca elevar inferência ou hipótese a fato sem evidência direta.

### Passo 7 — Aplicar regra `unknown`

Para qualquer executor sem acesso ao filesystem (ex.: ChatGPT via handoff textual):
- Declarar `unknown` para status que dependa de arquivo, hash ou commit não anexado.
- Nunca declarar `current` sem filesystem ou hash verificável.
- Solicitar o menor conjunto de arquivos/anexos quando faltar fonte obrigatória.

### Passo 8 — Validar antes de salvar

Verificar:
- [ ] Frontmatter YAML válido (sem tabs, campos obrigatórios presentes).
- [ ] Seções F/I/H preenchidas onde há status operacional.
- [ ] Lacunas documentais declaradas explicitamente.
- [ ] Nenhuma etapa do roadmap foi executada durante a geração.
- [ ] `Documentação/` e `vault-maui/00_core/` não foram alterados.
- [ ] Roadmap não foi tratado como fonte única de status executado.
- [ ] P0.1.11 preservada como não executada salvo evidência direta em contrário.
- [ ] Instanciação manual Maui não assumida como pronta.
- [ ] Duplicidade verificada: não existe brief do mesmo escopo e data.

### Passo 9 — Salvar e commitar

Salvar em `vault-maui/context-packages/current/` com nome canônico (ver seção abaixo).

Executar:
```
git status --short
git add vault-maui/context-packages/current/<arquivo>.md
git commit -m "context: gera context brief <escopo>"
```

## Template mínimo de saída

```markdown
---
titulo: "Maui Context Brief — <escopo>"
versao: "1.0"
status: ativo
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
tarefa_relacionada: "<fase ou escopo>"
---

# Maui Context Brief — <escopo>

## Finalidade
<uma frase descrevendo a tarefa ou retomada que este brief viabiliza>

## Estado atual conhecido
- Estado:
- Evidências:
- Limites do que foi confirmado:

## Fontes consultadas
| Fonte | Caminho | Observação |
| --- | --- | --- |

## Decisões fechadas relevantes
- Decisão / Fonte / Impacto

## Pendências e bloqueios
- Pendência / Impacto / Menor ação necessária

## O que não assumir
- Lista de assunções que devem ser evitadas

## F/I/H
### Fatos
### Inferências
### Hipóteses

## Próximo passo recomendado
- Próximo passo / Pré-condições / Validações mínimas
```

## Onde salvar o brief

Caminho canônico:
```
vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<escopo>.md
```

Exemplos válidos:
- `2026-05-06-context-brief-pos-p0-1-28-system-prompt.md`
- `2026-05-07-context-brief-retomada-p0-1-29.md`
- `2026-05-07-context-brief-handoff-saara-instanciacao.md`

## Convenção de nome

- Sempre com prefixo de data `YYYY-MM-DD`.
- Prefixo `context-brief-` após a data.
- Escopo em kebab-case, descritivo e rastreável.
- Sem espaços, sem caracteres especiais, sem acentos.

## Regra para evitar duplicidade

Antes de criar um novo brief, verificar:
```
ls vault-maui/context-packages/current/
```
Se já existir brief do mesmo escopo e data, atualizar o existente em vez de criar novo, salvo se os escopos forem materialmente distintos. Registrar a decisão no exec-report.

## Regra para declarar lacunas

Se uma fonte obrigatória não estiver disponível:
1. Declarar a lacuna explicitamente no brief (seção de fontes ou seção de pendências).
2. Explicar o impacto da ausência na confiabilidade do brief.
3. Se a lacuna bloquear a continuidade, solicitar ao usuário o menor conjunto de documentos necessário.
4. Nunca inventar conteúdo para compensar a lacuna.

## Regra `unknown` para instâncias sem hash/filesystem

- Se o executor não tem acesso ao filesystem (ChatGPT via handoff, Claude sem filesystem):
  - Declarar `status: unknown` para qualquer campo que dependa de arquivo ou commit.
  - Nunca escrever `status: current` sem hash ou caminho verificável.
  - Indicar quais fontes precisariam ser anexadas para confirmar o status.

## Regra para não executar etapas futuras

- O brief descreve o estado atual. Não inicia execução de P0.1.X.
- Se o brief recomenda P0.1.29 como próximo passo, isso é recomendação, não execução.
- A execução de qualquer etapa do roadmap requer prompt/tarefa próprio e, quando aplicável, Human Gate.

## Regra para não reabrir `Documentação/`

- `Documentação/` não deve ser lida, alterada ou referenciada durante a geração de um Context Brief sem decisão humana explícita.
- Se houver dúvida sobre conteúdo em `Documentação/`, declarar lacuna e solicitar decisão ao usuário.

## Regra para não usar roadmap como fonte única de status

- O roadmap (`vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`) permanece `status: proposta`.
- Usar o roadmap apenas para: intenção macro, ordem de fases, critérios de entregável, lacunas planejadas.
- Para status de execução, usar sempre exec-reports, inventários e git como fontes primárias.

## F/I/H — Como separar fatos, inferências e hipóteses

| Categoria | Definição | Exemplo |
| --- | --- | --- |
| Fato (F) | Verificável por filesystem, commit, exec-report ou documento canônico com data. | "P0.1.28 criou `vault-maui/00_core/system-prompt-maui.md` (commit baf02e6)." |
| Inferência (I) | Dedução razoável a partir de fatos, mas sem hash/filesystem direto para confirmação. | "P0.1.29 provavelmente é a próxima tarefa por sequência do plano P0.1.25." |
| Hipótese (H) | Suposição plausível não confirmada por nenhuma fonte primária. | "A instanciação manual pode estar pronta se P0.1.11 foi executada fora do registro." |

Regras:
- Nunca promover H para F sem evidência direta.
- Nunca promover I para F sem hash, commit ou filesystem verificável.
- Quando há conflito entre I e F, F vence.
- Sempre declarar a categoria ao fazer afirmação de status operacional.

## Critérios de qualidade

Um Context Brief está pronto quando:

- [ ] Lista todas as fontes consultadas e indica fontes ausentes.
- [ ] Usa exec-reports, inventários, memórias e handoffs antes do roadmap para status executado.
- [ ] Declara roadmap apenas como fonte estrutural/proposta.
- [ ] Separa fatos, inferências e hipóteses explicitamente.
- [ ] Preserva `Documentação/` fora do escopo.
- [ ] Preserva P0.1.11 como não executada salvo evidência direta.
- [ ] Não assume instanciação manual Maui como pronta.
- [ ] Usa `unknown` para qualquer executor sem filesystem/hash verificável.
- [ ] Frontmatter YAML válido.
- [ ] Não é dump integral do corpus.
- [ ] Não executa etapas do roadmap.
- [ ] Não duplica brief existente do mesmo escopo sem justificativa.

## Relação com outros artefatos

- **Template:** `vault-maui/context-packages/templates/maui-context-brief.template.md` — estrutura de preenchimento.
- **Readiness:** `vault-maui/context-packages/readiness/` — define pré-condições e checklist por fase.
- **Skill:** `vault-maui/skills/maui-context-brief/SKILL.md` — instrução compacta para executores.
- **Exec-report:** registrar a criação do brief no exec-report da tarefa que o originou.
- **Memória:** após criar brief significativo, criar memória de marco em `vault-maui/project-memories/`.
