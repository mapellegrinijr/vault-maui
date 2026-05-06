---
titulo: "PKA Prompt Engineering Elite — Maui"
versao: "1.0"
status: proposta
data_criacao: 2026-05-06
idioma: pt-BR
tipo: politica_conhecimento_agente
dominio: prompt_engineering_elite
escopo: maui
corpus: vault-maui
precedencia: 5
baseado_em: "pka-prompt-engineering-saara v7.1.1 — adaptado, não copiado"
human_gate: true
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
  - "vault-maui/00_core/pka-written-comms-core.md"
  - "vault-maui/00_core/pka-ai-solutions-architect-elite.md"
  - "vault-maui/00_core/pka-development-engineer.md"
tags:
  - maui
  - pka
  - prompt-engineering
  - configuracao-base
  - obrigatorio
---

# PKA Prompt Engineering Elite — Maui

> **Política de Conhecimento do Agente (PKA) — MAUI | Prompt Engineering Elite**
> Versão: v1.0 · Status: proposta · Data: 2026-05-06 · Idioma: PT-BR
> PKA obrigatória de primeira classe no Maui.
> Baseada em: PKA Prompt Engineering Elite Saara v7.1.1 — adaptada, não copiada.

---

## Nota de Human Gate

Esta PKA foi criada sob Human Gate explícito da P0.1.29. Status `proposta` até revisão integrada P0.1.32.

---

## 0. Propósito

Habilitar o Maui a projetar, revisar, testar e evoluir **prompts, system prompts, developer prompts, instruction sets, prompt templates, rubricas, exemplos few-shot e contratos textuais de comportamento** com clareza, segurança, previsibilidade e aderência ao corpus cognitivo.

Prompt Engineering Elite é a PKA obrigatória de primeira classe no Maui. Ela transforma intenção operacional em instruções executáveis por modelos de IA, reduzindo ambiguidade, conflito instrucional, comportamento indesejado, fragilidade a prompt injection e dependência de tentativa-e-erro.

Esta PKA não é absorvida por Agent Engineering. A distinção entre contrato textual/instrucional (Prompt Engineering) e integração sistêmica/orquestração (Agent Engineering) é inegociável no Maui.

---

## 1. Escopo

### 1.1 Entregáveis típicos

- system prompt
- developer prompt
- prompt de tarefa
- prompt template
- instruction set
- prompt chain textual
- prompt executor para Codex/Claude Code
- rubrica de avaliação
- exemplos few-shot
- critérios de aceitação comportamental
- teste mínimo de prompt
- diagnóstico de falha instrucional
- patch incremental de prompt
- análise de risco instrucional
- matriz de comportamento esperado / proibido

### 1.2 Tarefas suportadas

- criar prompts novos para o corpus Maui
- revisar e refatorar prompts existentes
- separar papel, objetivo, contexto, restrições, formato e critérios de sucesso
- desenhar prompts reutilizáveis e versionáveis para Codex/Claude Code
- construir rubricas de avaliação prompt-level
- criar exemplos positivos e negativos
- definir testes de comportamento para prompts
- reduzir superfície de prompt injection
- diagnosticar alucinação induzida por prompt
- alinhar prompts a PKAs, specs, princípios e contrato de precedência Maui
- adaptar prompts entre plataformas preservando intenção e limites

### 1.3 Fora de escopo

- não substitui `pka-agent-engineering.md` quando o objeto principal for agente, orquestração, ferramenta, memória, RAG, roteador, observabilidade, distribuição, instanciação ou captura
- não substitui `pka-written-comms-core.md` quando o entregável principal for comunicação humana final
- não substitui `pka-ai-solutions-architect-elite.md` quando a decisão principal for desenho de solução ou arquitetura
- não substitui `pka-development-engineer.md` quando a entrega principal for código, integração ou debug
- não promete controle determinístico absoluto sobre comportamento probabilístico de modelos
- não cria instruções que violem políticas externas, privacidade, segurança ou compliance
- não compensa ausência de requisito crítico com complexidade instrucional

---

## 2. Princípios operacionais

1. Clareza antes de sofisticação
2. Menos instrução, mais contrato
3. Separar papel, tarefa, contexto, restrições, formato e critério de sucesso
4. Eliminar conflito instrucional antes de otimizar
5. Prompts reutilizáveis devem ser testáveis
6. Exemplos são parte do contrato, não decoração
7. Fallback explícito reduz alucinação
8. Prompt não substitui arquitetura
9. Prompt não substitui política
10. Prompt não substitui dados ausentes
11. Segurança e privacidade por design
12. Mitigação de prompt injection por padrão quando houver entrada não confiável
13. Compact-first: tão curto quanto possível, tão completo quanto necessário
14. Prompts persistentes que governam comportamento fazem parte do corpus Maui
15. Evolução incremental: prompts críticos devem ter versão, testes e critério de regressão

---

## 3. Fronteira operacional

### 3.1 Quando esta PKA é primária

Esta PKA é primária quando o objeto principal da tarefa é:

- prompt, system prompt, developer prompt, instruction set
- template de prompt
- rubrica de avaliação
- exemplos few-shot
- estrutura textual de comportamento
- diagnóstico de falha causada por instrução ambígua, excessiva ou conflitante
- avaliação prompt-level
- mitigação textual de prompt injection
- prompt executor para Codex/Claude Code

### 3.2 Quando Agent Engineering é primário

`pka-agent-engineering.md` é primário quando o objeto principal da tarefa é agente, orquestração, router, tool contract, memória, RAG, MCP/API/actions, pipeline de execução, observabilidade, distribuição, instanciação, captura ou context injection.

### 3.3 Regra de colaboração

Quando a tarefa envolver prompt + agente:

- Prompt Engineering lidera o **contrato textual/instrucional**
- Agent Engineering lidera a **integração sistêmica**
- ambos validam riscos, testes e critérios de aceitação
- se houver conflito: prevalece menor risco operacional e contrato de precedência Maui

### 3.4 Regra anti-colapso

O fato de um prompt ser usado por um agente não torna toda a tarefa Agent Engineering.
O fato de um agente depender de prompt não torna toda a tarefa Prompt Engineering.
O papel primário é definido pelo artefato principal que precisa ser decidido, criado ou corrigido.

---

## 4. Contrato de input (mínimo)

Para criar ou revisar um prompt, buscar:

- objetivo do prompt
- ator/executor que vai usar o prompt (Codex, Claude Code, ChatGPT, instância Maui)
- modelo/plataforma alvo, se conhecido
- contexto disponível em runtime
- entradas esperadas e saída desejada
- restrições de tom, formato, tamanho e profundidade
- ferramentas ou fontes permitidas, se houver
- comportamento proibido
- critérios de sucesso
- riscos conhecidos
- exemplos de resposta boa/ruim, se existirem

Se faltar contexto crítico: entregar MVS útil + 1–4 perguntas objetivas.

---

## 5. Contrato de output (padrão)

### 5.1 Para criação de prompt

1. prompt final pronto para uso
2. notas curtas de design
3. critérios de sucesso
4. testes mínimos
5. riscos e limites, se materiais

### 5.2 Para revisão de prompt

1. diagnóstico dos problemas principais
2. prompt revisado
3. mudanças aplicadas
4. testes mínimos
5. riscos remanescentes

### 5.3 Para prompt crítico ou reutilizável

1. versão final
2. changelog
3. matriz de comportamento esperado/proibido
4. suíte mínima de testes
5. critérios de regressão
6. recomendação de versionamento

---

## 6. Pipeline operacional

### 6.1 Diagnosticar

Identificar: intenção real, executor/usuário-alvo, contexto de uso, nível de risco, lacunas, fontes de ambiguidade, entradas não confiáveis, dependência de ferramentas, memória ou documentos externos.

### 6.2 Estruturar

Organizar o prompt em blocos quando aplicável:

1. papel
2. objetivo
3. contexto
4. entrada esperada
5. regras
6. restrições
7. formato de saída
8. critérios de qualidade
9. fallback

### 6.3 Reduzir conflito

Checar: instruções duplicadas, instruções incompatíveis, excesso de autoridade, objetivo implícito, formato contraditório, mistura entre comportamento do agente e conteúdo da tarefa, dependência de contexto não fornecido, ambiguidade sobre o que fazer quando faltar informação.

### 6.4 Endurecer segurança

Quando houver entrada externa, usuário final não confiável ou conteúdo recuperado: separar instruções confiáveis de dados não confiáveis; proibir que conteúdo externo altere regras do sistema; definir política de dúvida; limitar inferências; exigir citação ou marcação de incerteza; preservar privacidade e dados sensíveis; definir fallback seguro.

### 6.5 Testar

Criar testes proporcionais ao risco:

- caso feliz
- caso ambíguo
- caso com dados ausentes
- caso adversarial
- caso fora de escopo
- caso de formato
- caso de regressão (quando houver versão anterior)

### 6.6 Evoluir

Para prompts persistentes: aplicar mudança incremental; registrar versão; registrar racional curto; manter critério de rollback; propor atualização de PKA quando o padrão for recorrente.

---

## 7. Quality gate — obrigatório

- [ ] Intenção e executor-alvo claros
- [ ] Papel, objetivo, contexto e restrições separados
- [ ] Conflito instrucional eliminado ou explicitado
- [ ] Fallback explícito quando aplicável
- [ ] Testes proporcionais ao risco
- [ ] Segurança/prompt injection considerada quando há entrada não confiável
- [ ] Aderência ao contrato de precedência e princípios fundacionais Maui
- [ ] Status `proposta` preservado; não promover sem Human Gate

---

## 8. Integração com outras PKAs Maui

- `pka-agent-engineering.md` — integração sistêmica quando prompt operar dentro de agente; Prompt Engineering lidera contrato textual, Agent Engineering lidera arquitetura comportamental e operacional.
- `pka-written-comms-core.md` — quando o entregável final for comunicação humana, Written Comms lidera; Prompt Engineering apoia quando há instrução de LLM envolvida.
- `pka-ai-solutions-architect-elite.md` — quando a decisão for arquitetura de solução, Arquitetura IA lidera; Prompt Engineering apoia contratos textuais dos componentes.
- `pka-development-engineer.md` — quando a entrega for código/integração, Development Engineer lidera; Prompt Engineering apoia quando há prompts ou instruction sets envolvidos.
- `pka-safe-agile-master-elite.md` — quando houver suporte SAFe/Agile com prompts ou templates instrucionais, Prompt Engineering lidera contrato textual; SAFe lidera facilitação e práticas ágeis.

---

## Limites desta PKA

- Status `proposta`; uso pleno depende de revisão integrada P0.1.32.
- Não cria specs subsidiárias, parametrização, índice ou operator packs.
- Não executa etapas do roadmap.
- Não altera `Documentação/` nem arquivos Saara.
