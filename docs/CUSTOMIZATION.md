# Guia de personalização

Este guia explica como adaptar o Agent Council às necessidades do seu projeto.

## Personalizando a stack técnica

### 1. Atualize `software_engineer/TECH_STACK.md`

Substitua a stack padrão pelas suas escolhas:

```markdown
# Stack técnica

- **Frontend:** Next.js, TypeScript, Chakra UI
- **Backend:** Node.js, Express, PostgreSQL
- **Infrastructure:** AWS, Docker
```

### 2. Atualize specs relacionadas

Depois de mudar a stack, atualize:

| Arquivo | O que mudar |
|------|----------------|
| `CODING_CONVENTIONS.md` | Ajuste as convenções para sua linguagem/framework |
| `DATABASE_SCHEMA.md` | Atualize para o seu banco (PostgreSQL, MongoDB etc.) |
| `DESIGN_SYSTEM.md` | Alinhe com sua biblioteca de UI |

---

## Personalizando papéis dos agentes

### Adicionando um novo agente

1. **Crie o diretório do agente:**

```bash
mkdir qa_engineer
```

2. **Adicione um README.md com responsabilidades:**

```markdown
# Agente QA Engineer

O QA Engineer é responsável por estratégia de testes e garantia de qualidade.

**Responsabilidades:**
- Criação de plano de testes
- Documentação de casos de teste
- Triagem e verificação de bugs
```

3. **Atualize `AGENTS.md`** para incluir o novo agente na lista e no fluxo de interação.

4. **Atualize `product_manager/GOVERNANCE.md`** para adicionar entradas RACI para o novo agente.

### Modificando responsabilidades de agentes

Edite `AGENTS.md` para redistribuir responsabilidades. Por exemplo, para fazer o PM ficar responsável por documentação técnica:

```markdown
## Agente Product Manager (PM)

**Responsabilidades:**
- ...existing items...
- **Documentação técnica:** responsável por documentação de API e guias de integração
```

---

## Personalizando a governança

### Alterar a Definition of Done (DoD)

Edite `product_manager/PROJECT_RULES.md`:

```markdown
## Definition of Done (DoD)

Um item de trabalho está "concluído" quando:
- [ ] Code review aprovado por 2 revisores
- [ ] Testes de integração passando
- [ ] Documentação atualizada
- [ ] Deploy em staging
```

### Ajustar a matriz RACI

Edite `product_manager/GOVERNANCE.md` para mudar responsabilidades:

```markdown
| Area | PM | Eng | UX | DevOps |
| --- | --- | --- | --- | --- |
| Infrastructure | I | C | I | A/R |
| API Design | C | A/R | I | I |
```

---

## Personalizando guardrails

### Modificar checks de CI

Edite `.github/workflows/ci.yml` para adicionar ou remover checks:

```yaml
# Adicionar check de cobertura de testes
- name: Check coverage
  run: npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
```

### Adicionar guardrails customizados

Create a new script in `scripts/guardrails/`:

```python
#!/usr/bin/env python3
"""Verifica comentários TODO sem links de issue."""

import re
import sys
from pathlib import Path

def check_todos():
    issues = []
    for file in Path('app').rglob('*.ts'):
        content = file.read_text()
        for i, line in enumerate(content.splitlines(), 1):
            if 'TODO' in line and not re.search(r'TODO\(.+\):', line):
                issues.append(f"{file}:{i}: TODO sem responsável")
    
    if issues:
        print("\\n".join(issues))
        sys.exit(1)
    print("OK: todos os TODOs têm responsável")

if __name__ == "__main__":
    check_todos()
```

Adicione ao workflow do CI:

```yaml
- name: TODO format check
  run: python3 scripts/guardrails/check_todos.py
```

---

## Personalizando templates

### Templates de issues

Edit files in `.github/ISSUE_TEMPLATE/`:

- `bug_report.yml` — Bug report format
- `feature_request.yml` — Feature request format

### Template de PR

Edit `.github/pull_request_template.md` to match your process.

### Template de ADR

Edit `docs/adr/0000-template.md` to add sections relevant to your project.

---

## Personalizando servidores MCP

Servidores MCP (Model Context Protocol) habilitam integrações de IA com serviços externos. Configure em `mcp.json`.

### Setup inicial

Copie o arquivo de exemplo e adicione suas credenciais:

```bash
cp mcp.json.example mcp.json
```

### Adicionando servidores MCP adicionais

You can add multiple MCP servers to `mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token"
      }
    },
    "supabase": {
      "command": "npx",
      "args": ["-y", "supabase-mcp-server"],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "your_supabase_token"
      }
    }
  }
}
```

### Servidores MCP disponíveis

| Servidor | Finalidade |
|--------|---------|
| `@modelcontextprotocol/server-github` | Operações no GitHub (issues, PRs, repositórios) |
| `supabase-mcp-server` | Banco Supabase e Edge Functions |
| `@modelcontextprotocol/server-filesystem` | Operações em arquivos locais |

> [!WARNING]
> Nunca faça commit de `mcp.json` no controle de versão. Garanta que esteja listado em `.gitignore`.

---

## Adaptações específicas por tipo de projeto

### Para apps mobile

- Add `ios/` and `android/` to structure
- Create `mobile_engineer/` agent folder
- Update DESIGN_SYSTEM.md for mobile patterns

### Para microserviços

- Create separate folders per service
- Add `devops/` or `platform_engineer/` agent
- Update DATABASE_SCHEMA.md for multi-database patterns

### Para times

- Add team-specific RACI entries
- Create on-call or rotation documentation
- Add deployment runbooks to `docs/`
