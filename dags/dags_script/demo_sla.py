from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
import pendulum

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["sriwworldofcoding@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "start_date" : pendulum.datetime(2024, 5,1, tz="UTC")
}

def sla_miss(*args,**kwargs):
    print("SLA miss happened")
    
dag = DAG("demo_sla_1", default_args=default_args,tags=['tutorial','learning','bash','operator','sla'],schedule="* * * * *",catchup= True,sla_miss_callback = sla_miss)

t1 = BashOperator(task_id="task_1", bash_command="echo 'task_1' && sleep 10",sla= timedelta(seconds=5) ,dag=dag)

t2 = BashOperator(task_id="task_2", bash_command="echo 'task_2'", retries=3, dag=dag)

t3 = BashOperator(task_id="task_3",bash_command="echo 'task_3'",dag=dag)

t1 >> t2 >> t3
