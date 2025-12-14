# Agente GitHub

O Agente GitHub é responsável por interagir com a API do GitHub. Ele pode ser usado para tarefas como criar repositórios, gerenciar issues e revisar pull requests.

## Responsabilidades

* **Interação com a API do GitHub:** Interage com a API do GitHub para executar várias tarefas. O agente usa o token de `mcp.json` para autenticar na API do GitHub.
* **Gestão de repositórios:** Gerencia repositórios no GitHub, incluindo criação, remoção e configuração.
* **Gestão de issues:** Gerencia issues no GitHub, incluindo criação, atribuição e acompanhamento.
* **Gestão de pull requests:** Gerencia pull requests, incluindo criação, revisão e merge.

## Uso

O Agente GitHub pode ser acionado por outros agentes para executar ações no GitHub. Por exemplo, o agente Software Engineer pode acionar o Agente GitHub para criar um novo repositório ou um novo pull request.

## Nota de segurança

- Não faça commit de tokens: mantenha `mcp.json` local e fora do controle de versão (ele é ignorado via `.gitignore`).
- Use `mcp.json.example` como template e defina `GITHUB_PERSONAL_ACCESS_TOKEN`.
