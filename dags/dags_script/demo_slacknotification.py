from airflow import DAG
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow"
}

with DAG("demo_slacknotification", start_date=datetime(2024, 5 ,1), schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    send_slack_notification = SlackWebhookOperator(
        task_id='slack_notification',
        slack_webhook_conn_id='slack_conn',
        message='Messege sent from Airflow Dag',
        channel='#notification',
        username='airflow'
    )

    send_slack_notification 