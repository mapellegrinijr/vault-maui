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

O Context Brief é artefato de Project, não de runtime. Status corrente do projeto vem de `vault-maui/status-project/STATUS-UPDATE-maui.md`.

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
| Status corrente do projeto | Sim | `vault-maui/status-project/STATUS-UPDATE-maui.md` quando houver filesystem; anexo quando não houver. |

## Fontes a consultar

Consultar nesta ordem:

1. `git status --short` e `git log --oneline -20`
2. `vault-maui/status-project/STATUS-UPDATE-maui.md` — status vivo do projeto
3. `vault-maui/context-packages/current/` — context brief atual ou briefs relacionados
4. `vault-maui/handoffs/` — handoff mais recente relevante
5. `vault-maui/exec-reports/submitted/` — exec-report mais recente relevante
6. `vault-maui/project-memories/` — histórico de projeto; usar arquivos com `deve_ser_considerado_em_context_brief: true`
7. `vault-maui/00_core/` e `vault-maui/01_manifest/` — contrato do corpus quando necessário ao escopo
8. `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` — apenas como referência estrutural

## Passos

```
1. git status --short       → confirmar working tree
2. git log --oneline -20    → identificar commits recentes
3. Ler vault-maui/status-project/STATUS-UPDATE-maui.md
4. Ler context brief atual ou relacionado
5. Ler handoff recente relevante
6. Ler exec-report recente relevante
7. Ler memórias de projeto com deve_ser_considerado_em_context_brief: true
8. Ler contrato do corpus em 00_core/ + 01_manifest/ quando necessário
9. Identificar e declarar lacunas documentais
10. Preencher template canônico com F/I/H
11. Aplicar regra `unknown` para executores sem filesystem
12. Validar checklist de qualidade
13. Salvar em vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<escopo>.md
14. Commitar com mensagem: context: gera context brief <escopo>
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
- Não usar `vault-maui/panel/status.md` como fonte de estado; é indexador de baixa confiança.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` como fontes de Project antes do runtime Maui operar.
- Não duplicar brief existente do mesmo escopo e data sem justificativa.
- Não transformar o brief em dump integral do corpus.

## Regra de evidência e compactação

- Status executado exige Git, exec-report, handoff verificável ou arquivo presente no filesystem.
- Painel e roadmap não provam execução.
- Não copiar texto longo das fontes; sintetizar somente decisões, pendências, riscos e próximos passos materialmente necessários.

## Relação com o procedimento

O procedimento detalhado está em:
```
vault-maui/procedures/procedimento-gerar-context-brief.md
```

Esta skill é a instrução compacta de execução. Para dúvidas sobre regras, fontes, critérios ou edge cases, consultar o procedimento.
