from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.sql import BranchSQLOperator
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG("demo_branchsqloperator", start_date=datetime(2024, 4 ,1),schedule_interval=None, default_args=default_args, catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
        
    branch_task = BranchSQLOperator(
        task_id = 'branch_task',
        sql = 'select count(1) from personal_info;',
        follow_task_ids_if_true = ['task_2'],
        follow_task_ids_if_false = ['task_3'],
        conn_id = 'postgres_localhost'
        )

    task_2 = DummyOperator(task_id='task_2')
    task_3 = DummyOperator(task_id='task_3')

    chain(start_task, branch_task ,[task_2,task_3])