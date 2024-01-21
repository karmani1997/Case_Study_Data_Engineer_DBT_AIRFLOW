Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](https://getdbt.com/community) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

sed -i 's|^dags_folder.*$|dags_folder = /home/mehtab/github/Case_Study_Data_Engineer_LichtBlick/dags|' /home/mehtab/airflow/a
irflow.cfg

airflow scheduler
airflow webserver -p 8080
airflow users create     --username admin     --firstname Mehtab     --lastname Meghwar     --role Admin     --email mehtab.karmani@gmail.com
airflow db init
ip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"