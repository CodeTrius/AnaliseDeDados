import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# --- 1. DEFINIÇÕES ---
FATOR_CONVERSAO_GHI = 0.5 # 30 minutos em horas
df_producao_filename = 'producao.csv'
df_nsrdb_filename = 'nsrdb_2024.csv'

# --- 2. PREPARAÇÃO DOS DADOS DE PRODUÇÃO ---
df_producao = pd.read_csv(df_producao_filename, skiprows=3, header=None)
df_producao.columns = ['Data', 'Energia_kWh', 'Energia_kWh_por_kWp', 'Instalacao_Total_kWh', 'Extra_col']
df_producao = df_producao.drop(columns=['Extra_col']).dropna(subset=['Data']).copy()
# Conversão de tipo de dados e formatação de data
for col in ['Energia_kWh', 'Energia_kWh_por_kWp', 'Instalacao_Total_kWh']:
    df_producao[col] = pd.to_numeric(df_producao[col].astype(str).str.replace(',', '.', regex=False).str.strip(), errors='coerce')
df_producao['Data_Diaria'] = pd.to_datetime(df_producao['Data'], format='%d.%m.%Y', errors='coerce').dt.normalize()
df_producao = df_producao.dropna(subset=['Data_Diaria']).copy()


# --- 3. PREPARAÇÃO DOS DADOS NSRDB (GHI) ---
df_nsrdb = pd.read_csv(df_nsrdb_filename, skiprows=[0, 2], header=0, engine='python')
# Atribuição dos nomes das colunas para acesso (baseado no formato NSRDB)
new_columns = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'DHI', 'DNI', 'GHI', 'Clearsky_DHI', 'Clearsky_DNI', 'Clearsky_GHI', 'Cloud_Type', 'Dew_Point', 'Solar_Zenith_Angle', 'Temperature', 'Pressure', 'Relative_Humidity', 'Wind_Direction', 'Wind_Speed', 'Wind_Gust']
if df_nsrdb.shape[1] >= len(new_columns):
    df_nsrdb.columns = new_columns + df_nsrdb.columns[len(new_columns):].tolist()
else:
    df_nsrdb.columns = new_columns[:df_nsrdb.shape[1]]

df_nsrdb['Data_Diaria'] = pd.to_datetime(
    df_nsrdb['Year'].astype(str) + '-' + df_nsrdb['Month'].astype(int).astype(str).str.zfill(2) + '-' + df_nsrdb['Day'].astype(int).astype(str).str.zfill(2)
)

# Agregação do GHI (Potência W/m²) para Irradiação (Energia Wh/m²)
df_nsrdb_daily = df_nsrdb.groupby('Data_Diaria')[['GHI']].sum() * FATOR_CONVERSAO_GHI
df_nsrdb_daily = df_nsrdb_daily.rename(columns={'GHI': 'GHI_Irradiacao_Wh_m2_dia'})
df_nsrdb_daily = df_nsrdb_daily.reset_index()

# --- 4. MERGE E TREINAMENTO ---
df_merged = pd.merge(df_producao, df_nsrdb_daily, on='Data_Diaria', how='inner')

# Variáveis para o modelo
X = df_merged[['GHI_Irradiacao_Wh_m2_dia']] # Variável de Entrada (GHI)
y = df_merged['Energia_kWh']                # Variável de Saída (Produção)

# Instanciar e Treinar o Modelo
model = LinearRegression()
model.fit(X, y)

# --- 5. RESULTADO ---
COEFICIENTE = model.coef_[0]
INTERCEPTO = model.intercept_

print("-" * 35)
print("RESULTADOS DO MODELO DE REGRESSÃO:")
print("-" * 35)
print(f"COEFICIENTE (Inclinação): {COEFICIENTE:.6f}")
print(f"INTERCEPTO (Constante): {INTERCEPTO:.4f}")
print("-" * 35)