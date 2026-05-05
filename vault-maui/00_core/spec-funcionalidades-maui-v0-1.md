---
titulo: "Spec Unificada — Funcionalidades Maui"
versao: "0.1"
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: especificacao_funcional
escopo: projeto_maui
---

# Spec Unificada — Funcionalidades Maui

## Nota de reconciliação de status e alinhamento

> Esta especificação funcional foi promovida ao `vault-maui/00_core/` após a execução parcial da adaptação Saara→Maui. O documento preserva seu conteúdo original de planejamento funcional e ainda requer reconciliação dedicada com a arquitetura Maui v0.2, o roadmap Maui v1.0, schemas já criados, handoffs e exec-reports posteriores.
>
> Até esta promoção, há evidências operacionais de conclusão de etapas até P0.1.14, incluindo inventário de `Documentação/`, classificação arquivo a arquivo, aplicação do Lote A, promoção da arquitetura Maui v0.2 ao core e promoção do roadmap Maui v1.0 ao core. Esta nota não atualiza automaticamente o status das funcionalidades nem resolve possíveis divergências; apenas marca a necessidade de revisão controlada posterior.

## 0. Finalidade do documento

Este documento consolida, em um único arquivo Markdown, as especificações funcionais da arquitetura Maui. Cada funcionalidade é definida em seção própria, com escopo, responsabilidades, contratos, critérios de aceite, riscos e relação com as demais partes do sistema.

A arquitetura base é corpus-first: **Maui é o corpus cognitivo multipapel, procedural, portátil e instanciável**. Toolkit, painel, scripts, MCP servers, adapters, bancos locais e operator packs são auxiliares substituíveis.

```text
Produto principal = Maui Corpus
Ferramentas auxiliares = Maui Toolkit + scripts + painel + operadores + MCP servers
```

## 1. Índice das funcionalidades

1. Maui Corpus
2. Maui Toolkit
3. Scripts de Condicionamento
4. Skills
5. Procedures e Reflexes
6. Hooks
7. Subagentes
8. Plugins
9. MCP Servers
10. Operator Packs
11. Context Engineering e Context Packages
12. Update Protocol
13. Schemas e Contratos Estruturados
14. Evals
15. Automations
16. Capture Layer, Memory e Insight Pipeline
17. Painel de Curadoria
18. Governança, Segurança e Human Gate
19. Estrutura física alvo
20. Roadmap incremental
21. Critérios globais de aceite
22. F/I/H

---

# 2. Funcionalidade — Maui Corpus

## 2.1 Propósito

Definir o **Maui Corpus** como produto principal da arquitetura Maui: a fonte de verdade versionada que contém identidade, governança, memória, procedimentos, capacidades operacionais e contratos de execução.

## 2.2 Decisão normativa

Maui é o corpus. Toolkit, painel, MCP servers, scripts executáveis, bancos locais, adapters, agentes e integrações são mecanismos auxiliares. Nenhum deles define a identidade do Maui.

```text
Corpus define → infraestrutura executa
Infraestrutura falha → corpus permanece íntegro
Evolução real → commit governado no corpus
```

## 2.3 Escopo

Inclui:

- documentos normativos;
- princípios;
- PKAs;
- specs;
- adendos;
- insights;
- memórias;
- skills;
- procedures;
- reflexes;
- scripts;
- hooks;
- subagentes;
- plugins;
- schemas;
- evals;
- automations;
- operator packs;
- context packages;
- exec requests/reports;
- update packages;
- validações.

Não inclui como identidade:

- Maui Toolkit;
- banco local `.maui/` ou `.saara/`;
- servidor MCP específico;
- Custom GPT, Gem, Claude Project, Claude Code, Codex ou Cursor;
- painel de curadoria;
- API REST;
- runtime de fornecedor específico.

## 2.4 Contrato de arquivo

Todo artefato normativo ou operacional persistente deve conter frontmatter YAML mínimo:

```yaml
titulo: string
versao: string
status: proposta | ativo | depreciado | arquivado | experimental
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: string
escopo: projeto_maui
confidencialidade: publica | interna | restrita
precedencia: number
referencias: []
tags: []
```

## 2.5 Regras de versionamento

1. Mudança material exige incremento de versão.
2. Mudança normativa exige changelog.
3. Breaking change exige seção explícita `Impacto de migração`.
4. Arquivo substituído deve apontar `substitui` ou `substituido_por`.
5. Status `ativo` só deve ser usado após validação humana quando a mudança alterar comportamento.

## 2.6 Estados permitidos

| Status         | Uso                                                 |
| -------------- | --------------------------------------------------- |
| `proposta`     | artefato em desenho ou piloto                       |
| `ativo`        | aprovado para uso operacional                       |
| `depreciado`   | ainda legível, não recomendado para novas operações |
| `arquivado`    | histórico, não usado em runtime                     |
| `experimental` | permitido apenas em sandbox ou piloto               |

## 2.7 Critérios de aceite

- O arquivo existe no diretório correto.
- Frontmatter obrigatório está completo.
- Links internos principais são resolvíveis.
- Escopo e confidencialidade estão declarados.
- Se for executável ou acionável, possui contrato de entrada/saída.
- Se alterar comportamento, possui critérios de sucesso e riscos.

## 2.8 Riscos e controles

| Risco                             | Controle                                          |
| --------------------------------- | ------------------------------------------------- |
| Confundir corpus com toolkit      | Repetir fronteira em specs, manifests e templates |
| Espalhar artefatos fora da árvore | Validação de estrutura do vault                   |
| Arquivos sem metadados            | Hook/skill de frontmatter obrigatório             |
| Evolução não auditável            | Changelog + commit + exec report                  |

---

# 3. Funcionalidade — Maui Toolkit

## 3.1 Propósito

Definir o Maui Toolkit como conjunto auxiliar para inicializar, validar, instanciar e operar o Maui Corpus sem se tornar fonte de identidade.

## 3.2 Fronteira arquitetural

O Toolkit executa contratos do corpus. Ele não cria política por conta própria, não substitui specs e não decide governança normativa.

```text
Corpus define → Toolkit executa
Toolkit falha → Corpus continua íntegro
```

## 3.3 Funcionalidades P0

### 3.3.1 `maui init`

Cria estrutura inicial do `vault-maui/`.

```bash
maui init --path ./vault-maui --template standard --dry-run
```

Saídas esperadas:

- árvore de diretórios;
- arquivos placeholder;
- relatório de criação;
- lista de próximos passos.

Critérios:

- idempotente;
- nunca sobrescreve arquivo existente sem `--force`;
- suporta `--dry-run`;
- gera relatório em Markdown e JSON.

### 3.3.2 `maui instantiate`

Gera artefatos para uma ferramenta-alvo.

```bash
maui instantiate --target claude-code --vault ./vault-maui --out ./generated/claude-code
```

Targets P0:

- `claude-code`;
- `codex`;
- `chatgpt-handoff`.

### 3.3.3 `maui validate`

Executa validações locais.

```bash
maui validate --scope corpus --format markdown
```

Valida:

- frontmatter;
- estrutura de diretórios;
- links;
- schemas;
- operator packs;
- scripts P0;
- permissões e riscos conhecidos.

### 3.3.4 `maui panel`

MVS do painel de curadoria, file-based/CLI.

```bash
maui panel status
maui panel dispatch --request exec-requests/001.md
maui panel collect --from exec-reports/
maui panel record-decision --file decisions/001.md
```

## 3.4 Funcionalidades P1

- servidor MCP local;
- API REST autenticada;
- UI local;
- automations agendadas;
- integração com Git;
- geração de diffs aplicáveis;
- painel multi-instância.

## 3.5 Requisitos não funcionais

| Requisito       | Critério                                                         |
| --------------- | ---------------------------------------------------------------- |
| Portabilidade   | Python padrão ou runtime simples; evitar dependências pesadas P0 |
| Segurança       | read-only por default; escrita exige flag explícita              |
| Auditabilidade  | toda operação que escreve gera relatório                         |
| Idempotência    | rodar duas vezes não deve duplicar nem corromper                 |
| Reversibilidade | operações destrutivas exigem backup/rollback                     |
| Observabilidade | logs locais estruturados em `.maui/logs/`                        |

## 3.6 Modelo de permissões

| Operação              | Default   | Requer confirmação |
| --------------------- | --------- | ------------------ |
| leitura do corpus     | permitido | não                |
| validação             | permitido | não                |
| geração em `exports/` | permitido | não                |
| alteração de specs    | bloqueado | sim                |
| alteração de memória  | bloqueado | sim                |
| instalação de plugin  | bloqueado | sim                |
| escrita por MCP/REST  | bloqueado | sim + autenticação |

## 3.7 Contrato de saída padrão

```yaml
operation_id: string
started_at: datetime
finished_at: datetime
status: success | partial | failed
inputs: object
outputs: object
changed_files: []
warnings: []
errors: []
next_steps: []
```

## 3.8 Critérios de aceite

- CLI executa `init`, `instantiate`, `validate` e `panel status`.
- Nenhuma escrita ocorre sem destino explícito.
- Todo comando suporta `--help`.
- Comandos de escrita suportam `--dry-run`.
- Relatórios são salvos em `validations/` ou `exec-reports/`.

---

# 4. Funcionalidade — Scripts de Condicionamento

## 4.1 Propósito

Definir scripts pequenos, portáveis, auditáveis e idempotentes que funcionam como “memória muscular” do Maui. Eles executam operações determinísticas descritas pelo corpus.

## 4.2 Princípios

1. Script é ferramenta, não política.
2. Read-only por default.
3. Toda escrita exige flag explícita.
4. Toda escrita gera relatório.
5. Deve ser possível executar por humano, agente de codificação ou MCP tool.
6. Falha segura: em dúvida, não escrever.

## 4.3 Scripts P0

### 4.3.1 `maui_registry.py`

Responsabilidade: manter registry de instâncias.

Comandos mínimos:

```bash
python scripts/maui_registry.py list --format markdown
python scripts/maui_registry.py register --tool-id claude_code_main --target claude-code --write
python scripts/maui_registry.py check --tool-id claude_code_main --format json
```

Dados mínimos:

```yaml
tool_id: string
target: claude-code | codex | chatgpt | gemini | cursor | other
label: string
instantiated_version: string
instantiated_hash: string | unknown
operator_pack: string
status: current | minor_drift | major_drift | incompatible | unknown
last_check_at: datetime
notes: string
```

### 4.3.2 `maui_memory_index.py`

Responsabilidade: indexar memórias Markdown sem transformar índice em fonte de verdade.

Operações:

- listar memórias;
- validar frontmatter;
- gerar índice JSON/SQLite reconstruível;
- detectar duplicidade provável;
- reportar memórias sem escopo ou confidencialidade.

### 4.3.3 `maui_memory_search.py`

Responsabilidade: busca local simples em `memorias/`, `insights/` e `adendos/`.

P0 pode ser lexical. Busca vetorial é P1.

### 4.3.4 `maui_context_export.py`

Responsabilidade: gerar context packages por target.

```bash
python scripts/maui_context_export.py --target chatgpt --scope bootstrap --out context-packages/generated/chatgpt-bootstrap.md
```

Saídas:

- pacote Markdown;
- manifesto JSON;
- lista de fontes incluídas;
- orçamento de tokens estimado quando possível.

### 4.3.5 `maui_update_export.py`

Responsabilidade: gerar Update Package a partir de Update Request.

```bash
python scripts/maui_update_export.py --request exec-requests/update-001.md --out exports/update-001/ --dry-run
```

Saídas:

- `update-package.md`;
- `manifest.yaml`;
- patches opcionais;
- validações executadas;
- rollback plan.

### 4.3.6 `maui_validate_frontmatter.py`

Valida frontmatter por tipo de documento.

### 4.3.7 `maui_validate_links.py`

Valida links internos `[[...]]` e caminhos relativos.

### 4.3.8 `maui_vault_health.py`

Executa diagnóstico geral do vault.

## 4.4 Interface padrão

Todo script P0 deve aceitar:

```bash
--help
--dry-run
--format markdown|json
--out PATH
--verbose
```

Scripts que escrevem devem aceitar:

```bash
--write
--force
--backup
```

## 4.5 Saída JSON padrão

```json
{
  "script": "maui_context_export.py",
  "version": "0.1",
  "status": "success",
  "dry_run": true,
  "changed_files": [],
  "warnings": [],
  "errors": [],
  "artifacts": []
}
```

## 4.6 Segurança de filesystem

- Nunca escrever fora do `vault-maui/` ou diretório `--out` explicitamente permitido.
- Resolver path traversal (`../`) antes de qualquer escrita.
- Criar backup antes de sobrescrever.
- Bloquear symlinks por default em operações destrutivas.

## 4.7 Testes mínimos

Cada script deve ter:

- teste de `--help`;
- teste de `--dry-run`;
- fixture mínima;
- teste de falha segura;
- teste de saída JSON válida.

## 4.8 Critérios de aceite

- Scripts P0 executam isoladamente.
- Não exigem Maui Toolkit grande.
- São chamáveis por Claude Code/Codex.
- Podem ser expostos como MCP tools futuramente.
- Geram relatório compatível com `exec-reports/`.

---

# 5. Funcionalidade — Skills

## 5.1 Propósito

Definir o padrão de skills do Maui como capacidades operacionais reutilizáveis, expressas em diretórios com `SKILL.md`, compatíveis com ferramentas de agentes e assistentes de codificação.

## 5.2 Relação entre skill, procedure e script

| Artefato  | Função                                         |
| --------- | ---------------------------------------------- |
| Skill     | ensina uma capacidade a um agente              |
| Procedure | descreve um processo operacional passo a passo |
| Script    | executa ação determinística                    |
| Hook      | aplica regra em evento de ciclo de vida        |
| Eval      | verifica se a skill funciona                   |

Uma skill pode chamar procedures e scripts. Uma skill não deve redefinir governança.

## 5.3 Estrutura padrão

```text
skills/nome-da-skill/
├── SKILL.md
├── examples/
├── fixtures/
├── tests/
└── README.md        # opcional
```

## 5.4 Frontmatter obrigatório de `SKILL.md`

```yaml
titulo: Skill — Nome
skill_id: maui-nome
versao: 0.1
status: proposta
descricao: string
quando_usar:
  - string
quando_nao_usar:
  - string
inputs:
  - nome: string
    tipo: string
    obrigatorio: true
outputs:
  - nome: string
    tipo: string
ferramentas_permitidas:
  - filesystem_read
  - filesystem_write_guarded
riscos:
  - string
success_criteria:
  - string
```

## 5.5 Corpo obrigatório

Toda skill deve conter:

1. propósito;
2. gatilhos de uso;
3. pré-condições;
4. entradas;
5. saídas;
6. procedimento resumido;
7. ferramentas permitidas;
8. limites;
9. critérios de sucesso;
10. exemplos;
11. critérios de falha segura.

## 5.6 Skills P0

```text
skills/maui-registry-maintenance/SKILL.md
skills/maui-memory-maintenance/SKILL.md
skills/maui-memory-create/SKILL.md
skills/maui-context-export/SKILL.md
skills/maui-update-export/SKILL.md
skills/maui-instance-update-check/SKILL.md
skills/maui-instance-integrate-update/SKILL.md
skills/maui-roadmap-audit/SKILL.md
skills/maui-doc-consistency-check/SKILL.md
skills/maui-vault-health/SKILL.md
```

## 5.7 Contrato de execução

Uma skill executada por agente deve produzir:

```yaml
skill_id: string
objective: string
inputs_used: object
steps_executed: []
artifacts_created: []
validation: []
risks: []
status: success | partial | failed
next_action: string
```

## 5.8 Regras de segurança

- Skill não concede permissão; apenas declara necessidade.
- Escrita persistente exige confirmação ou contexto autorizado.
- Skill crítica precisa de eval.
- Skill que chama script destrutivo deve exigir `--dry-run` antes de `--write`.

## 5.9 Critérios de aceite

- `SKILL.md` tem frontmatter válido.
- Possui gatilhos positivos e negativos.
- Possui success criteria mensuráveis.
- Declara ferramentas permitidas.
- Possui exemplo mínimo.
- Está mapeada em operator pack quando aplicável.

---

# 6. Funcionalidade — Procedures e Reflexes

## 6.1 Propósito

Definir procedures/runbooks e reflexes como camada procedural do Maui para operações recorrentes, seguras e repetíveis.

## 6.2 Diferença entre procedure e reflex

| Tipo      | Definição                                         | Tamanho típico | Uso                     |
| --------- | ------------------------------------------------- | -------------- | ----------------------- |
| Procedure | runbook completo com passos, validação e rollback | médio/longo    | operação recorrente     |
| Reflex    | microprocedimento acionado por condição clara     | curto          | resposta rápida a sinal |

## 6.3 Estrutura de procedure

```text
procedures/procedimento-nome.md
```

Seções obrigatórias:

1. objetivo;
2. quando usar;
3. quando não usar;
4. pré-condições;
5. entradas;
6. passos;
7. validação;
8. rollback;
9. output esperado;
10. riscos.

## 6.4 Estrutura de reflex

```text
reflexes/reflexo-se-condicao.md
```

Seções obrigatórias:

1. gatilho;
2. ação imediata;
3. limite;
4. escalonamento;
5. registro esperado.

## 6.5 Procedures P0

```text
procedures/procedimento-gerenciar-registry.md
procedures/procedimento-indexar-memorias.md
procedures/procedimento-exportar-contexto.md
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
procedures/procedimento-criar-memoria.md
procedures/procedimento-captura-explicita.md
procedures/procedimento-curadoria-painel.md
procedures/procedimento-validar-vault.md
procedures/procedimento-criar-operator-pack.md
```

## 6.6 Reflexes P0

```text
reflexes/reflexo-se-hash-mudou.md
reflexes/reflexo-se-context-package-defasado.md
reflexes/reflexo-se-instancia-pede-update.md
reflexes/reflexo-se-frontmatter-invalido.md
reflexes/reflexo-se-plugin-externo.md
reflexes/reflexo-se-escrita-persistente.md
reflexes/reflexo-se-falta-contexto.md
```

## 6.7 Contrato de saída

Toda execução de procedure deve gerar registro:

```yaml
procedure_id: string
executed_by: human | ai_agent | toolkit | mcp_tool
started_at: datetime
status: success | partial | failed
inputs: object
steps_completed: []
artifacts: []
validation_result: string
rollback_required: boolean
notes: string
```

## 6.8 Critérios de aceite

- Procedure permite execução por humano técnico sem contexto externo excessivo.
- Procedure é segura para agente de codificação.
- Reflex tem gatilho inequívoco.
- Todo passo que escreve no corpus declara artefato de saída.
- Operações destrutivas incluem rollback.

---

# 7. Funcionalidade — Hooks

## 7.1 Propósito

Definir hooks como camada de enforcement determinístico em eventos do ciclo de vida de uma sessão, ferramenta ou operação.

## 7.2 Princípio

Quando uma regra crítica pode ser verificada deterministicamente, ela deve ser implementada como hook, schema, validação ou script — não apenas como instrução textual.

## 7.3 Eventos suportados

| Evento         | Uso                                    |
| -------------- | -------------------------------------- |
| `SessionStart` | carregar contexto mínimo, checar drift |
| `PreToolUse`   | validar permissão antes de ferramenta  |
| `PostToolUse`  | registrar resultado e validar saída    |
| `PreWrite`     | bloquear escrita insegura              |
| `PostWrite`    | validar frontmatter, links e relatório |
| `OnCapture`    | sanitizar e classificar captura        |
| `OnExport`     | validar pacote exportado               |
| `Stop`         | sugerir exec report ou memória         |

## 7.4 Estrutura física

```text
hooks/
├── session-start/
│   └── check-context-and-drift.md
├── pre-write/
│   └── guard-persistent-write.md
├── post-write/
│   └── validate-frontmatter.md
└── on-capture/
    └── sanitize-memory-capture.md
```

## 7.5 Manifesto de hook

```yaml
hook_id: maui-guard-persistent-write
event: PreWrite
status: proposta
severity: blocking | warning | info
applies_to:
  - specs
  - memoria
conditions:
  - write_operation == true
actions:
  - require_explicit_authorization
  - require_dry_run_if_destructive
failure_mode: block
```

## 7.6 Regras de segurança

- Hook blocking deve falhar fechado.
- Hook não deve depender de rede no P0.
- Hook não deve modificar conteúdo sem gerar diff.
- Hook que escreve relatório deve fazê-lo em `validations/` ou `exec-reports/`.
- Hook não deve capturar conteúdo sensível sem sanitização.

## 7.7 Hooks P0

```text
hooks/session-start/check-instance-status.md
hooks/pre-write/guard-corpus-write.md
hooks/post-write/validate-frontmatter.md
hooks/post-write/validate-links.md
hooks/on-export/validate-update-package.md
hooks/on-capture/sanitize-and-classify.md
hooks/stop/suggest-exec-report.md
```

## 7.8 Critérios de aceite

- Cada hook declara evento, severidade e modo de falha.
- Hook blocking tem teste mínimo.
- Hook é mapeável por operator pack.
- Hook não cria política nova; referencia spec existente.

---

# 8. Funcionalidade — Subagentes

## 8.1 Propósito

Definir subagentes como especialistas isolados para tarefas do Maui, reduzindo contexto, melhorando qualidade e evitando mistura de papéis.

## 8.2 Modelos suportados

### 8.2.1 Subagentes nominais

Especialistas pré-definidos, versionados no corpus.

Exemplos:

```text
subagents/maui-doc-reviewer.md
subagents/maui-schema-validator.md
subagents/maui-context-compressor.md
subagents/maui-update-planner.md
subagents/maui-memory-curator.md
```

### 8.2.2 Clones via Task

Delegações temporárias criadas por agente principal. Devem receber escopo limitado, contexto mínimo e contrato de retorno.

## 8.3 Manifesto de subagente

```yaml
agent_id: maui-schema-validator
versao: 0.1
status: proposta
papel_primario: development_engineer
missao: validar schemas e contratos estruturados do Maui
ferramentas_permitidas:
  - filesystem_read
  - validation_scripts
ferramentas_bloqueadas:
  - persistent_write_without_approval
contexto_maximo: limitado
output_contract:
  - findings
  - severity
  - suggested_fix
```

## 8.4 Regras de isolamento

- Subagente recebe apenas contexto necessário.
- Subagente não altera corpus sem autorização explícita.
- Subagente retorna resumo estruturado, não despejo de raciocínio.
- Subagente não redefine arquitetura.
- Conflitos devem voltar ao agente principal.

## 8.5 Subagentes P0

| Subagente                 | Responsabilidade                  |
| ------------------------- | --------------------------------- |
| `maui-doc-reviewer`       | consistência documental e links   |
| `maui-schema-validator`   | schemas, frontmatter e contratos  |
| `maui-context-compressor` | compressão de context packages    |
| `maui-update-planner`     | geração de plano de update        |
| `maui-memory-curator`     | triagem de memória/adendo/insight |
| `maui-security-reviewer`  | riscos de escrita, plugin e MCP   |

## 8.6 Contrato de retorno

```yaml
subagent_id: string
task: string
status: success | partial | failed
findings:
  - severity: low | medium | high | critical
    item: string
    rationale: string
    recommendation: string
artifacts: []
needs_human_decision: boolean
```

## 8.7 Critérios de aceite

- Cada subagente tem escopo único.
- Ferramentas permitidas e bloqueadas estão declaradas.
- Output é estruturado.
- Há regra de escalonamento para decisão humana.

---

# 9. Funcionalidade — Plugins

## 9.1 Propósito

Definir plugins como bundles versionados que empacotam skills, hooks, subagentes, commands, schemas e assets relacionados.

## 9.2 Princípio

Plugin é unidade de distribuição, não unidade de identidade. Plugins externos são não confiáveis até validação.

## 9.3 Estrutura

```text
plugins/nome-do-plugin/
├── plugin.yaml
├── README.md
├── skills/
├── hooks/
├── subagents/
├── commands/
├── schemas/
├── evals/
└── examples/
```

## 9.4 `plugin.yaml`

```yaml
plugin_id: maui-core-essentials
name: Maui Core Essentials
version: 0.1
status: proposta
publisher: axiom-internal
compatibility:
  maui: ">=0.1"
capabilities:
  - skills
  - hooks
  - subagents
permissions:
  filesystem_read: true
  filesystem_write: guarded
  network: false
  mcp_tools: false
install:
  mode: copy | symlink | generated
conflicts: []
dependencies: []
```

## 9.5 Plugins P0

```text
plugins/maui-core-essentials/
plugins/maui-instance-management/
plugins/maui-curation-pack/
plugins/maui-eval-toolkit/
```

## 9.6 Instalação

Fluxo:

```text
1. validar plugin.yaml
2. verificar compatibilidade
3. verificar permissões
4. detectar conflitos
5. dry-run de instalação
6. Human Gate se plugin externo ou permissivo
7. instalar
8. gerar install report
```

## 9.7 Segurança

- Plugin externo exige Human Gate.
- Plugin com escrita exige revisão.
- Plugin com rede é P1/P2, não P0.
- Plugin não pode sobrescrever specs centrais sem pacote de update.
- Plugin deve ser removível.

## 9.8 Critérios de aceite

- Manifesto válido.
- Sem conflito de nomes.
- Dependências resolvidas.
- Permissões explícitas.
- Instalação dry-run disponível.
- Relatório pós-instalação gerado.

---

# 10. Funcionalidade — MCP Servers

## 10.1 Propósito

Definir como Maui expõe capacidades via MCP sem se confundir com um MCP server específico.

## 10.2 Princípio

MCP é protocolo de acesso. Maui é corpus. MCP servers são adapters substituíveis.

## 10.3 Modos

| Modo          | Uso                           | Escrita              |
| ------------- | ----------------------------- | -------------------- |
| read-only     | consulta ao corpus e contexto | não                  |
| validation    | execução de validações        | apenas relatórios    |
| guarded-write | escrita controlada            | sim, com autorização |
| admin         | manutenção avançada           | fora do P0           |

P0 deve priorizar `read-only` e `validation`.

## 10.4 Tools MCP P0

```text
maui.corpus.search
maui.corpus.read
maui.context.export
maui.registry.status
maui.validate.frontmatter
maui.validate.links
maui.update.package.preview
```

## 10.5 Tools MCP P1

```text
maui.memory.capture
maui.update.package.create
maui.registry.register
maui.plugin.install_preview
```

## 10.6 Envelope de resposta

```json
{
  "status": "success",
  "data": {},
  "warnings": [],
  "compliance_signal": {
    "status": "current|minor_drift|major_drift|incompatible|unknown",
    "message": "string"
  },
  "sources": [],
  "next_actions": []
}
```

## 10.7 Segurança

- Sem escrita no P0, exceto relatórios em diretório controlado.
- Autenticação obrigatória para escrita.
- Tool deve declarar escopo e permissões.
- Registro de auditoria obrigatório.
- Rate limit local quando exposto fora do localhost.

## 10.8 Critérios de aceite

- MCP server read-only consegue listar e ler artefatos permitidos.
- Respostas incluem compliance signal quando aplicável.
- Nenhuma tool escreve fora de diretórios autorizados.
- Operator pack declara configuração MCP por target.

---

# 11. Funcionalidade — Operator Packs

## 11.1 Propósito

Definir operator packs como pacotes de adaptação do Maui para ferramentas específicas, preservando a soberania do corpus.

## 11.2 Targets P0/P1

| Prioridade | Target          | Justificativa                       |
| ---------- | --------------- | ----------------------------------- |
| P0         | Claude Code     | filesystem + skills/hooks/subagents |
| P0         | Codex           | filesystem + `AGENTS.md`            |
| P0         | ChatGPT Handoff | operação sem filesystem             |
| P1         | ChatGPT Action  | REST autenticado                    |
| P1         | Gemini          | Gem/context packages                |
| P1         | Cursor          | rules + filesystem                  |
| P2         | Antigravity     | dependente de compatibilidade       |

## 11.3 Estrutura

```text
operator-packs/claude-code/
├── pack.yaml
├── CLAUDE.md.template
├── skills-map.yaml
├── hooks.example.json
├── mcp-config.example.json
└── install.md
```

## 11.4 `pack.yaml`

```yaml
pack_id: maui-claude-code
version: 0.1
target: claude-code
status: proposta
supports:
  filesystem: true
  skills: true
  hooks: true
  subagents: true
  mcp: true
  rest: false
install_mode: symlink_or_copy
requires_human_steps: true
```

## 11.5 Regras por target

### Claude Code

- gerar `CLAUDE.md` via template;
- mapear `skills/` para convenção suportada;
- mapear subagentes quando disponível;
- configurar hooks quando seguro;
- MCP opcional.

### Codex

- gerar `AGENTS.md`;
- usar `.agents/skills/` quando aplicável;
- priorizar instruções compactas;
- scripts P0 via filesystem.

### ChatGPT sem Action

- gerar context package;
- orientar Update Request;
- nunca declarar hash real;
- status default `unknown`.

### ChatGPT com Action

- usar REST autenticado;
- read-only primeiro;
- escrita apenas com Human Gate.

## 11.6 Critérios de aceite

- Pack instala por dry-run.
- Templates são gerados sem edição manual obrigatória quando possível.
- Capacidades e limitações do target estão explícitas.
- Pack não duplica identidade do Maui, apenas adapta.

---

# 12. Funcionalidade — Context Engineering e Context Packages

## 12.1 Propósito

Definir a disciplina de Context Engineering do Maui: escrever, selecionar, compactar e isolar contexto para cada ferramenta, sessão e tarefa.

## 12.2 Modelo operacional

```text
Write   → registrar contexto reutilizável
Select  → escolher o mínimo suficiente
Compress→ reduzir preservando decisões e contratos
Isolate → separar escopo, papel, confidencialidade e target
```

## 12.3 Camadas

| Camada | Conteúdo                                 | Cadência         | Meio                 |
| ------ | ---------------------------------------- | ---------------- | -------------------- |
| A      | identidade, princípios, PKAs, specs base | instanciação     | template/tool config |
| B      | adendos, insights, correções, drift      | início de sessão | MCP/REST/package     |
| C      | memórias e referências relevantes        | sob demanda      | retrieve/package     |

## 12.4 Context package

Estrutura:

```text
context-packages/
├── current/
│   └── maui-bootstrap.md
├── targets/
│   ├── claude-code.md
│   ├── codex.md
│   └── chatgpt-handoff.md
└── generated/
```

## 12.5 Frontmatter de context package

```yaml
titulo: Context Package — Maui Bootstrap
target: chatgpt-handoff
versao: 0.1
status: proposta
validade: 2026-06-30
camadas:
  - A
  - B
fontes:
  - "[[arquitetura-alvo-maui]]"
limites:
  - nao_calcula_hash_real
```

## 12.6 Critérios de seleção

1. Relevância para objetivo.
2. Precedência normativa.
3. Atualidade.
4. Confidencialidade compatível.
5. Orçamento de contexto.
6. Necessidade de execução.

## 12.7 Compressão segura

Preservar sempre:

- decisões;
- contratos;
- riscos;
- Human Gate;
- fronteira corpus/toolkit;
- limitações do target;
- F/I/H quando houver inferência.

Pode remover:

- exemplos redundantes;
- histórico sem decisão;
- explicações duplicadas;
- detalhes de implementação não usados na tarefa.

## 12.8 Critérios de aceite

- Todo package declara target e validade.
- Fontes estão listadas.
- Limitações estão explícitas.
- Não carrega tudo por default.
- É adequado ao modo da ferramenta.

---

# 13. Funcionalidade — Update Protocol

## 13.1 Propósito

Definir o protocolo tool-agnostic de atualização do Maui, baseado em três artefatos: Update Request, Update Package e Update Report.

```text
Update Request → Update Package → Update Report
```

## 13.2 Quando usar

- instância detecta drift;
- instância sem filesystem precisa pedir atualização;
- humano solicita evolução do corpus;
- operator pack precisa ser regenerado;
- specs ou skills mudaram;
- contexto de uma ferramenta está defasado.

## 13.3 Update Request

Arquivo em:

```text
exec-requests/update-YYYYMMDD-NNN.md
```

Conteúdo obrigatório:

```yaml
request_id: update-20260504-001
origin_tool_id: chatgpt_custom_gpt_maui
origin_target: chatgpt-handoff
perceived_version: unknown
perceived_hash: unknown
objective: atualizar instruções da instância
scope:
  - context-package
  - operator-pack
constraints:
  - sem filesystem direto
requested_output:
  - markdown
  - checklist
```

Corpo:

1. contexto;
2. objetivo;
3. estado percebido;
4. restrições;
5. evidências;
6. resultado desejado.

## 13.4 Update Package

Arquivo em:

```text
exports/update-YYYYMMDD-NNN/update-package.md
```

Conteúdo obrigatório:

- resumo;
- arquivos alterados/propostos;
- instruções de aplicação;
- validações executadas;
- riscos;
- rollback;
- critérios de aceite;
- Human Gate quando necessário.

## 13.5 Update Report

Arquivo em:

```text
exec-reports/update-YYYYMMDD-NNN-report.md
```

Conteúdo obrigatório:

```yaml
report_id: update-20260504-001-report
request_id: update-20260504-001
status: success | partial | failed
applied_by: human | ai_agent | toolkit
applied_at: datetime
changed_files: []
validation_results: []
remaining_drift: current | minor_drift | major_drift | incompatible | unknown
```

## 13.6 Fluxo

```text
1. Instância gera Update Request
2. Operador com acesso ao corpus lê request
3. Operador gera Update Package
4. Humano/instância aplica pacote
5. Validações rodam
6. Update Report registra resultado
7. Decisões relevantes viram memória/adendo/insight
```

## 13.7 Regras críticas

- Instância sem filesystem não calcula hash real.
- Instância sem acesso ao corpus declara estado `unknown`.
- Update Package não deve aplicar mudança silenciosa.
- Mudança normativa exige Human Gate.
- Toda atualização aplicada deve gerar report.

## 13.8 Critérios de aceite

- Request é suficiente para operador agir.
- Package é aplicável por humano técnico.
- Report permite auditoria posterior.
- Validações e riscos estão explícitos.

---

# 14. Funcionalidade — Schemas e Contratos Estruturados

## 14.1 Propósito

Definir schemas como contratos estruturados para validar documentos, pacotes, registros e artefatos operacionais do Maui.

## 14.2 Schemas P0

```text
schemas/memory.schema.yaml
schemas/skill.schema.yaml
schemas/procedure.schema.yaml
schemas/script.schema.yaml
schemas/operator-pack.schema.yaml
schemas/registry.schema.yaml
schemas/context-package.schema.yaml
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
schemas/execution-request.schema.yaml
schemas/execution-report.schema.yaml
schemas/plugin.schema.yaml
```

## 14.3 Regras

- Schema descreve estrutura; spec descreve semântica.
- Mudança de schema exige changelog.
- Breaking change exige migração.
- Validação deve poder rodar localmente.
- YAML é preferido para legibilidade; JSON Schema pode coexistir quando necessário.

## 14.4 Campos comuns

```yaml
titulo: string
versao: string
status: string
data_criacao: date
idioma: string
tipo: string
escopo: string
confidencialidade: string
referencias: array
tags: array
```

## 14.5 Severidade de validação

| Severidade | Exemplo                 | Efeito                             |
| ---------- | ----------------------- | ---------------------------------- |
| critical   | schema ilegível         | bloqueia                           |
| high       | falta campo obrigatório | bloqueia release                   |
| medium     | link quebrado           | alerta ou bloqueio conforme escopo |
| low        | tag ausente             | alerta                             |
| info       | sugestão                | não bloqueia                       |

## 14.6 Critérios de aceite

- Schemas P0 existem.
- Há fixtures válidas e inválidas.
- Validador gera saída Markdown e JSON.
- Falhas são classificadas por severidade.

---

# 15. Funcionalidade — Evals

## 15.1 Propósito

Definir evals como testes versionados que verificam comportamento de skills, procedures, scripts, update protocol, context packages e operator packs.

## 15.2 Escopo P0

```text
evals/skills/maui-context-export.eval.yaml
evals/skills/maui-update-export.eval.yaml
evals/scripts/maui-vault-health.eval.yaml
evals/update-protocol/request-package-report.eval.yaml
evals/operator-packs/claude-code-pack.eval.yaml
evals/regression/corpus-integrity.eval.yaml
```

## 15.3 Tipos de eval

| Tipo            | Verifica                                   |
| --------------- | ------------------------------------------ |
| schema eval     | estrutura válida                           |
| behavior eval   | execução produz saída esperada             |
| regression eval | mudança não quebrou contrato               |
| safety eval     | operação perigosa bloqueada                |
| context eval    | pacote contém contexto suficiente e mínimo |

## 15.4 Estrutura

```yaml
eval_id: maui-update-protocol-basic
version: 0.1
target: update-protocol
fixtures:
  - fixtures/update-request-valid.md
assertions:
  - type: contains_section
    value: "Rollback"
  - type: schema_valid
    schema: schemas/update-package.schema.yaml
success_threshold: 1.0
```

## 15.5 Critérios de bloqueio

Falha bloqueia release quando:

- envolve escrita persistente;
- envolve update protocol;
- envolve operator pack P0;
- envolve segurança de filesystem;
- envolve mudança normativa.

## 15.6 Critérios de aceite

- Evals P0 possuem fixtures.
- Evals rodam localmente.
- Resultado é salvo em `validations/`.
- Falha tem severidade e recomendação.

---

# 16. Funcionalidade — Automations

## 16.1 Propósito

Definir automations como cadências programadas ou gatilhadas. Skills definem método; automations definem quando e sob quais condições executar.

## 16.2 Princípio

Automation não deve escrever no corpus sem autorização explícita ou política aprovada. P0 deve ser read-only ou gerar recomendações.

## 16.3 Estrutura

```text
automations/
├── daily-vault-health.yaml
├── weekly-memory-index.yaml
├── weekly-drift-check.yaml
└── monthly-insight-review.yaml
```

## 16.4 Manifesto

```yaml
automation_id: weekly-drift-check
schedule: weekly
status: proposta
operation: maui_registry_check
mode: read-only
outputs:
  - validations/weekly-drift-check.md
requires_human_gate: false
```

## 16.5 Automations P0

| Automation              | Cadência      | Escrita              |
| ----------------------- | ------------- | -------------------- |
| vault health            | semanal       | relatório            |
| memory index check      | semanal       | índice reconstruível |
| drift check             | semanal       | relatório            |
| broken links check      | semanal       | relatório            |
| pending update requests | diária/manual | relatório            |

## 16.6 Automations proibidas no P0

- aplicar update automaticamente;
- instalar plugin externo;
- promover adendo;
- apagar memória;
- publicar via rede;
- escrever em specs normativas.

## 16.7 Critérios de aceite

- Toda automation declara cadência, modo e saída.
- Read-only por default.
- Escrita persistente exige Human Gate.
- Gera relatório rastreável.

---

# 17. Funcionalidade — Capture Layer, Memory e Insight Pipeline

## 17.1 Propósito

Definir como Maui captura material valioso, compacta, sanitiza e persiste no corpus como memória, insight ou candidato a adendo.

## 17.2 Princípios

1. Captura seletiva por design.
2. Compactação antes de persistência.
3. Sanitização antes de gravação.
4. Confidencialidade explícita.
5. Material bruto não é memória final.
6. Falha segura: descartar é melhor que capturar mal.

## 17.3 Critérios de captura

Capturar quando houver:

- comando explícito;
- decisão registrável;
- artefato reutilizável;
- preferência declarada;
- aprendizado operacional;
- resultado de execução relevante;
- alta densidade informacional.

## 17.4 Estrutura de memória

```text
memorias/YYYY/MM/YYYY-MM-DD-slug.md
```

Frontmatter:

```yaml
memory_id: mem-20260504-001
titulo: string
data: 2026-05-04
origem: chatgpt | claude-code | codex | human
escopo: projeto_maui
confidencialidade: interna
tipo: decisao | sessao | execucao | preferencia | artefato
relacionados: []
tags: []
```

## 17.5 Pipeline

```text
material bruto
→ seleção
→ compactação
→ sanitização
→ classificação
→ memória
→ padrão recorrente
→ insight
→ candidato a adendo
→ Human Gate
```

## 17.6 O que não capturar

- conversa bruta integral;
- segredo, token ou credencial;
- dado pessoal desnecessário;
- conteúdo fora do escopo;
- hipótese fraca como decisão;
- material que viole política externa.

## 17.7 Critérios de aceite

- Memória tem escopo e confidencialidade.
- Decisões estão separadas de hipóteses.
- Fonte e data estão preservadas.
- Conteúdo bruto sensível foi removido.
- Próximos passos, quando houver, são claros.

---

# 18. Funcionalidade — Painel de Curadoria

## 18.1 Propósito

Definir o painel de curadoria como ferramenta auxiliar para agrupar instâncias, distribuir tarefas, coletar reports, comparar respostas e registrar decisões humanas.

## 18.2 Fronteira

Painel não é Maui. Painel é operador auxiliar sobre o corpus.

## 18.3 MVS file-based/CLI

Estrutura:

```text
panel/
├── inbox/
├── assigned/
├── reports/
├── decisions/
├── dashboard.md
└── panel-state.yaml
```

## 18.4 Funcionalidades P0

- listar exec requests pendentes;
- atribuir request a operador;
- coletar exec reports;
- registrar decisão humana;
- gerar dashboard Markdown;
- sinalizar bloqueios.

## 18.5 Comandos conceituais

```bash
maui panel status
maui panel dispatch --request exec-requests/001.md --operator claude-code
maui panel collect --from exec-reports/
maui panel record-decision --title "Aprovar arquitetura Maui"
```

## 18.6 Estado mínimo

```yaml
requests_open: 3
requests_assigned: 2
reports_pending_review: 1
decisions_pending: 1
last_update: 2026-05-04T00:00:00Z
```

## 18.7 Critérios de aceite

- Painel funciona sem UI.
- Estado é legível por humano.
- Decisões são registradas separadamente de reports.
- Não executa alterações normativas sozinho.

---

# 19. Funcionalidade — Governança, Segurança e Human Gate

## 19.1 Propósito

Definir regras transversais de governança, segurança, privacidade, Human Gate e controle de mudança para todas as funcionalidades Maui.

## 19.2 Precedência preservada

Até decisão formal em contrário, Maui preserva a precedência do Saara v7.1.1:

1. políticas externas, lei e compliance;
2. system prompt ativo;
3. princípios fundacionais;
4. especificação completa;
5. PKAs e specs técnicas;
6. parametrização executável;
7. conteúdo recuperado;
8. pedido do usuário.

## 19.3 Human Gate obrigatório

Exige aprovação humana:

- adoção formal do Maui;
- mudança em princípios;
- promoção de adendo;
- mudança normativa;
- instalação de plugin externo;
- escrita persistente por MCP/REST;
- automation com escrita;
- operação destrutiva;
- exposição de endpoint com acesso ao corpus.

## 19.4 Política de escrita

| Operação       | Default    | Condição para permitir       |
| -------------- | ---------- | ---------------------------- |
| leitura        | permitido  | escopo válido                |
| relatório      | permitido  | diretório controlado         |
| memória        | controlado | captura válida + sanitização |
| spec           | bloqueado  | Human Gate                   |
| adendo ativo   | bloqueado  | Human Gate                   |
| plugin externo | bloqueado  | validação + Human Gate       |
| delete         | bloqueado  | backup + Human Gate          |

## 19.5 Privacidade

- minimização de dados;
- confidencialidade explícita;
- separação por escopo;
- sanitização antes de persistir;
- não armazenar segredo;
- não enviar conteúdo restrito para ferramenta sem autorização.

## 19.6 Drift e conformidade

Estados:

```text
current
minor_drift
major_drift
incompatible
unknown
```

Regra: `unknown` é preferível a falsa conformidade.

## 19.7 F/I/H

Usar F/I/H quando houver mistura material entre:

- fato documentado;
- inferência arquitetural;
- hipótese de implementação.

## 19.8 Critérios de aceite

- Toda spec funcional referencia esta governança.
- Operações de escrita têm controle.
- Riscos altos têm mitigação.
- Drift não é mascarado.
- Decisão humana é registrada.

---

# 19A. Decisões de adequação documental Saara → Maui

## 19A.1 Propósito

Registrar as decisões de governança já tomadas sobre como os documentos e estruturas atuais do Saara serão adequados para servir ao Maui, eliminando ambiguidades da fase de evolução.

## 19A.2 Decisões fechadas

| Tema | Decisão |
|---|---|
| Diretório final | O Maui viverá em `vault-maui/`. Não será uma camada dentro de `vault-saara/`. |
| Coexistência técnica | `.maui/` e `.saara/` devem coexistir durante a evolução. |
| Escopo dos adendos Maui | Adendos Maui servirão apenas ao Maui. Não serão aplicados ao Saara v7.1.1. |
| Versionamento | Maui iniciará como `Maui v1.0`. Saara manterá controle de versão separado. |
| `hash_config` | O hash de conformidade do Maui deve incluir todo o corpus: normativos, manifestos, scripts, skills, procedures, hooks, subagents, plugins, schemas, evals, automations, operator packs, context packages e demais artefatos versionados relevantes. |

## 19A.3 Implicações arquiteturais

### 19A.3.1 `vault-maui/` como raiz canônica

Todo artefato Maui deve ser organizado sob `vault-maui/`. O Saara pode continuar existindo em estrutura própria, mas não será a raiz do Maui.

Implicações:

- documentos herdados do Saara devem ser copiados, adaptados ou derivados para `vault-maui/`;
- referências internas devem ser revisadas para apontar para documentos Maui quando o contexto for Maui;
- documentos Saara preservados como fonte histórica devem ser marcados como origem, não como runtime Maui ativo, salvo decisão explícita.

### 19A.3.2 Coexistência de `.maui/` e `.saara/`

As pastas técnicas `.maui/` e `.saara/` devem coexistir para preservar rastreabilidade e permitir migração segura.

Regra:

```text
.saara/ = estado técnico e índices relacionados ao Saara
.maui/  = estado técnico e índices relacionados ao Maui
```

Não deve haver escrita cruzada silenciosa entre `.saara/` e `.maui/`.

### 19A.3.3 Adendos separados

Adendos Maui não devem alterar o comportamento do Saara v7.1.1. Eles pertencem ao ciclo de evolução do Maui.

Regra:

```text
adendos Saara → aplicam-se ao Saara
adendos Maui  → aplicam-se apenas ao Maui
```

Se um aprendizado Maui também for útil ao Saara, ele deve ser proposto separadamente como adendo Saara, com Human Gate próprio.

### 19A.3.4 Versionamento independente

Maui inicia em `v1.0`. Saara mantém versionamento separado.

Implicações:

- Maui não deve ser tratado como `Saara v7.2`;
- documentos Maui devem usar `versao: 1.0` quando forem promovidos a base inicial ativa;
- documentos ainda em desenho podem manter `versao: 0.x` e `status: proposta` até consolidação;
- referências a Saara v7.1.1 devem aparecer como origem/herança, não como versão do Maui.

### 19A.3.5 `hash_config` abrangente

O `hash_config` do Maui deve cobrir todos os artefatos versionados que influenciam identidade, comportamento, operação, validação ou distribuição.

Deve incluir, no mínimo:

```text
00_core/
01_manifest/
memorias/                # conforme política de hash por camada
adendos/
insights/
skills/
procedures/
reflexes/
scripts/
hooks/
subagents/
plugins/
schemas/
evals/
automations/
operator-packs/
mcp-servers/
context-packages/
exec-requests/           # quando fizerem parte de estado de execução versionado
exec-reports/            # quando fizerem parte de estado de execução versionado
exports/                 # apenas manifests/pacotes versionados, não builds temporários
```

Política recomendada:

- `hash_config_core`: identidade e governança base;
- `hash_operational`: capacidades executáveis e operadores;
- `hash_context`: context packages e materiais de instanciação;
- `hash_full`: composição total relevante do corpus Maui.

## 19A.4 Matriz de adequação documental

| Documento/estrutura atual do Saara | Ação para Maui |
|---|---|
| `principios-fundacionais.md` | copiar para `vault-maui/00_core/` e adaptar para Maui v1.0 preservando herança Saara |
| `system-prompt.md` | copiar como base histórica/runtime inicial e criar versão Maui proposta |
| `especificacao-completa.md` | copiar como referência de herança e derivar especificação completa Maui v1.0 |
| `pka-*.md` | copiar/adaptar para Maui, mantendo domínio; adendos Maui ficam separados |
| `spec-distribuicao.md` | adaptar para operator packs, context packages, MCP e handoff |
| `spec-instanciacao-conformidade.md` | adaptar para registry Maui e hash abrangente |
| `spec-context-injection.md` | evoluir para Context Engineering Maui |
| `spec-capture-layer.md` | adaptar para Capture/Memory Maui com hooks e procedures |
| `spec-memory-store.md` | adaptar para `.maui/`, mantendo `.saara/` coexistente |
| `spec-adendos.md` | adaptar para adendos exclusivos Maui |
| `spec-parametrizacao.json` | criar parametrização Maui separada, sem substituir Saara |
| `.saara/` | preservar para Saara; não usar como estado Maui |
| `.maui/` | criar para estado técnico Maui |
| roadmaps/handoffs Saara | migrar seletivamente para `01_manifest/`, `memorias/` ou `exec-reports/` conforme função |

## 19A.5 Critérios de aceite da adequação documental

- `vault-maui/` existe como raiz canônica.
- `.saara/` e `.maui/` coexistem sem escrita cruzada silenciosa.
- Adendos Maui não alteram Saara v7.1.1.
- Maui tem versionamento próprio iniciado em `v1.0`.
- `hash_config` Maui inclui todo o corpus relevante, não apenas `00_core/`.
- Documentos herdados do Saara indicam claramente se são referência histórica, base adaptada ou documento ativo Maui.
- Qualquer reaproveitamento de aprendizado Maui no Saara exige proposta separada e Human Gate próprio.

---

# 20. Estrutura física alvo

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
├── panel/                        # Curadoria file-based/CLI
└── exports/                      # Update packages e artefatos gerados
```

---

# 21. Roadmap incremental

## 21.1 Fase 0 — Formalização

- Salvar este documento em `01_manifest/spec-funcionalidades-maui.md`.
- Salvar arquitetura alvo em `01_manifest/arquitetura-alvo-maui.md`.
- Registrar decisão Saara → Maui como memória.
- Definir status oficial: proposta, piloto ou adoção.
- Criar changelog e owner.

## 21.2 Fase 1 — Estrutura mínima

- Criar árvore `vault-maui/`.
- Criar schemas mínimos.
- Criar scripts P0.
- Criar con
