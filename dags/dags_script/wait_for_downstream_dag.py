from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 4, 1),
    'owner': 'Airflow'
}

def second_task():
    print('This is second_task')
    #raise ValueError('This will turns the python task in failed state')

def third_task():
    print('This is third_task')
    #raise ValueError('This will turns the python task in failed state')

with DAG(dag_id='demo_wait_for_downstream_task', schedule_interval="*/1 * * * *",catchup = False, default_args=default_args) as dag:
    
    # Task 1
    bash_task_1 = BashOperator(task_id='bash_task_1', bash_command="echo 'This is first task'",wait_for_downstream =True)
    
    # Task 2
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_task)

    # Task 3
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_task)

    bash_task_1 >> python_task_2 >> python_task_3