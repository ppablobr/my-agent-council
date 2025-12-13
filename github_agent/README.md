# GITHUB Agent

The GITHUB agent is responsible for interacting with the GitHub API. It can be used to perform tasks such as creating repositories, managing issues, and reviewing pull requests.

## Responsibilities

*   **GitHub API Interaction:** Interacts with the GitHub API to perform various tasks. The agent uses the token from `mcp.json` to authenticate with the GitHub API.
*   **Repository Management:** Manages GitHub repositories, including creation, deletion, and configuration.
*   **Issue Tracking:** Manages GitHub issues, including creation, assignment, and tracking.
*   **Pull Request Management:** Manages pull requests, including creation, review, and merging.

## Usage

The GITHUB agent can be triggered by other agents to perform actions on GitHub. For example, the Software Engineer agent can trigger the GITHUB agent to create a new repository or a new pull request.

## Security Note

- Do not commit tokens: keep `mcp.json` local and untracked (it is ignored via `.gitignore`).
- Use `mcp.json.example` as a template and set `GITHUB_PERSONAL_ACCESS_TOKEN`.
