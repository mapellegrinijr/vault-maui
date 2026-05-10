---
titulo: "Exec-report — P0.1.28: system prompt Maui"
versao: "1.0"
status: submitted
data_execucao: 2026-05-06
idioma: pt-BR
tipo: exec_report
fase: "P0.1.28"
resultado: success
escopo: projeto_maui
---

# Exec-report — P0.1.28: system prompt Maui

## Resumo

A P0.1.28 criou `vault-maui/00_core/system-prompt-maui.md` como contrato runtime inicial do Maui, em `status: proposta`, usando a configuração Saara vigente como modelo estrutural e conceitual com adaptação curada para Maui.

Não foram criados PKAs, specs subsidiárias, parametrização, índice, operator packs ou context packages finais. O roadmap não foi alterado.

## Arquivos lidos

### Maui

- `vault-maui/00_core/principios-fundacionais-maui.md`
- `vault-maui/00_core/contrato-precedencia-maui.md`
- `vault-maui/00_core/especificacao-completa-maui.md`
- `vault-maui/context-packages/current/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md`
- `vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md`
- `vault-maui/inventarios/2026-05-06-diagnostico-configuracao-base-maui.md`
- `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-24-diagnostico-configuracao-base.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-25-plano-configuracao-base.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-25-post-marco-context-brief.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-26-principios-precedencia-maui.md`
- `vault-maui/exec-reports/submitted/2026-05-06-p0-1-27-especificacao-completa-maui.md`
- `vault-maui/project-memories/2026-05-06-marco-p0-1-27-especificacao-completa-maui.md`

### Saara usados como modelo

- `../Saara/vault-saara/00_core/system-prompt.md`
- `../Saara/vault-saara/00_core/principios-fundacionais.md`
- `../Saara/vault-saara/00_core/especificacao-completa.md`
- `../Saara/vault-saara/00_core/pka-prompt-engineering.md`
- `../Saara/vault-saara/00_core/pka-agent-engineering.md`
- `../Saara/vault-saara/00_core/pka-development-engineer.md`
- `../Saara/vault-saara/00_core/pka-ai-solutions-architect-elite.md`
- `../Saara/vault-saara/00_core/pka-written-comms-core.md`
- `../Saara/vault-saara/00_core/pka-safe-agile-master-elite.md`
- `../Saara/vault-saara/00_core/spec-distribuicao.md`
- `../Saara/vault-saara/00_core/spec-instanciacao-conformidade.md`
- `../Saara/vault-saara/00_core/spec-context-injection.md`
- `../Saara/vault-saara/00_core/spec-capture-layer.md`
- `../Saara/vault-saara/00_core/spec-memory-store.md`
- `../Saara/vault-saara/00_core/spec-adendos.md`
- `../Saara/vault-saara/00_core/spec-parametrizacao.md`
- `../Saara/vault-saara/00_core/spec-parametrizacao.json`
- `../Saara/vault-saara/00_core/indice.md`

## Arquivos criados/alterados

- Criado: `vault-maui/00_core/system-prompt-maui.md`
- Criado: `vault-maui/project-memories/2026-05-06-marco-p0-1-28-system-prompt-maui.md`
- Criado: `vault-maui/exec-reports/submitted/2026-05-06-p0-1-28-system-prompt-maui.md`

Nenhum arquivo em `Documentação/` foi alterado.

Nenhum arquivo Saara foi alterado.

O roadmap não foi alterado nesta tarefa. A conclusão da P0.1.28 pode ser registrada em reconciliação posterior, preservando `status: proposta`.

## Validações executadas

- `git status --short` antes da tarefa: working tree limpo.
- Confirmação de existência de `principios-fundacionais-maui.md`.
- Confirmação de existência de `contrato-precedencia-maui.md`.
- Confirmação de existência de `especificacao-completa-maui.md`.
- Confirmação de ausência prévia de `vault-maui/00_core/system-prompt-maui.md`.
- Busca por duplicidade de P0.1.28 ou system prompt Maui equivalente antes da escrita.
- Localização dos arquivos Saara modelo em `../Saara/vault-saara/00_core/`.
- Validação manual de frontmatter/YAML dos arquivos criados.
- Verificação manual dos caminhos citados.
- Busca por criação indevida de PKAs, specs subsidiárias, parametrização, índice, operator packs e bootstrap/context packages finais.
- Verificação de ausência de alterações em `Documentação/`.
- `git status --short` depois da tarefa e após commit.

## Decisões aplicadas

- Criar system prompt Maui em `status: proposta`.
- Usar `precedencia: 2`, compatível com o contrato de precedência Maui.
- Preservar separação Saara/Maui e proibir mistura entre `vault-saara/` e `vault-maui/`.
- Declarar que Saara é modelo/referência, não fonte de cópia integral.
- Incluir Prompt Engineering Elite no Domain Router Maui planejado como obrigatório.
- Preservar a fronteira Prompt Engineering vs Agent Engineering e a regra híbrida prompt + agente.
- Adaptar modos A/B/B1, profundidade D0-D3 e disclosure L0-L3 do modelo Saara para Maui.
- Declarar `vault-maui/project-memories/` como memória canônica.
- Manter `unknown` para ChatGPT/Handoff sem filesystem/hash verificável.
- Registrar que PKAs serão P0.1.29, specs subsidiárias P0.1.30 e parametrização/índice P0.1.31.
- Não atualizar roadmap por padrão.

## Human Gate aplicado

O usuário autorizou explicitamente a P0.1.28 para criar o system prompt Maui. A autorização foi tratada como Human Gate limitado à criação do contrato runtime inicial e aos registros mínimos de memória/exec-report.

O Human Gate desta tarefa não autorizou promoção de status geral, criação de PKAs, specs subsidiárias, parametrização, índice, operator packs, context packages finais, P0.1.11, P0.1.29, P0.1.30, P0.1.31 ou instanciação manual.

## Uso dos arquivos Saara como modelo

`system-prompt.md` orientou formato, compactação e seções runtime: identidade, prevalência, princípios, precedência, Domain Router, modos, tooling, contexto, memória, aviso de contexto e output padrão.

`especificacao-completa.md` orientou a relação entre precedência, anti-drift, PKAs planejadas, Context Engineering, Capture Layer, conformidade e limites.

`pka-prompt-engineering.md` orientou a inclusão de Prompt Engineering Elite como domínio obrigatório e a fronteira com Agent Engineering.

`spec-parametrizacao.md` e `spec-parametrizacao.json` orientaram modos, profundidade, progressive disclosure, domain router, política de incerteza, contexto e aviso de contexto.

As demais PKAs, specs subsidiárias e `indice.md` orientaram a lista de domínios e componentes futuros. Todo conteúdo foi reexpresso em termos Maui.

## Riscos remanescentes

- O system prompt está em `status: proposta`.
- PKAs Maui ainda não existem, incluindo Prompt Engineering Elite materializada.
- Specs subsidiárias, parametrização e índice ainda estão pendentes.
- Instanciação manual Maui permanece não pronta.
- Roadmap pode precisar de reconciliação posterior para registrar P0.1.28.

## Status final

success

## Próximo passo recomendado

Executar P0.1.29 em tarefa separada, com Human Gate, para materializar PKAs Maui, incluindo Prompt Engineering Elite como obrigatória. Não executar P0.1.11 nem instanciação manual por inferência.
