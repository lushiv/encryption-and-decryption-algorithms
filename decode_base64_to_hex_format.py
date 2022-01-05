import base64

def decode_public_key(pubkeyB64):
    '''
        decode base64 to hex format
    '''
    pubkeyBytes = base64.b64decode(pubkeyB64)
    pubkeyHex = pubkeyBytes.hex()   
    return '0x'+pubkeyHex

