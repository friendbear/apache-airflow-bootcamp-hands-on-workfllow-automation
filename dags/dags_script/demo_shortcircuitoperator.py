from airflow import DAG
from airflow.operators.python_operator import ShortCircuitOperator
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 24)
}

def check_condition():
    return True


with DAG('demo_shortcircuitoperator', default_args=default_args, schedule_interval=None) as dag:
    
    dummy_task_1 = DummyOperator(task_id='dummy_task_1')
    dummy_task_2 = DummyOperator(task_id='dummy_task_2')
    
    # Define the short circuit operator
    condition_check = ShortCircuitOperator(
    task_id = 'check_condition',
    python_callable = check_condition
    )

    # Downstream tasks
    task_to_skip = DummyOperator(task_id='task_to_skip')

    dummy_task_1 >> dummy_task_2 >> condition_check >> task_to_skip
