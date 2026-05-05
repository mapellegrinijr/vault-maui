

⸻

titulo: Arquitetura Alvo — Maui
versao: 0.1
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: especificacao_arquitetural
escopo: projeto_maui
confidencialidade: interna
papel_primario: ai_solutions_architect
papeis_secundarios:

* agent_engineering
* development_engineer
* written_comms_core
    precedencia: 5
    baseado_em:
* “[[spec-tecnica-atualizacao-saara-maui-v2]]”
* “[[Handoff — Nova versão do Saara: Maui]]”
* “[[principios-fundacionais]]”
* “[[especificacao-completa]]”
* “[[spec-distribuicao]]”
* “[[spec-instanciacao-conformidade]]”
* “[[spec-context-injection]]”
* “[[spec-capture-layer]]”
* “[[spec-memory-store]]”
* “[[spec-adendos]]”
    tags:
* maui
* arquitetura
* corpus-procedural
* saara-evolution
* skills
* hooks
* subagents
* plugins
* mcp
* operator-packs
* context-engineering

⸻

Arquitetura Alvo — Maui

1. Resumo executivo

Maui é a nova arquitetura de evolução do Saara. A decisão central é que Maui não é uma aplicação, backend, chatbot, MCP server ou interface específica. Maui é um corpus cognitivo multipapel, procedural, portátil e instanciável por diferentes modelos e ferramentas de IA.

A identidade, governança, comportamento, memória e capacidades operacionais do Maui vivem no corpus versionado. Infraestruturas como toolkit, painel, scripts, MCP servers, adapters, bancos locais ou integrações são mecanismos auxiliares e substituíveis.

A arquitetura adota o princípio de soberania do corpus e o expande: além de documentos normativos, o corpus passa a conter também skills, procedures, scripts, hooks, subagentes, plugins, schemas, evals, automations, operator packs, context packages e protocolos de execução.

2. Decisão arquitetural principal

Produto principal = Maui Corpus
Ferramentas auxiliares = Maui Toolkit + scripts + painel + operadores + MCP servers

O antigo saara-core deixa de ser interpretado como centro do produto. Ele pode evoluir para Maui Toolkit, com responsabilidade de bootstrap, instanciação, validação, curadoria e distribuição, mas não define a identidade do Maui.

3. Equação do Maui

Maui = corpus
     + memória + PKAs + specs + adendos + insights
     + skills + procedures + reflexes + scripts
     + hooks + subagents + plugins
     + schemas + evals + automations
     + operator-packs + mcp-servers
     + context-packages + exec-requests/reports

Essa equação define o Maui como uma arquitetura corpus-first e tool-agnostic, capaz de operar em ambientes com filesystem direto, MCP, REST/Actions ou handoff humano.

4. Objetivos da nova arquitetura

1. Tornar o Maui instanciável em diferentes ferramentas de IA sem depender de um backend único.
2. Transformar capacidades operacionais em artefatos versionados no corpus.
3. Separar produto, toolkit e operadores.
4. Preservar compatibilidade com Saara v7.1.1 até decisão formal de substituição.
5. Adotar padrões abertos de 2026: Agent Skills, AGENTS.md, hooks lifecycle, subagents, plugins e MCP.
6. Garantir evolução governada via memória, adendos, insights, evals e Human Gate.
7. Manter portabilidade, auditabilidade, idempotência e reversibilidade.

5. Princípios arquiteturais

5.1 Soberania cognitiva ampliada

A identidade do Maui vive no corpus. Código, bancos, servidores e integrações são substituíveis.

Em Maui, a soberania cognitiva passa a incluir também capacidades executáveis:

* scripts de condicionamento;
* skills;
* procedures/runbooks;
* hooks;
* subagentes;
* plugins;
* schemas;
* evals;
* automations;
* operator packs.

5.2 Padrão aberto por default

Maui adota convenções abertas quando elas não violam a soberania do corpus:

* SKILL.md com frontmatter;
* AGENTS.md para agentes de codificação;
* MCP como protocolo de exposição;
* plugins como bundles versionados;
* hooks lifecycle para enforcement determinístico;
* evals como código;
* context engineering como disciplina operacional.

5.3 Determinismo onde possível

Regras críticas não devem depender apenas de prompt. Quando possível, devem ser implementadas por:

* schemas;
* validações;
* scripts idempotentes;
* hooks;
* testes/evals;
* contratos de entrada e saída.

5.4 Output contract first

Todo entregável relevante do Maui deve declarar:

* contrato de entrada;
* contrato de saída;
* critérios de sucesso;
* riscos e limites;
* sinalização F/I/H quando houver fatos, inferências ou hipóteses materiais.

5.5 Context engineering

Maui evolui o Context Injection do Saara para uma disciplina explícita:

Write   → registrar e estruturar contexto reutilizável
Select  → selecionar o contexto certo para a tarefa
Compress→ compactar sem perder governança
Isolate → separar escopos, papéis, confidencialidade e ferramentas

6. Visão em camadas

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

7. Componentes arquiteturais

7.1 Maui Corpus

Produto principal. Fonte de verdade de identidade, comportamento, memória, governança, procedimentos e capacidades operacionais.

Responsabilidades:

* armazenar normativos, PKAs, specs e princípios;
* manter memória, adendos e insights;
* versionar skills, procedures, scripts e hooks;
* declarar schemas, evals e contratos;
* conter operator packs e context packages;
* suportar execução por agentes humanos e modelos de IA.

7.2 Maui Toolkit

Conjunto auxiliar para operar o corpus. Não é o produto.

Responsabilidades:

* criar estrutura inicial do corpus;
* gerar templates;
* instanciar Maui em ferramentas-alvo;
* preparar operator packs;
* executar validações;
* oferecer painel de curadoria;
* expor capacidades via CLI, filesystem, MCP ou REST quando aplicável.

Comandos conceituais:

maui init --path ./vault-maui --template standard
maui instantiate --target claude-code
maui instantiate --target codex
maui instantiate --target chatgpt
maui panel status
maui panel dispatch
maui panel collect
maui panel record-decision

7.3 Scripts de condicionamento

Scripts versionados no corpus que executam operações determinísticas e primitivas.

Scripts P0:

scripts/maui_registry.py
scripts/maui_memory_index.py
scripts/maui_context_export.py
scripts/maui_update_export.py

Responsabilidades:

* registry de instâncias;
* indexação de memória;
* exportação de contexto;
* geração de update packages;
* validação de integridade;
* suporte a instâncias sem filesystem direto.

7.4 Skills

Capacidades operacionais reutilizáveis, compatíveis com padrão SKILL.md.

Estrutura esperada:

skills/
├── maui-vault-health/
│   └── SKILL.md
├── maui-context-export/
│   └── SKILL.md
└── maui-frontmatter-validate/
    └── SKILL.md

Contrato mínimo de skill:

* propósito claro;
* quando usar;
* inputs;
* outputs;
* passos;
* ferramentas permitidas;
* critérios de sucesso;
* limites e riscos.

7.5 Procedures / Runbooks

Procedimentos explícitos para operações recorrentes.

Exemplos:

* atualizar instância Maui;
* criar novo operator pack;
* promover insight para adendo;
* validar corpus antes de release;
* gerar handoff para ferramenta sem filesystem.

7.6 Hooks

Camada de enforcement determinístico em eventos do ciclo de vida.

Exemplos de eventos:

* SessionStart;
* PreToolUse;
* PostToolUse;
* Stop;
* OnExport;
* OnCapture.

Usos prioritários:

* carregar contexto mínimo no início da sessão;
* bloquear escrita insegura;
* validar frontmatter;
* registrar exec reports;
* aplicar sanitização antes de captura;
* impedir drift silencioso.

7.7 Subagentes

Construto nativo para especialização e isolamento de tarefas.

Modelos suportados:

1. Subagentes nominais — especialistas pré-definidos, com escopo, tools e contratos fixos.
2. Clones via Task — delegações temporárias decididas pela instância principal, com contexto limitado e retorno resumido.

Exemplos:

* maui-doc-reviewer;
* maui-schema-validator;
* maui-context-compressor;
* maui-update-planner;
* maui-memory-curator.

7.8 Plugins

Bundles versionados que empacotam skills, hooks, subagents e commands.

Estrutura:

plugins/
├── maui-core-essentials/
│   ├── plugin.yaml
│   ├── skills/
│   ├── hooks/
│   └── subagents/
├── maui-curation-pack/
├── maui-instance-management/
└── maui-eval-toolkit/

Critérios:

* instalação sem conflito de nomes;
* namespacing explícito;
* validação de dependências;
* desinstalação sem resíduos;
* versão e changelog obrigatórios.

7.9 MCP Servers

Maui pode expor capacidades selecionadas via MCP servers locais ou controlados. Maui não é um MCP server; MCP é apenas um protocolo de acesso.

Usos:

* consulta ao corpus;
* retrieve de contexto;
* exportação de packages;
* validação de instância;
* execução controlada de scripts;
* capture layer assistida.

7.10 Operator Packs

Pacotes de adaptação para ferramentas específicas.

Targets iniciais:

* Claude Code;
* Codex;
* ChatGPT;
* Gemini;
* Cursor;
* Antigravity;
* Claude Desktop.

Conteúdo típico:

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

8. Estrutura física alvo

vault-maui/
├── 00_core/                      # Normativo herdado/evoluído
├── 01_manifest/                  # Definição de produto e arquitetura
├── memoria/                      # Memórias operacionais e episódicas
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

9. Topologia operacional

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

10. Modos de operação por ferramenta

Ferramenta	Modo principal	Modo secundário	Observação
Claude Code	Filesystem + skills/hooks	MCP	Primeiro operador ideal
Codex	Filesystem + AGENTS.md	Skills em .agents/	Segundo operador ideal
Cursor	Filesystem + rules	MCP	Adequado para desenvolvimento
Claude Desktop	MCP	Project knowledge	Bom para consulta e curadoria
ChatGPT com Action	REST/Action	Handoff humano	Depende de endpoint autenticado
ChatGPT sem Action	Handoff humano	Upload manual	Não presume hash real
Gemini	Gem / filesystem quando disponível	REST/MCP conforme suporte	Requer operator pack específico

11. Protocolo de atualização

O protocolo de atualização é baseado em três artefatos:

Update Request  →  Update Package  →  Update Report

11.1 Update Request

Solicitação estruturada gerada por uma instância Maui ou por humano.

Contém:

* instância de origem;
* versão percebida;
* objetivo da atualização;
* escopo;
* restrições;
* formato desejado;
* evidências e arquivos relevantes.

11.2 Update Package

Pacote gerado por ferramenta com acesso ao corpus ou pelo Maui Toolkit.

Contém:

* mudanças propostas;
* arquivos afetados;
* diff ou instruções;
* validações executadas;
* riscos;
* instruções de aplicação;
* rollback quando aplicável.

11.3 Update Report

Relatório pós-execução.

Contém:

* o que foi aplicado;
* o que falhou;
* validações executadas;
* drift remanescente;
* recomendações;
* decisão humana quando necessária.

12. Fluxo de atualização

1. Instância detecta necessidade de evolução ou drift
2. Instância gera exec-request estruturado
3. Operador com filesystem/MCP lê corpus e request
4. Operador executa scripts/skills/procedures autorizados
5. Operador gera update package
6. Instância ou humano aplica pacote
7. Validações e evals são executados
8. Exec report registra resultado
9. Decisões relevantes viram memória/adendo/insight

Regra: instância sem filesystem ou endpoint autenticado não calcula hash real e não presume estar atualizada.

13. Governança e lifecycle

13.1 Precedência

A arquitetura Maui preserva a precedência do Saara v7.1.1 até decisão formal de substituição:

1. Políticas externas, lei e compliance.
2. System prompt ativo.
3. Princípios Fundacionais.
4. Especificação Completa.
5. PKAs e specs técnicas.
6. Parametrização executável.
7. Conteúdo recuperado.
8. Pedido do usuário.

13.2 Human Gate

Exige aprovação humana:

* adoção formal do Maui como substituto do Saara v7.1.1;
* alteração de princípios fundacionais;
* promoção de adendos para ativo ou merged;
* mudanças de precedência;
* instalação de plugins externos;
* exposição MCP/REST que escreva no corpus;
* automations com escrita persistente.

13.3 Drift e conformidade

Cada instância deve manter estado verificável quando o ambiente permitir:

* tool_id;
* target;
* versão instanciada;
* hash quando disponível;
* operator pack usado;
* PKAs carregadas;
* adendos e insights carregados;
* último check;
* severidade de drift.

Estados:

current
minor_drift
major_drift
incompatible
unknown

unknown é obrigatório para instâncias sem filesystem, sem registry ou sem endpoint autenticado.

14. Context engineering

14.1 Camadas de contexto

Maui preserva a lógica A/B/C e a amplia operacionalmente:

Camada	Conteúdo	Cadência	Meio
A	identidade, princípios, PKAs, specs base	instanciação	Project, Custom GPT, Gem, CLAUDE.md, AGENTS.md
B	adendos, insights, correções, drift	início de sessão	MCP, REST, package, handoff
C	memórias e referências relevantes	sob demanda	retrieve, context package, MCP

14.2 Regras

* Não existe modo normal de “carregar tudo”.
* Contexto deve ser selecionado por relevância e escopo.
* Contexto sensível deve respeitar confidencialidade e separação de domínios.
* Todo context package deve declarar objetivo, alvo, validade e limites.
* Compressão deve preservar decisões, contratos e riscos.

15. Capture Layer e Insight Pipeline

Maui mantém a Capture Layer como mecanismo sancionado de escrita em memória operacional.

Fluxo:

Conversa/execução
  → captura seletiva
  → compactação sanitizada
  → memória estruturada
  → detecção de padrões
  → insight
  → candidato a adendo
  → Human Gate
  → adendo ativo ou rejeitado

Critérios de captura:

* comando explícito do usuário;
* decisão registrável;
* artefato reutilizável;
* preferência ou aprendizado declarado;
* alta densidade informacional;
* resultado de execução relevante.

16. Qualidade, validação e evals

16.1 Validações mínimas

* frontmatter obrigatório;
* links internos resolvíveis;
* schemas válidos;
* operator packs completos;
* scripts idempotentes;
* ausência de escrita fora do escopo;
* changelog em mudanças materiais;
* compatibilidade com Saara v7.1.1 até decisão formal.

16.2 Evals como código

Skills e procedures críticas devem ter evals versionadas.

Exemplos:

evals/
├── skills/
│   ├── maui-context-export.eval.yaml
│   └── maui-frontmatter-validate.eval.yaml
├── update-protocol/
│   └── update-request-package-report.eval.yaml
└── regression/
    └── corpus-integrity.eval.yaml

Critérios:

* regressão detectável;
* fixtures versionadas;
* resultado reproduzível;
* falha bloqueia release quando severidade for alta.

17. Segurança e privacidade

Regras base:

* privacidade por padrão;
* menor privilégio para tools, hooks e subagentes;
* separação entre escopos pessoal/trabalho/projeto;
* nenhuma escrita persistente sem trilha;
* sanitização antes de memória;
* plugins externos tratados como não confiáveis até validação;
* MCP/REST com autenticação e escopo explícito quando houver escrita;
* rollback obrigatório para alterações destrutivas.

18. Fronteiras arquiteturais

18.1 Maui é

* corpus cognitivo multipapel;
* arquitetura procedural;
* sistema instanciável;
* conjunto de contratos, skills, procedures e scripts;
* produto tool-agnostic;
* base de governança e memória.

18.2 Maui não é

* aplicação SaaS;
* app desktop;
* chatbot único;
* backend;
* banco de dados;
* MCP server específico;
* interface gráfica;
* Claude, ChatGPT, Gemini, Codex, Cursor ou Antigravity.

18.3 Maui Toolkit é

* auxiliar;
* reconstruível;
* substituível;
* operador do corpus;
* não fonte de identidade.

19. Plano incremental recomendado

Fase 0 — Formalização

* Salvar arquitetura alvo em 01_manifest/.
* Registrar decisão Saara → Maui como memória.
* Definir status oficial: proposta, piloto ou adoção.
* Criar changelog e owner.

Fase 1 — Estrutura mínima

* Criar árvore vault-maui/.
* Criar schemas mínimos.
* Criar scripts P0.
* Criar context package inicial.
* Criar operator packs Claude Code e Codex.

Fase 2 — Operação assistida

* Gerar CLAUDE.md e AGENTS.md por template.
* Validar maui_update_export.py.
* Testar Update Request/Package/Report.
* Executar piloto com Claude Code.
* Registrar exec reports.

Fase 3 — Qualidade e curadoria

* Criar evals P0.
* Criar hooks de validação.
* Criar subagentes nominais.
* Implementar painel CLI/file-based.
* Definir critérios de release.

Fase 4 — Integração ampliada

* Expor MCP servers selecionados.
* Criar Action/REST para ChatGPT quando seguro.
* Expandir operator packs.
* Introduzir automations controladas.
* Consolidar plugins P0.

20. Decisões registradas

Decisão	Status	Observação
Maui é corpus, não aplicação	proposta consolidada	base da arquitetura
Saara Core vira toolkit auxiliar	proposta consolidada	não fonte de identidade
Scripts P0 vivem no corpus	proposta consolidada	registry, memory-index, context-export, update-export
Skills usam padrão SKILL.md	proposta v2	alinhamento 2026
Hooks são camada determinística	proposta v2	enforcement não-alucinatório
Subagentes são nativos	proposta v2	nominais + clones via Task
Plugins são unidade distribuível	proposta v2	bundles versionados
MCP é protocolo de primeira classe	proposta v2	não identidade do produto
Update Protocol usa request/package/report	proposta consolidada	tool-agnostic
ChatGPT sem Action usa handoff humano	proposta consolidada	não presume filesystem/hash

21. Riscos e controles

Risco	Impacto	Controle
Recriar acoplamento ao toolkit	Alto	reforçar corpus-first em docs e gates
Drift entre instâncias	Alto	registry, hashes, update reports
Plugins externos inseguros	Alto	Human Gate, sandbox, validação de manifest
Contexto excessivo	Médio	context engineering, orçamento e compressão
Scripts com efeitos destrutivos	Alto	idempotência, dry-run e rollback
Ambiguidade entre skill/procedure/script	Médio	taxonomia e exemplos canônicos
Captura indevida de memória	Alto	sanitização, escopo, capture layer seletiva
Evals insuficientes	Médio	suíte P0 antes de release operacional

22. Contrato operacional resultante

A evolução deve seguir este contrato:

1. Toda mudança estrutural do Maui deve ser representada primeiro no corpus.
2. Toolkit, scripts e MCP servers só implementam contratos já descritos no corpus.
3. Instâncias com acesso a filesystem podem validar hash; instâncias sem acesso devem declarar estado unknown.
4. Toda capability crítica precisa de output contract e success criteria.
5. Toda escrita persistente em memória, adendo, insight ou spec deve passar por governança proporcional.
6. O piloto inicial deve priorizar Claude Code e Codex.
7. ChatGPT/Gemini sem filesystem devem operar via context packages e handoff estruturado.
8. Maui permanece proposta até decisão explícita de governança substituir ou promover o Saara v7.1.1.

23. F/I/H

Fatos

* Maui foi definido como nova geração do Saara.
* Maui é corpus cognitivo multipapel, procedural, portátil e instanciável.
* O produto principal é o corpus; toolkit, scripts e painel são auxiliares.
* A arquitetura herda princípios, PKAs e governança do Saara v7.1.1.
* A spec v2 adiciona Agent Skills, hooks, subagents, plugins, MCP, AGENTS.md, context engineering, automations e evals.

Inferências

* 01_manifest/ deve conter esta arquitetura alvo como documento canônico.
* Claude Code e Codex são os melhores pilotos iniciais por acesso a filesystem.
* ChatGPT sem Action deve depender de handoff humano ou upload manual.
* O painel MVS deve começar como CLI/file-based antes de UI.

Hipóteses

* Maui será adotado primeiro como proposta/piloto antes de substituir formalmente Saara v7.1.1.
* MCP servers devem começar somente com capacidades de leitura ou validação antes de permitir escrita.
* Plugins P0 devem ser internos antes de consumo de plugins externos.

⸻

Anexo A — Artefatos P0 sugeridos

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

Anexo B — Critérios de aceite da arquitetura

* A arquitetura deixa claro que Maui é corpus, não aplicação.
* A separação corpus/toolkit/operator está explícita.
* As camadas arquiteturais estão definidas.
* A estrutura física alvo está especificada.
* O protocolo Update Request/Package/Report está descrito.
* A estratégia multi-ferramenta está definida.
* Governança, segurança, contexto, captura e evals estão cobertos.
* Há plano incremental e riscos com controles.