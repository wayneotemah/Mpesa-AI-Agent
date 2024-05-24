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
    product_name = kwargs.get("product_name")
    phone_number = kwargs.get("phone_number")
    print(product_name, phone_number)
    message  = Product.send_product_picture_with_whatsAPP(product_name, phone_number)
    return message

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
            description="Provides  extra and detailed information about the XYZ company.",
        ),
    ),
    FunctionTool(
        fn=send_product_picture_with_whatsAPP_wrapper,
        metadata=ToolMetadata(
            name="send_product_picture_with_whatsAPP",
            description="""
            this sends a picture of a product to a user's whatsapp number, takes in product name and user's phone number in the following format {"product_name":product_id,"phone_number":phone_number}.
            it returns string sent
            """,
        ),
    ),
]

context = """Purpose: You are Debu, a friendly ecommers bot for the XYZ company on the WhatsApp platform whose primary role is to intreacts and assist users in thier shopping by providing accurate information and assistance about the products of the company.Your goal is to try keep customers engagement and get the client to buy a product by providing them with the information they need.Our major product categories are Electronics, Fashion, Home, Beauty, and Toys. And if the product does not exist, inform the user."""

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)