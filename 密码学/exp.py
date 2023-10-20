import base64
cipher="yQQeUDxlzRvPToe631KV1vcy8DyI4e0kz7Knb9K6GIH4yP8Q32kufQvWoD7oN3hzi2EpiBxx6t/7sfIH1pCExg=="
plain=base64.b64decode(cipher).decode('unicode_escape')
result=plain[0:13]+chr(ord(plain[13])^ord("n")^ord("a"))+plain[14:]
print(base64.b64encode(result.encode('latin-1')).decode())
