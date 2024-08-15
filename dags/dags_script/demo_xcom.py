from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def push_xcom(**kwargs):
    kwargs['ti'].xcom_push(key='message', value='Hello from push_task!')

def pull_xcom(**kwargs):
    message = kwargs['ti'].xcom_pull(task_ids='push_task', key='message')
    print(f"Received XCom message: {message}")

dag = DAG('demo_xcom', start_date=datetime(2024, 5, 1), schedule_interval=None,catchup=False)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_xcom,
    provide_context=True,
    dag=dag,
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_xcom,
    provide_context=True,
    dag=dag,
)

push_task >> pull_task