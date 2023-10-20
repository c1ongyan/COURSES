from Crypto.Util.number import *
f= lambda x : (x<<3|x>>5)&0xff
def decrypt(m,key):
    s=[]
    t=[]
    out=[] #putput
    for i in range(256):
        s.append(255-i)#s[]=[255,254,...,0]
        t.append(ord(key[i%len(key)]))
    j=0
    for i in range(256):
        j=(j+s[i]+t[i])%256
        s[i],s[j]=s[j],s[i]

    i,j=0,0
    for p in range(len(m)):
        i=(i+1)%256
        j=(j+s[i])%256

        s[i],s[j]=s[i],s[j]

        index=(s[i]+s[j])%256
        out.append(s[index]^f(m[p]))
    return bytes(out)
key="StreamCipherRCFour"
enc=0x3baf815ae9aa87513ceb82474a80ac13bca64f723d594622fcdaf7fef08987da278c676eb8cb17b655c0
enc=int(enc).to_bytes(42,byteorder='big')
'''
for i in range(42):
	tmp=enc[i]
	high=tmp&(2^5-1)<<3
	low=tmp>>5
	tmp=high|low#tmp=(tmp<<3|tmp>>5)&0xff
'''
res=decrypt(enc,key)
print(res)

