import json
from google.cloud import bigquery

client = bigquery.Client()
table_id = "your-project.mydataset.mytable_name"

# Load the schema file
with open("schema.json", "r") as f:
    schema_data = json.load(f)

# Convert dictionary objects into BigQuery SchemaField elements
schema = [bigquery.SchemaField.from_api_repr(field) for field in schema_data]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table) 
print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")
