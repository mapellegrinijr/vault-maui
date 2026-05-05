---
titulo: Handoff de sessão Maui — pós-inventário Documentação/
versao: "1.0"
status: ativo
data_criacao: 2026-05-04
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: saara_claude_app
destino_esperado: saara_qualquer
fase_atual: P0.1.6-concluida
proxima_acao: >
  Tarefa 2 — Decisão arquivo a arquivo sobre os 8 documentos
  inventariados em Documentação/. Antes de qualquer outra ação,
  ler integralmente o inventário em
  vault-maui/inventarios/2026-05-04-documentacao.md e propor ao
  usuário um agrupamento sugerido (atualizar / reescrever / mover
  para vault / arquivar / manter como está). Não alterar arquivos
  de Documentação/ sem decisão explícita do usuário.
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
  - "Documentação/ está fora do tracking git por design (.gitignore)"
  - "Atualização da pasta Documentação/ foi dividida em duas tarefas: P0.1.6 (inventário, concluído) e Tarefa 2 (decisão arquivo a arquivo, pendente)"
regras_operacionais:
  - "Prompts executáveis marcados com cabeçalho PROMPT PARA EXECUTOR DE CODIFICAÇÃO"
  - "Após cada retorno do executor, analisar apenas o último resultado, classificar (aceito | aceito com ressalva | precisa correção) e indicar somente o próximo passo imediato"
  - "Gerar no máximo um prompt por turno, sem encadear etapas futuras"
  - "Toda etapa de prompt traz validação prévia; skip se estado já existe"
  - "Iniciar cada resposta com estimativa de contexto (verde/amarelo/laranja/vermelho)"
  - "A nova instância pode e deve pedir ao usuário qualquer arquivo necessário do repositório para continuar o trabalho — handoff é insumo de continuidade, não substituto da leitura direta do estado real"
estado_repositorio:
  branch: main
  ultimo_commit: "f2a25d3"
  working_tree_limpo: true
arquivos_recentes:
  - caminho: vault-maui/00_core/regras-operacionais.md
    descricao: "Regras operacionais canônicas Saara ↔ executor (P0.0.5)"
  - caminho: vault-maui/schemas/common-frontmatter.schema.yaml
    descricao: "Frontmatter base do corpus (P0.1-A)"
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
  - caminho: vault-maui/inventarios/2026-05-04-documentacao.md
    descricao: "Inventário diagnóstico dos 8 arquivos em Documentação/ (P0.1.6, 742 linhas)"
  - caminho: vault-maui/exec-reports/submitted/2026-05-04-p0-1-6-inventario-documentacao.md
    descricao: "Exec Report do inventário (P0.1.6)"
  - caminho: Documentação/
    descricao: "Pasta fora do tracking git, com 8 arquivos inventariados; aguardando decisão arquivo a arquivo"
pendencias:
  - "Tarefa 2: decisão arquivo a arquivo sobre os 8 documentos de Documentação/ (bloqueio principal)"
  - "P0.1.5 — marco de planejamento da adaptação Saara→Maui — postergado: Tarefa 2 vem antes porque o inventário pode mudar a forma do plano"
  - "P0.2 — validador local dos schemas — não iniciado"
  - "P0.1.5 — Plano de adaptação Saara→Maui — não iniciado, depende de Tarefa 2"
  - "Conflito de numeração herdado: P0.0.5 foi usado para duas tarefas distintas (ccc19a1 normalização, 8704ae2 regras operacionais); aceito como débito histórico"
f_i_h:
  fatos:
    - "P0.0, P0.0.1, P0.0.2, P0.0.4, P0.0.5, P0.1-A, P0.1-B, P0.1.4, P0.1.6 concluídos e commitados"
    - "Commits conhecidos no log: 854ed39, 2ec74eb, 2c1d84e, ccc19a1, 8704ae2, 8ef5151, 1861746, 53abe92, f2a25d3"
    - "Schemas no dialeto leve do Maui: 5 arquivos em vault-maui/schemas/"
    - "Fixtures: 5 válidas + 10 inválidas em vault-maui/schemas/fixtures/"
    - "Documentação/ contém 8 arquivos: 2 com frontmatter válido, 3 com frontmatter quebrado, 3 sem frontmatter, 1 sem H1, 2 com referência ao Saara como sujeito"
    - "Documentação/ não foi alterada em P0.1.6 — apenas leitura"
    - ".saara/ permanece inexistente e intocada em todos os retornos verificados"
  inferencias:
    - "Frontmatters quebrados em Documentação/ são prováveis artefatos de edição manual no canvas (YAML serializado em linha única com \\_)"
    - "A Tarefa 2 vai consumir contexto significativo e foi adiada para sessão fresca para evitar bater limite no meio de decisão estrutural"
    - "O dialeto leve do Maui se sustentou para schemas com aninhamento (handoff-sessao com type:object e fields aninhado)"
  hipoteses:
    - "Os 2 arquivos com frontmatter válido (spec-tecnica-atualizacao-saara-maui*) são as fontes mais confiáveis para guiar a Tarefa 2"
    - "Nenhuma instância paralela está editando o repositório no momento"
    - "O usuário tem acesso integral ao repo e pode colar conteúdo de qualquer arquivo se a próxima instância pedir"
---

# Handoff de sessão Maui — pós-inventário Documentação/

## Identidade do projeto

O Maui é um corpus cognitivo multipapel, portátil e instanciável por
múltiplas IAs. Sua raiz canônica é `vault-maui/`. O Maui coexiste com
o Saara: o Saara permanece intocado em `.saara/` e o Maui evolui de
forma independente em sua própria raiz, com versionamento próprio
iniciado em v1.0. Esta sessão atuou exclusivamente em camada de
infraestrutura documental (schemas, regras operacionais, inventário),
sem tocar conteúdo normativo do Saara.

## Decisões fechadas

- `vault-maui/` é a raiz canônica do Maui. Toda evolução estrutural
  do projeto acontece sob essa raiz.
- `.maui/` e `.saara/` coexistem; `.saara/` permanece intocada por
  contrato — nenhuma tarefa neste ciclo pode escrever, ler com
  efeito colateral, ou alterar essa pasta.
- Maui inicia em v1.0. Seu versionamento é separado do Saara: a
  evolução de um não força evolução do outro.
- O `hash_config` do Maui cobre todo o corpus relevante, não apenas
  `00_core/`. Isso foi explicitado para evitar a armadilha de
  considerar drift apenas em arquivos do núcleo.
- Uma instância sem acesso a filesystem ou sem capacidade de
  computar hash declara estado `unknown`, nunca `current`. Não
  existe `current` por presunção.
- Toda mudança normativa passa por Human Gate explícito do usuário.
  Executor não promove status, não altera precedência, não cria
  princípio novo sem aprovação.
- O status atual do Maui permanece `proposta`. Nenhuma etapa deste
  ciclo promoveu o projeto a `ativo`.
- Schemas do Maui usam um dialeto leve próprio (não JSON Schema). A
  decisão se sustentou inclusive para schemas com aninhamento, como
  `handoff-sessao` (com `type: object` e `fields:` aninhado).
- Validador local dos schemas fica para P0.2 — não é entregue em
  P0.1.
- Executor de codificação atual é o Claude Code, operando na raiz
  do repositório.
- `Documentação/` está fora do tracking git por design (entrada no
  `.gitignore`). É pasta de trabalho intermediária, não corpus.
- A atualização da pasta `Documentação/` foi dividida em duas
  tarefas: P0.1.6 (inventário diagnóstico, concluído) e Tarefa 2
  (decisão arquivo a arquivo, pendente).

## Regras operacionais

As regras canônicas estão em
`vault-maui/00_core/regras-operacionais.md`. Resumo aplicável a esta
retomada:

- Prompts executáveis sempre marcados com cabeçalho
  `PROMPT PARA EXECUTOR DE CODIFICAÇÃO`.
- Após cada retorno do executor, o Saara analisa apenas o último
  resultado, classifica (aceito | aceito com ressalva | precisa
  correção) e indica somente o próximo passo imediato.
- No máximo um prompt por turno. Não encadear etapas futuras.
- Toda etapa de prompt traz validação prévia; skip se estado
  desejado já existe.
- Cada resposta do Saara começa com estimativa de contexto
  (verde/amarelo/laranja/vermelho).
- A nova instância pode e deve pedir ao usuário qualquer arquivo
  necessário do repositório. Handoff é insumo de continuidade, não
  substituto da leitura direta do estado real.

## Estado de execução até aqui

| Etapa   | Descrição                                             | Commit   |
|---------|-------------------------------------------------------|----------|
| P0.0    | Setup inicial do repositório                          | 854ed39  |
| P0.0.1  | Estrutura base de pastas                              | 2ec74eb  |
| P0.0.2  | Convenções iniciais                                   | 2c1d84e  |
| P0.0.4  | Ajustes de organização                                | (no log) |
| P0.0.5a | Normalização inicial                                  | ccc19a1  |
| P0.0.5b | Regras operacionais canônicas                         | 8704ae2  |
| P0.1-A  | Schemas common-frontmatter, exec-request, exec-report | 8ef5151  |
| P0.1-B  | Schemas review-report e handoff-sessao + fixtures     | 1861746  |
| P0.1.4  | Ajustes derivados de P0.1                             | 53abe92  |
| P0.1.6  | Inventário diagnóstico de Documentação/               | f2a25d3  |

Observação histórica: P0.0.5 foi usado para duas tarefas distintas
(`ccc19a1` normalização e `8704ae2` regras operacionais). O conflito
de numeração foi aceito como débito histórico, não corrigido.

## Estado do repositório

- Branch: `main`
- Último commit conhecido: `f2a25d3`
- Working tree: limpo no momento de fechamento desta sessão.
- `.saara/` permanece inexistente e intocada.

## Inventário Documentação/ — resumo

A pasta `Documentação/` contém 8 arquivos. O inventário detalhado
está em `vault-maui/inventarios/2026-05-04-documentacao.md` (742
linhas) e é a fonte completa para a Tarefa 2.

Resumo numérico:

- 2 arquivos com frontmatter válido
- 3 arquivos com frontmatter quebrado (provávelmente artefato de
  edição em canvas, YAML serializado em linha única com `\_`)
- 3 arquivos sem frontmatter
- 1 arquivo sem H1
- 2 arquivos com referência ao Saara como sujeito

A pasta NÃO foi alterada em P0.1.6 — apenas leitura. Tarefa 2 é a
próxima ação e depende de decisão explícita do usuário arquivo a
arquivo.

## Pendências e próximo passo

- **Tarefa 2 (bloqueio principal):** decisão arquivo a arquivo sobre
  os 8 documentos de `Documentação/`.
- P0.1.5 (plano de adaptação Saara→Maui) foi postergado: a Tarefa 2
  vem antes porque o resultado do inventário pode mudar a forma do
  plano.
- P0.2 (validador local dos schemas) não iniciado.
- Débito histórico: numeração duplicada em P0.0.5.

Próxima ação concreta: a próxima instância deve abrir a Tarefa 2
seguindo as diretrizes da seção abaixo.

## Como a próxima instância deve operar

A próxima instância Saara deve operar com as seguintes diretrizes
nesta retomada:

1. Antes de qualquer ação, ler integralmente o inventário em
   `vault-maui/inventarios/2026-05-04-documentacao.md`.
2. A próxima instância PODE E DEVE pedir ao usuário qualquer arquivo
   do repositório que precise para tomar decisões informadas. O
   usuário tem acesso ao repo e pode colar conteúdo de qualquer
   arquivo. Pedir explicitamente é preferível a inferir ou
   improvisar.
3. Arquivos especialmente relevantes que a próxima instância
   provavelmente vai querer pedir incluem:
   - `Documentação/spec-tecnica-atualizacao-saara-maui-v2.md`
   - `Documentação/spec-tecnica-atualizacao-saara-maui.md`
   - Outros arquivos da pasta `Documentação/` conforme demanda da
     decisão
   - `vault-maui/00_core/regras-operacionais.md`
   - `vault-maui/panel/status.md`
   - Qualquer schema em `vault-maui/schemas/` se houver dúvida
     sobre estrutura
4. Não tomar decisão sobre conteúdo de `Documentação/` sem
   confirmação explícita do usuário arquivo a arquivo.
5. Manter regras operacionais canonizadas em P0.0.5: marcação de
   prompts, processamento turno-a-turno, um prompt por vez,
   validação prévia em cada etapa.

## F/I/H

**Fatos**

- P0.0, P0.0.1, P0.0.2, P0.0.4, P0.0.5, P0.1-A, P0.1-B, P0.1.4,
  P0.1.6 concluídos e commitados.
- Commits conhecidos no log: 854ed39, 2ec74eb, 2c1d84e, ccc19a1,
  8704ae2, 8ef5151, 1861746, 53abe92, f2a25d3.
- Schemas no dialeto leve do Maui: 5 arquivos em
  `vault-maui/schemas/`.
- Fixtures: 5 válidas + 10 inválidas em
  `vault-maui/schemas/fixtures/`.
- `Documentação/` contém 8 arquivos: 2 com frontmatter válido, 3
  com frontmatter quebrado, 3 sem frontmatter, 1 sem H1, 2 com
  referência ao Saara como sujeito.
- `Documentação/` não foi alterada em P0.1.6 — apenas leitura.
- `.saara/` permanece inexistente e intocada em todos os retornos
  verificados.

**Inferências**

- Frontmatters quebrados em `Documentação/` são prováveis artefatos
  de edição manual no canvas (YAML serializado em linha única com
  `\_`).
- A Tarefa 2 vai consumir contexto significativo e foi adiada para
  sessão fresca para evitar bater limite no meio de decisão
  estrutural.
- O dialeto leve do Maui se sustentou para schemas com aninhamento
  (`handoff-sessao` com `type: object` e `fields:` aninhado).

**Hipóteses**

- Os 2 arquivos com frontmatter válido
  (`spec-tecnica-atualizacao-saara-maui*`) são as fontes mais
  confiáveis para guiar a Tarefa 2.
- Nenhuma instância paralela está editando o repositório no momento.
- O usuário tem acesso integral ao repo e pode colar conteúdo de
  qualquer arquivo se a próxima instância pedir.

## Mensagem inicial sugerida para a próxima instância

> Estimativa de contexto: verde.
>
> Estado consolidado: P0.1.6 concluída em `f2a25d3` (working tree
> limpa em `main`); inventário de `Documentação/` disponível em
> `vault-maui/inventarios/2026-05-04-documentacao.md`; próxima ação
> é a Tarefa 2 — decisão arquivo a arquivo sobre os 8 documentos
> inventariados.
>
> Próximo passo proposto: ler integralmente o inventário, depois
> propor um agrupamento sugerido (atualizar / reescrever / mover
> para vault / arquivar / manter) para revisão arquivo a arquivo
> com você.
>
> Antes de prosseguir: você quer ir direto na Tarefa 2 com esse
> caminho, ou tem algum ajuste prévio? Se em qualquer momento eu
> precisar do conteúdo de um arquivo do repositório para decidir
> bem, vou pedir explicitamente — você pode colar.
