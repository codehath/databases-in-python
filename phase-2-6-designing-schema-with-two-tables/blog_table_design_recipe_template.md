# Two Tables Design Recipe

## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
```

```
Nouns:

post, title, content, comment, comments content, comment author name, author
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| post                  | title, content
| comment               | content
| author                | author name 

1. Name of the first table: `posts` 

    Column names: `title`, `content`

2. Name of the second table: `comments` 

    Column names: `content`, `author_name`

3. Name of the third table: `users` 

    Column names: `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

```
Table: posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
content: text

Table: users
id: SERIAL
name: text
```

## 4. Decide on The Tables Relationship

```
1. Can one [post] have many [comments]? **YES**
2. Can one [comment] have many [posts]? **NO**
3. Can one [user] have many [comments]? **YES**
4. Can one [comment] have many [users]? **NO**

Therefore,
-> A post HAS MANY comments
-> A comment BELONGS TO a post
-> A user HAS MANY comments
-> A comment BELONGS TO  a user

-> Therefore, there are two foreign keys on the comments table.
```

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title: text,
  content: text,
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name: text
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  content text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade,
  constraint fk_author foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 blog < blog_tables.sql
```

---
