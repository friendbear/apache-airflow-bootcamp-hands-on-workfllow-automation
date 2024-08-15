from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models.param import Param

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 13)
}

dag = DAG(
    'demo_parameterizeddag_1',
    default_args=default_args,
    schedule_interval="*/2 * * * *",
    catchup = False,
    params= {
        'database': 'my_database',
        'table': 'my_table',
        "table": Param(
            'my_table',
            type="string"),
        'columns': ['col1', 'col2', 'col3']
    }
)

# Example task that accesses parameters from params
def my_task(**kwargs):
    print(kwargs)
    database = kwargs['params']['database']
    table = kwargs['params']['table']
    columns = kwargs['params']['columns']
    print(f"Executing task with database: {database}, table: {table}, columns: {columns}")

task = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    provide_context=True,
    params={"database": "postgres","table":"my_table_1","columns":["col1"]},
    dag=dag
)

task


