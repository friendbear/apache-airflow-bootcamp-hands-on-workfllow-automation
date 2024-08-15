from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
import random
import logging
from airflow.models import Variable


default_args = {
	'start_date' : datetime(2024,3,31),
	'owner' : 'airflow'
}

var_1 = Variable.get('genric_info',deserialize_json = True)

def retrive_values():

    owner = var_1.get('owner')
    firstname = var_1.get('firstname')
    lastname = var_1.get('lastname')
    print(owner,firstname,lastname)
    
dag = DAG('retrive_variables',default_args=default_args,catchup=False)

t1 = BashOperator(task_id = 'var1',bash_command = 'echo {{var.value.owner}}',dag=dag)
t2 = PythonOperator(task_id = 'var2',python_callable = retrive_values,dag=dag)

t1 >> t2

