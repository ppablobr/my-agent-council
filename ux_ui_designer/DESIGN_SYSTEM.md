# Design System

This document defines the design tokens and component patterns for the project, built on Tailwind CSS and shadcn/ui.

## Color Palette

Based on Tailwind CSS defaults with semantic naming. Customize in `tailwind.config.js`.

### Base Colors

| Token | Usage | Tailwind Class |
| --- | --- | --- |
| `background` | Page backgrounds | `bg-background` |
| `foreground` | Primary text | `text-foreground` |
| `muted` | Secondary text, disabled states | `text-muted-foreground` |
| `card` | Card backgrounds | `bg-card` |
| `border` | Borders, dividers | `border-border` |

### Semantic Colors

| Token | Usage | Tailwind Class |
| --- | --- | --- |
| `primary` | Primary actions, links | `bg-primary`, `text-primary` |
| `secondary` | Secondary actions | `bg-secondary` |
| `destructive` | Delete, error states | `bg-destructive` |
| `accent` | Highlights, hover states | `bg-accent` |

### Dark Mode

Use the `dark:` variant prefix for dark mode styles. The system uses `class` strategy for dark mode toggling.

```tsx
<div className="bg-white dark:bg-slate-900">
```

## Typography

Using the default Tailwind typography scale with Inter (or system fonts).

| Element | Class | Size |
| --- | --- | --- |
| H1 | `text-4xl font-bold` | 36px |
| H2 | `text-3xl font-semibold` | 30px |
| H3 | `text-2xl font-semibold` | 24px |
| H4 | `text-xl font-medium` | 20px |
| Body | `text-base` | 16px |
| Small | `text-sm` | 14px |
| Caption | `text-xs text-muted-foreground` | 12px |

## Spacing

Use Tailwind's spacing scale consistently:

| Token | Value | Usage |
| --- | --- | --- |
| `1` | 4px | Tight spacing (icon gaps) |
| `2` | 8px | Small spacing |
| `4` | 16px | Default padding |
| `6` | 24px | Section padding |
| `8` | 32px | Large gaps |

## Border Radius

| Token | Class | Value |
| --- | --- | --- |
| Small | `rounded-sm` | 2px |
| Default | `rounded-md` | 6px |
| Large | `rounded-lg` | 8px |
| Full | `rounded-full` | 9999px |

## Shadows

| Token | Class | Usage |
| --- | --- | --- |
| Small | `shadow-sm` | Subtle elevation |
| Default | `shadow` | Cards, dropdowns |
| Large | `shadow-lg` | Modals, popovers |

## Animation

### Transitions

Default transition: `transition-all duration-200 ease-in-out`

### Common Animations

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

## Component Patterns

### shadcn/ui Components

Use shadcn/ui as the base component library. Components are installed to `src/components/ui/`.

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add input
```

### Component Variants

Use the `variants` pattern from shadcn/ui for component variations:

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

## Responsive Breakpoints

| Breakpoint | Min Width | Usage |
| --- | --- | --- |
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablets |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Large desktop |

## Accessibility

- Minimum contrast ratio: 4.5:1 for normal text
- Focus states: visible focus ring (`ring-2 ring-ring ring-offset-2`)
- Interactive elements: minimum 44x44px touch target
- Motion: respect `prefers-reduced-motion`
