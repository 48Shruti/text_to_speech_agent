
import sqlglot
from sqlglot import exp

ALLOWED_TABLES = {"sales"}

def validate_sql(query):

    try:
        # Parse SQL query
        statements = sqlglot.parse(query, read="sqlite")

        # Check only one SQL statement
        if len(statements) != 1 or statements[0] is None:
            return False, "Only one SQL statement is allowed."

        parsed = statements[0]

        # Allow only SELECT queries
        if not isinstance(parsed, (exp.Select, exp.Union)):
            return False, "Only SELECT queries are allowed."

        # Check all tables used in the query
        for table in parsed.find_all(exp.Table):

            if table.name.lower() not in ALLOWED_TABLES:
                return False, f"Table not allowed: {table.name}"

            if table.db or table.catalog:
                return False, "Database-qualified tables are not allowed."

        # Add a limit if the query does not have one
        if parsed.args.get("limit") is None:
            parsed = parsed.limit(100)

        # Convert back to SQLite SQL
        safe_query = parsed.sql(dialect="sqlite")

        return True, safe_query

    except Exception as e:
        return False, f"Invalid SQL: {str(e)}"
