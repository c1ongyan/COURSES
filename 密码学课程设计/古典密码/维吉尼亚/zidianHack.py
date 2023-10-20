import detectEnglish,wordninja

Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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


def Hack(message):

	fo=open('dictionary.txt','r')
	words=fo.readlines()    #返回一个字符串列表，每个字符串是文件的一行
	fo.close()

	#开始爆破
	for word in words:
		word=word.strip()
		st=decrypt(word,message)

		#message=message.replace(" ", "") #清除输入中的空格
		#print(st)
		if detectEnglish.isEnglish(st,wordPercentage=40):
			print("密钥可能为%s"%word)
			print("对应明文可能为%s"%st)


def main():
	message='CHREE VOAHM AERAT BIAXX WTNXB EEOPH BSBQM QEQER BWRVX UOAKX AOSXX WEAHB WGJMM QMNKG RFVGX WTRZX WIAKL XFPSK AUTEM NDCMG TSXMX BTUIA DNGMG PSREL XNJEL XVRVP RTULH DNQWT WDTYG BPHXT FALJH ASVBF XNGLL CHRZB WELEK MSJIK NBHWR JGNMG JSGLX FEYPH AGNRB IEQJT AMRVL CRREM NDGLX RRIMG NSNRW CHRQH AEYEV TAQEB BIPEE WEVKA KOEWA DREMX MTBHH CHRTK DNVRZ CHRCL QOHPW QAIIW XNRMG WOIF KEE.'
	message=message.replace(" ","")
	Hack(message.upper())

if __name__ == '__main__':
	main()