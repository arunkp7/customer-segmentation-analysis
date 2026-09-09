import pandas as pd

# Load cleaned transaction data
df = pd.read_csv("data/processed/customer_transactions_clean.csv")

# Convert transaction date from text into a date format
df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"],
    dayfirst=True
)

# Reference date = day after the latest transaction in the dataset
reference_date = df["Transaction_Date"].max() + pd.Timedelta(days=1)

# Calculate customer-level metrics
customer_metrics = df.groupby("Customer_ID").agg(
    Transaction_Frequency=("Transaction_ID", "count"),
    Spending=("Transaction_Amount", "sum"),
    Last_Transaction_Date=("Transaction_Date", "max"),
    Product_Usage=("Product", "nunique")
)

# Calculate number of days since each customer's last purchase
customer_metrics["Recency"] = (
    reference_date - customer_metrics["Last_Transaction_Date"]
).dt.days

# Remove the date column because Recency is the metric we need
customer_metrics = customer_metrics.drop(
    columns=["Last_Transaction_Date"]
)

# Round spending to 2 decimal places
customer_metrics["Spending"] = customer_metrics["Spending"].round(2)

# Display the customer-level metrics
print("Customer metrics:")
print(customer_metrics.head())

print("\nCustomer metrics shape:", customer_metrics.shape)

print("\nMetric summary:")
print(customer_metrics.describe())

# Save the customer-level metrics for later analysis
customer_metrics.to_csv(
    "data/processed/customer_metrics.csv"
)

print("\nCustomer metrics saved successfully.")

# Display useful percentile values to help determine
# data-driven thresholds for customer segmentation

print("\nMetric percentiles:")

print("\nTransaction Frequency:")
print(customer_metrics["Transaction_Frequency"].quantile([0.25, 0.50, 0.75]))

print("\nSpending:")
print(customer_metrics["Spending"].quantile([0.25, 0.50, 0.75]))

print("\nRecency:")
print(customer_metrics["Recency"].quantile([0.25, 0.50, 0.75]))

print("\nProduct Usage:")
print(customer_metrics["Product_Usage"].quantile([0.25, 0.50, 0.75]))

# ---------------------------------------------------------
# 3. CUSTOMER SEGMENTATION
# ---------------------------------------------------------

# Score Transaction Frequency
# Higher frequency = better engagement
customer_metrics["Frequency_Score"] = pd.cut(
    customer_metrics["Transaction_Frequency"],
    bins=[-1, 3, 5, float("inf")],
    labels=[1, 2, 3]
).astype(int)


# Score Spending
# Higher spending = higher customer value
customer_metrics["Spending_Score"] = pd.cut(
    customer_metrics["Spending"],
    bins=[-float("inf"), 434.74, 1484.02, float("inf")],
    labels=[1, 2, 3]
).astype(int)


# Score Recency
# Lower recency = more recent purchase = better engagement
customer_metrics["Recency_Score"] = pd.cut(
    customer_metrics["Recency"],
    bins=[-1, 22, 113, float("inf")],
    labels=[3, 2, 1]
).astype(int)


# Score Product Usage
# Higher product usage = broader product engagement
customer_metrics["Product_Usage_Score"] = pd.cut(
    customer_metrics["Product_Usage"],
    bins=[-1, 3, 4, float("inf")],
    labels=[1, 2, 3]
).astype(int)


# Add the four metric scores together
customer_metrics["Total_Score"] = (
    customer_metrics["Frequency_Score"]
    + customer_metrics["Spending_Score"]
    + customer_metrics["Recency_Score"]
    + customer_metrics["Product_Usage_Score"]
)


# Assign one of the three customer segments
customer_metrics["Segment"] = pd.cut(
    customer_metrics["Total_Score"],
    bins=[0, 5, 8, 12],
    labels=[
        "At-Risk / Low Engagement",
        "Regular / Growth Potential",
        "High-Value / Engaged"
    ]
)


# Display segment counts
print("\nCustomer segment counts:")
print(customer_metrics["Segment"].value_counts())


# Display sample segmented customers
print("\nSegmented customers:")
print(
    customer_metrics[
        [
            "Transaction_Frequency",
            "Spending",
            "Product_Usage",
            "Recency",
            "Total_Score",
            "Segment"
        ]
    ].head(10)
)


# Save the final customer segmentation data
customer_metrics.to_csv(
    "data/processed/customer_segments.csv"
)

print("\nCustomer segmentation saved successfully.")

# ---------------------------------------------------------
# 4. SEGMENT PROFILE
# ---------------------------------------------------------

# Calculate average customer metrics for each segment
segment_profile = customer_metrics.groupby("Segment", observed=True)[
    [
        "Transaction_Frequency",
        "Spending",
        "Product_Usage",
        "Recency"
    ]
].mean().round(2)

print("\nSegment profile:")
print(segment_profile)

# ---------------------------------------------------------
# 5. SEGMENT BUSINESS ANALYSIS
# ---------------------------------------------------------

# Calculate the number of customers and average metrics
# for each customer segment
segment_analysis = customer_metrics.groupby(
    "Segment",
    observed=True
).agg(
    Customer_Count=("Segment", "size"),
    Avg_Frequency=("Transaction_Frequency", "mean"),
    Avg_Spending=("Spending", "mean"),
    Avg_Product_Usage=("Product_Usage", "mean"),
    Avg_Recency=("Recency", "mean")
).round(2)

print("\nSegment business analysis:")
print(segment_analysis)

# ---------------------------------------------------------
# 6. SEGMENT REVENUE CONTRIBUTION
# ---------------------------------------------------------

# Calculate total customer spending for each segment
segment_revenue = customer_metrics.groupby(
    "Segment",
    observed=True
)["Spending"].sum().round(2)

print("\nSegment revenue contribution:")
print(segment_revenue)

# Calculate each segment's percentage of total customer spending
segment_revenue_percentage = (
    segment_revenue / customer_metrics["Spending"].sum() * 100
).round(2)

print("\nSegment revenue percentage:")
print(segment_revenue_percentage)