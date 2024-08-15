from airflow import DAG
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# Define your DAG
default_args = {
    'start_date': datetime(2024, 5, 3)
}

with DAG('demo_timedeltasensor',
         default_args=default_args,
         schedule_interval=None,
         tags=['TimeDeltaSensor']) as dag:

    #define TimeDeltaSensor
    wait_task = TimeDeltaSensor(
        task_id = 'wait_task',
        delta = timedelta(minutes =3),
        mode = 'poke',
        poke_interval = 2 ,
        timeout = 180
    )
    
        

    downstream_task = DummyOperator(task_id='downstream_task')

    #Define task dependency
    wait_task >> downstream_task