# Decisões

Este log registra decisões de produto/processo que devem ser fáceis de encontrar sem precisar ler histórico de chat.

Use ADRs (`docs/adr/`) para decisões de arquitetura técnica com impacto de longo prazo.

## Formato de decisão

Cada entrada deve incluir:

- **Data**
- **Decisão**
- **Status:** Proposta / Aceita / Rejeitada / Substituída
- **Contexto:** por que isso foi necessário
- **Consequências:** o que muda por causa disso
- **Links:** ADRs, itens de backlog, PRs

## Log

### 2025-12-13 — Estabelecer baseline de governança + DoD

- **Status:** Aceita
- **Contexto:** Precisávamos de um processo durável para o Agent Council evitar “spec drift” e “scope creep”.
- **Consequências:** DoD, regras de congelamento de escopo e requisitos de rastreabilidade agora estão explícitos.
- **Links:** `product_manager/GOVERNANCE.md`, `product_manager/PROJECT_RULES.md`, `BACKLOG.md`, `ROADMAP.md`, `RISKS.md`

### 2025-12-13 — Adotar Spec-Driven Development como metodologia central

- **Status:** Aceita
- **Contexto:** Formalizamos a abordagem spec-driven como um ADR para referência de longo prazo.
- **Consequências:** Todos os agentes seguem fluxo “spec-first”; guardrails reforçam atualização de documentação.
- **Links:** ADR `docs/adr/0001-spec-driven-development.md`, BL-002
