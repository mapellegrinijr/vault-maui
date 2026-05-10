---
titulo: "Princípios Fundacionais do Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: principios_normativos
escopo: projeto_maui
confidencialidade: interna
precedencia: 3
fase_origem: P0.1.26
human_gate: true
referencias:
  - "vault-maui/00_core/contrato-precedencia-maui.md"
  - "vault-maui/00_core/arquitetura-maui-v0-2.md"
  - "vault-maui/project/roadmap/roadmap-desenvolvimento-maui-v1-0.md"
  - "vault-maui/00_core/spec-funcionalidades-maui-v0-1.md"
  - "vault-maui/00_core/spec-tecnica-atualizacao-saara-maui-v2.md"
  - "vault-maui/planos/2026-05-06-p0-1-25-plano-configuracao-base-maui.md"
  - "vault-maui/context-packages/current/2026-05-06-context-brief-pos-p0-1-25-configuracao-base.md"
tags:
  - maui
  - principios
  - configuracao-base
  - precedencia
  - prompt-engineering
  - human-gate
---

# Princípios Fundacionais do Maui

## Nota de Human Gate

Este documento foi criado na P0.1.26 sob Human Gate explícito do usuário para iniciar a base normativa da Configuração-base Maui. A autorização cobre apenas princípios fundacionais e contrato de precedência.

Esta etapa não promove o status geral do Maui, não cria system prompt, especificação completa, PKAs, specs subsidiárias, parametrização, índice core, operator packs ou context packages finais.

## Finalidade

Definir os princípios normativos iniciais do Maui para orientar a criação futura da Configuração-base e reduzir ambiguidade antes de system prompt, especificação completa, PKAs e parametrização.

## Relação com Saara

Maui é um corpus/projeto separado do Saara. Saara pode servir como referência conceitual, histórica e de/para curado, mas não deve ser copiado integralmente para Maui sem decisão humana explícita.

Princípios Saara podem ser herdados ou adaptados quando fizerem sentido, mas devem ser reexpressos em termos Maui, com escopo, precedência e limites próprios do projeto Maui.

## Princípios

### 1. Corpus Maui como fonte de verdade

O corpus versionado em `vault-maui/` é a fonte de verdade para identidade, governança, memória, comportamento esperado e evolução do Maui. Ferramentas, painéis, scripts, MCP servers, operator packs e instâncias de modelo são mecanismos auxiliares.

### 2. Separação Saara/Maui

Saara e Maui são corpus/projetos distintos. Referências Saara podem orientar adaptação, mas decisões Maui exigem registro próprio. Conteúdo Saara não deve ser importado integralmente para Maui sem curadoria, Human Gate e justificativa.

### 3. Configuração-base antes de operator packs

Operator packs P0.3, context packages/bootstrap P0.4 e instruções target-specific dependem da Configuração-base Maui. Criar packs antes da base aumenta risco de cristalizar comportamento incompleto.

### 4. Contrato antes de automação

Contratos normativos, precedência, critérios de pronto e limites devem preceder scripts complexos, automações, hooks, plugins e integrações. Quando houver conflito, a automação deve seguir o contrato vigente ou parar.

### 5. Read-only antes de write

Diagnóstico, inventário, validação e leitura precedem alterações persistentes. Escrita em documentos normativos exige escopo definido, evidência e Human Gate quando alterar comportamento ou precedência.

### 6. Handoff/contexto mínimo antes de integração profunda

Retomadas por instâncias sem filesystem devem usar context briefs mínimos, verificáveis e orientados a evidência. Integrações profundas, bootstrap final e instanciação manual dependem de configuração-base e validação posteriores.

### 7. Human Gate para mudanças normativas

Mudanças que criem, alterem ou promovam documentos normativos, PKAs, system prompt, especificação completa, parametrização, operator packs finais ou bootstrap exigem Human Gate explícito e registro em exec-report.

### 8. Conformidade verificável

Estados como `current`, `ativo`, concluído ou conforme exigem evidência verificável por filesystem, hash, commit ou arquivo anexado. Sem evidência verificável, usar `unknown`, especialmente para ChatGPT/Handoff.

### 9. Prompt Engineering como competência obrigatória

Prompt Engineering Elite é competência obrigatória do Maui. Ela responde por prompts, system prompts, developer prompts, instruction sets, templates, rubricas, testes prompt-level, diagnóstico de falha instrucional e mitigação textual de prompt injection.

### 10. Agent Engineering como competência de integração/orquestração

Agent Engineering lidera agentes, tools, memória, RAG, orquestração, roteamento, observabilidade, distribuição, instanciação, captura e rollout. Ela não absorve Prompt Engineering.

### 11. Context Engineering/Context Brief como mecanismo de retomada

Context Engineering organiza Write, Select, Compress e Isolate. Context Briefs são mecanismos de retomada e transferência de contexto; não substituem configuração-base, exec-reports, inventários ou evidência de filesystem.

### 12. Memória seletiva, sanitizada e canônica

Memórias de projeto/gestação vivem em `vault-maui/project-memories/`. Memórias operacionais de runtime devem ser seletivas, sanitizadas, rastreáveis e canônicas em `vault-maui/memorias/` quando o Maui operar. Memórias com `deve_ser_considerado_em_context_brief: true` devem ser priorizadas em retomadas.

## Limites do documento

- Não é system prompt Maui.
- Não é especificação completa Maui.
- Não cria PKAs Maui.
- Não cria parametrização ou índice core.
- Não cria operator packs ou bootstrap.
- Não executa P0.1.11, P0.1.27 ou instanciação manual.
- Não promove `status: proposta`.

## F/I/H

### Fatos

- P0.1.25 definiu P0.1.26 como lote para princípios e contrato de precedência.
- P0.1.26 recebeu Human Gate explícito do usuário para criação normativa limitada.
- Prompt Engineering Elite foi decidido como competência obrigatória do Maui.
- A Configuração-base Maui ainda não existe como pacote completo.

### Inferências

- Princípios explícitos reduzem risco de operator packs e context packages serem criados sobre base incompleta.
- A regra `unknown` é necessária para impedir falsa conformidade em ambientes sem filesystem ou hash.

### Hipóteses

- Parte dos princípios Saara continuará útil para Maui, desde que adaptada e registrada em linguagem Maui.
- A fronteira explícita Prompt Engineering/Agent Engineering reduzirá conflitos na criação futura de system prompt, PKAs e operator packs.
