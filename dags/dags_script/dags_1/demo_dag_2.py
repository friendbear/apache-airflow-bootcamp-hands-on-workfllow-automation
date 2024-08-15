from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 1, 1, 21),
    'owner': 'Airflow'
}

with DAG(dag_id='demo_dag_2', schedule="2 * * * *",catchup = False, default_args=default_args) as dag:
    
    # Task 1
    dummy_task_1 = DummyOperator(task_id='dummy_task_1')
    
    # Task 2
    dummy_task_2 = DummyOperator(task_id='dummy_task_2')
    
    dummy_task_1 >> dummy_task_2
