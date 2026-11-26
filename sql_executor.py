
import sqlite3
import pandas as pd

# Database connection
def get_connection():

    conn = sqlite3.connect(
        "file:database/sales.db?mode=ro",
        uri=True
    )

    return conn


# Get database tables
def get_tables():

    conn = get_connection()

    query = """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """

    tables = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return tables


# Get table columns
def get_schema():

    conn = get_connection()

    schema = pd.read_sql_query(
        "PRAGMA table_info(sales)",
        conn
    )

    conn.close()

    return schema


if __name__ == "__main__":

    print("Database Tables:")
    print(get_tables())

    print("\nDatabase Schema:")
    print(get_schema())
