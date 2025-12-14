# Esquema do banco de dados

Este documento descreve convenções e padrões de schema do banco de dados do projeto, usando Supabase (PostgreSQL).

## Convenções de nomenclatura

| Elemento | Convenção | Exemplo |
| --- | --- | --- |
| Tabelas | snake_case, plural | `user_profiles`, `chat_messages` |
| Colunas | snake_case | `created_at`, `user_id` |
| Chaves primárias | `id` (UUID) | `id uuid primary key default gen_random_uuid()` |
| Chaves estrangeiras | `[tabela_singular]_id` | `user_id`, `project_id` |
| Timestamps | `created_at`, `updated_at` | Padrão em todas as tabelas |
| Colunas booleanas | prefixo `is_` ou `has_` | `is_active`, `has_verified_email` |

## Colunas padrão

Toda tabela deve incluir:

```sql
id uuid primary key default gen_random_uuid(),
created_at timestamptz default now() not null,
updated_at timestamptz default now() not null
```

## Diretrizes de migração

- **Uma migração por mudança lógica** (não agrupe mudanças não relacionadas).
- **Nome da migração:** `YYYYMMDDHHMMSS_short_description.sql`
- **Sempre inclua rollback** em comentários ou uma migração “down” separada.
- **Teste migrações** em uma branch antes de aplicar em produção.

### Template de migração

```sql
-- Migration: create_user_profiles
-- Description: Cria a tabela user_profiles para armazenar dados de usuário
-- Rollback: DROP TABLE IF EXISTS user_profiles;

create table user_profiles (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete cascade not null,
  display_name text,
  avatar_url text,
  created_at timestamptz default now() not null,
  updated_at timestamptz default now() not null
);

-- Habilitar RLS
alter table user_profiles enable row level security;

-- Índice para queries comuns
create index idx_user_profiles_user_id on user_profiles(user_id);
```

## Padrões de Row Level Security (RLS)

### Dados “possuídos” pelo usuário

```sql
-- Usuários só podem ler/escrever seus próprios dados
create policy "Users can view own profile"
  on user_profiles for select
  using (auth.uid() = user_id);

create policy "Users can update own profile"
  on user_profiles for update
  using (auth.uid() = user_id);
```

### Leitura pública, escrita autenticada

```sql
-- Qualquer pessoa pode ler; apenas usuários autenticados podem escrever
create policy "Public read access"
  on posts for select
  to anon, authenticated
  using (is_published = true);

create policy "Authenticated users can create"
  on posts for insert
  to authenticated
  with check (auth.uid() = author_id);
```

## Padrões comuns de schema

### Soft delete

```sql
deleted_at timestamptz default null

-- Consultar apenas registros ativos
create policy "Hide deleted records"
  on items for select
  using (deleted_at is null);
```

### Trilha de auditoria

```sql
created_by uuid references auth.users(id),
updated_by uuid references auth.users(id)
```

### Colunas “tipo enum”

Use enums do PostgreSQL ou check constraints:

```sql
-- Opção 1: tipo enum
create type status_type as enum ('draft', 'published', 'archived');
status status_type default 'draft' not null

-- Opção 2: check constraint
status text not null check (status in ('draft', 'published', 'archived'))
```

## Índices

Crie índices para:
- Colunas de chave estrangeira
- Colunas usadas em cláusulas WHERE
- Colunas usadas em ORDER BY

```sql
create index idx_posts_author_id on posts(author_id);
create index idx_posts_created_at on posts(created_at desc);
```

## Integração com Edge Functions

Ao chamar Edge Functions que interagem com o banco:
- Use a service role key apenas em contextos confiáveis no servidor
- Prefira políticas de RLS em vez de checks manuais de autenticação
- Retorne o mínimo de dados para reduzir payload

---

## Current Schema

> **Nota:** esta seção deve ser atualizada conforme o schema evoluir. Adicione tabelas quando forem criadas.

_No tables defined yet._
