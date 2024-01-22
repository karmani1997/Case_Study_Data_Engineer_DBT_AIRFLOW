# ETL Pipeline for Monthly Data

## Overview

This ETL pipeline automates the extraction, transformation, and loading (ETL) process of monthly data into a Data Warehouse (DWH). The pipeline is implemented using Python, DBT, and Apache Airflow.

## Directory Structure

- **/src_data:** Contains monthly data export files following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.
- **/models:** DBT models for data transformations.
- **/dags:** Apache Airflow DAGs & python scripts for orchestrating the ETL workflow.
- **/seed:** Clean data for loading into DWH using dbt.
- **/macro:** To load the default schema.

## Setup

1. **Clone the repository:** 
   git clone https://github.com/karmani1997/Case_Study_Data_Engineer_LichtBlick.git
2. Open terminal and navigate to the project.
3. Activate the virtual environment command: `source myenv/bin/activate`
4. Install Python dependencies: 
```
pip install --upgrade pip
pip install -r requirements.txt
```
5. Set up dbt profiles and connection details in `profiles.yml`.
6. Airflow Installation and Configuration.

* Install Apache Airflow with Celery Executor:
``` 
pip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
```
* Initialize the airflow database
```
airflow db init
```
* Create Airflow User
```
airflow users create \
    --username admin \
    --firstname <first_name> \
    --lastname <last_name> \
    --role Admin \
    --email <email>
```
* Setup Dags Path

```
sed -i 's|^dags_folder.*$|dags_folder = /home/mehtab/github/Case_Study_Data_Engineer_LichtBlick/dags|' /home/mehtab/airflow/a
irflow.cfg
```
* Start Airflow Webserver
```
airflow webserver -p 8080
```
* Start Airflow Scheduler
```
airflow scheduler
```

## ETL Process

### Extraction

- Data exports are expected to be available in the `/src_data` directory with filenames following the naming convention `yyyymmddhhmmss_TABLENAME.csv`.

### Transformation

- Python scripts in `/dags/extractor.py` perform initial data transformations.
- dbt models in `/dbt_models` handle additional transformations and CDM historization.

### Loading

- Airflow DAGs in `etl_pipeline` schedule and orchestrate the ETL process.
- Airflow tasks include:
  - Data extraction using Python scripts.
  - Running dbt transformations.
  - Loading data into the Data Warehouse.

## Usage

1. Start Apache Airflow: `airflow webserver -p 8080` and `airflow scheduler`.
2. Access the Airflow web UI: [http://localhost:8080](http://localhost:8080).
3. Trigger the appropriate DAG to run the ETL process.

## Data Analysis

After the ETL process, answers of the questions given below & sql queries on cdm historization tables are available here `analyses/result_queries.sql`:

1. **How did the average revenue (base price + consumption * energy price , Grundpreis +
Verbrauch * Arbeitspreis) per contract develop between 01.10.2020 and 01.01.2021?**
- Average revenue per contract between October 1, 2020, and January 1, 2021 is based on the sum of two components for each contract:
    - Base Price Component (Grundpreis):
        For each contract, if the PRICECOMPONENTID is 1, the corresponding PRICE is added to the total.
    - Consumption * Energy Price Component (Verbrauch * Arbeitspreis):

        For each contract, if the PRICECOMPONENTID is 2, the product of the contract's USAGE and the PRICE divided by 100 to convert the cents to euros is added to the total.
- The average revenue is then calculated by summing up these two components and dividing by the total number of contracts.

- Result: datasheet available in the `analyses/answer_1.csv` file.

2. **How many contracts were on delivery on 01.01.2021?**
   - Answer: Zero.

3. **How many new contract were loaded into the DWH on 01.12.2020?**
   - Answer: 1720.

## Improvements
1. Add more test cases using dbt_utils packages