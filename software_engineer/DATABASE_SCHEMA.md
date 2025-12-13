# Database Schema

This document outlines the database schema conventions and patterns for the project, using Supabase (PostgreSQL).

## Naming Conventions

| Element | Convention | Example |
| --- | --- | --- |
| Tables | snake_case, plural | `user_profiles`, `chat_messages` |
| Columns | snake_case | `created_at`, `user_id` |
| Primary keys | `id` (UUID) | `id uuid primary key default gen_random_uuid()` |
| Foreign keys | `[table_singular]_id` | `user_id`, `project_id` |
| Timestamps | `created_at`, `updated_at` | Standard on all tables |
| Boolean columns | `is_` or `has_` prefix | `is_active`, `has_verified_email` |

## Standard Columns

Every table should include:

```sql
id uuid primary key default gen_random_uuid(),
created_at timestamptz default now() not null,
updated_at timestamptz default now() not null
```

## Migration Guidelines

- **One migration per logical change** (don't bundle unrelated changes).
- **Migration naming:** `YYYYMMDDHHMMSS_short_description.sql`
- **Always include rollback** in comments or separate down migration.
- **Test migrations** on a branch before applying to production.

### Migration Template

```sql
-- Migration: create_user_profiles
-- Description: Creates the user_profiles table for storing user data
-- Rollback: DROP TABLE IF EXISTS user_profiles;

create table user_profiles (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete cascade not null,
  display_name text,
  avatar_url text,
  created_at timestamptz default now() not null,
  updated_at timestamptz default now() not null
);

-- Enable RLS
alter table user_profiles enable row level security;

-- Index for common queries
create index idx_user_profiles_user_id on user_profiles(user_id);
```

## Row Level Security (RLS) Patterns

### User-Owned Data

```sql
-- Users can only read/write their own data
create policy "Users can view own profile"
  on user_profiles for select
  using (auth.uid() = user_id);

create policy "Users can update own profile"
  on user_profiles for update
  using (auth.uid() = user_id);
```

### Public Read, Authenticated Write

```sql
-- Anyone can read, only authenticated users can write
create policy "Public read access"
  on posts for select
  to anon, authenticated
  using (is_published = true);

create policy "Authenticated users can create"
  on posts for insert
  to authenticated
  with check (auth.uid() = author_id);
```

## Common Schema Patterns

### Soft Delete

```sql
deleted_at timestamptz default null

-- Query only active records
create policy "Hide deleted records"
  on items for select
  using (deleted_at is null);
```

### Audit Trail

```sql
created_by uuid references auth.users(id),
updated_by uuid references auth.users(id)
```

### Enum-like Columns

Use PostgreSQL enums or check constraints:

```sql
-- Option 1: Enum type
create type status_type as enum ('draft', 'published', 'archived');
status status_type default 'draft' not null

-- Option 2: Check constraint
status text not null check (status in ('draft', 'published', 'archived'))
```

## Indexes

Create indexes for:
- Foreign key columns
- Columns used in WHERE clauses
- Columns used in ORDER BY

```sql
create index idx_posts_author_id on posts(author_id);
create index idx_posts_created_at on posts(created_at desc);
```

## Edge Functions Integration

When calling Edge Functions that interact with the database:
- Use the service role key only in trusted server contexts
- Prefer RLS policies over manual auth checks
- Return minimal data to reduce payload size

---

## Current Schema

> **Note:** This section should be updated as the schema evolves. Add tables as they are created.

_No tables defined yet._
