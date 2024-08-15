from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.sensors.sql_sensor import SqlSensor
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG("demo_sqlsensor", start_date=datetime(2024, 4 ,1),schedule_interval=None, default_args=default_args, catchup=False) as dag:

    '''
    Make sure to have following library installed : pip install apache-airflow-providers-postgres
    '''
    create_table_postgres =  PostgresOperator(
        task_id='create_table_postgres',
        postgres_conn_id='postgres_localhost',
        sql= """
        create table if not exists personal_info (
        id varchar,
        name varchar,
        age varchar,
        address varchar,
        occupation varchar
        )
        """
	)
    
    #define SqlSensor
    
    check_records_exists = SqlSensor(
        task_id = 'SqlSensor',
        sql = 'select exists(select 1 from personal_info)',
        conn_id = 'postgres_localhost',
        poke_interval = 5,
        timeout = 180
    )


    data_processing = DummyOperator(task_id='data_processing')

    create_table_postgres  >> check_records_exists >> data_processing
