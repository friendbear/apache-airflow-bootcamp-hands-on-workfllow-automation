from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook
from io import StringIO
import pandas as pd

default_args = {
    'owner': 'airflow',
    "retries": 1,
    "retry_delay": timedelta(seconds=15),
    'start_date': datetime(2024, 4, 1),
}

dag = DAG('demo_s3hook', default_args=default_args, schedule_interval=None,catchup=False)

def read_s3_file():

    s3_hook = S3Hook(aws_conn_id = 'conn_id_aws_s3')

    bucket_name = 'airflow-tutorial-demo-bucket'

    file_content = s3_hook.read_key(bucket_name = bucket_name ,key = 'activity.csv')

    if isinstance(file_content,bytes):
        file_content = file_content.decode('utf-8')

    df = pd.read_csv(StringIO(file_content))

    return df.to_json()


read_s3_file = PythonOperator(
    task_id = 'read_s3_file',
    python_callable = read_s3_file,
    dag= dag 
)
