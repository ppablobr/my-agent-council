# Recursos monitorados

Este documento descreve os recursos que o agente Plan Guardian deve monitorar para garantir que o plano do projeto permaneça atualizado.

## Arquivos e diretórios locais

O agente deve monitorar os seguintes arquivos e diretórios locais:

- `app/`: código-fonte da aplicação. Monitorar arquivos novos, modificados ou removidos.
- `.github/`: workflows de CI e templates (guardrails de processo).
- `scripts/`: scripts de validação/guardrails usados no CI.
- `docs/adr/`: Registros de Decisão de Arquitetura (decisões técnicas).
- `product_manager/`: documentação do agente Product Manager.
- `software_engineer/`: documentação do agente Software Engineer.
- `ux_ui_designer/`: documentação do agente UX/UI Designer.
- `github_agent/`: documentação do agente GitHub.
- `plan_guardian/`: documentação do próprio Plan Guardian.
- `*.md`: todos os arquivos Markdown na raiz, pois podem conter informações importantes do projeto.

## Sistema de controle de versão

O agente deve monitorar o repositório Git para os seguintes eventos:

- **Novos commits:** analisar mensagens para identificar o objetivo das mudanças.
- **Novas branches:** acompanhar branches para entender se se relacionam a feature/bug específico.
- **Novos pull requests:** acompanhar PRs para verificar se estão prontos para merge.

## Recursos em nuvem (futuro)

No futuro, o agente pode ser estendido para monitorar recursos de nuvem, como:

- **AWS GuardDuty:** para detectar ameaças de segurança.
- **AWS Route 53 Recovery Control Config:** para garantir resiliência da aplicação.

Ao monitorar esses recursos, o Plan Guardian pode fornecer uma visão abrangente do status do projeto e garantir que o plano esteja sempre atualizado.
