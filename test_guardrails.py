
from sql_guardrails import validate_sql

queries = [
    "SELECT product_name, price FROM sales",
    "DELETE FROM sales",
    "DROP TABLE sales",
    "UPDATE sales SET price = 100",
    "SELECT * FROM customers"
]

for query in queries:

    is_valid, result = validate_sql(query)

    print("\nOriginal Query:", query)

    if is_valid:
        print("Status: ALLOWED")
        print("Safe SQL:", result)
    else:
        print("Status: BLOCKED")
        print("Reason:", result)
