from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
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

    run_spark_etl = SparkSubmitOperator(
        task_id='run_spark_etl',
        application='/opt/airflow/etl/spark_jobs.py',
        conf={
            'spark.master': 'spark://spark-master:7077',
            'spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version': '2'
        },
        application_args=[
            output_file,
            "/opt/airflow/data/processed"
        ]
    )

    ingest_data >> run_spark_etl
