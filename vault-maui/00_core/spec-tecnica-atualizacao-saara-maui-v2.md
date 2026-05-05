---
titulo: Spec Técnica — Atualização Saara → Maui
versao: 0.2
spec_versao: 2.0
status: proposta
data_atualizacao: 2026-05-04
idioma: pt-BR
tipo: especificacao_tecnica_atualizacao
escopo: projeto_maui
confidencialidade: interna
papel_primario: ai_solutions_architect
papeis_secundarios:
  - development_engineer
  - written_comms_core
  - agent_engineering
precedencia: 5
substitui: spec_tecnica_atualizacao_saara_maui_v1_0
compatibilidade:
  - saara_v7_1_1
  - principios_fundacionais_saara_v7_1_1
  - handoff_maui_v0_1
  - claude_code_skills_2026
  - codex_skills_2026
  - mcp_protocol_2026
  - agents_md_open_standard
referencias:
  - "[[principios-fundacionais]]"
  - "[[especificacao-completa]]"
  - "[[spec-distribuicao]]"
  - "[[spec-instanciacao-conformidade]]"
  - "[[spec-context-injection]]"
  - "[[spec-capture-layer]]"
  - "[[spec-memory-store]]"
  - "[[spec-adendos]]"
  - "[[pka-agent-engineering]]"
  - "[[pka-ai-solutions-architect-elite]]"
  - "[[pka-development-engineer]]"
  - "[[pka-written-comms-core]]"
  - "[[pka-safe-agile-master-elite]]"
  - "[[Handoff_Maui_v0_1]]"
  - "[[context-packages/current]]"
  - "[[spec-tecnica-atualizacao-saara-maui-v1]]"
tags:
  - maui
  - saara
  - atualizacao
  - especificacao-tecnica
  - corpus-procedural
  - skills
  - hooks
  - subagents
  - plugins
  - mcp
  - operator-packs
  - update-protocol
  - agents-md-standard
  - context-engineering
  - v2
---

# Spec Técnica — Atualização Saara → Maui (v2.0)

> **Versão 2.0** desta especificação. Substitui a v1.0 (`spec-tecnica-atualizacao-saara-maui.md`), preservando todas as suas decisões e adicionando integração nativa com o estado-da-arte de 2026 em criação e configuração de agentes: **padrão aberto Agent Skills**, **hooks lifecycle**, **subagentes**, **plugins**, **MCP nativo**, **AGENTS.md**, **context engineering**, **automations** e **evals como código**.
>
> Esta spec consolida o trabalho dos papéis de **Arquiteto de Soluções**, **Engenheiro de Desenvolvimento**, **Written Comms** e **Agent Engineering**.
>
> Maui v0.2 nasce **diretamente alinhado** ao ecossistema 2026 — não é retrofit.

---

## 0. Status, governança e relação com a v1.0

### 0.1 Status

`status: proposta` · `spec_versao: 2.0` · `substitui: v1.0`. Esta spec não substitui Saara v7.1.1 silenciosamente. A adoção formal requer decisão de governança registrada como memória e adendo.

### 0.2 O que muda em relação à v1.0

A v1.0 contratou Maui como **"corpus + scripts + skills + procedures"** sem ainda incorporar o vocabulário convergente da indústria em 2026. A v2.0:

- Adota o **padrão aberto Agent Skills** (`SKILL.md` + frontmatter), compatível com Claude Code, Codex, Cursor, Gemini CLI e demais.
- Incorpora **hooks lifecycle** como camada de enforcement determinístico (não-alucinatório).
- Define **subagentes** como construto nativo de Maui, com modelo dual: **subagentes nominais** (especialistas pré-definidos) e **clones via Task** (agente decide delegação).
- Define **plugins** como unidade de distribuição (bundle skills+hooks+subagents+commands).
- Eleva **MCP** de "modelo de distribuição entre vários" para **protocolo de primeira classe** do Maui Toolkit.
- Substitui edição manual de `CLAUDE.md`/`AGENTS.md` por **geração via templates** + convenção `.agents/skills/` quando aplicável.
- Introduz **context engineering** (Write/Select/Compress/Isolate) como disciplina de primeira classe, evoluindo Context Injection.
- Introduz **evals** e **promptfoo-style testing** como parte do ciclo de vida de skills.
- Introduz **automations** como construto separado de skills (skills = método; automations = cadência).
- Introduz **output contracts** + **success criteria** como obrigatórios em todo entregável Maui.
- Reposiciona scripts: continuam viváveis, mas agora podem ser **expostos como MCP tools** quando a ferramenta-cliente suporta MCP.

### 0.3 Precedência (preservada)

Esta spec opera no nível 5 da precedência operacional. Em conflito conceitual prevalecem: políticas externas, system prompt ativo, princípios fundacionais Saara v7.1.1, especificação completa Saara v7.1.1, esta spec e demais specs paritárias.

### 0.4 Stop rule (preservada)

Onde esta spec não cobrir um aspecto, valem as specs Saara v7.1.1 vigentes. Lacunas materiais devem ser sinalizadas, não inventadas.

---

## 1. Resumo executivo

### 1.1 O que muda no produto

O Saara v7.1.1 já estabelecia que a identidade vive no corpus, não na infraestrutura. Maui leva esse princípio até o limite: capacidades executáveis (scripts, skills, procedures), mecanismos de adaptação (operator packs, hooks, subagents) e protocolos de comunicação (MCP, exec requests/reports) também passam a viver no corpus.

Maui v0.2 vai além: nasce **alinhado a um padrão aberto da indústria**. O mesmo `SKILL.md` que vive em `vault-maui/skills/` é descoberto e executado nativamente por Claude Code (`.claude/skills/`), Codex (`$HOME/.agents/skills/`), Cursor, Gemini CLI e Antigravity — sem retrofit.

### 1.2 O que não muda (preservado da v1.0)

- Os 5 Princípios Fundacionais do Saara v7.1.1.
- As 5 PKAs herdadas (Agent Engineering, Development Engineer, AI Solutions Architect, Written Comms, SAFe — ativo condicional).
- O system prompt v7.1.1 como contrato runtime até decisão explícita.
- O modelo de governança (precedência, stop rule, anti-drift, F/I/H, Human Gate).
- O conjunto de funcionalidades base contratadas na v1.0 (registry, memory index, context export, update export).

### 1.3 Equação Maui v0.2

```
Maui = corpus
     + memória + PKAs + specs + adendos + insights        (camada cognitiva)
     + skills + procedures + reflexes + scripts           (camada procedural)
     + hooks + subagents + plugins                        (camada de execução)
     + schemas + evals + automations                      (camada de qualidade)
     + operator-packs + mcp-servers                       (camada de adaptação)
     + context-packages + exec-requests/reports           (camada de comunicação)
```

Qualquer ferramenta de IA com filesystem ou interface conversacional deve conseguir instanciar e operar Maui a partir dessa estrutura, **respeitando padrões abertos do mercado**.

---

## 2. Arquitetura — Visão do Arquiteto de Soluções

### 2.1 Princípio guia

> **Adesão ao padrão aberto + soberania do corpus.**
>
> Maui adota convenções de Agent Skills, AGENTS.md, MCP e demais padrões abertos sempre que isso não violar Soberania Cognitiva. Identidade Maui vem do corpus; estrutura vem do padrão aberto.

### 2.2 Camadas arquiteturais (revisão v2)

```
┌────────────────────────────────────────────────────────────┐
│ Camada 1 — COGNITIVA (Saara v7.1.1 herdada)                │
│ 00_core/ · 01_manifest/ · adendos/ · insights/ · memoria/  │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 2 — PROCEDURAL                                       │
│ skills/ (padrão SKILL.md) · procedures/ · scripts/          │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 3 — EXECUÇÃO                                         │
│ hooks/ · subagents/ · plugins/                              │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 4 — QUALIDADE                                        │
│ schemas/ · evals/ · automations/                            │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 5 — ADAPTAÇÃO                                        │
│ operator-packs/ · mcp-servers/                              │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│ Camada 6 — COMUNICAÇÃO                                      │
│ context-packages/ · exec-requests/ · exec-reports/          │
└────────────────────────────────────────────────────────────┘
```

### 2.3 Topologia híbrida 2026

Maui v0.2 reconhece três modos de operação simultâneos:

```
┌────────────────────┐  filesystem  ┌──────────────────┐
│  Claude Code       │ ←──────────→ │                  │
│  Codex             │              │   vault-maui/    │
│  Cursor            │              │                  │
└────────────────────┘              │   (corpus)       │
                                    │                  │
┌────────────────────┐  MCP/REST    │                  │
│  Claude Desktop    │ ←──────────→ │                  │
│  ChatGPT (Action)  │              │                  │
│  Gemini            │              └──────────────────┘
└────────────────────┘                       ▲
                                             │
┌────────────────────┐  Human-Handoff        │
│  ChatGPT (sem fs)  │ ────────────→ Update  │
│  Gemini (sem fs)   │              Protocol │
└────────────────────┘                       │
                                    ┌────────┴───────┐
                                    │  maui-toolkit/ │
                                    │  (auxiliar)    │
                                    └────────────────┘
```

Modos não são exclusivos: a mesma instância pode usar filesystem para Camada A e MCP para Camada B/C, e human-handoff em fallback.

### 2.4 Princípios arquiteturais (revisão v2)

| Princípio Saara v7.1.1 | Aplicação em Maui v0.2 |
|---|---|
| Soberania Cognitiva | Levada ao limite: capacidades executáveis vivem no corpus E aderem a padrões abertos da indústria |
| Lifecycle de Instanciação | Preservado; reforçado por Update Protocol + hooks de SessionStart |
| Context Injection Sob Demanda | Evoluído para **Context Engineering** (Write/Select/Compress/Isolate) |
| Capture Layer | Preservada; integrada com hooks `Stop`/`PostToolUse` e procedure de captura |
| Insight Pipeline | Preservado; pode usar subagentes para Pattern Detection e evals para validação |

Princípios novos (v0.2):

| Princípio | Definição |
|---|---|
| Adesão ao padrão aberto | Maui adota convenções da indústria sempre que não violem soberania |
| Determinismo onde possível | Hooks > prompts onde correção é não-negociável |
| Output contract first | Critério de sucesso e contrato de saída antes do prompt |
| Context engineering | Falha em produção é falha de assembly de contexto, não do prompt |
| Evals como código | Skills críticas têm suite de evals versionada |

### 2.5 Fronteiras (revisão v2)

**Maui é:** corpus cognitivo multipapel, procedural, portátil, instanciável, **alinhado a padrões abertos**.

**Maui não é:** aplicação, backend, banco, MCP server específico, ferramenta. **Mas Maui produz e expõe MCP servers** quando útil — diferente de "ser um MCP server".

**Fronteira Corpus / Toolkit / Operator / MCP Server:**

- **Corpus (`vault-maui/`)** — identidade, normativo, procedural, executável-portátil.
- **Toolkit (`maui-toolkit/`)** — bootstrap (init, instantiate, panel, eval).
- **Operator Packs (`vault-maui/operator-packs/`)** — adaptadores por ferramenta.
- **MCP Servers (`vault-maui/mcp-servers/`)** — exposição de capacidades Maui via protocolo MCP para ferramentas que o suportem.

---

## 3. Estrutura-alvo do corpus Maui (v0.2)

### 3.1 Diretórios canônicos

```
vault-maui/
├── 00_core/                           # Normativo herdado
│   ├── system-prompt.md
│   ├── especificacao-completa.md
│   ├── principios-fundacionais.md
│   ├── pka-*.md                       # 5 PKAs herdadas
│   └── spec-*.md                      # specs subsidiárias
│
├── 01_manifest/                       # Identidade Maui
│   ├── maui-product-definition.md
│   ├── maui-vault-structure.md
│   ├── maui-file-format-policy.md
│   ├── maui-toolkit-boundaries.md
│   ├── maui-runtime-model.md
│   ├── maui-procedural-layer.md
│   ├── maui-execution-layer.md        # NOVO v0.2: hooks, subagents, plugins
│   ├── maui-quality-layer.md          # NOVO v0.2: schemas, evals, automations
│   └── maui-open-standards-policy.md  # NOVO v0.2: como Maui adere a padrões abertos
│
├── memoria/                           # Memórias episódicas
│
├── adendos/                           # Evoluções incrementais
│
├── insights/                          # Padrões consolidados
│
├── skills/                            # Skills (padrão SKILL.md aberto)
│   └── {nome-skill}/
│       ├── SKILL.md                   # contrato (frontmatter + body)
│       ├── README.md                  # opcional
│       ├── examples/                  # opcional
│       ├── scripts/                   # opcional, scripts próprios da skill
│       └── evals/                     # opcional, suite de evals
│
├── procedures/                        # Runbooks e reflexes
│   ├── procedimento-*.md
│   └── reflexes/
│       └── reflexo-*.md
│
├── scripts/                           # Scripts de condicionamento globais
│
├── hooks/                             # NOVO v0.2: hooks lifecycle
│   ├── pre-tool-use/
│   ├── post-tool-use/
│   ├── user-prompt-submit/
│   ├── session-start/
│   ├── session-end/
│   ├── pre-compact/
│   ├── stop/
│   └── subagent-stop/
│
├── subagents/                         # NOVO v0.2: subagentes nominais
│   └── {nome}.md                      # frontmatter + system prompt do subagente
│
├── plugins/                           # NOVO v0.2: bundles distribuíveis
│   └── {nome-plugin}/
│       ├── plugin.yaml                # manifesto
│       ├── skills/                    # skills do plugin
│       ├── hooks/                     # hooks do plugin
│       ├── subagents/                 # subagents do plugin
│       └── README.md
│
├── schemas/                           # JSON/YAML Schema
│
├── evals/                             # NOVO v0.2: avaliações
│   ├── skills/
│   │   └── {skill}/                   # evals de uma skill
│   ├── prompts/
│   └── regression/
│
├── automations/                       # NOVO v0.2: tarefas agendadas
│   └── {nome}.yaml
│
├── operator-packs/                    # Adaptação por ferramenta
│   ├── claude-code/
│   ├── codex/
│   ├── chatgpt/
│   ├── gemini/
│   └── antigravity/
│
├── mcp-servers/                       # NOVO v0.2: servers MCP do Maui
│   ├── maui-corpus-server/            # expõe corpus via MCP
│   ├── maui-memory-server/            # expõe memory store via MCP
│   └── maui-update-server/            # expõe update protocol via MCP
│
├── context-packages/
│   ├── data/
│   ├── templates/
│   └── generated/
│
├── exec-requests/
├── exec-reports/
├── exports/
├── validations/
└── README.md
```

### 3.2 Toolkit auxiliar

```
maui-toolkit/
├── init/                # Monta estrutura inicial
├── instantiate/         # Gera primeira instância para target
├── panel/               # Curadoria multi-IA
├── eval/                # NOVO v0.2: roda evals localmente
├── mcp-launch/          # NOVO v0.2: inicia MCP servers do corpus
└── README.md
```

### 3.3 Convenção neutra: `.agents/skills/`

Para máxima portabilidade, Maui suporta dois modos de exposição de skills:

**Modo A — Skills nativas Maui** (vivem em `vault-maui/skills/`).

**Modo B — Skills compartilhadas multi-tool** (espelhadas em `~/.agents/skills/` ou no projeto-cliente em `.agents/skills/`).

Operator packs do Modo B geram links simbólicos ou cópias selecionadas para a convenção neutra, fazendo com que a mesma skill funcione em Claude Code, Codex e demais.

### 3.4 Política de formatos (v0.2)

| Formato | Uso |
|---|---|
| Markdown + YAML frontmatter | Conhecimento humano, contexto IA, SKILL.md, procedures, hooks scripts em prosa |
| YAML | Configuração: pack.yaml, plugin.yaml, instancia.yaml, automations |
| JSON | Saída de scripts/APIs/MCP. Schemas: JSON Schema |
| JSONL | Eventos, logs append-only, evals datasets |
| SQLite | Índices reconstruíveis (`.maui/memory.db`) |
| Jinja2 (`.md.j2`, `.yaml.j2`) | Templates |
| Python | Scripts de condicionamento, hooks scripts (preferido por portabilidade stdlib) |
| Shell | Hooks scripts simples (validação rápida) |

---

## 4. Funcionalidades do corpus Maui v0.2

Esta seção contrata cada funcionalidade. Para cada uma:

- **Definição** — o que faz e por que existe
- **Localização** — onde vive
- **Padrão aberto** — qual padrão da indústria respeita (quando aplicável)
- **Entradas / Saídas** — IO
- **Comportamento** — fluxo
- **Necessidades** — dependências
- **Output contract** — formato de saída testável
- **Success criteria** — critério objetivo de "funciona"
- **Eval mínimo** — como testar (quando aplicável)

### Princípios transversais (todas as funcionalidades)

1. **Read-only por padrão.** Escritas exigem flag (`--apply`, `--write-patch`).
2. **Idempotência.**
3. **Saída dual.** `--json` + `--markdown` quando aplicável.
4. **Sem sync automático.** Reconciliação requer humano ou autorização explícita.
5. **Determinismo.** Mesma entrada → mesma saída (módulo timestamps).
6. **Portabilidade.** Stdlib first; dependências externas justificadas.
7. **Validação prévia.** Schema antes de gravar.
8. **Auditoria.** Toda operação significativa registra evento estruturado.
9. **Output contract first** (NOVO v0.2). Contrato declarado antes do código.
10. **Eval-friendly** (NOVO v0.2). Skills críticas têm dataset de evals.

---

### 4.1 Skills — Padrão aberto Agent Skills

#### Definição

**Skills** são capacidades operacionais reutilizáveis em formato `SKILL.md` compatível com o **padrão aberto Agent Skills** (Claude Code, Codex, Cursor, Gemini CLI, Antigravity). Diferentes de scripts (determinísticos) e de procedures (runbooks textuais para humanos), skills são **descobertas e ativadas pelo modelo de IA** automaticamente quando o contexto match.

#### Localização

```
vault-maui/skills/{nome}/
├── SKILL.md            # frontmatter YAML + body markdown
├── README.md           # opcional, contexto adicional
├── examples/           # opcional
├── scripts/            # opcional
└── evals/              # opcional, suite de evals
```

Skills compartilhadas multi-tool são também espelhadas em `~/.agents/skills/{nome}/` ou `.agents/skills/{nome}/` no projeto-cliente.

#### Padrão aberto

`SKILL.md` segue o padrão aberto **Agent Skills** universal. Frontmatter reconhecido por todos os principais agentes de codificação em 2026.

#### Frontmatter mínimo

```yaml
---
name: maui-{nome-da-skill}
description: "Descrição curta + triggers de ativação"
status: ativo | proposta | deprecated
versao: 0.1
papel_primario: agent_engineering | development_engineer | ai_solutions_architect | written_comms_core | safe_agile_master_elite
inputs:
  - tipo: arquivo | string | yaml
    descricao: ...
outputs:
  - tipo: markdown | json | arquivo-no-fs
    contrato: ...
allowed-tools:                  # opcional, restringe tools usáveis
  - Read
  - Bash(git *)
disable-model-invocation: false # se true, skill é só por comando explícito
context: fork                   # opcional: roda em subagent isolado
agent: Explore | Plan | general-purpose | {custom}  # opcional
hooks:                          # opcional, hooks específicos da skill
  PreToolUse:
    - matcher: "Bash"
      command: "{path}/validate.sh"
scripts_chamados:
  - scripts/maui_{...}.py
procedures_relacionadas:
  - procedures/procedimento-{...}.md
evals_path: evals/skills/{nome}/   # opcional
---
```

#### Body padrão

```markdown
# {Nome da skill}

## Quando usar
{Triggers + situações que ativam a skill}

## Como executar
{Passos diretos, comandos, fluxo}

## Output contract
{Formato esperado de saída — testável}

## Success criteria
{Como saber que funcionou — bullets objetivos}

## Falhas comuns
{O que dá errado e como mitigar}

## Eval mínimo
{Referência ao dataset de evals ou caso mínimo de teste}
```

#### Skills mínimas P0 (Maui v0.2)

```
skills/maui-registry-maintenance/
skills/maui-memory-maintenance/
skills/maui-memory-create/
skills/maui-context-export/
skills/maui-update-export/
skills/maui-instance-update-check/
skills/maui-instance-integrate-update/
skills/maui-roadmap-audit/
skills/maui-doc-consistency-check/
skills/maui-vault-health/
skills/maui-eval-runner/             # NOVO v0.2
skills/maui-frontmatter-validate/    # NOVO v0.2
skills/maui-mcp-server-launch/       # NOVO v0.2
skills/maui-handoff-generate/        # NOVO v0.2: gera handoff entre sessões
```

#### Output contract típico

Skill produz: artefato concreto (arquivo, markdown, JSON), nunca apenas "explicação". Output sempre incluí F/I/H quando há inferência ou hipótese.

#### Success criteria

- SKILL.md valida contra `schemas/skill.schema.yaml`.
- Skill ativa automaticamente quando triggers do `description` semanticamente batem com a query.
- Skill nunca contém lógica embutida; delega para scripts/procedures.
- Skill compartilhada funciona em pelo menos 2 ferramentas (Claude Code + Codex).
- Skill crítica tem ao menos 3 casos de eval.

#### Eval mínimo

```
evals/skills/{nome}/
├── dataset.jsonl              # casos de entrada esperados
├── expected.jsonl             # outputs esperados
└── eval-config.yaml           # critérios de match (regex, exact, llm-judge)
```

---

### 4.2 Hooks — Determinismo e enforcement

#### Definição

**Hooks** são scripts disparados em pontos específicos do ciclo de vida de uma sessão de IA. Diferente de skills (que dependem da interpretação do modelo), hooks são **deterministas** — não alucinam. São a camada onde regras inegociáveis vivem.

#### Localização

```
vault-maui/hooks/
├── pre-tool-use/        # antes de qualquer tool executar (security checkpoint)
├── post-tool-use/       # depois de tool executar (logging, lint)
├── user-prompt-submit/  # antes do modelo ver o prompt (validação, injeção)
├── session-start/       # carga de contexto inicial
├── session-end/         # cleanup, captura
├── pre-compact/         # backup antes de compactação
├── stop/                # finalização do agente
└── subagent-stop/       # finalização de subagente
```

Cada subdiretório contém scripts (Python ou shell) + um `manifest.yaml` declarando quando ativar.

#### Padrão aberto

Hooks lifecycle de Claude Code (~25 eventos) e Codex (eventos paralelos). Maui adota subset comum portável.

#### Manifest de hook

```yaml
# vault-maui/hooks/pre-tool-use/maui-block-corpus-write.yaml
event: PreToolUse
matcher: "Edit|Write"
condition:
  path_glob:
    - "00_core/**"
    - "01_manifest/**"
script: hooks/pre-tool-use/scripts/block-corpus-write.sh
exit_2_blocks: true
description: "Bloqueia edição direta no corpus normativo sem human gate explícito"
status: ativo
```

#### Hooks mínimos P0

| Hook | Evento | Função |
|---|---|---|
| `maui-block-corpus-write` | PreToolUse | Bloqueia edição em `00_core/`, `01_manifest/` sem gate explícito |
| `maui-load-context` | SessionStart | Carrega context package atual + reflexes ativos |
| `maui-validate-frontmatter` | PostToolUse | Valida frontmatter após escrita em `memoria/`, `adendos/` |
| `maui-backup-session` | PreCompact | Salva transcrição antes de compactação |
| `maui-capture-on-stop` | Stop | Sugere captura se gatilhos disparam |
| `maui-warn-shared-modules` | PreToolUse | Avisa (não bloqueia) edição em módulos sensíveis |

#### Output contract

Exit code 2 bloqueia operação e retorna mensagem ao agente. Exit 0 permite. Saída JSON estruturada para hooks que injetam contexto.

#### Success criteria

- Hook `block-corpus-write` impede 100% das tentativas de edição direta sem gate.
- Hooks de SessionStart adicionam contexto sem ultrapassar 1000 tokens.
- Hooks são reentrantes (chamados múltiplas vezes não corrompem estado).

---

### 4.3 Subagentes — Modelo dual

#### Definição

**Subagentes** executam tarefas em contextos isolados e retornam apenas o sumário. Maui adota **modelo dual** reconhecendo o debate de 2026:

- **Modelo A — Subagentes nominais** — especialistas pré-definidos (`pattern-reviewer`, `security-reviewer`, etc.) com system prompt e tools próprios. Boa para padronização e governança.
- **Modelo B — Master-Clone** — agente principal usa `Task()` para spawnar clones de si mesmo conforme necessário, decidindo orquestração dinamicamente. Boa para flexibilidade.

Maui suporta **ambos**, com convenção: tarefas que tocam estado normativo (corpus, registry, memória) usam **Modelo A** (governança); tarefas operacionais usam **Modelo B** (flexibilidade).

#### Localização

```
vault-maui/subagents/
├── maui-doc-reviewer.md        # revisor de PKAs e specs
├── maui-skill-author.md        # autor de novas skills
├── maui-eval-runner.md         # executor de evals
├── maui-memory-curator.md      # curador de memórias
├── maui-update-validator.md    # validador de update packages
└── maui-handoff-writer.md      # autor de handoffs entre sessões
```

#### Padrão aberto

Compatível com Claude Code subagents (`.claude/agents/`) e Codex agents. Maui replica o frontmatter padrão.

#### Frontmatter mínimo

```yaml
---
name: maui-doc-reviewer
description: "Revisa PKAs, specs e adendos quanto a coerência, precedência e referências cruzadas"
papel_primario: written_comms_core
papel_secundario: agent_engineering
tools:                         # subset de tools permitidos
  - Read
  - Grep
  - Glob
model: sonnet                  # opcional, override
memory: project                # opcional, mantém memory persistente
proactive: true                # ativa automaticamente quando match
hooks:                         # opcional, hooks scoped
  PreToolUse:
    - matcher: "Bash"
      command: "validate-readonly.sh"
---

# Maui Doc Reviewer

System prompt do subagente: você é um revisor sênior de documentos
do corpus Maui. Verifica coerência, precedência operacional, integridade
referencial. Aplica F/I/H quando há inferência. Nunca edita; apenas
recomenda. ...
```

#### Output contract

Subagente retorna sumário estruturado com seções: `findings`, `severity`, `suggestions`, `confidence` (F/I/H), `next_steps`.

#### Success criteria

- Subagente nominal nunca edita estado fora de seus tools permitidos.
- Subagente clone (Task) recebe context completo da Master e retorna ≤ 500 tokens de sumário.
- Subagente respeita `allowed-tools` rigorosamente.

---

### 4.4 Plugins — Bundles distribuíveis

#### Definição

**Plugins** são bundles que empacotam skills + hooks + subagents + commands em uma unidade instalável e versionada. Servem para distribuição e reutilização cross-projetos. Maui pode tanto **publicar** plugins quanto **consumir** plugins externos.

#### Localização

```
vault-maui/plugins/
├── maui-core-essentials/
│   ├── plugin.yaml
│   ├── skills/
│   ├── hooks/
│   └── subagents/
└── maui-curation-pack/
    ├── plugin.yaml
    ├── skills/
    └── ...
```

#### Padrão aberto

Estrutura compatível com Claude Code plugins e Codex plugins. Namespacing automático: skill `simplify` em plugin `code-simplifier` vira `/code-simplifier:simplify`.

#### Manifest mínimo

```yaml
# plugins/maui-core-essentials/plugin.yaml
name: maui-core-essentials
version: 0.1.0
description: "Skills e hooks essenciais do Maui"
maintainer: "Saara/Maui project"
status: ativo
provides:
  skills:
    - maui-vault-health
    - maui-frontmatter-validate
    - maui-context-export
  hooks:
    - maui-load-context
    - maui-validate-frontmatter
  subagents:
    - maui-doc-reviewer
requires:
  python: ">=3.10"
  schemas:
    - schemas/skill.schema.yaml
    - schemas/hook.schema.yaml
```

#### Plugins P0 propostos

```
plugins/maui-core-essentials/        # skills/hooks/subagents básicos
plugins/maui-curation-pack/          # ferramentas de curadoria de corpus
plugins/maui-instance-management/    # registry, update protocol, conformidade
plugins/maui-eval-toolkit/           # evals, regression testing
```

#### Success criteria

- Plugin instala sem conflito de nomes (namespacing).
- Plugin desinstalável sem deixar resíduo no corpus.
- Plugin valida `requires:` antes de instalar.

---

### 4.5 MCP Servers do Maui — Exposição via protocolo padrão

#### Definição

Maui v0.2 expõe capacidades selecionadas via **MCP servers** rodáveis localmente. Permite que ferramentas-cliente que suportam MCP (Claude Desktop, Cursor, ChatGPT com Connectors, Gemini) acessem o corpus sem precisar do filesystem direto.

#### Localização

```
vault-maui/mcp-servers/
├── maui-corpus-server/             # expõe leitura do corpus
│   ├── server.py
│   ├── manifest.yaml
│   └── README.md
├── maui-memory-server/             # expõe memory store
│   ├── server.py
│   └── manifest.yaml
├── maui-update-server/             # expõe update protocol
│   ├── server.py
│   └── manifest.yaml
└── maui-skills-server/             # expõe skills como MCP tools
    ├── server.py
    └── manifest.yaml
```

#### Padrão aberto

**MCP (Model Context Protocol)** versão estável, JSON-RPC 2.0, transport stdio + HTTP. Compatível com 200+ clientes em 2026.

#### Tools expostas (mínimo P0)

```python
# maui-corpus-server expõe:
@tool
def get_pka(name: str) -> str:
    """Retorna conteúdo de uma PKA específica do corpus."""

@tool
def get_principle(id: str) -> str:
    """Retorna princípio fundacional específico."""

@tool
def list_skills(filter_papel: str = None) -> list[dict]:
    """Lista skills disponíveis no corpus."""

# maui-memory-server expõe:
@tool
def search_memory(query: str, escopo: str = "pessoal", limit: int = 10) -> list[dict]:
    """Busca memórias relevantes."""

@tool
def capture_memory(content: dict) -> str:
    """Captura nova memória (modo explícito)."""

# maui-update-server expõe:
@tool
def check_drift(tool_id: str, known_hash: str) -> dict:
    """Verifica drift de uma instância."""

@tool
def generate_update_package(instancia_yaml: dict) -> str:
    """Gera update package para instância."""
```

#### Resources expostos

```
mcp://maui/corpus/system-prompt
mcp://maui/corpus/pka/{name}
mcp://maui/corpus/spec/{name}
mcp://maui/corpus/principles
mcp://maui/memory/session/{id}
```

#### Sampling e Elicitation

Maui MCP servers usam **Sampling** quando precisam que o modelo gere texto (ex: compactação de memória) e **Elicitation** quando precisam input do humano (ex: aprovar adendo).

#### Output contract

JSON-RPC 2.0 conforme spec MCP. Tools sempre retornam estrutura tipada com schema.

#### Success criteria

- MCP server inicia em < 2s.
- Cliente Claude Desktop e Cursor conectam sem erro.
- Tools expõem schema OpenAPI-like válido.
- Sampling/Elicitation funcionam end-to-end.

---

### 4.6 Scripts de condicionamento (preservados da v1.0)

Os scripts contratados na v1.0 permanecem. Mudanças v0.2:

- Cada script tem skill associada (`skills/maui-{nome}/SKILL.md`).
- Cada script crítico pode ser exposto como MCP tool.
- Cada script tem ao menos um eval em `evals/scripts/{nome}/`.

Lista preservada e contratos detalhados ficam na v1.0; abaixo só o resumo:

| Script | Skill associada | MCP tool? | Eval? |
|---|---|---|---|
| `maui_registry.py` | `maui-registry-maintenance` | sim | sim |
| `maui_memory_index.py` | `maui-memory-maintenance` | sim | sim |
| `maui_memory_search.py` | `maui-memory-maintenance` | sim | sim |
| `maui_context_export.py` | `maui-context-export` | sim | sim |
| `maui_update_export.py` | `maui-update-export` | sim | sim |
| `maui_validate_frontmatter.py` | `maui-frontmatter-validate` | não | sim |
| `maui_validate_links.py` | `maui-doc-consistency-check` | não | sim |
| `maui_validate_memory.py` | `maui-memory-maintenance` | não | sim |
| `maui_vault_health.py` | `maui-vault-health` | sim | sim |
| `maui_eval_run.py` | `maui-eval-runner` | sim | sim (meta) |

Detalhes contratuais na v1.0 §4.1–4.8 permanecem válidos.

---

### 4.7 Procedures e reflexes (preservados)

Permanecem conforme v1.0 §4.10. Mudança v0.2: procedures críticas podem invocar **subagentes** ao invés de operadores humanos quando ferramenta-cliente suporta.

---

### 4.8 Operator Packs (atualizados)

#### Definição

Pacotes de adaptação por ferramenta. **Mudança v0.2:** operator packs agora geram **três** artefatos:

1. **Instruções nativas da ferramenta** — `CLAUDE.md`, `AGENTS.md`, instructions de Custom GPT/Gem.
2. **Convenção neutra** — symlinks ou cópias para `~/.agents/skills/` quando aplicável.
3. **Configuração MCP** — `mcp.json` ou equivalente apontando para os MCP servers do Maui.

#### Localização

```
operator-packs/claude-code/
├── pack.yaml
├── CLAUDE.md.j2                  # template
├── generated/CLAUDE.md
├── update-protocol.md
├── allowed-commands.md
├── hooks.example.json
├── mcp-config.json.j2            # NOVO v0.2
└── generated/mcp-config.json     # NOVO v0.2

operator-packs/codex/
├── pack.yaml
├── AGENTS.md.j2
├── generated/AGENTS.md
├── update-protocol.md
└── codex-config.toml.j2          # NOVO v0.2
```

#### Prioridade de implementação (revisada v0.2)

1. **Claude Code** (filesystem + persistência via `CLAUDE.md` + MCP)
2. **Codex** (filesystem + `AGENTS.md` + skills em `~/.agents/skills/`)
3. **Claude Desktop** (MCP nativo)
4. **ChatGPT** (Action + humano intermediário)
5. **Gemini** (filesystem ou MCP conforme contexto)
6. **Antigravity / Cursor** (skills via convenção neutra)

#### Success criteria (revisada v0.2)

- Operator pack gerado funcional sem edição manual.
- Pack inclui `mcp-config.json` válido quando aplicável.
- Skills compartilhadas (`.agents/skills/`) funcionam em ≥ 2 ferramentas.

---

### 4.9 Exec Requests / Reports (preservados)

Permanecem conforme v1.0 §4.12. Mudança v0.2: requests podem ser disparados via **MCP tool** quando ferramenta-cliente suporta, evitando humano intermediário.

---

### 4.10 Context Packages (preservados + extensões)

Permanecem conforme v1.0 §4.13. Extensões v0.2:

- Templates Jinja2 podem renderizar **três variantes** por target: `default.md.j2`, `compact.md.j2`, `mcp.md.j2`.
- Variante `mcp.md.j2` é otimizada para ferramentas MCP-aware (mais curta, com refs `mcp://` ao invés de conteúdo embutido).

---

### 4.11 Update Protocol (preservado + extensão MCP)

Permanece conforme v1.0 §4.14. Extensão v0.2:

- Update Request pode ser gerado via MCP tool `check_drift` quando aplicável.
- Update Package pode ser entregue via MCP resource `mcp://maui/update/package/{id}`.

---

### 4.12 Schemas (preservados + adicionais)

Permanecem conforme v1.0 §4.15. Schemas adicionais v0.2:

```
schemas/
├── ... (schemas v1.0) ...
├── hook.schema.yaml              # NOVO
├── subagent.schema.yaml          # NOVO
├── plugin.schema.yaml            # NOVO
├── mcp-server.schema.yaml        # NOVO
├── eval.schema.yaml              # NOVO
├── automation.schema.yaml        # NOVO
└── output-contract.schema.yaml   # NOVO
```

---

### 4.13 Evals — Avaliação como código

#### Definição

**Evals** são testes versionados que verificam que skills, scripts, prompts e operator packs continuam funcionando após mudanças. Inspirados em práticas Promptfoo / DSPy de 2026, mas adaptados ao corpus Maui.

#### Localização

```
vault-maui/evals/
├── skills/
│   └── {skill-name}/
│       ├── dataset.jsonl
│       ├── expected.jsonl
│       └── eval-config.yaml
├── prompts/
├── regression/
└── integration/
```

#### Tipos de eval suportados

| Tipo | Uso |
|---|---|
| `exact_match` | Output exato esperado |
| `regex_match` | Output bate regex |
| `schema_match` | Output valida schema |
| `llm_judge` | Outro LLM avalia (custo extra) |
| `human_check` | Marcado para revisão humana |
| `script_check` | Script Python decide pass/fail |

#### Eval config exemplo

```yaml
# evals/skills/maui-context-export/eval-config.yaml
name: maui-context-export-eval
target: skills/maui-context-export
dataset: evals/skills/maui-context-export/dataset.jsonl
expected: evals/skills/maui-context-export/expected.jsonl
checks:
  - type: schema_match
    schema: schemas/context-package.schema.yaml
  - type: script_check
    script: evals/skills/maui-context-export/check_size.py
    description: "Verifica que pacote compacto fica abaixo de budget"
  - type: regex_match
    pattern: "(?s)## 1\\. Identificação"
    description: "Pacote inclui seção Identificação"
pass_threshold: 0.95
```

#### CLI

```bash
maui eval run --skill maui-context-export
maui eval run --all
maui eval regress --since 2026-04-01
```

#### Success criteria

- Skills críticas têm cobertura ≥ 80% em evals.
- Eval roda em < 60s para suite completa básica.
- Falha de eval é bloqueante para promoção de adendo.

---

### 4.14 Automations — Cadência separada de método

#### Definição

**Automations** são tarefas agendadas que executam skills periodicamente. Inspirado em Codex Automations 2026: "skills definem método; automations definem cadência".

#### Localização

```
vault-maui/automations/
├── daily-vault-health-check.yaml
├── weekly-roadmap-audit.yaml
├── weekly-pattern-detection.yaml
└── monthly-instance-drift-report.yaml
```

#### Manifest exemplo

```yaml
# automations/weekly-pattern-detection.yaml
name: weekly-pattern-detection
description: "Roda Pattern Detector semanal sobre memórias para identificar candidatos a adendos"
schedule: "0 9 * * MON"   # cron, segundas 9h
skill: maui-pattern-detector
inputs:
  since: "P7D"            # últimos 7 dias
  threshold: 0.7
target: vault-maui
notify_on:
  - candidates_found
  - error
status: ativo
human_gate: true          # candidatos passam por aprovação
```

#### Success criteria

- Automation declarada em YAML executa conforme schedule.
- Falha de automation gera evento auditável.
- Automation com `human_gate: true` nunca aplica mudanças sem aprovação.

---

### 4.15 Maui Toolkit (atualizado)

#### Comandos (revisão v0.2)

```bash
maui init --path ./vault-maui --template standard
maui instantiate --target {claude-code|codex|chatgpt|gemini|claude-desktop|cursor}
maui panel {status|task|dispatch|collect|compare|record}
maui eval {run|regress|validate}              # NOVO v0.2
maui mcp-launch {corpus|memory|update|skills} # NOVO v0.2
maui plugin {install|uninstall|list|publish}  # NOVO v0.2
```

#### `maui mcp-launch`

Inicia um ou mais MCP servers do Maui em modo daemon ou stdio:

```bash
maui mcp-launch corpus --transport stdio
maui mcp-launch memory --transport http --port 8765
maui mcp-launch all --transport http
```

---

## 5. Tabela consolidada — funcionalidades v0.2

| # | Função | Localização | Padrão aberto | Novo v0.2 |
|---|---|---|---|---|
| 1 | Skills | `skills/{nome}/SKILL.md` | Agent Skills (Claude/Codex/Cursor) | upgrade |
| 2 | Hooks | `hooks/{event}/` | Lifecycle hooks (Claude Code) | NOVO |
| 3 | Subagentes | `subagents/{nome}.md` | Subagents (Claude Code/Codex) | NOVO |
| 4 | Plugins | `plugins/{nome}/plugin.yaml` | Plugin format (Claude Code/Codex) | NOVO |
| 5 | MCP Servers | `mcp-servers/{nome}/server.py` | MCP 2025-11-25 | NOVO |
| 6 | Scripts | `scripts/maui_*.py` | — (próprio) | preservado |
| 7 | Procedures | `procedures/*.md` | — (próprio) | preservado |
| 8 | Reflexes | `procedures/reflexes/*.md` | — (próprio) | preservado |
| 9 | Operator Packs | `operator-packs/{tool}/` | AGENTS.md / CLAUDE.md / mcp.json | upgrade |
| 10 | Exec Requests | `exec-requests/*.yaml` | — (próprio) | preservado |
| 11 | Exec Reports | `exec-reports/*.yaml` | — (próprio) | preservado |
| 12 | Context Packages | `context-packages/{data,templates,generated}/` | — (próprio) | upgrade |
| 13 | Update Protocol | `schemas/update-*.yaml` + scripts | — (próprio) | upgrade |
| 14 | Schemas | `schemas/*.schema.yaml` | JSON Schema | upgrade |
| 15 | Evals | `evals/{skills,prompts,regression}/` | Promptfoo-style | NOVO |
| 16 | Automations | `automations/*.yaml` | Codex Automations-style | NOVO |
| 17 | Memória | `memoria/**/*.md` (herdada Saara) | — (próprio) | preservado |
| 18 | Adendos | `adendos/*.md` (herdado Saara) | — (próprio) | preservado |
| 19 | Insights | `insights/*.md` (herdado Saara) | — (próprio) | preservado |
| 20 | Configurações | `00_core/` + `01_manifest/` (herdadas) | — (próprio) | preservado |
| 21 | Documentação | `00_core/` + `README.md` + skills | — (próprio) | preservado |
| 22 | Toolkit | `maui-toolkit/` (fora) | — (próprio) | upgrade |

---

## 6. Matriz Função → PKA primária (revisão v0.2)

| Função Maui | PKA primária | PKAs apoio | Artefato |
|---|---|---|---|
| Definir system prompt Maui | Agent Engineering | Written Comms, AI Architect | System Prompt |
| Estrutura do corpus | AI Solutions Architect | Agent Engineering, Dev Engineer | Manifest/spec |
| Criar skills | Agent Engineering | Written Comms, Dev Engineer | SKILL.md |
| Criar hooks | Development Engineer | Agent Engineering | Script + manifest |
| Criar subagentes | Agent Engineering | Written Comms | Subagent .md |
| Criar plugins | Agent Engineering | Written Comms, Dev Engineer | Plugin bundle |
| Implementar MCP servers | Development Engineer | Agent Engineering, AI Architect | server.py + manifest |
| Criar scripts | Development Engineer | Agent Engineering | Script + tests |
| Criar procedures/reflexes | Agent Engineering | Written Comms | Markdown |
| Criar memórias/handoffs | Written Comms | Agent Engineering | Memória/context package |
| Gerar update package | Written Comms | Agent Engineering, Dev Engineer | Skill+script+template |
| Validar registry/drift | Development Engineer | Agent Engineering | Script/schema |
| Instanciar ferramenta | Agent Engineering | AI Architect, Written Comms | Operator pack |
| Definir topologia | AI Solutions Architect | Development Engineer | Arquitetura/spec |
| Criar evals | Development Engineer | Agent Engineering | Eval YAML + dataset |
| Criar automations | Development Engineer | Agent Engineering | Automation YAML |
| Planejar/fechar marcos | SAFe Agile Master | Agent Engineering, Written Comms | Runbook/memória |
| Curadoria multi-IA | SAFe Agile Master | AI Architect, Written Comms | Painel/procedure |
| Propor adendos | Agent Engineering | Written Comms, domínio | Skill/adendo |

Regra preservada: nem toda função técnica colapsa em Agent Engineering.

---

## 7. Mapeamento de migração — Saara Core → Maui v0.2

### 7.1 O que migra (atualizado v0.2)

| No Saara v7.1.1 (Core) | Em Maui v0.2 | Forma |
|---|---|---|
| `saara registry` | `scripts/maui_registry.py` + skill + procedure + schema + MCP tool | Distribuído |
| `saara memory index` | `scripts/maui_memory_index.py` + skill + schema + MCP tool | Distribuído |
| `saara memory search` | `scripts/maui_memory_search.py` + skill + MCP tool | Distribuído |
| `saara update plan` (B5) | Absorvido em `maui_update_export.py` + MCP tool | Consolidado |
| `saara update export` (B6) | `scripts/maui_update_export.py` + skill + MCP tool | Distribuído |
| `saara status` | `maui_registry.py list` + `maui_vault_health.py` + skill | Coordenado |
| Schemas | `schemas/*.schema.yaml` + JSON Schema standard | Padronizado |
| Testes do Core (152) | Distribuídos: testes unitários por script + evals por skill + integration tests | Reorganizado |
| `.saara/` | `.maui/` (mesma função) | Renomeado |

### 7.2 Configurações herdadas e ampliadas

| Saara v7.1.1 | Maui v0.2 | Status |
|---|---|---|
| System prompt v7.1.1 | `00_core/system-prompt.md` (atualizado para v0.2) | Atualização contemplada em M0 |
| 5 PKAs | `00_core/pka-*.md` | Preservadas |
| 6 specs subsidiárias | `00_core/spec-*.md` | Preservadas |
| Princípios fundacionais | `00_core/principios-fundacionais.md` | Preservado, +5 novos princípios v0.2 |
| spec-parametrizacao.json | `01_manifest/spec-parametrizacao.json` | Preservada, +novas seções |
| Setup .saara/ | `.maui/` | Renomeado, mesma função |

### 7.3 Documentação herdada e ampliada

| Tipo de doc | Saara v7.1.1 | Maui v0.2 |
|---|---|---|
| Normativa | `00_core/` | preservado |
| Identidade do produto | (implícito) | `01_manifest/` (explícito) |
| Operacional | README + memórias | README + skills + procedures |
| API | spec-parametrizacao.md | spec-parametrizacao.md + MCP server schemas |
| Templates | (implícito) | `context-packages/templates/` + `operator-packs/*/` (Jinja2) |
| Roadmap | `roadmap-v7-1-1.md` | preservado + roadmap-maui |
| Handoffs | `memoria/handoff-*.md` | `skills/maui-handoff-generate/` produz formalmente |

### 7.4 Atualizações herdadas e ampliadas

| Mecanismo Saara v7.1.1 | Maui v0.2 |
|---|---|
| `saara update plan` (B5) | Absorvido em `maui_update_export.py` |
| `saara update export` (B6) | `scripts/maui_update_export.py` + skill + MCP |
| Update via humano | Update Protocol completo (Request/Package/Report) |
| Manual de current.md | `maui_context_export.py` + templates Jinja2 |
| Versionamento Git | Preservado + automations para detectar mudança |

### 7.5 Memória herdada e ampliada

| Aspecto | Saara v7.1.1 | Maui v0.2 |
|---|---|---|
| Estrutura | `memoria/YYYY-MM/*.md` | preservado |
| Frontmatter | YAML | preservado + schema validado |
| Captura | Manual / Capture Layer | Manual + skill `maui-memory-create` + hook `Stop` |
| Indexação | `.saara/memory.db` | `.maui/memory.db` (mesma função) |
| Busca | `saara memory search` | `maui_memory_search.py` + skill + MCP tool |
| Validação | Não formalizada | `maui_validate_memory.py` + eval |

---

## 8. Princípios fundacionais — materialização v0.2

### 8.1 Soberania Cognitiva (levada ao limite²)

**v7.1.1:** corpus normativo no vault; capacidades operacionais no Core.
**v0.2:** capacidades operacionais (skills, hooks, subagents, plugins, MCP servers) também no corpus, **e aderem a padrões abertos da indústria** — substituibilidade vai além do backend, alcançando o ecossistema.

### 8.2 Lifecycle de Instanciação

**v7.1.1:** Tool Instance Registry no Core.
**v0.2:** mesmo registry + reforçado por hooks SessionStart + Update Protocol completo + MCP tool `check_drift`.

### 8.3 Context Injection → Context Engineering

**v7.1.1:** três camadas (A/B/C).
**v0.2:** três camadas + disciplina explícita de **Write/Select/Compress/Isolate**:

| Estratégia | Como Maui aplica |
|---|---|
| **Write** | Capture Layer + memórias persistentes |
| **Select** | Filtros + retrieval + re-ranking (Camada C) |
| **Compress** | Compactor + summarization automática |
| **Isolate** | Subagentes (contextos separados) + plugins (namespacing) |

### 8.4 Capture Layer

**v7.1.1:** captura via Capture Layer no Core.
**v0.2:** mesma + integrada com hooks `Stop`/`PostToolUse` + skill `maui-memory-create` + procedure de captura explícita.

### 8.5 Insight Pipeline

**v7.1.1:** Pattern Detector → Drafter → Human Gate.
**v0.2:** mesmo + automation semanal + subagent `maui-pattern-detector` + evals para validar adendos antes de promoção.

### 8.6 NOVOS princípios v0.2

| Princípio | Materialização |
|---|---|
| Adesão ao padrão aberto | SKILL.md, AGENTS.md, MCP, JSON Schema, plugin format |
| Determinismo onde possível | Hooks (não-alucinatórios) > prompts onde correção é não-negociável |
| Output contract first | Frontmatter de toda skill declara `outputs:` antes do body |
| Context engineering | Disciplina W/S/C/I aplicada a todo retrieve |
| Evals como código | `evals/` versionado, CLI `maui eval`, gate em adendos |

---

## 9. Riscos arquiteturais e mitigações (revisão v0.2)

| Risco | Severidade | Mitigação |
|---|---|---|
| Confusão Maui-corpus vs Maui-toolkit durante transição | Alta | `01_manifest/maui-toolkit-boundaries.md` explícito |
| Perda de testes do Saara Core | Média | Migrar incrementalmente para `tests/scripts/` + evals |
| Drift documental Saara/Maui simultâneos | Alta | Saara v7.1.1 vigente até promoção; Maui = proposta |
| Scripts pesados quebrando portabilidade | Média | Stdlib first; deps externas justificadas |
| Operator packs divergindo das ferramentas | Média | M12 valida cross-tool; ciclo de feedback |
| Update Protocol ignorado | Alta | System prompt + reflexes ativos |
| Fragmentação de scripts | Baixa | Schema + IO uniforme |
| **Aderência a padrão aberto cria amarras com fornecedores** (NOVO) | Média | Padrões adotados são open standards (Linux Foundation/AAIF); diversificar |
| **MCP servers expondo demais do corpus** (NOVO) | Alta | Allow-lists explícitas + scoped tokens + auditoria |
| **Hooks com side-effects inesperados** (NOVO) | Média | Hooks read-only por default; testes obrigatórios |
| **Subagentes vazando contexto sensível** (NOVO) | Alta | `allowed-tools` rigoroso + memory escopada |
| **Plugins de terceiros maliciosos** (NOVO) | Crítica | Auditoria obrigatória + escrutinio de SKILL.md como código |
| **Evals enviesando para o que é fácil testar** (NOVO) | Baixa | Mix de eval types (script + LLM judge + human) |
| **Automations rodando sem supervisão** (NOVO) | Alta | `human_gate: true` em automations que mudam estado |

---

## 10. Decisões abertas (revisão v0.2)

Decisões que esta spec **deliberadamente não fecha**:

**Preservadas da v1.0:**

1. Diretório-raiz: `vault-maui/` ou camada em `vault-saara/`?
2. Escopo do `hash_config`: incluir scripts/skills/procedures/manifest?
3. `context-packages/generated/` versionado ou regenerado?
4. `.maui/` vs `.saara/`?
5. Versionamento: Maui v0.2 standalone ou Saara/Maui v7.2?
6. Adendos Maui em Saara v7.1.1 ou branch separada?
7. Primeiro piloto operator pack: Claude Code, Codex, ambos?
8. B6 (`saara update export`): encerrado como Saara ou primeiro script Maui?
9. Painel: CLI, plugin Obsidian, UI?
10. Update Package: só Markdown ou também YAML/JSON?
11. Testes do Core: portar antes ou incrementalmente?

**Novas v0.2:**

12. **Hooks runtime:** Python stdlib ou aceitamos Node.js para hooks frontend-related?
13. **MCP transport:** stdio para todos local + HTTP para remote, ou escolher por server?
14. **Subagent model default:** nominal ou Master-Clone como default?
15. **Plugin marketplace:** próprio repositório Git ou aderir a registry existente?
16. **Eval framework:** Promptfoo, DSPy ou suite custom?
17. **Skills compartilhadas (`.agents/skills/`):** symlinks ou cópias?
18. **MCP authentication:** OAuth 2.1, API key estática ou ambos?
19. **Automations engine:** cron, Temporal (mcp-agent-style) ou GitHub Actions?
20. **Sampling/Elicitation:** habilitados desde MVS ou só após M7?
21. **Plugins de terceiros:** permitir ou apenas plugins próprios no MVS?

---

## 11. Roadmap de adoção v0.2

| Marco | Objetivo | Status | Mudança v0.2 |
|---|---|---|---|
| M0 | Decisão e baseline Maui | Próximo | preservado |
| M1 | Manifesto e estrutura (`01_manifest/`) | Aguarda M0 | +execution/quality/standards layers |
| M2 | Schemas mínimos | Aguarda M1 | +hook/subagent/plugin/mcp/eval/automation schemas |
| M3 | Scripts P0 | Aguarda M2 | +`maui_eval_run.py` |
| M4 | Skills P0 (padrão aberto SKILL.md) | Aguarda M3 | upgrade |
| **M4.5** | **Hooks P0** | Aguarda M4 | NOVO |
| **M4.6** | **Subagentes P0** | Aguarda M4 | NOVO |
| **M4.7** | **MCP servers P0** | Aguarda M4 | NOVO |
| M5 | Procedures e reflexes | Aguarda M4 | preservado |
| M6 | Operator Packs (com mcp-config) | Aguarda M5 | upgrade |
| M7 | Update Protocol completo | Aguarda M6 | preservado |
| M8 | Context packages gerados | Aguarda M3 | preservado |
| M9 | Maui Toolkit (com mcp-launch + eval) | Aguarda M6 | upgrade |
| **M9.5** | **Evals P0** | Aguarda M4 + M9 | NOVO |
| **M9.6** | **Automations P0** | Aguarda M4 + M9 | NOVO |
| **M9.7** | **Plugins P0** | Aguarda M4–M6 | NOVO |
| M10 | Painel multi-IA | Aguarda M9 | preservado |
| M11 | Adendos e promoção normativa | Aguarda M7 + M9.5 | upgrade |
| M12 | Validação cross-tool | Aguarda M11 | upgrade |

Roadmap detalhado vive em `roadmap-maui-v0-2.md` (a criar em M0).

---

## 12. Suíte mínima de testes da transição (revisão v0.2)

Cenários que devem passar ao final da adoção:

**Preservados da v1.0:**

- TC1: `maui init` cria estrutura mínima válida
- TC2: `maui instantiate --target claude-code` gera operator pack consumível
- TC3: `maui_registry.py list` reporta instâncias
- TC4: `maui_memory_index.py` indexa memórias herdadas sem perda
- TC5: `maui_context_export.py` produz pacote equivalente ao manual
- TC6: `maui_update_export.py` produz Update Package coerente
- TC7: Instância sem fs gera Update Request válido
- TC8: Update Package integrável + autoteste passa
- TC9: Vault Health roda sem erros
- TC10: Validações de frontmatter/links/memórias passam
- TC11: Saara v7.1.1 continua operacional durante coexistência
- TC12: Hash determinístico cross-machine

**Novos v0.2:**

- TC13: Skill `maui-vault-health` ativa automaticamente quando query menciona "saúde do vault"
- TC14: Hook `maui-block-corpus-write` impede edição em `00_core/` sem gate
- TC15: Subagente `maui-doc-reviewer` revisa PKA sem editar
- TC16: Plugin `maui-core-essentials` instala sem conflito
- TC17: MCP server `maui-corpus-server` conecta com Claude Desktop
- TC18: Skill compartilhada em `.agents/skills/` funciona em Claude Code E Codex
- TC19: Eval suite roda em < 60s para conjunto base
- TC20: Automation com `human_gate: true` nunca aplica sem aprovação
- TC21: Operator pack Claude Code gera `mcp-config.json` válido
- TC22: Sampling/Elicitation funcionam end-to-end em MCP server

---

## 13. Critérios de aceitação da transição (revisão v0.2)

Maui v0.2 é considerado **adotado** quando:

**Preservados da v1.0:**

1. M0–M7 concluídos.
2. Pelo menos um operator pack (Claude Code) validado em uso real.
3. Pelo menos uma instância atualizada via Update Protocol completo.
4. Validação cross-tool ≥ 8/12 TCs preservados.
5. Decisão formal de governança registrada.
6. Adendos Maui aprovados via Human Gate.
7. Saara Core reclassificado como `maui-toolkit/` ou descontinuado.
8. Context package atual reflete estado Maui.

**Novos v0.2:**

9. Pelo menos uma skill no padrão aberto SKILL.md validada em ≥ 2 ferramentas.
10. Pelo menos um MCP server Maui operacional.
11. Pelo menos um plugin Maui distribuído.
12. Suite de evals para skills P0 cobrindo ≥ 80%.
13. Pelo menos uma automation com `human_gate` rodando em produção.
14. Validação cross-tool v0.2 ≥ 7/10 TCs novos.

---

## 14. Comparação v1.0 vs v2.0 — síntese

| Aspecto | v1.0 | v2.0 |
|---|---|---|
| Funcionalidades core | 16 | 22 (preservadas + 6 novas) |
| Camadas arquiteturais | implícitas | 6 explícitas |
| Padrão aberto | mencionado | central |
| Skills | formato próprio | Agent Skills standard |
| Hooks | ausente | camada nativa |
| Subagentes | ausente | modelo dual |
| Plugins | ausente | distribuição nativa |
| MCP servers | mencionado | primeira classe |
| Evals | ausente | gate de qualidade |
| Automations | ausente | cadência separada |
| Context Engineering | Context Injection | Write/Select/Compress/Isolate |
| Princípios novos | 0 | 5 |
| Operator packs | nativos + skills | nativos + neutro `.agents/skills/` + MCP |
| Update Protocol | apenas humano | + MCP tool |
| Riscos | 7 | 14 (7 + 7 novos) |
| Decisões abertas | 11 | 21 (11 + 10 novas) |
| Marcos roadmap | 12 (M0–M12) | 18 (M0–M12 + 6 sub-marcos) |
| Suíte testes | 12 TCs | 22 TCs |

---

## 15. F/I/H

### 15.1 Fatos

- Saara v7.1.1 é base normativa atual.
- Nova geração foi nomeada Maui em 2026-05-01.
- Spec v1.0 (2026-05-04) contratou 16 funcionalidades.
- Em 2026, a indústria de agentes convergiu em padrões abertos: Agent Skills (`SKILL.md`), AGENTS.md, MCP, plugin format.
- Claude Code, Codex, Cursor, Gemini CLI e Antigravity adotaram convenção `.agents/skills/`.
- MCP foi doado à Linux Foundation/AAIF em dez/2025 com OpenAI e Block.
- Hooks de Claude Code suportam ~25 eventos lifecycle.
- Codex tem AGENTS.md como contraparte de CLAUDE.md.
- OpenAI lançou Workspace Agents (abril/2026) como evolução de GPTs.
- Promptfoo e DSPy são padrões de fato em evals 2026.
- Skills de elite (Frontend Design, Excalidraw, etc.) usam progressive disclosure por filesystem.

### 15.2 Inferências

- Maui se beneficia mais de aderir ao padrão aberto do que de criar formato próprio.
- Hooks resolvem categoria de problema (enforcement determinístico) que prompts não resolvem.
- Subagentes são úteis mas controversos; modelo dual é decisão prudente.
- MCP servers expondo capacidades Maui ampliam alcance sem comprometer soberania.
- Evals como código eleva qualidade de skills críticas.
- Automations transformam workflows estáveis em rotina sem aumentar carga humana.
- Plugins permitem distribuição interna entre projetos do mesmo usuário/equipe.
- Coexistência Saara v7.1.1 + Maui v0.2 ainda é prudente — 30-90 dias.

### 15.3 Hipóteses

- Maui v0.2 nascerá como proposta + memória + adendo antes de promoção formal.
- B6 será reinterpretado como `maui_update_export.py` com adaptações.
- Painel MVS começará file-based/CLI; UI vem depois.
- `hash_config` em Maui v0.2 incluirá `scripts/`, `skills/`, `hooks/`, `subagents/`, `01_manifest/`.
- O padrão aberto Agent Skills se consolidará e Anthropic + OpenAI + Google convergirão ainda mais.
- MCP webhooks (roadmap H2 2026) abrirão padrão para captura proativa.
- Stateless HTTP MCP (roadmap 2026) facilitará escala dos MCP servers Maui.
- A2A (Agent-to-Agent) eventualmente entra no Maui para curadoria multi-IA.

---

## 16. Próximos passos imediatos

1. Revisar esta spec contra Handoff Maui, context package corrente e v1.0.
2. Salvar como memória de proposta arquitetural v2.
3. Decidir governança: spec vira adendo ou versão maior?
4. Resolver decisões abertas críticas (§10): pelo menos diretório-raiz, versionamento, primeiro piloto e MCP transport default.
5. Iniciar M0 do roadmap Maui (memória de decisão).
6. Validar com Claude Code real um POC de skill compartilhada Maui (`.agents/skills/maui-vault-health/`).

---

## Apêndice A — Glossário v0.2

| Termo | Definição |
|---|---|
| **Agent Skills** | Padrão aberto para skills (`SKILL.md` + frontmatter) compatível com Claude Code, Codex, Cursor, Gemini CLI |
| **AGENTS.md** | Contraparte do CLAUDE.md para Codex; convenção de instruções persistentes por projeto |
| **Automation** | Tarefa agendada que executa skill com cadência definida |
| **Context Engineering** | Disciplina de assembly de contexto (Write/Select/Compress/Isolate) |
| **Eval** | Teste versionado de skill/script/prompt |
| **Hook** | Script disparado em evento lifecycle (PreToolUse, SessionStart, etc.) |
| **MCP** | Model Context Protocol; padrão aberto para integração de agentes |
| **Operator Pack** | Bundle de adaptação por ferramenta (CLAUDE.md, AGENTS.md, mcp-config) |
| **Plugin** | Bundle distribuível (skills + hooks + subagents + commands) |
| **Skill** | Capacidade reutilizável em formato SKILL.md aberto |
| **Subagente** | Especialista isolado em contexto próprio |
| **Master-Clone** | Padrão alternativo: agente principal usa Task() para spawnar clones |
| **Sampling** | Capacidade MCP de servidor pedir ao LLM gerar texto |
| **Elicitation** | Capacidade MCP de servidor pedir input ao humano |
| **Update Request/Package/Report** | Tríade do Update Protocol Maui |

---

## Apêndice B — Mapeamento padrões abertos × diretórios Maui

| Padrão aberto | Diretório nativo | Convenção neutra | Operator Pack |
|---|---|---|---|
| Agent Skills (SKILL.md) | `vault-maui/skills/` | `.agents/skills/` | symlink ou cópia |
| AGENTS.md | — | — | `operator-packs/codex/AGENTS.md.j2` |
| CLAUDE.md | — | — | `operator-packs/claude-code/CLAUDE.md.j2` |
| Hooks | `vault-maui/hooks/` | — | `operator-packs/claude-code/hooks.example.json` |
| Subagents | `vault-maui/subagents/` | `.claude/agents/` | symlink ou cópia |
| Plugins | `vault-maui/plugins/` | `.claude/plugins/` | dependência |
| MCP servers | `vault-maui/mcp-servers/` | `mcp.json` config | `operator-packs/*/mcp-config.json.j2` |
| JSON Schema | `vault-maui/schemas/` | — | — |

---

**FIM — Spec Técnica Atualização Saara → Maui v0.2 (spec_versao 2.0)**
