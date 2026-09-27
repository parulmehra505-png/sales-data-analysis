import pandas as pd
import numpy as np

np.random.seed(42)

products = [
    ("Wireless Mouse", "Electronics", 19.99),
    ("Mechanical Keyboard", "Electronics", 59.99),
    ("USB-C Hub", "Electronics", 29.99),
    ("Laptop Stand", "Office", 34.99),
    ("Desk Lamp", "Office", 24.99),
    ("Office Chair", "Office", 149.99),
    ("Notebook Set", "Stationery", 8.99),
    ("Gel Pens (Pack)", "Stationery", 6.49),
    ("Water Bottle", "Lifestyle", 15.99),
    ("Backpack", "Lifestyle", 45.99),
]

regions = ["North", "South", "East", "West"]

date_range = pd.date_range("2024-01-01", "2024-12-31", freq="D")

rows = []
order_id = 1000

for date in date_range:
    seasonal_boost = 1.8 if date.month in (11, 12) else 1.0
    weekday_boost = 1.3 if date.weekday() < 5 else 0.8
    num_orders_today = int(np.random.poisson(6 * seasonal_boost * weekday_boost))

    for _ in range(num_orders_today):
        product_name, category, price = products[np.random.randint(len(products))]
        quantity = np.random.randint(1, 6)

        rows.append({
            "order_id": order_id,
            "date": date.strftime("%Y-%m-%d"),
            "product": product_name,
            "category": category,
            "region": regions[np.random.randint(len(regions))],
            "quantity": quantity,
            "unit_price": price,
            "revenue": round(price * quantity, 2),
        })
        order_id += 1

df = pd.DataFrame(rows)
df.to_csv("Data/sales_data.csv", index=False)

print(f"Done! Created {len(df)} sales records in Data/sales_data.csv")