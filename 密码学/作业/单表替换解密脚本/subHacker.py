# 单表替换解密

import pprint,os,makeWordPatterns,re,copy

if not os.path.exists('wordPattern.py'): #不存在wordPattern就运行得到wordPattern
	makeWordPatterns.main()
import wordPatterns

Letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #字母表
reg=re.compile('[^A-Z\s]') #固定一个匹配模式，匹配所有不是A-Z或者空格的字符

def getBlankZd():
#返回一个空字典
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addLettersToZd(letterZd,cipherword,candidate):
#根据相同模式的单词，给出密文字母可能对应明文字母的字典
	letterZd=copy.deepcopy(letterZd) #这样才能创建一个字典副本，不然只是传的引用
	for i in range(len(cipherword)):
		if candidate[i] not in letterZd[cipherword[i]]:
			letterZd[cipherword[i]].append(candidate[i])
	return letterZd

def intersectZd(ZdA,ZdB):
#取两个字典的交集
	intersectZd=getBlankZd()
	for i in Letters:
		if ZdA[i]==[]:
			intersectZd[i]=copy.deepcopy(ZdB[i])
		elif ZdB[i]==[]:
			intersectZd[i]=copy.deepcopy(ZdA[i])
		else:
			for j in ZdA[i]:
				if j in ZdB[i]:
					intersectZd[i].append(j)
	#print(intersectZd)
	return intersectZd

def removeSolvedLettersFromZd(letterZd):
#根据
	letterZd=copy.deepcopy(letterZd)
	loopAgain=True
	while loopAgain:
		loopAgain=False

		solvedList=[]
		for i in Letters:
			if len(letterZd[i])==1:
				solvedList.append(letterZd[i][0])

		for i in Letters:
			for s in solvedList:
				if len(letterZd[i])!=1 and s in letterZd[i]:
					letterZd[i].remove(s)
					if len(letterZd[i])==1:
						loopAgain=True

	#print(letterZd)
	return letterZd

def hackSub(message):
#找出对应表
	intersectedZd=getBlankZd()

	cipherwordList=reg.sub('',message.upper()).split()
	#print(cipherwordList)

	for i in cipherwordList:
		newZd=getBlankZd()

		wordPattern=makeWordPatterns.getPattern(i)
		if wordPattern not in wordPatterns.allPatterns:
			continue 
		for j in wordPatterns.allPatterns[wordPattern]:
			newZd=addLettersToZd(newZd,i,j)
			#print(newZd)
		intersectedZd=intersectZd(intersectedZd,newZd)

	return removeSolvedLettersFromZd(intersectedZd)

def desiglesub(key, message):
#根据替换关系解密
	result=''
	for i in message:
		if i.upper() in key:
			index=key.find(i.upper())
			if i.isupper():
				result=result+Letters[index].upper()
			else:
				result=result+Letters[index].lower()
		else:
			result=result+i

	return result



def decrypt(ciphertext,letterZd):
#生成密钥，解密
	key=['x']*len(Letters)
	for i in Letters:
		if len(letterZd[i])==1:
			keyIndex=Letters.find(letterZd[i][0])
			key[keyIndex]=i
		else:
			ciphertext=ciphertext.replace(i.lower(),'_')
			ciphertext=ciphertext.replace(i.upper(),'_')
	key=''.join(key)

	return desiglesub(key,ciphertext)

def main():
	message='YKHLBA JCZ SVIJ JZB LZVHI JCZ VHJ DR IZXKHLBA VSS RDHEI DR YVJV LBXSKYLBA YLALJVS IFZZXC CVI LEFHDNZY EVBTRDSY JCZ FHLEVHT HZVIDB RDH JCLI CVI WZZB JCZ VYNZBJ DR ELXHDZSZXJHDBLXI JCZ XDEFSZQLJT DR JCZ RKBXJLDBI JCVJ XVB BDP WZ FZHRDHEZY WT JCZ EVXCLBZ CVI HLIZB YHVEVJLXVSST VI V HZIKSJ DR JCLI JCVJ PZHZ DBXZ XDBILYZHZY IZXKHZ VHZ BDP WHZVMVWSZ '
	print("Hacking")
	print("根据字母模式匹配得到的替换表：")
	keyZd=hackSub(message)
	pprint.pprint(keyZd)
	hackedM=decrypt(message,keyZd)
	print("最终破解出来的密文：")
	print(hackedM)

if __name__ == '__main__':
	main()















