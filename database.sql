-- Create Database
CREATE DATABASE users;

-- Use Database
USE users;

-- Create Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
);

-- Insert Sample Data
INSERT INTO users (name, email, role) VALUES
('John Doe', 'john.doe@example.com', 'Admin'),
('Jane Smith', 'jane.smith@example.com', 'User');

-- Retrieve All Users
SELECT * FROM users;

-- Retrieve User by ID
SELECT * FROM users WHERE id = 1;