from sympy.ntheory.modular import crt  
log = [1, 1, 1016839, 813641, 35993350]
pri = [4,3,1246057,2357351,435374689]
x,mod=crt(pri,log)
print('x=',x)
print('mod=',mod)
from Crypto.Util.number import *
x= 11000838085296873931177
mod= 15346402501700727093876
k= 2064665+1
K = x+mod*k
print(long_to_bytes(K))