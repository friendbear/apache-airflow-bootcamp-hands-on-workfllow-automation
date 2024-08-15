from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 4, 1),
    'owner': 'Airflow'
}

def first_func():
    print('This is first_task')

def second_func():
    print('This is second_task')
    #raise ValueError('This will turns the python task in failed state')

def third_func():
    print('This is third_task')


with DAG(dag_id='demo_wait_for_downstream', schedule_interval=timedelta(seconds=30),catchup = False, default_args=default_args) as dag:
    
    # Task 1
    python_task_1 = PythonOperator(task_id='python_task_1', python_callable=first_func,wait_for_downstream =True)

    # Task 2
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_func)

    # Task 3
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_func)

    python_task_1 >> python_task_2 >> python_task_3