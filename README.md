<div align="center">
  <h1>Agent Council for Product Development</h1>
  <p><strong>Um “sistema operacional” spec-driven</strong> para construir produtos com um conselho de agentes (PM, Eng, UX, etc.) e colaboração via documentação durável.</p>

  <p>
    <a href="./AGENTS.md"><img alt="Agents" src="https://img.shields.io/badge/agents-council-6f42c1"></a>
    <a href="./docs/adr/README.md"><img alt="ADRs" src="https://img.shields.io/badge/ADRs-enabled-8a2be2"></a>
    <a href="./PLAN_MAINTENANCE.md"><img alt="Plan Guardian" src="https://img.shields.io/badge/guardrails-CI-green"></a>
    <a href="./.github/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/badge/CI-configured-1f6feb"></a>
  </p>

  <p>
    <em>Para usar badge real do GitHub Actions, troque <code>OWNER/REPO</code> e use:</em><br/>
    <code>https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg</code>
  </p>
</div>

---

## Índice

- [O que é](#o-que-é)
- [Agentes](#agentes)
- [Como trabalhamos (Spec-Driven)](#como-trabalhamos-spec-driven)
- [Começando rápido](#começando-rápido)
- [Documentos principais](#documentos-principais)
- [Guardrails (Automação)](#guardrails-automação)
- [ADRs](#adrs)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Contribuição](#contribuição)

## O que é

Um workflow opinionado para:

- transformar um objetivo do usuário em requisitos claros
- especificar UX/UI com artefatos versionados
- implementar com convenções e stack acordadas
- evitar “spec drift” (docs != código) via guardrails e CI

## Agentes

- **Master Agent:** interface com o usuário e orquestração ([`AGENT_MASTER.md`](AGENT_MASTER.md))
- **Product Manager:** requisitos, estrutura e regras ([`product_manager/`](product_manager/))
- **UX/UI Designer:** design system, UI spec e UX flow ([`ux_ui_designer/`](ux_ui_designer/))
- **Software Engineer:** implementação e padrões técnicos ([`software_engineer/`](software_engineer/))
- **GitHub Agent:** higiene de issues/PRs e operações GitHub ([`github_agent/`](github_agent/))
- **Plan Guardian:** manutenção do plano e guardrails ([`plan_guardian/`](plan_guardian/), [`PLAN_MAINTENANCE.md`](PLAN_MAINTENANCE.md))

Definições completas: [`AGENTS.md`](AGENTS.md)

## Como trabalhamos (Spec-Driven)

1. **Captura de intenção** → [`product_manager/PRD.md`](product_manager/PRD.md)
2. **Quebra em itens pequenos** → [`BACKLOG.md`](BACKLOG.md) com critérios de aceitação
3. **Milestones e scope freeze** → [`ROADMAP.md`](ROADMAP.md)
4. **Riscos sempre visíveis** → [`RISKS.md`](RISKS.md)
5. **Decisões registradas**
   - log leve → [`DECISIONS.md`](DECISIONS.md)
   - decisões técnicas duráveis → ADRs em [`docs/adr/`](docs/adr/)
6. **Implementação** → [`app/`](app/) seguindo [`software_engineer/`](software_engineer/)
7. **Guardrails** → CI + scripts (abaixo)

## Começando rápido

1. Leia a governança e o DoD:
   - [`product_manager/GOVERNANCE.md`](product_manager/GOVERNANCE.md)
   - [`product_manager/PROJECT_RULES.md`](product_manager/PROJECT_RULES.md)
2. Escolha um item no [`BACKLOG.md`](BACKLOG.md) e garanta critérios de aceitação.
3. Se a mudança for arquitetural, crie um ADR:
   - template: [`docs/adr/0000-template.md`](docs/adr/0000-template.md)
4. Antes de abrir PR, rode o check de docs:

```bash
python3 scripts/check_markdown_links.py
```

## Documentos principais

- Planejamento: [`BACKLOG.md`](BACKLOG.md), [`ROADMAP.md`](ROADMAP.md), [`PLAN.md`](PLAN.md), [`plan.json`](plan.json)
- Decisões: [`DECISIONS.md`](DECISIONS.md), [`docs/adr/`](docs/adr/)
- Governança e regras: [`product_manager/GOVERNANCE.md`](product_manager/GOVERNANCE.md), [`product_manager/PROJECT_RULES.md`](product_manager/PROJECT_RULES.md)
- Riscos: [`RISKS.md`](RISKS.md)
- Manutenção do plano: [`PLAN_MAINTENANCE.md`](PLAN_MAINTENANCE.md), [`plan_guardian/`](plan_guardian/)

## Guardrails (Automação)

Checks base (rodando em CI via [`.github/workflows/ci.yml`](.github/workflows/ci.yml)):

- links relativos em Markdown válidos → [`scripts/check_markdown_links.py`](scripts/check_markdown_links.py)
- `PLAN.md` e `plan.json` atualizados juntos → [`scripts/guardrails/check_plan_files_in_sync.py`](scripts/guardrails/check_plan_files_in_sync.py)
- mudanças em `app/` exigem atualização de algum spec (ou override) → [`scripts/guardrails/check_traceability.py`](scripts/guardrails/check_traceability.py)

Rodar localmente:

```bash
python3 scripts/check_markdown_links.py
python3 scripts/guardrails/check_plan_files_in_sync.py
python3 scripts/guardrails/check_traceability.py
```

Observação: alguns guardrails dependem de contexto Git (usam `git diff`).

## ADRs

- Index: [`docs/adr/README.md`](docs/adr/README.md)
- Template: [`docs/adr/0000-template.md`](docs/adr/0000-template.md)
- Padrão de nome: `docs/adr/NNNN-short-title.md`

## Estrutura do repositório

- `app/` — código da aplicação (quando existir)
- `product_manager/`, `software_engineer/`, `ux_ui_designer/` — specs por papel
- `docs/adr/` — decisões arquiteturais
- `scripts/` — automações e guardrails
- `.github/` — templates e CI

## Contribuição

- Siga o DoD em [`product_manager/PROJECT_RULES.md`](product_manager/PROJECT_RULES.md)
- Conecte PRs a um item de backlog e atualize specs quando o comportamento mudar
- Use ADRs para decisões técnicas difíceis de reverter
