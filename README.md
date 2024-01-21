# ETL Pipeline for Monthly Data

## Overview

This ETL pipeline automates the extraction, transformation, and loading (ETL) process of monthly data into a Data Warehouse (DWH). The pipeline is implemented using Python, DBT, and Apache Airflow.

## Directory Structure

- **/src_data:** Contains monthly data export files following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.
- **/models:** DBT models for data transformations.
- **/dags:** Apache Airflow DAGs & python scripts for orchestrating the ETL workflow.
- **/seed:** Clean data for loading into DWH using dbt.
- **/macro:** To load the default schema.

## Requirements

- Python 3.x
- dbt
- Apache Airflow

## Setup

1. **Clone the repository:** 
   git clone https://github.com/karmani1997/Case_Study_Data_Engineer_LichtBlick.git
2. Open terminal and navigate to the project.
3. Activate the virtual environment command: `source myenv/bin/activate`
4. Install Python dependencies: `pip install -r requirements.txt`
5. Set up dbt profiles and connection details in `profiles.yml`.
6. Configure Apache Airflow.

* Install Apache Airflow:
` 
pip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
`

`
airflow db init
`
`
airflow users create     --username admin     --firstname Mehtab     --lastname Meghwar     --role Admin     --email email.com
`
* setup the dags path:
`sed -i 's|^dags_folder.*$|dags_folder = /home/mehtab/github/Case_Study_Data_Engineer_LichtBlick/dags|' /home/mehtab/airflow/a
irflow.cfg
`
`airflow webserver -p 8080`
`airflow scheduler`

# ETL Process

## Extraction

- Data exports are expected to be available in the `/src_data` directory with filenames following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.

## Transformation

- Python scripts in `/dags/extractor.py` perform initial data transformations.
- dbt models in `/dbt_models` handle additional transformations and CDM historization.

## Loading

- Airflow DAGs in `etl_pipeline` schedule and orchestrate the ETL process.
- Airflow tasks include:
  - Data extraction using Python scripts.
  - Running dbt transformations.
  - Loading data into the Data Warehouse.

# Usage

1. Start Apache Airflow: `airflow webserver -p 8080` and `airflow scheduler`.
2. Access the Airflow web UI: [http://localhost:8080](http://localhost:8080).
3. Trigger the appropriate DAG to run the ETL process.

# Data Analysis

After the ETL process, answers of the questions given below & queries are available in the `analyses/result_queries.sql`:

1. **Use dbt to query the Data Warehouse for the average revenue per contract between 01.10.2020 and 01.01.2021.**
   - Answer: Result available in the `analyses/answer_1.csv` file.

2. **Query the Data Warehouse to find the number of contracts on delivery on 01.01.2021.**
   - Answer: Zero.

3. **Check the logs or dbt run results to determine how many new contracts were loaded on 01.12.2020.**
   - Answer: 1720.
