
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)

n = 5000

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Printer"
]

categories = [
    "Electronics",
    "Accessories",
    "Computers"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

# Create DataFrame
df = pd.DataFrame({

    "order_id": range(1, n + 1),

    "order_date": pd.date_range(
        start="2025-01-01",
        periods=n,
        freq="h"
    ),

    "product_name": np.random.choice(
        products, n
    ),

    "category": np.random.choice(
        categories, n
    ),

    "quantity": np.random.randint(
        1, 10, n
    ),

    "price": np.random.randint(
        500, 50000, n
    ),

    "region": np.random.choice(
        regions, n
    ),

    "customer_id": np.random.randint(
        1000, 2000, n
    )

})

# Save CSV
df.to_csv(
    "data/sales.csv",
    index=False
)

print("Dataset created successfully!")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())
