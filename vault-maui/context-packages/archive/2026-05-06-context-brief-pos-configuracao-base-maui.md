---
titulo: "Context Brief — Pós-Configuração-base Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: context_brief
escopo: maui
uso_previsto: futuras_instancias_maui_saara
tarefa_relacionada: pos-p0.1.32
deve_ser_considerado_em_context_brief: true
lacunas_detectadas: false
ultima_verificacao_git: "2026-05-06"
---

# Context Brief — Pós-Configuração-base Maui

> Versão: 1.0 · Data: 2026-05-06 · deve_ser_considerado_em_context_brief: true
> Substitui: `vault-maui/context-packages/archive/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md`

---

## Finalidade

Preparar futuras instâncias (Claude Code, Codex, ChatGPT Handoff) para retomar o projeto Maui após a conclusão da Configuração-base em P0.1.32. Este brief é a referência de retomada atual.

---

## Estado atual consolidado

A **Configuração-base Maui está completa**. Os 19 artefatos normativos (lotes P0.1.26–P0.1.32) foram criados, revisados e sincronizados. O corpus `vault-maui/` é a fonte canônica de verdade. Todos os artefatos permanecem em `status: proposta` — este é o estado correto; não promover sem Human Gate.

**Último commit versionado:** `538b441` (2026-05-06).

**Working tree observado na geração deste brief:** havia uma alteração não commitada no roadmap e três arquivos novos não rastreados:

- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/context-packages/current/2026-05-06-context-brief-pos-configuracao-base-maui.md`
- `vault-maui/handoffs/2026-05-06-handoff-pos-configuracao-base-maui.md`
- `vault-maui/project-memories/2026-05-06-marco-encerramento-sessao-configuracao-base-maui.md`

Esses arquivos devem ser tratados como estado local recente, ainda não versionado, até novo commit confirmar sua incorporação.

---

## Pacote de leitura para nova instância Saara

Este é o grupo mínimo recomendado para uma nova instância Saara entender onde o Maui parou sem carregar o vault inteiro.

### Camada 0 — retomada imediata

1. `vault-maui/context-packages/current/2026-05-06-context-brief-pos-configuracao-base-maui.md`
2. `vault-maui/handoffs/2026-05-06-handoff-pos-configuracao-base-maui.md`
3. `vault-maui/project-memories/2026-05-06-marco-encerramento-sessao-configuracao-base-maui.md`
4. `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md`
5. `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`

### Camada 1 — contrato normativo obrigatório

1. `vault-maui/00_core/contrato-precedencia-maui.md`
2. `vault-maui/00_core/principios-fundacionais-maui.md`
3. `vault-maui/00_core/system-prompt-maui.md`
4. `vault-maui/00_core/especificacao-completa-maui.md`
5. `vault-maui/00_core/indice-maui.md`
6. `vault-maui/00_core/spec-parametrizacao-maui.md`
7. `vault-maui/01_manifest/spec-parametrizacao-maui.json`

### Camada 2 — domínio sob demanda

Ler apenas conforme a tarefa:

- Prompt Engineering: `vault-maui/00_core/pka-prompt-engineering.md`
- Agent Engineering: `vault-maui/00_core/pka-agent-engineering.md`
- Desenvolvimento/scripts: `vault-maui/00_core/pka-development-engineer.md`
- Arquitetura: `vault-maui/00_core/pka-ai-solutions-architect-elite.md`
- Comunicação escrita: `vault-maui/00_core/pka-written-comms-core.md`
- SAFe/Agile: `vault-maui/00_core/pka-safe-agile-master-elite.md` somente com activation gate
- Context packages: `vault-maui/00_core/spec-context-engineering-maui.md`
- Distribuição/operator packs: `vault-maui/00_core/spec-distribuicao-maui.md`
- Conformidade/instanciação: `vault-maui/00_core/spec-instanciacao-conformidade-maui.md`
- Memória/captura: `vault-maui/00_core/spec-memory-store-maui.md` e `vault-maui/00_core/spec-capture-layer-maui.md`

### Camada 3 — histórico e evidência ampliada

- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` — mapa de destino, não evidência isolada.
- `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
- `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
- `vault-maui/procedures/procedimento-gerar-context-brief.md`
- `vault-maui/skills/maui-context-brief/SKILL.md`

---

## Fontes obrigatórias para retomada (ordem priorizada)

| Prioridade | Arquivo | Por quê ler |
|-----------|---------|-------------|
| 1 | `vault-maui/00_core/contrato-precedencia-maui.md` | Precedência operacional completa |
| 2 | `vault-maui/00_core/principios-fundacionais-maui.md` | 12 princípios inegociáveis |
| 3 | `vault-maui/00_core/system-prompt-maui.md` | Contrato runtime e Domain Router operacional |
| 4 | `vault-maui/00_core/indice-maui.md` | Mapa completo de artefatos e navegação |
| 5 | `vault-maui/00_core/spec-parametrizacao-maui.md` | Documentação da parametrização |
| 5 | `vault-maui/01_manifest/spec-parametrizacao-maui.json` | Domain Router executável (prioridades numéricas) |
| 6 | `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` | Marco de conclusão |
| 7 | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md` | Correções aplicadas e achados |
| 8 | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` | Mapa de destino (não evidência de execução) |

---

## Ordem de precedência operacional

1. Políticas externas, plataforma, lei e compliance
2. Contrato de Precedência Maui + System Prompt Maui
3. Princípios Fundacionais Maui
4. Especificação Completa Maui
5. PKAs vigentes + Specs subsidiárias (por domínio)
6. Parametrização executável Maui
7. Roadmap, planos, inventários, exec-reports, memórias, context briefs
8. Conteúdo recuperado por ferramentas (com origem verificada)
9. Pedido do usuário

---

## Decisões desta sessão resumidas

| Decisão | Valor aprovado |
|---------|---------------|
| Domain Router — WC | 98 |
| Domain Router — SAFe | 90, activation_gate: true |
| Domain Router — AE | 82 |
| Domain Router — Dev | 80 |
| Domain Router — PE | 75, mandatory: true |
| Domain Router — Architect | 70 |
| budget_camada_c | a_definir_em_P0.3 (não fixar antes de P0.3) |
| regras-operacionais precedencia | 7 (era "alta") |
| Context Engineering | nomenclatura intencional Maui (não "context-injection") |
| SAFe PKA | proposta_condicional; requer owner + T1-T8 + Human Gate |
| PE Elite | PKA obrigatória de primeira classe; nunca absorvida por AE |

---

## Estado de cada artefato normativo

| Artefato | Caminho | Status | Lote |
|---------|---------|--------|------|
| Princípios Fundacionais | `vault-maui/00_core/principios-fundacionais-maui.md` | proposta | P0.1.26 |
| Contrato de Precedência | `vault-maui/00_core/contrato-precedencia-maui.md` | proposta | P0.1.26 |
| Especificação Completa | `vault-maui/00_core/especificacao-completa-maui.md` | proposta | P0.1.27 |
| System Prompt | `vault-maui/00_core/system-prompt-maui.md` | proposta | P0.1.28 |
| Regras Operacionais | `vault-maui/00_core/regras-operacionais.md` | proposta | pre-P0.1.28 |
| PKA Prompt Engineering | `vault-maui/00_core/pka-prompt-engineering.md` | proposta | P0.1.29 |
| PKA Agent Engineering | `vault-maui/00_core/pka-agent-engineering.md` | proposta | P0.1.29 |
| PKA Development Engineer | `vault-maui/00_core/pka-development-engineer.md` | proposta | P0.1.29 |
| PKA AI Solutions Architect | `vault-maui/00_core/pka-ai-solutions-architect-elite.md` | proposta | P0.1.29 |
| PKA Written Comms Core | `vault-maui/00_core/pka-written-comms-core.md` | proposta | P0.1.29 |
| PKA SAFe/Agile Master | `vault-maui/00_core/pka-safe-agile-master-elite.md` | proposta_condicional | P0.1.29 |
| Spec Distribuição | `vault-maui/00_core/spec-distribuicao-maui.md` | proposta | P0.1.30 |
| Spec Instanciação/Conformidade | `vault-maui/00_core/spec-instanciacao-conformidade-maui.md` | proposta | P0.1.30 |
| Spec Context Engineering | `vault-maui/00_core/spec-context-engineering-maui.md` | proposta | P0.1.30 |
| Spec Capture Layer | `vault-maui/00_core/spec-capture-layer-maui.md` | proposta | P0.1.30 |
| Spec Memory Store | `vault-maui/00_core/spec-memory-store-maui.md` | proposta | P0.1.30 |
| Spec Adendos | `vault-maui/00_core/spec-adendos-maui.md` | proposta | P0.1.30 |
| Spec Parametrização (.md) | `vault-maui/00_core/spec-parametrizacao-maui.md` | proposta | P0.1.31 |
| Spec Parametrização (.json) | `vault-maui/01_manifest/spec-parametrizacao-maui.json` | proposta | P0.1.31 |
| Índice Core | `vault-maui/00_core/indice-maui.md` | proposta | P0.1.31 |

---

## O que não assumir

- Não assumir que `status: proposta` significa incompleto — é o estado canônico dos normativos Maui v1.0.
- Não promover nenhum normativo para outro status sem Human Gate.
- Não executar P0.2, P0.3, P0.4 ou qualquer lote sem pedido explícito.
- Não executar P0.1.11 sem evidência de autorização explícita.
- Não misturar `vault-saara/` com `vault-maui/`.
- Não marcar instância como `current` sem filesystem/hash verificável.
- Não tratar o roadmap como evidência de execução — confirmar por Git/exec-reports.
- Não usar `panel/status.md` como fonte atual de estado; ele está defasado em P0.1.7.
- Não usar o trecho final de `indice-maui.md` que ainda diz "pós-P0.1.31" e "P0.1.32 pendente" como estado atual. A evidência mais recente é Git + exec-report P0.1.32 + memória marco.

---

## Instruções para instâncias sem filesystem (ChatGPT Handoff)

- Declarar conformidade como `unknown` — nunca `current`
- Usar este brief como contexto de retomada
- Gerar Update Request quando necessidade de alteração normativa for identificada
- Não escrever diretamente no corpus

---

## Próximos passos recomendados

**P0.2** — scripts de validação local:
- `maui_vault_health.py` — integridade do corpus
- `maui_validate_frontmatter.py` — validação de frontmatter
- `maui_validate_links.py` — links internos
- `maui_context_export.py` — geração de context packages

**P0.3** — operator packs:
- Claude Code (`CLAUDE.md` template)
- Codex (`AGENTS.md` template)
- ChatGPT Handoff (custom instructions + protocolo de handoff)

Aguardar decisão humana explícita. Não iniciar por inferência.

---

## Limites e riscos

- **C2 (aberto):** `system-prompt-maui.md §8` ainda referencia context brief pré-P0.1.26. Será atualizado em curadoria futura com Human Gate.
- **Índice Core:** `indice-maui.md` ainda contém uma seção final com estado "pós-P0.1.31" e "P0.1.32 pendente"; considerar defasado frente ao commit `538b441` e ao exec-report P0.1.32.
- **Painel de status:** `vault-maui/panel/status.md` está defasado em P0.1.7.
- **Working tree sujo:** este brief, o handoff pós-configuração-base, a memória de encerramento e a reconciliação do roadmap estavam sem commit no momento da verificação.
- **spec-funcionalidades-maui-v0-1.md:** placeholder; curadoria futura.
- **P0.3 depende de Configuração-base:** desbloqueado, mas ainda requer Human Gate e tarefa própria.

---

## F/I/H

### Fatos

- Configuração-base Maui completa em 2026-05-06.
- 19 artefatos normativos criados e sincronizados (commits `1f32776` a `538b441`).
- P0.3 e P0.4 desbloqueados.
- P0.1.11 não executada.

### Inferências

- Context brief pós-P0.1.32 (este documento) é mais atual que o anterior pós-P0.1.25.
- A próxima sessão provavelmente abordará P0.2 ou P0.3.

### Hipóteses

- Operator packs P0.3 seguirão estrutura do roadmap sem grandes revisões.
- Instanciação manual Maui permanecerá fora de escopo até P0.3+ completo.
