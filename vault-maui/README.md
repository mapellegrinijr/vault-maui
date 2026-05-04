# Maui

Maui e um corpus cognitivo multipapel, procedural, portatil e instanciavel por diferentes modelos de IA.

Este diretorio (`vault-maui/`) e a raiz canonica do corpus Maui.

## Versao inicial

- Versao Maui: `v1.0`
- Estado tecnico Maui: `.maui/`
- Repositorio Git: inicializado em `main`
- Estado Saara: `.saara/`, quando existir, pertence ao Saara e nao deve ser removido, sobrescrito ou usado como estado tecnico do Maui.

## Principios iniciais

- Adendos Maui servem apenas ao Maui.
- O versionamento do Maui e separado do Saara.
- Toda execucao deve gerar um Exec Report em `exec-reports/`.
- `hash_config` do Maui devera futuramente cobrir todo o corpus relevante, nao apenas `00_core/`.

## Estado documental pos-fundacao

- A fundacao documental minima foi criada em `vault-maui/`.
- O estado tecnico minimo foi criado em `.maui/`.
- O commit inicial do repositorio foi criado com a mensagem `chore: initialize maui repository`.
- A pasta historica `Documentação/` permanece fora do corpus Maui ate decisao explicita futura.
- `.obsidian/` permanece fora do versionamento do Maui.
