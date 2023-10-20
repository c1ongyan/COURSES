from Crypto.Util.number import *
from base64 import b64encode,b64decode

n=4929631834//2
a=38219
b=51853
status=295614965
status = (a*status +b) %n

def stream_key():
    global status
    status = (a*status +b) %n
    tk=[]
    tmp=status
    for i in range(4):
        tk.append(tmp&0xff)
        tmp>>=8
    return tk
def encry(m):
    xxx=b''
    rk=[]
    for i in range(11):
        rk.extend(stream_key())
    for i in range(len(m)):
        #print(rk[i])
        #print(long_to_bytes(m[i]^rk[i]))
        xxx+=long_to_bytes(m[i]^rk[i])
    return  xxx
flag=b'R/TOdy+8Glz/ub5d5eDWHq82FXIkfo8bUYs9YwsxLlcW1Sk2eOVIZBY3'
flag=b64decode(flag)
#print(flag)
enc=encry(flag)
print('Your flag is:{}'.format(enc))
#flag{f2235aa7-de3a-4fc0-8b4a-78b3a308b4d1}
