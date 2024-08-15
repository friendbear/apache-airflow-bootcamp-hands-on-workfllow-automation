from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 1, 1, 21),
    'owner': 'Airflow'
}

with DAG(dag_id='demo_dag_version_v1', schedule="2 * * * *",catchup = False, default_args=default_args) as dag:
    
    
    task_1 = BashOperator(task_id= 'task_1',bash_command = 'echo 123')
    task_2 = BashOperator(task_id= 'task_2',bash_command = 'echo 123')
    task_3 = BashOperator(task_id= 'task_3',bash_command = 'echo 123')


task_1 >> task_2 >> task_3