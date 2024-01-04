# traffic.py

from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.models.baseoperator import chain
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType
from airflow.operators.python import PythonOperator
import os
from google.cloud import storage
from google.oauth2 import service_account


@dag(
    start_date=datetime(2023, 7, 7),
    schedule=None,
    catchup=False,
    tags=['create_table'],
)
def create_table():
    create_traffic_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_youtube_dataset',
        dataset_id='youtube',
        gcp_conn_id='gcp',
    )
    gcs_to_raw_cities = aql.load_file(
        task_id='gcs_to_raw_cities',
        input_file=File(
            'gs://airflow-tut/raw/cities.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name='raw_cities',
            conn_id='gcp',
            metadata=Metadata(schema='youtube')
        ),
        use_native_support=True,
    )

    gcs_to_raw_total = aql.load_file(
        task_id='gcs_to_raw_total',
        input_file=File(
            'gs://airflow-tut/raw/total_traffic.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name='raw_total',
            conn_id='gcp',
            metadata=Metadata(schema='youtube')
        ),
        use_native_support=True,
    )
    gcs_to_raw_viewer = aql.load_file(
        task_id='gcs_to_raw_viewer',
        input_file=File(
            'gs://airflow-tut/raw/viewer_gender.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name='raw_gender',
            conn_id='gcp',
            metadata=Metadata(schema='youtube')
        ),
        use_native_support=True,
    )
    # @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    # def check_load(scan_name='check_load', checks_subpath='sources'):
    #     from include.soda.check_function import check
    #     return check(scan_name, checks_subpath)
    # check_load()


create_table()
