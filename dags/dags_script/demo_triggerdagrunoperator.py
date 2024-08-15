from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

default_args = {
	'start_date' : datetime(2024,4,5),
	'owner' : 'airflow',
	'depends_on_past' : False,
}

def func_1():
	print('This is task1 executing')
	
with DAG(dag_id = 'demo_triggerdagrunoperator',description = 'showcase triggerdagrunoperator',
                          default_args=default_args ,catchup=False,schedule=None) as dag:
	
	t1 = PythonOperator(task_id = 'task1_python_operator',python_callable = func_1)
	
	t2 = TriggerDagRunOperator(task_id = 'task2_triggerdagrunoperator', 
								trigger_dag_id = 'demo_parameterizeddag',
								wait_for_completion = True,
								poke_interval = 60,
								allowed_states = ['success'])
		
						

t1 >> t2
	
	