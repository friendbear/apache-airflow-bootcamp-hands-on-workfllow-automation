from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 1),
    'retries': 0,  # Disable retries
    'retry_delay': timedelta(seconds=1),
    'execution_timeout': timedelta(seconds=10)
}

with DAG('demo_execution_timeout', default_args=default_args, schedule_interval=None,catchup=False) as dag:

    start_task = BashOperator(task_id="bash_1", bash_command="sleep 5", dag=dag)

    end_task = BashOperator(task_id="bash_2", bash_command="sleep 15", dag=dag)

    start_task >> end_task

