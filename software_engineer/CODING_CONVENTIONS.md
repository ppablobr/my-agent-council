# Convenções de código

Este documento descreve as convenções de código do projeto, alinhadas com a stack (Vite, React, Tailwind CSS, shadcn/ui, Supabase).

## Nomes de arquivos

| Tipo | Convenção | Exemplo |
| --- | --- | --- |
| Componentes React | PascalCase | `UserProfile.tsx` |
| Hooks | camelCase com prefixo `use` | `useAuth.ts` |
| Utilitários | camelCase | `formatDate.ts` |
| Types/Interfaces | PascalCase | `types.ts` → `User`, `ApiResponse` |
| Constantes | SCREAMING_SNAKE_CASE | `API_ENDPOINTS.ts` |
| Arquivos de teste | `*.test.ts` ou `*.spec.ts` | `UserProfile.test.tsx` |

## Estrutura de diretórios

```
app/
├── src/
│   ├── components/       # Reusable UI components
│   │   ├── ui/           # shadcn/ui primitives
│   │   └── [Feature]/    # Feature-specific components
│   ├── hooks/            # Custom React hooks
│   ├── lib/              # Utilities and helpers
│   ├── pages/            # Route pages
│   ├── types/            # TypeScript type definitions
│   └── styles/           # Global styles
```

## Convenções de TypeScript

- **Prefira `interface` em vez de `type`** para shapes de objetos (melhores mensagens de erro).
- **Tipos de retorno explícitos** em funções exportadas.
- **Evite `any`**; use `unknown` quando o tipo for realmente desconhecido.
- **Use `readonly`** para props e dados imutáveis.

```typescript
// ✅ Bom
interface UserProps {
  readonly id: string;
  readonly name: string;
}

export function formatUser(user: UserProps): string {
  return `${user.name} (${user.id})`;
}

// ❌ Evite
export const formatUser = (user: any) => user.name;
```

## Convenções de componentes React

- **Apenas componentes funcionais** (sem class components).
- **Interface de props** com nome `[ComponentName]Props`.
- **Desestruture props** na assinatura da função.
- **Exporte como named export** (default export apenas para páginas).

```tsx
interface UserCardProps {
  readonly user: User;
  readonly onSelect?: (id: string) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  return (
    <Card onClick={() => onSelect?.(user.id)}>
      <CardHeader>{user.name}</CardHeader>
    </Card>
  );
}
```

## Ordem de imports

Organize imports nesta ordem (com linhas em branco entre grupos):

1. Imports de React e framework
2. Bibliotecas de terceiros
3. Aliases internos (`@/`)
4. Imports relativos
5. Imports de tipos

```typescript
import { useState, useEffect } from 'react';

import { clsx } from 'clsx';

import { Button } from '@/components/ui/button';
import { useAuth } from '@/hooks/useAuth';

import { UserAvatar } from './UserAvatar';

import type { User } from '@/types';
```

## Estilização com Tailwind

- **Use classes do Tailwind** diretamente no JSX.
- **Use o helper `cn()`** para classes condicionais (do shadcn/ui).
- **Extraia padrões repetidos** para componentes, não para “utility classes”.

```tsx
import { cn } from '@/lib/utils';

<Button className={cn('w-full', isDisabled && 'opacity-50')} />
```

## Tratamento de erros

- **Use o padrão Result** para funções que podem falhar.
- **Use throw apenas para casos realmente excepcionais** (bugs, violações de invariantes).
- **Logue erros** com contexto antes de expor na UI.

```typescript
type Result<T, E = Error> = 
  | { ok: true; value: T }
  | { ok: false; error: E };

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await supabase.from('users').select().eq('id', id).single();
    return { ok: true, value: user.data };
  } catch (error) {
    console.error('[fetchUser]', { id, error });
    return { ok: false, error: error as Error };
  }
}
```

## Comentários e documentação

- **JSDoc para APIs públicas** (funções, hooks, componentes exportados).
- **Comentários inline** apenas para lógica não óbvia.
- **Formato de TODO:** `// TODO(owner): descrição [link-para-issue]`

```typescript
/**
 * Formata uma data para exibição na UI.
 * @param date - ISO date string or Date object
 * @param locale - locale BCP 47 (padrão: 'pt-BR')
 */
export function formatDate(date: string | Date, locale = 'pt-BR'): string {
  // ...
}
```
