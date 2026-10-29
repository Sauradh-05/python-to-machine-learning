
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Tablet", "Tablet"],
    "Region": ["West", "East", "East", "West", "West", "East"],
    "Quantity": [5, 10, 3, 8, 6, 4],
    "Price": [50000, 20000, 50000, 20000, 15000, 15000]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# 1. Total revenue by product
print("\nTotal Revenue by Product")
print(df.groupby("Product")["Revenue"].sum())

# 2. Revenue summary by region
print("\nRevenue Summary by Region")
print(df.groupby("Region")["Revenue"].agg(["sum", "mean"]))

# 3. Product revenue across regions
print("\nProduct Revenue Pivot Table")
print(pd.pivot_table(
    df,
    values="Revenue",
    index="Product",
    columns="Region",
    aggfunc="sum",
    fill_value=0
))
