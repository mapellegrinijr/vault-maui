---
titulo: "Spec Memory Store — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: spec_subsidiaria
dominio: memory_store
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "spec-memory-store-saara v7.1.1 — adaptado, não copiado"
human_gate: true
materializado_em: "P0.1.30 — spec materializada; index SQLite e API dependem de P0.3"
compatibilidade:
  - system_prompt_maui_v1_0
  - especificacao_completa_maui_v1_0
  - principios_fundacionais_maui_v1_0
  - contrato_precedencia_maui_v1_0
referencias:
  - "vault-maui/00_core/system-prompt-maui.md"
  - "vault-maui/00_core/principios-fundacionais-maui.md"
  - "vault-maui/00_core/especificacao-completa-maui.md"
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/pka-agent-engineering.md"
  - "vault-maui/00_core/spec-capture-layer-maui.md"
  - "vault-maui/00_core/spec-context-engineering-maui.md"
tags:
  - maui
  - spec
  - memory-store
  - configuracao-base
---

# Spec Memory Store — Maui

> **Spec Subsidiária — MAUI | Memory Store**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> Baseada em: spec-memory-store-saara v7.1.1 — adaptada, não copiada.
> **Materialização:** esta spec é materializada em P0.1.30 conforme declarado no system-prompt-maui.md §9 e §12. Index SQLite e API de retrieve dependem de P0.3.

---

## Nota de Human Gate

Esta spec foi criada sob Human Gate explícito da P0.1.30. Status `proposta`. Index SQLite e API de retrieve dependem de P0.3.

---

## 0. Propósito

Definir a estrutura, governança e operação do repositório canônico de memórias do Maui: `vault-maui/memorias/`. O Memory Store é o local onde decisões, marcos, preferências e artefatos com valor futuro são preservados de forma seletiva, sanitizada e rastreável.

---

## 1. Princípio fundamental

**Os arquivos markdown em `vault-maui/memorias/` são a fonte de verdade.**

O índice SQLite (quando existir) é auxiliar e derivado; se houver divergência entre o índice e um arquivo markdown, o arquivo markdown prevalece. Nunca apagar um arquivo markdown baseado apenas no estado do índice.

---

## 2. Estrutura do diretório

```
vault-maui/memorias/
├── [YYYY-MM-DD]-[slug].md     # memórias canônicas
└── (index.sqlite)             # índice auxiliar — planejado para P0.3
```

Convenção de nomenclatura: `YYYY-MM-DD-slug-descritivo.md`
- Data de captura no nome
- Slug em kebab-case, descritivo e único
- Sem subdiretórios por padrão; estrutura plana é preferida

---

## 3. Frontmatter canônico de memória

Toda memória em `vault-maui/memorias/` deve conter:

```yaml
---
titulo: "[título conciso e descritivo]"
data: "YYYY-MM-DD"
tipo: decisao | marco | preferencia_operacional | risco | artefato | outro
escopo: maui | [projeto-específico]
dominio: [ex: prompt-engineering, configuracao-base, agent-engineering]
confidencialidade: interna | restrita | publica
deve_ser_considerado_em_context_brief: true | false
fonte: explicit | proactive | manual
tags:
  - [tag1]
  - [tag2]
---
```

- `deve_ser_considerado_em_context_brief: true` marca memórias prioritárias para Context Brief e retomada
- `fonte: manual` para memórias criadas por commit human-approved sem passar pela Capture Layer
- `confidencialidade: restrita` exige controle de acesso na distribuição

---

## 4. Escritores sanctioned

| Escritor | Modo | Condição |
|---------|------|----------|
| Capture Layer | programático | via fluxo Observer → Selector → Compactor |
| Human Gate (commit) | manual | commit aprovado explicitamente pelo usuário |
| Claude Code (exec-report) | manual | durante exec-reports com instrução explícita |

Nenhum outro processo pode escrever em `vault-maui/memorias/` sem autorização explícita.

---

## 5. Index SQLite (planejado para P0.3)

O índice SQLite é auxiliar: acelera retrieve sem substituir os arquivos markdown.

Schema mínimo:

```sql
CREATE TABLE memories (
  id TEXT PRIMARY KEY,
  arquivo TEXT NOT NULL,
  titulo TEXT,
  data TEXT,
  tipo TEXT,
  escopo TEXT,
  dominio TEXT,
  confidencialidade TEXT,
  context_brief_flag INTEGER DEFAULT 0,
  tags TEXT,  -- JSON array
  instantiated_hash TEXT  -- hash do conteúdo no momento da indexação
);
```

- `instantiated_hash`: SHA-256 do conteúdo do arquivo no momento da indexação; detecta se arquivo foi modificado fora do fluxo sanctioned
- Reconstruível a qualquer momento via scan de `vault-maui/memorias/`

---

## 6. Contrato de retrieve (Memory Store)

### Entrada

```
retrieve_memory(
  tipo: str | null,
  escopo: str | null,
  dominio: str | null,
  confidencialidade: str | null,
  context_brief_flag: bool | null,
  max_resultados: int  // padrão: 10
)
```

### Saída

Lista de memórias ordenadas por data descendente, contendo arquivo, título, data, tipo, trecho relevante.

- Se `context_brief_flag=true`, retornar apenas memórias marcadas com `deve_ser_considerado_em_context_brief: true`
- Se índice ausente (pré-P0.3): scan manual de `vault-maui/memorias/` com grep por frontmatter

---

## 7. Ciclo de vida de memórias

| Estado | Descrição |
|--------|-----------|
| ativa | arquivo presente, conteúdo válido |
| obsoleta | substituída por versão mais recente; manter arquivo com nota de obsolescência |
| arquivada | movida para subdiretório `vault-maui/memorias/arquivo/` com nota de motivo |

Nunca deletar memórias sem decisão humana explícita. Preferir obsolescência com nota à deleção.

---

## 8. Quality gate — obrigatório

- [ ] Arquivos markdown são fonte de verdade; índice é auxiliar
- [ ] Frontmatter canônico presente em toda memória
- [ ] Escritor está na lista de sanctioned writers
- [ ] Sanitização aplicada (sem dados pessoais desnecessários)
- [ ] `deve_ser_considerado_em_context_brief` declarado
- [ ] Memórias obsoletas marcadas, não deletadas
- [ ] Aderência aos princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 9. Dependências P0.3

- P0.3: implementar index SQLite e reconstruct CLI
- P0.3: implementar retrieve_memory com filtros programáticos
- P0.3: integrar instantiated_hash com Capture Layer para detecção de drift

---

## Limites desta spec

- Status `proposta`; index SQLite e API dependem de P0.3.
- Retrieve manual via scan de filesystem operável desde o MVP.
- Não cria scripts, banco de dados ou endpoints.
- Não executa etapas do roadmap por inferência.
- A fonte de verdade são os arquivos markdown, não o índice.
