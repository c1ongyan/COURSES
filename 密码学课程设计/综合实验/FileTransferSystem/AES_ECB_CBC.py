#pkcs7填充
#ECB CBC模式加密

import AES_128 as aes


def ECBEncrypt(message,key):

	#调整输入格式
	m=aes.StrToBinList(message)
	if len(key)<=16:
		k=aes.StrToBinList(key)
	else:
		print('密钥长度超出128bit,取前128bit加密')
		k=aes.StrToBinList(key)[:4]

	result=''

	for i in range(len(m)//4):
		mix=aes.StreamListToMix(m[4*i:4*i+4])
		res_mix=aes.encrypt(mix,k)
		tmp=aes.MixToStr(res_mix)
		result+=tmp

	result=aes.StrToBase64(result)
	return result

def ECBDecrypt(message,key):

	#调整输入格式
	m=aes.Base64ToStr(message)
	#print(m)
	m=aes.StrToBinList(m)
	#print(m)
	if len(key)<=16:
		k=aes.StrToBinList(key)
	else:
		print('密钥长度超出128bit,取前128bit解密')
		k=aes.StrToBinList(key)[:4]

	result=''

	for i in range(len(m)//4):
		#print(m[4*i:4*i+4])
		#print(k)
		mix=aes.StreamListToMix(m[4*i:4*i+4])
		res_mix=aes.decrypt(mix,k)
		tmp=aes.MixToStr(res_mix)
		result+=tmp

	return result

def CBCEncrypt(message,key,iv):

	#调整输入格式
	m=aes.StrToBinList(message)
	if len(key)<=16:
		k=aes.StrToBinList(key)
	else:
		print('密钥长度超出128bit,取前128bit加密')
		k=aes.StrToBinList(key)[:4]
	if len(iv)<=16:
		iv=aes.StrToBinList(iv)
	else:
		print('IV超出128bit,取前128bit加密')
		iv=aes.StrToBinList(iv)[:4]
	
	result=''
 
	iv_mix=aes.StreamListToMix(iv) #初始化向量矩阵


	for i in range(len(m)//4):
		mix=aes.StreamListToMix(m[4*i:4*i+4])
		mix=iv_mix^mix
		res_mix=aes.encrypt(mix,k)
		tmp=aes.MixToStr(res_mix)
		iv_mix=res_mix
		result+=tmp

	result=aes.StrToBase64(result)
	return result

def CBCDecrypt(message,key,iv):
	
	#调整输入格式
	m=aes.Base64ToStr(message)
	#print(m)
	m=aes.StrToBinList(m)
	#print(m)
	if len(key)<=16:
		k=aes.Str2ToBinList(key)
	else:
		print('密钥长度超出128bit,取前128bit解密')
		k=aes.Str2ToBinList(key)[:4]
	if len(iv)<=16:
		iv=aes.Str2ToBinList(iv)
	else:
		print('IV超出128bit,取前128bit解密')
		iv=aes.Str2ToBinList(iv)[:4]
	
	result=''
	
	iv_mix=aes.StreamListToMix(iv) #初始化向量矩阵


	for i in range(len(m)//4):
		mix=aes.StreamListToMix(m[4*i:4*i+4])
		res_mix=aes.decrypt(mix,k)
		res_mix=iv_mix^res_mix
		tmp=aes.MixToStr(res_mix)
		iv_mix=mix
		if i==len(m)//4-1:
			tmp=aes.delnullbyte(tmp)
		result+=tmp
	return result

'''
m=ECBEncrypt('chongyanisyyds','auefawifs')
print(m)
print(ECBDecrypt(m,'auefawifs'))

m=CBCEncrypt('chongyanisyyds','auefawifs','sacsfdvsv')
print(m)
print(CBCDecrypt(m,b'auefawifs',b'sacsfdvsv'))
'''

def main():
	print("---AES_128bit ECB与CBC模式加密 明文密钥初始化向量不足均填充0---")
	mode=input('加密输入e,解密输入d,退出输入0\n')
	while mode!='0':      
		if mode=='e':
			mode_2=input('ECB模式输入1,CBC模式输入2,退出输入0\n')
			if mode_2=='1':
				plain=input('输入明文(格式是字符串，如：chongyanisyyds)：\n')
				key=input('输入密钥(格式是字符串，如：auefawifs)：\n')
				m=ECBEncrypt(plain,key)
				print('密文(格式为base64)=',m)
			if mode_2=='2':
				plain=input('输入明文(格式是字符串，如：chongyanisyyds)：\n')
				key=input('输入密钥(格式是字符串，如：auefawifs)：\n')
				iv=input('输入IV(格式是字符串，如：sacsfdvsv)：\n')
				m=CBCEncrypt(plain,key,iv)
				print('密文(格式为base64)=',m)
			if mode=='0':
				break

		if mode=='d':
			mode_2=input('ECB模式输入1,CBC模式输入2,退出输入0\n')
			if mode_2=='1':
				cipher=input('输入密文(格式是base64，如：wpjDgMObw4MRwqrDlkbDjcKlEcKOT8Kpwo1u)：\n')
				key=input('输入密钥(格式是字符串，如：auefawifs)：\n')
				plain=ECBDecrypt(cipher,key)
				print('明文=',plain)
			if mode_2=='2':
				cipher=input('输入密文(格式是base64，如：CMKiwpZawppRVsOsNRF4HcOwODLDhA==)：\n')
				key=input('输入密钥(格式是字符串，如：auefawifs)：\n')
				iv=input('输入IV(格式是字符串，如：sacsfdvsv)：\n')
				plain=CBCDecrypt(cipher,key,iv)
				print('明文=',plain)
			if mode=='0':
				break
		if mode=='0':
			break
		
		mode=input('加密输入e,解密输入d,结束输入0\n')


if __name__ == '__main__':
	main()

