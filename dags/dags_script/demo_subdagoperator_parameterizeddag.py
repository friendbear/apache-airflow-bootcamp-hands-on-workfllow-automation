from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'demo_subdagoperator_parameterizeddag',
    default_args=default_args,
    schedule_interval="*/2 * * * *"
)

trigger_child_dag = TriggerDagRunOperator(
        task_id="trigger_child_dag",
        trigger_dag_id="demo_parameterizeddag",
        conf={"database": "postgres","table":"dag_code","columns":["col1","col2","col3","col4"]},
        dag =dag
    )
