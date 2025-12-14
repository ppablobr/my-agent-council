# Regras do projeto

Este documento descreve as regras do projeto.

## Gestão do plano

- O arquivo `PLAN.md` na raiz é a única fonte de verdade do plano do projeto.
- `PLAN.md` deve mostrar todo o histórico do planejamento, com tarefas concluídas marcadas com `[x]`.
- `plan.json` é uma representação legível por máquina do plano e deve ficar em sincronia com `PLAN.md`.

## Definition of Done (DoD)

Um item de trabalho só é considerado “concluído” quando todos os critérios aplicáveis forem atendidos:

- **Critérios de aceitação claros:** a história tem critérios testáveis (idealmente em Gherkin).
- **Docs atualizadas:** specs impactadas são atualizadas (`PRD.md`, `STRUCTURE.md`, `PROJECT_RULES.md`, docs de UX e/ou ADR/log de decisões).
- **Changelog atualizado:** mudanças visíveis ao usuário são registradas em `CHANGELOG.md` em `[Unreleased]`.
- **Gates de qualidade:** testes e lint relevantes passando (ou explicitamente fora de escopo com motivo).
- **Rastreabilidade:** PRs referenciam a história/issue relacionada e incluem um resumo curto do impacto no usuário.
- **Revisão de riscos:** novos riscos são adicionados a `RISKS.md` quando descobertos, com propostas de mitigação.

## Formato de história de usuário (template)

Use este template para qualquer item do backlog que represente valor para o usuário:

- **Título:** curto e específico
- **História:** como `<persona>`, eu quero `<capacidade>`, para `<benefício>`.
- **Contexto:** por que agora? qual problema estamos resolvendo?
- **Critérios de aceitação (Gherkin):**
  - Dado `<estado>`, quando `<ação>`, então `<resultado>`.
- **Não objetivos:** o que explicitamente não está incluído?
- **Casos de borda:** erros, estados vazios, restrições de performance
- **Dependências:** APIs, outras histórias, decisões/ADRs

## Escopo, marcos e controle de mudanças

- O trabalho é organizado em **marcos** em `ROADMAP.md`.
- Ao iniciar um marco, seu escopo é **congelado**: mudanças exigem aprovação do PM e devem ser registradas como novo item de backlog (não reescreva silenciosamente histórias em andamento).
- Correções de bug e issues críticas de segurança podem entrar em um marco congelado, mas devem ser registradas e linkadas ao marco.

## Regras de rastreabilidade

- Todo pull request deve referenciar pelo menos um item do backlog (issue/história) e descrever o impacto para o usuário.
- Se um PR mudar o comportamento do produto, pelo menos um dos seguintes arquivos deve ser atualizado: `PRD.md`, `BACKLOG.md`, `ROADMAP.md`, `DECISIONS.md` ou um ADR relevante em `docs/adr/`.
