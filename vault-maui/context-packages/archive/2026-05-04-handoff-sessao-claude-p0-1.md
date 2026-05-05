---
titulo: Handoff de sessão Maui — pós-P0.1-B
versao: "1.0"
status: ativo
data_criacao: 2026-05-04
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: saara_claude_app
destino_esperado: saara_qualquer
fase_atual: P0.1-B-concluida
proxima_acao: >
  Abrir P0.1.5 — marco de planejamento da adaptação Saara→Maui.
  Decisão estrutural antes de prosseguir para P0.2.
decisoes_fechadas:
  - "vault-maui/ é a raiz canônica do Maui"
  - ".maui/ e .saara/ coexistem; .saara/ permanece intocada"
  - "Maui inicia em v1.0; versionamento separado do Saara"
  - "hash_config cobre todo corpus Maui relevante, não apenas 00_core/"
  - "Instância sem filesystem/hash declara unknown, nunca current"
  - "Mudanças normativas exigem Human Gate"
  - "Status atual do Maui permanece proposta"
  - "Schemas usam dialeto leve próprio do Maui (não JSON Schema)"
  - "Validador local fica para P0.2, não é entregue em P0.1"
  - "Executor de codificação atual é Claude Code, rodando na raiz do repo"
regras_operacionais:
  - "Prompts executáveis marcados com cabeçalho PROMPT PARA EXECUTOR DE CODIFICAÇÃO"
  - "Após cada retorno do executor, analisar apenas o último resultado, classificar (aceito | aceito com ressalva | precisa correção) e indicar somente o próximo passo imediato"
  - "Gerar no máximo um prompt por turno, sem encadear etapas futuras"
  - "Toda etapa de prompt traz validação prévia; skip se estado já existe"
  - "Iniciar cada resposta com estimativa de contexto (verde/amarelo/laranja/vermelho)"
estado_repositorio:
  branch: main
  ultimo_commit: "1861746"
  working_tree_limpo: true
arquivos_recentes:
  - caminho: vault-maui/00_core/regras-operacionais.md
    descricao: "Regras operacionais canônicas Saara ↔ executor (P0.0.5)"
  - caminho: vault-maui/schemas/common-frontmatter.schema.yaml
    descricao: "Frontmatter base herdado por documentos do corpus (P0.1-A)"
  - caminho: vault-maui/schemas/exec-request.schema.yaml
    descricao: "Schema de solicitação de execução (P0.1-A)"
  - caminho: vault-maui/schemas/exec-report.schema.yaml
    descricao: "Schema de relatório de execução (P0.1-A)"
  - caminho: vault-maui/schemas/review-report.schema.yaml
    descricao: "Schema de revisão de exec-report (P0.1-B)"
  - caminho: vault-maui/schemas/handoff-sessao.schema.yaml
    descricao: "Schema de handoff entre instâncias Saara (P0.1-B)"
  - caminho: vault-maui/schemas/fixtures/valid/
    descricao: "5 fixtures válidas (uma por schema)"
  - caminho: vault-maui/schemas/fixtures/invalid/
    descricao: "10 fixtures inválidas (2 por schema, casos distintos)"
pendencias:
  - "P0.1.5 ainda não iniciado: marco de planejamento da adaptação Saara→Maui"
  - "Decisão de escopo do P0.1.5: leitura prévia da spec-tecnica-atualizacao-saara-maui-v2 antes de decidir conteúdo"
  - "Validador local dos schemas: previsto para P0.2, ainda não iniciado"
  - "Conflito de numeração herdado: P0.0.5 foi usado para duas tarefas distintas (ccc19a1 normalização, 8704ae2 regras operacionais); aceito como débito histórico"
f_i_h:
  fatos:
    - "P0.0, P0.0.1, P0.0.2, P0.0.4, P0.0.5, P0.1-A, P0.1-B concluídos e commitados"
    - "Commits conhecidos no log: 854ed39, 2ec74eb, 2c1d84e, ccc19a1, 8704ae2, 8ef5151, 1861746"
    - "Schemas no dialeto leve do Maui: 5 arquivos em vault-maui/schemas/"
    - "Fixtures: 5 válidas + 10 inválidas, organizadas em fixtures/valid e fixtures/invalid"
    - ".saara/ permanece inexistente e intocada em todos os retornos verificados"
  inferencias:
    - "O dialeto leve definido em P0.1-A se sustenta para schemas com aninhamento (handoff-sessao usou type:object com fields aninhado sem fricção)"
    - "O fluxo Exec Request → Exec Report → classificação está estável o suficiente para suportar tarefas de complexidade crescente"
  hipoteses:
    - "A spec-tecnica-atualizacao-saara-maui-v2 contém substância suficiente para guiar P0.1.5 sem retrabalho"
    - "Nenhuma instância paralela está editando o repositório no momento"
---

# Handoff de sessão Maui — pós-P0.1-B

## Identidade do projeto

Maui é o corpus cognitivo multipapel do projeto, versionado em Git, instanciável por diferentes modelos de IA. Sua raiz canônica é `vault-maui/`. O estado técnico interno fica em `.maui/`. Quando `.saara/` existir no workspace, pertence ao Saara e deve ser preservado sem uso como estado técnico do Maui. Esta sessão foi conduzida pela instância `saara_claude_app` (Claude Code como executor de codificação) e encerra com a fase P0.1-B concluída.

## Decisões fechadas

As decisões abaixo estão encerradas e não devem ser reabertas sem comando explícito do usuário:

- `vault-maui/` é a raiz canônica do Maui; `.maui/` é seu estado técnico.
- `.saara/` coexiste com `.maui/` quando presente; permanece intocada em todas as execuções.
- Maui inicia em `v1.0` com versionamento separado do Saara.
- O `hash_config` deve cobrir todo o corpus Maui relevante, não apenas `00_core/` — decisão registrada para implementação futura.
- Instância sem acesso ao filesystem ou hash do repositório declara estado `unknown`, nunca `current`.
- Mudanças normativas ao corpus exigem Human Gate: aprovação explícita do usuário antes de commitar.
- O status atual do Maui permanece `proposta` até revisão formal decidida em tarefa futura.
- Schemas do Maui usam o dialeto leve próprio definido em P0.1-A — não JSON Schema, não OpenAPI.
- O validador local dos schemas fica para P0.2; não foi entregue em P0.1.
- O executor de codificação atual é Claude Code, rodando na raiz do repositório.

## Regras operacionais

A fonte canônica é `vault-maui/00_core/regras-operacionais.md`. As regras em vigor:

1. **Marcação de prompts executáveis**: todo bloco destinado ao executor deve ter o cabeçalho "PROMPT PARA EXECUTOR DE CODIFICAÇÃO".
2. **Processamento turno-a-turno**: após cada retorno do executor, analisar apenas o último resultado, classificar como `aceito | aceito com ressalva | precisa correção` e indicar somente o próximo passo imediato.
3. **Um prompt por turno**: não encadear etapas futuras no mesmo prompt.
4. **Validação prévia em toda etapa**: skip registrado no Exec Report quando o estado desejado já existe.
5. **Estimativa de contexto**: cada resposta da instância Saara inicia com estimativa de contexto (verde / amarelo / laranja / vermelho).

## Estado de execução até aqui

| Tarefa | Descrição | Commit |
|---|---|---|
| P0.0 | Fundação documental — árvore `vault-maui/`, `.maui/`, templates, painel | `854ed39` |
| P0.0.1 | Inicialização do repositório Git, `.gitignore` | `854ed39` |
| P0.0.2 | Sincronização documental pós-fundação e Git | `2ec74eb` |
| P0.0.4 | Geração do handoff inicial da sessão Maui | `2c1d84e` |
| P0.0.5 | Normalização do handoff (estrutura e conteúdo) | `ccc19a1` |
| P0.0.5 | Registro das regras operacionais no corpus | `8704ae2` |
| P0.1-A | Schemas de coordenação: `common-frontmatter`, `exec-request`, `exec-report` + fixtures | `8ef5151` |
| P0.1-B | Schemas `review-report` e `handoff-sessao` + fixtures | `1861746` |

Nota: P0.0.5 foi usado para duas tarefas distintas — débito histórico de numeração, aceito sem reabertura.

## Estado do repositório

- Branch: `main`
- Último commit conhecido: `1861746` (feat(schemas): add review-report and handoff-sessao schemas)
- Working tree: limpo no momento do handoff
- `.saara/`: inexistente e intocada em todos os retornos desta sessão

## Pendências e próximo passo

**Próxima ação imediata**: abrir `P0.1.5 — marco de planejamento da adaptação Saara→Maui`. Esta é uma decisão estrutural que precede P0.2 (validador local).

O conteúdo de P0.1.5 depende de leitura prévia da `spec-tecnica-atualizacao-saara-maui-v2` antes de decidir escopo e ações concretas. Essa leitura não foi realizada nesta sessão.

Demais pendências em aberto:

- Validador local dos schemas (P0.2) — ainda não iniciado.
- Débito histórico de numeração P0.0.5 — aceito, sem ação requerida.

## F/I/H

**Fatos** (verificados ou reportados por esta instância):
- P0.0, P0.0.1, P0.0.2, P0.0.4, P0.0.5, P0.1-A, P0.1-B concluídos e commitados.
- Commits no log: `854ed39`, `2ec74eb`, `2c1d84e`, `ccc19a1`, `8704ae2`, `8ef5151`, `1861746`.
- Schemas no dialeto leve do Maui: 5 arquivos em `vault-maui/schemas/`.
- Fixtures: 5 válidas + 10 inválidas em `vault-maui/schemas/fixtures/`.
- `.saara/` permanece inexistente e intocada em todos os retornos verificados.

**Inferências** (conclusões derivadas, não verificadas diretamente):
- O dialeto leve definido em P0.1-A se sustenta para schemas com aninhamento — `handoff-sessao` usou `type: object` com `fields` aninhado sem fricção.
- O fluxo Exec Request → Exec Report → classificação está estável o suficiente para suportar tarefas de complexidade crescente.

**Hipóteses** (não confirmadas):
- A `spec-tecnica-atualizacao-saara-maui-v2` contém substância suficiente para guiar P0.1.5 sem retrabalho.
- Nenhuma instância paralela está editando o repositório no momento.

## Mensagem inicial sugerida para a próxima instância

> Olá. Este é o handoff pós-P0.1-B do projeto Maui.
>
> Estado atual: branch `main` limpa, 7 commits, 5 schemas no dialeto leve do Maui com 15 fixtures. O conjunto de schemas de coordenação (P0.1) está encerrado.
>
> Próximo passo: abrir P0.1.5 — marco de planejamento da adaptação Saara→Maui. Antes de prosseguir, leia este arquivo e confirme: (1) estado do repositório bate com o reportado; (2) `.saara/` continua inexistente; (3) você está pronta para iniciar P0.1.5 ou prefere outra ação.
