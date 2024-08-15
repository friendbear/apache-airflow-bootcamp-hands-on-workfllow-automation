from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("demo_filesensors", start_date=datetime(2024, 4 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:


    is_file_available = FileSensor(
        task_id="is_file_available",
        filepath="/home/sriw/files/test.csv",
        poke_interval=5,
        timeout=60,
        fs_conn_id='fs_default',
        mode='poke'
    )

    process_file_task = DummyOperator(task_id='process_file_task')


    is_file_available >> process_file_task
    



