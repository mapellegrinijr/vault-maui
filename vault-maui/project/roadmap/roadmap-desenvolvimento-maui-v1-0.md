---
titulo: "Roadmap de Desenvolvimento — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: roadmap
escopo: projeto_maui
---

# Roadmap de Desenvolvimento — Maui

## Nota de reconciliação de status

> Reconciliação atualizada em 2026-05-06, após P0.1.21.
>
> Este roadmap permanece em `status: proposta` e deve ser usado como mapa de destino, critérios e referência estrutural. Ele não deve ser usado como fonte única de status executado.
>
> O estado executado deve ser confirmado preferencialmente por Git, `status-project/`, exec-reports, inventários, project-memories e handoffs recentes. A atualização abaixo corrige a defasagem da nota anterior, que registrava evidências apenas até P0.1.13.

## Estado operacional reconciliado em 2026-05-06

Fontes de execução preferenciais: Git local, `vault-maui/status-project/STATUS-UPDATE-maui.md`, `vault-maui/exec-reports/submitted/`, `vault-maui/inventarios/`, `vault-maui/project-memories/` e `vault-maui/handoffs/`. O readiness P0.1.21 formaliza essa precedência em `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md`.

Etapas com evidência direta até esta reconciliação:

| Etapa | Estado reconciliado | Evidência resumida |
| --- | --- | --- |
| Tarefa 2 / saneamento inicial de `Documentação/` | concluída | Inventário `vault-maui/inventarios/2026-05-04-documentacao.md` e exec-report P0.1.16 registram os 8 destinos finais e nenhuma pendência esperada em `Documentação/`. |
| P0.1.16 | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-16-fechamento-tarefa-2-documentacao.md`; commit `31c63e90f4c330d500701c79daf409155e24fe47`. |
| P0.1.17 | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-17-diagnostico-estrutural.md`; commit `7de2211122aa709e484e232a4ff4af18afd99f32`. |
| P0.1.18 | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-18-normalizacao-memorias.md`; commit `ccf9efce4cea1261959c83beaf4c62836dce5266`. |
| P0.1.19 | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-19-normalizacao-referencias-wikilinks.md`; commit `e554136d14f0bbcaec7e41a9e2096a7e24684e94`. |
| P0.1.20 | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-20-normalizacao-frontmatter-slugs.md`; commit `86756e18bf90d13b9036963fb7eecaf86603abc6`. |
| P0.1.20-pre | concluída | `vault-maui/exec-reports/submitted/2026-05-05-p0-1-20-pre-context-brief-pos-normalizacao.md`; commit `0dc40fb3195f33092d9c9780937555804ac21e6b`. |
| P0.1.21 | concluída | `vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md` e `vault-maui/exec-reports/submitted/2026-05-06-p0-1-21-context-brief-readiness.md`; commit `03dab3d5258f433fd47b667a2a1531ec4a907798`. |
| P0.1.26 | concluída | `vault-maui/00_core/principios-fundacionais-maui.md` e `vault-maui/00_core/contrato-precedencia-maui.md`; commit `1f32776`. |
| P0.1.27 | concluída | `vault-maui/00_core/especificacao-completa-maui.md`; commit `221d481`. |
| P0.1.28 | concluída | `vault-maui/00_core/system-prompt-maui.md`; commit `4493448`. |
| P0.1.29 | concluída | 6 PKAs em `vault-maui/00_core/pka-*.md` (PE Elite obrigatória + 5 adaptadas); commit `4c06623`. |
| P0.1.30 | concluída | 6 specs subsidiárias em `vault-maui/00_core/spec-*-maui.md`; commit `b8c8749`. |
| P0.1.31 | concluída | `vault-maui/00_core/spec-parametrizacao-maui.md`, `vault-maui/01_manifest/spec-parametrizacao-maui.json`, `vault-maui/00_core/indice-maui.md`; commit `9f2afc9`. |
| P0.1.32 | concluída | Revisão integrada — 7 correções (A1 B1-B5 C1) em 5 normativos + exec-report + memória marco; commit `538b441`. **Configuração-base Maui concluída em 2026-05-06.** |
| H0.x | concluída | Separação Project vs Runtime: `project-memories/`, `status-project/`, `memorias/` runtime, `status/` runtime e roadmap em `project/roadmap/`; commits `f8b5120` e `9c76d62`. |

Ressalvas operacionais:

- P0.1.11 permanece não executada; não assumir instrução equivalente para Claude Code sem evidência posterior.
- `vault-maui/project-memories/` guarda memória de projeto/gestação; `vault-maui/memorias/` fica reservado para memória operacional de runtime.
- `vault-maui/status-project/STATUS-UPDATE-maui.md` é a fonte viva de status do projeto; `vault-maui/status/` fica reservado para status operacional de runtime.
- Este roadmap vive em `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`.
- `Documentação/` não possui pendências esperadas dos 8 arquivos inventariados e não deve ser reaberta sem decisão humana explícita.
- Instanciação manual Maui ainda não está pronta e permanece fora do escopo desta reconciliação.
- Uma memória antiga pode conter trecho defasado tratando P0.1.20 como próximo passo; conferir exec-reports P0.1.20, P0.1.20-pre e P0.1.21 antes de declarar estado atual.
- `vault-maui/review-reports/` não existe; há `vault-maui/exec-reports/reviewed/`, ainda sem uso como fonte principal.
- ChatGPT/Handoff sem filesystem, hash ou commit verificável deve declarar conformidade como `unknown`, nunca `current`.

## Planejamento P0.1.24-pre — Configuração-base Maui

P0.1.24-pre registra uma frente explícita de **Configuração-base Maui** antes da P0.1.24. Esta frente atualiza o mapa de execução, mas não cria nem adapta arquivos de configuração-base.

Sequência planejada:

| Etapa | Papel | Limite |
| --- | --- | --- |
| P0.1.24-pre | Planejar a frente de Configuração-base Maui no roadmap e registrar decisão de Prompt Engineering Elite | Não cria configuração-base. |
| P0.1.24 | Diagnosticar a configuração-base Maui necessária e lacunas atuais | Não implementa arquivos finais. |
| P0.1.25 | Planejar implementação da configuração-base Maui, se aprovado | Ainda depende de decisão humana para execução posterior. |

Escopo mínimo da Configuração-base Maui:

- system prompt Maui;
- especificação completa Maui;
- princípios fundacionais Maui ou decisão explícita de herança/adaptação dos princípios Saara;
- PKAs Maui, incluindo obrigatoriamente **Prompt Engineering Elite**;
- specs subsidiárias Maui;
- parametrização executável Maui;
- índice core Maui;
- contrato de precedência;
- relação de dependência com operator packs P0.3 e context packages P0.4.

Prompt Engineering Elite é PKA/competência obrigatória de primeira classe no Maui. Ela responde por prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection. Agent Engineering continua responsável por agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout. Em tarefas híbridas, Prompt Engineering lidera o contrato textual/instrucional; Agent Engineering lidera integração sistêmica e operacional.

De/para conceitual Saara → Maui, para diagnóstico futuro:

| Saara / origem conceitual | Maui planejado | Observação |
| --- | --- | --- |
| `system-prompt.md` | `system-prompt-maui.md` | A criar/adaptar só após diagnóstico e plano. |
| `especificacao-completa.md` | `especificacao-completa-maui.md` | Deve consolidar identidade e comportamento Maui. |
| `principios-fundacionais.md` | princípios Maui ou decisão de herança/adaptação | Exige decisão explícita de precedência. |
| `pka-agent-engineering.md` | PKA Agent Engineering Maui | Mantém fronteira operacional/sistêmica. |
| `pka-prompt-engineering.md` | PKA Prompt Engineering Maui obrigatória | Inclui Prompt Engineering Elite como domínio de primeira classe. |
| demais `pka-*.md` relevantes | PKAs Maui adaptadas | Diagnóstico deve decidir herança, adaptação ou exclusão. |
| specs subsidiárias Saara | specs subsidiárias Maui | Não copiar integralmente sem curadoria. |
| `spec-parametrizacao.md` / `spec-parametrizacao.json` | parametrização Maui | Deve ser separada da parametrização Saara. |
| `indice.md` | índice core Maui | Deve apontar precedência e artefatos core. |
| `CLAUDE.md`, `AGENTS.md`, Custom GPT instructions | operator packs P0.3 | Dependem da configuração-base; não criar nesta etapa. |
| bootstrap / context packages | context packages P0.4 | Dependem da configuração-base; não criar bootstrap final nesta etapa. |

Limites desta frente: não criar `system-prompt-maui.md`, `especificacao-completa-maui.md`, PKAs, specs subsidiárias, parametrização Maui, operator packs, context packages ou bootstrap final; não executar P0.1.24 nesta etapa.

## 1. Objetivo

Definir o roadmap de desenvolvimento do Maui v1.0, quebrado por funcionalidade e por atividades dentro de cada funcionalidade, com foco em iniciar o uso do Maui com segurança, governança e rastreabilidade.

Este roadmap segue a priorização definida para o **mínimo Maui utilizável com segurança**:

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

## 2. Princípios de execução

1. **Corpus primeiro:** toda decisão estrutural deve ser registrada em `vault-maui/` antes de virar automação.
2. **Contrato antes de código:** schemas e contracts vêm antes dos scripts complexos.
3. **Read-only antes de write:** validar e exportar antes de alterar.
4. **Filesystem antes de rede:** P0 não depende de MCP, REST ou UI.
5. **Handoff antes de integração profunda:** ChatGPT sem filesystem opera por context package e Update Request.
6. **Humano no gate:** mudanças normativas, adendos, plugins externos e escrita persistente exigem Human Gate.
7. **Saara e Maui separados:** `vault-maui/`, `.maui/`, adendos e versionamento Maui são independentes do Saara.
8. **Hash abrangente:** conformidade Maui considera todo o corpus relevante, não apenas `00_core/`.

## 3. Marcos executivos

| Marco | Nome                    | Resultado esperado                                      |
| ----- | ----------------------- | ------------------------------------------------------- |
| M0    | Fundação documental     | `vault-maui/` estruturado e documentos-base salvos      |
| M1    | Contratos mínimos       | schemas e validações manuais/automatizáveis definidos   |
| M2    | Primeira execução local | scripts P0 de validação e exportação funcionando        |
| M3    | Primeira instanciação   | Claude Code/Codex/ChatGPT Handoff operáveis             |
| M4    | Ciclo de atualização    | Update Request/Package/Report funcionando               |
| M5    | Operação assistida      | skills, procedures e smoke tests mínimos disponíveis    |
| M6    | Piloto controlado       | primeiro uso real com registro de decisão e exec report |
| M7    | Expansão P1             | hooks, subagentes, painel CLI e MCP read-only           |
| M8    | Expansão P2             | plugins, automations, guarded-write, REST/Action e UI   |

---

## 3.1 Housekeeping concluído — Project vs Runtime

| Etapa | Estado | Evidência | Resultado |
| --- | --- | --- | --- |
| H0.x — Separação Project vs Runtime | concluída | commits `f8b5120` e `9c76d62`; exec-reports de 2026-05-10 | `project-memories/` para memória de projeto; `status-project/` para status vivo do projeto; `memorias/` e `status/` reservados para runtime; roadmap movido para `project/roadmap/`. |

Esta etapa é housekeeping estrutural e não executa P0.2, P0.3, P0.4 nem qualquer lote do roadmap.

---

# 4. P0.0 — Formalização do corpus e estrutura mínima

## 4.1 Funcionalidade: Maui Corpus

### Objetivo

Criar a raiz canônica `vault-maui/` e estabelecer o corpus como produto principal.

### Atividades

1. Criar diretório raiz `vault-maui/`.
2. Criar árvore mínima de diretórios P0.
3. Salvar arquitetura alvo em `01_manifest/arquitetura-alvo-maui.md`.
4. Salvar spec unificada em `01_manifest/spec-funcionalidades-maui.md`.
5. Criar `01_manifest/definicao-produto-maui.md`.
6. Criar este roadmap em `01_manifest/roadmap-desenvolvimento-maui.md`.
7. Definir `status: proposta` ou `status: piloto` nos documentos iniciais.
8. Registrar decisão de separação Saara/Maui.
9. Definir convenção de frontmatter comum.
10. Definir convenção de links internos e nomes de arquivos.

### Entregáveis

```text
vault-maui/
01_manifest/arquitetura-alvo-maui.md
01_manifest/spec-funcionalidades-maui.md
01_manifest/definicao-produto-maui.md
01_manifest/roadmap-desenvolvimento-maui.md
```

### Dependências

Nenhuma dependência técnica. Depende apenas de decisão humana já registrada.

### Critérios de pronto

- `vault-maui/` existe.
- A estrutura mínima está criada.
- Os documentos-base estão salvos.
- A fronteira corpus/toolkit está explícita.
- Não há uso de `vault-saara/` como raiz Maui.

## 4.2 Funcionalidade: Coexistência `.saara/` e `.maui/`

### Objetivo

Separar estado técnico do Saara e estado técnico do Maui sem escrita cruzada silenciosa.

### Atividades

1. Criar `.maui/` dentro ou ao lado da raiz operacional definida.
2. Manter `.saara/` preservado para estado técnico do Saara.
3. Definir política: `.saara/` não é estado Maui.
4. Criar placeholder `.maui/README.md` explicando finalidade.
5. Criar `.maui/instances/` ou `.maui/registry/` como estrutura futura.
6. Criar `.maui/logs/` para logs técnicos.
7. Criar `.maui/cache/` para índices reconstruíveis.
8. Documentar que índices são reconstruíveis, não fonte de verdade.

### Entregáveis

```text
.maui/README.md
.maui/logs/
.maui/cache/
.maui/registry/
```

### Critérios de pronto

- `.maui/` existe.
- `.saara/` não foi removido.
- Documentação deixa claro que não há escrita cruzada silenciosa.

---

# 5. P0.1 — Schemas mínimos e validação local

## 5.1 Funcionalidade: Schema comum de frontmatter

### Objetivo

Criar contrato mínimo comum para documentos Maui.

### Atividades

1. Definir campos obrigatórios comuns.
2. Definir valores permitidos para `status`.
3. Definir valores permitidos para `confidencialidade`.
4. Definir padrão de `versao` para Maui v1.0.
5. Definir campos opcionais recomendados: `owner`, `substitui`, `substituido_por`, `changelog`.
6. Criar fixture válida.
7. Criar fixture inválida.
8. Definir severidade de falhas.

### Entregáveis

```text
schemas/common-frontmatter.schema.yaml
schemas/fixtures/common-frontmatter.valid.md
schemas/fixtures/common-frontmatter.invalid.md
```

### Critérios de pronto

- Schema cobre campos mínimos.
- Fixtures existem.
- Falhas de campo obrigatório são `high` ou `critical`.

## 5.2 Funcionalidade: Schemas de registry e conformidade

### Objetivo

Definir estrutura para registrar instâncias Maui e calcular conformidade.

### Atividades

1. Definir `tool_id`.
2. Definir `target`.
3. Definir `instantiated_version`.
4. Definir `instantiated_hash`.
5. Definir estados: `current`, `minor_drift`, `major_drift`, `incompatible`, `unknown`.
6. Definir campos de operator pack.
7. Definir campos de last check.
8. Criar fixture de instância com hash conhecido.
9. Criar fixture de ChatGPT Handoff com `unknown`.

### Entregáveis

```text
schemas/registry.schema.yaml
schemas/fixtures/registry.valid.yaml
schemas/fixtures/registry-chatgpt-unknown.valid.yaml
```

### Critérios de pronto

- `unknown` é estado válido.
- Instâncias sem filesystem não podem ser marcadas como `current` sem evidência.

## 5.3 Funcionalidade: Schemas de context package

### Objetivo

Definir contrato para pacotes de contexto por target.

### Atividades

1. Definir campos: `target`, `validade`, `camadas`, `fontes`, `limites`.
2. Definir targets P0: `claude-code`, `codex`, `chatgpt-handoff`.
3. Definir exigência de fontes.
4. Definir exigência de limitações quando target não tem filesystem.
5. Criar fixture válida para ChatGPT Handoff.

### Entregáveis

```text
schemas/context-package.schema.yaml
schemas/fixtures/context-package-chatgpt.valid.md
```

### Critérios de pronto

- Context package sem target falha.
- Context package sem limites para ChatGPT Handoff falha ou alerta alto.

## 5.4 Funcionalidade: Schemas de Update Protocol

### Objetivo

Definir contratos para Update Request, Update Package e Update Report.

### Atividades

1. Criar schema de Update Request.
2. Criar schema de Update Package.
3. Criar schema de Update Report.
4. Definir campos obrigatórios.
5. Definir relação entre `request_id` e `report_id`.
6. Definir estados de execução.
7. Criar exemplos válidos.
8. Criar exemplos inválidos.

### Entregáveis

```text
schemas/update-request.schema.yaml
schemas/update-package.schema.yaml
schemas/update-report.schema.yaml
schemas/fixtures/update-request.valid.md
schemas/fixtures/update-package.valid.md
schemas/fixtures/update-report.valid.md
```

### Critérios de pronto

- Os três artefatos são validáveis.
- Mudança normativa exige campo de Human Gate.

## 5.5 Funcionalidade: Schemas de skill e operator pack

### Objetivo

Permitir criação segura de skills e operator packs P0.

### Atividades

1. Criar `skill.schema.yaml`.
2. Criar `operator-pack.schema.yaml`.
3. Definir ferramentas permitidas/bloqueadas.
4. Definir `quando_usar` e `quando_nao_usar` como obrigatórios para skills.
5. Definir capacidades suportadas por target em operator pack.
6. Criar fixtures válidas.

### Entregáveis

```text
schemas/skill.schema.yaml
schemas/operator-pack.schema.yaml
schemas/fixtures/skill.valid.md
schemas/fixtures/operator-pack.valid.yaml
```

### Critérios de pronto

- Skill sem critérios de sucesso falha.
- Operator pack sem limitações por target falha.

---

# 6. P0.2 — Scripts P0 de bootstrap, validação e contexto

## 6.1 Funcionalidade: `maui_vault_health.py`

### Objetivo

Validar a integridade mínima do corpus Maui.

### Atividades

1. Definir interface CLI.
2. Implementar `--help`.
3. Implementar `--dry-run`.
4. Verificar existência da árvore mínima.
5. Verificar presença dos documentos-base.
6. Verificar presença de schemas P0.
7. Gerar relatório Markdown.
8. Gerar relatório JSON.
9. Classificar falhas por severidade.
10. Salvar relatório em `validations/` quando `--write-report` for usado.

### Entregáveis

```text
scripts/maui_vault_health.py
validations/examples/vault-health-example.md
validations/examples/vault-health-example.json
```

### Critérios de pronto

- Roda sem dependências pesadas.
- Não escreve fora de `validations/`.
- Falha se `vault-maui/` não existir.
- Saída JSON é parseável.

## 6.2 Funcionalidade: `maui_validate_frontmatter.py`

### Objetivo

Validar frontmatter dos documentos Maui.

### Atividades

1. Ler arquivos Markdown.
2. Extrair frontmatter YAML.
3. Validar campos obrigatórios.
4. Validar status permitido.
5. Validar confidencialidade.
6. Gerar lista de falhas.
7. Suportar escopo por diretório.
8. Suportar saída Markdown/JSON.

### Entregáveis

```text
scripts/maui_validate_frontmatter.py
validations/examples/frontmatter-validation-example.md
```

### Critérios de pronto

- Arquivo sem frontmatter é reportado.
- Documento normativo sem `precedencia` é falha alta.

## 6.3 Funcionalidade: `maui_validate_links.py`

### Objetivo

Detectar links internos quebrados e referências ausentes.

### Atividades

1. Localizar links `[[...]]`.
2. Localizar caminhos relativos relevantes.
3. Resolver aliases quando possível.
4. Reportar links quebrados.
5. Classificar severidade.
6. Gerar relatório.

### Entregáveis

```text
scripts/maui_validate_links.py
validations/examples/link-validation-example.md
```

### Critérios de pronto

- Links inexistentes são detectados.
- Links externos não bloqueiam P0, apenas alertam quando necessário.

## 6.4 Funcionalidade: `maui_context_export.py`

### Objetivo

Gerar context packages por target.

### Atividades

1. Definir input `--target`.
2. Definir input `--scope`.
3. Implementar export para `chatgpt-handoff`.
4. Implementar export para `claude-code`.
5. Implementar export para `codex`.
6. Incluir fontes e limites no output.
7. Evitar carregar todo o corpus por default.
8. Gerar manifest JSON.

### Entregáveis

```text
scripts/maui_context_export.py
context-packages/generated/chatgpt-bootstrap.md
context-packages/generated/claude-code-bootstrap.md
context-packages/generated/codex-bootstrap.md
```

### Critérios de pronto

- ChatGPT Handoff declara `unknown` para hash.
- Export inclui fontes.
- Export inclui limites.

## 6.5 Funcionalidade: `maui_registry.py`

### Objetivo

Registrar e consultar instâncias Maui.

### Atividades

1. Implementar comando `list`.
2. Implementar comando `register`.
3. Implementar comando `check`.
4. Suportar `unknown`.
5. Salvar snapshot legível.
6. Evitar dependência obrigatória de banco no P0.
7. Gerar saída Markdown/JSON.

### Entregáveis

```text
scripts/maui_registry.py
.maui/registry/instances-snapshot.json
```

### Critérios de pronto

- Registra Claude Code.
- Registra Codex.
- Registra ChatGPT Handoff como `unknown`.

## 6.6 Funcionalidade: `maui_update_export.py`

### Objetivo

Gerar Update Package a partir de Update Request.

### Atividades

1. Ler Update Request.
2. Validar schema.
3. Gerar pacote Markdown.
4. Gerar manifest YAML.
5. Incluir riscos.
6. Incluir rollback.
7. Incluir Human Gate quando aplicável.
8. Suportar `--dry-run`.

### Entregáveis

```text
scripts/maui_update_export.py
exports/examples/update-package-example.md
exports/examples/manifest.yaml
```

### Critérios de pronto

- Request inválido não gera package.
- Mudança normativa marca Human Gate.

## 6.7 Funcionalidade: `maui_memory_index.py`

### Objetivo

Indexar memórias Markdown como índice reconstruível, distinguindo memória de projeto (`project-memories/`) e memória operacional de runtime (`memorias/`, reservada enquanto o Maui não opera).

### Atividades

1. Listar arquivos em `project-memories/` para histórico de projeto.
2. Validar que `memorias/` permanece reservado para runtime quando não houver operação Maui ativa.
3. Validar frontmatter mínimo.
4. Gerar índice JSON.
5. Detectar possíveis duplicidades por título/data/tags.
6. Não tratar índice como fonte de verdade.

### Entregáveis

```text
scripts/maui_memory_index.py
.maui/cache/memory-index.json
```

### Critérios de pronto

- Índice é reconstruível.
- Memória sem confidencialidade gera alerta.

---

# 7. P0.3 — Operator packs iniciais

## 7.1 Funcionalidade: Operator Pack Claude Code

### Objetivo

Permitir operação inicial do Maui em Claude Code com filesystem.

### Atividades

1. Criar diretório `operator-packs/claude-code/`.
2. Criar `pack.yaml`.
3. Criar `CLAUDE.md.template`.
4. Criar `install.md`.
5. Criar `skills-map.yaml`.
6. Declarar suporte a filesystem.
7. Declarar suporte futuro a skills/hooks/subagentes.
8. Declarar limitações.
9. Incluir instrução de não tratar runtime como identidade.
10. Incluir instrução para gerar exec report.

### Entregáveis

```text
operator-packs/claude-code/pack.yaml
operator-packs/claude-code/CLAUDE.md.template
operator-packs/claude-code/install.md
operator-packs/claude-code/skills-map.yaml
```

### Critérios de pronto

- Pack é validável por schema.
- Template referencia `vault-maui/`.
- Pack não depende de MCP para P0.

## 7.2 Funcionalidade: Operator Pack Codex

### Objetivo

Permitir operação inicial do Maui em Codex com filesystem e `AGENTS.md`.

### Atividades

1. Criar diretório `operator-packs/codex/`.
2. Criar `pack.yaml`.
3. Criar `AGENTS.md.template`.
4. Criar `install.md`.
5. Criar `skills-map.yaml`.
6. Declarar convenção `.agents/skills/` quando aplicável.
7. Declarar limitações.
8. Incluir instrução de Update Request/Report.

### Entregáveis

```text
operator-packs/codex/pack.yaml
operator-packs/codex/AGENTS.md.template
operator-packs/codex/install.md
operator-packs/codex/skills-map.yaml
```

### Critérios de pronto

- Pack é validável.
- Template é compacto e operacional.
- Não duplica docs inteiros sem necessidade.

## 7.3 Funcionalidade: Operator Pack ChatGPT Handoff

### Objetivo

Permitir operação do Maui em ChatGPT sem filesystem direto.

### Atividades

1. Criar diretório `operator-packs/chatgpt-handoff/`.
2. Criar `pack.yaml`.
3. Criar `custom-gpt-instructions.md`.
4. Criar `handoff-protocol.md`.
5. Declarar `hash_config: unknown`.
6. Declarar que não há escrita direta no corpus.
7. Definir como pedir Update Request.
8. Definir como consumir Update Package.
9. Definir formato de resposta para handoff.

### Entregáveis

```text
operator-packs/chatgpt-handoff/pack.yaml
operator-packs/chatgpt-handoff/custom-gpt-instructions.md
operator-packs/chatgpt-handoff/handoff-protocol.md
```

### Critérios de pronto

- Pack declara limitações claramente.
- Não presume acesso ao vault.
- Produz Update Request quando necessário.

---

# 8. P0.4 — Context package inicial e protocolo de handoff

## 8.1 Funcionalidade: Maui Bootstrap Context

### Objetivo

Criar pacote mínimo de contexto para iniciar uma instância Maui.

### Atividades

1. Definir objetivo do bootstrap.
2. Selecionar conteúdo mínimo.
3. Incluir definição de Maui.
4. Incluir decisões de adequação documental.
5. Incluir fronteira corpus/toolkit.
6. Incluir precedência.
7. Incluir limitações por target.
8. Incluir instrução para solicitar update.
9. Validar contra schema.

### Entregáveis

```text
context-packages/current/maui-bootstrap.md
```

### Critérios de pronto

- Bootstrap não tenta carregar tudo.
- Bootstrap contém fontes e limites.
- Bootstrap é reutilizável por targets P0.

## 8.2 Funcionalidade: Context Package Claude Code

### Atividades

1. Adaptar bootstrap para filesystem.
2. Incluir caminhos esperados.
3. Incluir instrução para scripts P0.
4. Incluir instrução para exec report.
5. Incluir limitação de não alterar normas sem Human Gate.

### Entregável

```text
context-packages/targets/claude-code.md
```

## 8.3 Funcionalidade: Context Package Codex

### Atividades

1. Adaptar bootstrap para `AGENTS.md`.
2. Incluir instrução para uso de scripts.
3. Incluir formato de output técnico.
4. Incluir Update Request/Report.

### Entregável

```text
context-packages/targets/codex.md
```

## 8.4 Funcionalidade: Context Package ChatGPT Handoff

### Atividades

1. Declarar ausência de filesystem.
2. Declarar `unknown` para hash.
3. Incluir protocolo de handoff.
4. Incluir formato de Update Request.
5. Incluir limites de atuação.

### Entregável

```text
context-packages/targets/chatgpt-handoff.md
```

---

# 9. P0.5 — Update Protocol mínimo

## 9.1 Funcionalidade: Update Request

### Objetivo

Permitir que qualquer instância solicite evolução ou correção estruturada.

### Atividades

1. Definir template.
2. Definir exemplos.
3. Definir campos obrigatórios.
4. Incluir estado percebido.
5. Incluir restrições do target.
6. Incluir evidências.
7. Incluir output esperado.

### Entregáveis

```text
exec-requests/templates/update-request-template.md
exec-requests/examples/update-request-example.md
```

## 9.2 Funcionalidade: Update Package

### Objetivo

Permitir que operador com acesso ao corpus gere pacote de atualização aplicável.

### Atividades

1. Definir template.
2. Definir manifest.
3. Incluir lista de arquivos afetados.
4. Incluir instruções de aplicação.
5. Incluir validações.
6. Incluir riscos.
7. Incluir rollback.
8. Incluir Human Gate quando necessário.

### Entregáveis

```text
exports/templates/update-package-template.md
exports/examples/update-package-example.md
```

## 9.3 Funcionalidade: Update Report

### Objetivo

Registrar o resultado da aplicação de um update.

### Atividades

1. Definir template.
2. Definir status: `success`, `partial`, `failed`.
3. Relacionar com `request_id`.
4. Registrar arquivos alterados.
5. Registrar validações.
6. Registrar drift remanescente.
7. Registrar decisão humana quando houver.

### Entregáveis

```text
exec-reports/templates/update-report-template.md
exec-reports/examples/update-report-example.md
```

## 9.4 Funcionalidade: Procedures de update

### Atividades

1. Criar procedure de verificar atualizações.
2. Criar procedure de integrar atualização.
3. Criar checklist de Human Gate.
4. Criar checklist de rollback.

### Entregáveis

```text
procedures/procedimento-verificar-atualizacoes.md
procedures/procedimento-integrar-atualizacao.md
```

### Critérios de pronto do P0.5

- Request, Package e Report têm schema, template e exemplo.
- Há procedure para executar o fluxo.
- Fluxo funciona manualmente sem MCP.

---

# 10. P0.6 — Skills P0 para agentes de codificação

## 10.1 Funcionalidade: Skill `maui-vault-health`

### Atividades

1. Criar diretório da skill.
2. Criar `SKILL.md`.
3. Declarar quando usar.
4. Declarar quando não usar.
5. Apontar para `maui_vault_health.py`.
6. Definir output esperado.
7. Definir critérios de sucesso.

### Entregável

```text
skills/maui-vault-health/SKILL.md
```

## 10.2 Funcionalidade: Skill `maui-frontmatter-validate`

### Atividades

1. Criar `SKILL.md`.
2. Apontar para schema comum.
3. Apontar para script de validação.
4. Definir falhas bloqueantes.

### Entregável

```text
skills/maui-frontmatter-validate/SKILL.md
```

## 10.3 Funcionalidade: Skill `maui-context-export`

### Atividades

1. Criar `SKILL.md`.
2. Declarar targets P0.
3. Apontar para `maui_context_export.py`.
4. Definir limites de contexto.
5. Definir critérios de sucesso.

### Entregável

```text
skills/maui-context-export/SKILL.md
```

## 10.4 Funcionalidade: Skill `maui-update-export`

### Atividades

1. Criar `SKILL.md`.
2. Apontar para Update Protocol.
3. Apontar para `maui_update_export.py`.
4. Exigir `--dry-run` antes de `--write`.
5. Incluir Human Gate para mudanças normativas.

### Entregável

```text
skills/maui-update-export/SKILL.md
```

## 10.5 Funcionalidade: Skill `maui-doc-consistency-check`

### Atividades

1. Criar `SKILL.md`.
2. Combinar frontmatter, links e estrutura.
3. Gerar relatório de consistência.
4. Não alterar documentos por default.

### Entregável

```text
skills/maui-doc-consistency-check/SKILL.md
```

## 10.6 Funcionalidade: Skill `maui-registry-maintenance`

### Atividades

1. Criar `SKILL.md`.
2. Definir registro de instâncias.
3. Incluir regra para `unknown`.
4. Apontar para `maui_registry.py`.

### Entregável

```text
skills/maui-registry-maintenance/SKILL.md
```

## 10.7 Funcionalidade: Skill `maui-memory-maintenance`

### Atividades

1. Criar `SKILL.md`.
2. Apontar para `maui_memory_index.py`.
3. Declarar que índice não é fonte de verdade.
4. Definir alerta para memória sem confidencialidade.

### Entregável

```text
skills/maui-memory-maintenance/SKILL.md
```

### Critérios de pronto do P0.6

- Skills P0 têm frontmatter válido.
- Cada skill aponta script/procedure relacionada.
- Skills não concedem permissão de escrita por conta própria.

---

# 11. P0.7 — Procedures P0 e reflexes críticos

## 11.1 Funcionalidade: Procedure validar vault

### Atividades

1. Definir objetivo.
2. Listar pré-condições.
3. Executar validações manuais/scripts.
4. Interpretar severidade.
5. Definir output.
6. Definir quando bloquear avanço.

### Entregável

```text
procedures/procedimento-validar-vault.md
```

## 11.2 Funcionalidade: Procedure exportar contexto

### Atividades

1. Definir targets.
2. Selecionar fontes.
3. Rodar export.
4. Validar package.
5. Registrar report.

### Entregável

```text
procedures/procedimento-exportar-contexto.md
```

## 11.3 Funcionalidade: Procedure verificar atualizações

### Atividades

1. Checar registry.
2. Checar context package.
3. Checar versão/hash quando disponível.
4. Gerar Update Request se necessário.

### Entregável

```text
procedures/procedimento-verificar-atualizacoes.md
```

## 11.4 Funcionalidade: Procedure integrar atualização

### Atividades

1. Ler Update Package.
2. Executar dry-run.
3. Verificar Human Gate.
4. Aplicar quando autorizado.
5. Rodar validações.
6. Gerar Update Report.

### Entregável

```text
procedures/procedimento-integrar-atualizacao.md
```

## 11.5 Funcionalidade: Procedure criar operator pack

### Atividades

1. Definir target.
2. Definir capacidades.
3. Criar `pack.yaml`.
4. Criar template.
5. Criar install doc.
6. Validar pack.

### Entregável

```text
procedures/procedimento-criar-operator-pack.md
```

## 11.6 Funcionalidade: Procedure captura explícita

### Atividades

1. Receber comando explícito.
2. Classificar tipo de memória.
3. Sanitizar.
4. Compactar.
5. Salvar memória.
6. Registrar fonte.

### Entregável

```text
procedures/procedimento-captura-explicita.md
```

## 11.7 Reflexes críticos

### Atividades

Criar os reflexes:

```text
reflexes/reflexo-se-frontmatter-invalido.md
reflexes/reflexo-se-falta-contexto.md
reflexes/reflexo-se-instancia-pede-update.md
reflexes/reflexo-se-escrita-persistente.md
reflexes/reflexo-se-plugin-externo.md
```

Cada reflex deve conter:

- gatilho;
- ação imediata;
- limite;
- escalonamento;
- registro esperado.

### Critérios de pronto do P0.7

- Procedures são executáveis por humano técnico.
- Reflexes têm gatilho inequívoco.
- Escrita persistente passa por Human Gate.

---

# 12. P0.8 — Evals e smoke tests mínimos

## 12.1 Funcionalidade: Eval de integridade do corpus

### Atividades

1. Criar eval de estrutura mínima.
2. Verificar documentos-base.
3. Verificar schemas P0.
4. Verificar operator packs P0.
5. Verificar context package bootstrap.

### Entregável

```text
evals/regression/corpus-integrity.eval.yaml
```

## 12.2 Funcionalidade: Eval do `maui_vault_health.py`

### Atividades

1. Criar fixture de vault válido.
2. Criar fixture de vault inválido.
3. Validar saída JSON.
4. Validar severidade.

### Entregável

```text
evals/scripts/maui-vault-health.eval.yaml
```

## 12.3 Funcionalidade: Eval do Update Protocol

### Atividades

1. Validar Update Request exemplo.
2. Validar Update Package exemplo.
3. Validar Update Report exemplo.
4. Verificar relação request/report.
5. Verificar presença de rollback.
6. Verificar Human Gate quando aplicável.

### Entregável

```text
evals/update-protocol/request-package-report.eval.yaml
```

## 12.4 Funcionalidade: Evals de operator packs

### Atividades

1. Validar Claude Code pack.
2. Validar Codex pack.
3. Validar ChatGPT Handoff pack.
4. Verificar limitações por target.
5. Verificar ausência de falsa conformidade.

### Entregáveis

```text
evals/operator-packs/claude-code-pack.eval.yaml
evals/operator-packs/codex-pack.eval.yaml
evals/operator-packs/chatgpt-handoff-pack.eval.yaml
```

## 12.5 Funcionalidade: Eval de context package bootstrap

### Atividades

1. Verificar fontes.
2. Verificar limites.
3. Verificar target.
4. Verificar que não carrega todo o corpus.

### Entregável

```text
evals/context-packages/bootstrap-context.eval.yaml
```

### Critérios de pronto do P0.8

- Smoke tests cobrem primeiro uso real.
- Falhas críticas bloqueiam piloto.
- Relatórios são graváveis em `validations/`.

---

# 13. P0.9 — Registro de decisão, memória mínima e curadoria file-based

## 13.1 Funcionalidade: Registro de decisão

### Objetivo

Registrar decisões humanas do piloto Maui.

### Atividades

1. Criar template de decisão.
2. Criar primeira memória de decisão.
3. Registrar decisões sobre versionamento e diretórios.
4. Registrar decisões sobre adendos separados.
5. Registrar decisão de hash abrangente.

### Entregáveis

```text
project-memories/templates/decisao-template.md
project-memories/YYYY-MM-DD-decisao-adocao-piloto-maui.md
```

## 13.2 Funcionalidade: Memória mínima

### Atividades

1. Definir frontmatter mínimo de memória.
2. Criar procedure de captura explícita.
3. Criar índice inicial.
4. Validar confidencialidade.

### Entregáveis

```text
memorias/README.md
procedures/procedimento-captura-explicita.md
.maui/cache/memory-index.json
```

## 13.3 Funcionalidade: Curadoria file-based

### Atividades

1. Criar `panel/`.
2. Criar `panel/dashboard.md`.
3. Criar `panel/decisions/`.
4. Criar `panel/reports/`.
5. Criar `panel/pending.md`.
6. Definir formato simples de status.

### Entregáveis

```text
panel/dashboard.md
panel/pending.md
panel/decisions/
panel/reports/
```

### Critérios de pronto do P0.9

- Decisões são registráveis.
- Reports são coletáveis.
- Memória tem confidencialidade.
- Não há promoção automática de insight/adendo.

---

# 14. P1 — Expansão operacional controlada

## 14.1 Funcionalidade: Hooks P1

### Objetivo

Adicionar enforcement determinístico sem bloquear o P0.

### Atividades

1. Criar hook `session-start/check-instance-status`.
2. Criar hook `pre-write/guard-corpus-write`.
3. Criar hook `post-write/validate-frontmatter`.
4. Criar hook `post-write/validate-links`.
5. Criar hook `on-export/validate-update-package`.
6. Criar manifesto de hook.
7. Criar teste mínimo por hook blocking.

### Entregáveis

```text
hooks/session-start/check-instance-status.md
hooks/pre-write/guard-corpus-write.md
hooks/post-write/validate-frontmatter.md
hooks/post-write/validate-links.md
hooks/on-export/validate-update-package.md
```

## 14.2 Funcionalidade: Subagentes P1

### Atividades

1. Criar `maui-doc-reviewer`.
2. Criar `maui-schema-validator`.
3. Criar `maui-context-compressor`.
4. Criar `maui-update-planner`.
5. Criar contrato de retorno comum.
6. Definir ferramentas permitidas e bloqueadas.

### Entregáveis

```text
subagents/maui-doc-reviewer.md
subagents/maui-schema-validator.md
subagents/maui-context-compressor.md
subagents/maui-update-planner.md
```

## 14.3 Funcionalidade: Painel CLI completo P1

### Atividades

1. Implementar `maui panel status`.
2. Implementar `maui panel dispatch`.
3. Implementar `maui panel collect`.
4. Implementar `maui panel record-decision`.
5. Gerar dashboard consolidado.
6. Integrar exec reports.

### Entregáveis

```text
scripts/maui_panel.py
panel/dashboard.md
panel/panel-state.yaml
```

## 14.4 Funcionalidade: MCP read-only P1

### Atividades

1. Definir server read-only.
2. Expor `maui.corpus.search`.
3. Expor `maui.corpus.read`.
4. Expor `maui.context.export`.
5. Expor `maui.registry.status`.
6. Bloquear escrita.
7. Logar chamadas.

### Entregáveis

```text
mcp-servers/read-only/server.md
mcp-servers/read-only/tools.yaml
```

## 14.5 Critérios de entrada em P1

- P0.0 a P0.8 concluídos.
- Piloto Claude Code ou Codex executado pelo menos uma vez.
- Update Request/Package/Report testado.
- Validação mínima sem falhas críticas.

---

# 15. P2 — Integração avançada e distribuição

## 15.1 Funcionalidade: Plugins P2

### Atividades

1. Criar `plugins/maui-core-essentials/`.
2. Criar `plugins/maui-instance-management/`.
3. Criar `plugins/maui-curation-pack/`.
4. Criar schema de plugin completo.
5. Criar dry-run de instalação.
6. Definir Human Gate para plugin externo.

### Entregáveis

```text
plugins/maui-core-essentials/plugin.yaml
plugins/maui-instance-management/plugin.yaml
plugins/maui-curation-pack/plugin.yaml
```

## 15.2 Funcionalidade: Automations P2

### Atividades

1. Criar automation de vault health semanal.
2. Criar automation de drift check semanal.
3. Criar automation de revisão mensal de insights.
4. Garantir modo read-only ou relatório.
5. Bloquear escrita persistente sem Human Gate.

### Entregáveis

```text
automations/weekly-vault-health.yaml
automations/weekly-drift-check.yaml
automations/monthly-insight-review.yaml
```

## 15.3 Funcionalidade: MCP guarded-write P2

### Atividades

1. Definir autenticação.
2. Definir escopos de escrita.
3. Exigir dry-run.
4. Exigir Human Gate.
5. Gerar audit log.
6. Criar rollback.

### Entregáveis

```text
mcp-servers/guarded-write/spec.md
mcp-servers/guarded-write/tools.yaml
```

## 15.4 Funcionalidade: REST/Action para ChatGPT P2

### Atividades

1. Definir endpoints read-only.
2. Definir autenticação.
3. Criar action schema.
4. Criar operator pack ChatGPT Action.
5. Validar privacidade.
6. Manter escrita bloqueada no início.

### Entregáveis

```text
operator-packs/chatgpt-action/action-schema.yaml
operator-packs/chatgpt-action/install.md
```

## 15.5 Funcionalidade: UI do painel P2

### Atividades

1. Definir escopo da UI.
2. Ler panel-state.
3. Mostrar exec requests.
4. Mostrar reports.
5. Registrar decisões.
6. Não aplicar mudanças normativas automaticamente.

### Entregáveis

```text
panel-ui/spec.md
```

---

# 16. Backlog adiado explicitamente

Estas funcionalidades não bloqueiam o primeiro uso do Maui:

- UI completa do painel.
- Plugins externos.
- Automations com escrita persistente.
- MCP guarded-write.
- REST/Action para ChatGPT.
- Busca vetorial de memória.
- Subagentes numerosos ou especializados demais.
- Suporte completo a todos os targets.
- Instalação automática em múltiplas ferramentas.

---

# 17. Sequência de execução resumida

## 17.1 Semana/iteração 1 — Fundação

1. Criar `vault-maui/`.
2. Salvar documentos-base.
3. Criar `.maui/`.
4. Criar schemas comuns.
5. Criar fixtures iniciais.

## 17.2 Semana/iteração 2 — Validação e contexto

1. Implementar `maui_vault_health.py`.
2. Implementar validação de frontmatter.
3. Implementar validação de links.
4. Criar context package bootstrap.
5. Criar export inicial.

## 17.3 Semana/iteração 3 — Instanciação

1. Criar Claude Code pack.
2. Criar Codex pack.
3. Criar ChatGPT Handoff pack.
4. Validar packs.
5. Registrar instâncias piloto.

## 17.4 Semana/iteração 4 — Update cycle

1. Criar templates de Update Request/Package/Report.
2. Implementar `maui_update_export.py` básico.
3. Criar procedures de update.
4. Executar teste manual ponta a ponta.

## 17.5 Semana/iteração 5 — Operação assistida

1. Criar skills P0.
2. Criar procedures P0.
3. Criar reflexes críticos.
4. Criar smoke tests mínimos.
5. Registrar primeira decisão/memória.

## 17.6 Semana/iteração 6 — Piloto controlado

1. Rodar `maui_vault_health.py`.
2. Instanciar Claude Code ou Codex.
3. Gerar context package.
4. Executar Update Request/Package/Report.
5. Registrar exec report.
6. Registrar decisão de avanço para P1 ou ajustes.

---

# 18. Marco de primeiro uso real

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

---

# 19. Riscos globais do roadmap

| Risco                                  | Impacto | Mitigação                                                  |
| -------------------------------------- | ------- | ---------------------------------------------------------- |
| Começar por UI/MCP antes do corpus     | Alto    | Travar P2 até P0 validado                                  |
| Scripts codificarem política implícita | Alto    | Schemas e specs antes dos scripts                          |
| Misturar Saara e Maui                  | Alto    | `vault-maui/`, `.maui/`, adendos e versionamento separados |
| Falsa conformidade em ChatGPT Handoff  | Alto    | Estado obrigatório `unknown`                               |
| Automação escrever sem Human Gate      | Alto    | Read-only por default e hooks P1                           |
| Falta de validação inicial             | Médio   | `maui_vault_health.py` como primeiro script                |
| Excesso de contexto                    | Médio   | Context package mínimo e target-specific                   |
| Plugins externos prematuros            | Médio   | Adiar para P2 com Human Gate                               |

---

# 20. Métricas de acompanhamento

| Métrica                            | Alvo P0      |
| ---------------------------------- | ------------ |
| Diretórios obrigatórios criados    | 100%         |
| Docs-base salvos em `01_manifest/` | 100%         |
| Schemas P0 criados                 | 8/8          |
| Scripts P0 essenciais funcionando  | 4/4 iniciais |
| Operator packs P0 criados          | 3/3          |
| Update artifacts com exemplos      | 3/3          |
| Skills P0 criadas                  | 7/7          |
| Procedures P0 criadas              | 6/6          |
| Smoke tests mínimos                | 6/6          |
| Falhas críticas no health check    | 0            |

---

# 21. F/I/H

## 21.1 Fatos

- Maui será organizado em `vault-maui/`.
- `.maui/` e `.saara/` coexistirão.
- Adendos Maui servirão apenas ao Maui.
- Maui inicia em `v1.0` com versionamento separado do Saara.
- `hash_config` Maui deve incluir todo o corpus relevante.

## 21.2 Inferências

- O primeiro uso real depende mais de estrutura, validação, context package e operator pack do que de MCP ou UI.
- Claude Code e Codex são os melhores operadores iniciais por acesso a filesystem.
- ChatGPT Handoff deve operar com estado `unknown` e Update Request.

## 21.3 Hipóteses

- O desenvolvimento inicial será feito por operador com filesystem.
- P0 pode ser implementado sem servidor persistente.
- Busca vetorial, UI e integrações REST podem ser adiadas sem comprometer o início do uso.
