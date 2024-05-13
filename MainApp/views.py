from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from twilio.rest import Client
from dotenv import load_dotenv
import os

from Commerce.agent import agent

load_dotenv()

client = Client(os.getenv("TWILIO_ACCOUNT_SID"),os.getenv("TWILIO_AUTH_TOKEN"))


@api_view(["POST"])
def rag_agent(request):
    try: 
        # view inteeface for a rag agent that uses the SQL query engine
        from_number = request.POST.get('From')
        
        #remove the "whatsapp:" from the string, by spiliting by : then take the second part
        user_number = from_number.rsplit(":")[1]
        
        prompt = request.POST.get('Body')
        prompt = prompt + f"\nmy phone number is {user_number}"
        
        print(prompt)
        
        response = agent.query(prompt)
        client.messages.create(
            body=response,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=f"{from_number}"
        )
        return HttpResponse("message sent")  
    except Exception as e:
        print(e)
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    
    