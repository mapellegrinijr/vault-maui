---
titulo: "Exec-report — P0.1.26: princípios e precedência Maui"
versao: "1.0"
status: submitted
data_execucao: 2026-05-06
idioma: pt-BR
tipo: exec_report
fase: "P0.1.26"
resultado: success
escopo: projeto_maui
---

# Exec-report — P0.1.26: princípios e precedência Maui

## Resumo

A P0.1.26 definiu a base normativa inicial da Configuração-base Maui, criando documentos de princípios fundacionais e contrato de precedência operacional. A tarefa foi executada com escrita controlada e Human Gate explícito.

Não foram criados system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs ou context packages finais.

## Arquivos lidos

- `vault-maui/context-packages/current/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md`
- `vault-maui/memorias/2026-05-06-marco-pos-p0-1-25-configuracao-base-maui.md`
- `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
- `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
- `vault-maui/00_core/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/00_core/arquitetura-maui-v0-2.md`
- `vault-maui/00_core/spec-funcionalidades-maui-v0-1.md`
- `vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md`
- `vault-maui/00_core/regras-operacionais.md`
- `vault-maui/01_manifest/README.md`
- `vault-maui/memorias/2026-05-06-decisao-configuracao-base-maui-prompt-engineering.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-21-context-brief-readiness.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-22-reconciliacao-roadmap.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-23-correcao-memoria-defasada.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-pre-planejamento-configuracao-base.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-diagnostico-configuracao-base.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-25-plano-configuracao-base.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-25-post-marco-context-brief.md`

## Arquivos criados/alterados

- Criado: `vault-maui/00_core/principios-fundacionais-maui.md`
- Criado: `vault-maui/00_core/contrato-precedencia-maui.md`
- Criado: `vault-maui/memorias/2026-05-06-marco-p0-1-26-principios-precedencia-maui.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-06-p0-1-26-principios-precedencia-maui.md`

Nenhum arquivo em `Documentação/` foi alterado.

O roadmap não foi alterado nesta tarefa. Uma reconciliação posterior pode registrar a conclusão da P0.1.26 sem promover `status: proposta`.

## Validações executadas

- `git status --short` antes da tarefa: working tree limpo.
- Busca por duplicidade de `p0-1-26`, `principios-fundacionais-maui` e `contrato-precedencia-maui`: nenhum equivalente encontrado antes da escrita.
- Confirmação de existência do plano P0.1.25.
- Confirmação de existência da memória e context brief pós-P0.1.25.
- Leitura de documentos core e manifest existentes.
- Validação de frontmatter/YAML dos arquivos criados.
- Verificação manual dos caminhos citados.
- Verificação de ausência de alterações em `Documentação/`.
- Verificação de que artefatos fora do escopo não foram criados.

## Decisões aplicadas

- Criar princípios fundacionais Maui em `status: proposta`.
- Criar contrato de precedência Maui em `status: proposta`.
- Definir `precedencia: 2` para contrato de precedência e `precedencia: 3` para princípios fundacionais.
- Registrar `unknown` como estado obrigatório para ChatGPT/Handoff sem filesystem/hash verificável.
- Preservar Prompt Engineering Elite como competência obrigatória e separada de Agent Engineering.
- Manter Saara e Maui separados, com Saara apenas como referência curada.
- Não atualizar roadmap por padrão nesta tarefa.

## Human Gate aplicado

O usuário autorizou explicitamente a P0.1.26 como etapa para definir princípios e contrato de precedência Maui. Essa autorização foi tratada como Human Gate limitado à criação dos dois documentos normativos iniciais.

O Human Gate desta tarefa não autorizou promoção de status geral, criação de system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs, context packages finais, P0.1.11, P0.1.27 ou instanciação manual.

## Riscos remanescentes

- Os documentos normativos criados estão em `status: proposta`; adoção operacional plena requer decisão posterior.
- A Configuração-base Maui continua incompleta até a criação dos demais artefatos planejados.
- Prompt Engineering Elite ainda não está materializada como PKA Maui.
- System prompt e especificação completa ainda estão ausentes.
- Roadmap ainda pode exigir reconciliação posterior para registrar P0.1.26 como concluída.

## Status final

success

## Próximo passo recomendado

Executar P0.1.27 em tarefa separada, com Human Gate, para criar a especificação completa Maui baseada nos princípios e no contrato de precedência. Não executar P0.1.11 nem instanciação manual por inferência.
