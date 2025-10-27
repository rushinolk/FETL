import requests
import pandas as pd
from datetime import datetime
from pandas_gbq import to_gbq
import logging
import config

# Extract

def extract_products_data():
    logging.info("Iniciando a extração dos dados")
    api_url = config.FAKESTORE_URL
    try:
        # Requisição para pegar na API
        response = requests.get(api_url, timeout=10)

        # Salvar dados brutos 
        raw_data = response.json()
        logging.info(f"Extração bem sucedida {len(raw_data)} produtos encontrados.")
        return raw_data
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao extrair dados da API {e}")
        return None


# Transform

def transform_data(raw_data):

    # Tratamento de erro de carregamento de dados pela API
    if raw_data is None:
        logging.warning("Nenhum dado foi encontrado para tratamento")
        return None
    
    logging.info("Iniciando transformações dos dados")
    
    # Salvando dados em um dataframe
    df = pd.DataFrame(raw_data)

    # Dataframe com colunas selecionadas
    df_transformado = df[['id','title','price','category','rating']]

    # Dividindo coluna rating
    df_transformado['rating_rate'] = df_transformado['rating'].apply(lambda r: r.get('rate',0))
    df_transformado['rating_count'] = df_transformado['rating'].apply(lambda r: r.get('count',0))
    df_transformado = df_transformado.drop(columns='rating')

    # Renomeando colunas
    df_final = df_transformado.rename(columns={
        'id':'id_produto',
        'title': 'nome_produto',
        'price': 'preco',
        'category': 'categoria',
        'rating_rate': 'avaliacao',
        'rating_count': 'num avaliacao'
    })

    # Coluna com data e hora da última carga PADRÃO BIGQUERRY
    df_final['DataHoraCarga'] = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    

    return df_final

# Load

def load_data(df_final,project_id, table_id):

    # Tratamento de erro de carregamento de dados pela API
    if df_final is None:
        logging.warning("Nenhum dado foi encontrado para tratamento")
        return None
    
    logging.info(f'iniciando carregamento de dados para {table_id}')
    try:
        df_final.to_gbq(
            destination_table=table_id,
            project_id=project_id,
            if_exists='replace'  
        )
    except Exception as e:
        logging.error(f'Ocorreu um erro inesperado na carga. Detalhes: {e}')


# Start ETL

def run_pipeline(project_id, table_id):
    dados_brutos = extract_products_data()
    dados_transformados = transform_data(dados_brutos)
    load_data(dados_transformados,project_id,table_id)

    


