from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime
from airflow.operators.email_operator import EmailOperator

def send_success_status_email(**context):
    task_instance = context['task_instance']
    task_status = task_instance.current_state()
    
    subject = f"Airflow task {task_instance.task_id} : {task_status}"
    body = f"The task {task_instance.task_id} finished with status  : {task_status}"
    
    to_email = "sriwworldofcoding@gmail.com"
    send_email(to = to_email , subject = subject, html_content = body)
    
    
with DAG(dag_id = 'demo_sendmail_2',start_date=datetime(2024, 1, 1),catchup=False, schedule_interval=None) as dag:

    success_email_task = PythonOperator(
        task_id='success_email_task',
        python_callable = send_success_status_email,
        provide_context=True)
    
    
    email_task = EmailOperator(
        task_id = 'email_task',
        to = "sriwworldofcoding@gmail.com",
        subject = "Mail sent from airflow",
        html_content = "Email is sent from emailoperator "
      
    )


success_email_task  >> email_task