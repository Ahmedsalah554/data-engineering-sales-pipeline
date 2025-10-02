CREATE DATABASE sales_db;

\c sales_db;

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    product_name VARCHAR(100),
    quantity INT,
    unit_price NUMERIC(10,2),
    total_price NUMERIC(10,2),
    order_date DATE
);
