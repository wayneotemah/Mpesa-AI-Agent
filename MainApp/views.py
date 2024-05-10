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
        
        prompt = request.POST.get('Body').lower()
        
        response = agent.query(prompt)
        client.messages.create(
            body=response,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=f"whatsapp:{from_number}"
        )
        return HttpResponse("Reminder sent")  
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    
    