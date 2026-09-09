-- Query 1: Total sales by product
SELECT
    Product,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM transactions
GROUP BY Product
ORDER BY Total_Sales DESC;


-- Query 2: Top 10 customers by total spending
SELECT
    Customer_ID,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Spending
FROM transactions
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 10;


-- Query 3: Top 10 customers by transaction frequency
SELECT
    Customer_ID,
    COUNT(Transaction_ID) AS Transaction_Frequency
FROM transactions
GROUP BY Customer_ID
ORDER BY Transaction_Frequency DESC
LIMIT 10;


-- Query 4: Sales by product category
SELECT
    Product_Category,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM transactions
GROUP BY Product_Category
ORDER BY Total_Sales DESC;


-- Query 5: Sales by region
SELECT
    Region,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM transactions
GROUP BY Region
ORDER BY Total_Sales DESC;


-- Query 6: Average transaction value by payment method
SELECT
    Payment_Method,
    ROUND(AVG(Transaction_Amount), 2) AS Average_Transaction_Value,
    COUNT(Transaction_ID) AS Transaction_Count
FROM transactions
GROUP BY Payment_Method
ORDER BY Average_Transaction_Value DESC;


-- Query 7: Monthly sales trend
SELECT
    substr(Transaction_Date, 4, 7) AS Month,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM transactions
GROUP BY substr(Transaction_Date, 4, 7)
ORDER BY substr(Transaction_Date, 7, 4), substr(Transaction_Date, 4, 2);