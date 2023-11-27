# Student-Cohort Tables Design Recipe

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

student, name, cohort, cohort name, starting date
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| cohort                | cohort name, starting date
| student               | name

1. Name of the first table (always plural): `cohorts` 

    Column names: `cohort_name`, `starting_date`

2. Name of the second table (always plural): `students` 

    Column names: `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

```
# EXAMPLE:

Table: cohorts
id: SERIAL
cohort_name: text
starting_date: int

Table: students
id: SERIAL
name: name
```

## 4. Decide on The Tables Relationship

```
1. Can one [cohort] have many [students]? **YES**
2. Can one [student] have many [Tcohorts]? **NO**

-> Therefore,
-> A cohort HAS MANY students
-> A student BELONGS TO a cohort

-> Therefore, the foreign key is on the albums table.
```

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name: text,
  starting_date: int
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 student_directory < student_cohort_tables.sql
```

---
