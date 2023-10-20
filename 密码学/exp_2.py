import base64
cipher="wRPT3VONV2zFV6D2PbHjIm1lIjtzOjU6ImFkbWluIjtzOjg6InBhc3N3b3JkIjtzOjU6IjEyMzQ1Ijt9"
plain=base64.b64decode(cipher).decode('unicode_escape')
oldiv=base64.b64decode("uxrq4TtskqrNJh7JUZV9rg==").decode('unicode_escape')
one='a:2:{s:8:"userna'
iv=""
for i in range(0,16):
     iv=iv+chr(ord(one[i])^ord(plain[i])^ord(oldiv[i]))
print(base64.b64encode(iv.encode('latin-1')).decode())#GzMLBhOS//4yU8tMCVbw7Q==
