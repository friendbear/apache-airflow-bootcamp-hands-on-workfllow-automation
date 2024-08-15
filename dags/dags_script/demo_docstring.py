from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag_md_doc = """
## following tasks will be done in this dag

Data Preprocessing: Clean and preprocess the data to make it suitable for training. This may involve handling missing values, encoding categorical variables, scaling features, etc.

Model Training: Train the selected model(s) on the preprocessed data. This step involves feeding the data into the model and optimizing its parameters.

Model Evaluation: Assess the performance of the trained model(s) using appropriate evaluation metrics. This step helps you understand how well the model generalizes to new, unseen data.
"""

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


doc_md_task = """

### Purpose of this task

This task will preprocess the data and prepare data for training.
"""
doc_monospace_task = """
This task will preprocess the data and prepare data for training.
"""
doc_json_task = """
{
    "purpose": {
        "Aim": "This task will preprocess the data and prepare data for training."
    }
}
"""
doc_yaml_task = """
---
purpose: This task will preprocess the data and prepare data for training.
"""
doc_rst_task = """
===========
purpose
===========
This task will preprocess the data and prepare data for training
"""

# Define the DAG
dag = DAG('demo_docstring', 
          default_args=default_args,
          schedule_interval=None,
          doc_md=dag_md_doc)

# Define tasks
preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    doc_md=doc_md_task,
    doc=doc_monospace_task,
    doc_json=doc_json_task,
    doc_yaml=doc_yaml_task,
    doc_rst=doc_rst_task,
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

preprocess_task >> train_task
train_task >> evaluate_task
