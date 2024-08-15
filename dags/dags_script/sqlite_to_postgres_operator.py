import sqlite3
from psycopg2.extras import execute_values
from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.hooks.base import BaseHook
from airflow.utils.decorators import apply_defaults

class SQLiteToPostgresOperator(BaseOperator):
    @apply_defaults
    def __init__(self, sqlite_conn_id, postgres_conn_id,source_table,target_table, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.sqlite_conn_id = sqlite_conn_id
        self.postgres_conn_id = postgres_conn_id
        self.source_table = source_table
        self.target_table = target_table
        
    def get_sqlite_conn(self):
        conn = BaseHook.get_connection(self.sqlite_conn_id)
        return sqlite3.connect(conn.host)

    def get_postgres_conn(self):
        postgres_hook = PostgresHook(postgres_conn_id = self.postgres_conn_id)
        return postgres_hook.get_conn()
         

    def execute(self, context):
        sqlite_conn = self.get_sqlite_conn()
        postgres_conn = self.get_postgres_conn()
        sqlite_cursor = sqlite_conn.cursor()
        postgres_cursor = postgres_conn.cursor()

        sqlite_cursor.execute(f"SELECT * FROM {self.source_table}")
        rows = sqlite_cursor.fetchall()
        insert_query = f"INSERT INTO {self.target_table} VALUES %s"
        execute_values(postgres_cursor,insert_query, rows)

        postgres_conn.commit()

        sqlite_cursor.close()
        postgres_cursor.close()
        sqlite_conn.close()
        postgres_conn.close()
        
