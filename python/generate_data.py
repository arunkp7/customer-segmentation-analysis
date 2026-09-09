import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)

NUM_TRANSACTIONS = 1200
NUM_CUSTOMERS = 280

products = {
    "Laptop": ("Electronics", 600, 1200),
    "Smartphone": ("Electronics", 300, 900),
    "Headphones": ("Electronics", 40, 200),
    "Keyboard": ("Accessories", 30, 120),
    "Mouse": ("Accessories", 15, 80),
    "Backpack": ("Accessories", 30, 120),
    "T-Shirt": ("Clothing", 15, 50),
    "Jeans": ("Clothing", 30, 90),
    "Sneakers": ("Footwear", 50, 150),
    "Jacket": ("Clothing", 50, 180),
    "Coffee Maker": ("Home", 50, 180),
    "Blender": ("Home", 40, 150),
}

payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash"]
regions = ["North", "South", "East", "West"]

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

customer_ids = [f"C{i:03d}" for i in range(1, NUM_CUSTOMERS + 1)]

rows = []

for transaction_number in range(1, NUM_TRANSACTIONS + 1):

    customer_id = random.choice(customer_ids)
    product = random.choice(list(products.keys()))

    category, min_price, max_price = products[product]

    quantity = random.choices(
        [1, 2, 3, 4],
        weights=[70, 20, 8, 2]
    )[0]

    unit_price = round(random.uniform(min_price, max_price), 2)
    transaction_amount = round(quantity * unit_price, 2)

    days_range = (end_date - start_date).days
    transaction_date = start_date + timedelta(
        days=random.randint(0, days_range)
    )

    rows.append({
        "Customer_ID": customer_id,
        "Transaction_ID": f"T{transaction_number:04d}",
        "Transaction_Date": transaction_date.date(),
        "Product": product,
        "Product_Category": category,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Transaction_Amount": transaction_amount,
        "Payment_Method": random.choice(payment_methods),
        "Region": random.choice(regions),
    })


df = pd.DataFrame(rows)

df.to_csv(
    "data/raw/customer_transactions_raw.csv",
    index=False
)

print("Dataset created successfully.")
print(f"Rows: {len(df)}")
print(f"Customers: {df['Customer_ID'].nunique()}")
print(f"Products: {df['Product'].nunique()}")
print(f"Date range: {df['Transaction_Date'].min()} to {df['Transaction_Date'].max()}")