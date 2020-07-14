
#other libraries import
from access_token import authentication
import requests
import keys
from encryption_password import data_encryption
from utils import timestamp



#create the lipa na mpesa API
def lipa_na_mpesa():
        
    access_token = authentication()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": data_encryption(timestamp()),
        "Timestamp": timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 100,
        "PartyA":254701850242,
        "PartyB":keys.business_shortcode,
        "PhoneNumber": 254701850242,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": "11111 ",
        "TransactionDesc": "Pay school Fees"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
  
#authentication() 
lipa_na_mpesa()