#in this file we register our url to safaricon

import requests
import keys
import daraja
from access_token import authentication

access_token = authentication()

def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode":keys.business_shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fullstackdjango.com/confirm",
        "ValidationURL": "https://fullstackdjango.com/confirm"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)