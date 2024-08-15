from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime , timedelta
import time 
from airflow.utils.dates import days_ago

default_args = {
    'start_date' : days_ago(1),
    'owner' : 'airflow',
    "email": ["sriwworldofcoding@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
}

def sleep_function():
    print("Output of sleep_function")
    time.sleep(10)

def success_function():
    print("Output of success_function")

def failure_function():
    print("Output of failure_function")
    raise Exception("Output of failure_function")
    
def retry_function():
    print("Output of retry_function")
    raise Exception("Output of retry_function")
    
def sla_callback(*args,**kwargs):
    print("Output of sla_callback")
    
def success_callback(*args,**kwargs):
    print("Output of success_callback")
    
def retry_callback(*args,**kwargs):
    print("Output of retry_callback")
    
def failure_callback(*args,**kwargs):
    print("Output of failure_callback")

def execute_callback(*args,**kwargs):
    print("Output of execute_callback")


 
dag = DAG("demo_callbackfunction",
    default_args=default_args,
    tags=['tutorial','learning','callback'],
    schedule="*/2 * * * * ",
    catchup= True,
    sla_miss_callback = sla_callback,
  )

task_1 = PythonOperator(task_id = 'task_1',
    python_callable = sleep_function ,
    sla = timedelta(seconds=5),
    dag = dag
)

task_2 = PythonOperator(task_id = 'task_2',
    python_callable = success_function ,
    on_success_callback=success_callback,
    dag = dag
)
    
task_3 = PythonOperator(task_id = 'task_3',
    python_callable = failure_function ,
    on_failure_callback=failure_callback,
    dag = dag
)

task_4 = PythonOperator(task_id='task_4',
        python_callable=retry_function,
        retries = 3,
        retry_exponential_backoff = True,
        retry_delay = timedelta(seconds=2),
        on_retry_callback = retry_callback,
        trigger_rule="all_done",
        dag = dag
)

task_5 = PythonOperator(task_id = 'task_5',
    python_callable = success_function ,
    on_execute_callback = execute_callback,
    on_success_callback = success_callback,
    trigger_rule="all_done",
    dag = dag
)

task_1 >> task_2 >> task_3 >> task_4  >> task_5

