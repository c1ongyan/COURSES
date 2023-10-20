from hashlib import *
res='11010111100111101110111101100100'
print(sha256(str(int(res,2)).encode()).hexdigest())
