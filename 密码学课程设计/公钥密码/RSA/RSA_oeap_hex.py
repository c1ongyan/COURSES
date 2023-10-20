from Crypto.Util.number import *
import hashlib
import rsa
import libnum
import math
import random

def get_str_sha1_secret_str(res):
    """
    使用sha1加密算法，返回bytes加密后的hex字符串
    """
    sha = hashlib.sha1(res)
    encrypts = sha.hexdigest()
    return encrypts


def oeap_encode(n,e,m,l=b''):
    n_hex = hex(n)[2:]
    if len(n_hex)&1 == 1:
        n_hex = '0' + n_hex
    k = len(n_hex)//2
    hLen = 20
    mLen = len(m)
    #长度检查
    if mLen>(k-2-2*hLen):
        return '消息过长!\n'
    #EME_oaep编码
    lhash = get_str_sha1_secret_str(l)
    if (k - mLen - 2*hLen - 2)>0:
        ps = '00' * (k - mLen - 2*hLen - 2) + '01'
    else:
        ps = '01'
    DB = lhash + ps + m.hex()
    seed = g_seed(hLen)
    dbMask = MGF(seed,k - hLen -1,hLen)
    maskedDB = hex_xor(dbMask,DB,(k-hLen-1)*2)  #da39a3ee5e6b4b0d3255bfef95601890afd80709
    seedMask = MGF (maskedDB, hLen,hLen)
    maskedSeed = hex_xor(seed ,seedMask ,hLen*2)
    EM = '00' + maskedSeed + maskedDB
    return EM

def MGF(x,maskLen,hLen):
    T=bytearray(b'')
    k = maskLen // hLen
    if len(x)&1 == 1:
        x= '0'+x
    X = bytearray.fromhex(x)
    if maskLen%hLen == 0:
        k -= 1
    for i in range(k+1):
        tmp = X + bytearray.fromhex('%08x'%i)
        T = T + bytearray.fromhex(get_str_sha1_secret_str(tmp))
    mask = T[:maskLen]
    return mask.hex()



def g_seed(hLen):
    b = bytearray(hLen)
    for i in range(hLen):
        b[i] = random.randint(0,255)
    return b.hex()


'''
rsa.encrypt(m,e,N):
    return c

rsa.decrypt(c,d,N):
    return m
'''
def En(m,e,N):
    EM=oeap_encode(N,e,m,l=b'')
    return rsa.encrypt(EM,e,N)

def De(c,d,N):
    pass

#print(hashlib.sha1(1).hexdigest())
print(hashlib.sha1(b''))
print(hashlib.sha1(b'').hexdigest())
c=hashlib.sha1(b'').digest()
print(c)
print(int('da',16))
print(c[0].to_bytes(2, byteorder='big'))
'''
message="Zhouzixin is a handsome girl.If you like her, she also like you."
m=libnum.s2n(message)
m=long_to_bytes(m)
print(m)
e=87611
N=82288670010532815175470059788418565917756764136120014418374696488719267692808285630768685256262000729912808615457831444722845533599198982089245807163465129010952647154384614878460514524078564986455281426684722876490811970921076679894460016585230905662489683380098202186769190993903487883974031644274921961447
En(m,e,N)
'''

