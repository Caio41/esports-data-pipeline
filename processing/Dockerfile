FROM apache/spark:3.5.8

ARG AIRFLOW_UID=50000

USER root

RUN useradd --uid ${AIRFLOW_UID} --gid 0 --no-log-init -o airflow

RUN mkdir -p /opt/spark/work && chown -R airflow:0 /opt/spark/work

USER airflow
