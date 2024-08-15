from airflow.decorators import dag,task
from airflow.utils.dates import days_ago

@dag(
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': days_ago(1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
    },
    dag_id = 'demo_dagcreation_3',
    schedule_interval=None,
    catchup=False,
    description='DAG using @dag decorator',
    tags=['taskflow','dag']
)
def my_dag():   
    @task
    def func_1():
        print('func_1')
        
    @task
    def func_2():
        print('func_2')
    
    func_1() >> func_2()

dag = my_dag()
