from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='esports_spark_etl',
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
) as dag:

    run_spark_etl = BashOperator(
        task_id='run_spark_etl',
        bash_command='python /opt/airflow/etl/spark_jobs.py /opt/airflow/data/raw/2026_LoL_esports_match_data_from_OraclesElixir.csv /opt/airflow/data/processed'
    )

    run_spark_etl
