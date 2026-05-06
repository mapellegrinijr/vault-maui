---
titulo: "Marco P0.1.28 — System prompt Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-28
  - system-prompt
  - configuracao-base
  - prompt-engineering
  - human-gate
deve_ser_considerado_em_context_brief: true
---

# Marco P0.1.28 — System prompt Maui

## Resumo

A P0.1.28 criou `vault-maui/00_core/system-prompt-maui.md` como contrato runtime inicial do Maui, em `status: proposta`, sob Human Gate explícito do usuário.

## Documento criado

- `vault-maui/00_core/system-prompt-maui.md`

## Decisões runtime

- Maui é definido pelo corpus versionado em `vault-maui/`, não por backend, ferramenta, MCP, painel, operador ou fornecedor.
- Políticas externas, plataforma, lei, segurança e compliance prevalecem.
- O system prompt referencia princípios fundacionais, contrato de precedência e especificação completa Maui.
- A Configuração-base permanece `status: proposta` enquanto faltarem PKAs, specs subsidiárias, parametrização, índice e revisão integrada.
- O Context Brief pós-P0.1.25 segue como referência de retomada até haver Configuração-base completa, reconciliado com Git/filesystem e exec-reports mais recentes.
- `vault-maui/memorias/` segue como diretório canônico de memórias.
- ChatGPT/Handoff sem filesystem/hash verificável deve declarar `unknown`, nunca `current`.

## Relação com Saara como modelo

Foram usados como modelo estrutural e conceitual os arquivos Saara vigentes disponíveis em `../Saara/vault-saara/00_core/`, especialmente `system-prompt.md`, `especificacao-completa.md`, `principios-fundacionais.md`, `pka-prompt-engineering.md`, PKAs, specs subsidiárias, parametrização e índice.

O conteúdo foi adaptado para Maui, sem cópia integral e sem alterar arquivos Saara. Saara permanece referência/modelo; Maui permanece corpus/projeto separado.

## Prompt Engineering Elite

Prompt Engineering Elite foi incluído no Domain Router Maui planejado como domínio obrigatório. O system prompt declara que Prompt Engineering lidera prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

Agent Engineering permanece responsável por integração sistêmica, agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, captura e rollout. Em tarefas híbridas, ambos se aplicam.

## Limites

- Não criou PKAs Maui.
- Não criou specs subsidiárias Maui.
- Não criou parametrização ou índice Maui.
- Não criou operator packs.
- Não criou bootstrap/context packages finais.
- Não executou P0.1.11, P0.1.29, P0.1.30, P0.1.31 ou instanciação manual.
- Não promoveu `status: proposta`.
- Não alterou `Documentação/`.
- Não marcou ChatGPT/Handoff como `current`.

## Próximos passos

1. Executar P0.1.29 para materializar PKAs Maui, incluindo Prompt Engineering Elite como obrigatória.
2. Executar P0.1.30 para specs subsidiárias Maui.
3. Executar P0.1.31 para parametrização e índice Maui.
4. Executar P0.1.32 para revisão integrada antes de P0.3/P0.4.

## Riscos

- O system prompt está em `status: proposta`; adoção operacional plena depende de decisão posterior.
- PKAs Maui ainda ausentes podem limitar o detalhamento de IO, quality gates e limites por domínio.
- Specs, parametrização e índice ainda pendentes mantêm a Configuração-base incompleta.
- Roadmap pode precisar de reconciliação posterior para registrar a conclusão da P0.1.28 sem promover status geral.
