from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.utils.edgemodifier import Label

def preprocess_data():
    # Task to preprocess data
    pass

def train_model():
    # Task to train machine learning model
    pass

def evaluate_model():
    # Task to evaluate the trained model
    pass

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 10),
    'retries': 1,
}

# Define the DAG
dag = DAG('demo_edgelabels', 
          default_args=default_args,
          schedule_interval=None)

# Define tasks
preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

evaluate_task = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag
)

# Define dependencies between tasks

#preprocess_task >> Label('training of data') >> train_task
#train_task >> Label('evaluation of data') >> evaluate_task

preprocess_task.set_downstream(train_task,Label('training of data'))
train_task.set_downstream(evaluate_task,Label('evaluation of data'))