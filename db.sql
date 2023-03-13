CREATE DATABASE pharmacymanagement;

USE pharmacymanagement;

CREATE TABLE details (
    Id INT,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    problem VARCHAR(255),
    tabletname VARCHAR(255),
    tabletcount INT,
    cost FLOAT,
    discount FLOAT,
    total VARCHAR(255),
    save VARCHAR(255)
);
