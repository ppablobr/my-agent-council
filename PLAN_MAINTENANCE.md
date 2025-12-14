# Manutenção do plano

Este documento descreve o processo para garantir que `PLAN.md` permaneça atualizado com as mudanças mais recentes no codebase. Esse processo foi pensado para ser automatizado por um agente dedicado: o **Plan Guardian**.

## O agente Plan Guardian

O Plan Guardian monitora o codebase em busca de mudanças e garante que elas sejam refletidas no plano do projeto. Ele é um componente-chave das metodologias de Spec-Driven Development (SDD) e Vibe Coding, pois mantém o plano como a única fonte de verdade do projeto.

A documentação do Plan Guardian fica no diretório `plan_guardian/`.

## Processo de manutenção do plano

O Plan Guardian segue o processo descrito em `plan_guardian/README.md` e reforça os seguintes guardrails:

1. **Consistência de arquivos de plano:** `PLAN.md` e `plan.json` devem ser atualizados juntos.
2. **Integridade de docs:** links relativos em Markdown não podem quebrar.
3. **Rastreabilidade:** quando `app/` muda o comportamento do produto, pelo menos um artefato de spec/produto deve ser atualizado (`PRD.md`, backlog/roadmap, log de decisões ou ADR).

Esses checks são implementados como scripts do repositório e rodam no CI:

- `scripts/check_markdown_links.py`
- `scripts/guardrails/check_plan_files_in_sync.py`
- `scripts/guardrails/check_traceability.py`
- `.github/workflows/ci.yml`
