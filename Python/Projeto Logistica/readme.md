# Projeto de Portfólio: Otimização de Custos Logísticos (SQL + PuLP)

## 1. O Problema de Negócio

O objetivo deste projeto é determinar o plano de distribuição de produtos que **minimiza o custo total de frete** para uma rede de logística.

Temos 3 Centros de Distribuição (CDs) que precisam atender 5 Regiões. Precisamos decidir quanto enviar de cada CD para cada Região, respeitando duas restrições principais:

1.  A capacidade de envio de cada CD não pode ser excedida.
2.  A demanda total de cada Região deve ser 100% atendida.

## 2. Metodologia e Ferramentas

O projeto foi dividido em três etapas principais:

1.  **Engenharia de Dados (SQL):** Os dados de capacidade, demanda e custos foram criados e armazenados em um banco de dados **SQLite**.
2.  **Análise de Dados (Python + Pandas):** Os dados foram extraídos do SQL para o Python usando `Pandas` e `SQLAlchemy`. Em seguida, foram tratados e transformados em dicionários para alimentar o modelo.
3.  **Otimização (Python + PuLP):** Foi construído um modelo de **Programação Linear** com a biblioteca `PuLP` para encontrar a solução ótima que minimiza a função de custo total.

## 3. Resultados: A Solução Ótima

Após executar o otimizador, a solução ótima foi encontrada:

```
Status da Solução: Optimal
Custo Total Ótimo = R$ 7100.00

--- Plano de Envio (Unidades) ---
Enviar de CD1 para R1: 300.0 unidades
Enviar de CD1 para R2: 700.0 unidades
Enviar de CD2 para R3: 500.0 unidades
Enviar de CD2 para R4: 300.0 unidades
Enviar de CD3 para R1: 100.0 unidades
Enviar de CD3 para R5: 600.0 unidades

--- Utilização da Capacidade ---
CD1: Usado 1000.
## (Próximos Passos - Opcional)

Para uma V2 deste pr0 / 1000 (Capacidade)
CD2: Usado 800.0 / 800 (Capacidade)
CD3: Usado 700.0 / 700 (Capacidade)
```

## 4. Conclusão e Insights

* A solução encontrada gera um custo mínimo de **R$ 7100.00** e fornece o plano de ação exato para a equipe de logística.
* **Insight Chave:** O sistema opera com 100% de utilização da capacidade em todos os CDs. Isso indica que a demanda total é exatamente igual à capacidade total da rede, não havendo folga para picos de demanda.

ojeto, a etapa de **Estatística** seria aprimorada. Em vez de usar uma demanda fixa, poderíamos usar dados históricos de vendas e aplicar uma **previsão de séries temporais** (como ARIMA ou Prophet) para estimar a demanda futura, tornando o modelo preditivo.

<img width="1331" height="332" alt="image" src="https://github.com/user-attachments/assets/fceaf163-75fc-4726-9ab5-bc49cd5364de" />

<img width="689" height="124" alt="image" src="https://github.com/user-attachments/assets/1e425a7d-fc16-4f9f-9919-3e7f78362395" />

<img width="710" height="373" alt="image" src="https://github.com/user-attachments/assets/cd1402f1-ac32-4c16-a6f7-fe81481eaad2" />

<img width="423" height="617" alt="image" src="https://github.com/user-attachments/assets/2e03cb19-0d1d-495a-82de-b3734080bf8e" />

<img width="1305" height="637" alt="image" src="https://github.com/user-attachments/assets/808b6e59-6957-489a-912e-f7f285be50c4" />

<img width="709" height="236" alt="image" src="https://github.com/user-attachments/assets/09e8bd5b-d07f-474a-ad02-add7f5829199" />
<img width="897" height="520" alt="image" src="https://github.com/user-attachments/assets/06cbed5b-81b0-42c9-a25d-d1cdc7cad250" />
<img width="712" height="733" alt="image" src="https://github.com/user-attachments/assets/5202edae-21ed-4b25-973e-3a8a555d1b8c" />








