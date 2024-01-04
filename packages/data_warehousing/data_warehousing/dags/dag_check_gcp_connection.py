from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
from google.cloud import storage
from google.oauth2 import service_account


def check_service_account_connection():
    service_account_path = '/usr/local/airflow/include/gcp/service_account.json'
    if not service_account_path:
        raise Exception(
            "Service account JSON file path not found in environment variables."
        )
    try:
        credentials = service_account.Credentials.from_service_account_file(
            "/usr/local/airflow/include/gcp/service_account.json"
        )
        storage_client = storage.Client(credentials=credentials)
        print("Connection using service account successful!")
    except Exception as e:
        print("Connection failed:", e)
        raise


@dag(
    start_date=datetime(2023, 7, 7),
    schedule=None,
    catchup=False,
    tags=['connection_gcp'],
)
def connection_gcp():
    check_connection = PythonOperator(
        task_id='check_connection',
        python_callable=check_service_account_connection
    )


connection_gcp()
