import pandas as pd
from sqlalchemy import create_engine

# Conecta ao banco (será criado como 'marketing.db')
engine = create_engine('sqlite:///marketing.db')

# Carrega os dados
df_historico = pd.read_csv('dados/historico_campanhas.csv')

# Salva dados como tabelas no banco SQL
df_historico.to_sql('historico_campanhas', engine, index=False, if_exists='replace')

print("Banco de dados 'marketing.db' criado com sucesso!")