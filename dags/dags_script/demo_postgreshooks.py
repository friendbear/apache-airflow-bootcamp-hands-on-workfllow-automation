from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook


default_args = {
    'owner': 'airflow',
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'start_date': datetime(2024, 4, 1),
}

def hook_function():
    source_hook = PostgresHook(postgres_conn_id = 'postgres_localhost')
    source_conn = source_hook.get_conn()
    source_cursor = source_conn.cursor()
    query = "select table_catalog,table_schema,table_name,column_name,data_type from information_schema.columns where table_name = 'personal_info'"
    source_cursor.execute(query)
    records = source_cursor.fetchall()
    for row in records:
        print(row)
    source_cursor.close()
    source_conn.close()

dag = DAG('demo_postgreshook', default_args=default_args, schedule_interval=None,catchup=False)
	
t1 = PythonOperator(task_id='hook', python_callable=hook_function, provide_context=True, dag=dag)

t1
