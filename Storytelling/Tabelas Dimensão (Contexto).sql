-- Para Produtos
CREATE VIEW vw_Dim_Produto AS
SELECT
    ProductKey,
    EnglishProductName AS ProdutoNome,
    (SELECT Name FROM DimProductSubcategory WHERE ProductSubcategoryKey = p.ProductSubcategoryKey) AS Subcategoria,
    (SELECT Name FROM DimProductCategory WHERE ProductCategoryKey = (SELECT ProductCategoryKey FROM DimProductSubcategory WHERE ProductSubcategoryKey = p.ProductSubcategoryKey)) AS Categoria
FROM DimProduct p;

-- Para Clientes
CREATE VIEW vw_Dim_Cliente AS
SELECT CustomerKey, FirstName + ' ' + LastName AS ClienteNome FROM DimCustomer;

-- Para Regiões
CREATE VIEW vw_Dim_Regiao AS
SELECT TerritoryKey, Name AS Regiao, CountryRegionCode AS Pais FROM DimSalesTerritory;