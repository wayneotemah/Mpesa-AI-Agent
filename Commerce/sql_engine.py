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

tables = ["Commerce_product"]

sql_database = SQLDatabase(engine,include_tables=tables)

llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))


sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    llm = llm
)

