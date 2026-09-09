# Import pandas for loading and analyzing the dataset
import pandas as pd


# Load the cleaned transaction data from the processed folder
df = pd.read_csv("data/processed/customer_transactions_clean.csv")


# ---------------------------------------------------------
# 1. DATASET OVERVIEW
# ---------------------------------------------------------

# Display the number of rows and columns in the dataset
print("Dataset shape:", df.shape)

# Display the first 5 rows to understand how the data looks
print("\nFirst 5 rows:")
print(df.head())

# Display the data type of each column
# This helps us check whether columns contain text, integers, decimals, etc.
print("\nData types:")
print(df.dtypes)

# Count the number of unique customers
print("\nUnique customers:", df["Customer_ID"].nunique())

# Count the number of unique products
print("Unique products:", df["Product"].nunique())

# Count the number of unique product categories
print("Unique categories:", df["Product_Category"].nunique())

# Find the earliest and latest transaction dates
print("\nDate range:")
print(df["Transaction_Date"].min(), "to", df["Transaction_Date"].max())

# Calculate total sales across all transactions
print("\nTotal sales:", round(df["Transaction_Amount"].sum(), 2))


# ---------------------------------------------------------
# 2. TRANSACTIONS PER CUSTOMER
# ---------------------------------------------------------

# Group transactions by customer and count how many transactions
# each customer has made
customer_transactions = df.groupby("Customer_ID").size()

# Show summary statistics for transaction frequency
# This includes average, minimum, maximum, median, etc.
print("\nTransactions per customer:")
print(customer_transactions.describe())

# Sort customers by transaction count from highest to lowest
# and display the top 10 customers
print("\nTop 10 customers by transaction count:")
print(customer_transactions.sort_values(ascending=False).head(10))


# ---------------------------------------------------------
# 3. SPENDING PER CUSTOMER
# ---------------------------------------------------------

# Group transactions by customer and calculate
# the total amount spent by each customer
customer_spending = df.groupby("Customer_ID")["Transaction_Amount"].sum()

# Show summary statistics for customer spending
print("\nSpending per customer:")
print(customer_spending.describe())

# Sort customers by total spending from highest to lowest
# and display the top 10 customers
print("\nTop 10 customers by total spending:")
print(customer_spending.sort_values(ascending=False).head(10))


# ---------------------------------------------------------
# 4. SALES BY PRODUCT CATEGORY
# ---------------------------------------------------------

# Group transactions by product category
# and calculate total sales for each category
category_sales = df.groupby("Product_Category")["Transaction_Amount"].sum()

# Display categories from highest sales to lowest sales
print("\nSales by product category:")
print(category_sales.sort_values(ascending=False))


# ---------------------------------------------------------
# 5. SALES BY REGION
# ---------------------------------------------------------

# Group transactions by region
# and calculate total sales for each region
region_sales = df.groupby("Region")["Transaction_Amount"].sum()

# Display regions from highest sales to lowest sales
print("\nSales by region:")
print(region_sales.sort_values(ascending=False))