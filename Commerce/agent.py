from llama_index.llms.groq import Groq
from llama_index.core.tools import QueryEngineTool,ToolMetadata,FunctionTool
from Commerce.models import Product
from Commerce.pdf_engine import about_company_engine
from Commerce.sql_engine import sql_query_engine
from llama_index.core.agent import ReActAgent
import os
from dotenv import load_dotenv

load_dotenv()


llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))

def send_product_picture_with_whatsAPP_wrapper(*arg,**kwargs):
    product_id = kwargs.get("input")
    phone_number = kwargs.get("phone_number")
    print(product_id, phone_number)
    Product.send_product_picture_with_whatsAPP(product_id, phone_number)

tools = [
    QueryEngineTool(
        query_engine=sql_query_engine,
        metadata=ToolMetadata(
            name="product_information",
            description="sql tool to get the products records and details for database.",
        ),
    ),
    QueryEngineTool(
        query_engine=about_company_engine,
        metadata=ToolMetadata(
            name="company_information",
            description="this gives information about the XYZ company.",
        ),
    ),
    FunctionTool(
        fn=send_product_picture_with_whatsAPP_wrapper,
        metadata=ToolMetadata(
            name="send_product_picture_with_whatsAPP",
            description="this sends a picture of a product to a user's whatsapp number, take in product id and user phone number.",
        ),
    )
     
]

context = """Purpose: The primary role of this agent is to assist users in there shopping by providing accurate 
            information and assistance about the products our the company. """

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)