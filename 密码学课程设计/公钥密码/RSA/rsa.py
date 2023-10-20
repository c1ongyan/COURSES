import sys
import math
from random import randint 
import libnum

def gcd(a, b):
	#辗转相除法求最大公因数
    if a > b: a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

def ExtGcd(a,b):
	#扩展欧几里得算法 用辗转相除法计算a,b的最大公因子gcd(a,b),倒推求出满足xa+yb=gcd(a,b)的x,y
	if b==0:
		return 1,0,a #x,y,gcd(a,b)
	else:
		x,y,g=ExtGcd(b,a%b)
		x,y=y,(x-(a//b)*y)
		return x,y,g

def ModInverse(a,m):
	#求a模n的逆元b 即a*b=1(mod m)  
	x,y,g=ExtGcd(a,m) #ax+my=1 ==>ax=1(mod m)
	if g!=1:
		print(str(a)+'不可逆')
	else:
		return x%m
'''
def MyPow(a,n,m):
	#实现a的n次幂模m
	#n==>2进制串AiAi-1...A0==>2^i*Ai+2^(i-1)*Ai-1+...+2^0*(A0)
	#a^n==>a^(2^i*Ai+2^(i-1)*Ai-1+...+2^0*(A0))
	a=a%m
	result=1
	while n!=0:
		if n&1:
			result=(result*x)%m
		n=n>>1
		a=(a*a)%m
	return result
'''
def primality_testing(n, k):
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
'''
def GetPrime(n):
	#得到一个n位的素数
	while True:
		n=randint(n)
		if primality_testing(n,10):
			pass
		else:continue
		return n
'''
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
		if primality_testing(num,10):
			return num

def GetKey(n):
	#获取位数为n的p,q 并选取合适的e,求出d
	while True:
		p=GetPrime(n)
		q=GetPrime(n)
		if p==q: #取不相等的素数p,q
			continue 
		N=p*q
		phi=(p-1)*(q-1)
		e=randint(65536,100000)#一般选取16位以上素数=>防止低指数攻击
		if gcd(e,phi)==1:
			d=ModInverse(e,phi)
			return e,N,d 



def encrypt(m,e,N):
	return pow(m,e,N)

def decrypt(c,d,N):
	return pow(c,d,N)

def main():

	while True:
		mode=input("加密输入e,解密输入d,退出输入0\n")
		if mode=='e':
			message=input("输入明文:\n")
			n=input("输入密钥位数:\n")
			n=int(n)
			m=libnum.s2n(message)
			e,N,d=GetKey(n)
			c=encrypt(m,e,N)
			print("公钥e为:"+str(e))
			print("公钥N为:"+str(N))
			print("私钥d为:"+str(d))
			print("密文为(10进制):"+str(c))

		elif mode=='d':
			c=input("输入密文(10进制):\n")
			d=input("输入私钥d:\n")
			N=input("输入公钥N:\n")
			c=int(c)
			d=int(d)
			N=int(N)
			c=decrypt(c,d,N)
			c=libnum.n2s(c)
			print("密文为:"+str(c))

		elif mode=='0':
			break

if __name__ == '__main__':
	main()





	




