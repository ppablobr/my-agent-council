# Monitored Resources

This document describes the resources that the Plan Guardian Agent should monitor to ensure that the project plan remains up-to-date.

## Local Files and Directories

The agent should monitor the following local files and directories for changes:

-   `app/`: The application source code. The agent should monitor this directory for new, modified, or deleted files.
-   `.github/`: CI workflows and templates (process guardrails).
-   `scripts/`: Guardrail and validation scripts used by CI.
-   `docs/adr/`: Architecture Decision Records (technical decisions).
-   `product_manager/`: The documentation for the Product Manager agent.
-   `software_engineer/`: The documentation for the Software Engineer agent.
-   `ux_ui_designer/`: The documentation for the UX/UI Designer agent.
-   `github_agent/`: The documentation for the GITHUB agent.
-   `plan_guardian/`: The documentation for the Plan Guardian Agent itself.
-   `*.md`: All markdown files in the root directory, as they may contain important information about the project.

## Version Control System

The agent should monitor the Git repository for the following events:

-   **New commits:** The agent should analyze the commit messages to identify the purpose of the changes.
-   **New branches:** The agent should monitor new branches to see if they are related to a specific feature or bug fix.
-   **New pull requests:** The agent should monitor new pull requests to see if they are ready to be merged.

## Cloud Resources (Future)

In the future, the agent could be extended to monitor cloud resources, such as:

-   **AWS GuardDuty:** To detect security threats.
-   **AWS Route 53 Recovery Control Config:** To ensure the resilience of the application.

By monitoring these resources, the Plan Guardian Agent can provide a comprehensive view of the project's status and ensure that the project plan is always up-to-date.
