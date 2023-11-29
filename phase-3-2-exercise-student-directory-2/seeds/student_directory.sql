
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq CASCADE;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;


-- Create the table without the foreign key first.
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    name text,
    starting_date DATE
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


-- Insert data into the cohorts table
INSERT INTO cohorts (name, starting_date) VALUES
('Cohort A', '2022-01-01'),
('Cohort B', '2022-02-01'),
('Cohort C', '2022-03-01');

-- Insert data into the students table
INSERT INTO students (name, cohort_id) VALUES
('John Doe', 1),
('Jane Smith', 2),
('Bob Johnson', 1),
('Alice Williams', 3),
('Eva Rodriguez', 2),
('Michael Brown', 1),
('Sophia Lee', 3),
('Daniel Miller', 1),
('Olivia Davis', 2),
('William Wilson', 3),
('Emma Martinez', 1),
('Alexander Taylor', 2),
('Ava Moore', 3),
('James Anderson', 1);