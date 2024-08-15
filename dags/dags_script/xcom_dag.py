import logging
import random
from datetime import datetime, timedelta

from airflow import DAG, AirflowException
from airflow.operators.python_operator import PythonOperator

def task_xcom_push(**kwargs):
    print(kwargs)
    #ti = kwargs['ti']
    #ti.xcom_push(key= 'message',value="This is message")
    return "This is message"
    
    

def task_xcom_pull(**kwargs):
    print(kwargs)
    ti = kwargs['ti']
    #message = ti.xcom_pull(key= 'message')
    message = ti.xcom_pull()

    print(message)

with DAG(
    "xcom_part_2",
    start_date=datetime(2023, 2, 27),
    schedule=timedelta(minutes=5),
    catchup = False
) as dag:
    task_1 = PythonOperator(
        task_id="task_xcom_push", python_callable=task_xcom_push,provide_context=True
    )
    task_2 = PythonOperator(task_id="task_xcom_pull", python_callable=task_xcom_pull,provide_context=True)
    task_1 >> task_2