---
titulo: "Marco de memória — Decisão de normalização estrutural do vault Maui"
versao: "1.0"
status: ativo
data_criacao: 2026-05-05
idioma: pt-BR
tipo: memoria_decisao
escopo: projeto_maui
confidencialidade: interna
tags:
  - maui
  - p0-1-17
  - diagnostico-estrutural
  - normalizacao
  - roadmap
  - context-brief
deve_ser_considerado_em_context_brief: true
---

# Marco de memória — Decisão de normalização estrutural do vault Maui

## Resumo

Antes de executar a P0.1.17, foi tomada a decisão de ampliar o escopo da etapa: em vez de diagnosticar apenas a divergência `vault-maui/memoria/` vs `vault-maui/memorias/`, a P0.1.17 passará a ser um diagnóstico estrutural completo do vault Maui.

O objetivo é identificar divergências de estrutura antes de aplicar qualquer correção, para que a normalização seja planejada em subetapas explícitas no roadmap.

## Decisão

A P0.1.17 será tratada como:

**P0.1.17 — Diagnóstico estrutural do vault Maui**

Essa etapa deve ser somente diagnóstica e propositiva. Ela não deve corrigir, mover, renomear, apagar ou reescrever arquivos existentes.

## Motivação

Durante o fechamento da Tarefa 2 / saneamento inicial de `Documentação/`, foi detectada uma divergência estrutural entre:

- `vault-maui/memoria/`
- `vault-maui/memorias/`

A partir dessa divergência, decidiu-se ampliar o diagnóstico para procurar outras inconsistências estruturais antes de seguir com P0.1.5, P0.3/P0.4 ou instanciação manual do Maui.

## Subetapas de normalização a incluir no roadmap

A normalização estrutural será planejada em lotes futuros, a serem incorporados ao roadmap como subetapas após o diagnóstico P0.1.17.

### Lote 1 — Memórias

Objetivo:
- normalizar ou compatibilizar `vault-maui/memoria/` vs `vault-maui/memorias/`;
- garantir que memórias relevantes, especialmente as marcadas com `deve_ser_considerado_em_context_brief: true`, sejam encontradas por futuros `Maui Context Briefs`.

### Lote 2 — Referências e wikilinks

Objetivo:
- identificar e corrigir referências obsoletas;
- atualizar wikilinks apontando para nomes antigos;
- revisar referências a `Documentação/`, arquivos promovidos ao `00_core/`, arquivos arquivados e placeholders como `[[...]]`, `[[link]]` e `[[wikilink]]`.

### Lote 3 — Frontmatter e slugs

Objetivo:
- normalizar frontmatter mínimo;
- detectar YAML inválido, campos ausentes, status inconsistentes e tipos documentais divergentes;
- padronizar slugs, versões e nomes de arquivos, reduzindo inconsistências como underscores vs hífens e padrões `v_0_1`, `v0-1`, `v0.1`.

### Lote 4 — Context Brief readiness

Objetivo:
- garantir que o template de `Maui Context Brief` consiga localizar memórias, handoffs, exec-reports, insights, inventários e atualizações relevantes;
- verificar se o template aponta para diretórios corretos;
- assegurar que memórias marcadas para Context Brief sejam priorizadas sem copiar conteúdo integral por padrão.

### Lote 5 — Instanciação manual Maui

Objetivo:
- avaliar e consolidar os artefatos necessários para uma primeira instanciação manual confiável;
- verificar presença de `00_core/system-prompt.md`;
- verificar PKAs herdadas em `00_core/pka-*.md`;
- verificar operator packs;
- verificar context package bootstrap/current;
- garantir regra para instância sem filesystem declarar `unknown`, nunca `current`;
- preparar base para um marco futuro de instanciação manual mínima.

## Regras de execução

- A P0.1.17 não aplica correções.
- Qualquer normalização real deve ocorrer apenas em etapas posteriores e com aprovação humana explícita.
- Cada lote de correção deve ser pequeno, validável e commitado separadamente.
- Mudanças normativas continuam exigindo Human Gate.
- Nenhuma etapa deve inventar origem, intenção, status, hash ou decisão ausente.
- Fatos, inferências e hipóteses devem ser separados.

## Efeito operacional

A P0.1.17 deixa de ser um diagnóstico pontual de diretórios de memória e passa a ser o diagnóstico estrutural que orientará a normalização do vault Maui.

O roadmap deve incorporar as subetapas de normalização estrutural antes de avançar para atividades dependentes de estrutura estável, como:

- retomada profunda da P0.1.5;
- operator packs;
- context packages;
- instanciação manual;
- automações futuras;
- validações locais mais amplas.

## Instrução para Context Brief

Ao criar um `Maui Context Brief` para qualquer uma das frentes abaixo:

- P0.1.17;
- normalização estrutural;
- memória;
- Context Brief readiness;
- instanciação manual;
- roadmap;
- continuação Saara→Maui;

consultar esta memória e refletir:

- a decisão de ampliar P0.1.17;
- os cinco lotes futuros de normalização;
- a regra de não corrigir nada durante o diagnóstico;
- a necessidade de Human Gate antes de aplicar qualquer normalização;
- a dependência entre estrutura estável e instanciação manual.

## Próximo passo recomendado

Executar P0.1.17 como diagnóstico estrutural completo do vault Maui, criando apenas inventário diagnóstico e exec-report.