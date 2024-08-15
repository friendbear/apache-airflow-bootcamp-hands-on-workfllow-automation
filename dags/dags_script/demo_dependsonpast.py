from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 4, 1),
    'owner': 'Airflow'
}

def first_func():
    print('This func is executed by first_task')
    
def second_func():
    print('This func is executed by second_task')
    #raise ValueError('This will turn the python task in failed state')

def third_func():
    print('This func is executed by third_task')

with DAG(dag_id='demo_dependsonpast', schedule_interval=timedelta(seconds=30), catchup = False ,default_args=default_args) as dag:
    
    # Task 1
    python_task_1 = PythonOperator(task_id='python_task_1', python_callable=first_func)
    
    # Task 2
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_func,depends_on_past = True)

    # Task 3
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_func)

    python_task_1 >> python_task_2 >> python_task_3

