---
titulo: Regras operacionais — interação Saara ↔ Executor de Codificação
versao: 1.0
status: proposta
data_criacao: 2026-05-04
idioma: pt-BR
tipo: regra_operacional
escopo: projeto_maui
precedencia: alta
---

# Regras operacionais — interação Saara ↔ Executor de Codificação

Este documento governa a interação entre instâncias Saara e qualquer executor de codificação (Codex, Claude Code e futuros), garantindo continuidade entre sessões e disciplina de avanço incremental. As regras aqui registradas são fonte única de verdade para o comportamento esperado nessa interação e devem ser respeitadas independentemente do modelo ou interface utilizada.

A ausência dessas regras produz ambiguidade na marcação de prompts e tendência de extrapolação de etapas, comprometendo a rastreabilidade e o controle incremental do projeto. Este documento corrige esse vácuo de forma explícita e versionada.

## REGRA 1 — Marcação de prompts executáveis

Todo bloco que deva ser copiado e executado por um executor de codificação precisa estar identificado com o cabeçalho explícito "PROMPT PARA EXECUTOR DE CODIFICAÇÃO". Comandos internos a um prompt não devem ser confundidos com comandos sugeridos ao usuário fora do prompt. Esta regra aplica-se a Codex, Claude Code e quaisquer executores futuros.

## REGRA 2 — Processamento turno-a-turno de retornos do executor

Após cada retorno do executor de codificação, a instância Saara deve:
1. Analisar apenas o último resultado executado.
2. Classificar como: aceito | aceito com ressalva | precisa correção.
3. Indicar somente o próximo passo imediato.
4. Gerar no máximo um prompt para o executor por vez.
5. Não extrapolar várias etapas futuras nem propor normalizações não solicitadas se o resultado atual for suficiente.

## Maui Context Brief sob demanda

Quando o usuário pedir para "criar context brief", "gerar context brief", "preparar contexto", "retomar tarefa", "continuar trabalho com contexto" ou expressão equivalente, o Codex deve criar um `Maui Context Brief`.

O Context Brief deve usar como referência primária o template `vault-maui/context-packages/templates/maui-context-brief.template.md` e deve ser salvo preferencialmente em `vault-maui/context-packages/current/YYYY-MM-DD-context-brief-<slug>.md`.

Antes de criar o brief, o Codex deve consultar, quando existirem e forem relevantes:

- `vault-maui/00_core/`
- `vault-maui/memorias/` ou pasta equivalente de memórias
- adendos
- insights
- handoffs
- exec-reports
- review-reports
- inventários
- atualizações recentes do corpus

O Codex deve carregar apenas o contexto materialmente necessário, evitando copiar o corpus inteiro.

Se faltar documento essencial, o Codex deve:

1. declarar a lacuna;
2. explicar o impacto;
3. pedir ao usuário o menor conjunto de documentos/anexos necessário;
4. não inventar conteúdo, status, versões, hashes ou decisões;
5. se possível, oferecer continuidade degradada com confiança marcada.

O Codex deve registrar no próprio Context Brief:

- fontes consultadas;
- fontes ausentes;
- decisões fechadas;
- pendências;
- próximo passo recomendado.
