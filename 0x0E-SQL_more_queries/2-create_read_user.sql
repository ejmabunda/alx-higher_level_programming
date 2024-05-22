-- Creates a database and user

-- Create database if none exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Add user with SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';