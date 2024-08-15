import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="demo_externaltasksensor", default_args=default_args, schedule_interval="@daily") as dag:
    sensor = ExternalTaskSensor(
        task_id='sensor_task',
        external_dag_id='demo_sleep_dag',
        external_task_id='sleep_task' ,
        allowed_states = ['success'],
        poke_interval=60,
        timeout=600   
    )

    last_task = DummyOperator(task_id="last_task")

    sensor >> last_task



