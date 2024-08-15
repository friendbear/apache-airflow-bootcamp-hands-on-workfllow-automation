from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime, timedelta
from airflow.sensors.filesystem import FileSensor
import csv
import requests
import json
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("demo_sensors", start_date=datetime(2024, 4 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:


    is_file_available = FileSensor(
        task_id="is_file_available",
        filepath="/home/sriw/files/test_1.csv",
        poke_interval=5,
        timeout=60
    )
    



