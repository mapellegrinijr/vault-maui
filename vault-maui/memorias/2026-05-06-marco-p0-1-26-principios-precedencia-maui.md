---
titulo: "Marco P0.1.26 — Princípios e precedência Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-26
  - principios
  - precedencia
  - configuracao-base
  - prompt-engineering
  - human-gate
deve_ser_considerado_em_context_brief: true
---

# Marco P0.1.26 — Princípios e precedência Maui

## Resumo

A P0.1.26 criou a base normativa inicial da Configuração-base Maui: princípios fundacionais e contrato de precedência operacional. A criação foi feita sob Human Gate explícito e com escopo limitado.

## Documentos criados

- `vault-maui/00_core/principios-fundacionais-maui.md`
- `vault-maui/00_core/contrato-precedencia-maui.md`

## Decisões normativas tomadas

- Maui é corpus/projeto separado do Saara.
- Saara pode orientar conceitualmente, mas não deve ser copiado integralmente sem curadoria e Human Gate.
- Configuração-base deve preceder operator packs e bootstrap/context packages finais.
- Mudanças normativas exigem Human Gate.
- Estados sem filesystem/hash verificável devem usar `unknown`.
- Prompt Engineering Elite é competência obrigatória do Maui.
- Prompt Engineering e Agent Engineering têm fronteiras distintas e complementares.
- Roadmap é mapa de destino, não fonte única de status executado.

## Limites

- Não executou P0.1.11.
- Não executou P0.1.27.
- Não criou system prompt Maui.
- Não criou especificação completa Maui.
- Não criou ou adaptou PKAs Maui.
- Não criou specs subsidiárias, parametrização ou índice core.
- Não criou operator packs ou context packages finais.
- Não promoveu `status: proposta`.
- Não assumiu instanciação manual pronta.

## Próximos passos

Executar P0.1.27 em tarefa separada, com Human Gate, para criar a especificação completa Maui usando os princípios e o contrato de precedência como base.

## Riscos

- Os documentos criados estão em `status: proposta`; uso como contrato ativo exige decisão humana posterior.
- A Configuração-base continua incompleta até P0.1.32 ou revisão equivalente.
- Prompt Engineering Elite ainda precisa ser materializado como PKA Maui em etapa futura.
- Futuras instâncias podem confundir princípios/precedência com system prompt completo; essa inferência deve ser bloqueada.
