from django_daraja.mpesa.core import MpesaClient


def mpesa_stk_push(phone_number, amount, transaction_desc, callback_url):
    cl = MpesaClient()
    phone_number = phone_number
    amount = amount
    account_reference = "reference"
    transaction_desc = "Description"
    callback_url = callback_url
    response = cl.stk_push(
        phone_number, amount, account_reference, transaction_desc, callback_url
    )
    return response