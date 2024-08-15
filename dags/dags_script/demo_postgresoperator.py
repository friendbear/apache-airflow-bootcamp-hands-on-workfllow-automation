from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG("demo_postgresoperator", start_date=datetime(2024, 4 ,1),schedule_interval=None, default_args=default_args, catchup=False) as dag:

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

    insert_table_postgres =  PostgresOperator(
        task_id='insert_table_postgres',
        postgres_conn_id='postgres_localhost',
        sql= "scripts/insert_into_table.sql"
    )
    
    multi_postgres_task = PostgresOperator(
        task_id='multi_postgres_task',
        postgres_conn_id='postgres_localhost',
        sql= ['select count(1) from personal_info',"scripts/delete_from_table.sql"],
        params = {'id' : '1'}
)

    create_table_postgres >> insert_table_postgres >> multi_postgres_task
