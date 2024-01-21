# data_pipeline_dag.py
import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from extractor import extractor, move_files

# default_args = {
#     'start_date': datetime(2024, 1, 21),
# }

seed_folder = "../seeds"
processed_folder = "../logs/processed_files"
#common_prefix = datetime.today().strftime('%Y%m%d') + "22"
src_folder = "../src_data"
logs_folder = "../logs/raw_files"
script_directory = os.path.dirname(os.path.abspath(__file__))
src_folder = os.path.join(script_directory, src_folder)
logs_folder = os.path.join(script_directory, logs_folder)
processed_folder = os.path.join(script_directory, processed_folder)
seed_folder = os.path.join(script_directory, seed_folder)


#common_prefix = datetime.today().strftime("%Y%m%d") #+ "22"
common_prefix = "20201001"




# Define default_args and DAG
default_args = {
    'owner': 'Mehtab Meghwar',
    'start_date': datetime(2024, 1, 1, 23, 0, 0),  # January 1st, 2024, at 11:00 PM
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='A DAG that runs every month on the 1st date at 11:00 PM',
    schedule_interval='@monthly',  # Monthly schedule
)



#dag = DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily')

# def hello_function():
#     # Your Python code here
#     print("airflow is running")

extractor_op_args = [src_folder, seed_folder, logs_folder, common_prefix]

extractor_task = PythonOperator(
    task_id='extractor_task',
    python_callable=extractor,
    op_args=extractor_op_args,
    dag=dag,
)



dbt_build = BashOperator(
    task_id='dbt_build',
    bash_command='dbt build',
    dag=dag,
)

file_mover_op_args = [seed_folder, processed_folder, common_prefix]

files_mover_task = PythonOperator(
    task_id='files_mover_task',
    python_callable=move_files,
    op_args=file_mover_op_args,
    dag=dag,
)


extractor_task >> dbt_build >> files_mover_task
