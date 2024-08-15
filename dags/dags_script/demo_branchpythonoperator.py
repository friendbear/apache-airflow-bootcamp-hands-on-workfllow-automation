from airflow import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, date
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.dates import days_ago

def decide_branch():
    someday = date(2024,6,25)
    today = date.today()
    diff = (today - someday).days
    if diff > 0:
        return 'task_1'
    elif diff < 0:
        return 'task_2'
    else:
        return ['task_3','task_4']

dag = DAG('demo_branchpythonoperator', start_date=days_ago(1),schedule_interval =None ,catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

branch_task =BranchPythonOperator (
    task_id = 'branch_task' ,
    python_callable = decide_branch,
    dag=dag)

task_1 = DummyOperator(task_id='task_1', dag=dag)
task_2 = DummyOperator(task_id='task_2', dag=dag)
task_3 = DummyOperator(task_id='task_3', dag=dag)
task_4 = DummyOperator(task_id='task_4', dag=dag)

end_task = DummyOperator(task_id='end_task', dag=dag,trigger_rule=TriggerRule.ONE_SUCCESS)

start_task >> branch_task >> [task_1,task_2,task_3,task_4] >>  end_task




