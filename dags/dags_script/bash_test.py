from __future__ import annotations
import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["bash", "operator"],
) as dag:

    a = BashOperator(
        task_id="task_1",
        bash_command="echo 123",
    )
    b = BashOperator(
        task_id="task_2",
        bash_command="sleep 1",
    )
    c = BashOperator(
        task_id="task_3",
        bash_command="echo Sriw_World_of_Coding",
    )

a >> b >> c

if __name__ == "__main__":
    dag.test()
