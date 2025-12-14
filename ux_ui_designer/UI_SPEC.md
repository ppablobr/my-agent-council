# Especificação de UI

Este documento define como documentar especificações de interface do usuário para o projeto.

## Formato de documentação de páginas

Cada página/tela deve ser documentada com a seguinte estrutura:

```markdown
## [Nome da página]

### Purpose
Breve descrição do que esta página faz e seu papel no fluxo do usuário.

### Route
`/path/to/page`

### Layout
- Cabeçalho: [descrição]
- Conteúdo principal: [descrição]
- Barra lateral (se houver): [descrição]

### Components Used
- ComponentA
- ComponentB

### States
- Carregando: [descrição]
- Vazio: [descrição]
- Erro: [descrição]
- Sucesso: [descrição]

### Actions
| Ação | Disparo | Resultado |
| --- | --- | --- |
| Enviar formulário | Clique no botão | Chamada de API, redirect |

### Responsive Behavior
- Mobile: [mudanças]
- Tablet: [mudanças]
- Desktop: [padrão]
```

## Documentação de estados de componentes

Documente todos os estados possíveis de componentes interativos:

| Estado | Visual | Comportamento |
| --- | --- | --- |
| Padrão | Aparência normal | Aguardando interação |
| Hover | Mudança sutil de cor | Cursor pointer |
| Ativo/Pressionado | Tom mais escuro | Feedback visual |
| Foco | Focus ring visível | Acessível via teclado |
| Desabilitado | Cores neutras, 50% opacidade | Sem interação |
| Carregando | Spinner ou skeleton | Evita reenvio |
| Erro | Borda/texto vermelho | Mostra mensagem de erro |

## Breakpoints responsivos

Desenhe com abordagem mobile-first. Documente mudanças por breakpoint:

| Breakpoint | Largura | Mudanças no layout |
| --- | --- | --- |
| Mobile | < 640px | Coluna única, elementos empilhados |
| Tablet | 640px - 1023px | Duas colunas, navegação colapsada |
| Desktop | ≥ 1024px | Layout completo, sidebar visível |

## Checklist de acessibilidade

Para cada página/componente, verifique:

- [ ] Todas as imagens têm texto alternativo (alt)
- [ ] Inputs de formulário têm labels
- [ ] Cor não é o único indicador
- [ ] Navegação por teclado funciona
- [ ] Ordem de foco é lógica
- [ ] Leitor de tela anuncia corretamente

## Convenções de wireframe

Ao criar wireframes:

- Use escala de cinza para focar no layout
- Anote elementos interativos
- Mostre todos os estados (principalmente vazio/erro)
- Inclua versões responsivas

---

## Pages

> **Nota:** documente cada página abaixo conforme for desenhada.

_No pages documented yet._
