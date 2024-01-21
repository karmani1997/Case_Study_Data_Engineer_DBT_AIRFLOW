# data_pipeline_dag.py

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from extractor import extractor, move_files

default_args = {
    'start_date': datetime(2024, 1, 21),
}

dag = DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily')

def hello_function():
    # Your Python code here
    print("airflow is running")

python_task = PythonOperator(
    task_id='run_python_script',
    python_callable=hello_function,
    dag=dag,
)

dbt_run = BashOperator(
    task_id='run_dbt_models',
    bash_command='dbt build',
    dag=dag,
)

python_task #>> dbt_run
