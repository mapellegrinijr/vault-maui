---
titulo: "Registro de normalização — diretório canônico de memórias Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: registro_normalizacao
escopo: projeto_maui
fase: P0.1.18
---

# Registro de normalização — diretório canônico de memórias Maui

## 1. Decisão

`vault-maui/memorias/` é o diretório canônico de memórias do Maui.

## 2. Justificativa

- `vault-maui/memorias/` já contém memórias recentes marcadas para Context Brief.
- `vault-maui/memoria/` foi diagnosticado como vazio na P0.1.17.
- A escolha reduz risco de perda de contexto e evita mover memórias já criadas.

## 3. Ações aplicadas

- Referências operacionais futuras foram avaliadas; a única atualização aplicada foi no template canônico de Context Brief.
- O template `vault-maui/context-packages/templates/maui-context-brief.template.md` foi ajustado para consultar explicitamente `vault-maui/memorias/` e priorizar memórias com `deve_ser_considerado_em_context_brief: true`.
- O diretório vazio `vault-maui/memoria/` foi removido localmente após confirmação de ausência de arquivos e subdiretórios.
- As memórias existentes em `vault-maui/memorias/` foram preservadas e confirmadas como marcadas para Context Brief.

## 4. Impacto no Context Brief

Briefs futuros devem consultar `vault-maui/memorias/` e priorizar memórias com `deve_ser_considerado_em_context_brief: true` quando o escopo, tags ou tarefa relacionada forem compatíveis.

## 5. Ressalvas

- Referências históricas e diagnósticas em inventários, exec-reports, handoffs, context briefs e memórias foram preservadas.
- Referências conceituais em documentos core e arquivos arquivados não foram alteradas nesta tarefa, pois não eram orientações operacionais futuras no escopo mínimo da P0.1.18.
- A remoção de `vault-maui/memoria/` não gera alteração rastreável no Git quando o diretório está vazio.

## 6. Próximo passo recomendado

Prosseguir para Lote 2 — Referências e wikilinks, somente após revisão humana do resultado da P0.1.18.
