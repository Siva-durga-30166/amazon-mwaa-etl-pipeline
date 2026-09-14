from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import os


def extract_data():
    print("EXTRACT: Reading data sources...")

    sales = pd.read_csv("data/sales.csv")
    customers = pd.read_csv("data/customers.csv")

    print("Sales data extracted successfully.")
    print("Customer data extracted successfully.")

    return "Data extracted successfully"


def transform_data():
    print("TRANSFORM: Processing data...")

    sales = pd.read_csv("data/sales.csv")
    customers = pd.read_csv("data/customers.csv")

    df = pd.merge(sales, customers, on="customer_id", how="inner")

    df["total_amount"] = df["quantity"] * df["price"]

    df = df.dropna()

    df["customer_name"] = df["customer_name"].str.upper()

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/transformed_sales.csv", index=False)

    print("Data transformed successfully.")


def load_data():
    print("LOAD: Creating final output...")

    df = pd.read_csv("output/transformed_sales.csv")

    df.to_csv("output/processed_sales.csv", index=False)

    print("Processed data loaded successfully.")


with DAG(
    dag_id="multi_source_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "data-engineering", "mwaa"]
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    extract >> transform >> load