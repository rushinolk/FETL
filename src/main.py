# src/main.py
import os
from .etl_pipeline import run_pipeline
import config
import logging

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato da mensagem
    datefmt='%Y-%m-%d %H:%M:%S', # Formato da data
    handlers=[
        logging.FileHandler("pipeline.log"), # Salva o log em um arquivo
        logging.StreamHandler()            # Também exibe o log no console
    ]
)

if __name__ == "__main__":
    
    # Variável de ambiente com credencial GBQ.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.GCP_CREDENCIAL
    
    logging.info("======================================================")
    logging.info("==  Iniciando o pipeline de ETL de produtos ==")
    logging.info("== Credencial sendo usada ==")
    logging.info("======================================================")

    # Start no pipeline com configuração de credencial GBQ.
    try:
        run_pipeline( project_id=config.GCP_PROJECT_ID, 
                    table_id=config.BIGQUERY_TABLE_ID  )
    except Exception as e:
        logging.error(f"\nERRO CRÍTICO NO PIPELINE: Ocorreu um erro inesperado: {e}")
        

    logging.info("\n======================================================")
    logging.info("==  Pipeline de ETL concluído!              ==")
    logging.info("== Verifique sua tabela no BigQuery.              ==")
    logging.info("======================================================")