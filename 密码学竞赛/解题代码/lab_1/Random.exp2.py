import hashlib
ccc=3305128028>>16
qqq=3305128028& (2 ** 16 - 1)
for num in range(0,10001000000):#1983594588
    high = (int(hashlib.md5(str(num).encode()).hexdigest(),16) >> 16) & (2 ** 16 - 1)
    if (high == ccc) and (num & (2 ** 16 - 1)==qqq):   
        print(str(num)) #等待执行结束 输出结果
