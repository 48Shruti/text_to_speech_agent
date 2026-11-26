
import streamlit as st
import pandas as pd
import sqlite3

from agent.sql_generator import generate_sql
from agent.sql_guardrails import validate_sql


# Streamlit page settings
st.set_page_config(
    page_title="Text-to-SQL Analytics Agent",
    page_icon="🤖",
    layout="wide"
)


# Function to clean generated SQL
def clean_sql(query):

    query = query.replace("```sql", "")
    query = query.replace("```SQL", "")
    query = query.replace("```", "")

    return query.strip()


# Function to execute SQL safely
def execute_query(query):

    conn = sqlite3.connect(
        "file:database/sales.db?mode=ro",
        uri=True
    )

    try:
        conn.execute("PRAGMA query_only = ON")

        df = pd.read_sql_query(query, conn)

        return df

    finally:
        conn.close()


# Application heading
st.title("🤖 Text-to-SQL Analytics Agent")

st.write(
    "Ask business questions in English "
    "and get answers directly from your sales database."
)

st.divider()


# User question
st.subheader("Ask Your Business Question")

question = st.text_area(
    "Enter your question:",
    placeholder="Example: Show top 5 products by revenue",
    height=100
)


# Submit button
if st.button("Generate Answer", type="primary"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Generating SQL using Qwen..."):

                # Step 1: Generate SQL
                generated_sql = generate_sql(question)

                generated_sql = clean_sql(generated_sql)

            st.subheader("Generated SQL")

            st.code(generated_sql, language="sql")


            # Step 2: Validate SQL
            is_valid, result = validate_sql(generated_sql)

            if not is_valid:

                st.error("SQL query blocked by guardrails.")

                st.write("Reason:", result)

            else:

                st.success("SQL query approved!")

                st.subheader("Validated SQL")

                st.code(result, language="sql")


                # Step 3: Execute SQL
                with st.spinner("Fetching database results..."):

                    df = execute_query(result)


                # Step 4: Display results
                st.subheader("Query Results")

                if df.empty:

                    st.info("No records found.")

                else:

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                    st.success(
                        f"Found {len(df)} records."
                    )

                    # Download results
                    csv = df.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        label="Download Results as CSV",
                        data=csv,
                        file_name="query_results.csv",
                        mime="text/csv"
                    )

        except Exception as e:

            st.error(f"Something went wrong: {e}")


st.divider()

st.caption(
    "Powered by Ollama, Qwen 2.5, SQLGlot, SQLite and Streamlit"
)
