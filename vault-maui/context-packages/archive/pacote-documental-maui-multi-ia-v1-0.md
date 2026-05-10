# Pacote Documental Maui v1.0 — Preparado para Desenvolvimento por Equipe Multi-IA

> Este documento reúne novas versões completas e compatibilizadas dos arquivos alterados/criados para que o projeto Maui possa ser desenvolvido por uma equipe composta por múltiplos modelos de IA em diferentes ferramentas: Claude Code, Google Antigravity, Codex, ChatGPT, Gemini e Claude.
>
> Cada bloco abaixo representa um arquivo Markdown autônomo a ser salvo no `vault-maui/`.

---

# Arquivo 1 — `01_manifest/arquitetura-alvo-maui.md`

---

titulo: Arquitetura Alvo — Maui versao: 1.0 status: proposta data\_criacao: 2026-05-04 idioma: pt-BR tipo: especificacao\_arquitetural escopo: projeto\_maui confidencialidade: interna papel\_primario: ai\_solutions\_architect papeis\_secundarios:

- agent\_engineering
- development\_engineer
- written\_comms\_core
- safe\_agile\_master\_elite precedencia: 5 baseado\_em:
- "[[spec-tecnica-atualizacao-saara-maui-v2]]"
- "[[Handoff — Nova versão do Saara: Maui]]"
- "[[principios-fundacionais]]"
- "[[especificacao-completa]]"
- "[[spec-funcionalidades-maui]]"
- "[[roadmap-desenvolvimento-maui]]" decisoes\_aplicadas:
- "Maui vive em vault-maui/"
- ".maui/ e .saara/ coexistem"
- "Adendos Maui servem apenas ao Maui"
- "Maui inicia em v1.0 com versionamento separado do Saara"
- "hash\_config Maui inclui todo o corpus relevante"
- "Desenvolvimento será realizado por equipe multi-IA com líderes e executores" tags:
- maui
- arquitetura
- corpus-procedural
- multi-ia
- operator-packs
- claude-code
- codex
- antigravity
- chatgpt
- gemini
- claude

---

# Arquitetura Alvo — Maui

## 1. Resumo executivo

Maui é a nova arquitetura de evolução do Saara. Maui não é aplicação, backend, chatbot, MCP server ou interface específica. Maui é um **corpus cognitivo multipapel, procedural, portátil e instanciável por diferentes modelos e ferramentas de IA**.

A identidade, governança, comportamento, memória e capacidades operacionais do Maui vivem no corpus versionado. Infraestruturas como toolkit, painel, scripts, MCP servers, adapters, bancos locais, integrações e modelos específicos são mecanismos auxiliares e substituíveis.

A arquitetura Maui deve ser desenvolvida por uma **equipe multi-IA**, composta por:

- modelos executores com acesso a filesystem e capacidade de implementação;
- modelos líderes/técnicos responsáveis por coordenação, revisão, decomposição e handoff;
- artefatos estruturados para comunicação entre instâncias;
- contratos de saída e validação comuns.

## 2. Decisão arquitetural principal

```text
Produto principal = Maui Corpus
Ferramentas auxiliares = Maui Toolkit + scripts + painel + operadores + MCP servers
Equipe de execução = múltiplas IAs coordenadas por contratos e handoffs
```

O antigo `saara-core` deixa de ser interpretado como centro do produto. Ele pode evoluir para Maui Toolkit, com responsabilidade de bootstrap, instanciação, validação, curadoria e distribuição, mas não define a identidade do Maui.

## 3. Equação Maui v1.0

```text
Maui = corpus
     + memória + PKAs + specs + adendos + insights
     + skills + procedures + reflexes + scripts
     + hooks + subagents + plugins
     + schemas + evals + automations
     + operator-packs + mcp-servers
     + context-packages + exec-requests/reports
     + painel de curadoria multi-IA
     + contratos de coordenação entre modelos
```

## 4. Objetivos da arquitetura

1. Tornar Maui instanciável em diferentes ferramentas de IA sem depender de backend único.
2. Permitir desenvolvimento por equipe multi-IA com papéis claros.
3. Transformar capacidades operacionais em artefatos versionados no corpus.
4. Separar produto, toolkit, operadores e ferramentas líderes.
5. Preservar compatibilidade conceitual com Saara v7.1.1 sem colapsar versionamento.
6. Adotar padrões abertos: Agent Skills, `AGENTS.md`, hooks lifecycle, subagents, plugins e MCP.
7. Garantir evolução governada via memória, adendos, insights, evals e Human Gate.
8. Manter portabilidade, auditabilidade, idempotência, reversibilidade e clareza cross-tool.

## 5. Princípios arquiteturais

### 5.1 Soberania cognitiva ampliada

A identidade do Maui vive no corpus. Código, bancos, servidores, modelos e integrações são substituíveis.

### 5.2 Padrão aberto por default

Maui adota convenções abertas quando elas não violam a soberania do corpus:

- `SKILL.md` com frontmatter;
- `AGENTS.md` para agentes de codificação;
- `CLAUDE.md` para Claude Code;
- MCP como protocolo de exposição;
- plugins como bundles versionados;
- hooks lifecycle para enforcement determinístico;
- evals como código;
- context engineering como disciplina operacional.

### 5.3 Desenvolvimento por contratos, não por memória implícita

Toda IA participante deve receber:

- papel;
- escopo;
- input contract;
- output contract;
- Definition of Ready;
- Definition of Done;
- ferramentas permitidas;
- limites de escrita;
- formato de report.

### 5.4 Determinismo onde possível

Regras críticas devem ser implementadas por schemas, validações, scripts, hooks, testes/evals e contratos, não apenas por prompt.

### 5.5 Read-only antes de write

Em P0, modelos devem priorizar leitura, análise, validação e geração de patches/reports. Escrita persistente exige autorização explícita ou contexto operacional aprovado.

## 6. Camadas arquiteturais

```text
┌────────────────────────────────────────────────────────────┐
│ Camada 1 — Cognitiva                                       │
│ 00_core/ · 01_manifest/ · memoria/ · adendos/ · insights/ │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 2 — Procedural                                      │
│ skills/ · procedures/ · reflexes/ · scripts/               │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 3 — Execução                                        │
│ hooks/ · subagents/ · plugins/                             │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 4 — Qualidade                                       │
│ schemas/ · evals/ · validations/ · automations/            │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 5 — Adaptação                                       │
│ operator-packs/ · mcp-servers/ · adapters/                 │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 6 — Comunicação                                     │
│ context-packages/ · exec-requests/ · exec-reports/ exports/│
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 7 — Coordenação Multi-IA                            │
│ panel/ · task-briefs/ · review-reports/ · decision-log/    │
└────────────────────────────────────────────────────────────┘
```

## 7. Topologia multi-IA

```text
                         ┌─────────────────────────────┐
                         │ Líder Técnico / Coordenação │
                         │ ChatGPT · Gemini · Claude   │
                         └──────────────┬──────────────┘
                                        │ task briefs / review
                                        ▼
┌────────────────────┐ filesystem ┌──────────────────────┐ filesystem ┌────────────────────┐
│ Claude Code        │───────────▶│     vault-maui/      │◀───────────│ Codex              │
│ Executor           │            │      corpus          │            │ Executor           │
└────────────────────┘            └──────────┬───────────┘            └────────────────────┘
                                             │
                                             │ filesystem/API quando disponível
                                             ▼
                                   ┌────────────────────┐
                                   │ Google Antigravity │
                                   │ Executor/Explorador│
                                   └────────────────────┘

┌────────────────────┐ handoff/context ┌──────────────────────┐ handoff/context ┌────────────────────┐
│ ChatGPT            │────────────────▶│ exec-requests/reports│◀────────────────│ Gemini / Claude    │
│ Líder ou instância │                 │ panel/decisions      │                 │ Líder/Revisor      │
└────────────────────┘                 └──────────────────────┘                 └────────────────────┘
```

## 8. Papéis por ferramenta

| Ferramenta         | Papel primário                         | Papel secundário                            | Escrita direta no corpus | Modo P0                     |
| ------------------ | -------------------------------------- | ------------------------------------------- | ------------------------ | --------------------------- |
| Claude Code        | Executor filesystem                    | Implementação, scripts, validações, patches | Sim, quando autorizado   | Operator pack + `CLAUDE.md` |
| Codex              | Executor filesystem                    | Implementação, refatoração, testes          | Sim, quando autorizado   | Operator pack + `AGENTS.md` |
| Google Antigravity | Executor/explorador                    | Protótipos, validações, integrações         | Condicional              | Operator pack próprio       |
| ChatGPT            | Líder técnico / PM técnico / arquiteto | Decomposição, revisão, handoff, decisões    | Não no P0                | Context package + handoff   |
| Gemini             | Líder/revisor/analista                 | Revisão ampla, alternativas, documentação   | Não no P0                | Context package + handoff   |
| Claude             | Líder/revisor/agent engineer           | Revisão de specs, prompts, governança       | Não no P0                | Context package + handoff   |

## 9. Componentes principais

### 9.1 Maui Corpus

Produto principal. Fonte de verdade de identidade, comportamento, memória, governança, procedimentos e capacidades operacionais.

### 9.2 Maui Toolkit

Conjunto auxiliar para operar o corpus. Não é o produto.

Responsabilidades:

- criar estrutura inicial;
- gerar templates;
- instanciar Maui em ferramentas-alvo;
- preparar operator packs;
- executar validações;
- oferecer painel de curadoria;
- expor capacidades via CLI, filesystem, MCP ou REST quando aplicável.

### 9.3 Scripts de condicionamento

Scripts versionados no corpus que executam operações determinísticas e primitivas.

P0:

```text
scripts/maui_vault_health.py
scripts/maui_validate_frontmatter.py
scripts/maui_validate_links.py
scripts/maui_context_export.py
scripts/maui_registry.py
scripts/maui_update_export.py
scripts/maui_memory_index.py
```

### 9.4 Operator packs

Pacotes de adaptação por ferramenta.

P0:

```text
operator-packs/claude-code/
operator-packs/codex/
operator-packs/chatgpt-handoff/
```

P1/P2:

```text
operator-packs/gemini/
operator-packs/claude/
operator-packs/antigravity/
operator-packs/chatgpt-action/
```

### 9.5 Exec requests/reports

Arquivos estruturados para comunicação entre líderes e executores.

Fluxo:

```text
Task Brief / Exec Request
→ execução por Claude Code/Codex/Antigravity
→ Exec Report
→ revisão por ChatGPT/Gemini/Claude
→ decisão humana ou nova tarefa
```

## 10. Estrutura física alvo

```text
vault-maui/
├── 00_core/
├── 01_manifest/
├── memoria/
├── adendos/
├── insights/
├── skills/
├── procedures/
├── reflexes/
├── scripts/
├── hooks/
├── subagents/
├── plugins/
├── schemas/
├── evals/
├── automations/
├── validations/
├── operator-packs/
│   ├── claude-code/
│   ├── codex/
│   ├── antigravity/
│   ├── chatgpt-handoff/
│   ├── chatgpt-action/
│   ├── gemini/
│   └── claude/
├── mcp-servers/
├── context-packages/
│   ├── current/
│   ├── targets/
│   └── generated/
├── exec-requests/
│   ├── templates/
│   ├── backlog/
│   ├── assigned/
│   └── examples/
├── exec-reports/
│   ├── templates/
│   ├── submitted/
│   ├── reviewed/
│   └── examples/
├── panel/
│   ├── dashboard.md
│   ├── task-board.md
│   ├── decisions/
│   └── reviews/
└── exports/
```

## 11. Decisões de adequação documental Saara → Maui

| Tema                    | Decisão                                                    |
| ----------------------- | ---------------------------------------------------------- |
| Diretório final         | Maui vive em `vault-maui/`                                 |
| Coexistência técnica    | `.maui/` e `.saara/` coexistem                             |
| Escopo dos adendos Maui | Adendos Maui servem apenas ao Maui                         |
| Versionamento           | Maui inicia em `v1.0`; Saara mantém versionamento separado |
| `hash_config`           | Inclui todo o corpus Maui relevante                        |

## 12. Hashes de conformidade

```text
hash_config_core       = 00_core/ + princípios + PKAs + specs normativas
hash_operational       = scripts/ + skills/ + procedures/ + hooks/ + subagents/
hash_context           = operator-packs/ + context-packages/ + templates
hash_quality           = schemas/ + evals/ + validations relevantes
hash_full              = composição total relevante do corpus Maui
```

Instância sem filesystem ou endpoint autenticado deve declarar `unknown`, nunca `current`.

## 13. Contrato de operação multi-IA

Todo trabalho atribuído a uma IA deve ter:

```yaml
task_id: string
titulo: string
fase: P0.0 | P0.1 | P0.2 | P0.3 | P0.4 | P0.5 | P0.6 | P0.7 | P0.8 | P0.9 | P1 | P2
papel_requerido: leader | executor | reviewer | curator
ferramenta_alvo: claude-code | codex | antigravity | chatgpt | gemini | claude
entrada:
  - arquivos
  - contexto
saida_esperada:
  - patch
  - markdown
  - json
  - report
permissoes:
  filesystem_read: true
  filesystem_write: false
human_gate: false
criterios_de_aceite:
  - string
```

## 14. Riscos e controles

| Risco                                                       | Severidade | Controle                                      |
| ----------------------------------------------------------- | ---------- | --------------------------------------------- |
| Modelos diferentes interpretarem escopo de forma divergente | Alta       | Task Brief + Output Contract + Exec Report    |
| Executor alterar corpus sem autorização                     | Alta       | Read-only por default + Human Gate            |
| Líder conversacional presumir hash/conformidade             | Alta       | Estado `unknown` obrigatório sem filesystem   |
| Duplicidade de tarefas entre modelos                        | Média      | Painel e task board                           |
| Perda de contexto entre ferramentas                         | Alta       | Context package por target + handoff protocol |
| Revisão superficial por modelo único                        | Média      | Separar executor e reviewer                   |
| Antigravity/Codex/Claude Code divergirem em convenções      | Média      | Operator packs por ferramenta                 |

## 15. Critérios de aceite da arquitetura multi-IA

- Cada ferramenta tem papel definido.
- Ferramentas executoras recebem operator pack próprio.
- Ferramentas líderes recebem context package e protocolo de handoff.
- Toda tarefa executável passa por Exec Request.
- Toda execução gera Exec Report.
- Mudança normativa exige Human Gate.
- Instâncias sem filesystem declaram `unknown`.
- P0 funciona sem MCP, REST ou UI.

---

# Arquivo 2 — `01_manifest/spec-funcionalidades-maui.md`

---

titulo: Spec Unificada — Funcionalidades Maui versao: 1.0 status: proposta data\_criacao: 2026-05-04 idioma: pt-BR tipo: especificacao\_funcional\_unificada escopo: projeto\_maui confidencialidade: interna papel\_primario: ai\_solutions\_architect papeis\_secundarios:

- agent\_engineering
- development\_engineer
- written\_comms\_core
- safe\_agile\_master\_elite precedencia: 5 baseado\_em:
- "[[arquitetura-alvo-maui]]"
- "[[roadmap-desenvolvimento-maui]]"
- "[[modelo-operacional-time-multi-ia]]"
- "[[spec-tecnica-atualizacao-saara-maui-v2]]"
- "[[Handoff — Nova versão do Saara: Maui]]" decisoes\_aplicadas:
- "Maui vive em vault-maui/"
- ".maui/ e .saara/ coexistem"
- "Adendos Maui servem apenas ao Maui"
- "Maui inicia em v1.0 com versionamento separado do Saara"
- "hash\_config Maui inclui todo o corpus relevante"
- "Desenvolvimento será executado por equipe multi-IA" tags:
- maui
- especificacao-unificada
- funcionalidades
- multi-ia
- operator-packs
- update-protocol

---

# Spec Unificada — Funcionalidades Maui

## 1. Finalidade

Este documento consolida as funcionalidades do Maui v1.0 para desenvolvimento por equipe multi-IA. Cada funcionalidade deve ser compreensível por modelos executores e líderes em diferentes ferramentas.

Maui é corpus-first:

```text
Produto principal = Maui Corpus
Execução = scripts + skills + procedures + operator packs
Coordenação = task briefs + exec requests + exec reports + painel
Ferramentas = substituíveis
```

## 2. Funcionalidades P0

### 2.1 Maui Corpus

Responsabilidade: fonte de verdade de identidade, governança, memória, procedimentos e capacidades.

Atividades P0:

- criar `vault-maui/`;
- criar `01_manifest/`;
- salvar arquitetura, spec funcional, roadmap e modelo operacional multi-IA;
- definir frontmatter comum;
- registrar decisões Saara → Maui.

Output esperado:

```text
01_manifest/arquitetura-alvo-maui.md
01_manifest/spec-funcionalidades-maui.md
01_manifest/roadmap-desenvolvimento-maui.md
01_manifest/modelo-operacional-time-multi-ia.md
```

### 2.2 Schemas mínimos

Responsabilidade: garantir contratos antes de código.

Schemas P0:

```text
schemas/common-frontmatter.schema.yaml
schemas/registry.schema.yaml
schemas/context-package.schema.yaml
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
schemas/skill.schema.yaml
schemas/operator-pack.schema.yaml
schemas/exec-request.schema.yaml
schemas/exec-report.schema.yaml
```

### 2.3 Scripts P0

Responsabilidade: camada executável mínima, local-first e read-only por default.

Scripts:

```text
scripts/maui_vault_health.py
scripts/maui_validate_frontmatter.py
scripts/maui_validate_links.py
scripts/maui_context_export.py
scripts/maui_registry.py
scripts/maui_update_export.py
scripts/maui_memory_index.py
```

Contrato mínimo:

```bash
--help
--dry-run
--format markdown|json
--out PATH
```

Scripts que escrevem exigem:

```bash
--write
--force
--backup
```

### 2.4 Operator packs P0

Responsabilidade: adaptar Maui para cada ferramenta.

P0:

```text
operator-packs/claude-code/
operator-packs/codex/
operator-packs/chatgpt-handoff/
```

P1/P2:

```text
operator-packs/antigravity/
operator-packs/gemini/
operator-packs/claude/
operator-packs/chatgpt-action/
```

### 2.5 Context packages

Responsabilidade: fornecer contexto mínimo, específico por target.

P0:

```text
context-packages/current/maui-bootstrap.md
context-packages/targets/claude-code.md
context-packages/targets/codex.md
context-packages/targets/chatgpt-handoff.md
```

P1:

```text
context-packages/targets/antigravity.md
context-packages/targets/gemini.md
context-packages/targets/claude.md
```

### 2.6 Update Protocol

Responsabilidade: permitir atualização entre instâncias com e sem filesystem.

Fluxo:

```text
Update Request → Update Package → Update Report
```

Instância sem filesystem gera Update Request e declara `unknown`.

### 2.7 Skills P0

Responsabilidade: tornar operações reutilizáveis por agentes de codificação.

Skills P0:

```text
skills/maui-vault-health/SKILL.md
skills/maui-frontmatter-validate/SKILL.md
skills/maui-context-export/SKILL.md
skills/maui-update-export/SKILL.md
skills/maui-doc-consistency-check/SKILL.md
skills/maui-registry-maintenance/SKILL.md
skills/maui-memory-maintenance/SKILL.md
```

### 2.8 Procedures e reflexes P0

Responsabilidade: operação manual e semiassistida segura.

Procedures P0:

```text
procedures/procedimento-validar-vault.md
procedures/procedimento-exportar-contexto.md
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
procedures/procedimento-criar-operator-pack.md
procedures/procedimento-captura-explicita.md
```

Reflexes P0:

```text
reflexes/reflexo-se-frontmatter-invalido.md
reflexes/reflexo-se-falta-contexto.md
reflexes/reflexo-se-instancia-pede-update.md
reflexes/reflexo-se-escrita-persistente.md
reflexes/reflexo-se-plugin-externo.md
```

### 2.9 Evals e smoke tests P0

Responsabilidade: garantir que primeiro uso real não quebre.

Evals P0:

```text
evals/regression/corpus-integrity.eval.yaml
evals/scripts/maui-vault-health.eval.yaml
evals/update-protocol/request-package-report.eval.yaml
evals/operator-packs/claude-code-pack.eval.yaml
evals/operator-packs/codex-pack.eval.yaml
evals/operator-packs/chatgpt-handoff-pack.eval.yaml
evals/context-packages/bootstrap-context.eval.yaml
```

### 2.10 Memória e curadoria file-based

Responsabilidade: registrar decisões, reports e aprendizado do piloto.

P0:

```text
memoria/templates/decisao-template.md
panel/dashboard.md
panel/task-board.md
panel/decisions/
panel/reviews/
exec-reports/submitted/
exec-reports/reviewed/
```

## 3. Funcionalidades P1

### 3.1 Hooks

- `session-start/check-instance-status`
- `pre-write/guard-corpus-write`
- `post-write/validate-frontmatter`
- `post-write/validate-links`
- `on-export/validate-update-package`

### 3.2 Subagentes

- `maui-doc-reviewer`
- `maui-schema-validator`
- `maui-context-compressor`
- `maui-update-planner`
- `maui-security-reviewer`

### 3.3 Painel CLI completo

- `maui panel status`
- `maui panel dispatch`
- `maui panel collect`
- `maui panel record-decision`
- `maui panel review`

### 3.4 MCP read-only

- `maui.corpus.search`
- `maui.corpus.read`
- `maui.context.export`
- `maui.registry.status`

## 4. Funcionalidades P2

- plugins internos;
- automations read-only;
- MCP guarded-write;
- REST/Action para ChatGPT;
- UI do painel;
- busca vetorial;
- integração avançada com Antigravity, Gemini e Claude.

## 5. Contratos para equipe multi-IA

### 5.1 Exec Request

```yaml
request_id: string
titulo: string
fase: string
funcionalidade: string
papel_requerido: executor | reviewer | leader | curator
ferramenta_preferida: claude-code | codex | antigravity | chatgpt | gemini | claude
contexto:
  - arquivo
  - referencia
entrada:
  - item
saida_esperada:
  - artifact
permissoes:
  read: true
  write: false
human_gate: false
criterios_de_aceite:
  - string
```

### 5.2 Exec Report

```yaml
report_id: string
request_id: string
executor: string
ferramenta: string
status: success | partial | failed
arquivos_lidos: []
arquivos_alterados: []
artefatos_gerados: []
validacoes_executadas: []
riscos: []
pendencias: []
requer_human_gate: false
```

### 5.3 Review Report

```yaml
review_id: string
report_id: string
reviewer: string
status: approved | changes_requested | rejected
findings:
  - severidade: low | medium | high | critical
    descricao: string
    recomendacao: string
decisao_recomendada: string
```

## 6. Regras por ferramenta

### 6.1 Claude Code

Uso principal: implementação com filesystem.

Deve receber:

```text
operator-packs/claude-code/CLAUDE.md.template
context-packages/targets/claude-code.md
skills/*/SKILL.md
exec-requests/assigned/*.md
```

Deve produzir:

```text
patches ou arquivos alterados
exec-reports/submitted/*.md
validations/*.md
```

### 6.2 Codex

Uso principal: implementação com filesystem e `AGENTS.md`.

Deve receber:

```text
operator-packs/codex/AGENTS.md.template
context-packages/targets/codex.md
exec-requests/assigned/*.md
```

Deve produzir:

```text
patches
exec-reports/submitted/*.md
```

### 6.3 Google Antigravity

Uso principal: exploração, protótipos, validação cross-tool e integração quando filesystem/API estiver disponível.

Deve receber:

```text
operator-packs/antigravity/pack.yaml
context-packages/targets/antigravity.md
exec-requests/assigned/*.md
```

### 6.4 ChatGPT

Uso principal: líder técnico, decomposição de tarefas, revisão, geração de handoffs e acompanhamento.

Não deve presumir filesystem. Deve operar por:

```text
context-packages/targets/chatgpt-handoff.md
exec-requests/templates/*.md
exec-reports/submitted/*.md
panel/dashboard.md
```

### 6.5 Gemini

Uso principal: revisão ampla, análise de alternativas, crítica arquitetural e documentação.

### 6.6 Claude

Uso principal: revisão de agent engineering, prompts, specs, governança e consistência textual.

## 7. Definition of Ready

Uma tarefa está pronta para execução quando:

- tem `request_id`;
- tem ferramenta preferida;
- tem escopo claro;
- tem arquivos de entrada;
- tem saída esperada;
- tem permissões declaradas;
- tem critérios de aceite;
- indica se exige Human Gate.

## 8. Definition of Done

Uma tarefa está concluída quando:

- entregável foi produzido;
- exec report foi gerado;
- validações aplicáveis foram executadas;
- riscos foram declarados;
- pendências foram listadas;
- reviewer aprovou ou solicitou mudanças;
- decisão humana foi registrada quando exigida.

## 9. Critérios de aceite globais

- Documentos são compreensíveis por modelos sem memória prévia da conversa.
- Cada ferramenta sabe seu papel.
- Cada executor sabe onde ler, onde escrever e o que reportar.
- Líderes conseguem decompor, revisar e acompanhar tarefas.
- P0 não depende de MCP/REST/UI.
- Nenhuma instância sem filesystem declara conformidade plena.

---

# Arquivo 3 — `01_manifest/roadmap-desenvolvimento-maui.md`

---

titulo: Roadmap de Desenvolvimento — Maui versao: 1.0 status: proposta data\_criacao: 2026-05-04 idioma: pt-BR tipo: roadmap\_desenvolvimento escopo: projeto\_maui confidencialidade: interna papel\_primario: ai\_solutions\_architect papeis\_secundarios:

- agent\_engineering
- development\_engineer
- written\_comms\_core
- safe\_agile\_master\_elite precedencia: 5 baseado\_em:
- "[[arquitetura-alvo-maui]]"
- "[[spec-funcionalidades-maui]]"
- "[[modelo-operacional-time-multi-ia]]"
- "[[spec-tecnica-atualizacao-saara-maui-v2]]"
- "[[Handoff — Nova versão do Saara: Maui]]" decisoes\_aplicadas:
- "Maui vive em vault-maui/"
- ".maui/ e .saara/ coexistem"
- "Adendos Maui servem apenas ao Maui"
- "Maui inicia em v1.0 com versionamento separado do Saara"
- "hash\_config Maui inclui todo o corpus relevante"
- "Roadmap organizado para execução por equipe multi-IA" tags:
- maui
- roadmap
- desenvolvimento
- multi-ia
- priorizacao
- p0
- p1
- p2

---

# Roadmap de Desenvolvimento — Maui

## 1. Objetivo

Definir o roadmap de desenvolvimento do Maui v1.0, quebrado por funcionalidade, atividades e responsáveis por tipo de ferramenta/modelo de IA.

O roadmap é orientado ao **mínimo Maui utilizável com segurança** e preparado para execução por equipe multi-IA.

## 2. Papéis de execução

| Papel               | Ferramentas típicas             | Responsabilidade                                              |
| ------------------- | ------------------------------- | ------------------------------------------------------------- |
| Líder técnico       | ChatGPT, Gemini, Claude         | decompor tarefas, revisar reports, manter alinhamento         |
| Executor filesystem | Claude Code, Codex, Antigravity | implementar arquivos, scripts, schemas, operator packs        |
| Reviewer            | Claude, Gemini, ChatGPT         | revisar coerência, riscos, critérios de aceite                |
| Curador             | ChatGPT, Claude, Gemini         | registrar decisões, consolidar handoffs, atualizar painel     |
| Human Gate          | humano responsável              | aprovar mudanças normativas, escrita crítica e avanço de fase |

## 3. Sequência de desenvolvimento

```text
P0.0 — Formalização do corpus e estrutura mínima
P0.1 — Schemas mínimos e validação local
P0.2 — Scripts P0 de bootstrap, validação e contexto
P0.3 — Operator packs iniciais: Claude Code, Codex e ChatGPT Handoff
P0.4 — Context package inicial e protocolo de handoff
P0.5 — Update Protocol mínimo
P0.6 — Skills P0 para agentes de codificação
P0.7 — Procedures P0 e reflexes críticos
P0.8 — Evals/smoke tests mínimos
P0.9 — Registro de decisão, memória mínima e curadoria file-based
P1   — Hooks, subagentes, painel CLI completo, MCP read-only
P2   — Plugins, automations, MCP guarded-write, REST/Action e UI
```

## 4. P0.0 — Fundação documental

### Objetivo

Criar a estrutura inicial e documentos-base do Maui.

### Atividades

| ID      | Atividade                          | Executor recomendado | Reviewer       | Entregável                                        |
| ------- | ---------------------------------- | -------------------- | -------------- | ------------------------------------------------- |
| P0.0-A1 | Criar árvore `vault-maui/`         | Claude Code ou Codex | ChatGPT/Claude | diretórios                                        |
| P0.0-A2 | Criar `.maui/` mantendo `.saara/`  | Claude Code          | ChatGPT        | `.maui/README.md`                                 |
| P0.0-A3 | Salvar arquitetura alvo            | ChatGPT/Claude       | Gemini         | `01_manifest/arquitetura-alvo-maui.md`            |
| P0.0-A4 | Salvar spec funcional              | ChatGPT/Claude       | Gemini         | `01_manifest/spec-funcionalidades-maui.md`        |
| P0.0-A5 | Salvar modelo operacional multi-IA | ChatGPT              | Claude/Gemini  | `01_manifest/modelo-operacional-time-multi-ia.md` |
| P0.0-A6 | Salvar roadmap                     | ChatGPT              | Claude/Gemini  | `01_manifest/roadmap-desenvolvimento-maui.md`     |

### Definition of Done

- Estrutura mínima criada.
- Documentos-base salvos.
- `.maui/` e `.saara/` coexistem.
- Decisões Saara → Maui registradas.

## 5. P0.1 — Schemas mínimos

### Objetivo

Criar contratos verificáveis antes da implementação.

### Atividades

| ID      | Atividade                                   | Executor recomendado | Reviewer      | Entregável                                                       |
| ------- | ------------------------------------------- | -------------------- | ------------- | ---------------------------------------------------------------- |
| P0.1-A1 | Criar schema comum de frontmatter           | Codex                | Claude        | `schemas/common-frontmatter.schema.yaml`                         |
| P0.1-A2 | Criar schema de registry                    | Codex                | Claude Code   | `schemas/registry.schema.yaml`                                   |
| P0.1-A3 | Criar schema de context package             | Codex                | ChatGPT       | `schemas/context-package.schema.yaml`                            |
| P0.1-A4 | Criar schemas Update Request/Package/Report | Codex                | Claude/Gemini | `schemas/update-*.schema.yaml`                                   |
| P0.1-A5 | Criar schemas Exec Request/Report           | Codex                | ChatGPT       | `schemas/exec-*.schema.yaml`                                     |
| P0.1-A6 | Criar schema de skill e operator pack       | Codex                | Claude Code   | `schemas/skill.schema.yaml`, `schemas/operator-pack.schema.yaml` |
| P0.1-A7 | Criar fixtures válidas/inválidas            | Claude Code          | Codex         | `schemas/fixtures/`                                              |

### Definition of Done

- Schemas P0 existem.
- Fixtures existem.
- Falhas críticas são classificadas.
- Exec Request/Report está pronto para coordenar equipe multi-IA.

## 6. P0.2 — Scripts P0

### Objetivo

Criar primeira camada executável local-first.

**Status pós-P0.2:** Implementado em 2026-05-10 (`6c5c2c7` · `p0.2-complete`).

### Atividades

| ID      | Atividade                                  | Executor recomendado | Reviewer       | Entregável                 |
| ------- | ------------------------------------------ | -------------------- | -------------- | -------------------------- |
| P0.2-A1 | Implementar `maui_vault_health.py`         | Claude Code          | Codex          | script + relatório exemplo |
| P0.2-A2 | Implementar `maui_validate_frontmatter.py` | Codex                | Claude Code    | script                     |
| P0.2-A3 | Implementar `maui_validate_links.py`       | Codex                | Claude Code    | script                     |
| P0.2-A4 | Implementar `maui_context_export.py`       | Claude Code          | ChatGPT/Claude | script + examples          |
| P0.2-A5 | Implementar `maui_registry.py`             | Claude Code          | Codex          | script + snapshot exemplo  |
| P0.2-A6 | Implementar `maui_update_export.py`        | Claude Code          | ChatGPT/Claude | script + package exemplo   |
| P0.2-A7 | Implementar `maui_memory_index.py`         | Codex                | Claude Code    | script + índice exemplo    |

### Regras

- Todos os scripts suportam `--help`, `--dry-run`, `--format markdown|json`.
- Escrita exige `--write` ou flag equivalente.
- Nenhum script escreve fora do escopo permitido.

## 7. P0.3 — Operator packs iniciais

### Objetivo

Permitir que os modelos executores e líderes operem Maui corretamente.

### Atividades

| ID      | Atividade                      | Executor recomendado | Reviewer       | Entregável                        |
| ------- | ------------------------------ | -------------------- | -------------- | --------------------------------- |
| P0.3-A1 | Criar Claude Code pack         | Claude Code          | ChatGPT/Claude | `operator-packs/claude-code/`     |
| P0.3-A2 | Criar Codex pack               | Codex                | Claude Code    | `operator-packs/codex/`           |
| P0.3-A3 | Criar ChatGPT Handoff pack     | ChatGPT              | Claude/Gemini  | `operator-packs/chatgpt-handoff/` |
| P0.3-A4 | Criar Antigravity pack inicial | Antigravity ou Codex | ChatGPT        | `operator-packs/antigravity/`     |
| P0.3-A5 | Criar Gemini leader pack       | Gemini/ChatGPT       | Claude         | `operator-packs/gemini/`          |
| P0.3-A6 | Criar Claude leader pack       | Claude/ChatGPT       | Gemini         | `operator-packs/claude/`          |

### Priorização

P0 obrigatório:

```text
claude-code
codex
chatgpt-handoff
```

P0 estendido/P1:

```text
antigravity
gemini
claude
```

## 8. P0.4 — Context packages e handoff

### Objetivo

Dar a cada ferramenta o contexto certo, sem carregar todo o corpus.

### Atividades

| ID      | Atividade                    | Executor recomendado | Reviewer      | Entregável                                    |
| ------- | ---------------------------- | -------------------- | ------------- | --------------------------------------------- |
| P0.4-A1 | Criar bootstrap              | ChatGPT              | Claude/Gemini | `context-packages/current/maui-bootstrap.md`  |
| P0.4-A2 | Criar target Claude Code     | Claude Code          | ChatGPT       | `context-packages/targets/claude-code.md`     |
| P0.4-A3 | Criar target Codex           | Codex                | ChatGPT       | `context-packages/targets/codex.md`           |
| P0.4-A4 | Criar target ChatGPT Handoff | ChatGPT              | Claude        | `context-packages/targets/chatgpt-handoff.md` |
| P0.4-A5 | Criar target Gemini          | Gemini/ChatGPT       | Claude        | `context-packages/targets/gemini.md`          |
| P0.4-A6 | Criar target Claude          | Claude/ChatGPT       | Gemini        | `context-packages/targets/claude.md`          |
| P0.4-A7 | Criar target Antigravity     | Antigravity/Codex    | ChatGPT       | `context-packages/targets/antigravity.md`     |

## 9. P0.5 — Update Protocol mínimo

### Objetivo

Fechar o ciclo de atualização entre líderes, executores e instâncias.

### Atividades

| ID      | Atividade                     | Executor recomendado | Reviewer       | Entregável                                           |
| ------- | ----------------------------- | -------------------- | -------------- | ---------------------------------------------------- |
| P0.5-A1 | Criar template Update Request | ChatGPT              | Claude         | `exec-requests/templates/update-request-template.md` |
| P0.5-A2 | Criar template Update Package | ChatGPT/Codex        | Claude         | `exports/templates/update-package-template.md`       |
| P0.5-A3 | Criar template Update Report  | ChatGPT              | Gemini         | `exec-reports/templates/update-report-template.md`   |
| P0.5-A4 | Criar examples                | Claude Code/Codex    | ChatGPT        | examples                                             |
| P0.5-A5 | Testar fluxo ponta a ponta    | Claude Code          | ChatGPT/Claude | exec report                                          |

## 10. P0.6 — Skills P0

### Objetivo

Padronizar capacidades de execução para Claude Code, Codex e Antigravity.

### Atividades

| ID      | Skill                        | Executor recomendado | Reviewer       |
| ------- | ---------------------------- | -------------------- | -------------- |
| P0.6-A1 | `maui-vault-health`          | Claude Code          | Codex          |
| P0.6-A2 | `maui-frontmatter-validate`  | Codex                | Claude Code    |
| P0.6-A3 | `maui-context-export`        | Claude Code          | ChatGPT        |
| P0.6-A4 | `maui-update-export`         | Claude Code          | Claude         |
| P0.6-A5 | `maui-doc-consistency-check` | Claude               | ChatGPT/Gemini |
| P0.6-A6 | `maui-registry-maintenance`  | Codex                | Claude Code    |
| P0.6-A7 | `maui-memory-maintenance`    | Codex                | Claude         |

## 11. P0.7 — Procedures e reflexes

### Objetivo

Garantir operação manual/semiassistida por qualquer modelo.

Atividades:

- criar procedure validar vault;
- criar procedure exportar contexto;
- criar procedure verificar atualizações;
- criar procedure integrar atualização;
- criar procedure criar operator pack;
- criar procedure captura explícita;
- criar reflexes críticos.

Reviewer recomendado: Claude ou ChatGPT para consistência; Gemini para crítica ampla.

## 12. P0.8 — Evals e smoke tests

### Objetivo

Permitir avanço para piloto com segurança.

Atividades:

- eval de integridade do corpus;
- eval de `maui_vault_health.py`;
- eval de Update Protocol;
- eval de operator packs;
- eval de context package bootstrap.

Executor recomendado: Codex/Claude Code. Reviewer recomendado: ChatGPT/Claude.

## 13. P0.9 — Memória, decisão e painel file-based

### Objetivo

Dar rastreabilidade mínima ao piloto multi-IA.

Atividades:

- criar template de decisão;
- criar dashboard;
- criar task board;
- criar diretórios de reports;
- registrar primeira decisão Maui v1.0;
- registrar exec reports do piloto.

## 14. P1 — Expansão controlada

Funcionalidades:

- hooks;
- subagentes;
- painel CLI;
- MCP read-only;
- operator packs completos para Antigravity, Gemini e Claude.

Entrada em P1 exige:

- P0.0 a P0.8 completos;
- piloto Claude Code ou Codex executado;
- Update Protocol testado;
- health check sem falhas críticas.

## 15. P2 — Integração avançada

Funcionalidades:

- plugins;
- automations;
- MCP guarded-write;
- ChatGPT Action/REST;
- UI do painel;
- busca vetorial;
- integração avançada multi-ferramenta.

## 16. Marco de primeiro uso real

O Maui está pronto para primeiro uso real quando:

1. `vault-maui/` existe.
2. Documentos-base existem em `01_manifest/`.
3. `maui_vault_health.py` roda sem falhas críticas.
4. Existe context package bootstrap.
5. Existe operator pack Claude Code ou Codex.
6. Existe ChatGPT Handoff pack.
7. Existe schema e exemplo para Update Request/Package/Report.
8. Existe schema e exemplo para Exec Request/Report.
9. Existe forma de registrar exec report.
10. Mudanças normativas continuam protegidas por Human Gate.

---

# Arquivo 4 — `01_manifest/modelo-operacional-time-multi-ia.md`

---

titulo: Modelo Operacional — Time Multi-IA Maui versao: 1.0 status: proposta data\_criacao: 2026-05-04 idioma: pt-BR tipo: modelo\_operacional escopo: projeto\_maui confidencialidade: interna papel\_primario: agent\_engineering papeis\_secundarios:

- ai\_solutions\_architect
- development\_engineer
- written\_comms\_core
- safe\_agile\_master\_elite precedencia: 5 baseado\_em:
- "[[arquitetura-alvo-maui]]"
- "[[spec-funcionalidades-maui]]"
- "[[roadmap-desenvolvimento-maui]]" tags:
- maui
- multi-ia
- modelo-operacional
- lideranca-tecnica
- exec-requests
- exec-reports

---

# Modelo Operacional — Time Multi-IA Maui

## 1. Objetivo

Definir como uma equipe composta por múltiplos modelos de IA deve desenvolver o Maui, com papéis, fluxos, contratos, critérios de pronto, critérios de concluído e mecanismos de coordenação.

## 2. Princípio operacional

Modelos de IA não devem colaborar por memória implícita ou contexto informal. Devem colaborar por artefatos versionados:

```text
Task Brief → Exec Request → Execução → Exec Report → Review Report → Decisão → Memória/Backlog
```

## 3. Papéis do time

### 3.1 Líder técnico

Ferramentas típicas:

- ChatGPT;
- Claude;
- Gemini.

Responsabilidades:

- decompor roadmap em tarefas;
- criar Exec Requests;
- definir prioridade;
- revisar entregas;
- consolidar decisões;
- atualizar task board;
- acionar Human Gate.

Não deve:

- presumir acesso ao filesystem;
- declarar hash real sem evidência;
- aplicar mudança normativa sozinho.

### 3.2 Executor filesystem

Ferramentas típicas:

- Claude Code;
- Codex;
- Google Antigravity quando houver workspace.

Responsabilidades:

- implementar arquivos;
- criar scripts;
- criar schemas;
- executar validações;
- gerar patches;
- gerar Exec Reports.

Não deve:

- alterar normas sem Human Gate;
- escrever fora de `vault-maui/` ou área autorizada;
- ocultar falhas;
- marcar tarefa como concluída sem report.

### 3.3 Reviewer

Ferramentas típicas:

- Claude;
- Gemini;
- ChatGPT;
- Codex/Claude Code em revisão técnica.

Responsabilidades:

- verificar coerência;
- validar critérios de aceite;
- apontar riscos;
- solicitar mudanças;
- aprovar quando apropriado.

### 3.4 Curador

Ferramentas típicas:

- ChatGPT;
- Claude;
- Gemini.

Responsabilidades:

- registrar decisões;
- transformar reports em memória;
- organizar handoffs;
- manter painel file-based.

### 3.5 Human Gate

Responsável humano.

Aprova:

- mudanças normativas;
- promoção de adendos;
- alteração de princípios;
- escrita persistente crítica;
- plugins externos;
- automations com escrita;
- avanço P0 → P1 e P1 → P2.

## 4. Matriz ferramenta → função

| Ferramenta         | Tipo                | Função primária                      | Função secundária   | Modo de comunicação                |
| ------------------ | ------------------- | ------------------------------------ | ------------------- | ---------------------------------- |
| Claude Code        | executor            | implementação filesystem             | validações, patches | `CLAUDE.md`, Exec Request/Report   |
| Codex              | executor            | implementação filesystem             | refatoração, testes | `AGENTS.md`, Exec Request/Report   |
| Google Antigravity | executor/explorador | protótipos, validação cross-tool     | integração          | operator pack, Exec Request/Report |
| ChatGPT            | líder               | decomposição, coordenação, handoff   | revisão, escrita    | context package, painel            |
| Gemini             | reviewer/líder      | revisão ampla, alternativas          | documentação        | context package, review report     |
| Claude             | reviewer/líder      | agent engineering, coerência textual | governança          | context package, review report     |

## 5. Fluxo padrão de tarefa

```text
1. Líder técnico cria Task Brief
2. Líder converte Task Brief em Exec Request
3. Painel marca tarefa como pending/assigned
4. Executor recebe Exec Request
5. Executor executa somente escopo autorizado
6. Executor gera Exec Report
7. Reviewer avalia Exec Report
8. Reviewer gera Review Report
9. Líder decide: aceitar, pedir ajuste ou escalar Human Gate
10. Curador registra decisão/memória quando aplicável
```

## 6. Estados de tarefa

```text
backlog
ready
assigned
in_progress
blocked
submitted
in_review
changes_requested
approved
rejected
done
archived
```

## 7. Exec Request — template

```yaml
---
titulo: Exec Request — <nome da tarefa>
request_id: req-YYYYMMDD-NNN
status: ready
fase: P0.0 | P0.1 | P0.2 | P0.3 | P0.4 | P0.5 | P0.6 | P0.7 | P0.8 | P0.9 | P1 | P2
funcionalidade: string
prioridade: critical | high | medium | low
papel_requerido: executor | reviewer | leader | curator
ferramenta_preferida: claude-code | codex | antigravity | chatgpt | gemini | claude
confidencialidade: interna
human_gate: false
permissoes:
  filesystem_read: true
  filesystem_write: false
  network: false
  persistent_write: false
entradas:
  - caminho/ou/referencia
saidas_esperadas:
  - caminho/ou/formato
criterios_de_aceite:
  - string
---

# Objetivo

# Contexto mínimo

# Escopo

## Inclui

## Não inclui

# Instruções de execução

# Validações obrigatórias

# Formato do Exec Report
```

## 8. Exec Report — template

```yaml
---
titulo: Exec Report — <nome da tarefa>
report_id: rep-YYYYMMDD-NNN
request_id: req-YYYYMMDD-NNN
status: success | partial | failed | blocked
executor: string
ferramenta: claude-code | codex | antigravity | chatgpt | gemini | claude
confidencialidade: interna
arquivos_lidos: []
arquivos_alterados: []
artefatos_gerados: []
validacoes_executadas: []
riscos: []
pendencias: []
requer_human_gate: false
---

# Resumo

# O que foi feito

# Arquivos alterados ou propostos

# Validações executadas

# Riscos e limitações

# Pendências

# Próxima ação recomendada
```

## 9. Review Report — template

```yaml
---
titulo: Review Report — <nome da tarefa>
review_id: rev-YYYYMMDD-NNN
report_id: rep-YYYYMMDD-NNN
status: approved | changes_requested | rejected
reviewer: string
ferramenta: chatgpt | gemini | claude | codex | claude-code
confidencialidade: interna
---

# Decisão da revisão

# Findings

| Severidade | Item | Recomendação |
|---|---|---|

# Critérios de aceite verificados

# Riscos remanescentes

# Decisão recomendada
```

## 10. Definition of Ready

Uma tarefa está pronta quando:

- possui Exec Request;
- objetivo é claro;
- escopo e não escopo estão definidos;
- ferramenta preferida está definida;
- permissões estão explícitas;
- arquivos de entrada estão listados;
- saída esperada está definida;
- critérios de aceite estão definidos;
- Human Gate está indicado quando necessário.

## 11. Definition of Done

Uma tarefa está concluída quando:

- entregável existe;
- Exec Report foi gerado;
- validações foram executadas ou justificadas;
- Reviewer aprovou;
- Human Gate aprovou quando necessário;
- painel foi atualizado;
- decisão/memória foi registrada quando aplicável.

## 12. Cerimônias operacionais

### 12.1 Planning multi-IA

Responsável: líder técnico.

Entradas:

- roadmap;
- backlog;
- reports pendentes;
- riscos.

Saídas:

- tarefas priorizadas;
- Exec Requests criados;
- owner/ferramenta sugerida.

### 12.2 Daily/Check-in assíncrono

Formato:

```text
Ontem/última execução:
Hoje/próxima execução:
Bloqueios:
Requests/reports afetados:
```

### 12.3
