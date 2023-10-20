import gmpy2
from Crypto.Util.number import *
from randcrack import RandCrack
n1=219877546370517990751590059202563484101
P1= 14697342479840190421
P2= 14960360804826860081
phi1=(P1-1)*(P2-1)
e=0x10001
d1=gmpy2.invert(e,phi1)
with open(r'test', 'r') as f:
    l = f.readlines()
l = [int(i.strip()) for i in l]
t = []
for i in range(len(l)):
    l[i]=pow(l[i],d1,n1)
    t.append(l[i] & (2 ** 32 - 1))
    t.append(l[i] >> 32)

rc = RandCrack()
for i in t:
    #print(i)
    rc.submit(i)

p= gmpy2.next_prime(rc.predict_getrandbits(1024))
q=gmpy2.next_prime(rc.predict_getrandbits(1024))
phi=(p-1)*(q-1)
e=0x10001
d=gmpy2.invert(e,phi)
n=282192787045300012512653348205023100633977961994319785455334878485878279155002597477586988139884708984967932299592184370913920154454529411340214002000184203858663348493798685214382285918768428977731739212686497807723945591897144193648675116590231356660052801887629464918391922154136991319586559816540237338585497480469612503603415205364509226801281944738737389838935248786451046766991788078169921109893699568857037445013576217368707802159332844126239428388993459172642776613311083103371374305339933633675017290937043850137562211032613075733292432423304470749812237194900717702085370608137840991471631835910828039687
m=259238822988977566695012424617063995573117089930208556670657599145025337427702878466226185238420864305947007012310554910092798322465348131913436133467234016346494141355781195340465361281577893230222262078303595408757793213981286451081005077114130101133457951582227249802820407016903011597830679808031094060911606519874888196020844361558955599635335257045010062614755515111267775986244493922725255973020330354340380649419924718935693718959879310778250636103417817054187661609076142747012790813043280864817735409842410276005950340121160775700206448447277295111684172139757988356188588207743329594782844076702075775387
flag=pow(m,d,n)
print(long_to_bytes(flag))