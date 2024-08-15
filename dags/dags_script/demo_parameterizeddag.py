from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models.param import Param

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 14)
}

def my_task(**kwargs):
    print(kwargs)
    database = kwargs['params']['database']
    table = kwargs['params']['table']
    columns = kwargs['params']['columns']
    print(f"Executing task with database: {database}, table: {table}, columns: {columns}")

dag = DAG(
    'demo_parameterizeddag',
    default_args=default_args,
    schedule_interval=None,
    catchup = False,
    params= {
        'database': 'postgres',
        'table': Param(
            'dag_run',
            type='string'),
        'columns': ['col1', 'col2', 'col3']
    }
)

task = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    provide_context=True,
    params={"database": "postgres","table":"dag","columns":["col1"]},
    dag=dag
)

task


