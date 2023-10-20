from Crypto.Util.number import *
from hashlib import sha256
from random import *
res_sha='c4558413cfcfaaa24183a94fc245990b44b9585080f234fa6d89aaedbba08981'
res1= ['CTF@DR@@', 'CTF@DR@A', 'CTF@DRA@', 'CTF@DRAA', 'CTF@DS@@', 'CTF@DS@A', 'CTF@DSA@', 'CTF@DSAA', 'CTF@ER@@', 'CTF@ER@A', 'CTF@ERA@', 'CTF@ERAA', 'CTF@ES@@', 'CTF@ES@A', 'CTF@ESA@', 'CTF@ESAA']
res=[]
for s in res1:
	L=s[:3]
	R=s[4:]
	res.append(L+R+'@'*7)
#print(res)
for s in res:
	tmp=sha256(s.encode()).hexdigest()
	if tmp==res_sha:
		k=s
#print(k)
enc=[35, 33, 208, 39, 70, 31, 18, 191, 171, 111, 97, 116, 149, 159, 117, 119, 182, 28, 120, 129, 196, 229, 20, 241, 245, 207, 120, 108, 206, 159, 13, 219, 230, 119, 157, 38, 15, 180, 75, 228, 100, 247]
seed(k[:5])
m=[enc[i]^getrandbits(8) for i in range(len(enc))]
flag=''
for i in range(len(m)):
	flag+=chr(m[i])
print(flag)

