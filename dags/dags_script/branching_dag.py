from airflow import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, date
from airflow.utils.trigger_rule import TriggerRule


def decide_branch():
    # Logic to determine which branch to take
    someday = date(2024, 4, 3)


    today = date.today()
    diff = (today - someday).days
    if diff > 0 :
        return 'task_1'
    elif diff < 0:
        return 'task_2'
    else:
        return ['task_3','task_4']

# Create a DAG
dag = DAG('branching_dag', start_date=datetime(2024, 3, 3),catchup=False)

# Start with the initial task
start_task = DummyOperator(task_id='start_task', dag=dag)

# Define the BranchPythonOperator
branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=decide_branch,
    dag=dag,
)


# Define the two branches
task_1 = DummyOperator(task_id='task_1', dag=dag)
task_2 = DummyOperator(task_id='task_2', dag=dag)
task_3 = DummyOperator(task_id='task_3', dag=dag)
task_4 = DummyOperator(task_id='task_4', dag=dag)
# End task
end_task = DummyOperator(task_id='end_task', dag=dag,trigger_rule=TriggerRule.ONE_SUCCESS)


start_task >> branch_task
branch_task >> [task_1,task_2,task_3,task_4]
[task_1,task_2,task_3,task_4] >> end_task





