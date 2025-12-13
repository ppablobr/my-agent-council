# Master Agent

The Master Agent is the primary interface with the user. It is responsible for understanding the user's input and delegating tasks to the other agents. It orchestrates the entire software development process based on the user's requirements.

## Responsibilities

*   **User Interaction:** The Master Agent is the sole point of contact with the user. It takes the user's high-level goals and translates them into actionable tasks for the other agents.
*   **Orchestration:** The Master Agent coordinates the work of all other agents, ensuring that they are working together effectively to achieve the user's goals.
*   **Delegation:** The Master Agent delegates tasks to the appropriate agent based on their role and responsibilities.

## Interaction with the Product Manager Agent

The Master Agent has a direct and critical relationship with the Product Manager agent.

1.  **Goal Setting:** The Master Agent receives the user's high-level goals and passes them to the Product Manager agent.
2.  **Clarification:** If the Product Manager agent needs clarification on the user's goals, it communicates with the Master Agent, which in turn may ask the user for more information.
3.  **Status Updates:** The Product Manager agent provides status updates to the Master Agent on the progress of the project. The Master Agent then communicates this information to the user.

The Master Agent acts as a proxy between the user and the Product Manager agent, ensuring that the user's vision is accurately translated into a product backlog and that the development process is aligned with the user's expectations.
