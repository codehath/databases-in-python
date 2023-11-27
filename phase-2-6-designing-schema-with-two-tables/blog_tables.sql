-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq CASCADE;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;


-- Create the table without the foreign key first.
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    cohort_name text,
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


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    post_id INT,
    user_id INT,
    CONSTRAINT fk_post FOREIGN KEY(post_id)
        REFERENCES posts(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_author FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);



-- Insert data into the users table
INSERT INTO users (name) VALUES
    ('John Doe'),
    ('Jane Smith'),
    ('Alice Johnson');

-- Insert data into the posts table
INSERT INTO posts (title, content) VALUES
    ('First Post', 'This is the content of the first post.'),
    ('Programming Tips', 'Here are some tips for programming.'),
    ('Travel Adventures', 'Exploring new places and cultures.');

-- Insert data into the comments table
INSERT INTO comments (content, post_id, user_id) VALUES
    ('Great post!', 1, 2),
    ('I found the programming tips helpful.', 2, 1),
    ('Nice insights!', 1, 3),
    ('The programming tips are so helpful, thanks!', 2, 2),
    ('What an exciting travel experience!', 3, 1),
    ('Looking forward to reading more from you.', 1, 1),
    ('I completely agree with your thoughts.', 2, 3),
    ('Can you share more details about your travel?', 3, 2),
    ('This is a valuable post for beginners.', 2, 3),
    ('Looking forward to more travel stories.', 3, 3);