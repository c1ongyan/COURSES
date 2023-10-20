from Crypto.Util.number import *
from hashlib import sha256
from random import *
from Crypto.Cipher import DES
magic=b"2022CUMT"
def My_Hash_Plus_L(s):
    des=DES.new(s.encode(),DES.MODE_ECB)
    cl=des.encrypt(magic)
    return (cl).hex()
#assert k[:3]=='CTF'
l='a3be9fbb2169d2d5'
k='CTF@'
res1=[]
for j1 in range(32,97):
    k1=chr(j1)
    for j2 in range(32,97):
        k2=chr(j2)
        for j3 in range(32,97):
            k3=chr(j3)
            for j4 in range(32,97):
                k4=chr(j4) 
                h1=k+k1+k2+k3+k4
                res_l=My_Hash_Plus_L(h1)
                if res_l==l:
                    res1.append(h1)
print('res1=',res1)
'''
res1= ['CTF@DR@@', 'CTF@DR@A', 'CTF@DRA@', 'CTF@DRAA', 'CTF@DS@@', 'CTF@DS@A', 'CTF@DSA@', 'CTF@DSAA', 'CTF@ER@@', 'CTF@ER@A', 'CTF@ERA@', 'CTF@ERAA', 'CTF@ES@@', 'CTF@ES@A', 'CTF@ESA@', 'CTF@ESAA']
'''
