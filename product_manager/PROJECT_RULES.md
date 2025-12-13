# Project Rules

This document outlines the project rules.

## Plan Management

- The `PLAN.md` file in the root directory is the single source of truth for the project plan.
- The `PLAN.md` file must show the entire planning history, with completed tasks marked with `[x]`.
- The `plan.json` file is a machine-readable representation of the plan, and is kept in sync with `PLAN.md`.

## Definition of Done (DoD)

A work item is considered “done” only when all applicable criteria are met:

- **Clear acceptance criteria:** The user story has testable acceptance criteria (ideally in Gherkin form).
- **Docs updated:** Any impacted specs are updated (`PRD.md`, `STRUCTURE.md`, `PROJECT_RULES.md`, UX docs, and/or ADR/decision log).
- **Changelog updated:** User-facing changes are documented in `CHANGELOG.md` under `[Unreleased]`.
- **Quality gates:** Relevant tests and lint checks pass (or are explicitly documented as out-of-scope with a reason).
- **Traceability:** Pull requests reference the related story/issue and include a short summary of user impact.
- **Risk review:** New risks are added to `RISKS.md` when discovered; mitigations are proposed.

## User Story Format (Template)

Use this template for any backlog item that represents user value:

- **Title:** Short and specific
- **Story:** As a `<persona>`, I want `<capability>`, so that `<benefit>`.
- **Context:** Why now? What problem are we solving?
- **Acceptance criteria (Gherkin):**
  - Given `<state>`, when `<action>`, then `<outcome>`.
- **Non-goals:** What is explicitly not included?
- **Edge cases:** Error states, empty states, performance constraints
- **Dependencies:** APIs, other stories, decisions/ADRs

## Scope, Milestones, and Change Control

- Work is organized into **milestones** in `ROADMAP.md`.
- When a milestone starts, its scope is **frozen**: changes require PM approval and must be recorded as a new backlog item (do not silently rewrite in-progress stories).
- Bug fixes and critical security issues are allowed within a frozen milestone; they must still be logged and linked to the milestone.

## Traceability Rules

- Every pull request must reference at least one backlog item (issue/story) and describe user-facing impact.
- If a PR changes product behavior, at least one of the following must be updated: `PRD.md`, `BACKLOG.md`, `ROADMAP.md`, `DECISIONS.md`, or a relevant ADR in `docs/adr/`.
