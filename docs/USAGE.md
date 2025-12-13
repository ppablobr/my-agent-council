# Usage Guide

This guide explains how to work with each agent in the Agent Council.

## Working with Agents

The Agent Council uses a **spec-driven** approach where each agent has specific responsibilities and documentation they own.

### Invoking an Agent

When working with your AI assistant, you can invoke a specific agent by using prompts like:

```
Act as the [Agent Name] agent and [task description].
```

The AI will read the relevant specs and follow the established patterns.

---

## Product Manager Agent

**Owns:** `product_manager/PRD.md`, `BACKLOG.md`, `ROADMAP.md`, `RISKS.md`

### Common Tasks

| Task | Prompt Example |
|------|----------------|
| Define requirements | "As PM agent, help me write user stories for a shopping cart feature" |
| Prioritize backlog | "As PM agent, review and prioritize the items in BACKLOG.md" |
| Scope a milestone | "As PM agent, define scope for Milestone 1 in ROADMAP.md" |
| Assess risks | "As PM agent, identify risks for implementing payment processing" |

### Example Workflow

```markdown
User: "I want to add user profiles to my app"

PM Agent:
1. Creates user stories in BACKLOG.md with acceptance criteria
2. Updates PRD.md with the feature description
3. Assigns to a milestone in ROADMAP.md
4. Notes any risks in RISKS.md
```

---

## Software Engineer Agent

**Owns:** `software_engineer/CODING_CONVENTIONS.md`, `TECH_STACK.md`, `DATABASE_SCHEMA.md`, `app/`

### Common Tasks

| Task | Prompt Example |
|------|----------------|
| Implement feature | "As Eng agent, implement BL-005 following our conventions" |
| Add database table | "As Eng agent, add a `user_profiles` table following DATABASE_SCHEMA.md" |
| Review architecture | "As Eng agent, should we use SSR or CSR for this page?" |
| Create ADR | "As Eng agent, create an ADR for choosing Supabase as our backend" |

### Example Workflow

```markdown
User: "Implement the user profile feature (BL-005)"

Eng Agent:
1. Reads acceptance criteria from BACKLOG.md
2. Follows CODING_CONVENTIONS.md for code style
3. Creates database migration per DATABASE_SCHEMA.md patterns
4. Implements in app/ using TECH_STACK.md technologies
5. Updates PLAN.md and marks BL-005 as Done
```

---

## UX/UI Designer Agent

**Owns:** `ux_ui_designer/DESIGN_SYSTEM.md`, `UI_SPEC.md`, `UX_FLOW.md`

### Common Tasks

| Task | Prompt Example |
|------|----------------|
| Design component | "As UX agent, design a profile card component following our design system" |
| Document flow | "As UX agent, create a user journey for the checkout process in UX_FLOW.md" |
| Specify page | "As UX agent, document the dashboard page layout in UI_SPEC.md" |

### Example Workflow

```markdown
User: "Design the onboarding flow"

UX Agent:
1. Documents user journey in UX_FLOW.md
2. Specifies each screen in UI_SPEC.md
3. Ensures components use DESIGN_SYSTEM.md tokens
4. Notes interaction patterns and edge cases
```

---

## GitHub Agent

**Owns:** `.github/` templates, repository hygiene

### Common Tasks

| Task | Prompt Example |
|------|----------------|
| Create issue | "As GitHub agent, create an issue for the bug in user login" |
| Review PR checklist | "As GitHub agent, verify this PR meets our DoD" |
| Setup workflows | "As GitHub agent, add a CI workflow for running tests" |

---

## Plan Guardian Agent

**Owns:** `PLAN.md`, `plan.json`, consistency checks

### Common Tasks

| Task | Prompt Example |
|------|----------------|
| Sync plan files | "As Plan Guardian, ensure PLAN.md and plan.json are in sync" |
| Validate changes | "As Plan Guardian, run guardrail checks before I merge" |
| Update progress | "As Plan Guardian, mark completed items in PLAN.md" |

---

## Multi-Agent Collaboration

For complex features, agents collaborate:

```markdown
User: "Build a complete user authentication system"

1. PM Agent → Writes requirements in PRD.md, creates backlog items
2. UX Agent → Designs login/signup flows, documents in UI_SPEC.md
3. Eng Agent → Implements auth using Supabase, follows UX specs
4. GitHub Agent → Creates tracking issue, reviews PR
5. Plan Guardian → Updates PLAN.md, validates documentation
```

---

## Tips for Effective Use

1. **Be specific** — Reference backlog items (BL-XXX) and file names
2. **Start with PM** — Define requirements before implementation
3. **Update docs** — Ask agents to update their specs after changes
4. **Run guardrails** — Use `python3 scripts/check_markdown_links.py` before commits
5. **Record decisions** — Use DECISIONS.md for lightweight choices, ADRs for architecture
