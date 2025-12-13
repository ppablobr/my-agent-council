# Guardrails

Guardrails are automated checks that are used to enforce the project rules and policies. They are a key component of our development process, as they help to ensure that the codebase remains consistent, maintainable, and secure.

The Plan Guardian Agent uses guardrails to monitor the codebase and the project plan. If a guardrail is violated, the agent will take action to correct the problem.

## Example: The Math Guardrail

The `math_guardrail` function is a simple example of a guardrail. This function checks if a given input is a math homework question. If it is, the function returns a response indicating that it cannot answer the question.

This guardrail is used to prevent the agent from being used to cheat on math homework.

## Guardrails in this Project

In this project, we use guardrails to enforce a variety of rules, including:

-   **Plan Consistency:** The Plan Guardian Agent uses a guardrail to ensure that the `PLAN.md` file is consistent with the `plan.json` file. If the two files are out of sync, the agent will automatically update the `PLAN.md` file.
-   **Code Style:** We can use a linter as a guardrail to enforce a consistent code style across the project. If a developer commits code that does not conform to the code style, the CI/CD pipeline will fail.
-   **Security:** We can use a security scanner as a guardrail to detect potential security vulnerabilities in the codebase. If a vulnerability is found, the agent will create an issue in the issue tracker.
-   **Resource Management:** Inspired by the AWS GuardDuty and Route 53 Recovery Control Config examples, we can create guardrails to monitor the use of cloud resources and ensure that they are being used efficiently and securely.

## Implemented Guardrails (Baseline)

- **Docs integrity:** `scripts/check_markdown_links.py` validates relative links across `*.md`.
- **Plan consistency:** `scripts/guardrails/check_plan_files_in_sync.py` enforces “change both or change neither” for `PLAN.md` ↔ `plan.json`.
- **Traceability:** `scripts/guardrails/check_traceability.py` ensures `app/` changes are accompanied by updates to at least one spec artifact (or an explicit override).

These run in CI via `.github/workflows/ci.yml`.

Guardrails are a powerful tool for automating the enforcement of project rules and policies. By using guardrails, we can improve the quality of our codebase and reduce the amount of manual work required to maintain the project.
