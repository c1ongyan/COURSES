n = 6290400850108673527783456723558868077251853788073859360516042680251422818079380463161520548743184302018140978345372703177688378631564416901363981788817257
pbits=256
#kbits = 120
PR.<x> = PolynomialRing(Zmod(n))#生成一个以x为符号的一元多项式环
for i in range(2**11):
	p0 = 57303545022436031674172379509633863887077# 已知的p的高位
	p0=p0<<11
	p0=p0+i
	kbits=pbits - p0.nbits()
	p0=p0<<kbits
	#print(p0)
	f = x + p0
	root = f.small_roots(X=2^kbits, beta=0.3) # beta=0.3表明存在factor 大于n ^0.3
	if root:
		p=root[0] + p0
		print('p=',p)
	