---
titulo: "Decisão — Claude Code instrução para gerar Context Brief Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: memoria_decisao
escopo: projeto_maui
confidencialidade: interna
deve_ser_considerado_em_context_brief: true
tags:
  - context-brief
  - procedimento
  - skill
  - claude-code
  - retomada
---

# Decisão — Claude Code instrução para gerar Context Brief Maui

## Resumo da decisão

Foi criado um procedimento operacional e uma skill para que Claude Code (e outros executores) saibam como gerar um `Maui Context Brief` sempre que solicitado. Os artefatos ensinam: seleção de fontes, ordem de leitura, regras de lacuna, separação F/I/H e critérios de qualidade.

## Arquivos criados

| Arquivo | Tipo | Finalidade |
| --- | --- | --- |
| `vault-maui/procedures/procedimento-gerar-context-brief.md` | Procedimento operacional | Referência completa: fontes, ordem, regras, template, validações |
| `vault-maui/skills/maui-context-brief/SKILL.md` | Skill compacta | Instrução de execução rápida para Claude Code e outros executores |
| `vault-maui/project-memories/2026-05-06-decisao-claude-code-gerar-context-brief.md` | Memória de decisão | Este arquivo |
| `vault-maui/exec-reports/submitted/2026-05-06-claude-code-context-brief-procedure.md` | Exec-report | Registro da tarefa de documentação |

## Regra operacional

Claude Code deve usar `vault-maui/procedures/procedimento-gerar-context-brief.md` como referência quando for gerar um Context Brief. A skill em `vault-maui/skills/maui-context-brief/SKILL.md` é a versão compacta para execução direta.

## Ordem de precedência ao gerar um brief

1. Git local e filesystem verificável
2. Exec-reports recentes (`vault-maui/exec-reports/submitted/`)
3. Inventários (`vault-maui/inventarios/`)
4. Memórias com `deve_ser_considerado_em_context_brief: true`
5. Handoffs recentes (`vault-maui/handoffs/`)
6. Context briefs atuais (`vault-maui/context-packages/current/`)
7. Roadmap e documentos core — apenas como referência estrutural

## Limites preservados

- P0.1.11 permanece não executada.
- Instanciação manual Maui não deve ser assumida como pronta.
- `Documentação/` não deve ser reaberta sem decisão humana explícita.
- `vault-maui/00_core/` não foi alterado nesta tarefa.
- Nenhuma etapa do roadmap foi executada.
- Sem filesystem/hash verificável, declarar `unknown`, nunca `current`.

## Próximos passos recomendados

1. Revisar e validar o procedimento e a skill com o usuário.
2. Usar este procedimento nas próximas retomadas e handoffs.
3. Atualizar o procedimento se novas regras operacionais forem decididas.
4. Considerar integrar a skill ao operator-pack de Claude Code quando este for criado.
