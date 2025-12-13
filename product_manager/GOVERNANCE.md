# Governance

This document defines how the agent council makes decisions, manages scope, and stays aligned.

## Decision Rights (RACI-lite)

Legend: **R** = Responsible (does the work), **A** = Accountable (final decision), **C** = Consulted, **I** = Informed.

| Area | Master Agent | Product Manager | Software Engineer | UX/UI Designer | GitHub Agent | Plan Guardian |
| --- | --- | --- | --- | --- | --- | --- |
| User communication & prioritization | A/R | C | I | I | I | I |
| PRD, backlog, roadmap, risks | C | A/R | C | C | I | I |
| UX flows, UI spec, design system | I | C | C | A/R | I | I |
| Architecture & implementation | I | C | A/R | C | I | I |
| Repo hygiene (issues/PR templates) | I | C | C | I | A/R | C |
| Changelog & releases | I | C | C | I | A/R | I |
| Plan consistency (PLAN.md ↔ plan.json) | I | C | C | I | I | A/R |


## How Decisions Are Made

1. **Prefer written decisions.** Product/UX/tech decisions are recorded in `DECISIONS.md`.
2. **Use ADRs for technical architecture.** Anything with long-term impact (stack choices, major patterns, persistence decisions) gets an ADR in `docs/adr/`.
3. **Escalation path.** If agents cannot converge, the Master Agent escalates to the user with options, trade-offs, and a recommended choice.

## Cadence

- **Backlog grooming:** as-needed; minimum weekly when active development.
- **Milestone review:** at milestone start (scope freeze) and end (retro + decision log update).

