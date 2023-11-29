-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Mac and Cheese', 90, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chicken Chow Mein', 45, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Spaghetti Bolognese', 120, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Thai Green Curry', 45, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Egg Fried Rice', 30, 5);
