
import pandas as pd
import sqlite3

# Read CSV file
df = pd.read_csv("data/sales.csv")

# Connect to SQLite database
conn = sqlite3.connect(
    "database/sales.db"
)

# Store DataFrame in database
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

# Read first 5 records
result = pd.read_sql_query(
    "SELECT * FROM sales LIMIT 5",
    conn
)

print("\nDatabase records:")
print(result)

# Check total records
count = pd.read_sql_query(
    "SELECT COUNT(*) AS total_records FROM sales",
    conn
)

print("\nTotal records:")
print(count)

conn.close()
