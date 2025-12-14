# Governança

Este documento define como o conselho de agentes toma decisões, gerencia escopo e mantém alinhamento.

## Direitos de decisão (RACI-lite)

Legenda: **R** = Responsável (executa), **A** = Accountable (decisão final), **C** = Consultado, **I** = Informado.

| Área | Master Agent | Product Manager | Software Engineer | UX/UI Designer | Agente GitHub | Plan Guardian |
| --- | --- | --- | --- | --- | --- | --- |
| Comunicação com usuário e priorização | A/R | C | I | I | I | I |
| PRD, backlog, roadmap, riscos | C | A/R | C | C | I | I |
| Fluxos de UX, UI spec, design system | I | C | C | A/R | I | I |
| Arquitetura e implementação | I | C | A/R | C | I | I |
| Higiene do repositório (templates de issue/PR) | I | C | C | I | A/R | C |
| Changelog e releases | I | C | C | I | A/R | I |
| Consistência do plano (PLAN.md ↔ plan.json) | I | C | C | I | I | A/R |


## Como as decisões são tomadas

1. **Prefira decisões por escrito.** Decisões de produto/UX/tech são registradas em `DECISIONS.md`.
2. **Use ADRs para arquitetura técnica.** Tudo que tiver impacto de longo prazo (stack, padrões principais, persistência) vira um ADR em `docs/adr/`.
3. **Caminho de escalonamento.** Se os agentes não convergirem, o Master Agent escala ao usuário com opções, trade-offs e uma recomendação.

## Cadência

- **Refinamento de backlog:** conforme necessário; no mínimo semanal quando houver desenvolvimento ativo.
- **Revisão de marcos:** no início (congelamento de escopo) e no fim (retro + atualização do log de decisões).
