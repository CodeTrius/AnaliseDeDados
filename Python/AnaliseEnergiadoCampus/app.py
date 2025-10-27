import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

COEFICIENTE = 0.003774
INTERCEPTO = 17.0673 # Valor estimado a partir dos dados do modelo anterior

# 1. Carregar os dados limpos
# Certifique-se de que o arquivo 'dados_analise_ia.csv' está no mesmo diretório do seu script.
df = pd.read_csv('dados_analise_ia.csv')

# Converter a coluna de data para datetime (útil para visualização e séries temporais)
df['Data_Diaria'] = pd.to_datetime(df['Data_Diaria'])

# 2. Preparação dos Dados para a IA
# Variável de Entrada (Feature): Irradiação GHI (a principal)
# O GHI é o recurso solar que se correlaciona com a produção.
X = df[['GHI_Irradiacao_Wh_m2_dia']]

# Variável de Saída (Target): Energia Produzida (o que queremos prever)
y = df['Energia_kWh']

# Dividir em conjuntos de Treinamento e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Treinar o Modelo de Regressão Linear
modelo_ia = LinearRegression()
modelo_ia.fit(X_train, y_train)

# 4. Avaliar o Modelo
y_pred = modelo_ia.predict(X_test)

# Métricas de Performance
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("-" * 30)
print("Análise de Eficiência (Modelo de IA)")
print(f"Coeficiente Angular (Slope): {modelo_ia.coef_[0]:.4f}")
print(f"Intercepto (Bias): {modelo_ia.intercept_:.4f}")
print("-" * 30)
print(f"Erro Médio Absoluto (MAE): {mae:.2f} kWh")
print(f"Coeficiente de Determinação (R2 Score): {r2:.4f}")
print("-" * 30)

# 5. Visualização (Salvar para PyCharm)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Reais (kWh)')
plt.plot(X, modelo_ia.predict(X), color='red', linewidth=2, label='Modelo de Regressão (IA)')
plt.title('Produção de Energia vs. Irradiação Solar (GHI)')
plt.xlabel('Irradiação Horizontal Global (GHI) - Wh/m²')
plt.ylabel('Energia Produzida (kWh)')
plt.legend()
plt.grid(True)
plt.show() # Em PyCharm, esta linha abrirá a janela do gráfico
# Se você quiser salvar o gráfico em vez de mostrar, use:
# plt.savefig('regressao_ia.png')
# plt.close()

media_eficiencia = df['Energia_kWh_por_kWp'].mean()

plt.figure(figsize=(12, 6))
plt.bar(df['Data_Diaria'], df['Energia_kWh_por_kWp'], width=0.8, color='skyblue')
plt.axhline(media_eficiencia, color='red', linestyle='--', label=f'Média de Fevereiro: {media_eficiencia:.3f} kWh/kWp')
plt.title('Eficiência Diária (kWh/kWp) em Fevereiro')
plt.xlabel('Data')
plt.ylabel('kWh/kWp')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

print(f"\nEficiência Média (kWh/kWp) em Fevereiro: {media_eficiencia:.3f}")

# 2. Calcular a Produção Prevista (o que o sistema "deveria" produzir)
df['Producao_Prevista_kWh'] = (df['GHI_Irradiacao_Wh_m2_dia'] * COEFICIENTE) + INTERCEPTO

# 3. Calcular a Anomalia de Eficiência
# Anomalia: (Produção Real - Produção Prevista)
# Um valor positivo alto indica que o sistema foi mais eficiente que a média.
# Um valor negativo alto indica baixa eficiência (possível problema).
df['Anomalia_Eficiencia_kWh'] = df['Energia_kWh'] - df['Producao_Prevista_kWh']

# 4. Análise dos Extremos (Piores e Melhores Dias)
df_anomalia = df[['Data_Diaria', 'Energia_kWh', 'Producao_Prevista_kWh', 'Anomalia_Eficiencia_kWh']].copy()
df_anomalia = df_anomalia.sort_values(by='Anomalia_Eficiencia_kWh', ascending=True)

print("--- Análise de Anomalias de Eficiência (Fevereiro) ---")
print("\nTop 5 Piores Dias (Anomalia Negativa - Baixa Eficiência):")
# Estes são os dias onde a produção real ficou muito abaixo do que o GHI indicava
print(df_anomalia.head(5).to_string(index=False))

print("\nTop 5 Melhores Dias (Anomalia Positiva - Alta Eficiência):")
# Estes são os dias onde a produção real superou a média indicada pelo GHI
print(df_anomalia.tail(5).sort_values(by='Anomalia_Eficiencia_kWh', ascending=False).to_string(index=False))


COEFICIENTE = 0.003774
INTERCEPTO = 17.0673

# 1. Carregar o arquivo mesclado
df = pd.read_csv('dados_analise_ia.csv')
df['Data_Diaria'] = pd.to_datetime(df['Data_Diaria']).dt.date

# Recalcular as métricas para o gráfico
df['Producao_Prevista_kWh'] = (df['GHI_Irradiacao_Wh_m2_dia'] * COEFICIENTE) + INTERCEPTO
df['Anomalia_Eficiencia_kWh'] = df['Energia_kWh'] - df['Producao_Prevista_kWh']

# 2. Visualização das Anomalias
plt.figure(figsize=(12, 6))
anomalias = df['Anomalia_Eficiencia_kWh']
cores = ['red' if anomalia < 0 else 'green' for anomalia in anomalias]

plt.bar(df['Data_Diaria'], anomalias, color=cores)
plt.axhline(0, color='black', linewidth=0.8) # Linha zero
plt.title('Anomalia de Eficiência Diária: Desvio em kWh (Fevereiro)')
plt.xlabel('Data')
plt.ylabel('Anomalia (Produção Real - Produção Prevista) [kWh]')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# 3. Análise do Clima nos Dias de Anomalia
df_anomalia = df.sort_values(by='Anomalia_Eficiencia_kWh', ascending=True)

# 5 Piores e 5 Melhores Dias
piores_dias = df_anomalia.head(5)
melhores_dias = df_anomalia.tail(5)

print("\n--- Análise das Condições Climáticas nos Dias Extremos ---")
print("\nTop 5 Piores Dias (Onde o sistema falhou):")
print(piores_dias[['Data_Diaria', 'Anomalia_Eficiencia_kWh',
                   'GHI_Irradiacao_Wh_m2_dia', 'Temperatura_Media_C', 'Velocidade_Vento_Media_ms']].to_string(index=False))

print("\nTop 5 Melhores Dias (Onde o sistema superou o esperado):")
print(melhores_dias[['Data_Diaria', 'Anomalia_Eficiencia_kWh',
                    'GHI_Irradiacao_Wh_m2_dia', 'Temperatura_Media_C', 'Velocidade_Vento_Media_ms']].sort_values(by='Anomalia_Eficiencia_kWh', ascending=False).to_string(index=False))

