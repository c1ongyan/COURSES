from random import randint
import math
import secrets
import hashlib
import os
import typing

Key = typing.Tuple[int, int]

def GetPrime(n):
    #得到nbit位的素数
    #为保证有n位，最高位为1
    while True:
        res='1'
        for _ in range(n-2):
            tmp=randint(0,1)
            res=res+str(tmp)
        res=res+'1' #保证最低位是1=>保证是奇数
        num=int(res,2)
        if miillerTest(num,10):
            return num

def mypower(a,n,m):
    #实现a的n次幂模m
    #n==>2进制串AiAi-1...A0==>2^i*Ai+2^(i-1)*Ai-1+...+2^0*(A0)
    #a^n==>a^(2^i*Ai+2^(i-1)*Ai-1+...+2^0*(A0))
    a=a%m
    result=1
    while n!=0:
        if n&1:
            result=(result*a)%m
        n=n>>1
        a=(a*a)%m
    return result



def miillerTest(n, k):
    #miiller素性检验
    #用miller_rabin算法对n进行k次检测
    if n%2==0:
        return False
    if n<2:
        return False
    d=n-1
    r=0
    while not (d&1): #d为偶数进入循环==>最后得到2^r*d
        r+=1
        d>>=1 #d除以2

    for _ in range(k):
        a=randint(1,n-1)
        x=pow(a,d,n) 
        if x==1 or x==n-1:
            continue
        flag=0 
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                flag=1
                break
        if flag==0:
            return False

    return True

def ext_gcd(a,b):
    #扩展欧几里得算法 用辗转相除法计算a,b的最大公因子gcd(a,b),倒推求出满足xa+yb=gcd(a,b)的x,y
    if b==0:
        return 1,0,a #x,y,gcd(a,b)
    else:
        x,y,g=ext_gcd(b,a%b)
        x,y=y,(x-(a//b)*y)
        return x,y,g

def mod_inverse(a,m):
    #求a模n的逆元b 即a*b=1(mod m)  
    x,y,g=ext_gcd(a,m) #ax+my=1 ==>ax=1(mod m)
    if g!=1:
        print(str(a)+'不可逆')
    else:
        return x%m

def gcd(a, b):
    #辗转相除法求最大公因数
    if a > b: a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a


def lcm(x, y):
    return x * y / gcd(x, y)

#OAEP模式

def sha1(m: bytes) :
    #SHA-1 hash
    hasher = hashlib.sha1()
    hasher.update(m)
    return hasher.digest()

def os2ip(x: bytes) :
    #按字节转换为非负整数
    return int.from_bytes(x, byteorder='big')

def i2osp(x: int, xlen: int) -> bytes:
    #将整数转换为指定长度的字节
    return x.to_bytes(xlen, byteorder='big')

def MGF1(seed: bytes, mlen: int) -> bytes:
    #基于SHA-1的掩模生成函数
    t = b''
    hlen = 128
    for c in range(0, math.ceil(mlen / hlen)):
        _c = i2osp(c, 4)
        t += sha1(seed + _c)
    return t[:mlen]

def xor(data: bytes, mask: bytes) -> bytes:
    #按字节位异或
    masked = b''
    ldata = len(data)
    lmask = len(mask)
    for i in range(max(ldata, lmask)):
        if i < ldata and i < lmask:
            masked += (data[i] ^ mask[i]).to_bytes(1, byteorder='big')
        elif i < ldata:
            masked += data[i].to_bytes(1, byteorder='big')
        else:
            break
    return masked

def get_key_len(key: Key):
    #公钥n的字节长度
    _, n = key
    return n.bit_length() // 8

def RSAOAEPEnc(M: bytes, publicKey: Key) :
    hLen = 20
    k = get_key_len(publicKey)
    mLen = len(M)

    #长度检查
    assert mLen <= k - hLen - 2

    lHash = sha1(b'')
    hLen = len(lHash)

    #EME-OAEP编码
    ps = b'\x00' * (k - mLen - 2 * hLen - 2)

    DB = lHash + ps + b'\x01' + M

    seed = os.urandom(hLen)
    dbMask = MGF1(seed, k - hLen - 1)
    maskedDB = xor(DB, dbMask)
    seedMask = MGF1(maskedDB, hLen)
    maskedSeed = xor(seed, seedMask)
    EM = b'\x00' + maskedSeed + maskedDB

    #RSA加密
    m = os2ip(EM)
    c = RSAEP(publicKey, m)
    C = i2osp(c, k)

    return C

def RSAOAEPDec(privateKey: Key, C: bytes):
    lHash = sha1(b'')

    # 使用 sha1 时的默认长度
    hLen = 20

    k = get_key_len(privateKey)
    assert len(C) == k

    c = os2ip(C)
    d, n = privateKey
    m = mypower(c, d, n)
    #print("m = " + str(m))
    EM = i2osp(m, k)

    #EME-OAEP 解码

    _, maskedSeed, maskedDB = EM[:1], EM[1:1 + hLen], EM[1 + hLen:]

    seedMask = MGF1(maskedDB, hLen)
    seed = xor(maskedSeed, seedMask)
    dbMask = MGF1(seed, k - hLen - 1)
    DB = xor(maskedDB, dbMask)

    _lHash = DB[:hLen]

    assert lHash == _lHash
    i = hLen
    while i < len(DB):
        if DB[i] == 0:
            i += 1
            continue
        elif DB[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    M = DB[i:]
    return M

def generateKeys(n):
    #获取位数为n的p,q 并选取合适的e,求出d
    while True:
        p=GetPrime(n)
        #print(p)
        q=GetPrime(n)
        if p==q: #取不相等的素数p,q
            continue 
        N=p*q
        phi=(p-1)*(q-1)
        e=randint(65536,100000)#一般选取16位以上素数=>防止低指数攻击
        if gcd(e,phi)==1:
            d=mod_inverse(e,phi)
            return ((e, N), (d, N))
        

def RSAEP(publicKey: Key, m: int):
    e, n = publicKey
    c = mypower(m, e, n)
    return c

message = "Zhouzixin is a handsome girl.If you like her, she also like you."
message = message.encode('utf-8')
pub_key, prv_key = generateKeys(512)
print("公钥e为:"+str(pub_key[0]))
print("公钥N为"+str(pub_key[1]))
C = RSAOAEPEnc(message, pub_key)
print('加密结果为')    
print(C)

M = RSAOAEPDec(prv_key, C)
print('解密结果为')
print(M)

