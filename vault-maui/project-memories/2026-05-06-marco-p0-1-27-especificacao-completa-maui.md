---
titulo: "Marco P0.1.27 — Especificação completa Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-27
  - especificacao-completa
  - configuracao-base
  - prompt-engineering
  - human-gate
deve_ser_considerado_em_context_brief: true
---

# Marco P0.1.27 — Especificação completa Maui

## Resumo

A P0.1.27 criou `vault-maui/00_core/especificacao-completa-maui.md` como documento normativo central da Configuração-base Maui, em `status: proposta`, sob Human Gate explícito.

## Documento criado

- `vault-maui/00_core/especificacao-completa-maui.md`

## Decisões normativas

- A especificação Maui referencia e respeita `principios-fundacionais-maui.md` e `contrato-precedencia-maui.md`.
- A ordem de precedência Maui permanece alinhada ao contrato P0.1.26.
- Roadmap continua sendo mapa de destino, não fonte única de status executado.
- `unknown` é obrigatório para ChatGPT/Handoff sem filesystem/hash verificável.
- Configuração-base deve preceder operator packs P0.3 e bootstrap/context packages P0.4.

## Relação com Saara como modelo

Foram usados como modelo estrutural e conceitual os arquivos Saara disponíveis em `../Saara/vault-saara/00_core/`, especialmente `especificacao-completa.md`, `system-prompt.md`, `principios-fundacionais.md`, `pka-prompt-engineering.md`, PKAs, specs subsidiárias, parametrização e índice.

O conteúdo foi adaptado para Maui. Esta etapa não copiou Saara integralmente nem alterou arquivos Saara.

## Prompt Engineering Elite

Prompt Engineering Elite foi registrado como domínio/PKA obrigatório planejado para Maui. A especificação declara sua responsabilidade por prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

Prompt Engineering não foi absorvido por Agent Engineering. Em tarefas híbridas, Prompt Engineering lidera contrato textual/instrucional e Agent Engineering lidera integração sistêmica e operacional.

## Limites

- Não criou system prompt Maui.
- Não criou PKAs Maui.
- Não criou specs subsidiárias Maui.
- Não criou parametrização ou índice Maui.
- Não criou operator packs.
- Não criou context packages finais.
- Não executou P0.1.11, P0.1.28 ou instanciação manual.
- Não promoveu `status: proposta`.

## Próximos passos

Executar P0.1.28 em tarefa separada, com Human Gate, para criar `vault-maui/00_core/system-prompt-maui.md` usando esta especificação, os princípios e o contrato de precedência como base.

## Riscos

- A especificação está em `status: proposta`; adoção plena depende de decisão posterior.
- System prompt e PKAs ainda ausentes mantêm instanciação manual bloqueada.
- Prompt Engineering Elite ainda precisa ser materializado como PKA Maui em P0.1.29.
- Roadmap pode precisar de reconciliação posterior para registrar a conclusão da P0.1.27.
