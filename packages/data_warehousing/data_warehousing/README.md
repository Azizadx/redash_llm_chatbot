Data Warehousing
========

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes two example DAGs:
    - `dag_check_gcp_connection`: This DAG check the gcp connection for the data pipeline 
    - `dag_to_create_bigquery_table`: This DAG converts the raw data into table schema and store it in bigquery.
    - `dag_upload_csv_to_gcs`: This DAG that uploads the CSV to the GCP bucket

- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. Also it contains the DBT install in env't
- include: This folder houses both data and GCP keys. Even if they're not present here, feel free to create yours during the installation process.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. 
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.
<img width="1269" alt="Screenshot 2024-01-08 at 7 25 26 PM" src="https://github.com/Azizadx/redash_llm_chatbot/assets/45791956/d77eed1f-b565-419c-863a-23911b930c83">





