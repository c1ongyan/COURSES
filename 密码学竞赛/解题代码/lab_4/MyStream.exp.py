from Crypto.Util.number import *
from base64 import b64encode,b64decode
import gmpy2 as gp
m1='TestAttackCrypto'
c1=b'2ufC/wJ0kSRD1HsWjMnqfg=='
c1=b64decode(c1)
#print(len(c1))
#print(len(m1))
hh=[]
for i in range(16):
	hh.append(c1[i]^ord(m1[i]))
#print(hh)
ss=[]
s=''
for i in range(4):
	for j in range(4):
		s+=hex(hh[4*i+3-j])[2:].zfill(2)
	ss.append(int(s,16))
	s=''
#print(ss)
def s3gcd(q,w,e):
	x0=GCD(q,w)
	x0=GCD(x0,e)
	if len(bin(x0)[2:])>30:
		return x0
	else:
		return 0

flag=0
xx=ss
#xx=[2343666318, 1172635715, 1681440544, 295614965]
for a in range(2**15,2**16):
	if a&1==0:
		continue
	#print(a)
	if flag==1:
		break
	for b in range(2**15,2**16):
		if b&1==0:
			continue
		x1=a*xx[0]+b-xx[1]
		x2=a*xx[1]+b-xx[2]
		x3=a*xx[2]+b-xx[3]
		n=s3gcd(x1,x2,x3)
		if n:
			print('n:')
			print(n)
			print('a:')
			print(a)
			print('b:')
			print(b)
			flag=1
			break
'''
n:
4929631834
a:
38219
b:
51853
'''