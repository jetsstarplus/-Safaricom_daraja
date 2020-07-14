import requests
import keys
import daraja
from access_token import authentication

access_token = authentication()


#register_url()
def simulate_transaction():
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode":keys.business_shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"10",
    "Msisdn":keys.TestMSISDN,
    "BillRefNumber":"12345678" }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)

simulate_transaction()
