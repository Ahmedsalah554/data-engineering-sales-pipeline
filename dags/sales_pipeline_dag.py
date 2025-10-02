from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def get_connection_config():
    
    try:
        
        conn = psycopg2.connect(
            host="postgres-db",
            port="5432",
            database="sales_db",
            user="postgres",
            password="1234",
            connect_timeout=3
        )
        conn.close()
        return {
            "host": "postgres-db",
            "port": "5432",
            "database": "sales_db",
            "user": "postgres",
            "password": "1234"
        }
    except Exception:
        # fallback → host.docker.internal
        return {
            "host": "host.docker.internal",
            "port": "5432",
            "database": "sales_db",
            "user": "postgres",
            "password": "1234"
        }

def extract(**kwargs):
    DB_CONFIG = get_connection_config()
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT * FROM sales_data;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict()

def transform(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='extract_task')
    df = pd.DataFrame.from_dict(data)
    summary = df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()
    return summary.to_dict()

def load(**kwargs):
    ti = kwargs['ti']
    summary = ti.xcom_pull(task_ids='transform_task')
    df = pd.DataFrame.from_dict(summary)

    DB_CONFIG = get_connection_config()
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales_summary (
            productline VARCHAR(100),
            total_sales NUMERIC
        )
    """)
    conn.commit()

    cur.execute("TRUNCATE TABLE sales_summary")

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO sales_summary (productline, total_sales) VALUES (%s, %s)",
            (row['PRODUCTLINE'], row['SALES'])
        )
    conn.commit()
    conn.close()

with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,  
    catchup=False,
    tags=["etl", "sales"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load
    )

    extract_task >> transform_task >> load_task