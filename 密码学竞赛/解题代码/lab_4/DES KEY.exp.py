from Crypto.Util.number import *
c = [int(x,16) for x in open('DES key.txt', 'r').readlines()]
res=''
#print(len(c))
for i in range(len(c)):
	a=''
	bb=bin(c[i])[2:]
	for j in range(1,9):
	    a+=bb[8*j-1]
	#print(a)
	res+=a
num=int(res,2)
print(long_to_bytes(num))