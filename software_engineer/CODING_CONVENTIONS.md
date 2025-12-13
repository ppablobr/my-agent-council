# Coding Conventions

This document outlines the coding conventions for the project, aligned with the tech stack (Vite, React, Tailwind CSS, shadcn/ui, Supabase).

## File Naming

| Type | Convention | Example |
| --- | --- | --- |
| React components | PascalCase | `UserProfile.tsx` |
| Hooks | camelCase with `use` prefix | `useAuth.ts` |
| Utilities | camelCase | `formatDate.ts` |
| Types/Interfaces | PascalCase | `types.ts` → `User`, `ApiResponse` |
| Constants | SCREAMING_SNAKE_CASE | `API_ENDPOINTS.ts` |
| Test files | `*.test.ts` or `*.spec.ts` | `UserProfile.test.tsx` |

## Directory Structure

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

## TypeScript Conventions

- **Prefer `interface` over `type`** for object shapes (better error messages).
- **Explicit return types** on exported functions.
- **Avoid `any`**; use `unknown` when type is truly unknown.
- **Use `readonly`** for props and immutable data.

```typescript
// ✅ Good
interface UserProps {
  readonly id: string;
  readonly name: string;
}

export function formatUser(user: UserProps): string {
  return `${user.name} (${user.id})`;
}

// ❌ Avoid
export const formatUser = (user: any) => user.name;
```

## React Component Conventions

- **Functional components only** (no class components).
- **Props interface** named `[ComponentName]Props`.
- **Destructure props** in function signature.
- **Export as named export** (default export only for pages).

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

## Import Order

Organize imports in this order (with blank lines between groups):

1. React and framework imports
2. Third-party libraries
3. Internal aliases (`@/`)
4. Relative imports
5. Type imports

```typescript
import { useState, useEffect } from 'react';

import { clsx } from 'clsx';

import { Button } from '@/components/ui/button';
import { useAuth } from '@/hooks/useAuth';

import { UserAvatar } from './UserAvatar';

import type { User } from '@/types';
```

## Styling with Tailwind

- **Use Tailwind classes** directly in JSX.
- **Use `cn()` helper** for conditional classes (from shadcn/ui).
- **Extract repeated patterns** into components, not utility classes.

```tsx
import { cn } from '@/lib/utils';

<Button className={cn('w-full', isDisabled && 'opacity-50')} />
```

## Error Handling

- **Use Result pattern** for functions that can fail.
- **Throw only for truly exceptional cases** (bugs, invariant violations).
- **Log errors** with context before surfacing to UI.

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

## Comments and Documentation

- **JSDoc for public APIs** (exported functions, hooks, components).
- **Inline comments** only for non-obvious logic.
- **TODO format:** `// TODO(owner): description [link-to-issue]`

```typescript
/**
 * Formats a date for display in the UI.
 * @param date - ISO date string or Date object
 * @param locale - BCP 47 locale string (default: 'en-US')
 */
export function formatDate(date: string | Date, locale = 'en-US'): string {
  // ...
}
```
