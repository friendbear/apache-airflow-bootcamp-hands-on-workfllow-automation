from airflow import DAG
from airflow.sensors.bash import BashSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define your DAG
default_args = {
    'start_date': datetime(2024, 5, 3)
}

with DAG('demo_bashsensor',
         default_args=default_args,
         schedule_interval=None,
         tags=['BashSensor']) as dag:

    # Define a BashSensor to wait for a file to be created
    wait_for_file_sensor = BashSensor(
        task_id='wait_for_file_sensor',
        bash_command='test -f /home/sriw/files/test.json',
        mode='poke',  
        timeout=180,  
        poke_interval=2  
    )

    # Define downstream tasks
    downstream_task = DummyOperator(task_id='downstream_task')

    # Define task dependencies
    wait_for_file_sensor >> downstream_task
