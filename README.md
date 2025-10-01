
# Data Engineering Sales Pipeline

This project is a full ETL pipeline for processing sales data using **Airflow** and **PostgreSQL**.

## Features
- Extract sales data from CSV files
- Transform: calculate total sales per product line
- Load: store summary into PostgreSQL table
- Airflow DAG for scheduling and monitoring
- Dockerized setup for easy deployment

## Requirements
- Docker & Docker Compose
- Python 3.13+
- Airflow 2.x
- PostgreSQL 13

## Usage
1. Start services:
```bash
docker-compose up -d
