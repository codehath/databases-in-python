-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq CASCADE;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    post_id INT,
    "user" TEXT,
    CONSTRAINT fk_post FOREIGN KEY(post_id)
        REFERENCES posts(id)
        ON DELETE CASCADE
);

-- Insert data into the posts table
INSERT INTO posts (title, content) VALUES
    ('First Post', 'This is the content of the first post.'),
    ('Programming Tips', 'Here are some tips for programming.'),
    ('Travel Adventures', 'Exploring new places and cultures.');

-- Insert data into the comments table
INSERT INTO comments (content, post_id, "user") VALUES
    ('Great post!', 1, 'Emily Johnson'),
    ('I found the programming tips helpful.', 2, 'Daniel Brown'),
    ('Nice insights!', 1, 'Sophia Miller'),
    ('The programming tips are so helpful, thanks!', 2, 'Elijah Davis'),
    ('What an exciting travel experience!', 3, 'Olivia Wilson'),
    ('Looking forward to reading more from you.', 1, 'Liam Garcia'),
    ('I completely agree with your thoughts.', 2, 'Ava Martinez'),
    ('Can you share more details about your travel?', 3, 'Noah Smith'),
    ('This is a valuable post for beginners.', 2, 'Isabella Anderson'),
    ('Looking forward to more travel stories.', 3, 'Mason Taylor');