from Crypto.Util.number import *
import os, random, hashlib

enc=[2741772603, 3265748928, 4143036380, 1027841819, 2514257662, 1097210779, 2378261371, 2498196396, 920739350, 3379745535, 2273781288]
x=1983594588

flag=b''
for i in range(0,11):
    high = (int(hashlib.md5(str(x).encode()).hexdigest(),16) >> 16) & (2 ** 16 - 1)
    low = x & (2 ** 16 - 1)
    result = high << 16 | low
    flag+=long_to_bytes(enc[i]^result)
    #print(long_to_bytes(enc[i]^result))
    x = int((x ** 2) // (100)) % 10001000000
print(flag)