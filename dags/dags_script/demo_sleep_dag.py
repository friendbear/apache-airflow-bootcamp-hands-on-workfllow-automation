import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="demo_sleep_dag", default_args=default_args, schedule_interval="@daily") as dag:

    t1 = DummyOperator(task_id="task_1")

    t2 = BashOperator(
            task_id="sleep_task",
            bash_command="sleep 30"
        )
    
    t1 >> t2