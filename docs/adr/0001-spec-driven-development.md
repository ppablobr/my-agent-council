# ADR 0001: Metodologia de Spec-Driven Development (SDD)

## Status

Aceito

## Context

Ao construir produtos de software com múltiplos stakeholders (produto, engenharia, design), times frequentemente enfrentam:

- **Spec drift:** a documentação fica desatualizada conforme o código evolui, gerando confusão sobre o comportamento esperado.
- **Scope creep:** requisitos expandem no meio do desenvolvimento sem reconhecimento formal.
- **Silos de conhecimento:** decisões críticas ficam apenas na cabeça de pessoas ou perdidas em mensagens.
- **Qualidade inconsistente:** sem uma definição compartilhada de "pronto", a qualidade varia.

Precisávamos de um processo durável que mantenha o conselho de agentes alinhado e evite esses anti-patterns.

## Decisão

Adotamos **Spec-Driven Development (SDD)** como metodologia central de governança. Isso significa:

1. **Documentos de especificação são a fonte de verdade** do comportamento do produto, e não o código ou acordos verbais.
2. **Toda mudança passa por specs documentadas** antes de implementar (`PRD.md`, `BACKLOG.md`, specs de UI etc.).
3. **Guardrails automatizados** reforçam que mudanças no código venham acompanhadas de atualização de specs (ou override explícito).
4. **Decisões são registradas** em `DECISIONS.md` (decisões leves) e em `docs/adr/` (decisões arquiteturais de longo prazo).

### Key Artifacts

| Artefato | Responsável | Finalidade |
| --- | --- | --- |
| `PRD.md` | Product Manager | Requisitos de alto nível do produto |
| `BACKLOG.md` | Product Manager | Itens priorizados com critérios de aceitação |
| `ROADMAP.md` | Product Manager | Marcos e limites de escopo |
| `DESIGN_SYSTEM.md`, `UI_SPEC.md`, `UX_FLOW.md` | UX/UI Designer | Especificações de design |
| `CODING_CONVENTIONS.md`, `TECH_STACK.md`, `DATABASE_SCHEMA.md` | Software Engineer | Especificações técnicas |
| `docs/adr/*.md` | Todos os agentes | Decisões arquiteturais |
| `PLAN.md` / `plan.json` | Plan Guardian | Plano de execução (legível por humanos e máquinas) |

## Alternatives Considered

- **Ágil com apenas histórias de usuário:** rejeitado porque tende a gerar decisões técnicas não documentadas e depende de comunicação síncrona.
- **Código como documentação:** rejeitado porque o código não registra o "porquê" das decisões nem alternativas consideradas.
- **Documentação em wiki:** rejeitado porque wikis tendem a ficar desatualizadas; manter docs junto do código e reforçar via CI é mais durável.

## Consequences

### Positive

- Fonte única de verdade do comportamento do produto
- Decisões rastreáveis e mais fáceis de revisar/reverter
- Onboarding de novas pessoas via documentação
- Guardrails no CI detectam drift cedo

### Negative

- Overhead inicial para escrever specs antes de codar
- Exige disciplina para manter documentação
- Risco de documentação excessiva (mitigado mantendo specs focadas)

### Risks Introduced

- R-001: Spec drift (mitigado por guardrails no CI e Plan Guardian)
- R-002: Scope creep (mitigado por congelamento de escopo em marcos)

## Links

- Backlog: BL-001, BL-002
- Decisões relacionadas: `DECISIONS.md`
- Governança: `product_manager/GOVERNANCE.md`
- Regras do projeto: `product_manager/PROJECT_RULES.md`
