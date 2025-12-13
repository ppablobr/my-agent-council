# ADR 0001: Spec-Driven Development Methodology

## Status

Accepted

## Context

When building software products with multiple stakeholders (product, engineering, design), teams often face:

- **Spec drift:** Documentation becomes stale as code evolves, leading to confusion about intended behavior.
- **Scope creep:** Requirements expand mid-development without formal acknowledgment.
- **Knowledge silos:** Critical decisions live only in individuals' heads or scattered chat messages.
- **Inconsistent quality:** No shared definition of "done" means variable output quality.

We needed a durable process that keeps the agent council aligned and prevents these anti-patterns.

## Decision

We adopt **Spec-Driven Development (SDD)** as our core governance methodology. This means:

1. **Specification documents are the source of truth** for product behavior, not code or verbal agreements.
2. **All changes flow through documented specs** before implementation (`PRD.md`, `BACKLOG.md`, UI specs, etc.).
3. **Automated guardrails** enforce that code changes are accompanied by spec updates (or explicit override).
4. **Decisions are recorded** in `DECISIONS.md` for lightweight choices and `docs/adr/` for architectural decisions with long-term impact.

### Key Artifacts

| Artifact | Owner | Purpose |
| --- | --- | --- |
| `PRD.md` | Product Manager | High-level product requirements |
| `BACKLOG.md` | Product Manager | Prioritized work items with acceptance criteria |
| `ROADMAP.md` | Product Manager | Milestones and scope boundaries |
| `DESIGN_SYSTEM.md`, `UI_SPEC.md`, `UX_FLOW.md` | UX/UI Designer | Design specifications |
| `CODING_CONVENTIONS.md`, `TECH_STACK.md`, `DATABASE_SCHEMA.md` | Software Engineer | Technical specifications |
| `docs/adr/*.md` | All agents | Architectural decisions |
| `PLAN.md` / `plan.json` | Plan Guardian | Execution plan (human + machine readable) |

## Alternatives Considered

- **Agile with only user stories:** Rejected because it often leads to undocumented technical decisions and relies on synchronous communication.
- **Code-as-documentation:** Rejected because code doesn't capture "why" decisions were made or what alternatives were considered.
- **Wiki-based documentation:** Rejected because wikis tend to become stale; co-locating docs with code and enforcing via CI is more durable.

## Consequences

### Positive

- Single source of truth for product behavior
- Decisions are traceable and reversible
- New team members can onboard from documentation
- CI guardrails catch drift early

### Negative

- Initial overhead to write specs before coding
- Requires discipline to maintain documentation
- Risk of over-documentation (mitigated by keeping specs focused)

### Risks Introduced

- R-001: Spec drift (mitigated by CI guardrails and Plan Guardian)
- R-002: Scope creep (mitigated by milestone scope freeze)

## Links

- Backlog: BL-001, BL-002
- Related decisions: `DECISIONS.md`
- Governance: `product_manager/GOVERNANCE.md`
- Project Rules: `product_manager/PROJECT_RULES.md`
