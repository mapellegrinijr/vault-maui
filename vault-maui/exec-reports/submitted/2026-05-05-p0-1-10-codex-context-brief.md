---
titulo: "Exec Report — P0.1.10 — Codex Context Brief sob demanda"
versao: "1.0"
status: submitted
data_criacao: 2026-05-05
idioma: pt-BR
tipo: exec_report
escopo: projeto_maui
fase: P0.1.10
---

## Objetivo

Instruir o Codex a criar um `Maui Context Brief` sob demanda quando o usuário solicitar preparação ou retomada de contexto para continuidade de tarefas no Maui.

## Arquivo de instruções Codex localizado

Arquivo escolhido: `vault-maui/00_core/regras-operacionais.md`.

Justificativa: é o único documento canônico existente que governa instruções para executores de codificação e cita explicitamente Codex; `vault-maui/operator-packs/codex/` existe, mas não contém arquivo-alvo.

## Alteração realizada

Adicionada a seção `Maui Context Brief sob demanda`, orientando o Codex a:

- criar um `Maui Context Brief` quando o usuário pedir por context brief, preparação de contexto, retomada de tarefa ou expressão equivalente;
- usar como referência primária `vault-maui/context-packages/templates/maui-context-brief.template.md`;
- salvar o brief instanciado preferencialmente em `vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<slug>.md`;
- consultar apenas fontes materialmente relevantes do corpus, memórias, adendos, insights, handoffs, exec-reports, review-reports, inventários e atualizações recentes;
- declarar lacunas documentais e pedir ao usuário o menor conjunto necessário quando faltar documento essencial;
- não inventar conteúdo, status, versões, hashes ou decisões.

## Existência do template

O template `vault-maui/context-packages/templates/maui-context-brief.template.md` existe e foi referenciado diretamente.

## Arquivos alterados/criados

- Alterado: `vault-maui/00_core/regras-operacionais.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-05-p0-1-10-codex-context-brief.md`

## Validações realizadas

- Localizados candidatos relacionados a Codex, instruções iniciais, operator pack e context package.
- Confirmado que `vault-maui/operator-packs/codex/` existe, mas não contém arquivo de instruções.
- Confirmado que `vault-maui/00_core/regras-operacionais.md` é o documento canônico existente para interação entre Saara e executores de codificação, incluindo Codex.
- Confirmado que `vault-maui/context-packages/templates/maui-context-brief.template.md` existe.
- Confirmado que a nova seção foi adicionada ao arquivo de instruções escolhido.
- Confirmado que a alteração ficou limitada ao arquivo de instruções e a este exec-report.

## Confirmação sobre `Documentação/`

Nenhum arquivo ou caminho dentro de `Documentação/` foi alterado, movido, renomeado ou removido nesta execução.

## Resultado

Aceito para revisão.

## Ressalvas

Não havia arquivo específico versionado dentro de `vault-maui/operator-packs/codex/`. Por isso, a instrução foi registrada no documento operacional canônico já existente para executores de codificação.

## Próximo passo recomendado

Quando o usuário solicitar retomada ou preparação de contexto, instanciar um `Maui Context Brief` usando o template canônico e salvar o resultado em `vault-maui/context-packages/current/`.
