---
titulo: "Procedimento — Preparar Handoff Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-10
idioma: pt-BR
tipo: procedure
escopo: maui
corpus: vault-maui
human_gate: true
disparado_por: "Saara — quando usuário pedir 'prepare handoff' no projeto Maui"
referencias:
  - "vault-maui/procedures/procedimento-gerar-context-brief.md"
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/status-project/STATUS-UPDATE-maui.md"
---

# Procedimento — Preparar Handoff Maui

## 1. Propósito

Formalizar o pipeline canônico de preparação de handoff do projeto Maui. Este
procedure é a referência para Saara, Cowork e Codex sempre que o usuário pedir
"prepare handoff", "prepare o handoff da sessão", "gere o pacote de retomada"
ou equivalente no contexto do projeto Maui.

O que este procedure faz: coleta estado real do vault via Git e filesystem,
atualiza os artefatos de status e retomada, gera handoff e exec-report, arquiva
context briefs anteriores e produz um pacote commitado com Human Gate.

O que este procedure não faz: não substitui o procedimento de gerar context
brief (`vault-maui/procedures/procedimento-gerar-context-brief.md`), que cobre
apenas a geração do context brief isolado. Este pipeline é mais amplo e inclui
o context brief como um de seus artefatos, além de status, handoff, exec-report
e memória marco opcional.

Quando é disparado: exclusivamente a pedido explícito do usuário. Saara não
executa este pipeline por inferência.

---

## 2. Papéis

**Saara (orquestrador):** recebe o pedido do usuário, instancia o prompt
executor a partir deste procedure, entrega ao executor (Cowork ou Codex) e
acompanha o Human Gate. Após commit aprovado, gera o relatório operacional
de atualização de instâncias.

**Cowork ou Codex (executor):** roda o pipeline passo a passo — coleta,
geração de artefatos, apresentação do Human Gate e, após aprovação, commit
único.

**Usuário:** revisa o Human Gate, aprova ou solicita ajuste em qualquer
artefato, autoriza o commit com aprovação explícita.

**Saara (pós-commit):** gera relatório operacional resumido com hash do commit,
lista de artefatos criados e instruções de atualização de instâncias por
ferramenta (Claude Projects, Claude Code, Codex, ChatGPT Handoff).

---

## 3. Pré-condições

Antes de iniciar o pipeline, verificar:

1. `git status --short` confirma working tree limpo. Se sujo: declarar quais
   arquivos estão pendentes e registrar como risco no exec-report. Não abortar
   automaticamente, mas registrar com clareza.
2. Acesso ao filesystem do vault confirmado — o executor consegue ler
   `vault-maui/status-project/STATUS-UPDATE-maui.md` via filesystem.
3. Modelo Opus em uso para raciocínio (requerido para este pipeline).
4. Nenhum lote do roadmap em execução paralela na sessão.
5. O executor leu este procedure por inteiro antes de iniciar qualquer etapa.

---

## 4. Pipeline — 8 itens obrigatórios

### Item 1 — Atualizar STATUS-UPDATE

Arquivo: `vault-maui/status-project/STATUS-UPDATE-maui.md`

Coletar e registrar:
- HEAD via `git log -1 --oneline` e `git show -s --format="%ci" HEAD`.
- Working tree via `git status --porcelain`.
- Últimos 20 commits via `git log --oneline -20`.
- Estado confirmado: último lote comprovado por exec-report, decisões humanas
  recentes, pendências e riscos.
- Próximo passo recomendado (sem executar).

Formato obrigatório do cabeçalho:
```
# Status Update — Projeto Maui (Project)

- Gerado em: <ISO local>
- HEAD: `<hash completo>` — <data> — `<mensagem>`
- Working tree: <limpo | sujo — listar arquivos>
```

Seguir estrutura de seções 1 a 6 conforme template existente no arquivo.

### Item 2 — Criar context brief em `current/`

Arquivo: `vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<escopo>-maui.md`

Nome padrão para handoff de sessão sem escopo específico:
`YYYY-MM-DD-context-brief-status-atual-maui.md`

Frontmatter obrigatório:
```yaml
---
titulo: "Context Brief — <escopo>"
versao: "1.0"
status: ativo
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
deve_ser_considerado_em_context_brief: true
---
```

Seções obrigatórias: fonte de status corrente (apontar para STATUS-UPDATE),
pacote mínimo de leitura (1–8), estado confirmado, o que NÃO assumir, próximo
passo recomendado, F/I/H.

Seguir o procedimento canônico em
`vault-maui/procedures/procedimento-gerar-context-brief.md` para o conteúdo.

### Item 3 — Arquivar context briefs anteriores

Mover todos os arquivos de `vault-maui/context-packages/current/` que não
sejam o recém-criado para `vault-maui/context-packages/archive/`.

Critério: qualquer arquivo com data anterior à do context brief criado no
Item 2 deve ir para `archive/`. O arquivamento não altera o conteúdo dos
arquivos.

Registrar no exec-report quais arquivos foram arquivados.

Se `current/` já estiver com apenas o novo context brief: pular e registrar.

### Item 4 — Criar handoff em `handoffs/`

Arquivo: `vault-maui/handoffs/YYYY-MM-DD-handoff-<escopo>.md`

Nome padrão: `YYYY-MM-DD-handoff-sessao-<lote-ou-atividade>.md`

Frontmatter obrigatório:
```yaml
---
titulo: "Handoff — <descrição da sessão>"
versao: "1.0"
status: ativo
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: handoff_sessao
escopo: projeto_maui
origem_instancia: <identificar executor>
destino_esperado: proxima_instancia_qualquer
deve_ser_considerado_em_context_brief: true
---
```

Conteúdo obrigatório: resumo do que foi feito na sessão, lista de artefatos
gerados/atualizados (A/B/C/D/...), checklist de retomada rápida (ordem de
leitura), ações proibidas por inferência, F/I/H quando material.

#### Conteúdo obrigatório do handoff principal do dia

O handoff gerado neste item **deve incluir** a seção "Protocolo Prepare Handoff
(manual-first)". Esta seção serve como âncora anti-drift para a próxima
instância: confirma que o pacote foi gerado via este pipeline canônico, registra
o HEAD verificado e indica o executor responsável.

Template obrigatório (inserir após a seção de Artefatos ou antes de F/I/H):

```markdown
## Protocolo Prepare Handoff (manual-first)

- Pipeline executado: `vault-maui/procedures/procedimento-preparar-handoff.md`
- HEAD verificado no início do pipeline: `<hash completo>`
- Data/hora de geração: <ISO local>
- Executor: <saara_cowork_local | saara_codex | saara_claude_code>
- Todos os 8 itens do pipeline foram executados: sim / não (listar omissões)
- Context briefs arquivados nesta execução: <lista ou "nenhum">
- Memória marco gerada: sim (`vault-maui/project-memories/<arquivo>`) / não (justificativa)
- Commit do pacote: <hash pós-commit ou "pendente — aguardando Human Gate">

> Anti-drift: esta seção confirma que o pacote foi gerado via pipeline canônico.
> Instâncias sem filesystem devem declarar conformidade `unknown`.
> Nunca assumir estado sem verificar HEAD via Git.
```

### Item 5 — Criar exec-report em `exec-reports/submitted/`

Arquivo: `vault-maui/exec-reports/submitted/YYYY-MM-DD-p0-x-pacote-handoff-<descricao>.md`

Frontmatter:
```yaml
---
titulo: "Exec-report — Pacote handoff <descrição>"
versao: "1.0"
status: submitted
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: exec_report
escopo: governanca_projeto_maui
---
```

Conteúdo obrigatório: escopo da sessão, evidência Git (HEAD + data + working
tree), lista de artefatos gerados/atualizados, confirmação de limite
(sem P0.2/P0.3/P0.4, sem promoção de status), context briefs arquivados,
riscos e observações, nota sobre HEAD pré-pacote vs HEAD pós-commit.

### Item 6 — Criar memória marco em `project-memories/` (condicional)

Arquivo: `vault-maui/project-memories/YYYY-MM-DD-marco-<descricao>.md`

Criar apenas se houver decisão nova e material registrada na sessão — decisão
de arquitetura, escolha de tecnologia, mudança de escopo, gate humano relevante
ou marco de implementação.

Se não houver decisão nova material: pular este passo e registrar a omissão
no exec-report com justificativa explícita ("nenhuma decisão nova material
nesta sessão").

Frontmatter:
```yaml
---
titulo: "Marco — <descrição>"
versao: "1.0"
status: ativo
data_criacao: YYYY-MM-DD
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
deve_ser_considerado_em_context_brief: true
---
```

### Item 7 — Human Gate

Antes de qualquer `git add` ou `git commit`, apresentar ao usuário:

- Lista de todos os artefatos criados/atualizados com paths completos.
- Resumo de mudanças em cada artefato (1–2 linhas por arquivo).
- Context briefs arquivados (se houver).
- Working tree após criação dos artefatos (`git status --short`).
- Quaisquer decisões tomadas pelo executor que requeiram validação humana.

Formato mínimo de apresentação:
```
## Human Gate — Pacote handoff YYYY-MM-DD

| Artefato | Ação | Path |
|---|---|---|
| STATUS-UPDATE | atualizado | vault-maui/status-project/STATUS-UPDATE-maui.md |
| Context Brief | criado | vault-maui/context-packages/current/... |
| Handoff | criado | vault-maui/handoffs/... |
| Exec-report | criado | vault-maui/exec-reports/submitted/... |
| Memória marco | criado / omitido | vault-maui/project-memories/... |
| Context briefs arquivados | movidos | vault-maui/context-packages/archive/... |

Aguardando aprovação explícita. Nenhum commit realizado.
```

PARAR. Não prosseguir até receber aprovação explícita do usuário.

### Item 8 — Commit único após aprovação

Após aprovação explícita do usuário:

```bash
git add -A
git status --short   # confirmar que apenas os artefatos esperados estão staged
git commit -m "chore(handoff): pacote manual-first YYYY-MM-DD — status, context brief, handoff, exec-report"
git status --short   # confirmar working tree limpo
git log -1 --oneline # confirmar HEAD novo
```

Limpar quaisquer arquivos `.bak`, `.disabled` ou temporários antes do commit.

Após commit: registrar o novo HEAD e repassar ao usuário o Relatório
Operacional Final (ver Seção 6).

---

## 5. Convenções obrigatórias

**Status de artefatos novos:**
- Context brief: `status: ativo`
- Handoff: `status: ativo`
- Exec-report: `status: submitted`
- Memória marco: `status: ativo`
- Normativos de `00_core/` e `01_manifest/`: nunca alterar status neste
  pipeline.

**Flag `deve_ser_considerado_em_context_brief: true`:** obrigatória em memórias
marco e context briefs. Opcional em handoffs (incluir quando o handoff tiver
conteúdo material para retomada).

**Mensagem de commit padronizada:**
```
chore(handoff): pacote manual-first YYYY-MM-DD — status, context brief, handoff, exec-report
```
Adicionar sufixo descritivo quando o pacote tiver escopo específico. Ex:
```
chore(handoff): pacote manual-first 2026-05-10 — pos-analise-critica-reorg
```

**HEAD verificado:** sempre coletar `git log -1 --oneline` no início do
pipeline e registrar o hash completo nos artefatos. Incluir nota: "Estado
futuro exige nova verificação via Git."

**Nunca usar `vault-maui/memorias/` ou `vault-maui/status/`** neste pipeline
— são pastas reservadas para runtime operacional.

---

## 6. Relatório operacional final

Após commit aprovado, Saara gera e entrega ao usuário:

**Conteúdo obrigatório:**
- Hash do commit do pacote.
- Lista de artefatos criados/atualizados com paths completos.
- Pacote mínimo de leitura para nova instância:
  1. `vault-maui/status-project/STATUS-UPDATE-maui.md`
  2. Novo context brief em `vault-maui/context-packages/current/`
  3. Novo handoff em `vault-maui/handoffs/`

**Instruções de aplicação por target:**

a) **Claude Projects:** anexar os 3 arquivos do pacote mínimo no início
   da conversa ou como "Project Knowledge". Confirmar atualização comparando
   o HEAD registrado no STATUS-UPDATE com o que está sendo usado no Project.

b) **Claude Code:** garantir vault montado e instruir o modelo a ler primeiro
   o context brief, depois o STATUS-UPDATE e depois o handoff antes de qualquer
   ação. Confirmar `git rev-parse HEAD` antes de declarar estado.

c) **Codex:** idem Claude Code. Prompt mínimo de inicialização: "Leia
   `vault-maui/context-packages/current/<context-brief>.md` e
   `vault-maui/status-project/STATUS-UPDATE-maui.md`, confirme HEAD, e apenas
   então responda." Observar modelo recomendado (Opus para raciocínio).

d) **ChatGPT Handoff:** colar o conteúdo dos 3 arquivos do pacote mínimo como
   contexto inicial. Declarar conformidade `unknown` por ausência de filesystem
   verificável. Não executar roadmap por inferência. Não promover status de
   normativos.

---

## 7. Ações proibidas dentro deste pipeline

- Executar qualquer etapa do roadmap (P0.x, P1.x, P2.x ou qualquer outra).
- Promover `status: proposta` de qualquer normativo de `00_core/` ou
  `01_manifest/`.
- Alterar arquivos de `00_core/` ou `01_manifest/` — salvo se for tarefa
  separada com prompt próprio e Human Gate dedicado.
- Commitar sem Human Gate explícito e aprovação do usuário.
- Tratar handoffs como documentos de baixo impacto — eles são fonte de verdade
  para a próxima instância e exigem revisão humana antes do commit.
- Pular o arquivamento de context briefs anteriores ao criar um novo (Item 3).
- Escrever em `vault-maui/memorias/` ou `vault-maui/status/` — são pastas
  runtime reservadas.
- Declarar conformidade `current` sem hash/filesystem verificável — usar
  `unknown` quando faltar evidência.

---

## 8. Critérios de pronto

O pipeline está completo quando:

- [ ] STATUS-UPDATE atualizado com HEAD verificado e working tree declarado.
- [ ] Novo context brief criado em `current/` com data atual.
- [ ] Context briefs anteriores de `current/` movidos para `archive/`.
- [ ] Novo handoff criado em `handoffs/`.
- [ ] Exec-report criado em `exec-reports/submitted/`.
- [ ] Memória marco criada em `project-memories/` — ou omissão justificada
      registrada no exec-report.
- [ ] Human Gate apresentado e aprovado pelo usuário.
- [ ] Commit único realizado com mensagem padronizada.
- [ ] Relatório operacional final gerado e entregue ao usuário.

Total de artefatos: 5 (sem memória marco) ou 6 (com memória marco), mais
STATUS-UPDATE atualizado.

---

## 9. Riscos e limites

**Dependência de filesystem:** este pipeline requer acesso direto ao vault via
filesystem. Instâncias sem filesystem (claude.ai, ChatGPT) não podem executá-lo
— apenas consumir o pacote gerado por um executor com acesso.

**HEAD pré-pacote nos artefatos:** os artefatos gerados durante o pipeline
registram o HEAD coletado no início, que é anterior ao commit do próprio pacote.
O exec-report deve sempre incluir a nota: "Este pacote registra o HEAD coletado
antes do commit do pacote; o HEAD pós-commit é a referência correta para
próxima sessão."

**Acúmulo em `archive/`:** context packages arquivados não têm critério de
retenção formalizado. O volume crescerá a cada execução do pipeline. Critério
de retenção é backlog para tratamento futuro (candidato a P0.2 ou P0.9).

**READMEs e índices:** este procedure não cobre atualização de READMEs,
painel ou índices auxiliares. Esses artefatos podem ficar desatualizados entre
execuções do pipeline.

**Ritmo de execução:** a médio prazo, executar este pipeline a cada sessão
gera ~5–6 novos arquivos por execução. Acima de duas execuções semanais, o
volume de governança começa a competir com o volume de implementação. Avaliar
automação leve (P0.2) quando esse ponto for atingido.
