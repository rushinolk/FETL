# src/main.py
import os
from .etl_pipeline import run_pipeline
import config

if __name__ == "__main__":

    credential_path = "credentials/gcp_service_account.json"
    
    # Variável de ambiente com credencial GBQ.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
    
    print("======================================================")
    print("==  Iniciando o pipeline de ETL de produtos ==")
    print(f"== Credencial sendo usada: {credential_path} ==")
    print("======================================================")

    # Start no pipeline com configuração de credencial GBQ.
    try:
        run_pipeline( project_id=config.GCP_PROJECT_ID, 
                    table_id=config.BIGQUERY_TABLE_ID  )
    except Exception as e:
        print(f"\nERRO CRÍTICO NO PIPELINE: Ocorreu um erro inesperado: {e}")
        

    print("\n======================================================")
    print("==  Pipeline de ETL concluído!              ==")
    print("== Verifique sua tabela no BigQuery.              ==")
    print("======================================================")