# 🤖 Text-to-SQL Analytics Agent

An AI-powered Text-to-SQL application that converts natural language questions into SQL queries using **Qwen 2.5 and Ollama**. It validates generated queries using SQLGlot guardrails, executes approved queries against a SQLite database, and displays results through an interactive Streamlit interface.

## 🚀 Features

- **Natural Language to SQL:** Convert business questions into SQL queries.
- **AI-Powered SQL Generation:** Uses Qwen 2.5 through Ollama.
- **SQL Validation:** Validates generated queries using SQLGlot.
- **Read-Only Database Access:** Prevents database modifications through read-only SQLite connections.
- **Interactive Results:** Displays query results using Streamlit.
- **CSV Export:** Download query results for further analysis.
- **Error Handling:** Handles invalid queries and database execution errors.
- **Automated Workflow:** Generates, validates, executes, and displays SQL results.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Qwen 2.5 | SQL generation |
| Ollama | Local LLM execution |
| Streamlit | Web application interface |
| SQLite | Database management |
| SQLGlot | SQL parsing and validation |
| LangChain Ollama | LLM integration |
| Pandas | Data processing |
| NumPy | Numerical computing |

## 🔄 Application Workflow

```text
User Question
     |
     v
Streamlit Interface
     |
     v
Qwen 2.5 via Ollama
     |
     v
SQL Generation
     |
     v
SQL Cleaning
     |
     v
SQLGlot Guardrails
     |
     v
SQL Validation
     |
     v
SQLite Database
     |
     v
Pandas DataFrame
     |
     v
Display Results
     |
     v
CSV Download
```

## 💡 Example Queries

Users can enter natural language questions such as:

- Show the top 5 products by revenue.
- Calculate total sales for each region.
- Find the top 10 customers by revenue.
- Show monthly sales trends.
- Calculate the average order value.
- Identify the highest revenue-generating product category.
- Display yearly sales performance.

*Results depend on the available database schema and records.*

## 🔐 SQL Security and Validation

The application implements multiple safeguards before executing generated SQL queries.

- SQL parsing and validation using SQLGlot.
- Configured restrictions on permitted SQL operations.
- Read-only SQLite database connection.
- SQLite query-only mode.
- Exception handling during query execution.
- Automatic database connection closure.

Example:

```python
conn = sqlite3.connect(
    "file:database/sales.db?mode=ro",
    uri=True
)

conn.execute("PRAGMA query_only = ON")
```

**Note:** Production deployments should additionally implement query timeouts, resource limits, schema-level permissions, and comprehensive SQL validation.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Text-to-SQL-Analytics-Agent.git

cd Text-to-SQL-Analytics-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama:

https://ollama.com/

Download the Qwen 2.5 model:

```bash
ollama pull qwen2.5
```

Ensure Ollama is running before launching the application.

### 5. Configure the Database

Place your SQLite database at:

```text
database/sales.db
```

Ensure the database contains the tables and columns expected by the SQL generation logic.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will be available at the local URL displayed in your terminal.

## 📦 Requirements

Add the following dependencies to `requirements.txt`:

```text
streamlit
pandas
numpy
sqlglot
langchain-ollama
```

**Note:** `sqlite3` is part of Python's standard library and does not require separate installation.

## 🔮 Future Enhancements

- Interactive data visualization using Plotly.
- Support for multiple database connections.
- Conversational memory for follow-up questions.
- SQL query history and saved queries.
- User authentication and access control.
- Query optimization and execution monitoring.
- Support for additional LLM models.

## 🎯 Learning Outcomes

- Large Language Model (LLM) integration.
- Natural Language Processing and Text-to-SQL.
- SQL parsing, validation, and guardrails.
- SQLite database connectivity.
- Python-based application development.
- Interactive data applications using Streamlit.
- Data processing using Pandas.

## 👩‍💻 Author

**Shruti Sharma**

Android Developer | AI & Data Analytics Enthusiast

- GitHub: https://github.com/48Shruti/
- LinkedIn: https://www.linkedin.com/in/shruti-sharma-861712227/

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ Star.

Contributions, suggestions, and feedback are welcome!

---

**Built using Python, Generative AI, and Data Analytics.**
