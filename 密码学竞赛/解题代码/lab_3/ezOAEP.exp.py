import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import rsa
import base64
with open('rsakey.pem','rb') as privatefile:
	keydata=privatefile.read()
privkey=rsa.PrivateKey.load_pkcs1(keydata)
private_key = RSA.construct((privkey.n, privkey.e, privkey.d, privkey.p, privkey.q))
decipher = PKCS1_OAEP.new(private_key)

crypto='bT3PZSdqkCAQ6oRu29yWF9N0sy+byIq6p5dcmy29xXAYE339gRn5cvwuwT8MVMV2bZem/o88I9fwImUUeiPhRdZGEDWqaxXwa38GkYrmWmu//7UV3SiXqiBxWx618qUYfbqfdScHpJ3JDzcq822oSB+3yNQU4vkGXvvoDx522FY='

c = base64.b64decode(crypto)
flag = decipher.decrypt(c)
print(flag)