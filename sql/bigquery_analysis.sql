
-- =====================================================
-- CUSTOMER SEGMENTATION & BEHAVIORAL ANALYSIS
-- BigQuery SQL Analysis
-- =====================================================


-- 1. Total Sales by Product
-- Business question: Which products generate the highest revenue?

SELECT
    Product,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Product
ORDER BY
    Total_Sales DESC;


-- =====================================================
-- 2. Top 10 Customers by Spending
-- Business question: Who are the highest-spending customers?

SELECT
    Customer_ID,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Spending
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Customer_ID
ORDER BY
    Total_Spending DESC
LIMIT 10;


-- =====================================================
-- 3. Top 10 Customers by Transaction Frequency
-- Business question: Which customers purchase most frequently?

SELECT
    Customer_ID,
    COUNT(Transaction_ID) AS Transaction_Frequency
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Customer_ID
ORDER BY
    Transaction_Frequency DESC
LIMIT 10;


-- =====================================================
-- 4. Sales by Product Category
-- Business question: Which product categories contribute most to revenue?

SELECT
    Product_Category,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Product_Category
ORDER BY
    Total_Sales DESC;


-- =====================================================
-- 5. Sales by Region
-- Business question: Which regions generate the highest revenue?

SELECT
    Region,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Region
ORDER BY
    Total_Sales DESC;


-- =====================================================
-- 6. Payment Method Analysis
-- Business question: How do transaction values and volumes vary by payment method?

SELECT
    Payment_Method,
    ROUND(AVG(Transaction_Amount), 2) AS Average_Transaction_Value,
    COUNT(Transaction_ID) AS Transaction_Count
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Payment_Method
ORDER BY
    Average_Transaction_Value DESC;


-- =====================================================
-- 7. Monthly Sales Trend
-- Business question: How does revenue change over time?

SELECT
    FORMAT_DATE('%Y-%m', Transaction_Date) AS Month,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Sales
FROM
    `rational-symbol-514709-e8.customer_segmentation.customer_transactions_clean`
GROUP BY
    Month
ORDER BY
    Month;
