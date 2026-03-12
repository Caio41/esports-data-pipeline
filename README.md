lol-data-platform
│
├── ingestion
│   └── download_matches.py
│
├── data
│   ├── raw
│   ├── processed
│   └── analytics
│
├── spark_jobs
│   └── transform_matches.py
│
├── airflow
│   └── dags
│       └── pipeline.py
│
├── warehouse
│   └── schema.sql
│
├── dashboards
│
├── docker-compose.yml
│
└── README.md


Ideia:
Criar um pipeline que coleta dados de partidas profissionais de League of Legends, processa e gera métricas analíticas.

Arquitetura:
API / scraping
     ↓
Airflow (orquestração)
     ↓
Raw layer (S3 / MinIO / local)
     ↓
Spark ETL
     ↓
Data Warehouse (Postgres / DuckDB)
     ↓
Dashboard / queries analíticas


Stack:
Apache Airflow → orquestração

Apache Spark (PySpark) → transformação

MinIO ou S3 → data lake

PostgreSQL ou DuckDB → data warehouse

Superset / Metabase → dashboards


usar java 17 no projeto:
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export PATH=$JAVA_HOME/bin:$PATH

