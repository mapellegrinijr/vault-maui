---
titulo: "Arquitetura Alvo — Maui"
versao: "0.2"
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: especificacao_arquitetural
escopo: projeto_maui
---

# Arquitetura Alvo — Maui

## 1. Resumo executivo

Maui é a nova arquitetura de evolução do Saara. A decisão central é que **Maui não é uma aplicação, backend, chatbot, MCP server ou interface específica**. Maui é um **corpus cognitivo multipapel, procedural, portátil e instanciável por diferentes modelos e ferramentas de IA**.

A identidade, governança, comportamento, memória e capacidades operacionais do Maui vivem no corpus versionado. Infraestruturas como toolkit, painel, scripts, MCP servers, adapters, bancos locais ou integrações são mecanismos auxiliares e substituíveis.

A arquitetura adota o princípio de **soberania do corpus** e o expande: além de documentos normativos, o corpus passa a conter também skills, procedures, scripts, hooks, subagentes, plugins, schemas, evals, automations, operator packs, context packages e protocolos de execução.

## 2. Decisão arquitetural principal

```text
Produto principal = Maui Corpus
Ferramentas auxiliares = Maui Toolkit + scripts + painel + operadores + MCP servers
```

O antigo `saara-core` deixa de ser interpretado como centro do produto. Ele pode evoluir para **Maui Toolkit**, com responsabilidade de bootstrap, instanciação, validação, curadoria e distribuição, mas não define a identidade do Maui.

## 3. Equação do Maui

```text
Maui = corpus
     + memória + PKAs + specs + adendos + insights
     + skills + procedures + reflexes + scripts
     + hooks + subagents + plugins
     + schemas + evals + automations
     + operator-packs + mcp-servers
     + context-packages + exec-requests/reports
```

Essa equação define o Maui como uma arquitetura **corpus-first** e **tool-agnostic**, capaz de operar em ambientes com filesystem direto, MCP, REST/Actions ou handoff humano.

## 4. Objetivos da nova arquitetura

1. Tornar o Maui instanciável em diferentes ferramentas de IA sem depender de um backend único.
2. Transformar capacidades operacionais em artefatos versionados no corpus.
3. Separar produto, toolkit e operadores.
4. Preservar compatibilidade com Saara v7.1.1 até decisão formal de substituição.
5. Adotar padrões abertos de 2026: Agent Skills, `AGENTS.md`, hooks lifecycle, subagents, plugins e MCP.
6. Garantir evolução governada via memória, adendos, insights, evals e Human Gate.
7. Manter portabilidade, auditabilidade, idempotência e reversibilidade.

## 5. Princípios arquiteturais

### 5.1 Soberania cognitiva ampliada

A identidade do Maui vive no corpus. Código, bancos, servidores e integrações são substituíveis.

Em Maui, a soberania cognitiva passa a incluir também capacidades executáveis:

- scripts de condicionamento;
- skills;
- procedures/runbooks;
- hooks;
- subagentes;
- plugins;
- schemas;
- evals;
- automations;
- operator packs.

### 5.2 Padrão aberto por default

Maui adota convenções abertas quando elas não violam a soberania do corpus:

- `SKILL.md` com frontmatter;
- `AGENTS.md` para agentes de codificação;
- MCP como protocolo de exposição;
- plugins como bundles versionados;
- hooks lifecycle para enforcement determinístico;
- evals como código;
- context engineering como disciplina operacional.

### 5.3 Determinismo onde possível

Regras críticas não devem depender apenas de prompt. Quando possível, devem ser implementadas por:

- schemas;
- validações;
- scripts idempotentes;
- hooks;
- testes/evals;
- contratos de entrada e saída.

### 5.4 Output contract first

Todo entregável relevante do Maui deve declarar:

- contrato de entrada;
- contrato de saída;
- critérios de sucesso;
- riscos e limites;
- sinalização F/I/H quando houver fatos, inferências ou hipóteses materiais.

### 5.5 Context engineering

Maui evolui o Context Injection do Saara para uma disciplina explícita:

```text
Write   → registrar e estruturar contexto reutilizável
Select  → selecionar o contexto certo para a tarefa
Compress→ compactar sem perder governança
Isolate → separar escopos, papéis, confidencialidade e ferramentas
```

## 6. Visão em camadas

```text
┌────────────────────────────────────────────────────────────┐
│ Camada 1 — Cognitiva                                       │
│ 00_core/ · 01_manifest/ · memorias/ · adendos/ · insights/ │
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
```

## 7. Componentes arquiteturais

### 7.1 Maui Corpus

Produto principal. Fonte de verdade de identidade, comportamento, memória, governança, procedimentos e capacidades operacionais.

Responsabilidades:

- armazenar normativos, PKAs, specs e princípios;
- manter memória, adendos e insights;
- versionar skills, procedures, scripts e hooks;
- declarar schemas, evals e contratos;
- conter operator packs e context packages;
- suportar execução por agentes humanos e modelos de IA.

### 7.2 Maui Toolkit

Conjunto auxiliar para operar o corpus. Não é o produto.

Responsabilidades:

- criar estrutura inicial do corpus;
- gerar templates;
- instanciar Maui em ferramentas-alvo;
- preparar operator packs;
- executar validações;
- oferecer painel de curadoria;
- expor capacidades via CLI, filesystem, MCP ou REST quando aplicável.

Comandos conceituais:

```bash
maui init --path ./vault-maui --template standard
maui instantiate --target claude-code
maui instantiate --target codex
maui instantiate --target chatgpt
maui panel status
maui panel dispatch
maui panel collect
maui panel record-decision
```

### 7.3 Scripts de condicionamento

Scripts versionados no corpus que executam operações determinísticas e primitivas.

Scripts P0:

```text
scripts/maui_registry.py
scripts/maui_memory_index.py
scripts/maui_context_export.py
scripts/maui_update_export.py
```

Responsabilidades:

- registry de instâncias;
- indexação de memória;
- exportação de contexto;
- geração de update packages;
- validação de integridade;
- suporte a instâncias sem filesystem direto.

### 7.4 Skills

Capacidades operacionais reutilizáveis, compatíveis com padrão `SKILL.md`.

Estrutura esperada:

```text
skills/
├── maui-vault-health/
│   └── SKILL.md
├── maui-context-export/
│   └── SKILL.md
└── maui-frontmatter-validate/
    └── SKILL.md
```

Contrato mínimo de skill:

- propósito claro;
- quando usar;
- inputs;
- outputs;
- passos;
- ferramentas permitidas;
- critérios de sucesso;
- limites e riscos.

### 7.5 Procedures / Runbooks

Procedimentos explícitos para operações recorrentes.

Exemplos:

- atualizar instância Maui;
- criar novo operator pack;
- promover insight para adendo;
- validar corpus antes de release;
- gerar handoff para ferramenta sem filesystem.

### 7.6 Hooks

Camada de enforcement determinístico em eventos do ciclo de vida.

Exemplos de eventos:

- `SessionStart`;
- `PreToolUse`;
- `PostToolUse`;
- `Stop`;
- `OnExport`;
- `OnCapture`.

Usos prioritários:

- carregar contexto mínimo no início da sessão;
- bloquear escrita insegura;
- validar frontmatter;
- registrar exec reports;
- aplicar sanitização antes de captura;
- impedir drift silencioso.

### 7.7 Subagentes

Construto nativo para especialização e isolamento de tarefas.

Modelos suportados:

1. **Subagentes nominais** — especialistas pré-definidos, com escopo, tools e contratos fixos.
2. **Clones via Task** — delegações temporárias decididas pela instância principal, com contexto limitado e retorno resumido.

Exemplos:

- `maui-doc-reviewer`;
- `maui-schema-validator`;
- `maui-context-compressor`;
- `maui-update-planner`;
- `maui-memory-curator`.

### 7.8 Plugins

Bundles versionados que empacotam skills, hooks, subagents e commands.

Estrutura:

```text
plugins/
├── maui-core-essentials/
│   ├── plugin.yaml
│   ├── skills/
│   ├── hooks/
│   └── subagents/
├── maui-curation-pack/
├── maui-instance-management/
└── maui-eval-toolkit/
```

Critérios:

- instalação sem conflito de nomes;
- namespacing explícito;
- validação de dependências;
- desinstalação sem resíduos;
- versão e changelog obrigatórios.

### 7.9 MCP Servers

Maui pode expor capacidades selecionadas via MCP servers locais ou controlados. Maui não é um MCP server; MCP é apenas um protocolo de acesso.

Usos:

- consulta ao corpus;
- retrieve de contexto;
- exportação de packages;
- validação de instância;
- execução controlada de scripts;
- capture layer assistida.

### 7.10 Operator Packs

Pacotes de adaptação para ferramentas específicas.

Targets iniciais:

- Claude Code;
- Codex;
- ChatGPT;
- Gemini;
- Cursor;
- Antigravity;
- Claude Desktop.

Conteúdo típico:

```text
operator-packs/
├── claude-code/
│   ├── CLAUDE.md.template
│   ├── skills-map.yaml
│   ├── hooks.yaml
│   └── install.md
├── codex/
│   ├── AGENTS.md.template
│   ├── skills-map.yaml
│   └── install.md
└── chatgpt/
    ├── custom-gpt-instructions.md
    ├── action-schema.yaml
    └── handoff-protocol.md
```

## 8. Estrutura física alvo

```text
vault-maui/
├── 00_core/                      # Normativo herdado/evoluído
├── 01_manifest/                  # Definição de produto e arquitetura
├── memorias/                     # Memórias operacionais e episódicas
├── adendos/                      # Evoluções incrementais aprovadas
├── insights/                     # Padrões consolidados
├── skills/                       # Capacidades executáveis por agentes
├── procedures/                   # Runbooks, reflexos e protocolos
├── reflexes/                     # Microprocedimentos acionáveis
├── scripts/                      # Scripts de condicionamento
├── hooks/                        # Hooks lifecycle
├── subagents/                    # Subagentes nominais
├── plugins/                      # Bundles distribuíveis
├── schemas/                      # Contratos e validações
├── evals/                        # Testes/evals como código
├── automations/                  # Cadências e rotinas programadas
├── validations/                  # Relatórios de validação
├── operator-packs/               # Adaptação por ferramenta
├── mcp-servers/                  # Exposição controlada via MCP
├── context-packages/             # Pacotes de contexto por alvo
├── exec-requests/                # Solicitações estruturadas de execução
├── exec-reports/                 # Relatórios estruturados de execução
└── exports/                      # Update packages e artefatos gerados
```

## 9. Topologia operacional

```text
┌────────────────────┐  filesystem  ┌──────────────────┐
│ Claude Code        │ ←──────────→ │                  │
│ Codex              │              │   vault-maui/    │
│ Cursor             │              │                  │
└────────────────────┘              │   corpus         │
                                    │                  │
┌────────────────────┐  MCP/REST    │                  │
│ Claude Desktop     │ ←──────────→ │                  │
│ ChatGPT Action     │              │                  │
│ Gemini             │              └──────────────────┘
└────────────────────┘                       ▲
                                             │
┌────────────────────┐  Human-Handoff        │
│ ChatGPT sem Action │ ────────────→ Update  │
│ Gemini sem FS      │              Protocol │
└────────────────────┘                       │
                                    ┌────────┴───────┐
                                    │ Maui Toolkit   │
                                    │ auxiliar       │
                                    └────────────────┘
```

## 10. Modos de operação por ferramenta

| Ferramenta         | Modo principal                     | Modo secundário           | Observação                      |
| ------------------ | ---------------------------------- | ------------------------- | ------------------------------- |
| Claude Code        | Filesystem + skills/hooks          | MCP                       | Primeiro operador ideal         |
| Codex              | Filesystem + `AGENTS.md`           | Skills em `.agents/`      | Segundo operador ideal          |
| Cursor             | Filesystem + rules                 | MCP                       | Adequado para desenvolvimento   |
| Claude Desktop     | MCP                                | Project knowledge         | Bom para consulta e curadoria   |
| ChatGPT com Action | REST/Action                        | Handoff humano            | Depende de endpoint autenticado |
| ChatGPT sem Action | Handoff humano                     | Upload manual             | Não presume hash real           |
| Gemini             | Gem / filesystem quando disponível | REST/MCP conforme suporte | Requer operator pack específico |

## 11. Protocolo de atualização

O protocolo de atualização é baseado em três artefatos:

```text
Update Request  →  Update Package  →  Update Report
```

### 11.1 Update Request

Solicitação estruturada gerada por uma instância Maui ou por humano.

Contém:

- instância de origem;
- versão percebida;
- objetivo da atualização;
- escopo;
- restrições;
- formato desejado;
- evidências e arquivos relevantes.

### 11.2 Update Package

Pacote gerado por ferramenta com acesso ao corpus ou pelo Maui Toolkit.

Contém:

- mudanças propostas;
- arquivos afetados;
- diff ou instruções;
- validações executadas;
- riscos;
- instruções de aplicação;
- rollback quando aplicável.

### 11.3 Update Report

Relatório pós-execução.

Contém:

- o que foi aplicado;
- o que falhou;
- validações executadas;
- drift remanescente;
- recomendações;
- decisão humana quando necessária.

## 12. Fluxo de atualização

```text
1. Instância detecta necessidade de evolução ou drift
2. Instância gera exec-request estruturado
3. Operador com filesystem/MCP lê corpus e request
4. Operador executa scripts/skills/procedures autorizados
5. Operador gera update package
6. Instância ou humano aplica pacote
7. Validações e evals são executados
8. Exec report registra resultado
9. Decisões relevantes viram memória/adendo/insight
```

Regra: instância sem filesystem ou endpoint autenticado **não calcula hash real** e **não presume estar atualizada**.

## 13. Governança e lifecycle

### 13.1 Precedência

A arquitetura Maui preserva a precedência do Saara v7.1.1 até decisão formal de substituição:

1. Políticas externas, lei e compliance.
2. System prompt ativo.
3. Princípios Fundacionais.
4. Especificação Completa.
5. PKAs e specs técnicas.
6. Parametrização executável.
7. Conteúdo recuperado.
8. Pedido do usuário.

### 13.2 Human Gate

Exige aprovação humana:

- adoção formal do Maui como substituto do Saara v7.1.1;
- alteração de princípios fundacionais;
- promoção de adendos para ativo ou merged;
- mudanças de precedência;
- instalação de plugins externos;
- exposição MCP/REST que escreva no corpus;
- automations com escrita persistente.

### 13.3 Drift e conformidade

Cada instância deve manter estado verificável quando o ambiente permitir:

- `tool_id`;
- `target`;
- versão instanciada;
- hash quando disponível;
- operator pack usado;
- PKAs carregadas;
- adendos e insights carregados;
- último check;
- severidade de drift.

Estados:

```text
current
minor_drift
major_drift
incompatible
unknown
```

`unknown` é obrigatório para instâncias sem filesystem, sem registry ou sem endpoint autenticado.

## 14. Context engineering

### 14.1 Camadas de contexto

Maui preserva a lógica A/B/C e a amplia operacionalmente:

| Camada | Conteúdo                                 | Cadência         | Meio                                               |
| ------ | ---------------------------------------- | ---------------- | -------------------------------------------------- |
| A      | identidade, princípios, PKAs, specs base | instanciação     | Project, Custom GPT, Gem, `CLAUDE.md`, `AGENTS.md` |
| B      | adendos, insights, correções, drift      | início de sessão | MCP, REST, package, handoff                        |
| C      | memórias e referências relevantes        | sob demanda      | retrieve, context package, MCP                     |

### 14.2 Regras

- Não existe modo normal de “carregar tudo”.
- Contexto deve ser selecionado por relevância e escopo.
- Contexto sensível deve respeitar confidencialidade e separação de domínios.
- Todo context package deve declarar objetivo, alvo, validade e limites.
- Compressão deve preservar decisões, contratos e riscos.

## 15. Capture Layer e Insight Pipeline

Maui mantém a Capture Layer como mecanismo sancionado de escrita em memória operacional.

Fluxo:

```text
Conversa/execução
  → captura seletiva
  → compactação sanitizada
  → memória estruturada
  → detecção de padrões
  → insight
  → candidato a adendo
  → Human Gate
  → adendo ativo ou rejeitado
```

Critérios de captura:

- comando explícito do usuário;
- decisão registrável;
- artefato reutilizável;
- preferência ou aprendizado declarado;
- alta densidade informacional;
- resultado de execução relevante.

## 16. Qualidade, validação e evals

### 16.1 Validações mínimas

- frontmatter obrigatório;
- links internos resolvíveis;
- schemas válidos;
- operator packs completos;
- scripts idempotentes;
- ausência de escrita fora do escopo;
- changelog em mudanças materiais;
- compatibilidade com Saara v7.1.1 até decisão formal.

### 16.2 Evals como código

Skills e procedures críticas devem ter evals versionadas.

Exemplos:

```text
evals/
├── skills/
│   ├── maui-context-export.eval.yaml
│   └── maui-frontmatter-validate.eval.yaml
├── update-protocol/
│   └── update-request-package-report.eval.yaml
└── regression/
    └── corpus-integrity.eval.yaml
```

Critérios:

- regressão detectável;
- fixtures versionadas;
- resultado reproduzível;
- falha bloqueia release quando severidade for alta.

## 17. Segurança e privacidade

Regras base:

- privacidade por padrão;
- menor privilégio para tools, hooks e subagentes;
- separação entre escopos pessoal/trabalho/projeto;
- nenhuma escrita persistente sem trilha;
- sanitização antes de memória;
- plugins externos tratados como não confiáveis até validação;
- MCP/REST com autenticação e escopo explícito quando houver escrita;
- rollback obrigatório para alterações destrutivas.

## 18. Fronteiras arquiteturais

### 18.1 Maui é

- corpus cognitivo multipapel;
- arquitetura procedural;
- sistema instanciável;
- conjunto de contratos, skills, procedures e scripts;
- produto tool-agnostic;
- base de governança e memória.

### 18.2 Maui não é

- aplicação SaaS;
- app desktop;
- chatbot único;
- backend;
- banco de dados;
- MCP server específico;
- interface gráfica;
- Claude, ChatGPT, Gemini, Codex, Cursor ou Antigravity.

### 18.3 Maui Toolkit é

- auxiliar;
- reconstruível;
- substituível;
- operador do corpus;
- não fonte de identidade.

## 19. Plano incremental recomendado

### Fase 0 — Formalização

- Salvar arquitetura alvo em `01_manifest/`.
- Registrar decisão Saara → Maui como memória.
- Definir status oficial: proposta, piloto ou adoção.
- Criar changelog e owner.

### Fase 1 — Estrutura mínima

- Criar árvore `vault-maui/`.
- Criar schemas mínimos.
- Criar scripts P0.
- Criar context package inicial.
- Criar operator packs Claude Code e Codex.

### Fase 2 — Operação assistida

- Gerar `CLAUDE.md` e `AGENTS.md` por template.
- Validar `maui_update_export.py`.
- Testar Update Request/Package/Report.
- Executar piloto com Claude Code.
- Registrar exec reports.

### Fase 3 — Qualidade e curadoria

- Criar evals P0.
- Criar hooks de validação.
- Criar subagentes nominais.
- Implementar painel CLI/file-based.
- Definir critérios de release.

### Fase 4 — Integração ampliada

- Expor MCP servers selecionados.
- Criar Action/REST para ChatGPT quando seguro.
- Expandir operator packs.
- Introduzir automations controladas.
- Consolidar plugins P0.

## 20. Decisões registradas

| Decisão                                    | Status               | Observação                                            |
| ------------------------------------------ | -------------------- | ----------------------------------------------------- |
| Maui é corpus, não aplicação               | proposta consolidada | base da arquitetura                                   |
| Saara Core vira toolkit auxiliar           | proposta consolidada | não fonte de identidade                               |
| Scripts P0 vivem no corpus                 | proposta consolidada | registry, memory-index, context-export, update-export |
| Skills usam padrão `SKILL.md`              | proposta v2          | alinhamento 2026                                      |
| Hooks são camada determinística            | proposta v2          | enforcement não-alucinatório                          |
| Subagentes são nativos                     | proposta v2          | nominais + clones via Task                            |
| Plugins são unidade distribuível           | proposta v2          | bundles versionados                                   |
| MCP é protocolo de primeira classe         | proposta v2          | não identidade do produto                             |
| Update Protocol usa request/package/report | proposta consolidada | tool-agnostic                                         |
| ChatGPT sem Action usa handoff humano      | proposta consolidada | não presume filesystem/hash                           |

## 21. Riscos e controles

| Risco                                    | Impacto | Controle                                    |
| ---------------------------------------- | ------- | ------------------------------------------- |
| Recriar acoplamento ao toolkit           | Alto    | reforçar corpus-first em docs e gates       |
| Drift entre instâncias                   | Alto    | registry, hashes, update reports            |
| Plugins externos inseguros               | Alto    | Human Gate, sandbox, validação de manifest  |
| Contexto excessivo                       | Médio   | context engineering, orçamento e compressão |
| Scripts com efeitos destrutivos          | Alto    | idempotência, dry-run e rollback            |
| Ambiguidade entre skill/procedure/script | Médio   | taxonomia e exemplos canônicos              |
| Captura indevida de memória              | Alto    | sanitização, escopo, capture layer seletiva |
| Evals insuficientes                      | Médio   | suíte P0 antes de release operacional       |

## 22. Contrato operacional resultante

A evolução deve seguir este contrato:

1. Toda mudança estrutural do Maui deve ser representada primeiro no corpus.
2. Toolkit, scripts e MCP servers só implementam contratos já descritos no corpus.
3. Instâncias com acesso a filesystem podem validar hash; instâncias sem acesso devem declarar estado `unknown`.
4. Toda capability crítica precisa de output contract e success criteria.
5. Toda escrita persistente em memória, adendo, insight ou spec deve passar por governança proporcional.
6. O piloto inicial deve priorizar Claude Code e Codex.
7. ChatGPT/Gemini sem filesystem devem operar via context packages e handoff estruturado.
8. Maui permanece proposta até decisão explícita de governança substituir ou promover o Saara v7.1.1.

## 23. F/I/H

### Fatos

- Maui foi definido como nova geração do Saara.
- Maui é corpus cognitivo multipapel, procedural, portátil e instanciável.
- O produto principal é o corpus; toolkit, scripts e painel são auxiliares.
- A arquitetura herda princípios, PKAs e governança do Saara v7.1.1.
- A spec v2 adiciona Agent Skills, hooks, subagents, plugins, MCP, AGENTS.md, context engineering, automations e evals.

### Inferências

- `01_manifest/` deve conter esta arquitetura alvo como documento canônico.
- Claude Code e Codex são os melhores pilotos iniciais por acesso a filesystem.
- ChatGPT sem Action deve depender de handoff humano ou upload manual.
- O painel MVS deve começar como CLI/file-based antes de UI.

### Hipóteses

- Maui será adotado primeiro como proposta/piloto antes de substituir formalmente Saara v7.1.1.
- MCP servers devem começar somente com capacidades de leitura ou validação antes de permitir escrita.
- Plugins P0 devem ser internos antes de consumo de plugins externos.

---

# Anexo A — Artefatos P0 sugeridos

```text
01_manifest/arquitetura-alvo-maui.md
01_manifest/definicao-produto-maui.md
schemas/exec-request.schema.yaml
schemas/exec-report.schema.yaml
schemas/update-package.schema.yaml
schemas/skill.schema.yaml
schemas/plugin.schema.yaml
scripts/maui_registry.py
scripts/maui_memory_index.py
scripts/maui_context_export.py
scripts/maui_update_export.py
operator-packs/claude-code/
operator-packs/codex/
context-packages/current/maui-bootstrap.md
```

# Anexo B — Critérios de aceite da arquitetura

- A arquitetura deixa claro que Maui é corpus, não aplicação.
- A separação corpus/toolkit/operator está explícita.
- As camadas arquiteturais estão definidas.
- A estrutura física alvo está especificada.
- O protocolo Update Request/Package/Report está descrito.
- A estratégia multi-ferramenta está definida.
- Governança, segurança, contexto, captura e evals estão cobertos.
- Há plano incremental e riscos com controles.


---

# 24. Priorização de desenvolvimento das funcionalidades

## 24.1 Critério de priorização

A priorização segue o princípio de **mínimo Maui utilizável com segurança**. Uma funcionalidade sobe de prioridade quando atende pelo menos um destes critérios:

1. Permite criar ou organizar o `vault-maui/`.
2. Permite instanciar Maui em uma ferramenta real.
3. Reduz risco de drift, escrita indevida ou perda de governança.
4. Habilita ciclo de atualização entre instâncias.
5. Gera capacidade operacional reutilizável por agentes de codificação.
6. É pré-requisito para múltiplas funcionalidades posteriores.

Funcionalidades com alto apelo, mas sem necessidade para o primeiro uso seguro, ficam em P1/P2: MCP completo, plugins externos, automations com escrita, painel UI e subagentes avançados.

## 24.2 Ordem executiva recomendada

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

## 24.3 P0.0 — Formalização do corpus e estrutura mínima

### Objetivo

Tornar o Maui materializável como diretório versionado, mesmo antes de qualquer automação avançada.

### Funcionalidades incluídas

- Maui Corpus.
- Estrutura física alvo.
- Governança mínima.
- Arquitetura alvo.
- Spec unificada de funcionalidades.

### Artefatos a criar primeiro

```text
vault-maui/
├── 00_core/
├── 01_manifest/
├── memorias/
├── adendos/
├── insights/
├── skills/
├── procedures/
├── reflexes/
├── scripts/
├── schemas/
├── validations/
├── operator-packs/
├── context-packages/
├── exec-requests/
├── exec-reports/
└── exports/
```

Arquivos mínimos:

```text
01_manifest/arquitetura-alvo-maui.md
01_manifest/spec-funcionalidades-maui.md
01_manifest/definicao-produto-maui.md
01_manifest/roadmap-priorizado-maui.md
```

### Critérios de pronto

- A árvore existe.
- Os documentos-base estão salvos.
- A fronteira corpus/toolkit está explícita.
- O status do Maui está como `proposta` ou `piloto`, não `ativo`, até decisão humana.

## 24.4 P0.1 — Schemas mínimos e validação local

### Objetivo

Evitar que o corpus comece sem contratos verificáveis.

### Funcionalidades incluídas

- Schemas e Contratos Estruturados.
- Governança e Segurança.
- Validação mínima.

### Schemas prioritários

```text
schemas/common-frontmatter.schema.yaml
schemas/registry.schema.yaml
schemas/context-package.schema.yaml
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
schemas/skill.schema.yaml
schemas/operator-pack.schema.yaml
```

### Justificativa

Scripts sem schemas tendem a codificar regras implícitas. Primeiro define-se contrato; depois implementa-se execução.

### Critérios de pronto

- Campos obrigatórios comuns definidos.
- Severidade de validação definida.
- Pelo menos uma fixture válida e uma inválida por schema crítico.
- Validação manual possível mesmo antes de automação completa.

## 24.5 P0.2 — Scripts P0 de bootstrap, validação e contexto

### Objetivo

Criar a primeira camada executável do Maui, ainda sem depender de MCP, painel ou UI.

### Ordem dos scripts

#### 1. `maui_vault_health.py`

Primeiro script porque valida se o corpus está íntegro.

Responsabilidades iniciais:

- verificar estrutura de diretórios;
- verificar arquivos obrigatórios;
- listar ausências;
- gerar relatório Markdown/JSON;
- não escrever fora de `validations/`.

#### 2. `maui_validate_frontmatter.py`

Responsável por garantir metadados mínimos.

#### 3. `maui_validate_links.py`

Responsável por detectar links internos quebrados e referências ausentes.

#### 4. `maui_context_export.py`

Responsável por gerar o primeiro context package para ChatGPT Handoff, Claude Code e Codex.

#### 5. `maui_registry.py`

Responsável por registrar instâncias quando houver pelo menos um operator pack piloto.

#### 6. `maui_update_export.py`

Responsável por gerar Update Package depois que context package e registry existirem.

#### 7. `maui_memory_index.py`

Responsável por indexar memórias. Pode vir depois do update protocol mínimo, pois memória não bloqueia o primeiro uso.

#### 8. `maui_memory_search.py`

Busca lexical simples. P0 tardio ou P1 inicial.

### Critérios de pronto

- Todos os scripts aceitam `--help`, `--dry-run`, `--format markdown|json`.
- Scripts de escrita exigem `--write`.
- Saídas são compatíveis com `validations/` ou `exec-reports/`.
- Falha segura implementada.

## 24.6 P0.3 — Operator packs iniciais

### Objetivo

Permitir que Maui seja usado em ferramentas reais.

### Ordem dos targets

#### 1. Claude Code

Prioridade mais alta por ser o operador ideal para trabalhar com filesystem, scripts, templates e artefatos.

Artefatos:

```text
operator-packs/claude-code/pack.yaml
operator-packs/claude-code/CLAUDE.md.template
operator-packs/claude-code/install.md
operator-packs/claude-code/skills-map.yaml
```

#### 2. Codex

Segundo operador ideal para desenvolvimento por filesystem e `AGENTS.md`.

Artefatos:

```text
operator-packs/codex/pack.yaml
operator-packs/codex/AGENTS.md.template
operator-packs/codex/install.md
operator-packs/codex/skills-map.yaml
```

#### 3. ChatGPT Handoff

Necessário para ferramentas sem filesystem direto.

Artefatos:

```text
operator-packs/chatgpt-handoff/pack.yaml
operator-packs/chatgpt-handoff/custom-gpt-instructions.md
operator-packs/chatgpt-handoff/handoff-protocol.md
```

### Fora do P0

- ChatGPT Action.
- Gemini pack completo.
- Cursor pack avançado.
- MCP config avançada.

### Critérios de pronto

- Cada pack declara capacidades e limitações.
- Claude Code e Codex conseguem receber instruções base sem edição manual extensa.
- ChatGPT Handoff declara `unknown` para hash e conformidade.
- Nenhum pack duplica a identidade do Maui; apenas adapta o corpus ao target.

## 24.7 P0.4 — Context package inicial e protocolo de handoff

### Objetivo

Permitir uso operacional do Maui em ferramentas sem acesso direto ao vault.

### Artefatos prioritários

```text
context-packages/current/maui-bootstrap.md
context-packages/targets/claude-code.md
context-packages/targets/codex.md
context-packages/targets/chatgpt-handoff.md
```

### Conteúdo mínimo do bootstrap

- definição de Maui;
- fronteira corpus/toolkit;
- precedência;
- responsabilidades do operador;
- limitações do target;
- status de conformidade;
- instrução para gerar Update Request quando houver drift ou lacuna.

### Critérios de pronto

- Package declara target, validade, fontes e limites.
- Não tenta carregar todo o corpus.
- ChatGPT Handoff não presume acesso a hash real.
- Claude Code/Codex recebem instruções compatíveis com filesystem.

## 24.8 P0.5 — Update Protocol mínimo

### Objetivo

Fechar o ciclo de evolução entre instâncias Maui e operadores com acesso ao corpus.

### Artefatos prioritários

```text
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
exec-requests/examples/update-request-example.md
exports/examples/update-package-example.md
exec-reports/examples/update-report-example.md
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
```

### Fluxo mínimo

```text
1. Instância identifica lacuna ou drift
2. Gera Update Request
3. Claude Code/Codex lê request
4. Gera Update Package
5. Humano aplica ou aprova
6. Gera Update Report
```

### Critérios de pronto

- Os três artefatos têm schema.
- Há exemplo válido de cada um.
- Há procedure de verificação e integração.
- Mudança normativa exige Human Gate.

## 24.9 P0.6 — Skills P0 para agentes de codificação

### Objetivo

Transformar operações repetíveis em capacidades reutilizáveis por Claude Code/Codex.

### Ordem das skills

```text
1. skills/maui-vault-health/SKILL.md
2. skills/maui-frontmatter-validate/SKILL.md
3. skills/maui-context-export/SKILL.md
4. skills/maui-update-export/SKILL.md
5. skills/maui-doc-consistency-check/SKILL.md
6. skills/maui-registry-maintenance/SKILL.md
7. skills/maui-memory-maintenance/SKILL.md
```

### Skills adiáveis

```text
skills/maui-memory-create/SKILL.md
skills/maui-roadmap-audit/SKILL.md
skills/maui-instance-integrate-update/SKILL.md
```

### Critérios de pronto

- Cada skill tem `SKILL.md` com frontmatter válido.
- Cada skill declara quando usar e quando não usar.
- Cada skill aponta scripts/procedures relacionados.
- Skills destrutivas exigem dry-run antes de write.

## 24.10 P0.7 — Procedures P0 e reflexes críticos

### Objetivo

Garantir operação manual e semiassistida mesmo quando scripts/skills ainda estiverem incompletos.

### Procedures prioritárias

```text
procedures/procedimento-validar-vault.md
procedures/procedimento-exportar-contexto.md
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
procedures/procedimento-criar-operator-pack.md
procedures/procedimento-captura-explicita.md
```

### Reflexes prioritários

```text
reflexes/reflexo-se-frontmatter-invalido.md
reflexes/reflexo-se-falta-contexto.md
reflexes/reflexo-se-instancia-pede-update.md
reflexes/reflexo-se-escrita-persistente.md
reflexes/reflexo-se-plugin-externo.md
```

### Critérios de pronto

- Procedures executáveis por humano técnico.
- Reflexes têm gatilho inequívoco.
- Operações de escrita declaram Human Gate quando aplicável.
- Existe rollback em operação destrutiva.

## 24.11 P0.8 — Evals e smoke tests mínimos

### Objetivo

Garantir que o Maui não quebre ao iniciar uso real.

### Evals prioritárias

```text
evals/regression/corpus-integrity.eval.yaml
evals/scripts/maui-vault-health.eval.yaml
evals/update-protocol/request-package-report.eval.yaml
evals/operator-packs/claude-code-pack.eval.yaml
evals/operator-packs/codex-pack.eval.yaml
evals/context-packages/bootstrap-context.eval.yaml
```

### Critérios de pronto

- Cada eval tem fixture.
- Rodar eval gera relatório em `validations/`.
- Falha em update protocol, filesystem safety ou operator pack P0 bloqueia avanço para piloto.

## 24.12 P0.9 — Registro de decisão, memória mínima e curadoria file-based

### Objetivo

Permitir que o Maui aprenda e mantenha rastreabilidade desde o piloto inicial, sem automação excessiva.

### Artefatos prioritários

```text
memorias/YYYY/MM/YYYY-MM-DD-decisao-adocao-piloto-maui.md
procedures/procedimento-captura-explicita.md
panel/dashboard.md
panel/decisions/
panel/reports/
```

### Escopo P0

- registro manual ou semiassistido de decisões;
- dashboard Markdown simples;
- coleta de exec reports;
- sem UI;
- sem automação de promoção de insight.

### Critérios de pronto

- Decisões são registráveis.
- Exec reports são coletáveis.
- Memória tem frontmatter mínimo.
- Insight/adendo continua dependente de Human Gate.

## 24.13 P1 — Expansão operacional controlada

### Objetivo

Aumentar automação e ergonomia depois que o ciclo P0 estiver seguro.

### Funcionalidades P1

```text
hooks/session-start/check-instance-status.md
hooks/pre-write/guard-corpus-write.md
hooks/post-write/validate-frontmatter.md
subagents/maui-doc-reviewer.md
subagents/maui-schema-validator.md
subagents/maui-context-compressor.md
mcp-servers/read-only/
panel CLI completo
maui_memory_search.py lexical
operator-packs/cursor/
operator-packs/gemini/
```

### Critérios de entrada em P1

- P0.0 a P0.8 concluídos.
- Piloto Claude Code ou Codex executado pelo menos uma vez.
- Update Request/Package/Report testado.
- Validação mínima sem falhas críticas.

## 24.14 P2 — Integração avançada e distribuição

### Objetivo

Introduzir capacidades avançadas apenas após estabilidade do núcleo.

### Funcionalidades P2

```text
plugins/maui-core-essentials/
plugins/maui-instance-management/
plugins/maui-curation-pack/
automations/weekly-drift-check.yaml
automations/monthly-insight-review.yaml
mcp guarded-write
REST/Action para ChatGPT
painel com UI
subagentes avançados
busca vetorial de memória
```

### Critérios de entrada em P2

- P1 validado.
- Política de permissões testada.
- Human Gate operacional.
- Relatórios de validação consistentes.
- Decisão humana autorizando expansão.

## 24.15 Backlog explicitamente adiado

Estas funcionalidades não devem bloquear o início do Maui:

- UI completa do painel.
- Plugins externos.
- Automations com escrita persistente.
- MCP guarded-write.
- REST/Action para ChatGPT.
- Busca vetorial de memória.
- Subagentes numerosos ou especializados demais.
- Suporte completo a todos os targets.
- Instalação automática em múltiplas ferramentas.

## 24.16 Marco de primeiro uso real

O Maui está pronto para primeiro uso real quando:

1. A árvore `vault-maui/` existe.
2. Arquitetura e spec funcional estão salvas em `01_manifest/`.
3. `maui_vault_health.py` roda com relatório sem falhas críticas.
4. Existe context package bootstrap.
5. Existe operator pack para Claude Code ou Codex.
6. Existe schema e exemplo para Update Request/Package/Report.
7. Existe procedure de validação e update.
8. Existe pelo menos uma forma de registrar exec report.
9. O status de conformidade desconhecido é declarado como `unknown`, não como `current`.
10. Mudanças normativas continuam protegidas por Human Gate.
