---
titulo: Spec Técnica — Atualização Saara → Maui
versao: 0.1
spec_versao: 1.0
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
precedencia: 5
compatibilidade:
  - saara_v7_1_1
  - principios_fundacionais_saara_v7_1_1
  - handoff_maui_v0_1
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
tags:
  - maui
  - saara
  - atualizacao
  - especificacao-tecnica
  - corpus-procedural
  - scripts-condicionamento
  - operator-packs
  - update-protocol
---

# Spec Técnica — Atualização Saara → Maui

> Especificação detalhada da transição arquitetural entre **Saara v7.1.1** e **Maui v0.1**. Documenta o reposicionamento conceitual, descreve a estrutura-alvo do corpus e contrata todas as funcionalidades que o corpus do Maui deve conter, com entradas, saídas, comportamentos, dependências e critérios de funcionamento.
>
> Esta spec consolida o trabalho dos papéis de **Arquiteto de Soluções** (arquitetura-alvo, fronteiras, trade-offs), **Engenheiro de Desenvolvimento** (contratos executáveis, IO, comportamentos) e **Written Comms** (organização, clareza, navegabilidade).

---

## 0. Status e governança

### 0.1 Status

`status: proposta` — esta spec descreve uma evolução proposta. Não substitui Saara v7.1.1 silenciosamente. A adoção formal exige decisão explícita de governança, registrada como memória e adendo.

### 0.2 Precedência

Esta spec opera no nível 5 da precedência operacional do Saara (PKAs + specs técnicas subsidiárias). Em conflito conceitual, prevalecem:

1. Políticas externas
2. System Prompt ativo
3. Princípios Fundacionais Saara v7.1.1
4. Especificação Completa Saara v7.1.1
5. **Esta spec** (paritária com PKAs e demais specs técnicas)

### 0.3 Stop rule

Onde esta spec não cobrir um aspecto, valem as specs Saara v7.1.1 vigentes. Lacunas materiais devem ser sinalizadas, não inventadas.

---

## 1. Resumo executivo

### 1.1 O que muda

O Saara v7.1.1 já estabelecia o **Princípio da Soberania Cognitiva**: a identidade do Saara vive no corpus versionado, não na infraestrutura. Na prática, porém, o `saara-core` estava crescendo como software substancial — 152 testes, comandos sendo desenvolvidos como módulos Python, B5/B6 entregues como funcionalidades de um backend.

Maui resolve essa tensão por **reclassificação radical**:

- O `saara-core` deixa de ser o centro do produto e passa a ser **toolkit auxiliar**.
- Funções que estavam virando módulos do Core (`registry`, `memory-index`, `context-export`, `update-export`) descem para dentro do corpus como **scripts de condicionamento**.
- O corpus passa a conter, além de conhecimento normativo, suas próprias capacidades executáveis (skills, procedures, scripts, schemas) e seus mecanismos de adaptação a ferramentas (operator packs, exec requests/reports).

### 1.2 O que não muda

- Os 5 Princípios Fundacionais do Saara v7.1.1 permanecem válidos e são **levados ao limite** pela arquitetura Maui.
- As 5 PKAs do Saara v7.1.1 são herdadas integralmente (Agent Engineering, Development Engineer, AI Solutions Architect Elite, Written Comms Core, SAFe Agile Master Elite — esta última ativo condicional).
- O system prompt v7.1.1 continua vigente até decisão explícita de promoção a versão Maui.
- O modelo de governança (precedência, stop rule, anti-drift, F/I/H) é preservado.

### 1.3 Equação que resume Maui

```
Maui = corpus + memória + PKAs + specs + adendos + insights
       + skills + procedures + scripts + schemas + operator-packs
       + exec-requests + exec-reports
```

Qualquer modelo de IA com filesystem ou interface conversacional deve conseguir instanciar e operar Maui a partir dessa estrutura, sem dependência de backend específico.

---

## 2. Arquitetura — Visão do Arquiteto de Soluções

### 2.1 Mudança arquitetural central

```
ANTES (Saara v7.1.1)                     DEPOIS (Maui v0.1)
─────────────────────                    ──────────────────

  ┌────────────────┐                       ┌──────────────────┐
  │   vault-saara/ │                       │   vault-maui/    │
  │   (corpus)     │ ◄──────┐              │   (corpus +      │
  └────────────────┘        │              │    capacidades)  │
                            │              └──────────────────┘
                            │ lê/escreve            │ ▲
                            │                       │ │ lê/colabora
  ┌────────────────┐        │              ┌────────▼─┴───────┐
  │  saara-core/   │ ───────┘              │  maui-toolkit/   │
  │  (backend      │                       │  (auxiliar:      │
  │   substancial) │                       │   init/inst./    │
  └────────────────┘                       │   panel)         │
                                           └──────────────────┘

  Identidade dispersa:                     Identidade unificada:
  corpus (normativo) +                     tudo no corpus,
  Core (procedural)                        toolkit é apoio
```

### 2.2 Princípios arquiteturais

| Princípio Saara v7.1.1 | Aplicação em Maui |
|---|---|
| Soberania Cognitiva | Levada ao limite: capacidades executáveis também vivem no corpus |
| Lifecycle de Instanciação | Preservado; reforçado pelo protocolo Update Request/Package/Report |
| Context Injection Sob Demanda | Preservado; context packages passam a ser geráveis por script |
| Capture Layer | Preservado; pode ser invocada por skill ou procedure |
| Insight Pipeline | Preservado; passa a ser executável via scripts de condicionamento |

### 2.3 Fronteiras

**O que Maui é:**

- Corpus cognitivo multipapel, procedural, portátil, instanciável.

**O que Maui não é:**

- Aplicação SaaS, app desktop, chatbot único, backend, banco de dados, MCP server, interface específica, ferramenta de IA específica.

**Fronteira Corpus / Toolkit / Operator:**

- **Corpus (`vault-maui/`)**: identidade, normativo, procedural, executável-mas-portátil.
- **Toolkit (`maui-toolkit/`)**: ferramentas de bootstrap (init, instantiate, panel). Não é o produto.
- **Operator (`vault-maui/operator-packs/`)**: adaptadores por ferramenta, vivem no corpus mas são consumidos por ferramentas externas.

### 2.4 Topologia-alvo

Local-first por padrão. Tool-agnostic por design. Multi-ferramenta por necessidade operacional.

```
┌─────────────────────────────────────────────────────┐
│              vault-maui/ (corpus)                    │
│   ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐    │
│   │ 00_core│  │ skills │  │scripts │  │op-packs│    │
│   └────────┘  └────────┘  └────────┘  └────────┘    │
└──────────────┬──────────────────────────────────────┘
               │
       ┌───────┴────────┬─────────────┬──────────────┐
       │                │             │              │
       ▼                ▼             ▼              ▼
  ┌────────┐      ┌─────────┐   ┌────────┐    ┌───────────┐
  │ Claude │      │  Codex  │   │ChatGPT │    │  Gemini   │
  │  Code  │      │         │   │        │    │           │
  └────────┘      └─────────┘   └────────┘    └───────────┘
   (filesystem)   (filesystem)  (sem fs)      (sem fs)
       │              │             │              │
       └──────────────┴─────────────┴──────────────┘
                          │
                  Update Request/
                  Package/Report
```

---

## 3. Estrutura-alvo do corpus Maui

### 3.1 Diretórios canônicos

```
vault-maui/
├── 00_core/                # Normativo herdado/evoluído (system prompt, especificação,
│                           # princípios, PKAs, specs)
├── 01_manifest/            # Definição formal do produto e estrutura
│   ├── maui-product-definition.md
│   ├── maui-vault-structure.md
│   ├── maui-file-format-policy.md
│   ├── maui-toolkit-boundaries.md
│   ├── maui-runtime-model.md
│   └── maui-procedural-layer.md
├── memoria/                # Memórias operacionais e episódicas
├── adendos/                # Evoluções incrementais aprovadas
├── insights/               # Padrões consolidados
├── skills/                 # Capacidades executáveis por agentes
│   └── {nome-skill}/
│       └── SKILL.md
├── procedures/             # Runbooks, reflexos e protocolos
│   ├── procedimento-*.md
│   └── reflexes/
│       └── reflexo-*.md
├── scripts/                # Scripts de condicionamento
├── schemas/                # Contratos e validações
├── context-packages/       # Pacotes de contexto
│   ├── data/               # Dados YAML de entrada
│   ├── templates/          # Templates Jinja2
│   └── generated/          # Pacotes gerados
├── operator-packs/         # Adaptação por ferramenta
│   ├── claude-code/
│   ├── codex/
│   ├── chatgpt/
│   ├── gemini/
│   └── antigravity/
├── exec-requests/          # Pedidos para agentes executores
├── exec-reports/           # Relatórios de execução
├── exports/                # Artefatos gerados
├── validations/            # Relatórios de validação
└── README.md
```

### 3.2 Toolkit auxiliar

```
maui-toolkit/
├── init/                   # Monta estrutura inicial do corpus
├── instantiate/            # Gera primeira instância para uma ferramenta
├── panel/                  # Curadoria multi-IA
└── README.md
```

### 3.3 Política de formatos

| Formato | Uso |
|---|---|
| Markdown + YAML frontmatter | Conhecimento humano e contexto para IA (`00_core/`, memórias, adendos, insights, skills, procedures) |
| YAML | Configuração e contratos editáveis (operator packs, schemas instanciados, instancia.yaml) |
| JSON | Saída de scripts/APIs (`--json`) |
| JSONL | Eventos e logs append-only |
| SQLite | Índices reconstruíveis (`.maui/memory.db`) |
| Jinja2 (`.md.j2`, `.yaml.j2`) | Templates |
| JSON Schema / YAML Schema | Validação de schemas |

---

## 4. Funcionalidades do corpus Maui — Visão do Engenheiro de Desenvolvimento

Esta seção contrata cada funcionalidade que o corpus Maui deve conter. Para cada uma:

- **Definição** — o que faz e por que existe
- **Localização** — onde vive no corpus
- **Entradas** — IO de entrada
- **Saídas** — IO de saída
- **Comportamento** — fluxo interno
- **Necessidades** — dependências
- **Critérios de funcionamento** — como saber que funciona

### Princípios transversais (aplicam-se a todas as funcionalidades)

1. **Read-only por padrão.** Escritas exigem flag explícita (`--apply`, `--write-patch`).
2. **Idempotência.** Executar o mesmo comando duas vezes não corrompe estado.
3. **Saída dual.** Todo script suporta `--json` e `--markdown` quando aplicável.
4. **Sem sync automático.** Reconciliação exige intervenção humana ou autorização explícita.
5. **Determinismo.** Mesma entrada produz mesma saída (exceto carimbos de tempo).
6. **Portabilidade.** Scripts não dependem de bibliotecas esotéricas; preferência por stdlib Python.
7. **Validação prévia.** Toda escrita valida schema antes de gravar.
8. **Auditoria.** Toda operação significativa registra evento em log estruturado.

---

### 4.1 Registry — Gestão de instâncias

#### Definição

Mantém o **Tool Instance Registry**: estado verificável de cada instância Maui em ferramentas-cliente (Claude Project, Custom GPT, Gem, Claude Code repo, etc.). Substitui o módulo `registry` do antigo `saara-core` por um conjunto coordenado de script + schema + procedure + skill que vive no corpus.

#### Localização

```
scripts/maui_registry.py
schemas/registry.schema.yaml
procedures/procedimento-gerenciar-registry.md
skills/maui-registry-maintenance/SKILL.md
```

#### Entradas

- `instancia.yaml` (ou múltiplos) descrevendo `tool_id`, `tool_type`, `platform`, `known_hash`, `known_version`, `last_seen`.
- Estado atual do corpus (lido do filesystem) para cálculo de hash.
- Flags CLI: `--tool-id`, `--json`, `--markdown`, `--apply`.

#### Saídas

- Lista de instâncias com status (`current`, `drift_minor`, `drift_major`, `incompatible`, `unknown`).
- Relatório de drift por instância.
- Plano de reconciliação (sem aplicar por padrão).
- Arquivo persistido (opcional, com `--apply`): `.maui/instances.db` ou `.maui/instances-snapshot.json`.

#### Comportamento

```
list:
  ler arquivos de instância → projetar status atual → emitir tabela

check --tool-id X:
  ler instancia X → recalcular hash atual → comparar →
  emitir status + diferença

diff --tool-id X:
  como check, mas detalha o que mudou (adendos, PKAs, etc.)

reconcile-plan --tool-id X:
  como diff + propõe sequência de ações (sem executar)
```

#### Necessidades

- Acesso ao filesystem do corpus.
- Função de cálculo de hash determinístico (compartilhada com `maui_update_export.py`).
- Schema de registry validado.

#### Critérios de funcionamento

- `python scripts/maui_registry.py list --json` retorna JSON válido com todas as instâncias declaradas.
- `check` em instância nunca declarada retorna status `unknown` sem inventar dados.
- `reconcile-plan` nunca aplica mudanças por padrão; exige `--apply` explícito.
- Schema rejeita YAMLs malformados antes de qualquer cálculo.

---

### 4.2 Memory Index — Indexação de memórias

#### Definição

Indexa as memórias operacionais em `memoria/**/*.md` para busca rápida. Substitui o módulo `memory-index` do antigo `saara-core`. O **arquivo Markdown é a fonte de verdade**; o índice é técnico e reconstruível.

#### Localização

```
scripts/maui_memory_index.py
scripts/maui_memory_search.py
schemas/memory.schema.yaml
procedures/procedimento-indexar-memorias.md
skills/maui-memory-maintenance/SKILL.md
```

#### Entradas

- `memoria/**/*.md` — fonte de verdade.
- Schema `memory.schema.yaml` para validação de frontmatter.
- Flags CLI: `--rebuild`, `--validate-only`, `--query`, `--limit`, `--filter`, `--json`.

#### Saídas

- Índice persistido: `.maui/memory.db` (SQLite) ou `.maui/memory-index.jsonl`.
- Relatório de validação: arquivos com frontmatter inválido, memórias órfãs, duplicações.
- Resultado de busca: lista ordenada de memórias relevantes com snippets.

#### Comportamento

```
maui_memory_index.py:
  varrer memoria/**/*.md → validar frontmatter contra schema →
  extrair metadados (data, tags, escopo, tipo) →
  indexar conteúdo (FTS) → emitir relatório de inválidos

maui_memory_search.py --query "..." --filter escopo=trabalho:
  consultar índice → aplicar filtros de metadados →
  busca textual (FTS) → re-rank por recência/relevância → emitir top-K
```

#### Necessidades

- Schema de memória validado.
- SQLite (Python stdlib) ou suporte a JSONL.
- Função de hash de conteúdo para detectar mudanças.

#### Critérios de funcionamento

- Indexação de 1000 memórias completa em menos de 30s em hardware comum.
- Frontmatter inválido nunca corrompe o índice; entrada é rejeitada com log claro.
- Busca por escopo `pessoal` nunca retorna memórias `trabalho` sem flag explícita.
- Reindexação é idempotente: rodar duas vezes produz o mesmo estado.

---

### 4.3 Context Export — Geração de Context Packages

#### Definição

Gera context packages compactos por target (Claude Code, Codex, ChatGPT, Gemini, etc.) a partir de dados YAML + templates Jinja2. Substitui o módulo `context-export` do antigo `saara-core`. **Substitui a edição manual de `current.md`** por geração estruturada.

#### Localização

```
scripts/maui_context_export.py
context-packages/data/             # Dados YAML por contexto/target
context-packages/templates/        # Templates .md.j2
context-packages/generated/        # Pacotes gerados
procedures/procedimento-exportar-contexto.md
skills/maui-context-export/SKILL.md
```

#### Entradas

- `context-packages/data/*.yaml` — dados estruturados (estado atual, marcos, decisões, hashes).
- `context-packages/templates/{target}.md.j2` — templates por target.
- Flags CLI: `--target`, `--all-targets`, `--compact`, `--budget`, `--output`, `--data-file`.

#### Saídas

- Markdown compacto em `exports/` ou `context-packages/generated/`.
- Manifesto da geração (data, hash do corpus, versão dos templates usados).

#### Comportamento

```
maui_context_export.py --target claude-code:
  carregar data/{target}.yaml + data/common.yaml →
  renderizar templates/{target}.md.j2 →
  validar tamanho contra budget → emitir Markdown

--all-targets:
  iterar sobre todos os targets registrados em pack.yaml

--compact:
  remove seções marcadas como expansíveis
```

#### Necessidades

- Jinja2 (única dependência externa não-stdlib).
- Schema de context package validado.
- Convenção de naming entre `data/{target}.yaml`, `templates/{target}.md.j2` e operator pack correspondente.

#### Critérios de funcionamento

- Pacote gerado para Claude Code é coerente com o operator pack `operator-packs/claude-code/`.
- Pacote `--compact` cabe dentro do budget declarado para o target.
- Geração é determinística: mesma data + mesmo template + mesmo corpus → mesmo output (módulo carimbo de tempo).
- Pacotes geradoss não são versionados por padrão (decisão aberta — ver §10).

---

### 4.4 Update Export — Geração de Update Packages

#### Definição

Recebe declaração de estado de uma instância (Update Request) e gera o pacote de atualização (Update Package) com o delta necessário. Substitui o que era B6 do `saara-core`.

#### Localização

```
scripts/maui_update_export.py
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
skills/maui-update-export/SKILL.md
skills/maui-instance-update-check/SKILL.md
skills/maui-instance-integrate-update/SKILL.md
```

#### Entradas

- `instancia.yaml` ou `exec-requests/{request}.yaml` validado contra `update-request.schema.yaml`.
- Estado atual do corpus.
- Flags CLI: `--from-file`, `--request`, `--output`, `--markdown`, `--json`.

#### Saídas

- Update Package em Markdown (humano-colável) e/ou JSON.
- Autoteste embutido no pacote.
- Não altera registry por padrão (apenas leitura).

#### Comportamento

```
maui_update_export.py --from-file instancia.yaml:
  validar request contra schema →
  ler corpus atual → calcular hash atual →
  comparar com known_hash do request →
  computar delta (PKAs novas, adendos, marcos, decisões) →
  renderizar Update Package via template →
  embutir autoteste de continuidade
```

#### Necessidades

- Função compartilhada de hash (mesma do `maui_registry.py`).
- Templates de Update Package.
- Schemas validados.

#### Critérios de funcionamento

- Request com `known_hash: desconhecido` produz pacote completo (full sync).
- Request com hash idêntico ao atual produz pacote vazio (no-op) com mensagem clara.
- Pacote sempre inclui autoteste com 4-5 perguntas mínimas.
- Script nunca escreve em `memoria/` nem em `00_core/`; apenas em `exports/`.

---

### 4.5 Frontmatter Validation

#### Definição

Valida frontmatter YAML de todos os arquivos Markdown do corpus contra os schemas correspondentes.

#### Localização

```
scripts/maui_validate_frontmatter.py
schemas/{tipo}.schema.yaml
```

#### Entradas

- Caminhos de arquivos `.md` (default: corpus inteiro).
- Schemas em `schemas/`.
- Flags CLI: `--path`, `--schema`, `--strict`, `--json`.

#### Saídas

- Relatório de validação: arquivos válidos, arquivos com erros, campos faltantes.
- Exit code não-zero em modo `--strict` se houver erros.

#### Comportamento

Identifica o tipo do documento pelo campo `tipo:` no frontmatter, seleciona o schema correspondente, valida.

#### Critérios de funcionamento

- Arquivos sem `tipo:` são reportados (não silenciosamente ignorados).
- Schemas faltantes geram aviso, não erro fatal.
- Integrável em pre-commit hook do Git.

---

### 4.6 Link Validation

#### Definição

Valida links internos `[[wikilink]]` e referências cruzadas no frontmatter (`referencias:`).

#### Localização

```
scripts/maui_validate_links.py
```

#### Entradas

- Corpus inteiro.
- Flags CLI: `--path`, `--strict`, `--json`.

#### Saídas

- Relatório de links quebrados, links órfãos (arquivo sem nenhum link de entrada), duplicações.

#### Comportamento

Constrói grafo de links e verifica integridade referencial. Não corrige automaticamente.

#### Critérios de funcionamento

- Detecta `[[link]]` que não corresponde a nenhum arquivo.
- Detecta `referencias:` com entradas inexistentes.
- Não falha em links externos (URLs).

---

### 4.7 Memory Validation

#### Definição

Validação semântica de memórias (além do frontmatter): presença de seções esperadas, F/I/H quando aplicável, escopo coerente.

#### Localização

```
scripts/maui_validate_memory.py
```

#### Entradas

- Memórias em `memoria/**/*.md`.

#### Saídas

- Relatório por memória: válida, com avisos, com erros.

#### Comportamento

Aplica regras semânticas declarativas (em YAML) sobre cada memória.

#### Critérios de funcionamento

- Memória de fechamento de marco sem seção "decisões" gera aviso.
- Memória com `confidencialidade: sensivel` sem sanitização explícita gera erro.

---

### 4.8 Vault Health

#### Definição

Diagnóstico geral de saúde do corpus: conta arquivos, valida estrutura de diretórios, executa subset de validações, gera score.

#### Localização

```
scripts/maui_vault_health.py
skills/maui-vault-health/SKILL.md
```

#### Entradas

- Corpus inteiro.
- Flags CLI: `--full`, `--json`, `--markdown`.

#### Saídas

- Relatório consolidado com seções: estrutura, frontmatter, links, memórias, índices, scripts.

#### Comportamento

Orquestra os scripts de validação anteriores e consolida resultados.

#### Critérios de funcionamento

- Roda em menos de 60s em corpus de tamanho médio.
- Saída Markdown legível por humanos sem ferramentas adicionais.

---

### 4.9 Skills — Capacidades executáveis

#### Definição

**Skills** são capacidades operacionais reutilizáveis, descritas em `SKILL.md`, que ensinam um agente (humano ou IA) a executar uma operação combinando scripts, procedures e contexto. São o equivalente Maui das "habilidades documentadas" — diferente de scripts (que são determinísticos) e diferente de procedures (que são runbooks).

#### Localização

```
skills/{nome-da-skill}/
├── SKILL.md           # contrato da skill
├── README.md          # opcional, contexto adicional
└── examples/          # opcional, exemplos
```

#### Skills mínimas (P0) previstas

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
```

#### Estrutura mínima de SKILL.md

```yaml
---
name: maui-{nome}
description: "Descrição curta + triggers"
status: ativo | proposta
versao: 0.1
inputs: [...]
outputs: [...]
scripts_chamados: [...]
procedures_relacionadas: [...]
---

# {Nome da skill}

## Quando usar
## Como executar
## Saída esperada
## Falhas comuns
```

#### Critérios de funcionamento

- SKILL.md valida contra `schema/skill.schema.yaml`.
- Skill aponta para script(s) e/ou procedure(s) consistentes com sua descrição.
- Skill nunca contém lógica executável; apenas descrição.

---

### 4.10 Procedures — Runbooks e reflexos

#### Definição

**Procedures** são runbooks textuais para operações recorrentes. **Reflexes** são procedures gatilhadas por condições — "se X, então rodar procedimento Y".

#### Localização

```
procedures/
├── procedimento-gerenciar-registry.md
├── procedimento-indexar-memorias.md
├── procedimento-exportar-contexto.md
├── procedimento-verificar-atualizacoes.md
├── procedimento-integrar-atualizacao.md
├── procedimento-criar-memoria.md
├── procedimento-captura-explicita.md
├── procedimento-curadoria-painel.md
└── reflexes/
    ├── reflexo-se-hash-mudou.md
    ├── reflexo-se-context-package-defasado.md
    ├── reflexo-se-instancia-pede-update.md
    └── reflexo-se-frontmatter-invalido.md
```

#### Estrutura mínima

```yaml
---
tipo: procedimento | reflexo
nome: ...
gatilho: (apenas para reflexos) condição
status: ativo
---

# {Nome}

## Objetivo
## Pré-requisitos
## Passos
## Validação
## Falhas conhecidas
```

#### Critérios de funcionamento

- Procedimento referencia skills e scripts existentes.
- Reflexo declara gatilho operacional verificável.
- Procedimento é executável manualmente por um humano competente sem contexto adicional.

---

### 4.11 Operator Packs — Adaptação por ferramenta

#### Definição

**Operator Packs** são pacotes de adaptação que ensinam uma ferramenta-cliente específica (Claude Code, Codex, ChatGPT, Gemini, Antigravity) a operar Maui. Vivem no corpus e são consumidos pelo `maui-toolkit/instantiate/`.

#### Localização

```
operator-packs/
├── claude-code/
│   ├── pack.yaml
│   ├── CLAUDE.md.j2
│   ├── generated/
│   │   └── CLAUDE.md
│   ├── update-protocol.md
│   ├── allowed-commands.md
│   └── hooks.example.json
├── codex/
│   ├── pack.yaml
│   ├── AGENTS.md.j2
│   ├── generated/
│   │   └── AGENTS.md
│   └── update-protocol.md
├── chatgpt/
│   ├── pack.yaml
│   ├── instructions.md.j2
│   ├── generated/
│   └── update-protocol.md
├── gemini/
└── antigravity/
```

#### Prioridade de implementação

1. Claude Code (filesystem + persistência via `CLAUDE.md`)
2. Codex (filesystem + `AGENTS.md`)
3. ChatGPT (sem filesystem; humano intermediário)
4. Gemini
5. Antigravity

#### Critérios de funcionamento

- Operator pack gerado é suficiente para uma ferramenta nova operar Maui.
- `pack.yaml` valida contra `schemas/operator-pack.schema.yaml`.
- Pack inclui instruções claras sobre limites (allowed-commands, hooks).

---

### 4.12 Exec Requests / Exec Reports

#### Definição

Arquivos estruturados para comunicação assíncrona entre instâncias Maui e assistentes de codificação (ou humanos). **Exec Request** é um pedido de execução; **Exec Report** é o relatório de retorno.

#### Localização

```
exec-requests/
└── {data}-{tool}-{purpose}.yaml

exec-reports/
└── {data}-{tool}-{purpose}-report.yaml
```

#### Schemas

- `schemas/execution-request.schema.yaml`
- `schemas/execution-report.schema.yaml`

#### Critérios de funcionamento

- Request inclui `tool_id`, `requested_action`, `inputs`, `expected_outputs`, `constraints`.
- Report referencia `request_id`, inclui `status`, `outputs_produced`, `errors`, `next_steps`.
- Report sempre referencia request original (rastreabilidade).

---

### 4.13 Context Packages

#### Definição

Pacotes de contexto humano-coláveis que alinham instâncias Maui sem reenviar todo o corpus. Evolução direta de `current.md` do Saara v7.1.1, agora **gerados** por `maui_context_export.py`.

#### Localização

```
context-packages/
├── data/                  # YAMLs de entrada
│   ├── common.yaml        # dados compartilhados
│   ├── claude-code.yaml
│   ├── codex.yaml
│   ├── chatgpt.yaml
│   └── current.yaml       # contexto geral atual
├── templates/             # Templates Jinja2
│   ├── default.md.j2
│   ├── claude-code.md.j2
│   ├── codex.md.j2
│   └── chatgpt.md.j2
└── generated/             # Pacotes gerados (não versionados por default)
```

#### Critérios de funcionamento

- Cada pacote gerado declara hash do corpus, versão Maui, data de geração.
- Pacote é absorvível por instância sem instruções adicionais.
- Edição manual continua possível, mas é exceção (não regra).

---

### 4.14 Update Protocol — Update Request / Package / Report

#### Definição

Protocolo para que instâncias Maui sem filesystem possam pedir atualização sem inventar estado. **Regra crítica**: instância sem filesystem não calcula hash, não presume status, não declara estar atualizada — gera Update Request.

#### Fluxo canônico

```
Instância Maui (sem fs)
   │
   │ 1. gera Update Request
   ▼
exec-requests/{request}.yaml
   │
   │ 2. operador (Claude Code / Codex / humano)
   │    lê corpus + executa scripts
   ▼
maui_update_export.py --request ...
   │
   │ 3. gera Update Package
   ▼
exports/update-package-{date}.md
   │
   │ 4. usuário cola na instância
   ▼
Instância integra + executa autoteste
   │
   │ 5. gera ou declara Update Report
   ▼
exec-reports/{report}.yaml
```

#### Schemas envolvidos

- `schemas/update-request.schema.yaml`
- `schemas/update-package.schema.yaml`
- `schemas/update-report.schema.yaml`

#### Update Request mínimo

```yaml
tipo: maui_update_request
request_id: 2026-05-04-chatgpt-maui-check
tool_id: chatgpt-maui-main
tool_type: chatgpt_custom_gpt
platform: chatgpt.com
known_maui_version: "Maui v0.1"
known_hash: "desconhecido"
known_context_package_date: "2026-05-01"
known_last_step: "M0"
requested_context:
  - current_state
  - active_pkas
  - roadmap_delta
  - update_protocol
  - procedural_layer
privacy_scope: interna
mode: human_handoff
output_preference: markdown_compact
```

#### Update Package mínimo (estrutura)

1. Identificação (tool_id, gerado_em, modo)
2. Estado atual do corpus (versão, hash, marco)
3. Delta desde estado conhecido
4. PKAs ativas
5. Instruções de integração
6. Autoteste (≥4 perguntas)
7. Próximo passo recomendado

#### Update Report mínimo

```yaml
tipo: maui_update_report
report_id: 2026-05-04-chatgpt-maui-report
tool_id: chatgpt-maui-main
received_package: 2026-05-04-chatgpt-maui-check
integration_status: integrated_in_session | partial | failed
autotest:
  version_answered: true
  pkas_answered: true
  update_protocol_answered: true
  no_hash_invention: true
notes: "..."
```

#### Critérios de funcionamento

- Instância sem filesystem nunca declara hash sem ter recebido Update Package.
- Toda integração é seguida de autoteste explícito.
- Report referencia request original.

---

### 4.15 Schemas

#### Definição

Schemas formais (JSON Schema ou YAML Schema) que definem contratos para todos os tipos estruturados do corpus.

#### Localização

```
schemas/
├── memory.schema.yaml
├── skill.schema.yaml
├── procedure.schema.yaml
├── script.schema.yaml
├── operator-pack.schema.yaml
├── registry.schema.yaml
├── context-package.schema.yaml
├── update-request.schema.yaml
├── update-package.schema.yaml
├── update-report.schema.yaml
├── execution-request.schema.yaml
└── execution-report.schema.yaml
```

#### Critérios de funcionamento

- Cada schema é versionado.
- Schemas são estáveis: mudança quebrável requer versão major do schema.
- Toda escrita em `memoria/`, `adendos/`, `exec-requests/`, etc., valida contra schema antes de gravar.

---

### 4.16 Maui Toolkit (auxiliar, fora do corpus)

#### Definição

Toolkit auxiliar com três comandos: `init`, `instantiate`, `panel`. **Não é o produto**; existe para bootstrap e curadoria.

#### Comandos

```
maui init --path ./vault-maui --template standard
  → cria estrutura de diretórios, copia templates,
    cria manifests, schemas base, primeiro context package,
    operator packs mínimos, scripts iniciais

maui instantiate --target {claude-code|codex|chatgpt|gemini}
  → renderiza operator pack para o target
  → gera CLAUDE.md / AGENTS.md / instructions.md
  → gera instancia.yaml
  → gera checklist humano de instanciação
  → opcionalmente registra via maui_registry.py

maui panel {status|task create|dispatch|collect|compare|record-decision}
  → curadoria multi-IA: agrupa instâncias, distribui prompts,
    compara respostas, registra decisão como memória
```

#### Critérios de funcionamento

- Toolkit nunca grava em `00_core/` automaticamente.
- Toolkit pode ser substituído sem afetar identidade Maui.

---

## 5. Tabela consolidada de funcionalidades

| Função | Localização | Substitui | Entradas principais | Saídas principais |
|---|---|---|---|---|
| Registry | `scripts/maui_registry.py` | `saara-core/registry` | `instancia.yaml`, corpus | Status, drift, plano |
| Memory Index | `scripts/maui_memory_index.py` | `saara-core/memory-index` | `memoria/**/*.md` | Índice, validação |
| Memory Search | `scripts/maui_memory_search.py` | `saara-core/memory search` | Query + filtros | Top-K memórias |
| Context Export | `scripts/maui_context_export.py` | `saara-core/context-export` | `data/`, `templates/` | Markdown compacto |
| Update Export | `scripts/maui_update_export.py` | `saara-core/update export` (B6) | `instancia.yaml` | Update Package |
| Validate Frontmatter | `scripts/maui_validate_frontmatter.py` | — (novo) | Corpus + schemas | Relatório |
| Validate Links | `scripts/maui_validate_links.py` | — (novo) | Corpus | Relatório |
| Validate Memory | `scripts/maui_validate_memory.py` | — (novo) | Memórias | Relatório |
| Vault Health | `scripts/maui_vault_health.py` | — (novo) | Corpus | Score + relatório |
| Skills | `skills/{nome}/SKILL.md` | — (novo) | — | Capacidades documentadas |
| Procedures | `procedures/*.md` | — (novo) | — | Runbooks |
| Operator Packs | `operator-packs/{tool}/` | — (novo) | Templates | Packs gerados |
| Exec Requests/Reports | `exec-requests/`, `exec-reports/` | — (novo) | YAMLs | Comunicação assíncrona |
| Context Packages | `context-packages/{data,templates,generated}/` | `current.md` manual | YAML + template | Markdown |
| Update Protocol | `schemas/update-*.yaml` + scripts | — (novo) | Request | Package + Report |
| Schemas | `schemas/*.schema.yaml` | — (novo) | — | Contratos |
| Toolkit | `maui-toolkit/` (fora) | `saara-core` no todo | CLI args | Estrutura, instâncias |

---

## 6. Matriz Função → PKA primária

Aplicação direta da regra anti-colapso: nem toda função técnica colapsa em Agent Engineering.

| Função Maui | PKA primária | PKAs de apoio | Artefato dominante |
|---|---|---|---|
| Definir system prompt Maui | Agent Engineering | Written Comms, AI Architect | System Prompt |
| Definir estrutura do corpus | AI Solutions Architect | Agent Engineering, Dev Engineer | Manifest/spec |
| Criar scripts de condicionamento | Development Engineer | Agent Engineering | Scripts/tests |
| Criar skills e procedures | Agent Engineering | Written Comms, Dev Engineer | Skills/procedures |
| Criar memórias/handoffs | Written Comms | Agent Engineering | Memória/context package |
| Gerar update package | Written Comms | Agent Engineering, Dev Engineer | Skill + script + template |
| Validar registry/drift | Development Engineer | Agent Engineering | Script/schema |
| Instanciar Claude/Codex/ChatGPT | Agent Engineering | AI Architect, Written Comms | Operator pack |
| Definir topologia/tooling | AI Solutions Architect | Development Engineer | Arquitetura/spec |
| Planejar/fechar marcos | SAFe Agile Master | Agent Engineering, Written Comms | Runbook/memória |
| Curadoria multi-IA | SAFe Agile Master | AI Architect, Written Comms | Painel/procedure |
| Propor adendos | Agent Engineering | Written Comms, domínio específico | Skill/adendo |

---

## 7. Mapeamento de migração — Antigo Saara Core → Maui

### 7.1 O que migra

| No Saara v7.1.1 (Core) | Em Maui | Forma |
|---|---|---|
| `saara registry` (módulo) | `scripts/maui_registry.py` + skill + procedure + schema | Script + corpus |
| `saara memory index` | `scripts/maui_memory_index.py` + skill + schema | Script + corpus |
| `saara memory search` | `scripts/maui_memory_search.py` + skill | Script + corpus |
| `saara update plan` (B5) | Absorvido por `maui_update_export.py` | Função consolidada |
| `saara update export` (B6) | `scripts/maui_update_export.py` | Script + corpus |
| `saara status` | `maui_registry.py list` + `maui_vault_health.py` | Scripts coordenados |
| Schema do registry no Core | `schemas/registry.schema.yaml` | Schema portável |
| Testes do Core (152) | Distribuídos: testes unitários por script + validações de schema + testes de integração via skills | Reorganização |
| `.saara/` (SQLite + índices) | `.maui/` (mesma função, infra reconstruível) | Renomeação |

### 7.2 O que permanece como toolkit

| No Saara v7.1.1 | Em Maui Toolkit |
|---|---|
| Bootstrap / scaffolding | `maui init` |
| Instanciação de ferramenta | `maui instantiate` |
| Painel multi-IA (futuro) | `maui panel` |

### 7.3 O que é deprecado

- A noção de que o Core é o produto.
- A noção de que comandos são adicionados ao Core ao invés de ao corpus.
- A noção de que o registry "pertence" a um backend.

---

## 8. Princípios herdados — Como cada um se materializa em Maui

### 8.1 Soberania Cognitiva (levada ao limite)

**No Saara v7.1.1:** corpus normativo (PKAs, specs) vive no vault; capacidades operacionais vivem no Core.
**Em Maui:** capacidades operacionais (scripts, skills, procedures) também vivem no corpus. O Toolkit é genuinamente substituível — pode ser reescrito em qualquer linguagem desde que respeite os contratos do corpus.

### 8.2 Lifecycle de Instanciação e Conformidade

**No Saara v7.1.1:** Tool Instance Registry vive em `.saara/instances.db`, gerenciado pelo Core.
**Em Maui:** mesmo mecanismo, mas operado por `scripts/maui_registry.py` que vive no corpus + reforçado pelo Update Protocol que cobre instâncias sem filesystem.

### 8.3 Context Injection Sob Demanda

**No Saara v7.1.1:** três camadas (A, B, C) com cadências próprias.
**Em Maui:** preservado integralmente. Camada A passa a poder ser **gerada por target** via `maui_context_export.py`, removendo a edição manual de `current.md`.

### 8.4 Capture Layer

**No Saara v7.1.1:** captura selectiva via Capture Layer no Core.
**Em Maui:** preservada conceitualmente. No MVS, captura é via skill + script (`maui-memory-create` + `procedimento-criar-memoria.md` + `procedimento-captura-explicita.md`). Captura proativa é evolução pós-MVS.

### 8.5 Insight Pipeline

**No Saara v7.1.1:** Pattern Detector → Insight Drafter → Human Gate → adendo ativo.
**Em Maui:** mesma estrutura. Pattern Detector pode ser implementado como `scripts/maui_pattern_detector.py` no futuro. Adendos continuam vivendo em `pka-{nome}-adendos/` ou `adendos/` consolidados.

---

## 9. Riscos arquiteturais e mitigações

| Risco | Severidade | Mitigação |
|---|---|---|
| Confusão entre "Maui o corpus" e "Maui o toolkit" durante transição | Alta | `01_manifest/maui-toolkit-boundaries.md` explícito; nomenclatura disciplinada |
| Perda de testes do Saara Core durante reorganização | Média | Migrar testes para `tests/scripts/` no corpus, organizados por script; validar paridade antes de descontinuar Core |
| Drift documental entre Saara v7.1.1 e Maui v0.1 simultâneos | Alta | Manter Saara v7.1.1 vigente até promoção formal; Maui é proposta até decisão explícita |
| Scripts pesados quebrarem portabilidade | Média | Limitar dependências externas; preferir stdlib; testar em Python 3.10+ minimal |
| Operator packs divergirem da realidade das ferramentas | Média | Validação por target (M12 do roadmap); ciclo de feedback documentado |
| Update Protocol ser ignorado por instâncias sem fs | Alta | System Prompt Maui inclui regra explícita; reflexes ativos em todas as instâncias |
| Fragmentação de scripts (cada um ligeiramente diferente) | Baixa | `schemas/script.schema.yaml` + convenções de IO uniformes (`--json`, `--markdown`, `--apply`) |

---

## 10. Decisões abertas

Decisões que esta spec **deliberadamente não fecha**, preservadas para deliberação:

1. Diretório-raiz: `vault-maui/` ou camada `maui/` dentro de `vault-saara/`?
2. Escopo do `hash_config`: incluir `scripts/`, `skills/`, `procedures/`, `01_manifest/`?
3. `context-packages/generated/`: versionado no Git ou sempre regenerado?
4. `.maui/` vs `.saara/`: substituição, coexistência durante migração, ou consolidação?
5. Versionamento: Maui v0.1 standalone, ou Saara/Maui v7.2 contínuo?
6. Adendos Maui: aplicados sobre Saara v7.1.1 ou em branch separada?
7. Primeiro piloto operator pack: Claude Code, Codex, ou ambos em paralelo?
8. B6 (`saara update export`) já entregue: encerrado como Saara ou reinterpretado como primeiro script Maui?
9. Painel: começa como CLI/file-based, plugin Obsidian, ou UI local?
10. Update Package: apenas Markdown ou também YAML/JSON desde o início?
11. Testes do Core (152) durante migração: portar todos antes da transição, ou portar incrementalmente?

---

## 11. Roadmap de adoção (resumo)

Detalhamento completo no Handoff Maui §14. Resumo:

Nota pós-P0.2: os scripts P0 de bootstrap, validação e contexto foram **Implementados** em 2026-05-10, com referência final `6c5c2c7` · `p0.2-complete`.

| Marco | Objetivo | Status |
|---|---|---|
| M0 | Decisão e baseline Maui (memória de decisão Saara→Maui, atualização de context package) | Próximo |
| M1 | Manifesto e estrutura do Maui Corpus (`01_manifest/`) | Aguarda M0 |
| M2 | Schemas mínimos (12 schemas) | Aguarda M1 |
| M3 | Scripts de condicionamento P0 (9 scripts) | Implementado em 2026-05-10 (`p0.2-complete`) |
| M4 | Skills P0 (10 skills) | Aguarda M3 |
| M5 | Procedures e reflexos (8 procedimentos + 4 reflexos) | Aguarda M3 |
| M6 | Operator Packs (Claude Code, Codex, ChatGPT, Gemini, Antigravity) | Aguarda M5 |
| M7 | Protocolo Update Request/Package/Report | Aguarda M6 |
| M8 | Context packages gerados (substitui edição manual) | Aguarda M3 |
| M9 | Maui Toolkit mínimo (init, instantiate, panel) | Aguarda M6 |
| M10 | Painel de curadoria multi-IA | Aguarda M9 |
| M11 | Adendos e promoção normativa | Aguarda M7 |
| M12 | Validação cross-tool (6 cenários mínimos) | Aguarda M11 |

---

## 12. Suíte mínima de testes da transição

Ao final da adoção, os seguintes cenários devem passar:

- **TC1:** `maui init` cria estrutura mínima válida em diretório novo.
- **TC2:** `maui instantiate --target claude-code` gera operator pack consumível por Claude Code real.
- **TC3:** `maui_registry.py list` reporta instâncias declaradas em `instancia.yaml`.
- **TC4:** `maui_memory_index.py` indexa memórias herdadas do Saara v7.1.1 sem perda.
- **TC5:** `maui_context_export.py --target claude-code` produz pacote equivalente ao `current.md` manual.
- **TC6:** `maui_update_export.py --from-file instancia.yaml` produz Update Package coerente.
- **TC7:** Instância ChatGPT sem filesystem gera Update Request válido contra schema.
- **TC8:** Update Package gerado é integrável por instância e o autoteste passa.
- **TC9:** Vault Health roda sem erros sobre corpus migrado.
- **TC10:** Validações de frontmatter, links e memórias passam sobre corpus migrado.
- **TC11:** Instância antiga (Saara v7.1.1) continua operacional durante coexistência.
- **TC12:** Hash determinístico produz mesmo valor em duas máquinas diferentes com mesmo corpus.

---

## 13. Critérios de aceitação da transição

Maui v0.1 é considerado **adotado** quando:

1. M0–M7 do roadmap foram concluídos.
2. Pelo menos um operator pack (Claude Code) foi validado em uso real.
3. Pelo menos uma instância foi atualizada via Update Protocol completo.
4. Validação cross-tool §12 passou em pelo menos 8 dos 12 TCs.
5. Decisão formal de governança foi registrada em memória.
6. Adendos Maui foram aprovados via Human Gate.
7. Saara Core v7.1.1 foi formalmente reclassificado como `maui-toolkit/` ou descontinuado em favor do toolkit novo.
8. Context package atual (`context-packages/data/current.yaml`) reflete o estado Maui.

---

## 14. F/I/H

### 14.1 Fatos

- Saara v7.1.1 é a base normativa atual e consolidada.
- A nova geração foi nomeada **Maui** pelo usuário em 2026-05-01.
- O usuário definiu que o produto é o corpus em arquivos texto, não aplicação.
- O usuário definiu que `registry`, `memory-index`, `context-export` e `update-export` viram scripts de condicionamento.
- O usuário definiu que o antigo Core ainda pode existir como toolkit auxiliar.
- O usuário pediu inclusão das 5 PKAs do Saara v7.1.1 em Maui.
- Saara Core hoje tem 152 testes passando e B6 (`saara update export`) entregue.

### 14.2 Inferências

- A migração se beneficia de coexistência temporária Saara/Maui em vez de cutover abrupto.
- Claude Code e Codex são os operadores mais adequados como primeiros pilotos por terem filesystem.
- ChatGPT sem Action precisa do humano intermediário até Action ser viável.
- A reorganização dos 152 testes do Core em testes distribuídos por script é não-trivial; merece marco próprio dentro de M3.
- `01_manifest/` precisa existir antes de M1 ser considerado completo, sob risco de identidade Maui ficar implícita.

### 14.3 Hipóteses

- Maui v0.1 nascerá como proposta + memória + adendo antes de promoção formal.
- B6 já entregue será reinterpretado como `maui_update_export.py` com adaptações mínimas.
- O painel MVS começará file-based/CLI; UI vem depois.
- O `hash_config` em Maui incluirá `scripts/`, `skills/`, `procedures/` e `01_manifest/` (decisão técnica futura).
- A coexistência Saara v7.1.1 + Maui v0.1 durará entre 30 e 90 dias antes de transição formal.

---

## 15. Próximos passos imediatos

1. Revisar esta spec contra o Handoff Maui v0.1 e o context package corrente.
2. Salvar como memória de proposta arquitetural.
3. Decidir governança da transição: spec vira adendo, ou resulta em versão maior (Saara v7.2 / Maui v0.1)?
4. Resolver decisões abertas mínimas (§10): pelo menos diretório-raiz e versionamento.
5. Iniciar M0 do roadmap Maui (memória de decisão Saara→Maui).

---

**FIM — Spec Técnica Atualização Saara → Maui v0.1**
