import matplotlib
matplotlib.use("Agg")  # lets matplotlib save charts to a file without opening a window
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Data/sales_data.csv")

print("Shape of the data (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types of each column:")
print(df.dtypes)

print("\nQuick statistics (count, mean, min, max, etc.):")
print(df.describe())
# --- Monthly sales trend ---

# Convert the 'date' column from plain text into an actual date type,
# so pandas understands it as a calendar date, not just a string.
df["date"] = pd.to_datetime(df["date"])

# Group all orders by month and sum up their revenue.
# resample("ME") means "group by Month End".
monthly_revenue = df.set_index("date").resample("ME")["revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)
# --- Top-performing products ---

# Group by product name, sum revenue per product, sort highest first
top_products_by_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

print("\nTop Products by Revenue:")
print(top_products_by_revenue)

# Same idea, but ranking by units sold instead of revenue
top_products_by_units = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

print("\nTop Products by Units Sold:")
print(top_products_by_units)
# --- Charts ---

# 1. Monthly revenue trend (line chart)
plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("Output/monthly_trend.png")
plt.close()

# 2. Top products by revenue (bar chart)
plt.figure(figsize=(9, 6))
top_products_by_revenue.sort_values().plot(kind="barh", color="steelblue")
plt.title("Top Products by Revenue")
plt.xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("Output/top_products.png")
plt.close()

print("\nCharts saved! Check the Output folder for monthly_trend.png and top_products.png")