-- "SELECTs" que usaríamos para buscar os dados brutos
CREATE VIEW vw_Fato_Vendas AS
SELECT
    SalesOrderNumber, -- Código do Pedido
    OrderDate,        -- Data do Pedido
    ProductKey,       -- Chave do Produto (para ligar na dProduto)
    CustomerKey,      -- Chave do Cliente (para ligar na dCliente)
    TerritoryKey,     -- Chave do Território (para ligar na dRegiao)
    SalesAmount,      -- Valor da Venda
    TotalProductCost, -- Custo do Produto
    OrderQuantity     -- Quantidade
FROM FactInternetSales
WHERE OrderDate >= '2023-01-01'; -- Filtramos só dados recentes