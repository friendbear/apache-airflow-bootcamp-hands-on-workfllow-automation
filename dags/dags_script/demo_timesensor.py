from airflow import DAG
from airflow.sensors.time_sensor import TimeSensor
from airflow.operators.dummy_operator import DummyOperator
import datetime

# Define your DAG
default_args = {
    'start_date': datetime.datetime(2024, 5, 3)
}

with DAG('demo_timesensor',
         default_args=default_args,
         schedule_interval=None,
         tags=['TimeSensor']) as dag:

    # Define a time sensor
    wait_for_time = TimeSensor(
        task_id = 'wait_for_time',
        target_time = (datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes = 3)).time(),
        mode = 'poke'
    )

    # Define downstream tasks
    downstream_task = DummyOperator(task_id='downstream_task')

    # Define task dependencies
    wait_for_time >> downstream_task
