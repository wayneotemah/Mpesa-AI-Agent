from llama_index.llms.groq import Groq
from llama_index.core.tools import QueryEngineTool,ToolMetadata
from Commerce.pdf_engine import about_company_engine
from Commerce.sql_engine import sql_engine
from llama_index.core.agent import ReActAgent
import os
from dotenv import load_dotenv

load_dotenv()


llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))


tools = [
    QueryEngineTool(
        query_engine=sql_engine,
        metadata=ToolMetadata(
            name="trainee_infromation",
            description="this gives detailed information about the trainees in the data science program.",
        ),
    ),
     QueryEngineTool(
        query_engine=about_company_engine,
        metadata=ToolMetadata(
            name="company_information",
            description="this gives information about the XYZ company.",
        ),
    ),
]


context = """Purpose: The primary role of this agent is to assist users in there shopping by providing accurate 
            information and assistance about the products or the company. """

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)