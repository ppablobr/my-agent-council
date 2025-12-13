# Plan Maintenance

This document describes the process for ensuring that the `PLAN.md` file remains up-to-date with the latest changes in the codebase. This process is designed to be automated by a dedicated agent, the "Plan Guardian Agent".

## The Plan Guardian Agent

The Plan Guardian Agent is responsible for monitoring the codebase for changes and ensuring that those changes are reflected in the project plan. This agent is a key component of our Spec-Driven Development (SDD) and Vibe Coding methodologies, as it ensures that the plan remains the single source of truth for the project.

The documentation for the Plan Guardian Agent can be found in the `plan_guardian` directory.

## Process for Plan Maintenance

The Plan Guardian Agent follows the process described in `plan_guardian/README.md` and enforces the following guardrails:

1. **Plan file consistency:** `PLAN.md` and `plan.json` must be updated together.
2. **Docs integrity:** Markdown relative links must not break.
3. **Traceability:** When `app/` changes product behavior, at least one product/spec artifact is updated (`PRD.md`, backlog/roadmap, decision log, or ADR).

These checks are implemented as repository scripts and run in CI:

- `scripts/check_markdown_links.py`
- `scripts/guardrails/check_plan_files_in_sync.py`
- `scripts/guardrails/check_traceability.py`
- `.github/workflows/ci.yml`
