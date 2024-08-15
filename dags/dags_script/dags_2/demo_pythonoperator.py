from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
import random
import logging
from airflow.models import Variable
from airflow.decorators import task
from airflow.models.baseoperator import chain
from airflow.operators.python import get_current_context

default_args = {
	'start_date' : datetime(2024,3,31),
	'owner' : 'airflow'
}

var_1 = Variable.get('genric_info',deserialize_json = True)
owner = var_1.get('owner')
firstname = var_1.get('firstname')
lastname = var_1.get('lastname')

    
def retrive_values(owner,firstname,lastname,**context):

    #owner = var_1.get('owner')
    #firstname = var_1.get('firstname')
    #lastname = var_1.get('lastname')
    try:
        print("context" , context)
        print(owner,firstname,lastname,context['ds'])
    except:
        print('No context passed')
    #print(\n)
    

@task 
def retrive_values_1(var_1):
    print(var_1)

@task(task_id = 'temp_task') 
def retrive_values_2(var_1):
    context = get_current_context()
    print(context)
    print(var_1)

    
with DAG('demo_pythonoperator', default_args=default_args,catchup=False, schedule_interval=None) as dag:

    

    a_list = [owner,firstname,lastname]
    t2 = PythonOperator(task_id = 't2',python_callable = retrive_values,op_args =a_list)

    a_dict = {'owner': owner,'firstname' :firstname ,'lastname' : lastname}
    t3 = PythonOperator(task_id = 't3',python_callable = retrive_values,op_args = a_dict)

    t5 = PythonOperator(task_id = 't5',python_callable = retrive_values,op_args = a_dict ,provide_context = True)

    chain( t2 , t3  , t5 , retrive_values_1(var_1)>> retrive_values_2(var_1))