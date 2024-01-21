# ETL Pipeline for Monthly Data Exports

## Overview

This ETL pipeline automates the extraction, transformation, and loading (ETL) process of monthly data exports into a Data Warehouse (DWH). The pipeline is implemented using Python, dbt, and Apache Airflow.

## Directory Structure

- **/data_exports:** Contains monthly data export files following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.
- **/etl_scripts:** Python scripts for ETL processes.
- **/dbt_models:** dbt models for data transformations.
- **/airflow_dags:** Apache Airflow DAGs for orchestrating the ETL workflow.

## Requirements

- Python 3.x
- dbt
- Apache Airflow

## Setup

1. Clone the repository: `git clone https://github.com/yourusername/etl-pipeline.git`
2. Install Python dependencies: `pip install -r requirements.txt`
3. Set up dbt profiles and connection details in `profiles.yml`.
4. Configure Apache Airflow by adding DAGs to the `airflow_dags` directory.

## ETL Process

### Extraction

- Data exports are expected to be available in the `/data_exports` directory with filenames following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.

### Transformation

- Python scripts in `/etl_scripts` perform initial data transformations.
- dbt models in `/dbt_models` handle additional transformations and historization.

### Loading

- Airflow DAGs in `/airflow_dags` schedule and orchestrate the ETL process.
- Airflow tasks include:
  - Data extraction using Python scripts.
  - Running dbt transformations.
  - Loading data into the Data Warehouse.

## Usage

1. Start Apache Airflow: `airflow webserver -p 8080` and `airflow scheduler`.
2. Access the Airflow web UI: `http://localhost:8080`.
3. Trigger the appropriate DAG to run the ETL process.

## Data Analysis

After the ETL process, you can answer the specified questions:

1. Use dbt to query the Data Warehouse for the average revenue per contract between 01.10.2020 and 01.01.2021.
2. Query the Data Warehouse to find the number of contracts on delivery on 01.01.2021.
3. Check the logs or dbt run results to determine how many new contracts were loaded on 01.12.2020.

## Contributors

- [Your Name]
- [Other Contributors]

## License

This project is licensed under the [MIT License](LICENSE).


sed -i 's|^dags_folder.*$|dags_folder = /home/mehtab/github/Case_Study_Data_Engineer_LichtBlick/dags|' /home/mehtab/airflow/a
irflow.cfg

airflow scheduler
airflow webserver -p 8080
airflow users create     --username admin     --firstname Mehtab     --lastname Meghwar     --role Admin     --email mehtab.karmani@gmail.com
airflow db init
ip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"