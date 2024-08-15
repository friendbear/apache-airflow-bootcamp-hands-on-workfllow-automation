from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.operators.python import get_current_context
from airflow.decorators import task

default_args = {
    'start_date' : datetime(2024,3,31),
    'owner' : 'airflow'
}

def retrive_context(**context):
    print('context : ',context)
    print('conf : ',context.get('conf'))
    print('conn : ',context.get('conn'))  
    print('dag : ',context.get('dag'))               
    print('dag_run : ',context.get('dag_run'))
    print('data_interval_start : ',context.get('data_interval_start'))
    print('data_interval_end : ',context.get('data_interval_end'))  
    print('ds : ',context.get('ds'))
    print('execution_date : ',context.get('execution_date'))    
    print('next_ds : ',context.get('next_ds'))
    print('next_execution_date : ',context.get('next_execution_date'))
    print('params : ',context.get('params'))
    print('task_instance : ',context.get('task_instance'))  
    print('task : ',context.get('task'))      
    print('ti : ',context.get('ti'))      
    print('exception : ',context.get('exception'))               
    print('run_id : ',context.get('run_id'))    

with DAG('demo_contextparameters', default_args=default_args,catchup=False, schedule_interval="*/2 * * * *") as dag:
    
    t1 = PythonOperator(task_id = 'task_1',python_callable = retrive_context,provide_context = True)

    @task(task_id = 'task_2')
    def retrive_context_taskflow():
        context_taskflow = get_current_context()
        print(context_taskflow)
        print('run_id : ' ,context_taskflow.get('run_id'))  
        print('task : ' ,context_taskflow.get('task'))        
        print('dag : ' ,context_taskflow.get('dag'))
        
    t1 >> retrive_context_taskflow()



