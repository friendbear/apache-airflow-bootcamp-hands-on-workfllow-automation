from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.models.baseoperator import chain
from datetime import datetime, timedelta
from airflow.models.baseoperator import chain_linear
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup

default_args = {
    'start_date': datetime(2024, 1, 1),
    'owner': 'airflow'
}

with DAG(dag_id='demo_task_dependency', schedule="5 * * * *",catchup = False, default_args=default_args) as dag:
    
    dummy_task_1 = DummyOperator(task_id='dummy_task_1')
    dummy_task_2 = DummyOperator(task_id='dummy_task_2')
    dummy_task_3 = DummyOperator(task_id='dummy_task_3')
    dummy_task_4 = DummyOperator(task_id='dummy_task_4')
    dummy_task_5 = DummyOperator(task_id='dummy_task_5')
    dummy_task_6 = DummyOperator(task_id='dummy_task_6')
    dummy_task_7 = DummyOperator(task_id='dummy_task_7')
    dummy_task_8 = DummyOperator(task_id='dummy_task_8')
    dummy_task_9 = DummyOperator(task_id='dummy_task_9')
    dummy_task_10 = DummyOperator(task_id='dummy_task_10')
    dummy_task_11 = DummyOperator(task_id='dummy_task_11')
    dummy_task_12 = DummyOperator(task_id='dummy_task_12')
    dummy_task_13 = DummyOperator(task_id='dummy_task_13')
    dummy_task_14 = DummyOperator(task_id='dummy_task_14')
    dummy_task_15 = DummyOperator(task_id='dummy_task_15')
    dummy_task_16 = DummyOperator(task_id='dummy_task_16')
    dummy_task_17 = DummyOperator(task_id='dummy_task_17')
    dummy_task_18 = DummyOperator(task_id='dummy_task_18')
    dummy_task_19 = DummyOperator(task_id='dummy_task_19')
    dummy_task_20 = DummyOperator(task_id='dummy_task_20')
    dummy_task_21 = DummyOperator(task_id='dummy_task_21')
    dummy_task_22 = DummyOperator(task_id='dummy_task_22')
    dummy_task_23 = DummyOperator(task_id='dummy_task_23')
    dummy_task_24 = DummyOperator(task_id='dummy_task_24')
    dummy_task_25 = DummyOperator(task_id='dummy_task_25')
    dummy_task_26 = DummyOperator(task_id='dummy_task_26')
    dummy_task_27 = DummyOperator(task_id='dummy_task_27')
    dummy_task_28 = DummyOperator(task_id='dummy_task_28')
    dummy_task_29 = DummyOperator(task_id='dummy_task_29')
    dummy_task_30 = DummyOperator(task_id='dummy_task_30')
    dummy_task_31 = DummyOperator(task_id='dummy_task_31')
    dummy_task_32 = DummyOperator(task_id='dummy_task_32')
    dummy_task_33 = DummyOperator(task_id='dummy_task_33')
    dummy_task_34 = DummyOperator(task_id='dummy_task_34')
    dummy_task_35 = DummyOperator(task_id='dummy_task_35')
    dummy_task_36 = DummyOperator(task_id='dummy_task_36')
    dummy_task_37 = DummyOperator(task_id='dummy_task_37')
    dummy_task_38 = DummyOperator(task_id='dummy_task_38')
    dummy_task_39 = DummyOperator(task_id='dummy_task_39')
    dummy_task_43 = DummyOperator(task_id='dummy_task_43')
    
    
    with TaskGroup(group_id='group_tasks', ui_color = "green",ui_fgcolor="black" ) as group_tasks:
        dummy_task_40 = DummyOperator(
            task_id="dummy_task_40"
        )
        
        dummy_task_41 = DummyOperator(
            task_id="dummy_task_41"
        ) 

        dummy_task_42 = DummyOperator(
            task_id="dummy_task_42"
        )
        
        dummy_task_40 >> dummy_task_41 >> dummy_task_42

    # Using bit-shift operators (<< and >>)
    dummy_task_1 >> dummy_task_2 >> dummy_task_3
    dummy_task_6 << dummy_task_5 << dummy_task_4

    #Using the set_upstream and set_downstream methods
    dummy_task_7.set_downstream(dummy_task_8)
    dummy_task_8.set_downstream(dummy_task_9)
    
    dummy_task_11.set_upstream(dummy_task_10)
    dummy_task_12.set_upstream(dummy_task_11)


    # Dependencies with lists
    dummy_task_13 >> dummy_task_14 >> [dummy_task_15, dummy_task_16]

    # Dependencies with tuples
    dummy_task_17 >> dummy_task_18 >> (dummy_task_19, dummy_task_20)
    
    #Using chain()
    chain(dummy_task_21, dummy_task_22, [dummy_task_23, dummy_task_24, dummy_task_25], [dummy_task_26, dummy_task_27, dummy_task_28], dummy_task_29)
    
    #Using chain_linear()
    chain_linear(dummy_task_30, dummy_task_31, [dummy_task_32, dummy_task_33, dummy_task_34], [dummy_task_35, dummy_task_36, dummy_task_37], dummy_task_38)

    #Using Task_groups
    dummy_task_39 >> group_tasks >> dummy_task_43