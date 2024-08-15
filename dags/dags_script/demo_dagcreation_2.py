from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def func_1():
    print('func_1')
    
def func_2():
    print('func_2')

with DAG("demo_dagcreation_2", default_args = default_args,schedule_interval=None,catchup=False,description='DAG using with context',tags=['with','context_manager','dag']) as dag:

    task_1 = PythonOperator(task_id = 'task_1',python_callable = func_1)
    task_2 = PythonOperator(task_id = 'task_2',python_callable = func_2)

    task_1 >> task_2