from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from sqlalchemy import create_engine
from llama_index.llms.groq import Groq
from llama_index.core.tools import QueryEngineTool

from dotenv import load_dotenv
import os

load_dotenv()

path_to_db = "/root/Projects/Mpesa-Agent/db.sqlite3"
engine = create_engine(f"sqlite:///{path_to_db}", future=True)

tables = ["product"]

sql_database = SQLDatabase(engine,_include_tables=tables)

llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))


sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    llm = llm
)

sql_tool = QueryEngineTool.from_defaults(
    query_engine=sql_query_engine,
    description=(
        "Useful for translating a natural language query into a SQL query over"
        " a table containing: product, containg a list of products offered by"
        " our e-commerce platform."
    ),
)
