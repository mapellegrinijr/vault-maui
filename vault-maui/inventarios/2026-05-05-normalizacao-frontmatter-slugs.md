---
titulo: "Registro de normalização — frontmatter e slugs Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: registro_normalizacao
escopo: projeto_maui
fase: P0.1.20
---

# Registro de normalização — frontmatter e slugs Maui

## 1. Decisão

A P0.1.20 corrigiu apenas frontmatter operacional atual com baixo risco e preservou históricos, arquivos arquivados, inventários, exec-reports, handoffs, memórias, templates antigos e READMEs sem necessidade operacional clara.

Nenhum slug foi renomeado nesta tarefa.

## 2. Critério de classificação

Categorias de frontmatter:

- `frontmatter_valido_completo`: arquivo Markdown com YAML válido e campos mínimos esperados.
- `frontmatter_valido_incompleto`: arquivo Markdown com YAML válido, mas sem campo mínimo.
- `frontmatter_invalido`: arquivo Markdown com bloco inicial YAML inválido.
- `frontmatter_ausente`: arquivo Markdown sem bloco de frontmatter.
- `template_sem_frontmatter_aceitavel`: template antigo ou exemplo sem frontmatter cuja correção não é necessária para operação atual.
- `historico_ou_arquivado_preservado`: arquivo histórico, arquivado, exec-report antigo, handoff ou inventário preservado sem reescrita.

Categorias de slugs:

- corrigir nesta tarefa: slug operacional atual com destino inequívoco e baixo risco.
- preservar histórico: slug em arquivo histórico, arquivado, exec-report, inventário, handoff ou memória.
- registrar pendência: inconsistência sem impacto operacional imediato.
- precisa decisão humana: renomeação com risco de quebrar referências ou sem destino inequívoco.

## 3. Frontmatter corrigido

| Arquivo | Problema | Correção aplicada | Justificativa |
| --- | --- | --- | --- |
| `vault-maui/panel/status.md` | Frontmatter ausente em painel operacional atual | Adicionado frontmatter com `titulo`, `versao`, `status`, `data_criacao`, `idioma`, `tipo` e `escopo` | O painel é arquivo operacional atual e os campos eram inferíveis com segurança. |

## 4. Frontmatter preservado ou pendente

| Arquivo | Problema | Motivo da preservação ou pendência |
| --- | --- | --- |
| `vault-maui/context-packages/templates/maui-context-brief.template.md` | Frontmatter válido completo com `status: template` e `tipo: context_brief_template` | Preservado porque já é o padrão aprovado na P0.1.9; alteração seria normalização sem necessidade operacional clara. |
| `vault-maui/00_core/README.md` | Frontmatter ausente | Pendente; README operacional possível, mas metadados não foram inferidos sem decisão específica. |
| `vault-maui/README.md` | Frontmatter ausente | Pendente; README raiz pode exigir política própria de frontmatter. |
| `vault-maui/01_manifest/README.md`, `vault-maui/adendos/README.md`, `vault-maui/panel/README.md`, `vault-maui/panel/decisions/index.md`, `vault-maui/panel/reviews/index.md` | Frontmatter ausente | Pendente; arquivos de índice/README preservados até haver regra de metadados para páginas auxiliares. |
| `vault-maui/exec-reports/submitted/2026-05-04-*.md` | Frontmatter ausente | Preservado; exec-reports antigos e históricos não foram reescritos. |
| `vault-maui/exec-reports/templates/*.md` e `vault-maui/exec-requests/templates/*.md` | Frontmatter ausente | Preservado como template antigo/exemplo; normalização deve ser aprovada em lote próprio. |
| `vault-maui/context-packages/archive/*.md` | Frontmatter ausente em parte dos arquivos arquivados | Preservado; arquivos arquivados não são corrigidos nesta tarefa. |

## 5. Slugs corrigidos

Nenhum slug foi corrigido nesta tarefa.

## 6. Slugs preservados ou pendentes

| Arquivo | Problema | Motivo da preservação ou pendência |
| --- | --- | --- |
| Arquivos Markdown sob `vault-maui/` | Não foram encontrados nomes com espaços, underscores, acentuação, versão `v_0_1`/`v0.1` ou arquivos Markdown sem extensão | Nenhuma ação necessária. |
| Arquivos históricos em `vault-maui/context-packages/archive/`, `vault-maui/exec-reports/`, `vault-maui/inventarios/`, `vault-maui/handoffs/` e `vault-maui/memorias/` | Possíveis convenções históricas de nome | Preservados por regra da tarefa; não houve renomeação. |

## 7. Impacto

- Context Brief: sem alteração estrutural; o template canônico já estava completo e foi preservado.
- Documentos core: nenhum conteúdo substantivo foi alterado.
- Instanciação manual futura: o painel operacional agora tem frontmatter mínimo válido.
- Próximos lotes de normalização: permanece pendente decidir se READMEs, índices auxiliares e templates antigos devem receber frontmatter padronizado.

## 8. Próximo passo recomendado

Prosseguir para Lote 4 — Context Brief readiness, somente após revisão humana do resultado da P0.1.20.
