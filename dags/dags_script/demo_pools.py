from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.models.baseoperator import chain


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("demo_pool", default_args=default_args,tags=['tutorial','learning','bash','operator','pools'],
    start_date=days_ago(1),schedule=None)

dummy_task_1 = DummyOperator(task_id='dummy_task_1',dag=dag)
dummy_task_2 = DummyOperator(task_id='dummy_task_2',dag=dag)

t1 = BashOperator(task_id="task_1", bash_command="sleep 30" ,pool = 'pool_1',dag=dag)

t2 = BashOperator(task_id="task_2", bash_command="sleep 30", retries=3,pool = 'pool_1', dag=dag)

t3 = BashOperator(task_id="task_3",bash_command="sleep 30",pool = 'pool_2',dag=dag)

t4 = BashOperator(task_id="task_4",bash_command="sleep 30",pool = 'pool_2',dag=dag)

chain(dummy_task_1,[t1,t2,t3,t4],dummy_task_2)
