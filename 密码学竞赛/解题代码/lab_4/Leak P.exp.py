n= 6290400850108673527783456723558868077251853788073859360516042680251422818079380463161520548743184302018140978345372703177688378631564416901363981788817257

import gmpy2
print(gmpy2.iroot(n**(49**2),100**2)[0].bit_length())
print(gmpy2.iroot(n**(48**2),100**2)[0].bit_length())
print(gmpy2.iroot(n**(47**2),100**2)[0].bit_length())
print(gmpy2.iroot(n**(46**2),100**2)[0].bit_length())

