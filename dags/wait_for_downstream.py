from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18),
}

def first_func():
    print("This is first_task")

def second_func():
    print("This is second task")
    raise ValueError("This will turn the python task in failed state")

def third_task():
    print("This is third task")

with DAG(
    dag_id='demo_wait_for_downstream', 
    schedule_interval=timedelta(seconds=30),
    catchup=False,
    default_args=default_args
) as dag:

    python_task_1 = PythonOperator(task_id='python_task_1', python_callable=first_func, wait_for_downstream=True) # 💫 if failer then wait for downstream
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_func)
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_task)

    python_task_1 >> python_task_2 >> python_task_3


