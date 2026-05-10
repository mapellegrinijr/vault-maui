---
titulo: "Context Brief — Status Atual Maui"
versao: "1.1"
status: ativo
data_criacao: 2026-05-10
data_atualizacao: 2026-05-10
idioma: pt-BR
tipo: context_brief
escopo: projeto_maui
---

# Context Brief — Status Atual Maui

## Fonte de status corrente

- Fonte canônica de status do projeto: `vault-maui/status-project/STATUS-UPDATE-maui.md`.
- HEAD de referência na coleta (sessão de retomada 2026-05-10T15:20): `143a3d9aae539f783c66668b2d31226106a1a971` (`docs(project): gerar pacote manual-first (status/context/handoff/guia instancias)`).
- Working tree na coleta: **sujo** — handoff não commitado: `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md`.
- Este brief é artefato de Project, não de runtime.

## Pacote mínimo de leitura (1–8)

1. `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md` — este brief.
2. `vault-maui/status-project/STATUS-UPDATE-maui.md` — status vivo do projeto.
3. `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md` — handoff da sessão do pacote manual-first (commitado).
4. `vault-maui/handoffs/2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md` — handoff Saara pós-reorg (gerado após o commit; a commitar).
5. `vault-maui/exec-reports/submitted/2026-05-10-p0-x-pacote-manual-first-status-context-handoff.md` — exec-report de governança do pacote.
6. `vault-maui/00_core/contrato-precedencia-maui.md` e `vault-maui/00_core/principios-fundacionais-maui.md`.
7. `vault-maui/00_core/system-prompt-maui.md` e `vault-maui/00_core/indice-maui.md`.
8. `vault-maui/00_core/spec-parametrizacao-maui.md` e `vault-maui/01_manifest/spec-parametrizacao-maui.json`.

Para retomada sem reler tudo: itens 1–3 são suficientes. Roadmap em `vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md` é mapa de destino; confirmar execução por evidência Git, não pelo roadmap isolado.

## Estado confirmado

- Configuração-base concluída por evidência de P0.1.32: exec-report `vault-maui/exec-reports/submitted/2026-05-06-p0-1-32-revisao-integrada-configuracao-base.md`, memória marco em `project-memories/` e commit `538b441`.
- Reorg Project vs Runtime aplicada por `f8b5120`/`9c76d62`/`1d875e3`; pacote manual-first gerado e commitado em `143a3d9`.
- Status corrente do projeto vive em `status-project/`; memórias de projeto vivem em `project-memories/`.
- `memorias/` e `status/` são pastas runtime reservadas, ainda sem uso operacional — apenas README.
- Painel é indexador baixo-trust; divergência deve ser resolvida por Git, exec-reports, handoffs e status-project.

## O que NÃO assumir

- Não usar `vault-maui/panel/status.md` como fonte declarativa de estado.
- Não usar `vault-maui/memorias/` nem `vault-maui/status/` para retomada de Project antes do runtime existir.
- Não executar P0.2, P0.3, P0.4 ou qualquer etapa do roadmap sem pedido humano explícito.
- Não promover `status: proposta` de normativos por inferência.
- Não depender de integrações externas ou automações para atualizar instâncias; o pacote é manual-first.
- Não declarar conformidade `current` sem hash/filesystem verificável; usar `unknown` quando faltar evidência.

## Próximo passo recomendado (sem executar)

- **Pendência imediata**: commitar handoff `2026-05-10-handoff-saara-claude-pos-reorg-manual-first.md` junto com artefatos da sessão de retomada.
- P0.2 é recomendado se o objetivo imediato for validação local e scripts de apoio.
- P0.3 é recomendado se o objetivo imediato for preparar instruções por ferramenta depois de decisão humana explícita.
- Em ambos os casos, começar lendo este brief, o status corrente e o handoff desta sessão.

## Fatos / Inferências / Hipóteses

- Fato: HEAD `143a3d9` registra o pacote manual-first de 2026-05-10. Working tree contém handoff não commitado.
- Fato: P0.1.32 é o último lote normativo concluído com evidência explícita.
- Inferência: o pacote manual-first reduz drift entre instâncias porque consolida status, brief, handoff e guia manual.
- Hipótese: P0.2 tende a reduzir risco antes de P0.3 se o foco for validação executável; requer decisão humana.
