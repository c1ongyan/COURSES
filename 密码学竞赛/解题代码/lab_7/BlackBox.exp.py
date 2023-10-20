cipher='25 1e 18 17 0f 5a 25 14 1b 49 42 0d 26 5f 1f 41 12 59 6e 46 4b 40 12 42 21 17 49 44 59 0d 22 43 41 11 4d 5c 71 17 4e 47 11 12'
cipher=cipher.split(' ')
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
setC='22 13 18 11 15 0e 22 13 18 11 15 0e 22 13 18 11 15 0e 22 13 18 11 15 0e 22 13 18 11 15 0e 22 13 18 11 15 0e 22 13 18 11 15 0e'
setC=setC.split(' ')
key=[]
for i in range(42):
	tmp=int(setC[i],16)^ord('a')
	key.append(tmp)
#print(key)
res=''
for i in range(42):
	tmp=int(cipher[i],16)^key[i]
	tmp=chr(tmp)
	res+=tmp
print(res)