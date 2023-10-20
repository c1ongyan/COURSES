#Affine Cipher Hacker
import gmpy2 as gp
L_m=[100, 58, 8, 93, 80, 90, 97, 121, 62, 34, 41, 83, 8, 118, 69, 114, 55, 62, 118, 69, 62, 97, 97, 118, 8, 100, 107, 41, 118, 97, 100, 48, 121, 107, 97, 48, 97, 8, 107, 107, 48, 66]

result=''
for j in range(127):
	for i in range(127):
		if gp.gcd(13,i)!=1:
			continue 
		modInverseOfKeya=gp.invert(i,127)
		for s in L_m:
			s=((s-j)*modInverseOfKeya+127)%127
			s=chr(s)
			#print(s)
			result=result+s
		if 'flag' in result:
			print(result)
		result=''