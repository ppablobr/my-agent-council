# Guardrails

Guardrails são verificações automatizadas usadas para reforçar regras e políticas do projeto. Eles são parte importante do processo, pois ajudam a manter o codebase consistente, sustentável e seguro.

O agente Plan Guardian usa guardrails para monitorar o codebase e o plano do projeto. Se um guardrail for violado, o agente toma ações para corrigir o problema.

## Exemplo: o guardrail de matemática

A função `math_guardrail` é um exemplo simples de guardrail. Ela verifica se a entrada é uma pergunta de lição de casa de matemática. Se for, a função retorna uma resposta indicando que não pode responder.

Esse guardrail serve para evitar que o agente seja usado para “colar” em tarefas de matemática.

## Guardrails neste projeto

Aqui, usamos guardrails para reforçar várias regras, incluindo:

- **Consistência do plano:** o Plan Guardian garante que `PLAN.md` esteja consistente com `plan.json`. Se estiverem fora de sincronia, o agente atualiza automaticamente `PLAN.md`.
- **Estilo de código:** um linter pode atuar como guardrail para reforçar estilo consistente. Se alguém commitar código fora do padrão, o pipeline falha.
- **Segurança:** um scanner de segurança pode detectar vulnerabilidades. Se encontrar algo, o agente pode criar uma issue.
- **Gestão de recursos:** inspirado por exemplos como AWS GuardDuty e Route 53 Recovery Control Config, podemos criar guardrails para monitorar recursos de nuvem e garantir uso eficiente e seguro.

## Guardrails implementados (baseline)

- **Integridade de docs:** `scripts/check_markdown_links.py` valida links relativos em `*.md`.
- **Consistência do plano:** `scripts/guardrails/check_plan_files_in_sync.py` reforça “mudar ambos ou nenhum” para `PLAN.md` ↔ `plan.json`.
- **Rastreabilidade:** `scripts/guardrails/check_traceability.py` garante que mudanças em `app/` venham acompanhadas de atualização de ao menos um artefato de spec (ou override explícito).

Esses checks rodam no CI via `.github/workflows/ci.yml`.

Guardrails são uma ferramenta poderosa para automatizar o reforço de regras do projeto. Ao usar guardrails, melhoramos a qualidade do codebase e reduzimos trabalho manual de manutenção.
