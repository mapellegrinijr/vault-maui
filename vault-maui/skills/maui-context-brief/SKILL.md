---
titulo: "Skill — maui-context-brief"
nome: maui-context-brief
versao: "1.0"
status: ativo
data_criacao: 2026-05-06
idioma: pt-BR
tipo: skill
escopo: projeto_maui
confidencialidade: interna
procedimento_referencia: "vault-maui/procedures/procedimento-gerar-context-brief.md"
---

# Skill — maui-context-brief

## Objetivo

Gerar um `Maui Context Brief` confiável e mínimo para viabilizar retomada segura de tarefas no projeto Maui. O brief descreve o estado atual verificável, as fontes consultadas, as lacunas, a separação F/I/H e o próximo passo recomendado.

## Quando usar

- Usuário pede: "gere o context brief", "prepare o contexto para retomada", "crie um brief para continuar".
- Antes de handoff entre sessões, agentes ou operadores.
- No início de uma tarefa que exija orientação de estado atual do projeto.

## Quando não usar

- Para executar etapas do roadmap.
- Para criar inventários, exec-reports ou planos.
- Para reabrir `Documentação/` ou alterar `vault-maui/00_core/`.
- Para fazer dump integral do corpus.
- Quando o objetivo for apenas registrar uma memória ou decisão.

## Inputs esperados

| Input | Obrigatório | Descrição |
| --- | --- | --- |
| Escopo ou tarefa-alvo | Sim | Ex.: "pós-P0.1.28", "retomada de P0.1.29", "handoff Saara". |
| Acesso ao filesystem | Desejável | Permite verificar git, exec-reports, inventários e memórias. |
| Arquivos anexados | Condicional | Necessários quando não há filesystem (ChatGPT, Claude sem repositório). |

## Fontes a consultar

Consultar nesta ordem:

1. `git status --short` e `git log --oneline -20`
2. `vault-maui/exec-reports/submitted/` — exec-reports mais recentes
3. `vault-maui/inventarios/` — diagnósticos e registros
4. `vault-maui/project-memories/` — apenas arquivos com `deve_ser_considerado_em_context_brief: true`
5. `vault-maui/handoffs/` — handoffs recentes
6. `vault-maui/context-packages/current/` — briefs anteriores relacionados
7. `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` — apenas como referência estrutural

## Passos

```
1. git status --short       → confirmar working tree
2. git log --oneline -20    → identificar commits recentes
3. Ler exec-reports recentes relevantes ao escopo
4. Ler inventários relevantes
5. Ler memórias com deve_ser_considerado_em_context_brief: true
6. Ler handoffs recentes
7. Ler context briefs atuais relacionados ao escopo
8. Identificar e declarar lacunas documentais
9. Preencher template canônico com F/I/H
10. Aplicar regra `unknown` para executores sem filesystem
11. Validar checklist de qualidade
12. Salvar em vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<escopo>.md
13. Commitar com mensagem: context: gera context brief <escopo>
```

## Output esperado

Arquivo salvo em:
```
vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<escopo>.md
```

Conteúdo mínimo:
- Frontmatter YAML válido
- Estado atual com evidências
- Fontes consultadas e ausentes
- Decisões fechadas relevantes
- Pendências e bloqueios
- O que não assumir
- Seção F/I/H
- Próximo passo recomendado

## Critérios de sucesso

- [ ] Brief salvo com nome canônico
- [ ] Fontes listadas, incluindo fontes ausentes
- [ ] F/I/H separados explicitamente
- [ ] `unknown` usado onde não há filesystem/hash verificável
- [ ] Nenhuma etapa do roadmap executada
- [ ] `Documentação/` não alterada
- [ ] `vault-maui/00_core/` não alterado
- [ ] Frontmatter YAML válido
- [ ] Working tree limpo após commit

## Restrições

- Não executar P0.1.11 ou qualquer fase do roadmap durante a geração.
- Não criar configuração-base, PKAs, specs subsidiárias, parametrização, índice, operator packs ou bootstrap.
- Não marcar instância (ChatGPT, Handoff) como `current` sem hash ou filesystem verificável.
- Não reabrir `Documentação/` sem decisão humana explícita.
- Não usar roadmap como fonte única de status executado.
- Não duplicar brief existente do mesmo escopo e data sem justificativa.
- Não transformar o brief em dump integral do corpus.

## Relação com o procedimento

O procedimento detalhado está em:
```
vault-maui/procedures/procedimento-gerar-context-brief.md
```

Esta skill é a instrução compacta de execução. Para dúvidas sobre regras, fontes, critérios ou edge cases, consultar o procedimento.
