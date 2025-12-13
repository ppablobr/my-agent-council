# Changelog

All notable changes to this project are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- **How-to documentation** (`docs/GETTING_STARTED.md`, `docs/USAGE.md`, `docs/CUSTOMIZATION.md`)
- Documentation badge and section in README

---

## [0.1.0] - 2025-12-13

### Added
- **Agent Council framework** with 6 agents:
  - Master Agent (orchestration)
  - Product Manager (requirements, governance)
  - Software Engineer (implementation, conventions)
  - UX/UI Designer (design system, flows)
  - GitHub Agent (repo hygiene)
  - Plan Guardian (plan maintenance)
- **Governance structure** (`GOVERNANCE.md`, `PROJECT_RULES.md`)
- **Spec-driven workflow** with guardrails
- **ADR process** with first ADR (0001-spec-driven-development)
- **CI pipeline** with documentation checks
- **Agent specifications**:
  - `CODING_CONVENTIONS.md` — TypeScript/React patterns
  - `DATABASE_SCHEMA.md` — Supabase/RLS guidelines
  - `DESIGN_SYSTEM.md` — Tailwind/shadcn tokens
  - `UI_SPEC.md` — Page documentation format
  - `UX_FLOW.md` — User journey templates
- **Project planning docs** (`BACKLOG.md`, `ROADMAP.md`, `PLAN.md`, `RISKS.md`)
- **GitHub templates** (issue templates, PR template)
- **Guardrail scripts** (markdown links, plan sync, traceability)

### Backlog Completed
- BL-001: Establish governance + guardrails baseline
- BL-002: Add ADR process + decision log
- BL-003: Add GitHub templates + CI docs checks
- BL-004: Add how-to documentation guides
