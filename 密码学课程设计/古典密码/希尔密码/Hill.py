import numpy as np

Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def strToArr(string):
#字符串转成数组
	numList=[]
	string=string.upper()

	for s in string:
		index=Letters.find(s)
		numList.append(index)

	Array=np.array(numList)

	return Array

def ListToStr(List):
#列表数子为字符
	result=''

	for i in List:
		result=result+Letters[i]

	return result

def mul_mod_inv(x):
# 在模26下求一个数x的乘法逆元y，只需要满足(x×y) mod 26 = 1
# y的取值范围为[0,26)
	x=round(x%26,0)
	y = 0
	while(y < 26):
		res = (x * y) % 26
		if res == 1:
			return y
			break
		else:
			y = y + 1
			if y == 26:
				print(x,"在模26下，不存在乘法逆元!")

def encrypt(message,m,key):
#Hill加密
	result='' #储存加密后的字符串

	m_arr=strToArr(message)    #将明文变成int型一维数组
	#print(m_arr)
	m_arr=m_arr.reshape(-1,m)  #将数组变成m列的向量
	#print(m_arr)
	c_arr=(np.matmul(m_arr,key))%len(Letters)    #加密

	c_arr=c_arr.reshape(-1)  #将结果变为一维数组 
	c_arr=np.around(c_arr)
	c_arr=c_arr.astype(int)
	c_list=c_arr.tolist()    
	#print(c_list)
	result=ListToStr(c_list)  #将列表中的数字转成对应字母

	return result

def matrix_inv(key):
	#整数域上求矩阵逆元
	k_1=np.linalg.inv(key) # 求key的逆矩阵，但由于其不是整数，故通过行列式的乘法逆元乘上伴随矩阵得到整数逆元
	k_det=np.linalg.det(key) #求key矩阵的行列式
	k_det_inv=mul_mod_inv(k_det) #求行列式模26的乘法逆元 本质上是1/|A|
	k_2=k_1*k_det%len(Letters)  #矩阵的逆乘行列式=伴随矩阵
	k_2=np.around(k_2) 
	k_2=k_2.astype(np.int64)#浮点型转int型
	k_3=k_det_inv*k_2%26 #行列式的乘法逆元乘上伴随矩阵得到整数逆元
	k_3=np.around(k_3)  # 由于伴随矩阵得到的可能是浮点数矩阵，故需要对其进行四舍五入取整
	k_3=k_3.astype(np.int64)  # 并将每个元素成员强制转换为int类型

	return k_3

def decrypt(c,m,key):
	k_3=matrix_inv(key)#行列式的乘法逆元乘上伴随矩阵得到整数逆元
	print("解密密钥为")
	print(k_3)
	return encrypt(c,m,k_3) 

def hackKey(p,c,m):
	if len(p)<m*m:
		print('数据过少不可爆破密钥')
		return False
	p_arr=strToArr(p[:m*m])
	#print(p_arr)
	p_arr=p_arr.reshape(-1,m)
	c_arr=strToArr(c[0:m*m])
	c_arr=c_arr.reshape(-1,m)
	p_inv=matrix_inv(p_arr)
	key_arr=(np.matmul(p_inv,c_arr))%len(Letters) 
	return key_arr



def main():
	message='hill'
	print("此次加密的明文为"+message)
	key=np.array([[8,6,9,5],
				[6,9,5,10],
				[5,8,4,9],
				[10,6,11,4]],dtype=int)
	m=4
	c=encrypt(message.upper(),m,key)
	p=decrypt(c,m,key)
	print("加密后的密文为"+c)
	print("对密文解密后的明文为"+p)
	p='friday'
	c='POCFKU'
	m=2
	print("明文:"+p+" 与密文: "+c+" 加密密钥为：")
	hac=hackKey(p.upper(),c.upper(),m)
	print(hac)
	print("用求解出的密钥加密"+p+"结果为")
	print(encrypt(p.upper(),m,hac))

if __name__ == '__main__':
	main()








