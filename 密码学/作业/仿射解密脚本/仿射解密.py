#Affine Cipher Hacker
import math,sys,detectEnglish,wordninja
from gmpy2 import invert

englishLetterFrea={'E':12.7,'T':9.06,'A':8.17,'O':7.51,'I':6.97,'N':6.75,'S':6.33,'H':6.09,'R':5.99,'D':4.25,'L':4.03,'C':2.78,'U':2.76,'M':2.41,'W':2.36,'F':2.23,'G':2.02,'Y':1.97,'P':1.93,'B':1.29,'V':0.98,'K':0.77,'J':0.15,'X':0.15,'Q':0.10,'Z':0.07}


ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'  #英文中词频排列顺序（降序）

Symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #明文空间 密文空间

def getLetterCount(message):

#统计字符串中每个字母的数量
	LetterCount={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

	for i in message.upper():
		if i in Symbols:
			LetterCount[i]+=1
	
	return LetterCount



def getItemAtIndexZero(x):
#返回变量的下标为0的值
	return x[0]

def getFrequencyOrder(message):
#按照字母出现的次数排序
	letterToFreq=getLetterCount(message) #字母到次数的映射
	freqToLetter={} #次数到字母的映射

	for i in Symbols:          
		if letterToFreq[i] not in freqToLetter:   #判断字母对应次数是否是字典freqToLetter的键，若不是则以该次数为键，以对于的字母为值；若是，则在最后追加一组键值对
			freqToLetter[letterToFreq[i]]=[i]     #因为次数可能出现相同的情况
		else:
			freqToLetter[letterToFreq[i]].append(i)

	for freq in freqToLetter:
		freqToLetter[freq].sort(key=ETAOIN.find,reverse=True)  #将同一次数的键所对应的字母按照ETAOIN的降序排列(做一个约定)
		freqToLetter[freq]=''.join(freqToLetter[freq])

	freqPairs=list(freqToLetter.items())                 #将字典变成一个元组列表
	freqPairs.sort(key=getItemAtIndexZero,reverse=True)  #按照元组列表索引为0的值排序

	return freqPairs




def getKey(key):
	#得到两个ab密钥
	key_a=key//len(Symbols)
	key_b=key%len(Symbols)
	return (key_a,key_b)

def checkKeys(key_a,key_b,mode):
	#检查密钥是否合法
	if mode=='encrypt':
		if key_a==1 or key_b==1:
			sys.exit('太简单')
	if key_a<0 or key_b<0 or key_b>len(Symbols)-1:
		sys.exit('不属于区间(0,len(Symbols))')
	if math.gcd(key_a,len(Symbols))!=1:
		sys.exit('密钥a和模数不互素')

def decryptM(key,message):
	#已知密钥的仿射解密
	K1,K2=getKey(key)
	checkKeys(K1,K2,'decrypt')
	result=''
	modInverseOfKeya=invert(K1,len(Symbols))    #求密钥a的模逆元

	for i in message:
		if i in Symbols:
			Index=Symbols.find(i)
			result+=Symbols[((Index-K2)*modInverseOfKeya)%len(Symbols)]
		else:
			result+=i

	return result

def hackAffine(message):  
#爆破得到明文
	cnt=0 #最后输出的可能解密结果数

	Max=getFrequencyOrder(message)[0][1]

	for i in message:
		if i==Max:
			ind = message.find(i)   #找到E所在的位置
			break
#                  
	print('hacking start')

	for key in range(len(Symbols)**2):   #爆破密钥
		key_a=getKey(key)[0]
		if math.gcd(key_a,len(Symbols))!=1:  #密钥a要和模数互素
			continue

		result=decryptM(key,message)  #将密钥带入根据公式求出对应明文

		if result[ind]=='E':
			#print('tried key %s...(%s)'%(key,result[:20]))
			text=' '.join(wordninja.split(result))  #利用wordninja工具给字符串分词，这样才能用detectEnglish判断是否是英文
			if detectEnglish.isEnglish(text):    #利用detectEnglish判断是否是英文
				cnt+=1
				print('possible encryption hack:')
				print('key:%s'%(key))
				print('c:'+result[:50])
				print(text)                      #输出最后可能结果
	return cnt

def main():
	Message='FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH'  # 输入密文

	HackedM=hackAffine(Message)

	if HackedM!=0:           #如果最后测得的可能解不为0，则成功解密
		print('Success')
	else:
		print('Failed')

if __name__=='__main__':
	main()