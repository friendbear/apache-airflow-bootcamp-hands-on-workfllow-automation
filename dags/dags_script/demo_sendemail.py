from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import time 
#import logging
import sys

def load_data():
    raise Exception("Python function error")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 1),
    'email' : 'sriwworldofcoding@gmail.com',
    'email_on_failure' : True,
    'email_on_retry' : False
}


with DAG('demo_sendmail', default_args=default_args,catchup=False, schedule_interval=None) as dag:
    load_data_task = PythonOperator(
        task_id='load_data_task',
        python_callable=load_data,
        retries = 3,
        retry_exponential_backoff = True,
        retry_delay = timedelta(seconds=5)
    )
