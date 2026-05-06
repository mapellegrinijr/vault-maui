---
titulo: "Índice Core — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: indice_navegacao
escopo: maui
corpus: vault-maui
precedencia: 5
human_gate: true
baseado_em: "indice-saara v7.1.1 — adaptado, não copiado"
compatibilidade:
  - system_prompt_maui_v1_0
  - especificacao_completa_maui_v1_0
  - principios_fundacionais_maui_v1_0
  - contrato_precedencia_maui_v1_0
referencias:
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/especificacao-completa-maui.md"
  - "vault-maui/00_core/pka-prompt-engineering.md"
  - "vault-maui/00_core/pka-agent-engineering.md"
  - "vault-maui/00_core/pka-development-engineer.md"
  - "vault-maui/00_core/pka-ai-solutions-architect-elite.md"
  - "vault-maui/00_core/pka-written-comms-core.md"
  - "vault-maui/00_core/pka-safe-agile-master-elite.md"
  - "vault-maui/00_core/spec-distribuicao-maui.md"
  - "vault-maui/00_core/spec-instanciacao-conformidade-maui.md"
  - "vault-maui/00_core/spec-context-engineering-maui.md"
  - "vault-maui/00_core/spec-capture-layer-maui.md"
  - "vault-maui/00_core/spec-memory-store-maui.md"
  - "vault-maui/00_core/spec-adendos-maui.md"
  - "vault-maui/00_core/spec-parametrizacao-maui.md"
  - "vault-maui/01_manifest/spec-parametrizacao-maui.json"
  - "vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md"
tags:
  - maui
  - indice
  - navegacao
  - configuracao-base
---

# Índice Core — Maui

> Mapa de navegação do vault Maui. Ponto de partida para entender estrutura, precedência e relações entre os documentos normativos do Maui v1.0.
> Status: `proposta` — criado em P0.1.31 sob Human Gate explícito.

---

## Visão em 10 segundos

O Maui é definido pelo seu **corpus cognitivo versionado** em `vault-maui/` (Princípio 1: Corpus Maui como fonte de verdade). Núcleo organizado em **9 níveis de precedência**, com:

- **12 Princípios Fundacionais** (corpus, separação Saara/Maui, configuração-base, contrato, read-only, handoff, Human Gate, conformidade, PE Elite, AE, Context Engineering, memória)
- **6 PKAs** — Prompt Engineering Elite (obrigatória), Agent Engineering, Development Engineer, AI Solutions Architect, Written Comms, SAFe/Agile (condicional)
- **6 Specs Subsidiárias** — distribuição, instanciação/conformidade, context engineering, capture layer, memory store, adendos
- **1 Spec de Parametrização** (`.md` + `.json`)

Infraestrutura (Claude Code, Codex, MCP server, ChatGPT, API) é substituível. A identidade do Maui vive no corpus.

---

## Por precedência operacional (v1.0)

| Nível | Fonte | Caminho no vault |
|-------|-------|-----------------|
| 1 | Políticas externas, plataforma, lei e compliance | *(externo ao vault)* |
| 2 | Contrato de Precedência Maui + System Prompt Maui | `vault-maui/00_core/contrato-precedencia-maui.md` · `vault-maui/00_core/system-prompt-maui.md` |
| 3 | Princípios Fundacionais | `vault-maui/00_core/principios-fundacionais-maui.md` |
| 4 | Especificação Completa | `vault-maui/00_core/especificacao-completa-maui.md` |
| 5 | PKAs vigentes + Specs subsidiárias (equalizadas por domínio) | ver seção "PKAs" e "Specs Subsidiárias" abaixo |
| 6 | Parametrização executável | `vault-maui/00_core/spec-parametrizacao-maui.md` · `vault-maui/01_manifest/spec-parametrizacao-maui.json` |
| 7 | Roadmap, planos, inventários, exec-reports, memórias e context briefs | conforme tipo e evidência |
| 8 | Conteúdo recuperado por ferramentas, com origem verificada | *(dinâmico)* |
| 9 | Pedido do usuário | *(runtime)* |

---

## PKAs (6)

| Domínio | Arquivo | Status | Nota |
|---------|---------|--------|------|
| Prompt Engineering Elite | `vault-maui/00_core/pka-prompt-engineering.md` | proposta | **Obrigatória, primeira classe** |
| Agent Engineering | `vault-maui/00_core/pka-agent-engineering.md` | proposta | |
| Development Engineer | `vault-maui/00_core/pka-development-engineer.md` | proposta | |
| AI Solutions Architect | `vault-maui/00_core/pka-ai-solutions-architect-elite.md` | proposta | |
| Written Comms Core | `vault-maui/00_core/pka-written-comms-core.md` | proposta | |
| SAFe/Agile Master Elite | `vault-maui/00_core/pka-safe-agile-master-elite.md` | proposta_condicional | Requer owner + T1-T8 + Human Gate para ativação no Domain Router |

---

## Specs Subsidiárias (6)

| Domínio | Arquivo | Status |
|---------|---------|--------|
| Distribuição | `vault-maui/00_core/spec-distribuicao-maui.md` | proposta |
| Instanciação e Conformidade | `vault-maui/00_core/spec-instanciacao-conformidade-maui.md` | proposta |
| Context Engineering | `vault-maui/00_core/spec-context-engineering-maui.md` | proposta |
| Capture Layer | `vault-maui/00_core/spec-capture-layer-maui.md` | proposta |
| Memory Store | `vault-maui/00_core/spec-memory-store-maui.md` | proposta |
| Adendos | `vault-maui/00_core/spec-adendos-maui.md` | proposta |

---

## Núcleo normativo (por tipo)

### Contratos e Precedência

- `vault-maui/00_core/contrato-precedencia-maui.md` v1.0 — contrato de precedência operacional (precedência 2)
- `vault-maui/00_core/principios-fundacionais-maui.md` v1.0 — 12 princípios fundacionais (precedência 3)
- `vault-maui/00_core/especificacao-completa-maui.md` v1.0 — especificação normativa de referência (precedência 4)
- `vault-maui/00_core/system-prompt-maui.md` v1.0 — contrato runtime (precedência 2)

### Parametrização

- `vault-maui/00_core/spec-parametrizacao-maui.md` v1.0 — documentação humana (precedência 6)
- `vault-maui/01_manifest/spec-parametrizacao-maui.json` v1.0 — executável (precedência 6)

### Documentos auxiliares core

- `vault-maui/00_core/regras-operacionais.md` — regras operacionais complementares
- `vault-maui/00_core/arquitetura-maui-v0-2.md` — arquitetura técnica
- `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md` — spec funcional
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md` — roadmap (mapa de destino, não evidência)

---

## Por domínio (Domain Router)

### Prompt Engineering Elite
**Quando ativar:** prompts, system prompts, developer prompts, instruction sets, templates, rubricas de avaliação, testes prompt-level, exemplos few-shot, diagnóstico de falha instrucional, mitigação textual de prompt injection, prompt executor (Codex/Claude Code).
**Documento:** `vault-maui/00_core/pka-prompt-engineering.md`
**Regra:** PKA obrigatória de primeira classe. Lidera o contrato textual/instrucional em qualquer tarefa que envolva prompt, mesmo que também haja componente de agente.

### Agent Engineering
**Quando ativar:** agentes, orquestração, tools, memória, RAG, roteamento, MCP/API/actions, distribuição, instanciação, captura, observabilidade e rollout.
**Documento:** `vault-maui/00_core/pka-agent-engineering.md`
**Regra:** lidera integração sistêmica e operacional. Não absorve Prompt Engineering.

### AI Solutions Architect
**Quando ativar:** arquitetura-alvo, desenho de solução, topologia, integração, trade-offs, make/buy/adapt, soluções com IA/LLM/RAG.
**Documento:** `vault-maui/00_core/pka-ai-solutions-architect-elite.md`

### Development Engineer
**Quando ativar:** implementação, código, refatoração, debug, testes, scripts, hardening técnico.
**Documento:** `vault-maui/00_core/pka-development-engineer.md`

### Written Comms Core
**Quando ativar:** comunicação escrita, reescrita, mensagem, memo, ajuste editorial, SACCE.
**Documento:** `vault-maui/00_core/pka-written-comms-core.md`

### SAFe/Agile Master Elite (condicional)
**Quando ativar:** SAFe, Agile, facilitação, eventos, impedimentos, riscos, cadência, PI Planning, ART — apenas após owner definido, suíte T1-T8 e Human Gate.
**Documento:** `vault-maui/00_core/pka-safe-agile-master-elite.md`
**Restrição:** não ativar no Domain Router enquanto `proposta_condicional`.

### Multi-domínio
Aplicar todos os PKAs relevantes. Prompt Engineering lidera contrato textual/instrucional; Agent Engineering lidera integração sistêmica. Explicitar trade-offs quando houver conflito.

---

## Pastas operacionais

| Pasta | Uso |
|-------|-----|
| `vault-maui/00_core/` | Normativos, PKAs, specs subsidiárias, parametrização, índice |
| `vault-maui/01_manifest/` | JSON executável, README |
| `vault-maui/memorias/` | Memórias canônicas (escopo, confidencialidade, context_brief_flag) |
| `vault-maui/exec-reports/submitted/` | Evidência de execução (fonte de verdade operacional) |
| `vault-maui/exec-reports/reviewed/` | Exec-reports revisados |
| `vault-maui/planos/` | Planos de implementação |
| `vault-maui/inventarios/` | Diagnósticos e inventários |
| `vault-maui/context-packages/current/` | Context briefs ativos para retomada |
| `vault-maui/context-packages/readiness/` | Readiness de context brief |
| `vault-maui/handoffs/` | Handoffs para instâncias sem filesystem |
| `vault-maui/procedures/` | Procedimentos operacionais |
| `vault-maui/skills/` | Skills reutilizáveis por executores |
| `vault-maui/schemas/` | Schemas de validação |
| `vault-maui/00_core/pka-*-adendos/` | Adendos por PKA (criados quando primeiro adendo for proposto) |

---

## Fluxos de uso comuns

### Retomada de contexto
1. Verificar git log e filesystem atual
2. Ler exec-reports em `vault-maui/exec-reports/submitted/`
3. Ler context brief atual em `vault-maui/context-packages/current/`
4. Consultar memórias com `deve_ser_considerado_em_context_brief: true` em `vault-maui/memorias/`
5. Usar handoff em `vault-maui/handoffs/` se disponível e verificável

### Iniciar tarefa com domínio identificado
1. Ler este índice para localizar PKA primária
2. Ler PKA primária e PKAs de suporte relevantes
3. Executar tarefa com Human Gate quando normativa
4. Registrar exec-report em `vault-maui/exec-reports/submitted/`

### Verificar estado de conformidade (MVP pré-P0.3)
1. Verificar existência dos arquivos em `vault-maui/00_core/` via filesystem
2. Comparar commit SHA com git log
3. Declarar `unknown` se filesystem não acessível; nunca declarar `current` sem evidência

### Adicionar adendo a uma PKA
1. Verificar limite de 2 adendos pendentes por PKA (`spec-adendos-maui.md`)
2. Criar arquivo em `vault-maui/00_core/pka-{nome}-adendos/`
3. Frontmatter canônico com status: proposto
4. Aguardar Human Gate antes de promover para `ativo`

---

## Glossário rápido

| Termo | Significado |
|-------|-------------|
| **PKA** | Política de Conhecimento do Agente |
| **Prompt Engineering Elite** | PKA obrigatória de primeira classe; lidera contratos textuais/instrucionais |
| **Agent Engineering** | PKA de integração sistêmica; agentes, tools, memória, RAG, orquestração |
| **Context Engineering** | Ciclo completo de contexto Maui: Write, Select, Compress, Isolate, Inject |
| **Camadas A/B/C** | Configuração base / Complementos de sessão / Contexto conversacional |
| **Capture Layer** | Inversa da distribuição; captura material valioso de conversas para Memory Store |
| **Insight Pipeline** | Observações operacionais → adendos → Human Gate → corpo da PKA |
| **Memory Store** | `vault-maui/memorias/`; markdown é fonte de verdade; SQLite é auxiliar |
| **hash_config** | SHA-256 sobre arquivos normativos de `vault-maui/00_core/` |
| **Modo A / B / B1** | Meta-arquitetura e governança / Operacional / Operacional com escalada |
| **D0–D3** | Profundidade de resposta: direto → riscos → opções → governança completa |
| **L0–L3** | Progressive Disclosure: resultado → rationale → opções → auditoria |
| **MVS** | Mínimo Verificável Seguro; entrega mínima antes de informação crítica ausente |
| **F/I/H** | Fato / Inferência / Hipótese |
| **Human Gate** | Aprovação humana explícita obrigatória para mudanças normativas |
| **proposta** | Status de todos os normativos Maui na Configuração-base |
| **proposta_condicional** | Status da PKA SAFe/Agile; requer owner + T1-T8 + Human Gate |
| **unknown** | Estado de conformidade quando filesystem/hash não verificável |
| **Domain Router** | Mecanismo de roteamento por domínio e tipo de tarefa |

---

## Estado atual da Configuração-base (pós-P0.1.31)

| Artefato | Caminho | Status |
|----------|---------|--------|
| Contrato de precedência | `vault-maui/00_core/contrato-precedencia-maui.md` | proposta ✓ |
| Princípios fundacionais | `vault-maui/00_core/principios-fundacionais-maui.md` | proposta ✓ |
| Especificação completa | `vault-maui/00_core/especificacao-completa-maui.md` | proposta ✓ |
| System prompt | `vault-maui/00_core/system-prompt-maui.md` | proposta ✓ |
| PKA Prompt Engineering Elite | `vault-maui/00_core/pka-prompt-engineering.md` | proposta ✓ |
| PKA Agent Engineering | `vault-maui/00_core/pka-agent-engineering.md` | proposta ✓ |
| PKA Development Engineer | `vault-maui/00_core/pka-development-engineer.md` | proposta ✓ |
| PKA AI Solutions Architect | `vault-maui/00_core/pka-ai-solutions-architect-elite.md` | proposta ✓ |
| PKA Written Comms Core | `vault-maui/00_core/pka-written-comms-core.md` | proposta ✓ |
| PKA SAFe/Agile Master Elite | `vault-maui/00_core/pka-safe-agile-master-elite.md` | proposta_condicional ✓ |
| Spec Distribuição | `vault-maui/00_core/spec-distribuicao-maui.md` | proposta ✓ |
| Spec Instanciação/Conformidade | `vault-maui/00_core/spec-instanciacao-conformidade-maui.md` | proposta ✓ |
| Spec Context Engineering | `vault-maui/00_core/spec-context-engineering-maui.md` | proposta ✓ |
| Spec Capture Layer | `vault-maui/00_core/spec-capture-layer-maui.md` | proposta ✓ |
| Spec Memory Store | `vault-maui/00_core/spec-memory-store-maui.md` | proposta ✓ |
| Spec Adendos | `vault-maui/00_core/spec-adendos-maui.md` | proposta ✓ |
| Spec Parametrização (.md) | `vault-maui/00_core/spec-parametrizacao-maui.md` | proposta ✓ |
| Spec Parametrização (.json) | `vault-maui/01_manifest/spec-parametrizacao-maui.json` | proposta ✓ |
| **Índice Core** | `vault-maui/00_core/indice-maui.md` | **proposta ✓ (este documento)** |
| Revisão integrada | P0.1.32 | **pendente** |

P0.1.11 permanece não executada. Instanciação manual Maui permanece não pronta.

---

## Limites deste índice

- Status `proposta`; revisão integrada em P0.1.32.
- Não cria operator packs, bootstrap ou context packages finais.
- Não executa etapas do roadmap por inferência.
- Não promove status de nenhum normativo.
- Links são caminhos filesystem; em ambientes sem filesystem, declarar `unknown`.

*Índice v1.0 · Criado em 2026-05-06 · Maui Configuração-base P0.1.31*
