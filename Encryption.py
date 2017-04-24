from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode


class Encryption(object):

    def __init__(self):
        self.key = b"the big brown black fox jumps the rail"

    def encrypt_RSA(self, message):
        '''
        param: public_key_loc Path to public key
        param: message String to be encrypted
        return base64 encoded encrypted string
        '''
        key = self.key
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message)
        return encrypted.encode('base64')

    def printname(self):
        print("that is the name of the function ")

encrypt = Encryption()
ans = encrypt.encrypt_RSA("moshood")
print(ans)
