from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.weekday import BranchDayOfWeekOperator
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

with DAG("demo_branchdayofweekoperator", start_date=datetime(2024, 4 ,1),schedule_interval=None, default_args=default_args, catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    
    #define BranchDayOfWeekOperator
    branch_task = BranchDayOfWeekOperator(
        task_id = 'branch_task',
        follow_task_ids_if_true = ['task_2'],
        follow_task_ids_if_false = ['task_3'],
        week_day = 'Sunday'
    )

    task_2 = DummyOperator(task_id='task_2')
    task_3 = DummyOperator(task_id='task_3')

    chain(start_task ,branch_task,[task_2,task_3])