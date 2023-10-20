import numpy as np

Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def strToArr(string):
#字符串转成数组
	numList=[]

	for s in string:
		numList.append(ord(s))

	Array=np.array(numList)

	return Array

def ListToStr(List):
#列表数子为字符
	result=''

	for i in List:
		result=result+chr(i)

	return result

def mul_mod_inv(x):
# 在模26下求一个数x的乘法逆元y，只需要满足(x×y) mod 26 = 1
# y的取值范围为[0,26)
	x=round(x%127,0)
	y = 0
	while(y < 127):
		res = (x * y) % 127
		if res == 1:
			return y
			break
		else:
			y = y + 1
			if y == 127:
				print(x,"在模127下，不存在乘法逆元!")

def encrypt(message,m,key):
#Hill加密
	result='' #储存加密后的字符串
	m_arr=np.array(message)
	#m_arr=strToArr(message)    #将明文变成int型一维数组
	#print(m_arr)
	m_arr=m_arr.reshape(-1,m)  #将数组变成m列的向量
	#print(m_arr)
	c_arr=(np.matmul(m_arr,key))%127   #加密

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
	k_2=k_1*k_det%127  #矩阵的逆乘行列式=伴随矩阵
	k_2=np.around(k_2) 
	k_2=k_2.astype(np.int64)#浮点型转int型
	k_3=k_det_inv*k_2%127 #行列式的乘法逆元乘上伴随矩阵得到整数逆元
	k_3=np.around(k_3)  # 由于伴随矩阵得到的可能是浮点数矩阵，故需要对其进行四舍五入取整
	k_3=k_3.astype(np.int64)  # 并将每个元素成员强制转换为int类型

	return k_3
def decrypt(c,m,key):
	k_3=matrix_inv(key)#行列式的乘法逆元乘上伴随矩阵得到整数逆元
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
	key_arr=(np.matmul(p_inv,c_arr))%127
	return key_arr

def main():
	p='flag'
	c=[98, 86, 15, 3]
	cc=''
	for i in range(4):
		cc+=chr(c[i])
	m=2
	print("明文:"+p+" 与密文: "+cc+" 加密密钥为：")
	hac=hackKey(p,cc,m)
	print(hac)
	message=[98, 86, 15, 3, 88, 7, 70, 66, 88, 90, 59, 75, 45, 51, 10, 110, 64, 68, 12, 125, 23, 54, 45, 51, 119, 86, 116, 104, 96, 109, 14, 106, 118, 85, 112, 108, 32, 30, 39, 53, 47, 22]
	res=''
	key=np.array([[20 ,22],
 [22 ,20]],dtype=int)
	m=2
	de=decrypt(message,m,key)
	print(de)
if __name__ == '__main__':
	main()
