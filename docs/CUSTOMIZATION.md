# Customization Guide

This guide explains how to adapt the Agent Council to your specific project needs.

## Customizing the Tech Stack

### 1. Update `software_engineer/TECH_STACK.md`

Replace the default stack with your choices:

```markdown
# Tech Stack

- **Frontend:** Next.js, TypeScript, Chakra UI
- **Backend:** Node.js, Express, PostgreSQL
- **Infrastructure:** AWS, Docker
```

### 2. Update Related Specs

After changing the stack, update:

| File | What to Change |
|------|----------------|
| `CODING_CONVENTIONS.md` | Adjust conventions for your language/framework |
| `DATABASE_SCHEMA.md` | Update for your database (PostgreSQL, MongoDB, etc.) |
| `DESIGN_SYSTEM.md` | Align with your UI library |

---

## Customizing Agent Roles

### Adding a New Agent

1. **Create agent directory:**

```bash
mkdir qa_engineer
```

2. **Add README.md with responsibilities:**

```markdown
# QA Engineer Agent

The QA Engineer is responsible for testing strategy and quality assurance.

**Responsibilities:**
- Test plan creation
- Test case documentation
- Bug triage and verification
```

3. **Update `AGENTS.md`** to include the new agent in the roster and interaction flow.

4. **Update `product_manager/GOVERNANCE.md`** to add RACI entries for the new agent.

### Modifying Agent Responsibilities

Edit `AGENTS.md` to reassign tasks. For example, to have the PM agent own technical documentation:

```markdown
## Product Manager Agent

**Responsibilities:**
- ...existing items...
- **Technical Documentation:** Owns API documentation and integration guides
```

---

## Customizing Governance

### Change the Definition of Done

Edit `product_manager/PROJECT_RULES.md`:

```markdown
## Definition of Done (DoD)

A work item is "done" when:
- [ ] Code review approved by 2 reviewers
- [ ] Integration tests pass
- [ ] Documentation updated
- [ ] Deployed to staging
```

### Adjust RACI Matrix

Edit `product_manager/GOVERNANCE.md` to change accountability:

```markdown
| Area | PM | Eng | UX | DevOps |
| --- | --- | --- | --- | --- |
| Infrastructure | I | C | I | A/R |
| API Design | C | A/R | I | I |
```

---

## Customizing Guardrails

### Modify CI Checks

Edit `.github/workflows/ci.yml` to add or remove checks:

```yaml
# Add test coverage check
- name: Check coverage
  run: npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
```

### Add Custom Guardrails

Create a new script in `scripts/guardrails/`:

```python
#!/usr/bin/env python3
"""Check for TODO comments without issue links."""

import re
import sys
from pathlib import Path

def check_todos():
    issues = []
    for file in Path('app').rglob('*.ts'):
        content = file.read_text()
        for i, line in enumerate(content.splitlines(), 1):
            if 'TODO' in line and not re.search(r'TODO\(.+\):', line):
                issues.append(f"{file}:{i}: TODO without owner")
    
    if issues:
        print("\\n".join(issues))
        sys.exit(1)
    print("OK: all TODOs have owners")

if __name__ == "__main__":
    check_todos()
```

Add to CI workflow:

```yaml
- name: TODO format check
  run: python3 scripts/guardrails/check_todos.py
```

---

## Customizing Templates

### Issue Templates

Edit files in `.github/ISSUE_TEMPLATE/`:

- `bug_report.yml` — Bug report format
- `feature_request.yml` — Feature request format

### PR Template

Edit `.github/pull_request_template.md` to match your process.

### ADR Template

Edit `docs/adr/0000-template.md` to add sections relevant to your project.

---

## Project-Specific Adaptations

### For Mobile Apps

- Add `ios/` and `android/` to structure
- Create `mobile_engineer/` agent folder
- Update DESIGN_SYSTEM.md for mobile patterns

### For Microservices

- Create separate folders per service
- Add `devops/` or `platform_engineer/` agent
- Update DATABASE_SCHEMA.md for multi-database patterns

### For Teams

- Add team-specific RACI entries
- Create on-call or rotation documentation
- Add deployment runbooks to `docs/`
