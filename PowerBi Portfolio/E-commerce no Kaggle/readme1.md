Descrição do Projeto

Este projeto consiste em um dashboard analítico desenvolvido no Power BI para explorar os dados reais de e-commerce da Olist (famoso marketplace brasileiro).

O objetivo é transformar dados brutos de vendas em insights estratégicos, permitindo o monitoramento de KPIs de vendas, análise temporal (sazonalidade) e perfil de pedidos.
🎯 Problema de Negócio

O desafio principal foi unificar dados dispersos em múltiplos arquivos relacionais para responder a perguntas como:

    Qual o faturamento total e volume de pedidos ao longo do tempo?

    Existe sazonalidade nas vendas?

    Qual o Ticket Médio das operações?

    Quais categorias de produtos performam melhor?

🛠️ Tecnologias e Técnicas Utilizadas
Ferramentas

    Microsoft Power BI Desktop

    Power Query (Para ETL e limpeza de dados)

    DAX (Para análise e cálculos de negócio)

Metodologia Aplicada

    ETL (Extração, Transformação e Carga):

        Conexão com múltiplos arquivos CSV (Dataset Kaggle).

        Desafio Técnico: A tabela de itens (order_items) continha os valores, mas a tabela de pedidos (orders) continha as datas. Foi realizado um Merge (Mesclagem) avançado no Power Query para unificar Data e Valor na tabela Fato, otimizando a performance.

        Limpeza de dados: Tratamento de tipos de dados e remoção de carimbos de hora (timestamps) para granularidade diária.

    Modelagem de Dados (Star Schema):

        Construção de um modelo Star Schema (Esquema Estrela) para garantir performance e integridade.

        Criação da tabela Fato: fSales.

        Criação das tabelas Dimensão: dProducts, dCustomers, dSellers.

        Criação de uma tabela dCalendar via DAX para inteligência temporal.

    Análise DAX:

        Criação de medidas explícitas para KPIs: Total Vendas, Total Pedidos, Ticket Médio.

        Formatação de moedas e categorização de dados.

📊 Visualização (Screenshots)

<img width="1323" height="646" alt="image" src="https://github.com/user-attachments/assets/ec49fc6d-37df-454d-9102-b0b31a6849bc" />

Visão Geral dos KPIs e Tendência Temporal.




📂 Estrutura do Dataset

Os dados utilizados são públicos e estão disponíveis no Kaggle - Brazilian E-Commerce Public Dataset by Olist.

As principais tabelas utilizadas foram:

    olist_order_items_dataset.csv (Detalhes dos itens e preços)

    olist_orders_dataset.csv (Datas e status dos pedidos)

    olist_products_dataset.csv (Informações dos produtos)

🚀 Próximos Passos

    [ ] Implementar Tooltips para detalhamento ao passar o mouse.

    [ ] Adicionar análise geográfica (Mapa de vendas por Estado).

    [ ] Criar Menu de Navegação para diferentes visões (Vendas vs Logística).
