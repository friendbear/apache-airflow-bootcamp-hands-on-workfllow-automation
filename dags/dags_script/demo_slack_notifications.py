from airflow import DAG
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def fail():
    raise Exception("Task failed intentionally for testing purpose")


def success():
    print("success")


def notification(context):
    slack_icon = "large_green_circle" if context.get('task_instance').state == "success" else "red_circle"
    task_state = context.get('task_instance').state
    task_id = context.get('task_instance').task_id
    dag_id = context.get('task_instance').dag_id
    task_exec_date = context.get('execution_date')
    task_log_url = context.get('task_instance').log_url

    slack_msg = """
            :{icon}: Task {state}.
            *Dag*: {dag} 
            *Task*: {task}  
            *Execution Time*: {exec_date}  
            *Log Url*: {log_url} 
            """.format(
        icon=slack_icon,
        state=task_state,
        dag=task_id,
        task=dag_id,
        exec_date=task_exec_date,
        log_url=task_log_url)
    html_msg = """
    <html>
      <body>
        <h2>Task Execution Notification</h2>
        <p>
          <strong>Task State:</strong> {state}<br>
          <strong>DAG:</strong> {dag}<br>
          <strong>Task:</strong> {task}<br>
          <strong>Execution Time:</strong> {exec_date}<br>
          <strong>Log URL:</strong> <a href="{log_url}">{log_url}</a><br>
        </p>
      </body>
    </html>
    """.format(
        state=task_state,
        dag=task_id,
        task=dag_id,
        exec_date=task_exec_date,
        log_url=task_log_url
    )
    slack_webhook_task = SlackWebhookOperator(
        task_id='slack_notification',
        http_conn_id='slack_conn',
        message=slack_msg,
        channel="#learnerpage")
    slack_webhook_task.execute(context=context)



default_args = {
    "owner": "airflow",
    "retries": 0,
    "on_failure_callback": notification,
    "on_success_callback": notification
}

with DAG(
        dag_id="demo_slack_notifications",
        start_date=datetime(2021, 1, 1),
        schedule_interval="@daily",
        default_args=default_args,
        description='Test Slack and Email Notification in case of job failure and success',
        catchup=False
) as dag:
    task_1 = PythonOperator(
        task_id="slack_notification_test",
        python_callable=fail
    )

    task_2 = PythonOperator(
        task_id="slack_notification_test2",
        python_callable=success
    )