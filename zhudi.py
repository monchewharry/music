'''
Zhudi is an ancient Chinese instrument. 
Unlike the common musical instruments which contain 
the whole scale in one piece, Zhudi is not a single individual 
instrument, but a set of instruments.  
When musicians are playing the zhudi, they need first choose the
right zhudi with the right key.
Sometimes choosing the right zhudi may come difficult to some amateur.

So I am trying to help people find the right zhudi by a simple function zhudi().
The only formal variable "keyscore"refers to the key of the score. 
For example,if 1=C, zhudi("C") will return the correct Quananzuo code for every zhudi.
'''

keys="ABCDEFG"
zhifa5= dict(zip("ABCDEFG","EFGABCD"))
#the absolute key of quananzuo=5 for every zhudi

def sign(keyscore):
		a=list(keys)
		loc= a.index(keyscore)#<=6
		b=a[loc:7]
		b.extend(a[0:loc])
		base = dict(zip(b,"1234567"))
		return base
		
def quanzuo(keyscore,keyzhudi):
	keyscore=keyscore.upper()
	keyzhudi=keyzhudi.upper()
	simplesign = sign(keyscore)#the score's sign
	return simplesign[zhifa5[keyzhudi]]

def zhudi(keyscore):
	'''
	if the score is 1=C, zhudi("C") will return the correct Quananzuo code for every zhudi.
	'''
	if not isinstance(keyscore, str):
		return "not a valid character"
	else:
		print "Zhudi","Quananzuo"
		for i in keys:
			print " ",i,"<","-"*4,">",quanzuo(keyscore,i) 


def zhudi2(keyscore):#faster
	if not isinstance(keyscore, str):
		return "not a valid character"
	else:
		base="5671234"
		keyscore=keyscore.upper()
		a=list(keys)
		loc= a.index(keyscore)#<=6
		b=a[loc:7]
		b.extend(a[0:loc])
		for i in range(7):
			print " ",b[i],"<","-"*4,">",base[i]
		


