from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='esports_spark_etl',
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
) as dag:

    output_file = '/opt/airflow/data/raw/{{ds}}-LoLEsportsMatchData.csv'

    ingest_data = BashOperator(
        task_id='ingest_data',
        bash_command=f'python /opt/airflow/etl/ingest.py {output_file}'
    )

    run_spark_etl = BashOperator(
        task_id='run_spark_etl',
        bash_command="python /opt/airflow/etl/spark_jobs.py {{task_instance.xcom_pull(task_ids='ingest_data')}} /opt/airflow/data/processed"
    )

    ingest_data >> run_spark_etl
