# Design system

Este documento define tokens de design e padrões de componentes do projeto, construído com Tailwind CSS e shadcn/ui.

## Paleta de cores

Baseada nos padrões do Tailwind CSS com nomes semânticos. Personalize em `tailwind.config.js`.

### Cores base

| Token | Uso | Classe Tailwind |
| --- | --- | --- |
| `background` | Page backgrounds | `bg-background` |
| `foreground` | Primary text | `text-foreground` |
| `muted` | Secondary text, disabled states | `text-muted-foreground` |
| `card` | Card backgrounds | `bg-card` |
| `border` | Borders, dividers | `border-border` |

### Cores semânticas

| Token | Uso | Classe Tailwind |
| --- | --- | --- |
| `primary` | Primary actions, links | `bg-primary`, `text-primary` |
| `secondary` | Secondary actions | `bg-secondary` |
| `destructive` | Delete, error states | `bg-destructive` |
| `accent` | Highlights, hover states | `bg-accent` |

### Dark Mode

Use o prefixo `dark:` para estilos de modo escuro. O sistema usa a estratégia `class` para alternância.

```tsx
<div className="bg-white dark:bg-slate-900">
```

## Tipografia

Usando a escala tipográfica padrão do Tailwind com Inter (ou fontes do sistema).

| Elemento | Classe | Tamanho |
| --- | --- | --- |
| H1 | `text-4xl font-bold` | 36px |
| H2 | `text-3xl font-semibold` | 30px |
| H3 | `text-2xl font-semibold` | 24px |
| H4 | `text-xl font-medium` | 20px |
| Body | `text-base` | 16px |
| Small | `text-sm` | 14px |
| Caption | `text-xs text-muted-foreground` | 12px |

## Espaçamento

Use a escala de espaçamento do Tailwind de forma consistente:

| Token | Valor | Uso |
| --- | --- | --- |
| `1` | 4px | Tight spacing (icon gaps) |
| `2` | 8px | Small spacing |
| `4` | 16px | Default padding |
| `6` | 24px | Section padding |
| `8` | 32px | Large gaps |

## Raio de borda

| Token | Classe | Valor |
| --- | --- | --- |
| Small | `rounded-sm` | 2px |
| Default | `rounded-md` | 6px |
| Large | `rounded-lg` | 8px |
| Full | `rounded-full` | 9999px |

## Sombras

| Token | Classe | Uso |
| --- | --- | --- |
| Small | `shadow-sm` | Subtle elevation |
| Default | `shadow` | Cards, dropdowns |
| Large | `shadow-lg` | Modals, popovers |

## Animação

### Transições

Transição padrão: `transition-all duration-200 ease-in-out`

### Animações comuns

```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide up */
@keyframes slideUp {
  from { transform: translateY(10px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
```

## Padrões de componentes

### shadcn/ui Components

Use shadcn/ui como biblioteca base. Componentes são instalados em `src/components/ui/`.

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add input
```

### Variantes de componente

Use o padrão `variants` do shadcn/ui para variações de componentes:

```tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground",
        outline: "border border-input bg-background hover:bg-accent",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 px-3",
        lg: "h-11 px-8",
      },
    },
  }
);
```

## Breakpoints responsivos

| Breakpoint | Largura mínima | Uso |
| --- | --- | --- |
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablets |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Large desktop |

## Acessibilidade

- Contraste mínimo: 4.5:1 para texto normal
- Estados de foco: focus ring visível (`ring-2 ring-ring ring-offset-2`)
- Elementos interativos: alvo de toque mínimo 44x44px
- Movimento: respeitar `prefers-reduced-motion`
