from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator


@dag(
    start_date=datetime(2023, 7, 7),
    schedule=None,
    catchup=False,
    tags=['csv_2_gcs'],

)
def csv_2_gcs():
    # Task to upload CSV to GCS
    upload_cities_data_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_cities_data_csv_to_gcs',
        src='include/data/Cities/cities.csv',
        dst='raw/cities.csv',
        bucket='airflow-tut',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )
    upload_total_views_data_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_total_views_data_csv_to_gcs',
        src='include/data/Cities/Totals.csv',
        dst='raw/total_traffic.csv',
        bucket='airflow-tut',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )
    upload_view_gender_data_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_view_gender_data_csv_to_gcs',
        src='include/data/Viewership by Date/viewer_date.csv',
        dst='raw/viewer_gender.csv',
        bucket='airflow-tut',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )


csv_2_gcs()
