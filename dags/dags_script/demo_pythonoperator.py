from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.models import Variable
from airflow.decorators import task
from airflow.operators.python import get_current_context

default_args = {
	'start_date' : datetime(2024,3,31),
	'owner' : 'airflow'

}
#read variables from Airflow Variable View
var_1 = Variable.get('genric_info',deserialize_json=True)
owner = var_1.get('owner')
firstname = var_1.get('firstname')
lastname = var_1.get('lastname')

def retrive_values(owner,firstname,lastname):
    print(owner,firstname,lastname)

def retrive_values_1(**kwargs):
    print(kwargs)

@task(task_id = 'task_3')  
def retrive_values_2(var_1):
    context  = get_current_context()
    print(context)
    print(var_1)
    
with DAG('demo_pythonoperator', default_args=default_args,catchup=False, schedule_interval=None) as dag:
    
    #pass argument to python function
    t1 = PythonOperator(task_id = 't1',python_callable = retrive_values,op_args = [owner,firstname,lastname])
    
    t2 = PythonOperator(task_id = 't2',python_callable = retrive_values_1,op_kwargs = var_1)
    
    #call a Python function using TaskFlow
    retrive_values_2(var_1)

