# dags/sales_pipeline_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
import os
import pandas as pd

# إضافة الـ scripts للف PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from extract import extract_data
from transform import transform_data
from load import load_data

# 🗓️ إعدادات عامة للـ DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# تعريف الـ DAG
with DAG(
    dag_id="sales_pipeline_dag",
    default_args=default_args,
    description="ETL pipeline for sales data with PostgreSQL",
    schedule_interval="@daily",  # كل يوم
    start_date=datetime(2025, 9, 30),
    catchup=False,
    tags=["etl", "sales", "postgres"],
) as dag:

    # 🟢 Task 1: Extract
    def extract_task(**kwargs):
        df = extract_data("data/sales_data.csv")
        kwargs["ti"].xcom_push(key="raw_data", value=df.to_json())

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_task,
        provide_context=True,
    )

    # 🟡 Task 2: Transform
    def transform_task(**kwargs):
        import json
        raw_json = kwargs["ti"].xcom_pull(task_ids="extract_data", key="raw_data")
        df_raw = pd.read_json(raw_json)
        df_transformed = transform_data(df_raw)
        kwargs["ti"].xcom_push(key="transformed_data", value=df_transformed.to_json())

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_task,
        provide_context=True,
    )

    # 🔵 Task 3: Load
    def load_task(**kwargs):
        import json
        transformed_json = kwargs["ti"].xcom_pull(task_ids="transform_data", key="transformed_data")
        df_transformed = pd.read_json(transformed_json)

        load_data(
            df_transformed,
            user="postgres",
            password="1234",   # ✏️ غير الباسورد حسب إعدادك
            host="localhost",
            port=5432,
            db="sales_db",
        )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_task,
        provide_context=True,
    )

    # ترتيب التاسكات
    extract >> transform >> load
