from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    'start_date': datetime(2024, 4, 11),
}

dag = DAG("demo_latestOnlyOperator", default_args=default_args,tags=['tutorial','learning','bash','operator','latestonlyoperator'],schedule='@daily')

t1 = LatestOnlyOperator(task_id = 'latest_only')

t2 = BashOperator(task_id="task_1", bash_command="sleep 1" ,dag=dag)

t3 = BashOperator(task_id="task_2", bash_command="sleep 1", dag=dag)

t4 = BashOperator(task_id="task_3",bash_command="sleep 1",dag=dag)

t5 = BashOperator(task_id="task_4",bash_command="sleep 1",dag=dag)

t1 >> t2 >> t3 >> t4


