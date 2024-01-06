import json
from google.cloud import bigquery


def get_database_info(dataset_id="youtube"):
    client = bigquery.Client.from_service_account_json(
        "service_account.json")
    database_schema_dict = get_database_schema(client, dataset_id)
    database_schema_string = "\n".join(
        [
            f"Table: {table['table_name']}\nColumns: {', '.join(table['column_names'])}"
            for table in database_schema_dict
        ]
    )
    return database_schema_string


def get_database_schema(client, dataset_id):
    table_dicts = []
    for table_name in get_table_names(client, dataset_id):
        column_names = get_column_names(client, dataset_id, table_name)
        table_dicts.append(
            {"table_name": table_name, "column_names": column_names})
    return table_dicts


def get_table_names(client, dataset_id):
    """Return a list of table names in the specified dataset."""
    table_names = []
    dataset_ref = client.dataset(dataset_id)
    # List tables in the dataset
    tables = client.list_tables(dataset_ref)
    for table in tables:
        table_names.append(table.table_id)
    return table_names


def get_column_names(client, dataset_id, table_name):
    """Return a list of column names for the specified table."""
    column_names = []
    table_ref = client.dataset(dataset_id).table(table_name)
    table = client.get_table(table_ref)
    for field in table.schema:
        column_names.append(field.name)
    return column_names


def get_database_info(client, dataset_id):
    """Return a list of dicts containing the table name and columns for each table in the dataset."""
    table_dicts = []
    for table_name in get_table_names(client, dataset_id):
        column_names = get_column_names(client, dataset_id, table_name)
        table_dicts.append(
            {"table_name": table_name, "column_names": column_names})
    return table_dicts


def ask_database(client, query):
    """Function to query BigQuery dataset with a provided SQL query."""
    try:
        query_job = client.query(query)
        results = query_job.result()
        rows = [row.values() for row in results]
    except Exception as e:
        results = f"query failed with error: {e}"
        rows = []
    return rows


def execute_function_call(message, client):
    if message["tool_calls"][0]["function"]["name"] == "ask_database":
        query = json.loads(message["tool_calls"][0]
                           ["function"]["arguments"])["query"]
        results = ask_database(client, query)
    else:
        results = f"Error: function {message['tool_calls'][0]['function']['name']} does not exist"
    return results
