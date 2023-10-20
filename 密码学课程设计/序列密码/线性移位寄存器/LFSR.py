#如何实现在特定位异或->用一个列表存放为参与异或的位数，将这个值作为索引找到当前寄存器序列中参与异或的值
#最后需要得到输出一个周期的序列(output)和周期数（output元素个数）
#1000000000010110 0000000000000001 1110001011110110

bitxor=[]  #存放参与异或的位数

def FeedBack(cache):#cache 寄存器字符串序列，bitxor 参与异或的位数(下标)——》
	#反馈函数->得到新加入的数
	res_xor=0     #反馈函数的结果
	for i in bitxor:
		res_xor=int(cache[i])^res_xor
	return res_xor

def LFSR(key,start):
	s_k=key #可约多项式序列 确定反馈函数参与异或位数
	
	for i in range(len(s_k)):
		if s_k[i]=='1':
			bitxor.append(i)

	s_0=start  #初始序列 右端为输出
	s_len=len(s_0)
	s_i=s_0 #现在寄存器状态

	output=[]       #存放每次是输出

	S_history=[]    #存放每一次在寄存器中的序列，用于判断周期结束
	S_history.append(s_0)
	T=0              #内循环周期数
	T_Max=0          #最大周期数
	Sb=0    #哨兵，重复的标志

	while True:
		tmp=str(FeedBack(s_i))
		output.append(s_i[-1:])
		s_i=tmp+s_i[:-1]

		if s_i==s_0:
			#print("周期结束")
			T_Max=len(output)
			T=T_Max
			Sb=1

		for i in range(len(S_history)-1): #如果当前序列与历史状态的序列有相同，表示周期结束，停止循环
			if s_i==S_history[i+1]:
				Sb=1
				#print("构成内循环，周期结束"+str(i)+':'+S_history[i+1])
				T=len(S_history)-(i+1)
				T_Max=len(output)
				break

		if Sb!=0:
			break
		
		S_history.append(s_i)

	return output,S_history,T_Max,T

def main():
	'''
	key='0110111101000111' #0110111101000111  
	start='0101010101010101' 
	output,S_history,t_max,t=LFSR(key,start)
	print(output)
	print(S_history)
	print('最大周期数为：'+str(t_max)+'    内循环周期数为：'+str(t))
	for i in range(len(output)):
		print('第'+str(i)+'次循环')
		print('当前寄存器序列为:'+S_history[i]+'    输出值为：'+output[i])
	

	'''
	while True:
		key=input('请输入对应反馈函数的可约多项式序列逆序(如0110111101000111):\n')
		start=input('请输入寄存器初始化序列(如0101010101010101):\n')
		if len(key)>len(start):
			print('错误：可约多项式序列过长！')
			continue
		output,S_history,t_max,t=LFSR(key,start)
		print('周期序列为：')
		print(''.join(output))
		print('最大周期数为：'+str(t_max)+'    内循环周期数为：'+str(t))
		mode_1=input('是否查看详细过程 y or n \n')
		if mode_1=='y':
			for i in range(len(output)):
				print('第'+str(i)+'次循环')
				print('当前寄存器序列为:'+S_history[i]+'    输出值为：'+output[i])
		mode_2=input('重新输入请输入y,结束请输入n\n')
		if mode_2=='n':
			break

	



if __name__ == '__main__':
	main()

				
	






	
