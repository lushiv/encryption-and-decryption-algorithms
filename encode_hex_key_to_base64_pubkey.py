
import base64

def encode_pubic_key(pubkeyHex):
    ''' 
        encode hex key to base64 pubkey
    '''
    pubkeybytes = bytes.fromhex(pubkeyHex)
    pubkeyB64  = base64.b64encode(pubkeybytes)
    return pubkeyB64
