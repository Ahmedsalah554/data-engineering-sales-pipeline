# 🚀 Data Engineering ETL Pipeline with Airflow & PostgreSQL

This project demonstrates a complete **ETL Data Pipeline** using:
- **Python** 🐍
- **PostgreSQL** 🐘
- **Apache Airflow** 🌬️
- **Docker** 🐳

---

## 📌 Project Overview
The pipeline processes sales data:
1. **Extract**: Load data from a CSV file.  
2. **Transform**: Clean data and calculate `total_price = quantity * unit_price`.  
3. **Load**: Store the transformed data in PostgreSQL.  
4. **Orchestration**: Manage and schedule the pipeline using Airflow.  

---

## 📂 Project Structure
```text
data-engineering-sales-pipeline/
├── dags/
│   └── sales_pipeline_dag.py      # Airflow DAG
├── scripts/
│   ├── extract.py                 # Extract step
│   ├── transform.py               # Transform step
│   └── load.py                    # Load step
├── data/
│   └── sales_data_sample.csv      # Sample sales data
├── sql/
│   └── create_tables.sql          # PostgreSQL schema
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation Python dependencies
└── README.md                      # Project documentation

⚡ Tech Stack

Python: Data processing with Pandas.

PostgreSQL: Relational database.

Airflow: Workflow orchestration.

SQLAlchemy: Database connection layer.

Docker: Containerized environment.

🎯 Goals

Hands-on practice with Data Engineering tools.

Build a real-world ETL pipeline.

Gain experience with Airflow and PostgreSQL.

Showcase as a portfolio project.

📌 Future Improvements

✅ Add Data Quality Checks.

✅ Support multiple data sources (CSV + API).

✅ Add visualization dashboards.

✅ Fully containerize the pipeline.

👨‍💻 Author

Ahmed Salah
Data Engineering Enthusiast 🚀
GitHub Profile
