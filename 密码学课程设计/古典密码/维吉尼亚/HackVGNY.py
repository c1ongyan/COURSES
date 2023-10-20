#维吉尼亚解密：不知道密钥情况下分析密钥，求出密文(适合长密文)
#思路：1.求出密钥长度：方法可以用kasiski或者重合指数,这里用重合指数法
#重合指数法思路：爆破key长度，将一组的子串计算重合指数p^2和(近似)，每一个子串重合指数都在0.065左右的则为真实密钥长度
#2.破解密钥：根据重合互指数，爆破相对偏移
#3.求解密文:已知密钥求密文

'''
表达难点：
子串计算的处理==>直接利用字符串自带的按步长分片
重合指数的存储判断==>方法一:计算平均值判断
重合互指数需要将已满足条件的
如何判断是约等于0.065
'''
import numpy as np
import wordninja

Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getCnt(string):
#统计字符出现的频率
	LettersZd={'A':0, 'B':0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	for i in string:
		if i  in LettersZd:
			LettersZd[i]+=1

	return LettersZd

def getIC(Zd):
#计算重合指数
	fi=0
	n=0 #总数n
	for k in Zd:
		fi=fi+Zd[k]*(Zd[k]-1)
		n=n+Zd[k]

	p=fi/(n*(n-1))

	return p


def getLenKey(message):
#得到密钥长度
#方法：计算子串重合指数
	cnt=0
	pi=0
	for i in range(1,len(Letters)):
		#print('key_length=%s'%i)
		for j in range(1,i+1):
			str=message[j::i]
			LettersZd=getCnt(str)

			pi=getIC(LettersZd)
			
			if pi>0.055 and pi<0.075:
				cnt+=1
		if cnt==i:
			return i 
			break
		cnt=0
		pi=0


def getMI(str_1):
#计算子串与标准英语之间的重合互指数
	Zd_1=[0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.010,0.023,0.001,0.020,0.001] #英语中a,b,c...z的频率
	Zd_2=getCnt(str_1)

	matrix_1=np.array(Zd_1)
	matrix_2=np.array(list(Zd_2.values()))  #转成数组便于计算内积


	n2=np.sum(matrix_2)
	pi=matrix_2/n2

	Hp=np.sum(pi*matrix_1)

	return Hp



def KaiSa(key,string):
#按需偏移字符串（凯撒加密）
	result=''
	for s in string:
		index=Letters.find(s)
		result=result+Letters[(index+key)%len(Letters)]

	return result

def getListMI(num,group):
#求出num号的子串的26种偏移下的重合互指数，并返回改组中最大互指数对应的偏移
	mm=0
	result=[] #存放一组重合互指数
	for i in range(0,len(Letters)):
		string=KaiSa(i,group[num])
		x=getMI(string)
		#print(x)
		if x>mm:
			mm=x
			key=i
		result.append(x)

	return result,key




def getKey(message):
#破解密钥
	key_len=getLenKey(message)

	group=[] #按照密钥长度分组
	h_key={} #存储偏移K
	MI={} #储存偏移值
	Letter_key=''#储存字母加密密钥

	for i in range(key_len):    
	#按照密钥长度分组
		group.append(message[i::key_len])
	
	for i in range(0,key_len):  
	#求出每组的所有重合互指数和最大重合互指数对应的偏移
		MI[i],h_key[i]=getListMI(i,group)

	for i in range(key_len):     
	#根据偏移写出密钥，因为偏移是相对密文的，而密钥则是相对明文的，故要用26-相对密文的偏移
		m=Letters[(26-h_key[i])%26]
		Letter_key=Letter_key+m

	return Letter_key
	

def decrypt(key,message):

	result=''
	l=len(key)
	j=0

	for i in message:
		if i in Letters:
			index=(Letters.find(i)-Letters.find(key[j]))%26
			j=(j+1)%l
			result=result+Letters[index]
		else:
			result=result+i

	text=' '.join(wordninja.split(result))

	return text

def main():
	message='CHREE VOAHM AERAT BIAXX WTNXB EEOPH BSBQM QEQER BWRVX UOAKX AOSXX WEAHB WGJMM QMNKG RFVGX WTRZX WIAKL XFPSK AUTEM NDCMG TSXMX BTUIA DNGMG PSREL XNJEL XVRVP RTULH DNQWT WDTYG BPHXT FALJH ASVBF XNGLL CHRZB WELEK MSJIK NBHWR JGNMG JSGLX FEYPH AGNRB IEQJT AMRVL CRREM NDGLX RRIMG NSNRW CHRQH AEYEV TAQEB BIPEE WEVKA KOEWA DREMX MTBHH CHRTK DNVRZ CHRCL QOHPW QAIIW XNRMG WOIF KEE'
	message=message.replace(" ", "") #清除输入中的空格
	#print(message)
	#print(getLenKey(message))
	s=getKey(message.upper())
	print('密钥为：%s'%s)
	t=decrypt(s,message.upper())
	print('解密结果为：%s'%t)



if __name__ == '__main__':
	main()

