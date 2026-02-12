import pandas as pd
import numpy as np


# 1. Load CSV into Pandas DataFrame


df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df)



# 2 - Add New Column "Total" = Quantity * Price

df["Total"] = df["Quantity"] * df["Price"]

print("\nData After Adding Total Column:")
print(df)


# 3 - Numpy Calculations

# Convert Total column into NumPy array
daily_sales = np.array(df["Total"])

# Total Sales
total_sales = np.sum(daily_sales)

# Average Daily Sales
average_sales = np.mean(daily_sales)

# Standard Deviation of Daily Sales
std_sales = np.std(daily_sales)

print("\n--- Sales Statistics ---")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation of Daily Sales:", std_sales)

# 4 - Best-Selling Product (Based on Quantity Sold)

# Group by Product and sum quantities
product_sales = df.groupby("Product")["Quantity"].sum()

# Find product with maximum quantity sold
best_selling_product = product_sales.idxmax()

print("\n--- Best Selling Product ---")
print("Total Quantity Sold per Product:")
print(product_sales)

print("\nBest Selling Product:", best_selling_product)
