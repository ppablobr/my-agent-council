# Papéis e responsabilidades dos agentes

Este documento define os papéis e responsabilidades dos agentes neste sistema de desenvolvimento de software.

## Master Agent (interação com o usuário)

O Master Agent é a interface principal com o usuário. Ele entende a solicitação do usuário e delega tarefas para os demais agentes. Ele orquestra todo o processo de desenvolvimento com base nos requisitos do usuário.

## Agente Product Manager (PM)

O agente Product Manager é responsável pela visão e estratégia do produto. Ele é o ponto central de decisão em assuntos de produto e a ponte entre o Master Agent e o time de execução (os demais agentes).

**Responsabilidades:**

* **Interação com o usuário:** conduz o relacionamento com o usuário, recebendo requisitos de alto nível do Master Agent e pedindo esclarecimentos quando necessário.
* **Requisitos do produto:** define os requisitos em `PRD.md` (histórias, funcionalidades e critérios de aceitação).
* **Estrutura do projeto:** define a estrutura geral em `STRUCTURE.md` (layout de diretórios, convenções de nomes e organização de componentes).
* **Regras do projeto:** define regras e diretrizes em `PROJECT_RULES.md` (padrões, processos e governança).

## Agente Software Engineer (Engenharia)

O agente Software Engineer é responsável pela implementação técnica do produto. Ele pega os requisitos e as especificações de design e transforma em software funcionando.

**Responsabilidades:**

* **Implementação:** escreve o código da aplicação com base nos requisitos e especificações.
* **Convenções de código:** segue as convenções definidas em `CODING_CONVENTIONS.md`.
* **Stack técnica:** utiliza a stack definida em `TECH_STACK.md`.
* **Esquema de banco de dados:** segue e evolui o esquema definido em `DATABASE_SCHEMA.md`.

## Agente UX/UI Designer

O agente UX/UI Designer é responsável pela experiência do usuário e pela interface do produto. Ele cria as especificações de design que o agente de Engenharia usa para construir a aplicação.

**Responsabilidades:**

* **Design system:** cria e mantém o design system em `DESIGN_SYSTEM.md` (cores, tipografia e biblioteca de componentes).
* **Especificação de UI:** cria a especificação de UI em `UI_SPEC.md` (mockups, wireframes e protótipos).
* **Fluxo de UX:** define fluxos e jornadas em `UX_FLOW.md` (jornadas, interações e modelos de comportamento).

## Agente GitHub

O agente GitHub é responsável por interagir com a API do GitHub. Ele pode ser usado para tarefas como criar repositórios, gerenciar issues e revisar pull requests.

**Responsabilidades:**

* **Interação com a API do GitHub:** executa tarefas via API do GitHub.
* **Gestão de repositórios:** gerencia repositórios (criação, remoção e configuração).
* **Gestão de issues:** gerencia issues (criação, atribuição e acompanhamento).
* **Gestão de pull requests:** gerencia PRs (criação, revisão e merge).
* **Gestão de releases:** mantém `CHANGELOG.md` e versionamento.

## Agente Plan Guardian

O agente Plan Guardian monitora o codebase em busca de mudanças e garante que elas sejam refletidas no plano do projeto. Ele é um componente-chave das metodologias de Spec-Driven Development (SDD) e Vibe Coding, pois mantém o plano como a única fonte de verdade. O processo é descrito em `PLAN_MAINTENANCE.md`.

## Interação entre agentes

Os agentes interagem da seguinte forma:

1. O **Master Agent** recebe a solicitação do usuário e a traduz em um objetivo de alto nível para o **Product Manager**.
2. O **Product Manager** cria requisitos iniciais, estrutura do projeto e regras do projeto.
3. O **UX/UI Designer** transforma requisitos em especificações de design.
4. O **Software Engineer** implementa o software com base nos requisitos e especificações.
5. O **Agente GitHub** pode ser acionado por outros agentes para executar ações no GitHub.
6. O **Plan Guardian** monitora o codebase e sugere atualizações no plano.
7. Todos os agentes se comunicam entre si por meio da documentação que produzem.
