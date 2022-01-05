import hmac
import hashlib
import binascii
import json

SHA_KEY = 'E49756B4C8FAB4E48222A3E7F3B97CC3'
data = { "id": "1001", "type": "Regular" }

def _generate_sha256_signature(data):
  key = SHA_KEY
  key_bytes= bytes(key , 'latin-1')
  data_bytes = bytes(data, 'latin-1')
  return hmac.new(key_bytes, data_bytes , hashlib.sha256).hexdigest().lower()

def clean_data(data):
    data_list_alphabetic = sorted(data.items())
    data_string = ''

    for data_ in data_list_alphabetic:
        new_str = '{}={}&'.format(data_[0],data_[1])
        data_string=data_string+new_str

    res_data = _generate_sha256_signature(data_string[:-1])
    print(res_data)

clean_data(data)