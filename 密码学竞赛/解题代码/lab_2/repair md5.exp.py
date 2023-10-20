import hashlib

for i in range(32, 127):
    for j in range(32, 127):
        for z in range(32,127):
            m = hashlib.md5()  # 获取一个md5加密算法对象
            #TASC?O3RJMV?WDJKX?ZM
            m.update(str('TASC' + chr(i) +'O3RJMV'+ chr(j) + 'WDJKX'+chr(z)+'ZM').encode("utf-8"))  # 指定需要加密的字符串
            des = m.hexdigest()
            #e9032???da???08????911513?0???a2
            if 'e9032' in des and 'da' in des and '08' in des and '911513' in des and 'a2' in des :  # 如果得到的密文和我们预期的密文相同，输出
                print(des)
    