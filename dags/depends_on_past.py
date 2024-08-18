from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 8, 15),
    "schedule_cron": "1/60 * * * *",
}

def first_func():
    print("This func is executed by the first task")

def second_func():
    print("This func is executed by the second task")
    raise ValueError("This will turn the python task state to failed")

def third_func():
    print("This func is executed by the third task")

with DAG(
    "depends_on_past", # 💫 this option can't running when failed. not running after tasks.
    default_args=default_args,
    schedule_interval=timedelta(1),
    catchup=False,
) as dag:
    first_task = PythonOperator(
        task_id="first_task",
        python_callable=first_func,
    )

    second_task = PythonOperator(
        task_id="second_task",
        python_callable=second_func,
        depends_on_past=True,
    )

    third_task = PythonOperator(
        task_id="third_task",
        python_callable=third_func,
        depends_on_past=True,
    )

    first_task >> second_task >> third_task
