import requests
import keys
from requests.auth import HTTPBasicAuth

#this is the authentication from safaricom
def authentication():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_token = r.json()
    my_access_token = json_token["access_token"]
    return my_access_token
