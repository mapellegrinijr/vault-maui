---
titulo: "Relatório — Atualizar instâncias manualmente"
versao: "1.0"
status: ativo
data_criacao: 2026-05-10
idioma: pt-BR
tipo: relatorio_operacional_project
escopo: projeto_maui
---

# Relatório — Como atualizar instâncias manualmente

## 1) Princípios (manual-first)

- `vault-maui/` é a fonte canônica.
- Usar como pacote mínimo de atualização: `vault-maui/status-project/STATUS-UPDATE-maui.md`, `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md` e `vault-maui/handoffs/2026-05-10-handoff-sessao-pacote-status-context.md`.
- Não executar roadmap por inferência; P0.2, P0.3 e P0.4 exigem pedido humano explícito.
- `vault-maui/memorias/` e `vault-maui/status/` ainda não são usadas; são reservadas para runtime.
- Se houver divergência, preferir Git, exec-reports, handoffs, context brief current e status-project.

## 2) Checklist — Claude Projects

- Copiar/colar o System Prompt do Maui a partir de `vault-maui/00_core/system-prompt-maui.md`.
- Adicionar como conhecimento do projeto, conforme suporte da ferramenta:
  - `vault-maui/00_core/contrato-precedencia-maui.md`
  - `vault-maui/00_core/principios-fundacionais-maui.md`
  - `vault-maui/00_core/especificacao-completa-maui.md`
  - `vault-maui/00_core/indice-maui.md`
  - `vault-maui/00_core/spec-parametrizacao-maui.md`
  - `vault-maui/01_manifest/spec-parametrizacao-maui.json`
  - `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`
- Confirmar a atualização comparando manualmente o HEAD registrado em `vault-maui/status-project/STATUS-UPDATE-maui.md` com a nota usada no Project.

## 3) Checklist — Claude Code

- Apontar a sessão para o repositório correto.
- Instruir o modelo a ler primeiro:
  - `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md`
  - `vault-maui/status-project/STATUS-UPDATE-maui.md`
  - `vault-maui/00_core/contrato-precedencia-maui.md`
  - `vault-maui/00_core/principios-fundacionais-maui.md`
  - `vault-maui/00_core/system-prompt-maui.md`
  - `vault-maui/00_core/indice-maui.md`
  - `vault-maui/01_manifest/spec-parametrizacao-maui.json`
- Regras: não executar lotes sem pedido humano explícito; não promover status; não usar pastas runtime como fonte de Project.

## 4) Checklist — Codex

- Prompt mínimo para iniciar: "Leia `vault-maui/context-packages/current/2026-05-10-context-brief-status-atual-maui.md` e `vault-maui/status-project/STATUS-UPDATE-maui.md`, confirme HEAD, e apenas então responda."
- Confirmar `git rev-parse HEAD` antes de declarar status corrente.
- Não executar P0.2, P0.3, P0.4 ou qualquer lote sem pedido humano explícito.
- Não alterar normativos exceto quando houver pedido específico e escopo claro.

## 5) Checklist — ChatGPT Handoff

- Ordem de leitura: Context Brief current -> Status Update -> Handoff da sessão -> exec-report do pacote -> contratos do corpus se necessário.
- Sem filesystem verificável, declarar conformidade como `unknown` quando depender de hash, commit, arquivo local ou working tree.
- Não promover status de normativos.
- Não executar roadmap por inferência.

## 6) Troubleshooting

- Se o painel divergir da evidência, confiar em Git, exec-reports e status-project.
- Se houver drift entre instâncias, atualizar manualmente o pacote mínimo novamente.
- Se uma instância citar `vault-maui/memorias/` ou `vault-maui/status/` como fonte de Project, corrigir para `project-memories/` e `status-project/`.
- Se o HEAD local divergir do registrado no status, registrar a divergência antes de qualquer decisão.
