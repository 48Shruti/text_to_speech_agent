
from langchain_ollama import ChatOllama

from agent.sql_executor import get_schema

# Connect Ollama
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)


# Generate SQL
def generate_sql(question):

    schema = get_schema()

    schema_text = schema[
        ["name", "type"]
    ].to_string(index=False)

    prompt = f"""
    You are an expert SQLite SQL assistant.

    Database table: sales

    Database schema:
    {schema_text}

    User question:
    {question}

    Rules:
    1. Generate only SELECT queries.
    2. Use only the sales table.
    3. Use only existing columns.
    4. Never generate DELETE, DROP,
       UPDATE, INSERT or ALTER.
    5. Never generate multiple SQL statements.
    6. Return only SQL without explanations.

    SQL:
    """

    response = llm.invoke(prompt)

    return response.content.strip()


# Test
if __name__ == "__main__":

    question = "Show top 5 products by revenue"

    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)
