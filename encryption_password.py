import base64
import keys

#encrypting the data we are using

def data_encryption(formatted_time):
    data_to_encode = keys.business_shortcode + keys.LipaNaMpesaOnlineShortcode + formatted_time
    encoded_data = base64.b64encode(data_to_encode.encode())
    #print(encoded_data)
    decoded_password = encoded_data.decode('utf-8')
    return decoded_password
