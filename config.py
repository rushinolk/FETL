import os
from dotenv import load_dotenv

load_dotenv()

GCP_CREDENCIAL= os.environ.get("BIGQUERY_CREDENCIAL")

FAKESTORE_URL = os.environ.get("FAKESTORE_API_URL")


# Configurações do Google Cloud Platform (GCP)
GCP_PROJECT_ID = "python-468018"
BIGQUERY_DATASET = "aulapython"
BIGQUERY_TABLE_NAME = "sales"

BIGQUERY_TABLE_ID = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}.{BIGQUERY_TABLE_NAME}"

