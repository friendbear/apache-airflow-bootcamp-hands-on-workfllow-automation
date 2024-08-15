from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.models import Variable
from airflow.decorators import task
from airflow.models.baseoperator import chain
from airflow.operators.python import get_current_context
import sqlite3
from airflow.hooks.base import BaseHook
from psycopg2.extras import execute_values
from airflow.hooks.postgres_hook import PostgresHook
from sqlite_to_postgres_operator import SQLiteToPostgresOperator

default_args = {
	'start_date' : datetime(2024,3,31),
	'owner' : 'airflow'

}
 
with DAG('demo_customoperator', default_args=default_args,catchup=False, schedule_interval=None) as dag:
    
    
    t1 = SQLiteToPostgresOperator(
    task_id = 'sqlite_postgresoperator',
    sqlite_conn_id = 'sqlite_conn', 
    postgres_conn_id = 'postgres_localhost' ,
    source_table = 'user_info',
    target_table = 'user_info'
    )