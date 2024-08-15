from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

def task_1():
    print("task_1")
    #raise ValueError("error")

def task_2():
    print("task_2")
    #raise ValueError("error")

def task_3b_all_failed():
    print("task_3b_all_failed")
    #raise ValueError("error")

def task_4b_one_success():
    print("task_4b_one_success")
    #raise ValueError("error")

def task_5b_all_done():
    print("task_5b_all_done")
    #raise ValueError("error")

def task_6b_none_failed():
    print("task_6b_none_failed")
    #raise ValueError("error")

def task_7b_one_failed():
    print("task_7b_one_failed")
    #raise ValueError("error")

with DAG(dag_id='trigger_rule_dag', default_args=default_args, schedule = None) as dag:

    
    task_1a = PythonOperator(
        task_id='task_1',
        python_callable=task_1
    )

    task_2a = PythonOperator(
        task_id='task_2',
        python_callable=task_2    
    )


    task_3a_all_failed = PythonOperator(
        task_id='task_3_all_failed',
        python_callable=task_3b_all_failed,
        trigger_rule="all_failed"
    )

    task_4a_one_success = PythonOperator(
        task_id='task_4_one_success',
        python_callable=task_4b_one_success,
        trigger_rule="one_success"
    )

    task_5a_all_done = PythonOperator(
        task_id='task_5_all_done',
        python_callable=task_5b_all_done,
        trigger_rule="all_done"
    )

    task_6a_none_failed = PythonOperator(
        task_id='task_6_none_failed',
        python_callable=task_6b_none_failed,
        trigger_rule="none_failed"
    )

    task_7a_one_failed = PythonOperator(
        task_id='task_7_one_failed',
        python_callable=task_7b_one_failed,
        trigger_rule="one_failed"
    )

[task_1a,task_2a] >> task_3a_all_failed
[task_1a,task_2a] >> task_4a_one_success
[task_3a_all_failed ,task_4a_one_success ] >> task_5a_all_done
task_5a_all_done >> task_6a_none_failed
task_5a_all_done >> task_7a_one_failed

