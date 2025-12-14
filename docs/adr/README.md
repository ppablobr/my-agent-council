# Registros de Decisão de Arquitetura (ADRs)

ADRs registram decisões técnicas difíceis de reverter ou que moldam o sistema no longo prazo.

## Índice

| ADR | Título | Status |
| --- | --- | --- |
| [0001](./0001-spec-driven-development.md) | Metodologia de Spec-Driven Development | Aceito |

## Quando escrever um ADR

- Novos padrões de arquitetura (roteamento, gerenciamento de estado, acesso a dados)
- Decisões importantes de dependências ou stack
- Decisões sobre modelo de dados e persistência
- Escolhas de design relacionadas a segurança, privacidade ou conformidade

## Nomeação

- Use `docs/adr/NNNN-short-title.md` (sequência de 4 dígitos).
- Exemplo: `docs/adr/0002-auth-strategy.md`

## Template

Comece a partir de `docs/adr/0000-template.md`.
