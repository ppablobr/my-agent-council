# Decisions

This log captures product/process decisions that should be easy to discover without reading chat history.

Use ADRs (`docs/adr/`) for technical architecture decisions with long-term impact.

## Decision Format

Each entry should include:

- **Date**
- **Decision**
- **Status:** Proposed / Accepted / Rejected / Superseded
- **Context:** why this was needed
- **Consequences:** what changes because of it
- **Links:** ADRs, backlog items, PRs

## Log

### 2025-12-13 — Establish baseline governance + DoD

- **Status:** Accepted
- **Context:** Needed a durable process for the agent council to avoid spec drift and scope creep.
- **Consequences:** DoD, scope-freeze rules, and traceability requirements are now explicit.
- **Links:** `product_manager/GOVERNANCE.md`, `product_manager/PROJECT_RULES.md`, `BACKLOG.md`, `ROADMAP.md`, `RISKS.md`

### 2025-12-13 — Adopt Spec-Driven Development as core methodology

- **Status:** Accepted
- **Context:** Formalized the spec-driven approach as an ADR for long-term reference.
- **Consequences:** All agents follow spec-first workflow; guardrails enforce documentation.
- **Links:** ADR `docs/adr/0001-spec-driven-development.md`, BL-002

