import pandas as pd
from sqlalchemy import create_engine, text, exc
from dotenv import load_dotenv
import os

#Importando planilhas
df_milho = pd.read_excel('Grao.xlsx', sheet_name="Milho")
df_soja = pd.read_excel('Grao.xlsx', sheet_name="Soja")

#Preencher os valores nulos com base no ultimo valor não nulo
df_milho.fillna(method='ffill', inplace=True)
df_soja.fillna(method='ffill', inplace=True)

# Carrega as variáveis do arquivo .env
load_dotenv()
      
# atribui as variaveis do aquivo
host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
database=os.getenv("DB_DATABASE")

#cria a conexao
engine = create_engine(fr'mysql+pymysql://{user}:{password}@{host}/{database}')

#Insere os dados do df_milho na tabela tb_milho no Mysql 
try:
    result = df_milho.to_sql('tb_milho', engine, if_exists='append', index=False )
    print(f'{result} linhas inseridas em tb_milho')

    result = df_soja.to_sql('tb_soja', engine, if_exists='append', index=False )
    print(f'{result} linhas inseridas em tb_soja')
except exc.SQLAlchemyError as error:
    print(f'Erro ao conectar ao banco de dados: {error}')

# Conferindo os dados inseridos no DB
try:
    with engine.connect() as conn:
        tb_milho = conn.execute(text("SELECT * FROM tb_milho")).fetchall()
        tb_soja = conn.execute(text("SELECT * FROM tb_soja")).fetchall()
        print('registros em tb_milho:', len(tb_milho))
        print('registros em tb_soja:', len(tb_soja))
except exc.SQLAlchemyError as error:
    print(f'Erro ao conectar ao banco de dados: {error}')


