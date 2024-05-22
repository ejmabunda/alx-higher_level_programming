-- Creates the database hbtn_0d_usa and the table
-- states.

-- Create database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create table in new database.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);