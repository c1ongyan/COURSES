#已知密钥解密维吉尼亚
import wordninja

Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(key,message):

	result=''
	l=len(key)
	key_all=key*(len(message)//l)
	j=0 #密钥指针

	for i in message:
		index=(Letters.find(i)+key[j])%26
		j+=1
		result=result+Letters[index]

	return result

def decrypt(key,message):

	result=''
	l=len(key)
	j=0

	for i in message:
		index=(Letters.find(i)-Letters.find(key[j]))%26
		j=(j+1)%l
		result=result+Letters[index]

	text=' '.join(wordninja.split(result))

	return text



def main():
	while True:
		mode=input("加密输入e,解密输入d,退出输入0\n")
		if mode=='e':
			message=input("输入要加密的文本:\n")
			key=input("输入密钥:\n")
			res=encrypt(key,message.upper())
			print("加密后的结果为:"+str(res))
		elif mode=='d':
			message=input("输入要解密的文本\n")
			key=input("输入密钥\n")
			res=decrypt(key,message.upper())
			print("解密后的结果为:"+str(res))
		elif mode=='0':
			break

	'''
	message='krkpewxvftksopztecxvbuhfvycgxouflihoffptrcwffwhkcevxhiuzfposdvccyctpmjtbfymllctiwxtacsmjmoncwdnawjrwtjgjsuystvbxgvcmgczbqecllttfkjlacpfttjgeegtbvkfpmhjzqaxhvvpgxoeychrcwumchhyigixhqdciawunmjerefkekcozqttznfdjlopuyqhjgrjawcpfrgxhwiljgrgiycrqkiajfgvrlrxgkkghdbqnliaovzrltgafslacjvjexrwjrdzsvruprttfkwxfgrlstznnmjerdvjdlhkwwdngjfsawgjfunhitjcaykgrptzicibtwrcpycwbkxfibrqemivotvwdnotvldmvgicshbqkztmfqlzaxrqekntqefscmbqkfxguyzjaaorgccmcovrwxbckgdgonrqhxadcclbznjfdpzgegtgqawygxkgcjiasofqiecxvbdyageztjikvrxymqlapghcbcrtfgfdnhitjcaytqiknlsnwgrtbpfrlkwvvycraqicqnhpfrwbbizliasyfpawqqljslhqgktmccumgxmqlsemcvycsxovy'
	key='CRYPTO'
	print(decrypt(key,message.upper()))
	'''

if __name__ == '__main__':
	main()