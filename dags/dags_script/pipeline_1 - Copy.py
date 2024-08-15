from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime, timedelta
from airflow.sensors.filesystem import FileSensor
import csv
import requests
import json
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
def download_rates():
    BASE_URL = "https://gist.githubusercontent.com/marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b/raw/"
    ENDPOINTS = {
        'USD': 'api_forex_exchange_usd.json',
        'EUR': 'api_forex_exchange_eur.json'
    }
    with open('/home/sriw/files/forex_currencies.csv') as forex_currencies:
        reader = csv.DictReader(forex_currencies, delimiter=';')
        for idx, row in enumerate(reader):
            base = row['base']
            with_pairs = row['with_pairs'].split(' ')
            indata = requests.get(f"{BASE_URL}{ENDPOINTS[base]}").json()
            outdata = {'base': base, 'rates': {}, 'last_update': indata['date']}
            for pair in with_pairs:
                outdata['rates'][pair] = indata['rates'][pair]
            with open('/home/sriw/files/forex_rates.json', 'a') as outfile:
                json.dump(outdata, outfile)
                outfile.write('\n')

with DAG("data_pipeline", start_date=datetime(2021, 1 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    '''
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        http_conn_id="forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        filepath="/home/sriw/files/forex_currencies.csv",
        poke_interval=5,
        timeout=20
    )
    
    downloading_rates = PythonOperator(
        task_id = 'downloading_rates',
        python_callable =  download_rates
    )
    '''
    create_table_postgres =  PostgresOperator(
        task_id='create_table_postgres',
        postgres_conn_id='postgres_localhost',
        sql=""" 
            create table if not exists dag_runs (
            dt date,
            dag_id varchar,
            primary key (dt,dag_id))
            """
    )

    postgres_task = PostgresOperator(
        task_id='postgres_task',
        postgres_conn_id='postgres_localhost',
        sql='SELECT * FROM dag_runs'

)

    #is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> 
    create_table_postgres >> postgres_task
