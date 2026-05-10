---
titulo: "Marco de memória — Diagnóstico estrutural P0.1.17"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: memoria_marco
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-17
  - diagnostico-estrutural
  - memoria
  - context-brief
  - instanciação
deve_ser_considerado_em_context_brief: true
---

# Marco de memória — Diagnóstico estrutural P0.1.17

## Resumo

A P0.1.17 foi executada como diagnóstico estrutural do `vault-maui/`, sem aplicar correções. Foram criados o inventário diagnóstico e o exec-report correspondentes.

## Resultado da execução

- Inventário criado: `vault-maui/inventarios/2026-05-05-diagnostico-estrutural-vault-maui.md`
- Exec-report criado: `vault-maui/exec-reports/submitted/2026-05-05-p0-1-17-diagnostico-estrutural.md`
- Commit: `7de2211122aa709e484e232a4ff4af18afd99f32`
- Mensagem: `p0.1.17: diagnostica estrutura do vault Maui`

## Decisões e limites aplicados

- A tarefa foi diagnóstica e propositiva.
- Nenhuma normalização foi aplicada.
- Nenhum arquivo existente foi movido, apagado, renomeado ou reescrito.
- `Documentação/` não foi alterada.
- P0.1.11 não foi executada.

## Principais achados

- `vault-maui/memoria/` e `vault-maui/project-memories/` coexistem.
- `vault-maui/memoria/` existe e está vazio.
- `vault-maui/project-memories/` existe e contém memórias com `deve_ser_considerado_em_context_brief: true`.
- `vault-maui/review-reports/` não existe.
- `vault-maui/operator-packs/` contém subdiretórios por target, mas sem arquivos de pack/template.
- Há diretórios planejados ainda vazios, incluindo `scripts/`, `procedures/`, `skills/`, `hooks/`, `evals/` e `exports/`.
- Handoffs aparecem em múltiplas áreas e havia pendências pré-existentes no working tree relacionadas a handoffs.

## Frontmatter e referências

- Não foram detectados frontmatters YAML inválidos nos arquivos Markdown com bloco `---`.
- Foram detectados vários arquivos sem frontmatter, incluindo READMEs, templates, exec-reports antigos, painel e alguns arquivos arquivados.
- Foram registrados placeholders e referências que exigem revisão futura, incluindo `[[...]]`, `[[link]]`, `[[wikilink]]` e referências a `context-packages/current/maui-bootstrap.md`.

## Readiness

- Readiness para Context Brief: parcial.
- Readiness para instanciação manual Maui: experimental.

Motivos principais:

- o template de Context Brief existe e prioriza memórias marcadas;
- o diretório canônico de memórias ainda está ambíguo;
- `system-prompt.md` não existe em `00_core/`;
- PKAs herdadas não existem em `00_core/`;
- operator packs ainda não estão materializados;
- não há bootstrap `maui-bootstrap.md` nem registry de instâncias materializado.

## Lotes futuros propostos

1. **Memórias** — normalizar ou compatibilizar `memoria/` vs `memorias/`.
2. **Referências e wikilinks** — revisar placeholders e referências obsoletas.
3. **Frontmatter e slugs** — normalizar campos mínimos, status, tipos e nomes.
4. **Context Brief readiness** — garantir descoberta confiável de memórias, handoffs, exec-reports, insights e atualizações.
5. **Instanciação manual Maui** — consolidar system prompt, PKAs, operator packs e context package bootstrap.

## Recomendação registrada

O próximo lote recomendado é **Lote 1 — Memórias**, com decisão humana explícita sobre o caminho canônico antes de qualquer movimentação.

## Ressalvas

Antes da criação desta memória, o working tree já continha pendências não relacionadas:

- remoção pendente em `vault-maui/context-packages/current/2026-05-04-handoff-sessao-claude-pos-inventario.md`;
- arquivo `Sem título.canvas` não rastreado;
- arquivos não rastreados em `vault-maui/handoffs/`;
- memória não rastreada em `vault-maui/project-memories/2026-05-05-marco-decisao-normalizacao-estrutural.md`.

Essas pendências não fazem parte do commit `7de2211122aa709e484e232a4ff4af18afd99f32`.

## Instrução para Context Brief

Ao criar um `Maui Context Brief` para normalização estrutural, memórias, Context Brief readiness, instanciação manual ou continuidade da P0.1.17, considerar esta memória para refletir:

- divergências estruturais já diagnosticadas;
- readiness parcial/experimental;
- lotes futuros propostos;
- recomendação de iniciar pelo Lote 1 — Memórias;
- ressalvas sobre pendências pré-existentes no working tree.

## Próximo passo recomendado

Aprovar e executar o **Lote 1 — Memórias**, preservando memórias marcadas com `deve_ser_considerado_em_context_brief: true` e registrando a decisão canônica entre `vault-maui/memoria/` e `vault-maui/project-memories/`.
