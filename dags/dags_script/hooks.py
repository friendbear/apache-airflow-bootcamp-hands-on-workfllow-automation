from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values

default_args = {
    'owner': 'airflow',
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'start_date': datetime(2024, 4, 12),
}

dag = DAG('demo_postgreshooks', default_args=default_args, schedule_interval=None,catchup=False)

def transfer_function(ds, **kwargs):
    #copy data from 1 table to another

    query = "SELECT * FROM population_details"

    #define source hook
    source_hook = PostgresHook(postgres_conn_id = 'postgres_localhost',schema = 'my_db')
    source_conn = source_hook.get_conn()

    #define destination hook
    destination_hook = PostgresHook(postgres_conn_id = 'postgres_localhost',schema = 'my_db')
    destination_conn = destination_hook.get_conn()
  
    source_cursor = source_conn.cursor()
    destination_cursor = destination_conn.cursor()
    
    source_cursor.execute(query)
    records = source_cursor.fetchall()
    
    execute_values(destination_cursor,"INSERT INTO population_details_bkp values %s", records)
    destination_conn.commit()
    
    #close connection
    source_cursor.close()
    destination_cursor.close()
    source_conn.close()
    destination_conn.close()

    print("Data transferred successfully!")

t1 = PythonOperator(task_id='transfer', python_callable=transfer_function, provide_context=True, dag=dag)

t1