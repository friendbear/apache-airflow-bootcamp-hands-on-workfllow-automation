from airflow import DAG
from airflow.operators.sqlite_operator import SqliteOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner' : 'airflow'
}

with DAG(dag_id = 'demo_sqliteoperator',default_args = default_args,start_date = days_ago(1),schedule_interval = None) as dag:
    create_table = SqliteOperator(
        task_id = 'create_table',
        sql = r"""
            CREATE TABLE IF NOT EXISTS user_info (
                    id INTEGER,
                    name VARCHAR,
                    age INTEGER 
            );
        """,
        sqlite_conn_id = 'sqlite_conn',
        dag = dag,
    )

    insert_values = SqliteOperator(
        task_id = 'insert_values',
        sql = r"""
            INSERT INTO user_info (id,name, age) VALUES 
                (1,'Sam', 33),
                (2,'Kristen', 25),
                (3,'Robert', 31);
        """,
        sqlite_conn_id = 'sqlite_conn',
        dag = dag,
    )

    display_records = SqliteOperator(
        task_id = 'display_records',
        sql = r"""SELECT * FROM user_info""",
        sqlite_conn_id = 'sqlite_conn',
        dag = dag,
        do_xcom_push = True
    )

create_table >> insert_values >> display_records