-- USER STORIES:
-- As a social network user,
-- So I can have my information registered,
-- I'd like to have a user account with my email address.

-- As a social network user,
-- So I can have my information registered,
-- I'd like to have a user account with my username.

-- As a social network user,
-- So I can write on my timeline,
-- I'd like to create posts associated with my user account.

-- As a social network user,
-- So I can write on my timeline,
-- I'd like each of my posts to have a title and a content.

-- As a social network user,
-- So I can know who reads my posts,
-- I'd like each of my posts to have a number of views.

-- KEYWORDS:
-- user account, email address, username, posts, title, content, views


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq CASCADE;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Users table to store user information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    username VARCHAR(50) UNIQUE
);

-- Posts table to store user posts
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    content TEXT,
    views INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert data into the users table
INSERT INTO users (email, username) VALUES
('john.doe@example.com', 'johndoe'),
('jane.smith@example.com', 'janesmith'),
('bob.johnson@example.com', 'bobjohnson');

-- Insert data into the posts table
INSERT INTO posts (user_id, title, content, views) VALUES
(1, 'First Post', 'This is the content of the first post.', 15),
(2, 'Hello World', 'Just saying hello to the world!', 8),
(1, 'Travel Adventures', 'Exploring new places and making memories.', 22),
(3, 'Tech News', 'Latest updates in the tech world.', 10),
(2, 'Favorite Users', 'A list of my favorite users and why I love them.', 18);