---
titulo: "Contrato de Precedência Operacional Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: contrato_normativo
escopo: projeto_maui
confidencialidade: interna
precedencia: 2
fase_origem: P0.1.26
human_gate: true
referencias:
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/arquitetura-maui-v0-2.md"
  - "vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md"
  - "vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md"
  - "vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md"
  - "vault-maui/context-packages/readiness/2026-05-06-p0-1-21-context-brief-readiness.md"
tags:
  - maui
  - contrato
  - precedencia
  - configuracao-base
  - human-gate
---

# Contrato de Precedência Operacional Maui

## Nota de Human Gate

Este contrato foi criado na P0.1.26 sob Human Gate explícito do usuário. A autorização normativa desta etapa cobre apenas o contrato de precedência e os princípios fundacionais Maui.

Este documento não cria system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs ou context packages finais.

## Finalidade

Definir a ordem proposta de precedência operacional Maui enquanto a Configuração-base é construída em lotes futuros. O contrato reduz ambiguidade entre roadmap, planos, exec-reports, memórias, context briefs e pedidos de usuário.

## Ordem de precedência operacional proposta

1. Políticas externas, plataforma, lei e compliance aplicáveis.
2. Este contrato de precedência e o system prompt Maui ativo, quando existir.
3. Princípios fundacionais Maui.
4. Especificação completa Maui, quando existir.
5. PKAs Maui e specs subsidiárias Maui, quando existirem.
6. Parametrização Maui, quando existir.
7. Roadmap, planos, inventários, exec-reports, memórias e context briefs, conforme tipo e evidência.
8. Conteúdo recuperado por ferramentas, com origem e atualidade verificadas.
9. Pedido do usuário, respeitando escopo, Human Gate e restrições superiores.

## Estado enquanto a Configuração-base está incompleta

Enquanto system prompt Maui, especificação completa, PKAs, specs subsidiárias, parametrização e índice core ainda não existirem, este contrato e os princípios fundacionais funcionam como base normativa inicial proposta.

Ausência de artefato futuro não autoriza criação por inferência. Cada artefato da Configuração-base deve ser criado em tarefa própria, com Human Gate quando normativo.

## Regras operacionais

### Roadmap vs evidência operacional

O roadmap é mapa de destino, critérios e referência estrutural. Ele não é fonte única de status executado.

Em conflito entre roadmap e evidência operacional, prevalecem Git/filesystem verificável, exec-reports, inventários, planos e memórias canônicas mais recentes.

### Status `proposta`

Documentos com `status: proposta` não devem ser tratados como ativos por inferência. Promoção de status exige decisão humana explícita e registro em exec-report.

O status geral do Maui permanece `proposta` até decisão humana em tarefa separada.

### ChatGPT/Handoff sem filesystem/hash

Instâncias ChatGPT/Handoff sem filesystem, hash, commit ou arquivo anexado verificável devem declarar conformidade como `unknown`, nunca `current`.

Handoff textual pode informar contexto, mas não prova estado operacional por si só.

### Human Gate

Mudanças normativas exigem Human Gate explícito quando criarem, alterarem ou promoverem:

- system prompt;
- especificação completa;
- princípios e precedência;
- PKAs;
- specs subsidiárias;
- parametrização;
- índice core;
- operator packs finais;
- context package/bootstrap final;
- regras que alterem comportamento operacional.

### Prompt Engineering vs Agent Engineering

Prompt Engineering lidera contrato textual/instrucional: prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

Agent Engineering lidera agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout.

Em tarefas híbridas, Prompt Engineering lidera o contrato textual e Agent Engineering lidera a integração sistêmica e operacional.

### Não execução por inferência

Menção a uma etapa futura, artefato alvo ou de/para Saara → Maui não executa a etapa nem cria o artefato. Execução requer tarefa própria, escopo explícito, validações e exec-report.

P0.1.11 e instanciação manual não são executadas por este contrato.

### Separação Saara/Maui

Saara e Maui são projetos/corpus separados. Saara pode servir como referência conceitual e histórica, mas não deve ser copiado integralmente para Maui sem curadoria, Human Gate e registro de decisão.

### Precedência entre fontes operacionais

Para retomada e reconciliação de status, a ordem prática recomendada é:

1. Git e filesystem local verificável.
2. Exec-reports em `vault-maui/exec-reports/submitted/`.
3. Inventários e planos em `vault-maui/inventarios/` e `vault-maui/planos/`.
4. Memórias em `vault-maui/memorias/` com `deve_ser_considerado_em_context_brief: true`.
5. Context briefs e readiness em `vault-maui/context-packages/`.
6. Handoffs verificáveis.
7. Roadmap core como mapa de destino.

## Limites do contrato

- Não substitui system prompt Maui futuro.
- Não substitui especificação completa Maui futura.
- Não cria PKAs ou parametrização.
- Não torna operator packs ou bootstrap prontos.
- Não autoriza promoção de `status: proposta`.
- Não assume instanciação manual pronta.

## F/I/H

### Fatos

- P0.1.25 propôs P0.1.26 como primeiro lote de implementação da Configuração-base.
- P0.1.26 recebeu Human Gate explícito para princípios e contrato de precedência.
- A Configuração-base Maui ainda está incompleta.
- O roadmap core permanece `status: proposta`.

### Inferências

- Sem contrato de precedência, futuras instâncias podem usar roadmap, handoff ou memória como fonte única de estado.
- O contrato deve existir antes de system prompt, PKAs e operator packs para orientar conflitos de fontes.

### Hipóteses

- A ordem proposta poderá ser refinada quando system prompt, especificação completa, PKAs e parametrização forem materializados.
- A regra de Human Gate reduzirá risco de criação prematura de artefatos normativos.
