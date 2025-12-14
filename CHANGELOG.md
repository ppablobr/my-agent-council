# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Adicionado
- **Guias de documentação (how-to)** (`docs/GETTING_STARTED.md`, `docs/USAGE.md`, `docs/CUSTOMIZATION.md`)
- Badge e seção de documentação no README

---

## [0.1.0] - 2025-12-13

### Adicionado
- **Framework do Agent Council** com 6 agentes:
  - Master Agent (orquestração)
  - Product Manager (requisitos, governança)
  - Software Engineer (implementação, convenções)
  - UX/UI Designer (design system, fluxos)
  - Agente GitHub (higiene do repositório)
  - Plan Guardian (manutenção do plano)
- **Estrutura de governança** (`GOVERNANCE.md`, `PROJECT_RULES.md`)
- **Workflow spec-driven** com guardrails
- **Processo de ADR** com o primeiro ADR (0001-spec-driven-development)
- **Pipeline de CI** com verificações de documentação
- **Especificações dos agentes**:
  - `CODING_CONVENTIONS.md` — padrões TypeScript/React
  - `DATABASE_SCHEMA.md` — diretrizes Supabase/RLS
  - `DESIGN_SYSTEM.md` — tokens Tailwind/shadcn
  - `UI_SPEC.md` — formato de documentação de páginas
  - `UX_FLOW.md` — templates de jornadas do usuário
- **Documentos de planejamento** (`BACKLOG.md`, `ROADMAP.md`, `PLAN.md`, `RISKS.md`)
- **Templates do GitHub** (templates de issues, template de PR)
- **Scripts de guardrails** (links Markdown, sincronia do plano, rastreabilidade)

### Backlog concluído
- BL-001: Estabelecer governança + baseline de guardrails
- BL-002: Adicionar processo de ADR + log de decisões
- BL-003: Adicionar templates do GitHub + checks de docs no CI
- BL-004: Adicionar guias “como fazer” (how-to)
