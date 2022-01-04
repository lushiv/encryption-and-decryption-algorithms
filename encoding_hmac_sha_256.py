
import hmac
import hashlib
import binascii
import uuid

#generate secret key
seckret_key = uuid.uuid4().hex

#you input data
request_data = 'TEST STRING DATA'

def encoding_with_hmac_sha256(key, message):
   ''' Python3 encoded string data with hmac sha256 '''
   byte_key = binascii.unhexlify(key)
   message = message.encode()
   encoded_data = hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
   print(encoded_data)

encoding_with_hmac_sha256(seckret_key,request_data)