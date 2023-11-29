-- User Stories
-- As a shop manager
-- So I can know which items I have in stock
-- I want to keep a list of my shop items with their name and unit price.

-- As a shop manager
-- So I can know which items I have in stock
-- I want to know which quantity (a number) I have for each item.

-- As a shop manager
-- So I can manage items
-- I want to be able to create a new item.

-- As a shop manager
-- So I can know which orders were made
-- I want to keep a list of orders with their customer name.

-- As a shop manager
-- So I can know which orders were made
-- I want to assign each order to their corresponding item.

-- As a shop manager
-- So I can know which orders were made
-- I want to know on which date an order was placed. 

-- As a shop manager
-- So I can manage orders
-- I want to be able to create a new order.

--Key Words:
-- shop items, name, unit price, quantity, 
-- orders, customer name, date

-- Functions
-- Create new item, create new order, Update quantity after order,  



DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq CASCADE;
DROP TABLE IF EXISTS orders_items ;


-- Create a sequence for items
CREATE SEQUENCE items_id_seq;

-- Create the items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INTEGER
);

-- Create a sequence for orders
CREATE SEQUENCE orders_id_seq;

-- Create the orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    order_date DATE
);

-- Create the orders_items table to associate items with orders
CREATE TABLE orders_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    item_id INTEGER REFERENCES items(id) ON DELETE CASCADE,
    quantity INTEGER
);

-- Insert data into the items table
INSERT INTO items (name, price, quantity) VALUES
    ('Super Shark Vacuum Cleaner', 99 , 30),
    ('Makerspresso Coffee Machine', 69, 15),
    ('Ultra-Slim Laptop', 899.99, 10),
    ('Smart LED TV', 549.95, 20),
    ('Wireless Bluetooth Earbuds', 39.99, 50),
    ('Foldable Electric Scooter', 299.50, 5),
    ('Stainless Steel Water Bottle', 12.99, 100),
    ('Fitness Tracker Watch', 79.99, 30),
    ('Portable External Hard Drive', 129.95, 15),
    ('Cordless Electric Drill', 59.99, 25);

-- Insert data into the orders table
INSERT INTO orders (customer_name, order_date) VALUES
    ('John Doe', '2023-11-28'),
    ('Jane Smith', '2023-11-29'),
    ('Alice Johnson', '2023-11-30');

-- Insert data into the orders_items table
INSERT INTO orders_items (order_id, item_id, quantity) VALUES
    (1, 1, 2),
    (1, 3, 1),
    (2, 2, 3),
    (2, 5, 2),
    (3, 4, 1),
    (3, 6, 2),
    (3, 8, 4);