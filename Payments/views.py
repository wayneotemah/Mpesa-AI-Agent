from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import os
from dotenv import load_dotenv
from Payments.utility import mpesa_stk_push


load_dotenv()



# Create your views here.


#propmt mpsea view
@api_view(['POST'])
def mpesa(request):
    phone_number = request.data.get('phone_number')
    amount = request.data.get('amount')
    transaction_desc = request.data.get('transaction_desc')
    callback_url = os.environ.get('MPESA_CALLBACK_URL')
    print(phone_number, amount, transaction_desc, callback_url)
    
    response_context = {}
    if phone_number and amount and transaction_desc and callback_url:
        response = mpesa_stk_push(phone_number,
                                  amount,
                                  transaction_desc,
                                  callback_url)
        if response.ok:
            message = "Mpesa Prompted sent on the phone. Conplete tracsaction then wait for a few seconds"
            response_context["message"]= message
            
            return Response(response_context, status=status.HTTP_200_OK)
        message = "Failed to send Mpesa Prompt. Please try again"
        response_context["message"] = message   
        return Response(response_context, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = "Please provide all the required fields"
        response_context["message"] = message
        return Response(response_context, status=status.HTTP_400_BAD_REQUEST)