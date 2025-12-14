# Guia de uso

Este guia explica como trabalhar com cada agente no Agent Council.

## Trabalhando com agentes

O Agent Council usa uma abordagem **spec-driven** em que cada agente tem responsabilidades específicas e documentação sob sua responsabilidade.

### Como invocar um agente

Ao trabalhar com seu assistente de IA, você pode invocar um agente específico usando prompts como:

```
Aja como o agente [Nome do agente] e [descrição da tarefa].
```

A IA vai ler as specs relevantes e seguir os padrões estabelecidos.

---

## Agente Product Manager (PM)

**Owns:** `product_manager/PRD.md`, `BACKLOG.md`, `ROADMAP.md`, `RISKS.md`

### Tarefas comuns

| Tarefa | Exemplo de prompt |
|------|----------------|
| Definir requisitos | "Como agente PM, me ajude a escrever histórias de usuário para um carrinho de compras" |
| Priorizar backlog | "Como agente PM, revise e priorize os itens em BACKLOG.md" |
| Definir escopo de marco | "Como agente PM, defina o escopo do Marco 1 em ROADMAP.md" |
| Avaliar riscos | "Como agente PM, identifique riscos para implementar processamento de pagamentos" |

### Exemplo de workflow

```markdown
Usuário: "Quero adicionar perfis de usuário no meu app"

Agente PM:
1. Cria histórias de usuário em `BACKLOG.md` com critérios de aceitação
2. Atualiza `PRD.md` com a descrição da funcionalidade
3. Atribui a um marco em `ROADMAP.md`
4. Registra riscos em `RISKS.md`
```

---

## Agente Software Engineer (Engenharia)

**Owns:** `software_engineer/CODING_CONVENTIONS.md`, `TECH_STACK.md`, `DATABASE_SCHEMA.md`, `app/`

### Tarefas comuns

| Tarefa | Exemplo de prompt |
|------|----------------|
| Implementar funcionalidade | "Como agente Eng, implemente BL-005 seguindo nossas convenções" |
| Adicionar tabela no banco | "Como agente Eng, adicione a tabela `user_profiles` seguindo DATABASE_SCHEMA.md" |
| Revisar arquitetura | "Como agente Eng, devemos usar SSR ou CSR para esta página?" |
| Criar ADR | "Como agente Eng, crie um ADR sobre escolher Supabase como backend" |

### Exemplo de workflow

```markdown
Usuário: "Implemente a funcionalidade de perfil de usuário (BL-005)"

Agente Eng:
1. Lê os critérios de aceitação em `BACKLOG.md`
2. Segue `CODING_CONVENTIONS.md` para estilo de código
3. Cria migração do banco conforme `DATABASE_SCHEMA.md`
4. Implementa em `app/` usando a stack de `TECH_STACK.md`
5. Atualiza `PLAN.md` e marca BL-005 como concluído
```

---

## Agente UX/UI Designer

**Owns:** `ux_ui_designer/DESIGN_SYSTEM.md`, `UI_SPEC.md`, `UX_FLOW.md`

### Tarefas comuns

| Tarefa | Exemplo de prompt |
|------|----------------|
| Desenhar componente | "Como agente UX, desenhe um componente de card de perfil seguindo o design system" |
| Documentar fluxo | "Como agente UX, crie uma jornada do usuário para o checkout em UX_FLOW.md" |
| Especificar página | "Como agente UX, documente o layout do dashboard em UI_SPEC.md" |

### Exemplo de workflow

```markdown
Usuário: "Desenhe o fluxo de onboarding"

Agente UX:
1. Documenta a jornada do usuário em `UX_FLOW.md`
2. Especifica cada tela em `UI_SPEC.md`
3. Garante que os componentes usem tokens de `DESIGN_SYSTEM.md`
4. Registra padrões de interação e casos de borda
```

---

## Agente GitHub

**Owns:** `.github/` templates, repository hygiene

### Tarefas comuns

| Tarefa | Exemplo de prompt |
|------|----------------|
| Criar issue | "Como agente GitHub, crie uma issue para o bug no login" |
| Revisar checklist do PR | "Como agente GitHub, verifique se este PR atende ao DoD" |
| Configurar workflows | "Como agente GitHub, adicione um workflow de CI para rodar testes" |

---

## Agente Plan Guardian

**Owns:** `PLAN.md`, `plan.json`, consistency checks

### Tarefas comuns

| Tarefa | Exemplo de prompt |
|------|----------------|
| Sincronizar arquivos do plano | "Como Plan Guardian, garanta que PLAN.md e plan.json estejam em sincronia" |
| Validar mudanças | "Como Plan Guardian, rode os checks de guardrails antes de eu fazer merge" |
| Atualizar progresso | "Como Plan Guardian, marque itens concluídos em PLAN.md" |

---

## Colaboração multiagente

For complex features, agents collaborate:

```markdown
Usuário: "Construa um sistema completo de autenticação de usuários"

1. Agente PM → escreve requisitos em `PRD.md`, cria itens de backlog
2. Agente UX → desenha fluxos de login/cadastro, documenta em `UI_SPEC.md`
3. Agente Eng → implementa autenticação com Supabase, segue specs de UX
4. Agente GitHub → cria issue de tracking, revisa PR
5. Plan Guardian → atualiza `PLAN.md`, valida documentação
```

---

## Dicas para uso eficaz

1. **Seja específico** — referencie itens de backlog (BL-XXX) e nomes de arquivos
2. **Comece pelo PM** — defina requisitos antes de implementar
3. **Atualize docs** — peça para os agentes atualizarem specs após mudanças
4. **Rode guardrails** — use `python3 scripts/check_markdown_links.py` antes de commits
5. **Registre decisões** — use `DECISIONS.md` para decisões leves e ADRs para arquitetura
