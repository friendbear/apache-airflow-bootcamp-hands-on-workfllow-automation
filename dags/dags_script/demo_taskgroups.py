from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.utils.task_group import TaskGroup

default_args = {
    'start_date': datetime(2024, 1, 1),
    'owner': 'airflow'
}

with DAG(dag_id='demo_taskgroups', schedule_interval=None,catchup = False, default_args=default_args) as dag:
    
    start_task = DummyOperator(task_id='start_task')
   
    #define TaskGroup
    with TaskGroup(group_id = 'group_tasks') as group_tasks:
        task_1 = DummyOperator(task_id='task_1')
        task_2 = DummyOperator(task_id='task_2')
        
        with TaskGroup(group_id = 'subgroup_tasks') as subgroup_tasks:
             task_3 = DummyOperator(task_id='task_3')
             task_4 = DummyOperator(task_id='task_4')
             
        task_1 >> task_2 >> subgroup_tasks
        
    end_task = DummyOperator(task_id='end_task')

    start_task  >> group_tasks >>  end_task