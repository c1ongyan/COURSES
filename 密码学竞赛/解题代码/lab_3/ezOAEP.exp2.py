import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
with open("rsakey.pem", 'rb') as x:
    private_key = RSA.importKey(x.read())
oaep=PKCS1_OAEP.new(private_key)

chiper='bT3PZSdqkCAQ6oRu29yWF9N0sy+byIq6p5dcmy29xXAYE339gRn5cvwuwT8MVMV2bZem/o88I9fwImUUeiPhRdZGEDWqaxXwa38GkYrmWmu//7UV3SiXqiBxWx618qUYfbqfdScHpJ3JDzcq822oSB+3yNQU4vkGXvvoDx522FY='
chiper=base64.b64decode(chiper)
flag=oaep.decrypt(chiper)
print(flag)