# Handoff da Sessao Maui

## Identificacao

- ID: `2026-05-04-handoff-sessao-maui`
- Tipo: `handoff-current`
- Projeto: `Maui`
- Versao Maui: `v1.0`
- Data: `2026-05-04`
- Estado: `normalizado para proxima sessao`
- Ultima normalizacao: `P0.0.5 Normalizar handoff da sessao Maui`

## Como usar este handoff

Este arquivo e o pacote de contexto primario para a proxima sessao Maui.

Antes de executar nova tarefa:

- Ler este arquivo.
- Verificar `git status --short`.
- Verificar `vault-maui/panel/status.md`.
- Verificar se `.saara/` existe; se existir, preservar e nao usar como estado tecnico do Maui.
- Criar Exec Report ao final de qualquer execucao.
- Criar commit proprio quando a execucao alterar arquivos versionados.

## Resumo executivo

Maui foi inicializado como corpus cognitivo multipapel, procedural, portatil e instanciavel por diferentes modelos de IA.

A fundacao fisica minima existe em `vault-maui/`. O estado tecnico Maui existe em `.maui/`. O repositorio Git local esta inicializado na branch `main`.

Esta fase ainda e P0 documental. Nao houve implementacao de funcionalidades, schemas, scripts Python, MCP, plugins, automacoes, UI, busca vetorial, operator packs completos ou migracao de documentos grandes.

## Estado Git atual

- Branch: `main`
- Status antes da P0.0.5: limpo
- Commits conhecidos antes do commit da P0.0.5:
  - `2c1d84e docs: add session handoff`
  - `2ec74eb docs: sync post-foundation git state`
  - `854ed39 chore: initialize maui repository`

## Execucoes concluidas

### P0.0 Fundacao Documental

- Criada a arvore canonica `vault-maui/`.
- Criada a estrutura tecnica `.maui/`.
- Criados arquivos minimos de orientacao:
  - `vault-maui/README.md`
  - `vault-maui/00_core/README.md`
  - `vault-maui/01_manifest/README.md`
  - `vault-maui/adendos/README.md`
  - `.maui/README.md`
  - `.maui/VERSION`
  - `.maui/hash_config.md`
- Criados templates minimos:
  - `vault-maui/exec-requests/templates/exec-request-template.md`
  - `vault-maui/exec-reports/templates/exec-report-template.md`
  - `vault-maui/exec-reports/templates/review-report-template.md`
- Criado painel file-based em `vault-maui/panel/`.
- Exec Report:
  - `vault-maui/exec-reports/submitted/2026-05-04-p0-0-fundacao-documental.md`

### P0.0.1 Inicializacao do repositorio Git

- Inicializado repositorio Git local em `main`.
- Criado `.gitignore` minimo.
- Criado commit:
  - `854ed39 chore: initialize maui repository`
- Mantidos fora do versionamento:
  - `.obsidian/`
  - `Documentação/`
- Exec Report:
  - `vault-maui/exec-reports/submitted/2026-05-04-p0-0-1-inicializacao-git.md`

### P0.0.2 Sincronizacao documental pos-fundacao e Git

- Sincronizado `vault-maui/README.md` com o estado pos-Git.
- Atualizado `vault-maui/panel/status.md`.
- Atualizado `vault-maui/panel/decisions/index.md`.
- Atualizado `.maui/README.md`.
- Criado `.maui/git.md`.
- Criado commit:
  - `2ec74eb docs: sync post-foundation git state`
- Exec Report:
  - `vault-maui/exec-reports/submitted/2026-05-04-p0-0-2-sincronizacao-documental-pos-fundacao-git.md`

### P0.0.4 Gerar handoff da sessao Maui

- Criado handoff da sessao em `vault-maui/context-packages/current/2026-05-04-handoff-sessao-maui.md`.
- Atualizado `vault-maui/panel/status.md`.
- Criado commit:
  - `2c1d84e docs: add session handoff`
- Exec Report:
  - `vault-maui/exec-reports/submitted/2026-05-04-p0-0-4-handoff-sessao-maui.md`

### P0.0.5 Normalizar handoff da sessao Maui

- Normalizado este handoff para representar o estado atual da sessao, incluindo a propria P0.0.4.
- Atualizado `vault-maui/panel/status.md`.
- Commit:
  - `docs: normalize session handoff`
- Exec Report:
  - `vault-maui/exec-reports/submitted/2026-05-04-p0-0-5-normalizar-handoff-sessao-maui.md`

## Decisoes registradas

- `vault-maui/` e a raiz canonica do corpus Maui.
- `.maui/` e o estado tecnico do Maui.
- `.saara/`, quando existir, pertence ao Saara e deve ser preservado.
- `.saara/` nao deve ser usado como estado tecnico do Maui.
- `.maui/` e `.saara/` devem coexistir quando ambos existirem.
- Maui inicia como `v1.0`.
- O versionamento do Maui e separado do Saara.
- Adendos Maui servem apenas ao Maui.
- Toda execucao deve gerar um Exec Report.
- `hash_config` do Maui devera futuramente incluir todo o corpus relevante, nao apenas `00_core/`.
- `Documentação/` permanece fora do corpus Maui ate decisao explicita futura.
- `.obsidian/` permanece fora do versionamento Maui.

## Regras operacionais — interação Saara ↔ Executor de Codificação

**REGRA 1 — Marcação de prompts executáveis**

Todo bloco que deva ser copiado e executado por um executor de codificação precisa estar identificado com o cabeçalho explícito "PROMPT PARA EXECUTOR DE CODIFICAÇÃO". Comandos internos a um prompt não devem ser confundidos com comandos sugeridos ao usuário fora do prompt. Esta regra aplica-se a Codex, Claude Code e quaisquer executores futuros.

**REGRA 2 — Processamento turno-a-turno de retornos do executor**

Após cada retorno do executor de codificação, a instância Saara deve:
1. Analisar apenas o último resultado executado.
2. Classificar como: aceito | aceito com ressalva | precisa correção.
3. Indicar somente o próximo passo imediato.
4. Gerar no máximo um prompt para o executor por vez.
5. Não extrapolar várias etapas futuras nem propor normalizações não solicitadas se o resultado atual for suficiente.

## Estado de preservacao

- `.saara/` nao existia no workspace durante as execucoes realizadas ate a P0.0.5.
- Nenhum arquivo ou diretorio Saara foi removido, movido, editado ou usado como estado tecnico do Maui.
- `Documentação/` foi preservada sem alteracoes e segue fora do corpus Maui.
- `.obsidian/` foi preservada sem alteracoes e segue fora do versionamento Maui.

## Restricoes ativas

- Nao migrar documentos Saara ou arquitetura sem Exec Request especifico.
- Nao incorporar `Documentação/` ao corpus Maui sem decisao explicita.
- Nao implementar schemas sem tarefa futura especifica.
- Nao implementar scripts Python sem tarefa futura especifica.
- Nao implementar MCP, plugins, automacoes, UI, busca vetorial ou operator packs completos sem tarefa futura especifica.
- Nao usar `.saara/` como estado tecnico do Maui.

## Pendencias

- Definir politica formal de versionamento e convencao de commits.
- Decidir se `Documentação/` sera migrada, preservada fora do Git ou incorporada ao corpus Maui.
- Definir schemas.
- Definir `hash_config` tecnico.
- Definir scripts, MCP, plugins, automacoes e validacoes.
- Definir operator packs completos.
- Criar processo de Review Report para execucoes submetidas.

## Proxima tarefa recomendada

Recomendada: `P0.0.3 Revisao da fundacao documental e Git`.

Motivo: antes de avancar para schemas, scripts ou automacoes, uma revisao formal deve validar a fundacao fisica, os Exec Reports, o estado Git, o `.gitignore`, o painel, o handoff e as decisoes registradas.

## Arquivos de referencia

- `vault-maui/README.md`
- `.maui/README.md`
- `.maui/git.md`
- `.maui/hash_config.md`
- `vault-maui/panel/status.md`
- `vault-maui/panel/decisions/index.md`
- `vault-maui/exec-reports/submitted/2026-05-04-p0-0-fundacao-documental.md`
- `vault-maui/exec-reports/submitted/2026-05-04-p0-0-1-inicializacao-git.md`
- `vault-maui/exec-reports/submitted/2026-05-04-p0-0-2-sincronizacao-documental-pos-fundacao-git.md`
- `vault-maui/exec-reports/submitted/2026-05-04-p0-0-4-handoff-sessao-maui.md`
- `vault-maui/exec-reports/submitted/2026-05-04-p0-0-5-normalizar-handoff-sessao-maui.md`
