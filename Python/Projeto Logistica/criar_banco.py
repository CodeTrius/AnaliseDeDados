import pandas as pd
from sqlalchemy import create_engine

# Conecta ao banco (ele será criado se não existir)
engine = create_engine('sqlite:///logistica.db')

# Carrega os dados
df_centros = pd.read_csv('dados/centros.csv')
df_demandas = pd.read_csv('dados/demandas.csv')
df_custos = pd.read_csv('dados/custos.csv')

# Salva dados como tabelas no banco SQL
df_centros.to_sql('centros', engine, index=False, if_exists='replace')
df_demandas.to_sql('demandas', engine, index=False, if_exists='replace')
df_custos.to_sql('custos', engine, index=False, if_exists='replace')

print("Banco de dados 'logistica.db' criado com sucesso!")