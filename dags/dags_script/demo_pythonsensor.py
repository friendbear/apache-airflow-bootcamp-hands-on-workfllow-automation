from airflow import DAG
from airflow.sensors.python import PythonSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define your Python function to check a condition
def check_condition():
    # Your condition logic goes here
    # For example, you can check if a specific file exists or a database record is updated
    # If the condition is met, return True, otherwise return False
    return False  # For demonstration, always return True

# Define your DAG
default_args = {
    'start_date': datetime(2024, 5, 3)
}

with DAG('demo_pythonsensor',
         default_args=default_args,
         schedule_interval=None,
         tags=['PythonSensor']) as dag:

    # Define a PythonSensor to wait for a condition to be met
    wait_for_condition_sensor = PythonSensor(
        task_id='wait_for_condition_sensor',
        python_callable=check_condition,
        mode='poke',  
        timeout=60,  
        poke_interval=2  
    )

    # Define downstream tasks
    downstream_task = DummyOperator(task_id='downstream_task')

    # Define task dependencies
    wait_for_condition_sensor >> downstream_task
