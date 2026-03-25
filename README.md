# LoL Esports Data Engineering Pipeline

This project builds a data pipeline for professional League of Legends match data, using Apache Spark to transform raw CSV files into analytics-ready Parquet datasets. The pipeline is orchestrated with Airflow, and DuckDB is used to query the data, powering an interactive Streamlit dashboard for exploring teams, players, champions, and leagues.


## Architecture

The pipeline follows a modern data engineering architecture, leveraging containerization for reproducibility and scalability.

1.  **Data Ingestion**: Raw match data (in `.csv` format) from sources like [Oracle's Elixir](https://oracleselixir.com/) is placed in the `data/raw` directory.
2.  **Orchestration**: **Apache Airflow** orchestrates the entire ETL process, scheduling and triggering the data processing job at defined intervals.
3.  **Processing**: An **Apache Spark** job, running in a cluster with a Master and Worker, reads the raw data and performs cleaning and transformations, generating analytics-ready datasets.
4.  **Storage**: The transformed data is stored as **Parquet files** in the `data/processed` directory, enabling efficient columnar storage and fast analytical access.
5.  **Visualization**: A **Streamlit** dashboard uses **DuckDB** to run analytical queries directly on the Parquet datasets, providing insights on champions, players, teams, and leagues.

## Tech Stack

| Category          | Technology                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Orchestration** | ![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white) |
| **Processing**    | ![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)     |
| **Query Engine**      | ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)         |
| **Dashboard**     | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)   |
| **Language**      | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)         |
| **Containerization**| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)           |

## Getting Started

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Caio41/esports-data-pipeline.git
    cd esports-data-pipeline
    ```

2.  **Create Environment File:**
    Create a `.env` file to configure your local user ID for Airflow (required to avoid permission issues when running containers).
    ```bash
    echo "AIRFLOW_UID=$(id -u)" > .env
    ```
    Alternatively, you can copy the example file:

    ```bash
    cp .env.example .env
    ```

3.  **Build and run the services:**
    From the root of the project directory, run the following command to build the images and start all services in the background.
    ```bash
    docker-compose up --build
    ```
    > **Note:** Once the services are up, the Airflow scheduler will automatically trigger the ETL DAG based on its schedule configuration. No manual intervention is required to start the pipeline.

### Accessing the Services

Once the containers are running, you can access the different components of the pipeline:

*   **Airflow Web UI**: [http://localhost:8080](http://localhost:8080)
    *   **Username**: `airflow`
    *   **Password**: `airflow`

*   **Streamlit Dashboard**: [http://localhost:8501](http://localhost:8501)

*   **Spark Master UI**: [http://localhost:9090](http://localhost:9090)

## Project Structure

```
esports-data-pipeline/
├── dashboard/         # Contains the Streamlit dashboard application
├── data/
│   ├── processed/     # Output directory for processed data (.parquet files)
│   └── raw/           # Input directory for raw CSV data
├── orchestration/
│   └── dags/          # Airflow DAGs to define the ETL workflow
├── processing/
│   └── etl/           # PySpark ETL scripts for data transformation
├── docker-compose.yaml  # Defines all services, networks, and volumes
└── README.md
```
