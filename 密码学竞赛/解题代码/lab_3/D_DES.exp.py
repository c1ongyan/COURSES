import gmpy2 as gp
from Crypto.Util.number import *
from Crypto.Cipher import DES
import sympy
g= 3766405567
p= 15598130864496243067
c= 13012006854898403582
enc=[231, 126, 194, 130, 178, 221, 226, 233, 245, 96, 156, 223, 12, 102, 97, 0, 82, 232, 211, 6, 115, 170, 144, 117, 59, 8, 217, 30, 79, 1, 7, 106, 65, 66, 47, 232, 59, 119, 63, 79, 192, 25]
mm=''
for i in range(42):
	mm+=chr(enc[i])
#mm=long_to_bytes(int(mm))
x=sympy.discrete_log(p,c,g)
#x=3459082537
k=long_to_bytes(x)*2
#print(len(k))
res=''
for i in range(0,len(mm),8):
    buf=mm[i:i+8]
    des=DES.new(k,DES.MODE_ECB)
    k=des.encrypt(k)
    for j in range(len(buf)):
        res+=chr(ord(buf[j])^k[j])

print(res)
