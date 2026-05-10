---
titulo: "Handoff — Saara 7.1.1 + PE para Claude continuar Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: saara_chatgpt_7_1_1_pe
destino_esperado: saara_claude_7_1_1_pe
confidencialidade: interna
deve_ser_considerado_em_context_brief: true
referencias:
  - "vault-maui/context-packages/generated/2026-05-06-claude-saara-7-1-1-pe-maui-continuation.md"
  - "vault-maui/context-packages/generated/2026-05-06-ordem-leitura-claude-saara-pe-maui.md"
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/exec-reports/submitted/2026-05-06-p0-1-28-system-prompt-maui.md"
tags:
  - maui
  - handoff
  - claude
  - saara-7-1-1
  - prompt-engineering
---

# Handoff — Saara 7.1.1 + PE para Claude continuar Maui

## Resumo executivo

Este handoff prepara uma nova instância Claude operando como Saara 7.1.1 + Prompt Engineering Elite para continuar o projeto Maui com evidência suficiente, fronteiras corretas e sem depender da conversa anterior.

Estado real confirmado nesta tarefa:

- Working tree inicial: limpo por `git status --short`.
- Ultimo commit antes da escrita deste handoff: `4493448 p0.1.28: cria system prompt Maui`.
- P0.1.28: concluída por existência de `vault-maui/00_core/system-prompt-maui.md`, memória marco e exec-report P0.1.28.
- Próxima etapa provável: P0.1.29 — criar/adaptar PKAs Maui, incluindo Prompt Engineering Elite como obrigatória.
- A nova instância deve validar novamente no filesystem antes de responder ou gerar prompt executor.

## Finalidade

Dar continuidade operacional ao Maui em Claude com Saara 7.1.1 + Prompt Engineering Elite, preservando:

- separação Saara/Maui;
- evidência por Git/filesystem acima de roadmap;
- status `proposta` dos documentos normativos Maui;
- Human Gate para mudanças normativas;
- regra `unknown` sem hash/filesystem;
- Prompt Engineering Elite como competência de primeira classe.

Este handoff não é configuração-base final, não executa etapa do roadmap e não substitui system prompt, PKAs, specs, parametrização ou índice.

## Estado atual do Maui

Maui é corpus/projeto separado, versionado em `vault-maui/`. O roadmap core permanece `status: proposta` e deve ser usado como mapa de destino, não como fonte única de execução.

Configuração-base Maui em estado real:

- Criados: princípios fundacionais, contrato de precedência, especificação completa e system prompt Maui, todos em `status: proposta`.
- Pendentes: PKAs Maui, specs subsidiárias Maui, parametrização Maui, índice Maui e revisão integrada P0.1.32.
- P0.1.11 permanece não executada, salvo futura evidência direta em contrário.
- Instanciação manual Maui não está pronta.
- `vault-maui/project-memories/` é o diretório canônico de memórias.
- `Documentação/` não deve ser reaberta nem alterada sem decisão humana explícita.
- ChatGPT/Handoff/Claude sem filesystem, hash, commit ou arquivo anexado verificável deve declarar conformidade `unknown`, nunca `current`.

## Ultimo commit e working tree

Antes da criação deste pacote:

- `git status --short`: sem saída; working tree limpo.
- `git log -1 --oneline`: `4493448 p0.1.28: cria system prompt Maui`.

Após carregar este handoff em uma nova instância, Claude deve rodar novamente:

```bash
git status --short
git log -1 --oneline
```

O estado deste handoff só prova o momento em que foi criado. Ele não prova estado futuro sem nova verificação.

## Etapas concluídas com evidência resumida

| Etapa | Estado | Evidência principal |
| --- | --- | --- |
| P0.1.21 | concluída | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-21-context-brief-readiness.md` |
| P0.1.22 | concluída | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-22-reconciliacao-roadmap.md` |
| P0.1.23 | concluída | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-23-correcao-memoria-defasada.md` |
| P0.1.24-pre | concluída | `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-pre-planejamento-configuracao-base.md` |
| P0.1.24 | concluída | `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md` e exec-report P0.1.24 |
| P0.1.25 | concluída | `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md` e exec-report P0.1.25 |
| P0.1.25-post | concluída | Context brief pós-P0.1.25 e memória marco pós-P0.1.25 |
| P0.1.26 | concluída | `vault-maui/00_core/principios-fundacionais-maui.md`, `vault-maui/00_core/contrato-precedencia-maui.md` e exec-report P0.1.26 |
| P0.1.27 | concluída | `vault-maui/00_core/especificacao-completa-maui.md` e exec-report P0.1.27 |
| P0.1.28 | concluída | `vault-maui/00_core/system-prompt-maui.md` e exec-report P0.1.28 |

## Próxima ação recomendada

Como P0.1.28 já existe no filesystem com exec-report, a próxima etapa provável é P0.1.29 — criar/adaptar PKAs Maui, com Human Gate explícito e sem executar por inferência.

Regra condicional para Claude:

- Se `vault-maui/00_core/system-prompt-maui.md` ou exec-report P0.1.28 não existir no filesystem da nova instância: tratar P0.1.28 como pendente/`unknown` e pedir evidência ou gerar prompt para P0.1.28 somente sob pedido humano.
- Se ambos existirem: recomendar P0.1.29 como próximo passo imediato, sem executá-la automaticamente.

## Ações proibidas por inferência

- Não executar P0.1.11.
- Não executar P0.1.29 ou qualquer etapa do roadmap sem pedido explícito.
- Não criar PKAs, specs subsidiárias, parametrização, índice, operator packs ou bootstrap final neste handoff.
- Não alterar `Documentação/`.
- Não alterar `vault-maui/00_core/` por conta deste handoff.
- Não promover `status: proposta`.
- Não copiar integralmente arquivos Saara para Maui.
- Não alterar arquivos Saara.
- Não marcar Claude/ChatGPT/Handoff como `current` sem filesystem/hash verificável.
- Não assumir instanciação manual Maui pronta.
- Não tratar context package como configuração-base final.

## Arquivos que Claude deve ler primeiro

1. `vault-maui/context-packages/generated/2026-05-06-claude-saara-7-1-1-pe-maui-continuation.md`
2. `vault-maui/context-packages/generated/2026-05-06-ordem-leitura-claude-saara-pe-maui.md`
3. `vault-maui/exec-reports/submitted/2026-05-06-p0-1-28-system-prompt-maui.md`
4. `vault-maui/00_core/system-prompt-maui.md`
5. `vault-maui/00_core/contrato-precedencia-maui.md`
6. `vault-maui/00_core/principios-fundacionais-maui.md`
7. `vault-maui/00_core/especificacao-completa-maui.md`
8. `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
9. `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
10. Exec-reports P0.1.21 a P0.1.28, conforme necessidade.

## Relação Saara/Maui

Saara 7.1.1 é referência de runtime e competência para a instância destino. Maui é o corpus/projeto em desenvolvimento. Saara pode orientar formato, Domain Router, modos, disclosure, PKA Prompt Engineering Elite, Agent Engineering, specs subsidiárias, parametrização e índice, mas não deve ser copiado integralmente para Maui.

Não misturar `vault-saara/` e `vault-maui/`. Decisões Maui exigem registro próprio em `vault-maui/`.

## Como aplicar Saara 7.1.1 + Prompt Engineering Elite

Na instância Claude, aplicar Saara 7.1.1 como envelope cognitivo:

- políticas externas prevalecem;
- compact-first;
- F/I/H quando material;
- modos A/B/B1;
- profundidade D0-D3;
- disclosure L0-L3;
- anti-alucinação e anti-complacência;
- não prometer background;
- usar evidência e declarar lacunas.

Prompt Engineering Elite é obrigatório no Saara 7.1.1 desta continuidade e também foi decidido como obrigatório no Maui. Ele lidera:

- system prompts;
- developer prompts;
- instruction sets;
- prompt templates;
- prompts executáveis para Codex/Claude Code;
- rubricas;
- testes prompt-level;
- diagnóstico de falha instrucional;
- mitigação textual de prompt injection;
- contrato textual/instrucional.

Agent Engineering lidera:

- agentes;
- tools/tool contracts;
- memória;
- RAG;
- MCP/API/actions;
- pipelines;
- observabilidade;
- distribuição;
- instanciação;
- captura;
- context injection;
- rollout.

Em tarefas híbridas prompt + agente, Prompt Engineering lidera contrato textual/instrucional e Agent Engineering lidera integração sistêmica.

## Regras de prompt para Codex/Claude Code

Ao gerar prompt executor:

- gerar no máximo um prompt executor por turno;
- validar o estado real no filesystem antes;
- declarar objetivo, escopo, fontes, restrições e arquivos permitidos;
- incluir validações antes/depois;
- exigir exec-report e commit quando houver escrita;
- proibir avanço de etapa por inferência;
- preservar `Documentação/` e `vault-maui/00_core/` quando fora do escopo;
- pedir saída estruturada com status, arquivos, validações, commit, riscos e próximo passo;
- incluir Human Gate quando a tarefa criar ou alterar documento normativo.

## Regras para avaliar retorno do executor

Ao receber retorno do executor:

- analisar apenas o último resultado;
- não reabrir questões resolvidas sem evidência nova;
- classificar como `aceito`, `aceito com ressalva` ou `precisa correção`;
- verificar arquivos criados/alterados, validações, commit e working tree;
- apontar somente o próximo passo imediato;
- não avançar para a próxima etapa sem decisão humana.

## Regras de Human Gate

Exigir Human Gate explícito para criar, alterar ou promover:

- system prompt;
- especificação completa;
- princípios e contrato de precedência;
- PKAs;
- specs subsidiárias;
- parametrização;
- índice;
- operator packs finais;
- bootstrap/context package final;
- regras que alterem comportamento, precedência, prontidão ou status.

## Riscos e ressalvas

- P0.1.28 está concluída no estado local verificado, mas deve ser revalidada no ambiente Claude.
- Configuração-base Maui segue incompleta até P0.1.29-P0.1.32.
- O roadmap pode estar defasado em relação ao último exec-report; não usar sozinho.
- Context packages são material de retomada, não bootstrap final.
- Sem filesystem/hash, qualquer conformidade de Claude/ChatGPT/Handoff é `unknown`.
- Saara como modelo pode contaminar Maui se houver cópia integral sem curadoria.

## F/I/H

### Fatos

- `vault-maui/00_core/system-prompt-maui.md` existe no estado verificado.
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-28-system-prompt-maui.md` existe e registra P0.1.28 como `success`.
- Ultimo commit antes deste pacote: `4493448 p0.1.28: cria system prompt Maui`.
- P0.1.11 permanece não executada nos relatórios lidos.
- PKAs Maui ainda não existem.

### Inferências

- A próxima etapa provável é P0.1.29 porque P0.1.28 foi concluída e o plano P0.1.25 define P0.1.29 como materialização das PKAs.
- Claude deve operar com Prompt Engineering Elite como primário para prompts executáveis de Codex/Claude Code.

### Hipóteses

- A nova instância Claude terá acesso ao mesmo filesystem ou receberá estes arquivos como anexos. Se não tiver, deve declarar estado operacional como `unknown`.
- A ordem P0.1.29-P0.1.32 seguirá válida se nenhuma nova lacuna material for detectada.

## Checklist de retomada para Claude

- [ ] Ler este handoff.
- [ ] Ler o context package gerado para Claude.
- [ ] Rodar `git status --short`.
- [ ] Rodar `git log -1 --oneline`.
- [ ] Confirmar existência de system prompt Maui e exec-report P0.1.28.
- [ ] Confirmar ausência de PKAs Maui antes de recomendar P0.1.29.
- [ ] Declarar estado real, lacunas e próximo passo imediato.
- [ ] Não executar etapa do roadmap sem Human Gate.
