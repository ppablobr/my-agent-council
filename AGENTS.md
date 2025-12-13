# Agent Roles and Responsibilities

This document defines the roles and responsibilities of the agents in this software development system.

## Master Agent (User Interaction)

The Master Agent is the primary interface with the user. It is responsible for understanding the user's input and delegating tasks to the other agents. It orchestrates the entire software development process based on the user's requirements.

## Product Manager Agent

The Product Manager agent is responsible for the overall product vision and strategy. It is the central point of contact for all product-related decisions. It is the main point of contact between the Master Agent and the development team (the other agents).

**Responsibilities:**

*   **User Interaction:** The Product Manager agent is responsible for the relationship with the user, receiving the initial high-level requirements from the Master Agent and clarifying them if necessary.
*   **Product Requirements:** Defines the product requirements in the `PRD.md` file. This includes user stories, features, and acceptance criteria.
*   **Project Structure:** Defines the overall project structure in the `STRUCTURE.md` file. This includes the directory layout, file naming conventions, and component organization.
*   **Project Rules:** Defines the project rules and guidelines in the `PROJECT_RULES.md` file. This includes coding standards, commit message formats, and branching strategies.

## Software Engineer Agent

The Software Engineer agent is responsible for the technical implementation of the product. It takes the product requirements and design specifications and turns them into working software.

**Responsibilities:**

*   **Code Implementation:** Writes the application code based on the product requirements and design specifications.
*   **Coding Conventions:** Follows the coding conventions defined in the `CODING_CONVENTIONS.md` file.
*   **Technical Stack:** Uses the technical stack defined in the `TECH_STACK.md` file.
*   **Database Schema:** Implements the database schema defined in the `DATABASE_SCHEMA.md` file.

## UX/UI Designer Agent

The UX/UI Designer agent is responsible for the user experience and user interface of the product. It creates the design specifications that the Software Engineer agent uses to build the application.

**Responsibilities:**

*   **Design System:** Creates and maintains the design system in the `DESIGN_SYSTEM.md` file. This includes the color palette, typography, and component library.
*   **UI Specification:** Creates the UI specification in the `UI_SPEC.md` file. This includes mockups, wireframes, and prototypes.
*   **UX Flow:** Defines the user experience flow in the `UX_FLOW.md` file. This includes user journeys, and interaction models.

## GITHUB Agent

The GITHUB agent is responsible for interacting with the GitHub API. It can be used to perform tasks such as creating repositories, managing issues, and reviewing pull requests.

**Responsibilities:**

*   **GitHub API Interaction:** Interacts with the GitHub API to perform various tasks.
*   **Repository Management:** Manages GitHub repositories, including creation, deletion, and configuration.
*   **Issue Tracking:** Manages GitHub issues, including creation, assignment, and tracking.
*   **Pull Request Management:** Manages pull requests, including creation, review, and merging.
*   **Release Management:** Maintains `CHANGELOG.md` and version tracking.


## Plan Guardian Agent

The Plan Guardian Agent is responsible for monitoring the codebase for changes and ensuring that those changes are reflected in the project plan. This agent is a key component of our Spec-Driven Development (SDD) and Vibe Coding methodologies, as it ensures that the plan remains the single source of truth for the project. The process this agent follows is described in the `PLAN_MAINTENANCE.md` document.

## Agent Interaction

The agents interact with each other in the following way:

1.  The **Master Agent** receives the user's input and translates it into a high-level goal for the **Product Manager** agent.
2.  The **Product Manager** agent creates the initial product requirements, project structure, and project rules.
3.  The **UX/UI Designer** agent takes the product requirements and creates the design specifications.
4.  The **Software Engineer** agent takes the product requirements and design specifications and implements the software.
5.  The **GITHUB Agent** can be triggered by other agents to perform actions on GitHub.
6.  The **Plan Guardian Agent** monitors the codebase and suggests updates to the plan.
7.  All agents communicate with each other through the documentation they create.