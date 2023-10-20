import gmpy2
import libnum
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
e1=58169
e2=42239
c1= 3692766036283943540313098286304266510361347054708449055542682692062073711536589405245241980174280061301491545039062178654512803574650276066141843678772940052974701
c2= 4373393412365268398260265778309120474718099194920969619404064575346090988834876519040940374935708519313863690656260819783978176441771230081801993603349968832253841
n1= 9759279324467394597831711179718508596171969739950295636856128025950371638938763801180107390878866914987308475151240906371719577893672311903919490118982067214334274
n2= 9362045778153069747981245933168456546468217717807806351786212097034735112184049936432161182243085684425770148036861181126308293616916494342533801458613562708886078

p= 145761754843820286365615274695640462761297014274071268462997502840493581759068851634614
q= 219673873853765612669813661096032565978134844881522541118068777157179360691471
c= 994772772317512037785187803773696380558134918614351250855785624718258501242901981846337801266369414061152226881009458849215835578985342658608537003662606
n=p*q
e = 2
n_list= [p,q]
c_list= [c%p, c%q]

resultant, mod = crt(n_list, c_list)
for i in range(10):
	mm=resultant+p*q*i
	value, is_perfect = gmpy2.iroot(mm, e)
	flag=long_to_bytes(value)
	if b'flag' in flag:
		print(flag)