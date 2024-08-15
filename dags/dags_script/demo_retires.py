from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import time 

def load_data():
    print("sleep for 5 sec")
    #time.sleep(5)
    raise Exception("Python function error")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 1),
    #'retries': 3,  # Retry the task up to 3 times upon failure
    #'retry_delay': timedelta(minutes=5)  # Wait for 5 minutes between retry attempts
}

with DAG('demo_retry_dag', default_args=default_args,catchup=False, schedule_interval='@daily') as dag:
    load_data_task = PythonOperator(
        task_id='load_data_task',
        python_callable=load_data,
        retries = 3,
        retry_exponential_backoff = True,
        retry_delay = timedelta(seconds=5)
    )
