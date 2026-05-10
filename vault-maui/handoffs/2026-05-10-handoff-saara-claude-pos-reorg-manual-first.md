---
titulo: "Handoff — Saara claude.ai pós reorg Project vs Runtime e pacote manual-first"
versao: "1.0"
status: ativo
data_criacao: 2026-05-10
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: saara_claude_code_local
destino_esperado: saara_claude_chat_7_1_1_pe
confidencialidade: interna
deve_ser_considerado_em_context_brief: true
referencias:
  - "vault-maui/status-project/STATUS-UPDATE-maui.md"
  - "vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md"
  - "vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md"
  - "vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md"
  - "vault-maui/status-project/RELATORIO-ATUALIZAR-INSTANCIAS-MANUAL-FIRST-2026-05-10.md"
  - "vault-maui/status-project/MIGRACAO-ESTRUTURA-2026-05-10.md"
  - "vault-maui/exec-reports/submitted/2026-05-10-p0-x-alinha-roadmap-e-core-apos-separacao-project-runtime.md"
  - "vault-maui/exec-reports/submitted/2026-05-10-p0-x-atualiza-procedure-context-brief-e-status-project.md"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/indice-maui.md"
  - "vault-maui/01_manifest/spec-parametrizacao-maui.json"
tags:
  - maui
  - handoff
  - saara
  - claude
  - reorganizacao
  - project-vs-runtime
  - manual-first
---

# Handoff — Saara claude.ai pós reorg Project vs Runtime e pacote manual-first

## Resumo executivo

- O vault Maui foi reorganizado em 2026-05-10 para separar artefatos de Project (gestação/implementação) de pastas reservadas a Runtime. Não há novos lotes do roadmap executados; a mudança é estrutural e documental.
- Configuração-base Maui segue concluída por evidência de P0.1.32 (commit `538b441`); estado posterior é apenas housekeeping (H0.x) e o pacote manual-first 2026-05-10.
- Foi gerado um pacote manual-first (status, context brief, handoff de sessão, exec-report, guia operacional) para que cada instância — incluindo esta de Saara em claude.ai — seja atualizada manualmente, sem dependência de integrações.
- A próxima decisão humana esperada continua sendo escolher entre P0.2 ou P0.3, ou pedir nova atualização manual-first. Nenhuma execução pode ocorrer por inferência.
- HEAD de referência registrado pelo pacote: `1d875e367f93645402b9eafdcba5e0f657d5a246` — `docs(project): alinhar roadmap e core à separação project vs runtime`. Working tree limpo na coleta.

## Finalidade deste handoff

Atualizar a instância Saara 7.1.1 + Prompt Engineering Elite que opera em claude.ai sobre:

1. a reorganização Project vs Runtime;
2. os novos paths canônicos e as pastas runtime reservadas;
3. a fonte corrente de status e o pacote mínimo de retomada;
4. o que está proibido executar/assumir;
5. o que muda no Domain Router e nas regras de Saara para o Maui depois desta reorg.

Este handoff não é configuração-base, não cria normativos, não promove status e não executa P0.2/P0.3/P0.4.

## O que mudou na estrutura do vault

### Princípio adotado

`vault-maui/` separa duas camadas dentro do mesmo corpus:

- **Project** — artefatos de gestação/implementação do Maui (vivos enquanto o Maui está sendo construído).
- **Runtime** — artefatos operacionais do Maui em uso (reservados; ainda sem operação).

Memória, status e roadmap foram divididos para refletir essa separação.

### Mapa de paths — antigo → novo

| Camada | Antigo | Novo / situação |
|---|---|---|
| Memória de gestação | `vault-maui/memorias/` (uso de Project) | `vault-maui/project-memories/` (Project) |
| Memória runtime | — | `vault-maui/memorias/` reservado para runtime, contém apenas README |
| Status do projeto | `vault-maui/status/STATUS-UPDATE-maui.md` | `vault-maui/status-project/STATUS-UPDATE-maui.md` |
| Status runtime | — | `vault-maui/status/` reservado para runtime, contém apenas README |
| Roadmap | `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md` | `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` |
| Painel | `vault-maui/panel/status.md` (qualquer leitura como status) | `vault-maui/panel/status.md` rebaixado a indexador de baixa confiança |
| Lista pastas/arquivos | `vault-maui/status/LISTA-PASTAS-E-ARQUIVOS-maui.md` | `vault-maui/status-project/LISTA-PASTAS-E-ARQUIVOS-maui.md` |

Detalhamento e contagem de referências atualizadas: `vault-maui/status-project/MIGRACAO-ESTRUTURA-2026-05-10.md`.

### Commits envolvidos

| Commit | Conteúdo |
|---|---|
| `f8b5120` | `chore(structure): separar project-memories e status-project; mover roadmap para project` |
| `9c76d62` | `docs(project): atualizar context brief + status-project para nova estrutura` |
| `1d875e3` | `docs(project): alinhar roadmap e core à separação project vs runtime` |

Exec-reports correspondentes:

- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-atualiza-procedure-context-brief-e-status-project.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-alinha-roadmap-e-core-apos-separacao-project-runtime.md`
- `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md`

### Atualizações em normativos

A reorg propagou-se nos seguintes documentos por substituição de paths e referências literais — sem promoção de status:

- `vault-maui/00_core/indice-maui.md`
- `vault-maui/00_core/regras-operacionais.md`
- `vault-maui/00_core/especificacao-completa-maui.md`
- `vault-maui/00_core/contrato-precedencia-maui.md`
- `vault-maui/00_core/principios-fundacionais-maui.md`
- `vault-maui/00_core/spec-memory-store-maui.md`
- `vault-maui/00_core/spec-capture-layer-maui.md`
- `vault-maui/00_core/spec-context-engineering-maui.md`
- `vault-maui/00_core/system-prompt-maui.md`
- `vault-maui/01_manifest/spec-parametrizacao-maui.json` (validado por `jq empty`)
- `vault-maui/procedures/procedimento-gerar-context-brief.md`
- `vault-maui/skills/maui-context-brief/SKILL.md`
- `vault-maui/context-packages/templates/maui-context-brief.template.md`
- `vault-maui/panel/status.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`

## Manual-first

Decisão registrada nesta sessão: atualização de instâncias Saara/Maui é manual-first.

- `vault-maui/` é a fonte canônica.
- O pacote mínimo para atualizar uma instância é: status corrente + context brief current + handoff da sessão.
- Não depender de integrações, automações ou MCP para essa atualização.
- Em conflito entre o que a instância acredita saber e o estado do vault, o vault prevalece.
- Em ausência de filesystem/hash verificável, declarar conformidade `unknown`, nunca `current`.

Guia operacional completo (Claude Projects, Claude Code, Codex, ChatGPT Handoff): `vault-maui/status-project/RELATORIO-ATUALIZAR-INSTANCIAS-MANUAL-FIRST-2026-05-10.md`.

## Estado atual confirmado por evidência

- Configuração-base Maui: concluída em P0.1.32. Evidência: `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco `vault-maui/project-memories/2026-05-06-marco-p0-1-32-revisao-integrada-maui.md` e commit `538b441`.
- Reorg Project vs Runtime: aplicada por `f8b5120` e estabilizada por `9c76d62` e `1d875e3`.
- Pacote manual-first: registrado em H0.y do roadmap e em exec-report 2026-05-10.
- HEAD de referência na coleta: `1d875e3`. Working tree limpo. Validações: `git status --porcelain` vazio; `vault-maui/status/` apenas README; `vault-maui/memorias/` apenas README; `jq empty vault-maui/01_manifest/spec-parametrizacao-maui.json` passou; sem execução de P0.2/P0.3/P0.4.
- Status `proposta` mantido em todos os normativos do `00_core/`. Sem promoção.
- P0.1.11 permanece não executada salvo evidência direta posterior.
- Instanciação manual Maui permanece não pronta.

## Pacote mínimo de leitura para Saara claude.ai

Ordem recomendada (parar quando o objetivo do turno estiver coberto):

1. Este handoff (`vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md`).
2. `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`.
3. `vault-maui/status-project/STATUS-UPDATE-maui.md`.
4. `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md`.
5. `vault-maui/status-project/RELATORIO-ATUALIZAR-INSTANCIAS-MANUAL-FIRST-2026-05-10.md` (apenas se for atualizar outra instância).
6. `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md`.
7. `vault-maui/00_core/contrato-precedencia-maui.md` e `vault-maui/00_core/principios-fundacionais-maui.md`.
8. `vault-maui/00_core/system-prompt-maui.md` e `vault-maui/00_core/indice-maui.md`.
9. `vault-maui/00_core/spec-parametrizacao-maui.md` e `vault-maui/01_manifest/spec-parametrizacao-maui.json`.
10. `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` (mapa de destino, não evidência).

Para retomada operacional sem reler tudo: itens 1–4 bastam.

## Domain Router e papéis (lembrete pós-P0.1.32)

- Prompt Engineering Elite é PKA obrigatória de primeira classe; lidera contrato textual/instrucional.
- Agent Engineering lidera integração sistêmica: agentes, tools, memória, RAG, MCP, distribuição, instanciação, captura, observabilidade, rollout.
- AI Solutions Architect lidera arquitetura-alvo, desenho, integração e trade-offs.
- Development Engineer lidera implementação, código, refatoração, testes, hardening.
- Written Comms Core lidera comunicação escrita, reescrita, SACCE.
- SAFe/Agile Master Elite permanece `proposta_condicional` — não ativar no Domain Router até owner + suíte T1-T8 + Human Gate.

Em tarefas híbridas prompt + agente, Prompt Engineering lidera o contrato textual; Agent Engineering lidera a integração sistêmica.

## Ações proibidas por inferência

- Não executar P0.2, P0.3, P0.4 ou qualquer etapa do roadmap sem pedido humano explícito.
- Não promover `status: proposta` de qualquer normativo Maui.
- Não tratar `vault-maui/panel/status.md` como fonte declarativa de estado; é apenas indexador.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` como fonte de Project; são pastas runtime reservadas.
- Não copiar integralmente arquivos Saara para Maui.
- Não alterar `vault-maui/00_core/` por conta deste handoff.
- Não declarar conformidade `current` sem filesystem/hash verificável; usar `unknown` quando faltar evidência.
- Não assumir instanciação manual Maui pronta.
- Não reabrir `Documentação/`.
- Não depender de integrações para aplicar este pacote — manual-first.

## Regras de Saara nesta continuidade

Aplicar Saara 7.1.1 + Prompt Engineering Elite normalmente, com os seguintes lembretes específicos:

- Compact-first, pt-BR, sem emojis em conteúdo técnico.
- F/I/H quando material; evitar elevar inferência a fato.
- Modo A para arquitetura/governança/agentes; Modo B/B1 para execução previsível.
- Profundidade mínima suficiente: D0 a D3 conforme risco/custo.
- Disclosure progressiva: L0 a L3 sob demanda; não abrir L2/L3 por hábito.
- Anti-alucinação e anti-complacência. Não prometer trabalho em background.
- Para retomada/status: usar Git e `vault-maui/status-project/STATUS-UPDATE-maui.md` antes de roadmap, painel ou memória.
- Para qualquer prompt executor (Codex/Claude Code) gerado a partir de Saara: validar estado real antes; declarar objetivo, escopo, fontes, restrições, validações antes/depois; exigir exec-report e commit quando houver escrita; Human Gate quando normativo.
- Para qualquer mudança em `vault-maui/00_core/`, `01_manifest/`, system prompt, princípios, precedência, PKAs, specs subsidiárias, parametrização, índice ou status: Human Gate explícito.

## Checklist de retomada para Saara claude.ai

- [ ] Ler este handoff por inteiro.
- [ ] Ler context brief 2026-05-10 e status-project current.
- [ ] Internalizar o mapa antigo→novo de paths.
- [ ] Confirmar que instância vai operar com `project-memories/` e `status-project/` como fontes de Project, e tratar `memorias/` e `status/` como reservadas.
- [ ] Atualizar resposta padrão de retomada para citar `status-project/STATUS-UPDATE-maui.md` e o context brief 2026-05-10.
- [ ] Em ambiente sem filesystem (claude.ai), declarar `status: unknown` para qualquer afirmação que dependa de hash, commit, working tree ou arquivo local não anexado.
- [ ] Não executar nenhuma etapa de P0.2/P0.3/P0.4 sem pedido humano.
- [ ] Quando o usuário pedir status corrente, partir do pacote mínimo (itens 1–4) e só aprofundar sob demanda.

## Riscos e ressalvas

- Saara em claude.ai opera sem filesystem direto; este handoff só prova o estado em que foi escrito. Estado futuro exige nova verificação.
- Documentos históricos podem citar `memorias/` e `status/` em sentido antigo (Project). Tratá-los como evidência temporal, não como status corrente.
- O painel pode divergir de `status-project/STATUS-UPDATE-maui.md`. Em divergência, prevalecem Git, exec-reports, status-project, handoffs e context brief current — nessa ordem.
- O roadmap permanece `status: proposta` e segue mapa de destino, não evidência operacional.

## F / I / H

### Fatos

- HEAD `1d875e367f93645402b9eafdcba5e0f657d5a246` registrado pelo pacote manual-first em 2026-05-10, com working tree limpo na coleta.
- `vault-maui/project-memories/`, `vault-maui/status-project/` e `vault-maui/project/roadmap/` existem como pastas canônicas de Project.
- `vault-maui/memorias/` e `vault-maui/status/` contêm apenas README e estão reservadas a runtime.
- `vault-maui/01_manifest/spec-parametrizacao-maui.json` validado por `jq empty`.
- Configuração-base Maui concluída em P0.1.32 (commit `538b441`).
- Existem três artefatos 2026-05-10 explicitamente datados: status-project STATUS-UPDATE, context brief current e handoff de sessão.

### Inferências

- O próximo passo recomendado, sem execução, é P0.2 (scripts/validations) ou P0.3 (operator packs), conforme prioridade humana — P0.2 reduz risco antes de P0.3 se o foco for validação executável.
- A reorg deve reduzir drift entre instâncias por estabilizar fontes canônicas e marcar pastas runtime como reservadas.

### Hipóteses

- Nenhum lote do roadmap foi executado por inferência durante a reorg ou o pacote manual-first; a checagem definitiva é por Git e por inspeção de `00_core/` quando a instância tiver acesso ao filesystem.
- A próxima decisão humana virá após esta atualização de instâncias.

## Próximo passo recomendado (sem executar)

- Quando o humano pedir avanço operacional: confirmar Human Gate explícito e escolha entre P0.2 e P0.3; partir do pacote mínimo desta sessão antes de propor qualquer prompt executor.
- Quando o humano pedir nova atualização manual-first: gerar novo trio (status-project, context brief current, handoff de sessão) seguindo o procedimento canônico em `vault-maui/procedures/procedimento-gerar-context-brief.md`.
