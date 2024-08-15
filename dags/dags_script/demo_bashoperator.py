from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("demo_bashoperator", default_args=default_args,tags=['tutorial','learning','bash','operator'],
    start_date=days_ago(1),schedule=None)


print_date = BashOperator(task_id="print_date", bash_command='date', dag=dag)

run_script = BashOperator(task_id="run_script",bash_command='./scripts/cmds.sh',dag=dag)

read_variable = BashOperator(task_id = 'read_variable',bash_command = 'echo {{var.value.owner}}',dag=dag)

excute_python_script = BashOperator(task_id='excute_python_script',bash_command='python -c "print(\'Hello from BashOperator\')"',dag=dag)

copy_files = BashOperator(task_id='copy_files',bash_command='cp /home/sriw/files/* /home/sriw/out',dag=dag)

print_date >> run_script >> read_variable >> excute_python_script >> copy_files