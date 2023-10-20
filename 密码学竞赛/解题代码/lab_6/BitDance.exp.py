from Crypto.Util.number import *
def de1(x):
	x&=0xffffffff
	tmp=x
	res1=tmp&(2**8-1)
	#print(res1)
	res2=res1^((tmp&(2**16-1))>>8)
	#print((tmp&(2**16-1))>>8)
	res3=res2^((tmp&(2**24-1))>>16)
	res4=res3^(tmp>>24)
	res_f=(res4<<24)|(res3<<16)|(res2<<8)|res1
	return res_f
def de2(x):
	x&=0xffffffff
	x=(x>>18)|(x<<14)
	x&=0xffffffff
	return x
def de3(x):
	x&=0xffffffff
	tmp=x
	res1=(tmp>>17)
	res2=((tmp>>2)&(2**15-1))^res1
	res3=(tmp&(2**2-1))^(res2>>13)
	res_f=(res1<<17)|(res2<<2)|res3
	return res_f
def de4(x):
	tmp=x
	res1=tmp&(2**17-1)
	res2=(tmp>>17)^(res1&(2**15-1))
	res_f=(res2<<17)|res1
	return res_f
def decrypt(x):
	return de4(de3(de2(de1(x))))

enc=[3188477616, 3086410, 2064398162, 3417626223, 3420114310, 3339741026, 4212574670, 1627596168, 1216621608, 4236761464, 4080586276]
m=[decrypt(i) for i in enc]
res=''
for s in m:
	tmp=long_to_bytes(s)
	tmp=list(tmp)
	tmp.reverse()
	for i in range(4):
		res+=chr(tmp[i])
print(res)







