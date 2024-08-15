from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("first_tutorial", default_args=default_args,tags=['tutorial','learning','bash','operator'],
    start_date=days_ago(1),schedule=None)


t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)

t2 = BashOperator(task_id="sleep", bash_command="sleep 20", retries=3, dag=dag)

t3 = BashOperator(task_id="list_files",bash_command="ls",dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)
